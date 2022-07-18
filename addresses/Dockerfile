FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN pip install pipenv
RUN apt-get update && apt-get -y install libpq-dev gcc

COPY . /code/

RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
