# Serverless Workflows

Amazon SageMaker Unified Studio supports serverless workflows powered by [Amazon MWAA Serverless](../../../mwaa/latest/mwaa-serverless-userguide/what-is-mwaa-serverless.md "../../../mwaa/latest/mwaa-serverless-userguide/what-is-mwaa-serverless.md"). With serverless workflows, you can orchestrate data processing tasks without provisioning or managing Apache Airflow infrastructure. Resources are automatically provisioned when a workflow runs and released when it completes, so you only pay for actual workflow run time.

Serverless workflows in Amazon SageMaker Unified Studio provide the following capabilities:

- Automatic scaling of compute resources to meet workflow demands without manual intervention.
- Workflow isolation, where each workflow runs with its own execution role and worker, providing enhanced security and preventing cross-workflow interference.
- Cost optimization through a pay-per-use model with no upfront costs or minimum provisioning required.
- Built-in integration with AWS services including Amazon S3, Amazon Redshift, Amazon EMR, AWS Glue, and Amazon SageMaker AI.
- YAML-based workflow definition files.
