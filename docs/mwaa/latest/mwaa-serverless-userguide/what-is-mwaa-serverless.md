# What is Amazon MWAA Serverless?

Amazon MWAA Serverless is a deployment option for MWAA that eliminates the operational overhead of managing Apache Airflow environments while providing
cost-effective serverless scaling. This solution simplifies managing operational scale, optimizing costs, and handling access control.

With Amazon MWAA Serverless, teams can concentrate on developing their workflow logic instead of worrying about capacity management.
The service automatically provides resources for both scheduled and on-demand workflow execution, with a cost model based on the actual compute time
during task execution.

Amazon MWAA Serverless also features an enhanced security architecture leveraging AWS Identity and Access Management (IAM). Individual workflows can be
assigned specific IAM permissions with tasks run in your chosen Virtual Private Cloud (VPC), enabling precise security controls without requiring
separate Airflow environments. This design reduces security administration overhead while strengthening overall security measures.

###### Note

Amazon MWAA Serverless uses [Apache Airflow v3](https://airflow.apache.org/docs/apache-airflow/3.0.0/release_notes.html#airflow-3-0-0-2025-04-22 "https://airflow.apache.org/docs/apache-airflow/3.0.0/release_notes.html#airflow-3-0-0-2025-04-22") with Python 3.12.

###### Topics

- [Key features](#mwaas-feature-overview "#mwaas-feature-overview")
- [How Amazon MWAA Serverless works](#mwaas-architecture-overview "#mwaas-architecture-overview")
- [Accessing Amazon MWAA Serverless](#acessing-mwaas "#acessing-mwaas")
- [Regions](#regions "#regions")
- [Are you a first-time Amazon MWAA Serverless user?](#first-time-user "#first-time-user")
- [Key concepts](mwaas-concepts.md "mwaas-concepts.md")
- [Apache Airflow Parameter Support](supported-airflow-parameters.md "supported-airflow-parameters.md")
- [Template Variables, Filters and Macros](supported-jinja-parameters.md "supported-jinja-parameters.md")

## Key features

The following are key features of Amazon MWAA Serverless:

- **Serverless architecture**: Provides an Amazon MWAA deployment option that eliminates the need to provision,
  configure, and tune Apache Airflow infrastructure.
- **Automatic scaling**: Dynamically scales compute resources to meet your workflow demands without manual intervention.
- **Workflow Isolation**: Each workflow runs with its own execution role and worker,
  providing enhanced security and preventing cross-workflow interference.
- **Enhanced security**: Workflow-specific IAM permissions for least-privilege access (compared to shared permissions
  in provisioned Amazon MWAA). Additionally, you can choose to run workflows in your VPC, where you can control the security for each workflow.
- **Cost optimization**: You only pay for actual workflow run time, which removes costs associated with idle resources.
  There are no upfront costs and no minimum provisioning is required.
- **Flexible workflow format**: Use YAML-based definition files to define your workflows.
- **AWS integration**: Use built-in access to other AWS services through open source Apache Airflow operators.
- **Workflow versioning**: Built-in versioning system allows you to manage workflow evolution and rollback to previous
  versions when needed.

### Amazon MWAA Serverless versus traditional Amazon MWAA

Understanding when to choose Amazon MWAA Serverless over Amazon MWAA helps you select the right orchestration approach for your use case.

| Category                      | Amazon MWAA Serverless                                                                                                                      | Traditional Amazon MWAA                                                                                                                                                                                                                                               |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Infrastructure management** | Fully managed<br>• no infrastructure to configure or maintain                                                                               | Managed Airflow environment with configurable capacity                                                                                                                                                                                                                |
| **Scaling**                   | Automatic scaling based on workflow demand                                                                                                  | Fixed always-on<br>[environment capacity](../userguide/environment-class.md "../userguide/environment-class.md")<br>, from micro to 2XL sizes, with<br>[automatic scaling](../userguide/mwaa-autoscaling.md "../userguide/mwaa-autoscaling.md")<br>of Airflow workers |
| **Cost model**                | Pay-per-use: charged only when workflows run                                                                                                | [Hourly rate](https://aws.amazon.com/managed-workflows-for-apache-airflow/pricing/ "https://aws.amazon.com/managed-workflows-for-apache-airflow/pricing/")<br>for environment, schedulers, web servers, and additional workers                                        |
| **Workflow isolation**        | Each workflow has its own execution role and access permissions. Tasks each run in isolated compute assuming the workflow's execution role. | Each MWAA environment provides the same access to all tasks. Airflow's role-based authentication supports UI-level<br>level isolation within an environment                                                                                                           |
| **Startup time**              | Each task provisions its own compute before execution                                                                                       | Environment always running, fast execution of tasks when worker capacity exists                                                                                                                                                                                       |
| **Workflow definition**       | YAML workflows definitions using the DAG factory format, supporting AWS operators, with option to convert Python definitions                | Python DAG support with AWS and custom operators                                                                                                                                                                                                                      |
| **Airflow UI access**         | No direct Airflow UI access (monitoring via logs)                                                                                           | Airflow web interface access                                                                                                                                                                                                                                          |

### When to use Amazon MWAA Serverless

Choose Amazon MWAA Serverless when you want to focus on workflow logic rather than infrastructure management. Amazon MWAA Serverless is particularly well-suited for:

- **Variable or unpredictable workloads**: Workflows that run sporadically or have varying resource requirements
  benefit from automatic scaling and pay-per-use pricing.
- **Cost-sensitive environments**: Development, testing, or production workloads where you want to minimize
  costs by avoiding idle infrastructure charges.
- **Multi-team organizations**: Teams that need workflow isolation for security or compliance reasons,
  with each workflow running under its own execution role.
- **AWS-native data pipelines**: Workflows primarily using AWS services like S3, Glue, EMR,
  Redshift, and SageMaker through built-in operators.
- **Simplified operations**: Organizations that want to reduce operational overhead by eliminating Apache
  Airflow environment management.

Consider provisioned Amazon MWAA when you need:

- Custom Python operators or complex DAG logic
- Direct access to the Airflow web interface
- Consistently high-volume workloads that benefit from always-on infrastructure
- Specific Airflow plugins or configurations not supported in the serverless model

## How Amazon MWAA Serverless works

Amazon MWAA Serverless uses a multi-tenant architecture that automatically manages infrastructure while maintaining strong isolation between workflows.
Here's how it works:

- **Workflow submission**: You submit YAML-based DAG definitions through AWS CLI, or API.
- **Automatic scheduling**: Amazon MWAA Serverless uses EventBridge Scheduler for reliable, timezone-aware scheduling of your workflows.
- **Resource allocation**: When a workflow runs, Amazon MWAA Serverless automatically provisions the necessary compute resources.
- **Isolated execution**: Each workflow runs with its own execution role and isolated compute environment, ensuring
  security and preventing interference.
- **Automatic cleanup**: Resources are automatically released when workflows complete, ensuring you only pay for actual usage.

This architecture provides the benefits of Apache Airflow workflow orchestration without the operational complexity of managing Airflow infrastructure.

## Accessing Amazon MWAA Serverless

You can access Amazon MWAA Serverless through multiple interfaces:

- **AWS Management Console**: Monitor workflows through the AWS Management Console.
- **AWS CLI**: Use the AWS CLI for programmatic workflow management and automation.
- **API**: Integrate Amazon MWAA Serverless into your applications using the REST API for workflow lifecycle management.
- **SDKs**: Use AWS SDKs in your preferred programming language to build applications that manage workflows.

## Regions

Amazon MWAA Serverless is available in the following AWS Regions.

- Europe (Ireland): eu-west-1
- Europe (London): eu-west-2
- Europe (Paris): eu-west-3
- Europe (Frankfurt): eu-central-1
- Europe (Stockholm): eu-north-1
- US East (N. Virginia): us-east-1
- US East (Ohio): us-east-2
- US West (Oregon): us-west-2
- South America (São Paulo): sa-east-1
- Asia Pacific (Tokyo): ap-northeast-1
- Asia Pacific (Seoul): ap-northeast-2
- Asia Pacific (Mumbai): ap-south-1
- Asia Pacific (Singapore): ap-southeast-1
- Asia Pacific (Sydney): ap-southeast-2
- Canada (Central): ca-central-1

## Are you a first-time Amazon MWAA Serverless user?

If you are a first-time user of Amazon MWAA Serverless, we recommend that you begin by reading the following sections:

- [Prerequisites for using Amazon MWAA Serverless](prerequisites-set-up.md "prerequisites-set-up.md")
- [Get started with Amazon MWAA Serverless](get-started.md "get-started.md")
- [Workflows](workflows.md "workflows.md")
