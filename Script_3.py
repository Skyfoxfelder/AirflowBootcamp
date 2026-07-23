from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
#from airflow.utils_rule import triggerRule


with DAG(
    dag_id="dag_exercice2",
    start_date=datetime(2026, 7, 23),
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
        #trigger_rule=triggerRule.ONE_SUCCESS
    )
    dodo = BashOperator(
        task_id="dodo",
        bash_command="echo 'Tache 2 : OK'"
        #trigger_rule=triggerRule.ONE_FAILED
    )
    Pipo = BashOperator(
            task_id="pipo",
            bash_command="echo 'Tache 2 : OK'"
    )
    toto = BashOperator(
            task_id="toto",
            bash_command="echo 'Tache 2 : OK'"
    )

    hello >> [babou, Pipo] >> [dodo, toto]