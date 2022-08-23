FROM python:3.10.2-alpine3.14
RUN apk update && apk upgrade

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY ./ ./

EXPOSE 5000

ENTRYPOINT [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]
