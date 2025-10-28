# Using a secret key in AWS Secrets Manager for an Apache Airflow connection

The following sample calls AWS Secrets Manager to get a secret key for an Apache Airflow connection on Amazon Managed Workflows for Apache Airflow. It assumes you've completed the steps in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").

###### Topics

- [Version](#samples-secrets-manager-version "#samples-secrets-manager-version")
- [Prerequisites](#samples-secrets-manager-prereqs "#samples-secrets-manager-prereqs")
- [Permissions](#samples-secrets-manager-permissions "#samples-secrets-manager-permissions")
- [Requirements](#samples-hive-dependencies "#samples-hive-dependencies")
- [Code sample](#samples-secrets-manager-code "#samples-secrets-manager-code")
- [What's next?](#samples-secrets-manager-next-up "#samples-secrets-manager-next-up")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

To use the sample code on this page, you'll need the following:

- The Secrets Manager backend as an Apache Airflow configuration option as listed in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").
- An Apache Airflow connection string in Secrets Manager as listed in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").

## Permissions

- Secrets Manager permissions as listed in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").

## Requirements

To use this code example with Apache Airflow v2 and later, no additional dependencies are required. Use
[aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images") to install Apache Airflow.

## Code sample

The following steps describe how to create the DAG code that calls Secrets Manager to get the secret.

1. In your command prompt, navigate to the directory where your DAG code is stored. For example:

```
cd dags
```

2. Copy the contents of the following code sample and save locally as `secrets-manager.py`.

```
"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from airflow import DAG, settings, secrets
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.hooks.base_aws import AwsBaseHook

from datetime import timedelta
import os

### The steps to create this secret key can be found at: https://docs.aws.amazon.com/mwaa/latest/userguide/connections-secrets-manager.html
sm_secretId_name = 'airflow/connections/myconn'

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'depends_on_past': False
}


### Gets the secret myconn from Secrets Manager
def read_from_aws_sm_fn(**kwargs):
    ### set up Secrets Manager
    hook = AwsBaseHook(client_type='secretsmanager')
    client = hook.get_client_type(region_name='us-east-1')
    response = client.get_secret_value(SecretId=sm_secretId_name)
    myConnSecretString = response["SecretString"]

    return myConnSecretString

### 'os.path.basename(__file__).replace(".py", "")' uses the file name secrets-manager.py for a DAG ID of secrets-manager
with DAG(
        dag_id=os.path.basename(__file__).replace(".py", ""),
        default_args=default_args,
        dagrun_timeout=timedelta(hours=2),
        start_date=days_ago(1),
        schedule_interval=None
) as dag:
    write_all_to_aws_sm = PythonOperator(
        task_id="read_from_aws_sm",
        python_callable=read_from_aws_sm_fn,
        provide_context=True
    )

```

## What's next?

- Learn how to upload the DAG code in this example to the `dags` folder in your Amazon S3 bucket in [Adding or updating DAGs](configuring-dag-folder.md "configuring-dag-folder.md").
