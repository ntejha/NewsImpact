from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'tejha',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='correlate_gold_layer',
    default_args=default_args,
    description='Aggregate sentiment to Gold Layer',
    start_date=datetime(2025, 7, 4),
    schedule_interval='*/5 * * * *',
    catchup=False
) as dag:

    generate_gold = BashOperator(
        task_id='generate_gold_layer',
        bash_command='source ~/Projects/small-projects/NewsImpact/venv/bin/activate && python ~/Projects/small-projects/NewsImpact/scripts/correlate.py'
    )
