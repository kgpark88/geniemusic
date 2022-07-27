# Vision AI 서비스 서버

## 1. 파이썬 가상환경 생성 및 실행
### Windows
- python –m venv venv 
- venv\Scripts\activate.bat
### MacOS/Linux
- python3 -m venv venv
- source venv/bin/activate

## 2. 서버프로그램 소스 다운로드
- git clone https://github.com/kgpark88/rserver

## 3. 파이썬 패키지 설치
- pip install django
- pip install pandas
- pip install matplotlib
- pip install django-crispy-forms
- pip install django-import-export
- pip install django-cors-headers
- pip install djangorestframework
- pip install django-rest-swagger
- pip install drf-yasg
- pip install git+https://github.com/haven-jeon/PyKoSpacing.git
- pip install git+https://github.com/ssut/py-hanspell.git
- pip install tensorflow
- pip install tensorflow_hub

## 4. 테이블 생성
- cd rserver
- python manage.py makemigrations review
- python manage.py migrate 

## 5. 데이터베이스 관리자 계정 생성
- python manage.py createsuperuser

## 6. 백엔드 서버 실행
- python manage.py runserver

## 7. 백엔드 웹서비스 접속
- http://localhost:8000

## 실행화면
![image](https://user-images.githubusercontent.com/17672596/142606611-9a9249d1-816f-45c2-98ef-f99826d3b2ad.png)

![image](https://user-images.githubusercontent.com/17672596/142606630-c1f561ed-2de1-4ce9-bc2b-90472e786459.png)

![image](https://user-images.githubusercontent.com/17672596/142606643-1def09c4-03d6-46b0-a921-9e7a4ba38b7d.png)




