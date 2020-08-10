FROM python:3.8.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /siteisdown

COPY requirements.txt /siteisdown

RUN pip install -r requirements.txt

COPY . /siteisdown

CMD ["python", "main.py"]