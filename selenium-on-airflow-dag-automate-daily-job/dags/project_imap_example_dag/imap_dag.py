
import os
from airflow.models import DAG
from airflow.operators.imap_plugin import IMAPAttachmentOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
import airflow.hooks.S3_hook
from datetime import datetime, timedelta
import logging
#
from airflow.hooks import IMAPHook
##
#
class ExtendedPythonOperator(PythonOperator):
    '''
    extending the python operator so macros
    get processed for the op_kwargs field.
    '''
    template_fields = ('templates_dict', 'op_kwargs')


def weekday_branch():
    '''
    Returns task_id based on day of weekend only.
    '''
    if datetime.today().weekday() in range(0, 6):
        return 'get_op'
    else:
        return 'end'

date = '{{ ds_nodash }}'


default_args = {
    'owner': 'github_user',
    'wait_for_downstream': True, # was commented before - JPAC
    'start_date': datetime(2020, 3, 9),
    'end_date': datetime(2020, 3, 19),
    'retries': 3,
    'retries_delay': timedelta(minutes=5)
    }

yesterday = (datetime.now() - timedelta(days=1)) # .strftime('%yyyy%m%d')

dag = DAG('imap_daily_download_emails_example_dag',
          schedule_interval='0 7 * * *',
          default_args=default_args,
          start_date=yesterday)

start = DummyOperator(
    task_id='start',
    dag=dag)

weekday_branch = BranchPythonOperator(
    python_callable=weekday_branch,
    task_id='weekday_branch',
    dag=dag)

hook = IMAPHook(imap_conn_id='imap_default')

get_op = IMAPAttachmentOperator(
    imap_conn_id='imap_default',
    mailbox='mail_test',
    search_criteria={"FROM": "noreply@example.com",
                    "SUBJECT": "daily_report"},
    local_path='',
    file_name='',
    task_id='imap_example')

end = DummyOperator(
    task_id='end',
    dag=dag)

start >> weekday_branch
weekday_branch >> get_op
get_op >> end
weekday_branch >> end

#get_op.execute(context={'yesterday_ds': '2020-03-09'})

