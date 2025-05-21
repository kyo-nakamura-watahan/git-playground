# Dockerfile
FROM python:3.13-alpine

WORKDIR /app
COPY . .

RUN pip install --upgrade pip

CMD ["ash"]
