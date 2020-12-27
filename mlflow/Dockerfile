FROM python:3.8.6-alpine

RUN apk add gcc g++ make libffi-dev openssl-dev
RUN pip3 install mlflow

CMD ["mlflow", "ui", "-h", "0.0.0.0"]