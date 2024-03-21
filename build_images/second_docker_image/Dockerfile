FROM alpine:3.17.0

RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache-dir fastapi==0.110.0 uvicorn==0.29.0 redis==4.3.5

EXPOSE 8000

COPY ./src /app

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0"]