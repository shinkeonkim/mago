# 베이스 이미지 설정
FROM python:3.12-slim as base

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG WEB_PORT

# 작업 디렉토리 설정
WORKDIR /app

# pipenv 및 패키지 설치
RUN pip install pipenv

# Pipfile, Pipfile.lock 복사
COPY Pipfile Pipfile.lock ./

# 종속성 설치
RUN pipenv install --system --deploy

# 애플리케이션 소스 복사
COPY . .

# uvicorn 명령어를 이용하여 FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
