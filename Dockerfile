FROM python:3.11.0-slim as production

ENV PYTHONBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
apt-get install -y \
bash \
build-essential \
gcc \
libffi-dev \
musl-dev \
openssl \
postgresql \
libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt
RUN pip install -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY AI_ICCBS_website ./AI_ICCBS_website

EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .
