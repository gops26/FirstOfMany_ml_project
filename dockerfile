FROM python:3.8-alpine
WORKDIR /app
COPY . /app
USER root
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]