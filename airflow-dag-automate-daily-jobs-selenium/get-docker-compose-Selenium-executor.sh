#/bin/bash env
#
# Follow Medium post here : https://towardsdatascience.com/selenium-on-airflow-automate-a-daily-online-task-60afc05afaae 
#
#sudo mkdir -p /usr/local/airflow/dags
#sudo mkdir -p /usr/local/airflow/plugins
#sudo mkdir -p /usr/local/airflow/downloads
#sudo mkdir -p /usr/local/airflow/selenium_scripts
#
docker build -t docker_airflow -f Dockerfile-airflow .
#
docker pull selenium/standalone-chrome
#
docker build -t docker_selenium -f Dockerfile-selenium .
#
docker pull selenium/standalone-chrome
#
docker network create container_bridge
#
docker volume create downloads
#
docker-compose up
#  
