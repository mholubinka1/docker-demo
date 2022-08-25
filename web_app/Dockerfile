FROM python:3.9.6-alpine3.14
RUN apk update && apk upgrade
RUN pip3 install --upgrade pip

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./ ./

ENTRYPOINT [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]