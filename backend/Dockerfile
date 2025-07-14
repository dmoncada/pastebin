FROM python:3.11-slim

ENV DOCKERIZE_VERSION v0.9.3

RUN apt-get update \
    && apt-get install -y wget \
    && wget -O - https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz | tar xzf - -C /usr/local/bin \
    && apt-get autoremove -yqq --purge wget && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["dockerize", "-wait", "tcp://db:5432", "-wait", "tcp://redis:6379", "-timeout", "30s", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

