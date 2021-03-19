FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1

RUN pip3 install pipenv
ADD Pipfile Pipfile.lock /app/

# Setup directory structure
WORKDIR /app
COPY ./app/ /app

RUN pipenv install --system --deploy

RUN adduser -D user
USER user