from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "eu_data-0216060218",
}

dag = DAG(
    "eu_data-0216060218",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.14.2 pipeline editor using `eu_data.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: covid-notebooks/notebooks/etl_eu_data.ipynb

op_da4f63d6_5165_4625_8383_4c50b2e0a57f = KubernetesPodOperator(
    name="etl_eu_data",
    namespace="airflow",
    image="codait/covid-notebooks-anaconda-py3:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eu_data' --cos-endpoint http://192.168.1.130:32090 --cos-bucket liuqi --cos-directory 'eu_data-0216060218' --cos-dependencies-archive 'etl_eu_data-da4f63d6-5165-4625-8383-4c50b2e0a57f.tar.gz' --file 'covid-notebooks/notebooks/etl_eu_data.ipynb' --outputs 'cases.csv' "
    ],
    task_id="etl_eu_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eu_data-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)


# Operator source: covid-notebooks/notebooks/features_eu_data.ipynb

op_d573f57d_e573_4b27_9eaf_3846a5541116 = KubernetesPodOperator(
    name="features_eu_data",
    namespace="airflow",
    image="codait/covid-notebooks-anaconda-py3:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eu_data' --cos-endpoint http://192.168.1.130:32090 --cos-bucket liuqi --cos-directory 'eu_data-0216060218' --cos-dependencies-archive 'features_eu_data-d573f57d-e573-4b27-9eaf-3846a5541116.tar.gz' --file 'covid-notebooks/notebooks/features_eu_data.ipynb' --inputs 'cases.csv' --outputs 'cases_features.csv' "
    ],
    task_id="features_eu_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eu_data-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_d573f57d_e573_4b27_9eaf_3846a5541116 << op_da4f63d6_5165_4625_8383_4c50b2e0a57f


# Operator source: covid-notebooks/notebooks/exploratory_eu_data.ipynb

op_22c4d83b_8cd5_4402_97fd_886d1ee0a895 = KubernetesPodOperator(
    name="exploratory_eu_data",
    namespace="airflow",
    image="codait/covid-notebooks-anaconda-py3:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eu_data' --cos-endpoint http://192.168.1.130:32090 --cos-bucket liuqi --cos-directory 'eu_data-0216060218' --cos-dependencies-archive 'exploratory_eu_data-22c4d83b-8cd5-4402-97fd-886d1ee0a895.tar.gz' --file 'covid-notebooks/notebooks/exploratory_eu_data.ipynb' --inputs 'cases_features.csv;cases.csv' "
    ],
    task_id="exploratory_eu_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eu_data-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_22c4d83b_8cd5_4402_97fd_886d1ee0a895 << op_d573f57d_e573_4b27_9eaf_3846a5541116


# Operator source: covid-notebooks/notebooks/pivot_eu_data.ipynb

op_f3280cdf_031d_4b92_9b55_4a4d2b775a1f = KubernetesPodOperator(
    name="pivot_eu_data",
    namespace="airflow",
    image="codait/covid-notebooks-anaconda-py3:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eu_data' --cos-endpoint http://192.168.1.130:32090 --cos-bucket liuqi --cos-directory 'eu_data-0216060218' --cos-dependencies-archive 'pivot_eu_data-f3280cdf-031d-4b92-9b55-4a4d2b775a1f.tar.gz' --file 'covid-notebooks/notebooks/pivot_eu_data.ipynb' --inputs 'cases.csv' --outputs 'cases_pivot.pickle' "
    ],
    task_id="pivot_eu_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eu_data-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_f3280cdf_031d_4b92_9b55_4a4d2b775a1f << op_da4f63d6_5165_4625_8383_4c50b2e0a57f


# Operator source: covid-notebooks/notebooks/pivot_analysis_eu_data.ipynb

op_216832bc_242b_40ca_82f2_a164c085576b = KubernetesPodOperator(
    name="pivot_analysis_eu_data",
    namespace="airflow",
    image="codait/covid-notebooks-anaconda-py3:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eu_data' --cos-endpoint http://192.168.1.130:32090 --cos-bucket liuqi --cos-directory 'eu_data-0216060218' --cos-dependencies-archive 'pivot_analysis_eu_data-216832bc-242b-40ca-82f2-a164c085576b.tar.gz' --file 'covid-notebooks/notebooks/pivot_analysis_eu_data.ipynb' --inputs 'cases.csv;cases_pivot.pickle' "
    ],
    task_id="pivot_analysis_eu_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eu_data-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_216832bc_242b_40ca_82f2_a164c085576b << op_f3280cdf_031d_4b92_9b55_4a4d2b775a1f


# Operator source: covid-notebooks/notebooks/model_gaussfit_eu_data.ipynb

op_1fbf6446_510c_403b_b988_98ee619cc72a = KubernetesPodOperator(
    name="model_gaussfit_eu_data",
    namespace="airflow",
    image="codait/covid-notebooks-anaconda-py3:latest",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt' && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra-py37.txt --output requirements-elyra-py37.txt && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.14.2/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'eu_data' --cos-endpoint http://192.168.1.130:32090 --cos-bucket liuqi --cos-directory 'eu_data-0216060218' --cos-dependencies-archive 'model_gaussfit_eu_data-1fbf6446-510c-403b-b988-98ee619cc72a.tar.gz' --file 'covid-notebooks/notebooks/model_gaussfit_eu_data.ipynb' --inputs 'cases.csv' "
    ],
    task_id="model_gaussfit_eu_data",
    env_vars={
        "ELYRA_RUNTIME_ENV": "airflow",
        "AWS_ACCESS_KEY_ID": "minioadmin",
        "AWS_SECRET_ACCESS_KEY": "minioadmin",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "eu_data-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_1fbf6446_510c_403b_b988_98ee619cc72a << op_da4f63d6_5165_4625_8383_4c50b2e0a57f
