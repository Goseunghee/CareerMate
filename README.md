# CareerMate - AI 진로 추천 서비스

## 1. 서비스 소개

CareerMate는 대학생이 자신의 학과, 학년, 관심 분야와 진로 고민을 입력하면 AI가 개인에게 맞는 진로 방향과 취업 준비 방법을 추천해주는 웹 서비스입니다.

전공을 통해 선택할 수 있는 직무를 알아보고, 필요한 역량과 대학생 때 준비하면 좋은 활동을 확인할 수 있도록 구성했습니다.

---

## 2. 주요 기능

### 🏠 홈

CareerMate 서비스를 소개하고 AI 진로 추천 기능으로 이동할 수 있습니다.

### 🎯 AI 진로 추천

사용자가 다음 정보를 입력하면 Gemini AI가 맞춤형 진로를 분석합니다.

* 학과
* 학년
* 관심 분야
* 희망 진로
* 현재 가장 큰 고민

AI는 다음과 같은 내용을 추천합니다.

* 추천 직무 3개
* 각 직무를 추천하는 이유
* 필요한 핵심 역량
* 대학생 때 해보면 좋은 활동
* 도움이 될 수 있는 자격증 및 학습 분야
* 학년별 취업 준비 방향
* 지금 당장 해볼 수 있는 행동 3가지

### 📚 취업 가이드

대학생의 학년에 따라 준비하면 좋은 내용을 제공합니다.

* 1학년: 진로 및 직무 탐색
* 2학년: 관심 직무 결정 및 경험 쌓기
* 3학년: 프로젝트, 대외활동, 인턴 등 경험 만들기
* 4학년: 자기소개서, 면접 및 취업 준비

### ℹ️ 서비스 소개

CareerMate의 서비스 목적과 주요 특징을 확인할 수 있습니다.

---

## 3. 기술 스택

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Vercel Serverless Functions

### AI

* Google Gemini API

### Deployment

* Vercel

### Version Control

* Git
* GitHub

---

## 4. 프로젝트 구조

```text
CareerMate/
├── api/
│   └── recommend.py
├── css/
│   └── style.css
├── js/
│   └── app.js
├── index.html
├── requirements.txt
├── pyproject.toml
├── vercel.json
└── README.md
```

### 주요 파일 설명

`index.html`

* CareerMate의 전체 웹 페이지 구성
* 홈
* AI 진로 추천
* 취업 가이드
* 서비스 소개

`css/style.css`

* 전체 화면 디자인
* 핑크색 테마
* 반응형 모바일 디자인
* AI 결과 화면 스타일

`js/app.js`

* 사용자 입력 처리
* AI 추천 API 요청
* 로딩 화면 처리
* AI 결과 화면 출력
* 오류 처리

`api/recommend.py`

* Python 백엔드
* 사용자 입력 수신
* Gemini API 호출
* AI 추천 결과 반환

`vercel.json`

* Vercel 배포 및 API 라우팅 설정

---

## 5. AI 기능 동작 과정

CareerMate의 AI 진로 추천 기능은 다음과 같이 동작합니다.

```text
사용자 정보 입력
       ↓
JavaScript에서 입력값 수집
       ↓
/api/recommend 요청
       ↓
Python 백엔드
       ↓
Gemini API 호출
       ↓
AI 진로 분석
       ↓
추천 결과 반환
       ↓
웹 페이지에 결과 표시
```

---

## 6. AI 기능 입력

사용자는 다음 정보를 입력합니다.

* 학과
* 학년
* 관심 분야
* 희망 진로
* 현재 가장 큰 고민

학과, 학년, 관심 분야는 필수 입력 항목입니다.

희망 진로와 현재 고민은 선택적으로 입력할 수 있습니다.

---

## 7. AI 기능 출력

Gemini AI는 사용자의 입력을 바탕으로 다음 내용을 제공합니다.

1. 추천 직무 3개
2. 직무별 추천 이유
3. 필요한 핵심 역량
4. 대학생 때 해보면 좋은 활동
5. 자격증 및 학습 분야
6. 현재 학년을 기준으로 한 취업 준비 방향
7. 지금 당장 해볼 수 있는 행동 3가지

---

## 8. 오류 및 실패 처리

### 필수 입력 누락

학과를 입력하지 않은 경우:

> 학과를 입력해주세요.

학년을 선택하지 않은 경우:

> 학년을 선택해주세요.

관심 분야를 입력하지 않은 경우:

> 관심 분야를 입력해주세요.

### AI API 오류

Gemini API 호출에 실패하는 경우:

> 😥 AI 추천을 불러오지 못했습니다.
> 잠시 후 다시 시도해주세요.

API 키가 설정되지 않은 경우 서버에서 환경변수 설정 오류를 반환합니다.

---

## 9. 환경 변수 설정

Gemini API를 사용하기 위해 다음 환경 변수가 필요합니다.

```text
GEMINI_API_KEY=본인의_Gemini_API_키
```

실제 API 키는 GitHub 저장소에 업로드하지 않습니다.

### Vercel 환경 변수 설정

Vercel 프로젝트의:

**Settings → Environment Variables**

에서 다음과 같이 설정합니다.

```text
Name:
GEMINI_API_KEY

Value:
본인의 Gemini API 키
```

환경 변수는 **Production** 환경에 등록합니다.

---

## 10. 로컬 실행 방법

프로젝트를 GitHub에서 내려받은 후 필요한 Python 패키지를 설치합니다.

```bash
pip install -r requirements.txt
```

Gemini API 키를 환경 변수에 설정한 후 프로젝트를 실행할 수 있습니다.

---

## 11. Vercel 배포 방법

Vercel CLI를 사용하는 경우 프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
vercel.cmd --prod
```

배포가 완료되면 생성된 Production URL을 통해 서비스를 확인할 수 있습니다.

---

## 12. 배포 URL

CareerMate 배포 주소:

https://career-mate-one.vercel.app

---

## 13. 반응형 웹

CareerMate는 데스크톱과 모바일 환경에서 사용할 수 있도록 반응형으로 제작했습니다.

CSS의 미디어 쿼리를 사용하여 화면 크기에 따라 다음 요소가 변경됩니다.

* 네비게이션 메뉴
* Hero 영역
* AI 진로 추천 입력 폼
* 취업 가이드 카드
* 서비스 소개 영역
* AI 결과 화면

---

## 14. 개발 목적

대학생들이 자신의 전공과 관심 분야를 바탕으로 진로를 탐색하고 취업 준비 방향을 쉽게 찾을 수 있도록 하는 것을 목표로 제작했습니다.

특히 진로를 아직 결정하지 못했거나 취업 준비를 어디서부터 시작해야 할지 모르는 대학생이 AI의 도움을 받아 자신의 진로 방향을 탐색할 수 있도록 구성했습니다.

---

## 15. 프로젝트 특징

* 대학생을 대상으로 한 AI 진로 추천 서비스
* Gemini API를 활용한 맞춤형 진로 분석
* HTML/CSS/JavaScript 기반 프론트엔드
* Python 기반 백엔드 API
* Vercel을 통한 웹 서비스 배포
* 모바일 반응형 디자인
* 입력값 검증 및 API 오류 처리
* AI 결과를 읽기 쉽게 표시하는 UI
