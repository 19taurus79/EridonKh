FROM python:3.12-slim

WORKDIR /usr/usr/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.dev.txt .
RUN pip install -r requirements.dev.txt

# copy project
COPY . .