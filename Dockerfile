FROM python:3.12.1
USER root
RUN mkdir /www
WORKDIR /www
COPY requirements.txt /www/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1
COPY . /www/

USER 1001

EXPOSE 8080

# CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8080 --timeout 1000 --log-level debug reciclomais.wsgi
# CMD gunicorn --bind 0.0.0.0:8080 --timeout 450 reciclomais.wsgi
# CMD python manage.py migrate && gunicorn --bind 0.0.0.0:8080 --timeout 1000 --log-level debug reciclomais.wsgi

CMD python manage.py runserver 0.0.0.0:8080
