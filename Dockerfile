FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt


ENV PYTHONPATH "${PYTHONPATH}:/app"
