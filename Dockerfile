FROM python:3.7-alpine

WORKDIR /app

RUN apk add --update bash postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev wkhtmltopdf
#apk add --virtual .build-deps postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

COPY requirements.txt /app

RUN pip3 install -r requirements.txt
#RUN apk del .build-deps

COPY . /app

EXPOSE 8080

CMD ["/app/start.sh"]