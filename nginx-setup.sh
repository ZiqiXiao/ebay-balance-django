#!/bin/bash
NGINX_CONFIG_PATH=${NGINX_CONFIG_PATH:-workspaces/ebay-balance-django/nginx/appseed-app.conf}

apt-get update
apt install -y nginx
rm -rf /etc/nginx/nginx.conf
ln -s "$NGINX_CONFIG_PATH" /etc/nginx/nginx.conf
service nginx start