# Key concepts

Understanding Amazon MWAA Serverless concepts helps you design, deploy, and manage your workflow orchestration solutions. This section explains the core concepts and how they relate to traditional
Apache Airflow terminology.

- **Workflow**: The Amazon MWAA Serverless resource that represents your orchestration logic. A workflow is created through the Amazon MWAA Serverless API, or CLI.
  It contains metadata about scheduling, execution roles, and the orchestrated data processing steps (tasks).
- **Workflow Definition**: The Apache Airflow concept that defines the structure and dependencies of your tasks. While creating your Workflow,
  you provide your workflow definition file in Amazon S3. You can use the [Python to YAML DAG converter](https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/ "https://pypi.org/project/python-to-yaml-dag-converter-mwaa-serverless/")  
  to convert existing Python based DAG to YAML definitions.
- **[Task](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html")**:
  An individual unit of work within a workflow. Each task represents a specific operation that runs on a worker.
- **[Operator](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html "https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html")**:
  An Operator is a template for a predefined task.

###### Topics

- [Workflow isolation](#workflow-isolation "#workflow-isolation")
- [Workflow versioning](#workflow-versioning "#workflow-versioning")
- [Execution model](#execution-model "#execution-model")
- [YAML support](#yaml-dag-authoring "#yaml-dag-authoring")
- [Monitoring](#concepts-monitoring "#concepts-monitoring")

## Workflow isolation

One of the key benefits of Amazon MWAA Serverless is workflow isolation, which provides security and operational benefits:

- **Execution role isolation**: Each workflow runs with its own IAM execution role, ensuring that workflows can only access the resources
  they're explicitly granted permission to use.
- **Compute isolation**: Workflows run on dedicated compute resources that are provisioned when the workflow starts and released when it completes.
- **Network isolation**: If you choose to specify a VPC, each workflow's tasks run in isolated network environments with their own security group configurations.
  VPCs are optional with Amazon MWAA Serverless.

This isolation model contrasts with traditional Amazon MWAA where all workflows share the same Airflow environment and execution context.

## Workflow versioning

Amazon MWAA Serverless automatically manages workflow versions to help you track changes and enable rollbacks:

- **Automatic versioning**: Each time you update a workflow, Amazon MWAA Serverless creates a new version while preserving previous versions.
- **Version identification**: Versions are identified by alphanumeric ID.
- **Immutable versions**: Once created, workflow versions cannot be modified, ensuring consistency and enabling reliable rollbacks.

This versioning system allows you to safely evolve your workflows while maintaining the ability to rollback to previous working versions if issues arise.

## Execution model

Amazon MWAA Serverless uses a serverless execution model that differs significantly from traditional Airflow deployments:

### On-demand provisioning

Resources are provisioned only when workflows need to run:

- **Workflow startup**: When a workflow is triggered (by schedule or on-demand), Amazon MWAA Serverless provisions the necessary compute resources.
- **Task execution**: Individual tasks run on isolated compute instances with the appropriate execution role and network configuration.
- **Automatic cleanup**: Resources are automatically released when the workflow completes, ensuring you only pay for actual usage.

### Scheduling model

Amazon MWAA Serverless uses EventBridge Scheduler for reliable workflow scheduling:

- **Timezone support**: Schedules can be defined with specific timezones, ensuring workflows run at the correct local time regardless of AWS region.
- **Flexible scheduling**: Support for cron expressions, rate expressions, and one-time schedules.
- **Reliable delivery**: EventBridge Scheduler provides built-in retry logic and dead letter queue support for failed workflow triggers.

## YAML support

Amazon MWAA Serverless uses YAML based workflow definitions that provide a declarative approach to workflow authoring. You can use the Python to YAML converter tool to convert exiting Python based DAGs to YAML definition.

- **Declarative syntax**: Define your workflow structure, dependencies, and task configurations using YAML syntax.
- **Version control-friendly**: YAML files are easy to version control, review, and collaborate on.
- **Validation**: Amazon MWAA Serverless validates your YAML definitions before execution to catch configuration errors early.
- **Template support**: Use Jinja2 templating within your YAML definition for dynamic configuration.

Example YAML structure:

YAML

```

dag_id: my_data_pipeline
description: "Process daily data from S3 to Redshift"
schedule_interval: "0 2 * * *"  # Daily at 2 AM
start_date: "2024-01-01"

tasks:
extract_data:
operator: S3ListOperator
bucket: my-data-bucket
prefix: daily/

transform_data:
operator: GlueJobOperator
job_name: transform-daily-data
depends_on: [extract_data]

load_data:
operator: RedshiftSQLOperator
sql: "COPY target_table FROM 's3://processed-data/'"
depends_on: [transform_data]

```

## Monitoring

You can observe your Amazon MWAA Serverless resources using AWS native services:

- **CloudWatch logs**: Access your workflow and task logs in CloudWatch for analysis and troubleshooting.
- **CloudTrail integration**: API calls and workflow management actions are logged in CloudTrail for audit and compliance.
- **Console**: View workflow status using the Amazon MWAA Serverless console.

Unlike traditional Amazon MWAA, you don't have direct access to the Apache Airflow web interface. Instead, you can build your custom monitoring and observability using AWS native tools.
