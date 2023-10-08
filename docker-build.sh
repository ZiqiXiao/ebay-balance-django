# gunicorn --config gunicorn-cfg.py core.wsgi
docker build -t ziqix/ebay-balance-django:0.1.0 .
docker push ziqix/ebay-balance-django:0.1.0