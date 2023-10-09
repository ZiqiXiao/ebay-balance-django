# gunicorn --config gunicorn-cfg.py core.wsgi
docker build -t ziqix/ebay-balance-django:0.1.0 --no-cache=true .
docker push ziqix/ebay-balance-django:0.1.0