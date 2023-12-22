FROM debian:alpine

RUN apt update -y && apt upgrade -y && apt install python3-venv && 

ENV ORACLE_HOME = /opt/instantclient_12/bin

WORKDIR /app

COPY requeriments.txt app/

RUN pip install -r requeriments.txt
