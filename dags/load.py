import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

def write_into_database():
    df = pd.read_csv('tweets.csv')
    data = df.to_csv(index=None, header=None)
    PostgresHook(postgres_conn_id='pg_connection').bulk_load('tweets', 'tweets.csv')
    return True
