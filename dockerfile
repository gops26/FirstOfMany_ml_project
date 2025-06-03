FROM python:3.8-alpine
WORKDIR /app
COPY . /app
<<<<<<< HEAD
RUN apt update -y
RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "app.py"]
=======
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]
>>>>>>> cf466cf6bcf08e2d6322f9e7ffee22800f07e0fe
