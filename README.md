# Twitter ETL Pipeline with Apache Airflow

This is an **educational project**.

[Apache Airflow](https://airflow.apache.org/) is a platform to programmatically author, schedule and monitor workflows using Python.

## Twitter ETL Pipeline

The pipeline

1. **extracts** data from Twitter (date, user, content, source, location of all `#ChatGPT` tweets since `2023-01-01`),
1. **transforms** it (remove all non-ascii charaters) and
1. **loads** it into a Postgres Database.

```
airflow dags show etl_twitter | sed 1d | graph-easy --as=boxart

                                     etl_twitter
    
    ╭──────────────╮     ╭──────────────╮     ╭────────────────╮     ╭───────────╮
    │ create_table │ ──▶ │ extract_data │ ──▶ │ transform_data │ ──▶ │ load_data │
    ╰──────────────╯     ╰──────────────╯     ╰────────────────╯     ╰───────────╯
```

## Setup

### Postgresql

    brew install postgresql@14
    brew services run postgresql@14
    createdb -h localhost -p 5432 -U <USER> twitter

### Apache Airflow

    git clone https://github.com/thomd/twitter-etl-pipeline-with-airflow.git
    cd twitter-etl-pipeline-with-airflow
    pyenv shell 3.10.9
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip

    export AIRFLOW_HOME=$(pwd)
    URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.5.3/constraints-3.10.txt"
    pip install "apache-airflow==2.5.3" --constraint "${URL}"
    pip install psycopg2-binary apache-airflow-providers-postgres

    export SQLALCHEMY_SILENCE_UBER_WARNING=1
    export AIRFLOW__CORE__LOAD_EXAMPLES=False
    airflow db init

## Run ETL Pipeline

    pip install snscrape pandas
    airflow connections add --conn-type postgres --conn-host localhost --conn-schema twitter --conn-login <USER> pg_connection
    airflow scheduler -D

### Run via Airflow CLI

    airflow dags list
    airflow dags unpause etl_twitter
    airflow dags trigger etl_twitter
    airflow dags list-runs -d etl_twitter

### Run via Airflow Web-UI

    airflow users create -u airflow -p airflow -r Admin -f John -l Doe -e john.doe@airflow.apache.org
    airflow webserver -p 8080 -D

