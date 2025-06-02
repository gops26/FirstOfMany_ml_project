FROM python:3.8-alpine
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awcli -y
CMD ["python3", "app.py"]
