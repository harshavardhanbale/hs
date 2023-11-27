#hai#hai
from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

def TEST():
    a=1
    b='hello'
    c=a+b
    return c
default_args={
    'owner': 'airflow',
    'start_date':datetime(2023, 1, 15),
    'email': ['harshavardhan.bale@transcendstreet.com'],
    'email_on_failure': True,
    'depends_on_past':False,
    'retries':0
}
dag=DAG(dag_id='DAG-1',default_args=default_args,catchup=False,schedule_interval='@once')
#hai
hello_operator = PythonOperator(task_id='hello_task', python_callable=TEST, dag=dag)
hello_operator
#hai
