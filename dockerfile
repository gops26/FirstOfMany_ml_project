FROM python:3.8-alpine
WORKDIR /app
COPY . /app
USER root
RUN apk update && apk add --no-cache aws-cli
CMD ["python3", "app.py"]
