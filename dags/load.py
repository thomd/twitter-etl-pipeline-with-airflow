import pandas as pd
from airflow.hooks.postgres_hook import PostgresHook

def write_into_database():
    pass
    # data = pd.read_csv('tweets.csv')
    # postgres_sql_upload = PostgresHook(postgres_conn_id='pg_connection')
    # postgres_sql_upload.bulk_load('tweets', data)

