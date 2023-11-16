FROM python:3.10
RUN apt-get update -y

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["./run.sh"]
