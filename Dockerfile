FROM apache/airflow:3.2.2-python3.12

USER root

RUN apt-get update && \
    apt-get install -y \
    curl \
    git && \
    apt-get clean

USER airflow

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt