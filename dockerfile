FROM python:3.8-alpine
WORKDIR /app
COPY . /app
USER root
RUN /usr/local/aws-cli/v2/current/install --update
CMD ["python3", "app.py"]
