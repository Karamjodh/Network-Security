FROM python:3.10-slim-buster
WORKDIR /App
COPY . /App

RUN apt update -y && apt install awscli -y

RUN apt-get update && pip install -r requirements.txt
CMD ["python3", "App.py"]