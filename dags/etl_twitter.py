from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator

from datetime import datetime, timedelta

from extract import extract_from_twitter
from transform import clean_twitter_data
from load import write_into_database

default_args = {
    'owner': 'me',
    'start_date': datetime(year=2023, month=4, day=4)
}

with DAG('etl_twitter', default_args=default_args, schedule_interval='0 * * * *', catchup=False) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='pg_connection',
        # sql=["""CREATE TABLE IF NOT EXISTS tweets(id SERIAL PRIMARY KEY, datetime DATE NOT NULL, username VARCHAR(200) NOT NULL, text TEXT, source VARCHAR(200), location VARCHAR(200))"""]
        sql='create_table.sql'
    )

    extract_data = PythonOperator(task_id='extract_data', python_callable=extract_from_twitter)

    transform_data = PythonOperator(task_id='transform_data', python_callable=clean_twitter_data)

    load_data = PythonOperator(task_id='load_data', python_callable=write_into_database)

create_table >> extract_data >> transform_data >> load_data

