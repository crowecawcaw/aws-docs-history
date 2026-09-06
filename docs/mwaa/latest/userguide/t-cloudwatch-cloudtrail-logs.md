

# Troubleshooting: CloudWatch Logs and CloudTrail errors
<a name="t-cloudwatch-cloudtrail-logs"></a>

The topics on this page contain resolutions to Amazon CloudWatch Logs and AWS CloudTrail errors you can encounter on an Amazon Managed Workflows for Apache Airflow environment.

**Contents**
+ [Logs](#troubleshooting-view-logs)
  + [I can't find my task logs, or I received a `Reading remote log from Cloudwatch log_group` error](#t-task-logs)
  + [Tasks are failing without any logs](#t-task-failing-no-logs)
  + [I get a `ResourceAlreadyExistsException` error in CloudTrail](#t-cloudtrail)
  + [I get an `Invalid request` error in CloudTrail](#t-cloudtrail-bucket)
  + [I get `Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory` in Apache Airflow logs](#t-plugins-logs)
  + [I get psycopg2 'server closed the connection unexpectedly' in my scheduler logs](#scheduler-postgres-library)
  + [I get `Executor reports task instance %s finished (%s) although the task says its %s` in my DAG processing logs](#long-running-tasks)
  + [Triggerer logs do not appear in the Airflow UI](#t-triggerer-logs-missing)
  + [I get `Could not read remote logs from log_group: airflow-*{*environmentName}-Task log_stream:* {*DAG_ID}/*{*TASK_ID}/*{*time}/*{*n}.log.` in my task logs](#t-task-fail-permission)

## Logs
<a name="troubleshooting-view-logs"></a>

The following topic describes the errors you might receive when accessing Apache Airflow logs.

### I can't find my task logs, or I received a `Reading remote log from Cloudwatch log_group` error
<a name="t-task-logs"></a>

Amazon MWAA has configured Apache Airflow to read and write logs directly from and to Amazon CloudWatch Logs. If a worker fails to start a task, or fails to write any logs, you will refer to the error:

```
*** Reading remote log from Cloudwatch log_group: airflow-{{environmentName}}-Task log_stream: {{DAG_ID}}/{{TASK_ID}}/{{timestamp}}/{{n}}.log.Could not read remote logs from log_group: airflow-{{environmentName}}-Task log_stream: {{DAG_ID}}/{{TASK_ID}}/{{time}}/{{n}}.log.
```
+ We recommend the following steps:

  1. Verify that you have enabled task logs at the `INFO` level for your environment. For more information, refer to [Accessing Airflow logs in Amazon CloudWatch](monitoring-airflow.md).

  1. Verify that the environment [execution role](mwaa-create-role.md) has the correct permission policies.

  1. Verify that your operator or task is working correctly, has sufficient resources to parse the DAG, and has the appropriate Python libraries to load. To verify your whether you have the correct dependencies, try eliminating imports until you find the one that is causing the issue. We recommend testing your Python dependencies using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images).

### Tasks are failing without any logs
<a name="t-task-failing-no-logs"></a>

If tasks are failing in a workflow and you can't locate any logs for the failed tasks, check if you are setting the `queue` parameter in your default arguments, as listed in the following.

```
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Setting queue argument to default.
default_args = {
	"start_date": days_ago(1),
	"queue": "default"
}

with DAG(dag_id="any_command_dag", schedule_interval=None, catchup=False, default_args=default_args) as dag:
    cli_command = BashOperator(
        task_id="bash_command",
        bash_command="{{ dag_run.conf['command'] }}"
    )
```

To resovle the issue, remove `queue` from your code, and invoke the DAG again.

### I get a `ResourceAlreadyExistsException` error in CloudTrail
<a name="t-cloudtrail"></a>

```
"errorCode": "ResourceAlreadyExistsException",
    "errorMessage": "The specified log stream already exists",
    "requestParameters": {
        "logGroupName": "airflow-MyAirflowEnvironment-DAGProcessing",
        "logStreamName": "scheduler_cross-account-eks.py.log"
    }
```

Certain Python requirements such as `apache-airflow-backport-providers-amazon` roll back the `watchtower` library that Amazon MWAA uses to communicate with CloudWatch to an older version. We recommend the following steps:
+ Add the following library to your `requirements.txt`

  ```
  watchtower==1.0.6
  ```

### I get an `Invalid request` error in CloudTrail
<a name="t-cloudtrail-bucket"></a>

```
Invalid request provided: Provided role does not have sufficient permissions for s3 location airflow-xxx-xxx/dags
```

If you're creating an Amazon MWAA environment and an Amazon S3 bucket using the same CloudFormation template, you need to add a `DependsOn` section within your CloudFormation template. The two resources (*MWAA Environment* and *MWAA Execution Policy*) have a dependency in CloudFormation. We recommend the following steps:
+ Add the following **DependsOn** statement to your CloudFormation template.

  ```
  ...
    MaxWorkers: 5
    NetworkConfiguration:
      SecurityGroupIds:
        - !GetAtt SecurityGroup.GroupId
      SubnetIds: !Ref subnetIds
    WebserverAccessMode: PUBLIC_ONLY
  DependsOn: MwaaExecutionPolicy
  
   MwaaExecutionPolicy:
   Type: AWS::IAM::ManagedPolicy
   Properties:
     Roles:
      - !Ref MwaaExecutionRole
    PolicyDocument:
      Version: 2012-10-17		 	 	 
      Statement:
        - Effect: Allow
          Action: airflow:PublishMetrics
          Resource:
  ...
  ```

  For an example, refer to [Quick start tutorial for Amazon Managed Workflows for Apache Airflow](quick-start.md).

### I get `Cannot locate a 64-bit Oracle Client library: "libclntsh.so: cannot open shared object file: No such file or directory` in Apache Airflow logs
<a name="t-plugins-logs"></a>
+ We recommend the following steps:

  1. If you're using Apache Airflow v2, add `core.lazy_load_plugins : False` as an Apache Airflow configuration option. To learn more, refer to [Using configuration options to load plugins in 2](configuring-env-variables.md#configuring-2.0-airflow-override).

### I get psycopg2 'server closed the connection unexpectedly' in my scheduler logs
<a name="scheduler-postgres-library"></a>

If you get an error similar to the following, your Apache Airflow scheduler might have run out of resources.

```
2021-06-14T10:20:24.581-05:00    sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) server closed the connection unexpectedly
2021-06-14T10:20:24.633-05:00    This probably means the server terminated abnormally
2021-06-14T10:20:24.686-05:00    before or while processing the request.
```

We recommend the following steps:
+ Consider upgrading to Apache Airflow v2.0.2, which you can use to specify up to 5 schedulers.

### I get `Executor reports task instance %s finished (%s) although the task says its %s` in my DAG processing logs
<a name="long-running-tasks"></a>

If you get an error similar to the following, your long-running tasks might have reached the task time limit on Amazon MWAA. Amazon MWAA has a limit of 12 hours for any one Airflow task, to prevent tasks from getting stuck in the queue and blocking activities like autoscaling.

```
Executor reports task instance %s finished (%s) although the task says its %s. (Info: %s) Was the task killed externally
```

We recommend the following steps:
+ Consider breaking up the task into multiple, shorter running tasks. Airflow typically has a model whereby operators are asynchronous. It invokes activities on external systems, and Apache Airflow Sensors poll to check when it's complete. If a Sensor fails, it can be safely retried without impacting the Operator's functionality.

### Triggerer logs do not appear in the Airflow UI
<a name="t-triggerer-logs-missing"></a>

If triggerer logs do not appear in the Apache Airflow UI, your execution role might be missing the `logs:DescribeLogStreams` permission. Without this permission, Amazon MWAA cannot discover triggerer log streams. No error appears in the logs, which can make this issue difficult to identify.

Add `logs:DescribeLogStreams` to your execution role. Scope the permission to your environment's log group ARN. For more information, see [Amazon MWAA execution role](mwaa-create-role.md).

**Note**  
This issue affects your environment if you use Apache Airflow version 3.x with deferrable operators. If you created your execution role in the console before the default role included this permission, add it manually.

### I get `Could not read remote logs from log_group: airflow-*{*environmentName}-Task log_stream:* {*DAG_ID}/*{*TASK_ID}/*{*time}/*{*n}.log.` in my task logs
<a name="t-task-fail-permission"></a>

If you get an error similar to the following, the execution role for your environment might not contain a permissions policy to create log streams for task logs.

```
Could not read remote logs from log_group: airflow-*{*environmentName}-Task log_stream:* {*DAG_ID}/*{*TASK_ID}/*{*time}/*{*n}.log.
```

We recommend the following steps:
+ Modify the execution role for your environment using one of the sample policies at [Amazon MWAA execution role](mwaa-create-role.md).

You might have also specified a provider package in your `requirements.txt` file that is incompatible with your Apache Airflow version. For example, if you're using Apache Airflow v2.0.2, you might have specified a package, such as the [apache-airflow-providers-databricks](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/index.html) package, which is only compatible with Airflow 2.1\+.

We recommend the following steps:

1. If you're using Apache Airflow v2.0.2, modify the `requirements.txt` file and add `apache-airflow[databricks]`. This installs the correct version of the Databricks package that is compatible with Apache Airflow v2.0.2.

1. Test your DAGs, custom plugins, and Python dependencies locally using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images) on GitHub.