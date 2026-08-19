# ⚙️ 시스템 (Backend + Frontend)

Django REST Framework 백엔드와 React 프론트엔드로 구성된 실행 가능한 소스코드가 위치하는 폴더입니다.

## 📂 폴더 구조

```
시스템/
├── backend/                  # Django REST Framework
│   ├── config/                 # 프로젝트 전역 설정
│   ├── accounts/                # 유저·부서·직군·직급·인증
│   ├── onboarding/              # 온보딩 트랙·스텝
│   ├── documents/               # 문서 업로드/열람
│   └── schedule/                 # 개인/공유 캘린더
└── frontend/                 # React + TypeScript + Vite
    └── src/
        ├── api/                  # 백엔드 API 호출 함수 (도메인별 분리)
        ├── pages/                # 라우트별 화면
        └── components/           # 재사용 컴포넌트
```

## 🖥 개발 환경

| 항목 | 버전/도구 |
|---|---|
| Python | 3.11 (conda 가상환경: `onboarding_env`) |
| Node.js | 18 이상 |
| DB | MySQL |

## 🚀 설치 및 실행

### Backend

```bash
conda create -n onboarding_env python=3.11
conda activate onboarding_env

cd backend
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 🔑 환경변수 (.env)

`backend/` 루트에 `.env` 파일을 만들고 아래 항목을 채워주세요.

| 변수명 | 설명 |
|---|---|
| `DB_NAME` | MySQL 데이터베이스명 |
| `DB_USER` | MySQL 사용자명 |
| `DB_PASSWORD` | MySQL 비밀번호 |
| `DB_HOST` | MySQL 호스트 |
| `DB_PORT` | MySQL 포트 |
| `AWS_ACCESS_KEY_ID` | S3 접근 키 |
| `AWS_SECRET_ACCESS_KEY` | S3 시크릿 키 |
| `AWS_STORAGE_BUCKET_NAME` | S3 버킷명 |

## 📡 API 개요

| 경로 | 담당 앱 | 설명 |
|---|---|---|
| `/api/accounts/` | accounts | 로그인/로그아웃, 부서·직군·직급·직원 관리 |
| `/api/onboarding/` | onboarding | 온보딩 트랙/스텝 조회 및 관리 |
| `/api/documents/` | documents | 문서 업로드/다운로드 |
| `/api/schedule/` | schedule | 개인/공유 일정 관리 |
| `/admin/` | - | Django 관리자 페이지 |