from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
 
with DAG(
    dag_id="dag_exercice",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["guide"],
) as dag:
    hello = BashOperator(
        task_id="hello",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date"
    )
    babou = BashOperator(
        task_id="babou",
        bash_command="echo 'Tache 1 : OK'"
    )
    dodo = BashOperator(
        task_id="dodo",
        bash_command="echo 'Tache 2 : OK'"
    )

    hello >> babou >> dodo
