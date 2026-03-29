# Provisioned Workflows

Amazon SageMaker Unified Studio supports provisioned workflows powered by [Amazon MWAA](../../../mwaa/latest/userguide/what-is-mwaa.md "../../../mwaa/latest/userguide/what-is-mwaa.md"). With provisioned workflows, you can create, schedule, and monitor workflows using Apache Airflow and Python without managing the underlying infrastructure for scalability, availability, and security.

Provisioned workflows in Amazon SageMaker Unified Studio provide the following capabilities:

- Automatic scaling of Apache Airflow workers to meet workflow demands, up to the maximum limits you define.
- Python DAG support with AWS and custom operators for orchestrating notebooks, querybooks, and data processing jobs.
- Workflow monitoring through Apache Airflow logs and metrics in Amazon CloudWatch.
- Built-in access to AWS services through open source Apache Airflow operators.
- Direct access to the Apache Airflow web interface for workflow management and monitoring.

###### Note

Provisioned workflows are available in Amazon SageMaker Unified Studio projects created with the **All capabilities** project profile.

Provisioned workflows run in a shared environment that all project members can access. To share your workflows with other users, commit the file defining your workflow and sync the workflow with the shared environment.
