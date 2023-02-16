from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "count-0216014644",
}

dag = DAG(
    "count-0216014644",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/test/component", "path": "add.py"}}

op_298b81e6_d87d_4ce3_8146_def7a12e059c = BashOperator(
    task_id="TestOperator", a="15", b="2", executor_config={}, dag=dag
)
