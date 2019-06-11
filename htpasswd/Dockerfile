FROM alpine:3.9

LABEL maintainer=me@ralavay.com

RUN apk add --no-cache apache2-utils

ENTRYPOINT [ "htpasswd", "-nb" ]
