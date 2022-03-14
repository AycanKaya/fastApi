web: gunicorn gettingstarted.wsgi
web: python manage.py runserver 0.0.0.0:5000
web: uvicorn main:sans --host=0.0.0.0 --port=${PORT:-5000}