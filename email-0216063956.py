from airflow.operators.email_operator import EmailOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "email-0216063956",
}

dag = DAG(
    "email-0216063956",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `email.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/airflow_component_examples/email_operator", "path": "test.py"}}

op_aac2ca23_bd76_4c1f_bcfc_50fb89a9e7ff = EmailOperator(
    task_id="EmailOperator",
    to="[sxdtlq0123@163.com]",
    subject="\u6d4b\u8bd5\u90ae\u4ef6",
    html_content="\u6d4b\u8bd5",
    files=[],
    cc=[],
    bcc=[],
    mime_subtype="mixed",
    mime_charset="us_ascii",
    executor_config={},
    dag=dag,
)
