# 자기소개서 평가 시스템 🤖

지원자의 자기소개서를 분석하고 기업 요구사항에 맞는 평가를 수행하는 AI 기반 시스템

## 주요 기능 ✨
- **적합도 평가**: 질문-답변 간 적합도 수치화
- **핵심가치 매칭**: 기업 핵심가치 별 점수 부여
- **역직무 예측**: 포지션 기대 역할 생성
- **면접 준비**: 상황별 면접 질문 자동 생성

## 기술 스택 🛠
- **백엔드**: 파이썬 3.9+
- **AI 프레임워크**: OpenAI GPT-4o
- **웹 인터페이스**: 스트림릿
- **구성**: Pydantic, python-dotenv

## 시스템 아키텍처 🏗
프로젝트/
├── app.py # 메인 애플리케이션
├-- config.py # 설정 관리
├── .env # 환경 변수
└-- 모듈/
├-- 프롬프트_handler.py # 프롬프트 템플릿 관리
├-- chatgpt_integration.파이 # 열기AI API 통신
└-- 평가_processor.py # 평가 로직 처리

알았다.

## 설치 가이드 📥
1. 저장소 복제
'''bash'''
git 클론 https://github.com/your-repo/self-introduction-evaluator.git
CD 자기소개-evalu 작성자
가상 환경 설정

바시
알았다.
파이썬 - m venv venv
소스 venv/bin/activate # Linux/Mac
venv\\Scripts\\activate # Windows
의존성 설치

바시
알았다.
pip 설치 -r 요구 사항.txt
환경 변수 설정 (.env 파일 생성)

부러움
알았다.
OPENAI_API_KEY=your_openai_api_key_here
실행 방법 🚀
바시
알았다.
streamlit 실행 app.py
사용 방법 📖
웹 브라우저에서 http://localhost:8501 접속

입력창에 평가 요청 문구 작성 (예: "이력서의 핵심가치 적합도 평가해 주세요")

시스템이 자동으로 분석 수행 후 결과 표시

주요 모듈 설명 📦
프롬프트 관리자
4가지 유형의 프롬프트 템플릿 관리

ID 기반 프롬프트 검색 기능

ChatGPTClient
OpenAI API 통신 처리

예외 처리 메커니즘 내장

응답 포맷 유효성 검증

평가 프로세서
자연어 질의 → 프롬프트 매핑

다단계 평가 파이프라인 처리

결과 통합 및 포맷팅

기여 가이드 🤝
이슈 생성 후 작업 브랜치 생성

코드 컨벤션 준수 (PEP8)

단위 테스트 작성 후 PR 요청

코드 리뷰 진행
