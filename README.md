# SSAFY Django Self-Study

## ⚠️ TIL 접근 제한 안내
- TIL에 공부하면서 정리한 Notebook의 내용을 바탕으로 실제 코드 작성 연습을 진행했습니다.
- [TIL 장고 실습 코드](https://github.com/mins-git/TIL/tree/master/WEB/Django/Notebook)는 현재 private 저장소로 설정되어 있어 토큰 없이 접근이 불가능합니다.

## 💫 상세 학습 내용
- 프로젝트의 상세 학습 내용은 [회원제 커뮤니티 게시판 구현 README](https://github.com/mins-git/ssafy-django-selfstudy/blob/master/day7-%20%ED%9A%8C%EC%9B%90%EC%A0%9C%20%EC%BB%A4%EB%AE%A4%EB%8B%88%ED%8B%B0%20%EA%B2%8C%EC%8B%9C%ED%8C%90%20%EA%B5%AC%ED%98%84/README.md)에서 확인할 수 있습니다.
- 오늘의 PJT를 통해 배운 내용과 구현 과정이 자세히 정리되어 있습니다



## 📌 프로젝트 소개
이 레포지토리는 회원제 커뮤니티 게시판 구현을 목표로 하는 Django 자기주도 학습 과정을 담고 있습니다. 
Django의 기본 개념부터 DRF(Django Rest Framework)까지 단계별로 학습하며 실전 프로젝트를 완성해나가는 과정을 기록했습니다.

## 🎯 학습 목표
- Django 프레임워크의 핵심 개념 이해 및 실전 적용
- RESTful API 설계 및 구현 능력 향상
- 회원제 커뮤니티 게시판 구현을 통한 실무 역량 강화

## 📚 학습 내용

### Day 1: ORM (Object-Relational Mapping)
- Django ORM의 기본 개념 이해
- 모델 정의 및 데이터베이스 조작
- QuerySet API 활용

### Day 2: ModelForm & HTTP
- ModelForm을 활용한 폼 처리
- HTTP 메소드 이해 및 적용
- CRUD 기능 구현

### Day 3: Static & Media 파일 관리
- 정적 파일 처리 방법
- 미디어 파일 업로드 구현
- 파일 시스템 설정

### Day 4: 인증 & 계정 관리
- Django 인증 시스템 활용
- 회원가입/로그인 기능 구현
- 사용자 권한 관리

### Day 5: Django Rest Framework (DRF) 기초
- REST API 개념 이해
- DRF 기본 구조 학습
- API View 구현 (GET, POST, PUT, DELETE)

### Day 6: DRF 심화 - 도서관리 API
- Serializer 심화 학습
- ViewSet 활용
- 도서관리 시스템 API 구현

### Day 7: 회원제 커뮤니티 게시판 구현
- 앞서 배운 내용을 종합한 실전 프로젝트
- 회원 관리 시스템 구축
- 게시판 CRUD 기능 구현

## 💡 주요 배운 점
1. **Django 프레임워크의 특징**
   - MVT 패턴의 이해와 활용
   - ORM을 통한 효율적인 데이터베이스 관리
   - Django의 보안 기능 활용

2. **API 개발 역량**
   - RESTful API 설계 원칙 적용
   - DRF를 활용한 효율적인 API 개발
   - API 문서화 및 테스트 방법

3. **실무 적용 가능한 기술**
   - 사용자 인증 및 권한 관리
   - 파일 업로드 처리
   - 커뮤니티 기능 구현

## 🛠 사용 기술
- Django
- Django Rest Framework
- SQLite
- Python
- HTML

## 📝 프로젝트 실행 방법
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치
pip install -r requirements.txt

# 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 서버 실행
python manage.py runserver