FROM python:3.8-alpine
WORKDIR /app
COPY . /app
USER root
RUN apk update && apk add aws-cli --update
CMD ["python3", "app.py"]
