# Using a secret key in AWS Secrets Manager for an Apache Airflow variable

The following sample calls AWS Secrets Manager to get a secret key for an Apache Airflow variable on Amazon Managed Workflows for Apache Airflow. It assumes you've completed the steps in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").

###### Topics

- [Version](#samples-secrets-manager-var-version "#samples-secrets-manager-var-version")
- [Prerequisites](#samples-secrets-manager-var-prereqs "#samples-secrets-manager-var-prereqs")
- [Permissions](#samples-secrets-manager-var-permissions "#samples-secrets-manager-var-permissions")
- [Requirements](#samples-hive-dependencies "#samples-hive-dependencies")
- [Code sample](#samples-secrets-manager-var-code "#samples-secrets-manager-var-code")
- [What's next?](#samples-secrets-manager-var-next-up "#samples-secrets-manager-var-next-up")

## Version

You can use the code example on this page with **Apache Airflow v2** in [Python 3.10](https://peps.python.org/pep-0619/ "https://peps.python.org/pep-0619/") and **Apache Airflow v3** in [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/").

## Prerequisites

To use the sample code on this page, you'll need the following:

- The Secrets Manager backend as an Apache Airflow configuration option as listed in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").
- An Apache Airflow variable string in Secrets Manager as listed in [Configuring an Apache Airflow connection using a AWS Secrets Manager secret](connections-secrets-manager.md "connections-secrets-manager.md").

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

2. Copy the contents of the following code sample and save locally as `secrets-manager-var.py`.

```
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago
from datetime import timedelta
import os
DAG_ID = os.path.basename(__file__).replace(".py", "")
DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}
def get_variable_fn(**kwargs):
    my_variable_name = Variable.get("test-variable", default_var="undefined")
    print("my_variable_name: ", my_variable_name)
    return my_variable_name
with DAG(
    dag_id=DAG_ID,
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(hours=2),
    start_date=days_ago(1),
    schedule_interval='@once',
    tags=['variable']
) as dag:
    get_variable = PythonOperator(
        task_id="get_variable",
        python_callable=get_variable_fn,
        provide_context=True
    )
```

## What's next?

- Learn how to upload the DAG code in this example to the `dags` folder in your Amazon S3 bucket in [Adding or updating DAGs](configuring-dag-folder.md "configuring-dag-folder.md").
