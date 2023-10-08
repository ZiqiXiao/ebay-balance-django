export GITHUB_TOKEN='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'
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver