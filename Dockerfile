FROM python:3.8-slim-buster

RUN pip install --upgrade pip
RUN apt-get update -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]