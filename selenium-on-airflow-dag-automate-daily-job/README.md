
  Job execution Airflow DAG Selenium Webscaper
===
   Run Job execution with selenium Dag using BBC Radio5 Wake-up-to-money mp3 podcast download as an webscraper example


     Execute installation with automated docker composer

        $ bash -x get-docker-compose-Selenium-executor.sh



  Selenium Plugin
===

   ![AirFlow - Docker Container ecosystem](images/Airflow-DAG-Selenium-example-BBC-Radio5-wake-up-to-money-mp3-downlod-webscrapper.png )


  Imap Plugin
===

The purpose of this plugin is to use the Internet Message Access Protocol (IMAP) to retrieve email messages from a given mail server.

## Creating a connection

To create an IMAP connection using the Airflow UI you need to open the interface > Admin dropdown menu > click on 'connections' > create. The connection needs to be of the form:
* Conn Id: Your connection id
* Host: This is the IMAP server url
* Login: Your email address
* Password: Your email password, this may not be the same as your everyday email password depending on your mail server

## Hooks

The hook is called IMAPHook and can be instantiated with the relevant Airflow connection id.

The hook has a series of methods to connect to a mail server, search for a specific email and download its attachments.

```python
from airflow.hooks import IMAPHook

hook = IMAPHook(imap_conn_id='imap_default')
```

## Operators

### IMAPAttachmentOperator

This operator downloads the attachement of an email recieved the day before the execution date within the airflow context and saves it to a local directory.

```python
op = IMAPAttachmentOperator(
    imap_conn_id='imap_default',
    mailbox='mail_test',
    search_criteria={"FROM": "noreply@example.com",
                     "SUBJECT": "daily_report"},
    local_path='',
    file_name='',
    task_id='imap_example')

op.execute(context={'yesterday_ds': '2019-08-04'})

```


  Information in Article
===
   Follow source selenium DAG article in [towards datascience link](https://towardsdatascience.com/selenium-on-airflow-automate-a-daily-online-task-60afc05afaae)

