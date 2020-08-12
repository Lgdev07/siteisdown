FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /siteisdown

COPY requirements.txt /siteisdown

RUN apk add --no-cache gcc && apk add linux-headers && apk add libc-dev
RUN pip install -r requirements.txt

COPY . /siteisdown

RUN pip install --editable .