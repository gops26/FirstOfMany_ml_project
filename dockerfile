FROM python:3.8-alpine
WORKDIR /app
COPY . /app
RUN apt update -y
RUN apt-get update && pip install -r requirements.txt
