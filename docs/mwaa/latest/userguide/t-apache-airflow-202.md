# Troubleshooting: DAGs, Operators, Connections, and other issues

The topics on this page describe resolutions to Apache Airflow v2 and v3 Python dependencies, custom plugins, DAGs, Operators, Connections, tasks, and webserver issues you can encounter on an Amazon Managed Workflows for Apache Airflow environment.

###### Contents

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

## Connections

The following topic describes the errors you might receive when using an Apache Airflow connection, or using another AWS database.

### I can't connect to Secrets Manager

We recommend the following steps:

1. Learn how to create secret keys for your Apache Airflow connection and variables in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").
2. Learn how to use the secret key for an Apache Airflow variable (`test-variable`) in [Using a secret key in AWS Secrets Manager for an Apache Airflow variable](samples-secrets-manager-var.md "samples-secrets-manager-var.md").
3. Learn how to use the secret key for an Apache Airflow connection (`myconn`) in [Using a secret key in AWS Secrets Manager for an Apache Airflow connection](samples-secrets-manager.md "samples-secrets-manager.md").

### How do I configure `secretsmanager:ResourceTag/<tag-key>` secrets manager conditions

or a resource restriction in my execution role policy?

###### Note

Applies to Apache Airflow version 2.0 and earlier.

Currently, you cannot limit access to Secrets Manager secrets by using condition keys or other resource restrictions in your environment's execution role, due to
a known issue in Apache Airflow.

### I can't connect to Snowflake

We recommend the following steps:

1. Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.
2. Add the following entries to the requirements.txt for your environment.

```
apache-airflow-providers-snowflake==1.3.0
```

3. Add the following imports to your DAG:

```
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
```

Ensure the Apache Airflow connection object includes the following key-value pairs:

1. **Conn Id:** snowflake_conn
2. **Conn Type:** Snowflake
3. **Host:** <my account>.<my region if not us-west-2>.snowflakecomputing.com
4. **Schema:** <my schema>
5. **Login:** <my user name>
6. **Password:** \*\*\*\*\*\*\*\*
7. **Port:** <port, if any>
8. **Extra:**

```
{
						"account": "<my account>",
						"warehouse": "<my warehouse>",
						"database": "<my database>",
						"region": "<my region if not using us-west-2 otherwise omit this line>"
						}
```

For example:

```
>>> import json
				>>> from airflow.models.connection import Connection
				>>> myconn = Connection(
				...    conn_id='snowflake_conn',
				...    conn_type='Snowflake',
				...    host='`123456789012`.`us-east-1`.snowflakecomputing.com',
				...    schema='`YOUR_SCHEMA`'
				...    login='`YOUR_USERNAME`',
				...    password='`YOUR_PASSWORD`',
				...    port='`YOUR_PORT`'
				...    extra=json.dumps(dict(account='`123456789012`', warehouse='`YOUR_WAREHOUSE`', database='`YOUR_DB_OPTION`', region='`us-east-1`')),
				... )
```

### I can't find my connection in the Airflow UI

Apache Airflow provides connection templates in the Apache Airflow UI. It uses this to generate the connection URI string, regardless of the connection type. If a connection template is not available in the Apache Airflow UI, an alternate connection template can be used to generate a connection URI string, such as using the HTTP connection template.

We recommend the following steps:

1. Access the connection types Amazon MWAA's providing in the Apache Airflow UI at [Apache Airflow provider packages installed on Amazon MWAA environments](connections-packages.md "connections-packages.md").
2. Access the commands to create an Apache Airflow connection in the CLI at [Apache Airflow CLI command reference](airflow-cli-command-reference.md "airflow-cli-command-reference.md").
3. Learn how to use connection templates in the Apache Airflow UI interchangeably for connection types that aren't available in the Apache Airflow UI on Amazon MWAA at [Overview of connection types](manage-connection-types.md "manage-connection-types.md").

## Webserver

The following topic describes the errors you might receive for your Apache Airflow webserver on Amazon MWAA.

### I get a 5xx error accessing the webserver

We recommend the following steps:

