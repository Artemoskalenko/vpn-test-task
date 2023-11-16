FROM python:3.10
RUN apt-get update -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .


CMD ["python3.10", "manage.py", "makemigrations"]
# RUN chmod 755 /app/db.sqlite3
CMD ["python3.10", "manage.py", "migrate"]
CMD ["python3.10", "manage.py", "initadmin"]
CMD ["python3.10", "manage.py", "runserver", "0.0.0.0:8000"]

