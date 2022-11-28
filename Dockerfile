FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 8000

CMD gunicorn -b 0.0.0.0:8000 delivery_crazy_project.wsgi
