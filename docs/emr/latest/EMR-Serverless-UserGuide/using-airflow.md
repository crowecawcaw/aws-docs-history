# Submitting EMR Serverless jobs from Airflow

The Amazon Provider in Apache Airflow provides EMR Serverless operators. For more
information about operators, refer to [Amazon EMR Serverless Operators](https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/emr_serverless.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/stable/operators/emr_serverless.html") in the Apache Airflow documentation.

You can use `EmrServerlessCreateApplicationOperator` to create a Spark or Hive
application. You can also use `EmrServerlessStartJobOperator` to start one or
more jobs with the your new application.

To use the operator with Amazon Managed Workflows for Apache Airflow (MWAA) with Airflow
2.2.2, add the following line to your `requirements.txt` file and update your
MWAA environment to use the new file.

```
apache-airflow-providers-amazon==6.0.0
boto3>=1.23.9
```

Note that EMR Serverless support was added to release 5.0.0 of the Amazon provider.
Release 6.0.0 is the last version compatible with Airflow 2.2.2. You can use later versions
with Airflow 2.4.3 on MWAA.

The following abbreviated example shows how to create an application, run multiple Spark
jobs, and then stop the application. A full example is available in the [EMR Serverless Samples](https://github.com/aws-samples/emr-serverless-samples/tree/main/airflow "https://github.com/aws-samples/emr-serverless-samples/tree/main/airflow") GitHub repository. For additional details of
`sparkSubmit` configuration, refer to [Using Spark configurations when you run EMR Serverless jobs](jobs-spark.md "jobs-spark.md").

```
from datetime import datetime

from airflow import DAG
from airflow.providers.amazon.aws.operators.emr import (
    EmrServerlessCreateApplicationOperator,
    EmrServerlessStartJobOperator,
    EmrServerlessDeleteApplicationOperator,
)

# Replace these with your correct values
JOB_ROLE_ARN = "arn:aws:iam::`account-id`:role/emr_serverless_default_role"
S3_LOGS_BUCKET = "`amzn-s3-demo-bucket`"

DEFAULT_MONITORING_CONFIG = {
    "monitoringConfiguration": {
        "s3MonitoringConfiguration": {"logUri": f"s3://`amzn-s3-demo-bucket`/logs/"}
    },
}

with DAG(
    dag_id="example_endtoend_emr_serverless_job",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    tags=["example"],
    catchup=False,
) as dag:
    create_app = EmrServerlessCreateApplicationOperator(
        task_id="create_spark_app",
        job_type="SPARK",
        release_label="emr-6.7.0",
        config={"name": "airflow-test"},
    )

    application_id = create_app.output

    job1 = EmrServerlessStartJobOperator(
        task_id="start_job_1",
        application_id=application_id,
        execution_role_arn=JOB_ROLE_ARN,
        job_driver={
            "sparkSubmit": {
                "entryPoint": "local:///usr/lib/spark/examples/src/main/python/pi_fail.py",
            }
        },
        configuration_overrides=DEFAULT_MONITORING_CONFIG,
    )

    job2 = EmrServerlessStartJobOperator(
        task_id="start_job_2",
        application_id=application_id,
        execution_role_arn=JOB_ROLE_ARN,
        job_driver={
            "sparkSubmit": {
                "entryPoint": "local:///usr/lib/spark/examples/src/main/python/pi.py",
                "entryPointArguments": ["1000"]
            }
        },
        configuration_overrides=DEFAULT_MONITORING_CONFIG,
    )

    delete_app = EmrServerlessDeleteApplicationOperator(
        task_id="delete_app",
        application_id=application_id,
        trigger_rule="all_done",
    )

    (create_app >> [job1, job2] >> delete_app)
```
