FROM python:3.8.2-alpine3.11
RUN apk --update add gcc postgresql-dev postgresql-client musl-dev
ENV APP_DIR /app
ADD ./docker /docker
ADD ./app/requirements.txt ${APP_DIR}/requirements.txt
RUN pip install -r ${APP_DIR}/requirements.txt
WORKDIR ${APP_DIR}
