from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.operators.empty import EmptyOperator   # ✅ use EmptyOperator instead of DummyOperator
from airflow.utils.dates import days_ago

DATABASE_ID = 'AIRFLOW_DB'
SCHEMA_ID = 'SILVER'

DEFAULT_ARGS = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    dag_id='snowflake_increment_loading_dag',
    default_args=DEFAULT_ARGS,
    schedule_interval='@daily',
    catchup=False,
) as dag:

    start = EmptyOperator(task_id='start')

    increment_load = SnowflakeOperator(
        task_id='increment_load',
        sql=f'CALL {DATABASE_ID}.{SCHEMA_ID}.increment_load();',
        snowflake_conn_id='snowflake_conn',
    )

    end = EmptyOperator(task_id='end')

    start >> increment_load >> end
