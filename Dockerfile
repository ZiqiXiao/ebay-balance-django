FROM python:3.11.5-slim-bullseye

WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=${GITHUB_TOKEN}
ENV FASTAPI_BACKEND_HOST=http://nginx_fastapi

RUN apt-get update && apt install git -y
RUN echo "Asia/Shanghai" > /etc/timezone && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# COPY requirements.txt .
# install python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# running migrations
RUN python manage.py migrate

EXPOSE 8080

# gunicorn
CMD gunicorn --config gunicorn-cfg.py core.wsgi
