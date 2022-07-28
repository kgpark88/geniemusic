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

## 3.JAVA 설치
- https://github.com/ojdkbuild/ojdkbuild
- 설치참조 : https://velog.io/@nsunny0908/JAVA-OpenJDK-1.8-%EC%84%A4%EC%B9%98

## 4. 파이썬 가상환경 생성 및 실행
- cd review_analysis  
- python –m venv venv   
#### Windows
- venv\Scripts\activate     
#### Linux, macOS
- source venv/bin/activate

## 5. 파이썬 패키지 설치
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

#### pip SSL 오류가 날때 파이썬 패키지 설치방법
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install django
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install pandas
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install matplotlib
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install seaborn
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install django-crispy-forms
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install django-import-export
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install django-cors-headers
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install djangorestframework
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install django-rest-swagger
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install drf-yasg
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install django-markdownx
- pip install JPype1-1.4.0-cp38-cp38-win_amd64.whl
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install sklearn
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install konlpy
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install git+https://github.com/haven-jeon/PyKoSpacing.git
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install git+https://github.com/ssut/py-hanspell.git
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install tensorflow
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install tensorflow_hub
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install jupyter
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install google_play_scraper
- pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org install app-store-scraper

## 6. 테이블 생성
- cd server
- python manage.py makemigrations review
- python manage.py migrate

## 7. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 8. 백엔드 실행
- python manage.py runserver

## 9. Javascript 패키지 설치 : review_analysis/frontend/ 디렉토리에서 실행
- npm install

## 10. 프론트엔드 실행
- npm run serve
