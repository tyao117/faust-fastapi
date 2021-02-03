
FROM python:3.8-slim-buster

WORKDIR /opt/microservices
COPY requirements.txt /opt/microservices/

RUN pip install -r /opt/microservices/requirements.txt

COPY main.py /opt/microservices/

EXPOSE 8000

ARG service_version
ENV SERVICE_VERSION ${service_version:-v1}

WORKDIR /opt/microservices

# working version
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
