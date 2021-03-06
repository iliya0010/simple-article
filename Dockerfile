FROM python:3.9 as django-build

RUN apt-get update && apt-get install -y gettext

COPY requirements.txt /app/requirements.txt
RUN pip install --no-deps --no-cache-dir -r /app/requirements.txt


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/
COPY . /app/

RUN python manage.py collectstatic --noinput
RUN python manage.py compilemessages

ENV PORT=80
CMD uwsgi --http=0.0.0.0:$PORT --module=simple_articles.wsgi