FROM python:3.11.5-slim-bullseye

WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV GITHUB_TOKEN=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

RUN apt-get update && apt install git -y

# COPY requirements.txt .
# install python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x nginx-setup.sh
RUN NGINX_CONFIG_PATH='/app/nginx/appseed-app.conf' /app/nginx-setup.sh

# running migrations
RUN python manage.py migrate

EXPOSE 8080

# gunicorn
CMD gunicorn --config gunicorn-cfg.py core.wsgi
