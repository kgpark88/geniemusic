import os
import re
import csv
import json
import pickle
import requests
import pandas as pd
from shutil import move
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from konlpy.tag import Okt
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression

from django.db.models import Q
from django.db.models import Avg
from django.db.models import Count
from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from review.models import Review

media_root = getattr(settings, "MEDIA_ROOT", 'media')

df = pd.read_csv("geniemusic_review.csv", encoding="utf-8")
df = df.dropna(axis=0)
stopwords = pd.read_csv("korean_stopwords.txt").values.tolist()
# load the model from disk
review_model = pickle.load(open('review_model.sav', 'rb'))
okt = Okt()

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def list(request):
    search_word = request.data.get('search_word', None)
    from_dt = request.data.get('from_dt')
    to_dt = request.data.get('to_dt')
    qs = Review.objects.filter(at__gte=from_dt, at__lte=to_dt,).order_by('-at')

    reviews = [] 
    for q in qs:           
        data = {
            'content': q.content or '',
            'score': q.score or '',
            'at': q.at or '',
            'source': q.source or '',
        }
        reviews.append(data)
    return JsonResponse({'count': qs.count(), 'reviews': reviews})


# 한글 텍스트 추출 함수 : 띄어 쓰기(1 개)를 포함한 한글만 추출
def hangul(text):
    p = re.compile('[^ ㄱ-ㅣ 가-힣]')  
    result = p.sub('', text)  
    return result

def text_cleaning(text):
    p = re.compile('[^ ㄱ-ㅣ 가-힣]')
    result = p.sub('', text)
    nouns = okt.nouns(result) 
    nouns = [x for x in nouns if len(x) > 1]  # 한글자 명사 제거
    nouns = [x for x in nouns if x not in stopwords]  # 불용어 제거
    return nouns

def rating_to_label(rating):
    if rating > 4:
        return 1
    else:
        return 0

@api_view(['POST'])
def data_upload(request):
    info = 'info'
    title = ''
    text = ''
    error_message = ''
    file_path = ''
    if request.FILES:
        file = request.FILES['file']
        if file.name.lower().endswith('.csv'):
            fs = FileSystemStorage()
            fname = fs.save(file.name, file)
            upload_fname = os.path.join(media_root, file.name)
            move(os.path.join(media_root, fname), upload_fname)
            file_path = 'media/' + os.path.basename(upload_fname)

            Review.objects.all().delete()
            
            with open(file_path, 'r', encoding='UTF-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    try:
                        w_date = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
                        review = Review(content=row[0], score=row[1], at=w_date, source=row[3])
                        ret = review.save()
                        print(f'INSERT REVIEW DATA : {row[2]}')
                    except Exception as ex:
                        print(ex)
            qs = Review.objects.all()

            info = 'success'
            result = f'리뷰 데이터 저장 : {qs.count()}건'
        else:
            result = '업로드가 허용되지 않는 파일타입니다.'

    return JsonResponse({'info': info, 'result' : result})



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_rating(request):
    rating_avg = 0
    rating = [0, 0, 0, 0, 0]
    total = 0
    positive = 0
    negative = 0

    from_dt = request.data.get('from_dt')
    to_dt = request.data.get('to_dt')

    qs = Review.objects.filter(at__gte=from_dt, at__lte=to_dt)
    total = qs.count()

    qs = Review.objects.filter(at__gte=from_dt, at__lte=to_dt).aggregate(Avg('score'))
    rating_avg = qs['score__avg'] or 0

    for i in range(5):
        qs = Review.objects.filter(at__gte=from_dt, at__lte=to_dt, score__gte=i, score__lt=i+1)
        rating[i] = qs.count()

    qs = Review.objects.filter(at__gte=from_dt, at__lte=to_dt, score__gte=4)
    positive = qs.count()
    negative = total - positive

    res = {
        'rating_avg': rating_avg, 
        'rating': rating,
        'total': f'총 {total}건',
        'positive': positive,
        'negative': negative
    }

    return JsonResponse(res)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def review_analysis(request):
    from_dt = request.data.get('from_dt')
    to_dt = request.data.get('to_dt')

    positive_word = []
    negative_word = []
    review = Review.objects.filter(at__gte=from_dt, at__lte=to_dt).values_list("content", flat=True)
    corpus = " ".join(review)
    nouns = okt.nouns(hangul(corpus))
    df['y'] = df['score'].apply(lambda x: rating_to_label(x))

    # corpus = " ".join(df['content'].tolist())
    # nouns = okt.nouns(hangul(corpus))
    # counter = Counter(nouns)
    # counter = Counter({x: counter[x] for x in counter if len(x) > 1})

    # BoW(Bag of Word) 벡터 생성
    vect = CountVectorizer(tokenizer = lambda x: text_cleaning(x))
    bow_vect = vect.fit_transform(df['content'].tolist())
    word_list = vect.get_feature_names()
    count_list = bow_vect.toarray().sum(axis=0)
    word_count_dict = dict(zip(word_list, count_list))
    print(f'bow_vect.shape : {bow_vect.shape}')

    # Bag of Words 벡터에 대해서 TF-IDF변환 진행
    tfidf_vectorizer = TfidfTransformer()
    tf_idf_vect = tfidf_vectorizer.fit_transform(bow_vect)
    invert_index_vectorizer = {v: k for k, v in vect.vocabulary_.items()}
    print(f'tf_idf_vect.shape : {tf_idf_vect.shape}')
    print(f'tf_idf_vect[0].toarray().shape : {tf_idf_vect[0].toarray().shape}')

    y_pred = review_model.predict(tf_idf_vect)
    # print(f'y_pred : {y_pred}')

    coef_pos_index = sorted(((value, index) for index, value in enumerate(review_model.coef_[0])), reverse = True)
    coef_neg_index = sorted(((value, index) for index, value in enumerate(review_model.coef_[0])), reverse = False)

    invert_index_vectorizer = {v: k for k, v in vect.vocabulary_.items()}
    coef_pos_index = sorted(((value, index) for index, value in enumerate(review_model.coef_[0])), reverse = True)
    coef_neg_index = sorted(((value, index) for index, value in enumerate(review_model.coef_[0])), reverse = False)
    invert_index_vectorizer = {v: k for k, v in vect.vocabulary_.items()}
    for coef in coef_pos_index[:50]:
        for n in nouns:
            if n == invert_index_vectorizer[coef[1]]:
                if n not in positive_word:
                    positive_word.append(n)
                    # print(invert_index_vectorizer[coef[1]], coef[0])
    for coef in coef_neg_index[:50]:
         for n in nouns:
            if n == invert_index_vectorizer[coef[1]]:
                if n not in negative_word:
                    negative_word.append(n)
                    # negative_word.append(invert_index_vectorizer[coef[1]])
                    # print(invert_index_vectorizer[coef[1]], coef[0])

    return JsonResponse({'positive_word': positive_word, 'negative_word': negative_word})