FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install python3-dev gcc

COPY ./scripts/seismic_ws_client/start.sh /start-ws-client
RUN sed -i 's/\r$//g' /start-ws-client
RUN chmod +x /start-ws-client

RUN pip3 install pipenv
ADD Pipfile Pipfile.lock /app/

# Setup directory structure
WORKDIR /app
COPY ./app/ /app

RUN pipenv install --system --deploy