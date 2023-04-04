import pandas as pd
from airflow.hooks.postgres_hook import PostgresHook

def write_into_database():
    df = pd.read_csv('tweets.csv')
    data = df.to_csv(index=None, header=None)
    postgres_sql_upload = PostgresHook(postgres_conn_id='pg_connection')
    postgres_sql_upload.bulk_load('tweets', data)

