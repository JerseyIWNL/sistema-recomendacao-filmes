from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import duckdb

DB_PATH = "/opt/airflow/data/movies.duckdb"
CSV_PATH = "/opt/airflow/data"

def load_csv_to_duckdb():
    """
    Carrega os CSVs para o DuckDB.
    """
    conn = duckdb.connect(database=DB_PATH, read_only=False)
    conn.execute(f"CREATE OR REPLACE TABLE movies AS SELECT * FROM '{CSV_PATH}/movies.csv';")
    conn.execute(f"CREATE OR REPLACE TABLE ratings AS SELECT * FROM '{CSV_PATH}/ratings.csv';")
    conn.execute(f"CREATE OR REPLACE TABLE genome_scores AS SELECT * FROM '{CSV_PATH}/genome-scores.csv';")
    conn.execute(f"CREATE OR REPLACE TABLE genome_tags AS SELECT * FROM '{CSV_PATH}/genome-tags.csv';")
    conn.execute(f"CREATE OR REPLACE TABLE links AS SELECT * FROM '{CSV_PATH}/links.csv';")
    conn.close()

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

with DAG("etl_movies_pipeline", default_args=default_args, schedule_interval=None) as dag:
    load_task = PythonOperator(
        task_id="load_csv_to_duckdb",
        python_callable=load_csv_to_duckdb,
    )
