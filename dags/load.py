import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

def write_into_database():
    PostgresHook(postgres_conn_id='pg_connection').bulk_load('tweets', 'tweets.csv')
