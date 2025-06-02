FROM python:3.8-alpine
WORKDIR /app
COPY . /app
USER root
RUN apt update && apt install -y awscli
CMD ["python3", "app.py"]
