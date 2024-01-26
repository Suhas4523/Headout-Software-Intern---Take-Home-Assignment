FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask

EXPOSE 8080

ENV DATA_DIR="/app/data"

CMD ["python", "http_server.py"]