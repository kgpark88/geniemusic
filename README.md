# 리뷰 데이터 분석 서비스 개발  
### 추천도서  
o 파이썬 텍스트 마이닝 완벽 가이드   
- https://wikibook.co.kr/textmining/  
- GitHub 저장소: https://github.com/wikibook/textmining   
- ZIP 형식으로 다운로드: https://github.com/wikibook/textmining/archive/refs/heads/main.zip  

# 설치 방법
# 1. Git 프로그램 설치 
- https://git-scm.com/downloads  

## 2. 소스 설치
git clone https://github.com/kgpark88/review_analysis 
 
## 3. 파이썬 가상환경 생성 및 실행
- cd review_analysis  
- python –m venv venv 
- venv\Scripts\activate  (windows)      source venv/bin/activate  (Linux, macOS) 

## 4. 파이썬 패키지 설치
- pip install django
- pip install pandas
- pip install matplotlib
- pip install seaborn
- pip install django-crispy-forms
- pip install django-import-export
- pip install django-cors-headers
- pip install djangorestframework
- pip install django-rest-swagger
- pip install drf-yasg
- pip install django-markdownx
- pip install JPype1-1.4.0-cp38-cp38-win_amd64.whl
- pip install sklearn
- pip install konlpy
- pip install git+https://github.com/haven-jeon/PyKoSpacing.git
- pip install git+https://github.com/ssut/py-hanspell.git
- pip install tensorflow
- pip install tensorflow_hub
- pip install jupyter
- pip install google_play_scraper
- pip install app-store-scraper

## 5. 테이블 생성
- cd server
- python manage.py makemigrations review
- python manage.py migrate

## 6. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 7. 백엔드 실행
- python manage.py runserver

## 8. Javascript 패키지 설치 
- npm install

## 9. 프론트엔드 실행
- npm run serve
