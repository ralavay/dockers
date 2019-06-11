FROM alpine:3.9

LABEL maintainer="me@ralavay.com"

RUN apk add --no-cache \
        python3 \
        libzmq \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        python3-dev \
        linux-headers \
    && pip3 install --upgrade pip \
    && pip3 install locust \
    && apk del .build-deps
