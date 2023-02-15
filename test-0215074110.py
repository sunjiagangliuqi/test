from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test-0215074110",
}

dag = DAG(
    "test-0215074110",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/test/component", "path": "load_data.py"}}

op_2b9d6766_20f3_4989_8941_241dbef7ac63 = SimpleHttpOperator(
    task_id="SimpleHttpOperator",
    url="https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz",
    executor_config={},
    dag=dag,
)
