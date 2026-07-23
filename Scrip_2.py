from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
 
with DAG(
    dag_id="dag_exercice",
    start_date=datetime(2026, 7, 23),
    schedule=None,
    catchup=False,
    tags=["guide"],
) as dag:
    hello = BashOperator(
        task_id="hello",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date"
    )
    hello = BashOperator(
        task_id="ex_1",
        bash_command="echo 'Tache 1 : OK"
    )
    hello = BashOperator(
        task_id="ex_2",
        bash_command="echo 'Tache 2 : OK"
    )
hello >> ex_1 >> ex_2