1. Check Apache Airflow configuration options. Verify that the key-value pairs you specified as an Apache Airflow configuration option, such as AWS Secrets Manager, were configured correctly. To learn more, refer to [I can't connect to Secrets Manager](#access-secrets-manager "#access-secrets-manager").
2. Check the `requirements.txt`. Verify the Airflow "extras" package and other libraries listed in your `requirements.txt` are compatible with your Apache Airflow version.
3. Explore ways to specify Python dependencies in a `requirements.txt` file, refer to [Managing Python dependencies in requirements.txt](best-practices-dependencies.md "best-practices-dependencies.md").

### I get a `The scheduler does not seem to be running` error

If the scheduler doesn't seem to be running, or the last "heart beat" was
received several hours ago, your DAGs might not be listed in Apache Airflow, and new tasks will not be
scheduled.

We recommend the following steps:

1. Confirm that your VPC security group allows inbound access to port `5432`.
   This port is needed to connect to the Amazon Aurora PostgreSQL metadata database for your environment.
   After this rule is added, give Amazon MWAA a few minutes, and the error can disappear.
   To learn more, refer to [Security in your VPC on Amazon MWAA](vpc-security.md "vpc-security.md").

###### Note

    * The Aurora PostgreSQL metadatabase is part of the [Amazon MWAA service architecture](what-is-mwaa.md#architecture-mwaa "what-is-mwaa.md#architecture-mwaa")
     and is not available in your AWS account.
    * Database-related errors are usually a symptom of scheduler failure and not the root cause.

2. If the scheduler is not running, it might be due to a number of factors such as
   [dependency installation failures](best-practices-dependencies.md "best-practices-dependencies.md"),
   or an [overloaded scheduler](best-practices-tuning.md "best-practices-tuning.md"). Confirm that your DAGs,
   plugins, and requirements are working correctly by accessing the corresponding log groups in CloudWatch Logs.
   To learn more, refer to [Monitoring and metrics for Amazon Managed Workflows for Apache Airflow](cw-metrics.md "cw-metrics.md").

## Tasks

The following topic describes the errors you might receive for Apache Airflow tasks in an environment.

### I get my tasks stuck or not completing

If your Apache Airflow tasks are "stuck" or not completing, we recommend the following steps:

1. There might be a large number of DAGs defined. Reduce the number of DAGs and perform an update of the environment (such as changing a log level) to force a reset.
   1. Airflow parses DAGs whether they are enabled or not. If you're using greater than 50% of your environment's capacity you might start overwhelming the Apache Airflow scheduler. This leads to large _Total Parse Time_ in CloudWatch Metrics or long DAG processing times in CloudWatch Logs. There are other ways to optimize Apache Airflow configurations which are outside the scope of this guide.
   2. To learn more about the best practices we recommend to tune the performance of your environment, refer to [Performance tuning for Apache Airflow on Amazon MWAA](best-practices-tuning.md "best-practices-tuning.md").

2. There might be a large number of tasks in the queue. This is often shown as a large—and growing—number of tasks in the `None` state, or as a large number in `Queued Tasks` and/or `Tasks Pending` in CloudWatch. This can occur for the following reasons:
   1. If there are more tasks to run than the environment has the capacity to run, and/or a large number of tasks that were queued before autoscaling has time to detect the tasks and deploy additional workers.
   2. If there are more tasks to run than an environment has the capacity to run, we recommend **reducing** the number of tasks that your DAGs run concurrently, and/or increasing the minimum Apache Airflow workers.
   3. If there are a large number of tasks that were queued before autoscaling has had time to detect and deploy additional workers, we recommend **staggering** task deployment and/or increasing the minimum Apache Airflow workers.
   4. You can use the [update-environment](../../../cli/latest/reference/mwaa/update-environment.md "../../../cli/latest/reference/mwaa/update-environment.md") command in the AWS Command Line Interface (AWS CLI) to change the minimum or maximum number of workers that run on your environment.

   ```
   aws mwaa update-environment --name MyEnvironmentName --min-workers 2 --max-workers 10
   ```

   5. To learn more about the best practices we recommend to tune the performance of your environment, refer to [Performance tuning for Apache Airflow on Amazon MWAA](best-practices-tuning.md "best-practices-tuning.md").

3. If your tasks are stuck in the "running" state, you can also clear the tasks or mark them as succeeded or failed. This allows the autoscaling component for your environment to scale down the number of workers running on your environment. The following image depicts an example of a stranded task.

![This is an image with a stranded task.](images/mwaa-airflow-scaling.png)

    1. Choose the circle for the stranded task, and then select **Clear** (as shown). This allows Amazon MWAA to scale down workers; otherwise, Amazon MWAA can't determine which DAGs are enabled or disabled, and can't scale down, if there are still queued tasks.



    ![Apache Airflow Actions](images/mwaa-airflow-scaling-menu.png)

4. Learn more about the Apache Airflow task lifecycle at [Concepts](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#task-lifecycle "https://airflow.apache.org/docs/apache-airflow/stable/concepts.html#task-lifecycle") in the _Apache Airflow reference guide_.

### I get task failures without logs in Airflow v3

If your Apache Airflow 3 tasks are failing without logs, follow these steps:

- If the worker logs present an error such as `Task handler raised error: WorkerLostError('Worker exited prematurely: exitcode 15 Job: 12.')` around the time the task failed, this indicates that the forked worker process assigned to the task was likely terminated unexpectedly.

To address this, consider configuring celery.worker_autoscale with the same minimum and maximum values. For example:

```
celery.worker_autoscale=5,5  # for mw1.small
celery.worker_autoscale=10,10 # for mw1.medium
celery.worker_autoscale=20,20 # for mw1.large
```

This ensures that the worker pool size remains fixed, preventing unexpected worker terminations.

## CLI

The following topic describes the errors you might receive when running Airflow CLI commands in the AWS Command Line Interface.

### I get a '503' error when triggering a DAG in the CLI

The Airflow CLI runs on the Apache Airflow webserver, which has limited concurrency. Typically a maximum of 4 CLI commands can run simultaneously.

### Why does the `dags backfill` Apache Airflow CLI command fail? Is there a workaround?

###### Note

The following applies only to Apache Airflow v2.0.2 environments.

The `backfill` command, like other Apache Airflow CLI commands, parses all DAGs locally before any DAGs are processed, regardless of which DAG the CLI operation applies to.
In Amazon MWAA environments using Apache Airflow v2.0.2, because plugins and requirements are not yet installed on the webserver by the time the CLI command runs,
the parsing operation fails, and the `backfill` operation is not invoked. If you did not have any requirements nor plugins in your environment,
the `backfill` operation would succeed.

To be able to run the `backfill` CLI command, we recommend invoking it in a bash operator. In a bash operator, `backfill` is initiated from the worker, allowing the
DAGs to parse successfully as all necessary requirements and plguins are available and installed. Use the following example to create a DAG with a `BashOperator` to run
`backfill`.

```
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

with DAG(dag_id="backfill_dag", schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
    cli_command = BashOperator(
        task_id="bash_command",
        bash_command="airflow dags backfill my_dag_id"
    )
```

## Operators

The following topic describes the errors you might receive when using Operators.

### I received a `PermissionError: [Errno 13] Permission denied` error using the S3Transform operator

We recommend the following steps if you're trying to run a shell script with the _S3Transform_ operator and you're receiving a `PermissionError: [Errno 13] Permission denied` error. The following steps assume you have an existing plugins.zip file. If you're creating a _new_ plugins.zip, refer to [Installing custom plugins](configuring-dag-import-plugins.md "configuring-dag-import-plugins.md").

1. Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") on GitHub.
2. Create your "transform" script.

```
#!/bin/bash
cp $1 $2
```

3. (optional) macOS and Linux users might need to run the following command to ensure the script is executable.

```
chmod 777 transform_test.sh
```

4. Add the script to your plugins.zip.

```
zip plugins.zip transform_test.sh
```

5. Follow the steps in [Upload the plugins.zip to Amazon S3](configuring-dag-import-plugins.md#configuring-dag-plugins-upload "configuring-dag-import-plugins.md#configuring-dag-plugins-upload").
6. Follow the steps in [Specifying the plugins.zip version on the Amazon MWAA console](configuring-dag-import-plugins.md#configuring-dag-plugins-s3-mwaaconsole "configuring-dag-import-plugins.md#configuring-dag-plugins-s3-mwaaconsole").
7. Create the following DAG.

```
from airflow import DAG
						from airflow.providers.amazon.aws.operators.s3_file_transform import S3FileTransformOperator
						from airflow.utils.dates import days_ago
						import os

						DAG_ID = os.path.basename(__file__).replace(".py", "")

						with DAG (dag_id=DAG_ID, schedule_interval=None, catchup=False, start_date=days_ago(1)) as dag:
						file_transform = S3FileTransformOperator(
						task_id='file_transform',
						transform_script='/usr/local/airflow/plugins/transform_test.sh',
						source_s3_key='s3://`amzn-s3-demo-bucket`/files/input.txt',
						dest_s3_key='s3://`amzn-s3-demo-bucket`/files/output.txt'
						)
```

8. Follow the steps in [Uploading DAG code to Amazon S3](configuring-dag-folder.md#configuring-dag-folder-uploading "configuring-dag-folder.md#configuring-dag-folder-uploading").
