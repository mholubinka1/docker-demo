FROM python:3.10.2-alpine3.14
RUN apk update && apk upgrade

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./ ./
COPY ./uwsgi.ini /etc/uwsgi.ini

EXPOSE 80

ENTRYPOINT [ "sh", "./start.sh"]
