# Troubleshooting Amazon Managed Workflows for Apache Airflow

This chapter describes common issues and errors you can encounter when using Apache Airflow on Amazon Managed Workflows for Apache Airflow and recommended steps to resolve these errors.

###### Contents

- [Troubleshooting: DAGs, Operators, Connections, and other issues](t-apache-airflow-202.md "t-apache-airflow-202.md")
  - [Connections](t-apache-airflow-202.md#troubleshooting-conn-202 "t-apache-airflow-202.md#troubleshooting-conn-202")
    - [I can't connect to Secrets Manager](t-apache-airflow-202.md#access-secrets-manager "t-apache-airflow-202.md#access-secrets-manager")
    - [How do I configure secretsmanager:ResourceTag/<tag-key> secrets manager conditions
      or a resource restriction in my execution role policy?](t-apache-airflow-202.md#access-secrets-manager-condition-keys "t-apache-airflow-202.md#access-secrets-manager-condition-keys")
    - [I can't connect to Snowflake](t-apache-airflow-202.md#missing-snowflake "t-apache-airflow-202.md#missing-snowflake")
    - [I can't find my connection in the Airflow UI](t-apache-airflow-202.md#connection-type-missing "t-apache-airflow-202.md#connection-type-missing")

  - [Webserver](t-apache-airflow-202.md#troubleshooting-webserver-202 "t-apache-airflow-202.md#troubleshooting-webserver-202")
    - [I get a 5xx error accessing the webserver](t-apache-airflow-202.md#5xx-webserver-202 "t-apache-airflow-202.md#5xx-webserver-202")
    - [I get a The scheduler does not seem to be running error](t-apache-airflow-202.md#error-scheduler-202 "t-apache-airflow-202.md#error-scheduler-202")

  - [Tasks](t-apache-airflow-202.md#troubleshooting-tasks-202 "t-apache-airflow-202.md#troubleshooting-tasks-202")
    - [I get my tasks stuck or not completing](t-apache-airflow-202.md#stranded-tasks-202 "t-apache-airflow-202.md#stranded-tasks-202")
    - [I get task failures without logs in Airflow v3](t-apache-airflow-202.md#failed-task-no-log "t-apache-airflow-202.md#failed-task-no-log")

  - [CLI](t-apache-airflow-202.md#troubleshooting-cli-202 "t-apache-airflow-202.md#troubleshooting-cli-202")
    - [I get a '503' error when triggering a DAG in the CLI](t-apache-airflow-202.md#cli-toomany-202 "t-apache-airflow-202.md#cli-toomany-202")
    - [Why does the dags backfill Apache Airflow CLI command fail? Is there a workaround?](t-apache-airflow-202.md#troubleshooting-cli-backfill "t-apache-airflow-202.md#troubleshooting-cli-backfill")

  - [Operators](t-apache-airflow-202.md#troubleshooting-operators-202 "t-apache-airflow-202.md#troubleshooting-operators-202")
    - [I received a PermissionError: [Errno 13] Permission denied error using the S3Transform operator](t-apache-airflow-202.md#op-s3-transform "t-apache-airflow-202.md#op-s3-transform")

- [Troubleshooting: Creating and updating an Amazon MWAA environment](t-create-update-environment.md "t-create-update-environment.md")
  - [Updating requirements.txt](t-create-update-environment.md#troubleshooting-reqs "t-create-update-environment.md#troubleshooting-reqs")
    - [I specified a new version of my requirements.txt and it's taking more than 20 minutes to update my environment](t-create-update-environment.md#t-requirements "t-create-update-environment.md#t-requirements")

  - [Plugins](t-create-update-environment.md#troubleshooting-plugins "t-create-update-environment.md#troubleshooting-plugins")
    - [Does Amazon MWAA support implementing custom UI?](t-create-update-environment.md#custom-ui "t-create-update-environment.md#custom-ui")

  - [Create bucket](t-create-update-environment.md#troubleshooting-create-bucket "t-create-update-environment.md#troubleshooting-create-bucket")
    - [I can't select the option for S3 Block Public Access settings](t-create-update-environment.md#t-create-bucket "t-create-update-environment.md#t-create-bucket")

  - [Create environment](t-create-update-environment.md#troubleshooting-create-environment "t-create-update-environment.md#troubleshooting-create-environment")
    - [I tried to create an environment and it's stuck in the Creating state](t-create-update-environment.md#t-stuck-failure "t-create-update-environment.md#t-stuck-failure")
    - [I tried to create an environment but it displays the status as Create failed](t-create-update-environment.md#t-create-environ-failed "t-create-update-environment.md#t-create-environ-failed")
    - [I tried to select a VPC and received a Network Failure error](t-create-update-environment.md#t-network-failure "t-create-update-environment.md#t-network-failure")
    - [I tried to create an environment and received a service, partition, or resource "must be passed" error](t-create-update-environment.md#t-service-partition "t-create-update-environment.md#t-service-partition")
    - [I tried to create an environment and it displays the status as Available but when I try to access the Airflow UI an Empty Reply from Server or 502 Bad Gateway error is shown](t-create-update-environment.md#t-create-environ-empty-reply "t-create-update-environment.md#t-create-environ-empty-reply")
    - [I tried to create an environment and my user name is a bunch of random character names](t-create-update-environment.md#t-create-environ-random-un "t-create-update-environment.md#t-create-environ-random-un")

  - [Update environment](t-create-update-environment.md#troubleshooting-update-environment "t-create-update-environment.md#troubleshooting-update-environment")
    - [I tried changing the environment class but the update failed](t-create-update-environment.md#t-rollback-billing-failure "t-create-update-environment.md#t-rollback-billing-failure")

  - [Access environment](t-create-update-environment.md#troubleshooting-access-environment "t-create-update-environment.md#troubleshooting-access-environment")
    - [I can't access the Apache Airflow UI](t-create-update-environment.md#t-no-access-airflow-ui "t-create-update-environment.md#t-no-access-airflow-ui")

- [Troubleshooting: CloudWatch Logs and CloudTrail errors](t-cloudwatch-cloudtrail-logs.md "t-cloudwatch-cloudtrail-logs.md")
  - [Logs](t-cloudwatch-cloudtrail-logs.md#troubleshooting-view-logs "t-cloudwatch-cloudtrail-logs.md#troubleshooting-view-logs")
    - [I can't find my task logs, or I received a Reading remote log from Cloudwatch log_group error](t-cloudwatch-cloudtrail-logs.md#t-task-logs "t-cloudwatch-cloudtrail-logs.md#t-task-logs")
    - [Tasks are failing without any logs](t-cloudwatch-cloudtrail-logs.md#t-task-failing-no-logs "t-cloudwatch-cloudtrail-logs.md#t-task-failing-no-logs")
    - [I get a ResourceAlreadyExistsException error in CloudTrail](t-cloudwatch-cloudtrail-logs.md#t-cloudtrail "t-cloudwatch-cloudtrail-logs.md#t-cloudtrail")
    - [I get an Invalid request error in CloudTrail](t-cloudwatch-cloudtrail-logs.md#t-cloudtrail-bucket "t-cloudwatch-cloudtrail-logs.md#t-cloudtrail-bucket")
    - [I get Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory in Apache Airflow logs](t-cloudwatch-cloudtrail-logs.md#t-plugins-logs "t-cloudwatch-cloudtrail-logs.md#t-plugins-logs")
    - [I get psycopg2 'server closed the connection unexpectedly' in my scheduler logs](t-cloudwatch-cloudtrail-logs.md#scheduler-postgres-library "t-cloudwatch-cloudtrail-logs.md#scheduler-postgres-library")
    - [I get Executor reports task instance %s finished (%s) although the task says its %s in my DAG processing logs](t-cloudwatch-cloudtrail-logs.md#long-running-tasks "t-cloudwatch-cloudtrail-logs.md#long-running-tasks")
    - [I get Could not read remote logs from log_group: airflow-\*{\*environmentName}-Task log_stream:\* {\*DAG_ID}/\*{\*TASK_ID}/\*{\*time}/\*{\*n}.log. in my task logs](t-cloudwatch-cloudtrail-logs.md#t-task-fail-permission "t-cloudwatch-cloudtrail-logs.md#t-task-fail-permission")
