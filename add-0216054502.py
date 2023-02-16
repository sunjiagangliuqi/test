from airflow.operators.bash_operator import BashOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "add-0216054502",
}

dag = DAG(
    "add-0216054502",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `test.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/test/component", "path": "add.py"}}

op_0ad6234a_b1a1_461e_8883_2f084ea38948 = BashOperator(
    task_id="BashOperator",
    bash_command="cd /home",
    a="12",
    b="15",
    executor_config={},
    dag=dag,
)
