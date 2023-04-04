# Twitter ETL Pipeline with Apache Airflow

This is an **educational project**.

[Apache Airflow](https://airflow.apache.org/) is a platform to programmatically author, schedule and monitor workflows using Python.

With Apache Airflow, a workflow is represented as a **DAG** (Directed Acyclic Graph)

The ETL pipeline **extracts** data from Twitter (date, user, content, source, location of all tweets with hashtag `ChatGPT` since 2023-01-01),  **transforms** it (remove all non-ascii charaters) and **loads** it into a Postgres Database.


    airflow dags show etl_twitter | sed 1d | graph-easy --as=boxart

                                     etl_twitter
    
    ╭──────────────╮     ╭──────────────╮     ╭────────────────╮     ╭───────────╮
    │ create_table │ ──▶ │ extract_data │ ──▶ │ transform_data │ ──▶ │ load_data │
    ╰──────────────╯     ╰──────────────╯     ╰────────────────╯     ╰───────────╯

## Setup Postgresql

    brew install postgresql@14
    brew services run postgresql@14
    createdb -h localhost -p 5432 -U <USER> twitter

## Setup Apache Airflow

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

    airflow scheduler -D
    airflow connections add --conn-type postgres --conn-host localhost --conn-schema twitter --conn-login <USER> pg_connection

    airflow dags list
    airflow dags test etl_twitter
