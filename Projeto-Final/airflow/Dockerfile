FROM apache/airflow:2.6.2
USER root
RUN mkdir -p /opt/airflow/dags /opt/airflow/data
RUN chown -R airflow: /opt/airflow
USER airflow
COPY dags/ /opt/airflow/dags
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
