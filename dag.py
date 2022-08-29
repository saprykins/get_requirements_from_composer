import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta


import requests
import json


def get_requirements(ti):
    import os
    os.system("pip list --format=freeze > req.txt")
    print(os.popen('cat req.txt').read())
    print('requirements were sent')


default_args = {
    'owner': 'airflow',    
    #'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(),
    # 'depends_on_past': False,
    #'email': ['airflow@example.com'],
    #'email_on_failure': False,
    #'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    #'retries': 1,
    'retry_delay': timedelta(minutes=5),
    }


dag_python = DAG(
	dag_id = "get_requirements",
	default_args=default_args,
	# schedule_interval='0 0 * * *',
	schedule_interval='@once',	
	dagrun_timeout=timedelta(minutes=60),
	description='use case of python operator in airflow',
	start_date = airflow.utils.dates.days_ago(1))


get_requirements = PythonOperator(
    task_id='get_requirements', 
    python_callable=get_requirements, 
    dag=dag_python
    )


get_requirements
