# Invoking DAGs in different Amazon MWAA

environments

The following code example creates an Apache Airflow CLI token. The code then uses a directed acyclic
graph (DAG) in one Amazon MWAA environment to invoke a DAG in a different Amazon MWAA environment.

###### Topics

- [Version](#samples-invoke-dag-version "#samples-invoke-dag-version")
- [Prerequisites](#samples-invoke-dag-prereqs "#samples-invoke-dag-prereqs")
- [Permissions](#samples-invoke-dag-permissions "#samples-invoke-dag-permissions")
- [Dependencies](#samples-invoke-dag-dependencies "#samples-invoke-dag-dependencies")
- [Code example](#samples-invoke-dag-code "#samples-invoke-dag-code")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

To use the code example on this page, you need the following:

- Two [Amazon MWAA environments](get-started.md "get-started.md") with **public network** webserver access, including your current
  environment.
- A sample DAG uploaded to your target environment's Amazon Simple Storage Service (Amazon S3) bucket.

## Permissions

To use the code example on this page, your environment's execution role must have
permission to create an Apache Airflow CLI token. You can attach the AWS-managed policy
`AmazonMWAAAirflowCliAccess` to grant this permission.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "airflow:CreateCliToken"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information, refer to [Apache Airflow CLI policy: AmazonMWAAAirflowCliAccess](access-policies.md#cli-access "access-policies.md#cli-access").

## Dependencies

To use this code example with Apache Airflow v2 and later, no additional dependencies are required. Use
[aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") to install Apache Airflow.

## Code example

The following code example assumes that you're using a DAG in your current environment to
invoke a DAG in another environment.

1. In your terminal, navigate to the directory where your DAG code is stored. For example:

```
cd dags
```

2. Copy the content of the following code example and save it locally as `invoke_dag.py`. Replace the following values
   with your information.
   - `your-new-environment-name` – The name of the other environment where
     you want to invoke the DAG.
   - `your-target-dag-id` – The ID of the DAG in the other environment
     that you want to invoke.

```
from airflow.decorators import dag, task
import boto3
from datetime import datetime, timedelta
import os, requests

DAG_ID = os.path.basename(__file__).replace(".py", "")

@task()
def invoke_dag_task(**kwargs):
    client = boto3.client('mwaa')
    token = client.create_cli_token(Name='your-new-environment-name')
    url = f"https://{token['WebServerHostname']}/aws_mwaa/cli"
    body = 'dags trigger your-target-dag-id'
    headers = {
        'Authorization' : 'Bearer ' + token['CliToken'],
        'Content-Type': 'text/plain'
        }
    requests.post(url, data=body, headers=headers)

@dag(
    dag_id=DAG_ID,
    schedule_interval=None,
    start_date=datetime(2022, 1, 1),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False
    )
def invoke_dag():
    t = invoke_dag_task()

invoke_dag_test = invoke_dag()
```

3. Run the following AWS CLI command to copy the DAG to your environment's bucket, then trigger the DAG using the Apache Airflow UI.

```
`aws s3 cp `your-dag`.py s3://`your-environment-bucket`/dags/`
```

4. If the DAG runs successfully, you'll get output similar to the following in the task logs for `invoke_dag_task`.

```
[2022-01-01, 12:00:00 PDT] {{python.py:152}} INFO - Done. Returned value was: None
[2022-01-01, 12:00:00 PDT] {{taskinstance.py:1280}} INFO - Marking task as SUCCESS. dag_id=invoke_dag, task_id=invoke_dag_task, execution_date=20220101T120000, start_date=20220101T120000, end_date=20220101T120000
[2022-01-01, 12:00:00 PDT] {{local_task_job.py:154}} INFO - Task exited with return code 0
[2022-01-01, 12:00:00 PDT] {{local_task_job.py:264}} INFO - 0 downstream tasks scheduled from follow-on schedule check
```

To verify that your DAG was successfully invoked, navigate to the Apache Airflow UI for your new environment, then do the following:

    1. On the **DAGs** page, locate your new target DAG in the list of DAGs.
    2. Under **Last Run**, check the timestamp for the latest DAG run. This timestamp should closely match the latest timestamp for
     `invoke_dag` in your other environment.
    3. Under **Recent Tasks**, check that the last run was successful.
