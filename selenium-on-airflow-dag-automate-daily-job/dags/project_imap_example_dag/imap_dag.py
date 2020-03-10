
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
#
#
default_args = {
    'owner': 'github_user',
    # 'wait_for_downstream': True,
    'start_date': datetime(2019, 10, 8),
    'end_date': datetime(2019, 10, 20),
    'retries': 3,
    'retries_delay': timedelta(minutes=5)
    }
#
dag = DAG('imap_daily_download_emails_example_dag',
          schedule_interval='0 7 * * *',
          default_args=default_args)
#
hook = IMAPHook(imap_conn_id='imap_default')
#
#
op = IMAPAttachmentOperator(
    imap_conn_id='imap_default',
    mailbox='mail_test',
    search_criteria={"FROM": "noreply@example.com",
                    "SUBJECT": "daily_report"},
    local_path='',
    file_name='',
    task_id='imap_example')
#
op.execute(context={'yesterday_ds': '2020-03-09'})
#
