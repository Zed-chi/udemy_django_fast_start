FROM python:3.7-alpine
MAINTAINER Zed-chi
ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers musl-dev zlib zlib-dev
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
RUN mkdir /app
WORKDIR /app
COPY ./pizzashopproject /app
RUN adduser -D user
USER user