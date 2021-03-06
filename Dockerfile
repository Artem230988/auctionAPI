FROM python:3.8

ENV PYTHONBUFFERED=1

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000