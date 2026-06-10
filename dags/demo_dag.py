from datetime import datetime
import time

from airflow.sdk import DAG, task

with DAG(
    dag_id="HelloDemo",
    start_date=datetime(2025, 1, 1),
    schedule="*/5 * * * *",
    catchup=False,
    tags=["demo"],
    
) as dag:

    @task
    def task_1()->str:
        message = "Hola test 1"
        return message
    
    @task
    def task_2()->str:
        message = "Hola test 2"
        time.sleep
        return message
    

    @task
    def task_3()->str:
        message = "Hola test 3"
        return message

    @task
    def task_4()->str:
        message = "Hola test 4"
        return message
    
    @task
    def task_5()->str:
        message = "Hola test 5"
        return message
    
    @task
    def task_6()->str:
        message = "Hola test 6"
        return message
    
    @task
    def task_7()->str:
        message = "Hola test 7"
        return message
    
    @task
    def task_8()->str:
        message = "Hola test 8"
        return message
    
    @task
    def task_9()->str:
        message = "Hola test 9"
        return message
    
    @task
    def task_10()->str:
        message = "Hola test 10"
        return message
    
    task_t1 = task_1()
    task_t2 = task_2()
    task_t3 = task_3()
    task_t4 = task_4()
    task_t5 = task_5()
    task_t6 = task_6()
    task_t7 = task_7()
    task_t8 = task_8()
    task_t9 = task_9()
    task_t10 = task_10()
    
    task_t1 >> task_t2
    task_t2 >> [task_t3, task_t4]
    [task_t3, task_t4] >> task_t5
    task_t6 >> [task_t7,task_t8]
    task_t8 >> task_t9 >> task_t10
    