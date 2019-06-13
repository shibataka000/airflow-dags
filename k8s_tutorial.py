from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator

from airflow import DAG
from datetime import datetime, timedelta


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 5, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG('k8s_tutorial', default_args=default_args, schedule_interval=timedelta(days=1))

k = KubernetesPodOperator(
    namespace='default',
    image="ubuntu:16.04",
    cmds=["bash", "-cx"],
    arguments=["echo", "10"],
    labels={"foo": "bar"},
    name="test",
    task_id="task",
    is_delete_operator_pod=True,
    in_cluster=True,
    hostnetwork=False,
    dag=dag
)
