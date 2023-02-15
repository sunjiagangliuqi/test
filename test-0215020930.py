from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "test-0215020930",
}

dag = DAG(
    "test-0215020930",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "url-catalog", "component_ref": {"url": "https://raw.githubusercontent.com/elyra-ai/examples/main/pipelines/run-pipelines-on-apache-airflow/components/http_operator.py"}}

op_6662cdfb_d2b8_4a7e_93c9_4b3b2e199060 = SimpleHttpOperator(
    task_id="SimpleHttpOperator",
    endpoint="/repos/elyra-ai/examples/contents/pipelines/run-pipelines-on-apache-airflow/resources/command.txt",
    method="GET",
    data={"ref": "master"},
    headers={"Accept": "Accept:application/vnd.github.v3.raw"},
    response_check="",
    extra_options={},
    xcom_push=True,
    http_conn_id="http_github",
    log_response=False,
    executor_config={},
    dag=dag,
)
