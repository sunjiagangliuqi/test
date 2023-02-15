from airflow.operators.bash_operator import BashOperator
from airflow.operators.http_operator import SimpleHttpOperator
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "liuqi-0215090951",
}

dag = DAG(
    "liuqi-0215090951",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `liuqi.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "http_operator.py"}}

op_2a99e8c3_d361_4b83_81dd_6d9916d61623 = SimpleHttpOperator(
    task_id="去github下载1",
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


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "http_operator.py"}}

op_73e2e8bd_1cbb_45b3_9af7_03d2208a560d = SimpleHttpOperator(
    task_id="去github下载2",
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


# Operator source: {"catalog_type": "local-file-catalog", "component_ref": {"base_dir": "/home/jovyan/work/examples/pipelines/run-pipelines-on-apache-airflow/components", "path": "bash_operator.py"}}

op_e52b89d4_2da6_45be_bf8a_58226944e10c = BashOperator(
    task_id="执行脚本",
    bash_command="{{ ti.xcom_pull(task_ids='去github下载2') }}",
    xcom_push=False,
    env={"name": "World"},
    output_encoding="utf-8",
    executor_config={},
    dag=dag,
)

op_e52b89d4_2da6_45be_bf8a_58226944e10c << op_2a99e8c3_d361_4b83_81dd_6d9916d61623

op_e52b89d4_2da6_45be_bf8a_58226944e10c << op_73e2e8bd_1cbb_45b3_9af7_03d2208a560d
