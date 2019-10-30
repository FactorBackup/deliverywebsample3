# 음식배달 웹 서비스_프로젝트

### H shell A neo C pmank K Shell.bat

#### 가상환경 설정
$ pip install virtualenv <br>
$ python -m virtualenv venv <br>
$ source venv/bin/activate <br>
=== 가상환경 설정

requirements.txt에 버전 관리<br>
pip install -r requirements.txt 로 설치 가능<br>
django 2.2<br>
python 3.6<br>
가상환경 venv<br>

#### 구성
* Projectname : config
* Appname : shop
* models.py
  * Category - 메뉴
  * Shop - 가게
  * Item - 음식
  * Review - 리뷰

### Database
* AWS Postgresql

### 배포
* AWS ELB(Elastic Load Balancing)

### MVP
* 가게 / 음식 리스트 나열
* 메뉴 갯수 추가(javascript)
* 가게 위치 네이버 map 위치 정보 구현
* 로그인 구현
* 댓글 추가/삭제/수정 구현

#### (크롤링)
* 가게 및 음식 메뉴 정보 받아오기

### 추가 사항
- 결제연동 - iamport-rest-client 사용
- AWS S3 - static / media 관리
- 소셜 로그인 구현
- ACM 으로 SSL 적용 (https)
