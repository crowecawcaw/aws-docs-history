# Using workflows in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio provides workflow capabilities that allow you to set up and run a series of tasks to orchestrate your data processing procedures. Workflows use Apache Airflow to model data processing procedures and orchestrate your Amazon SageMaker Unified Studio code artifacts.

Amazon SageMaker Unified Studio supports [MWAA serverless](../../../mwaa/latest/mwaa-serverless-userguide/what-is-mwaa-serverless.md "../../../mwaa/latest/mwaa-serverless-userguide/what-is-mwaa-serverless.md") and [MWAA provisioned](../../../mwaa/latest/userguide/what-is-mwaa.md "../../../mwaa/latest/userguide/what-is-mwaa.md") workflows:

- **Serverless** - Eliminates the operational overhead of managing Apache Airflow environments while providing cost-effective serverless scaling.
- **Provisioned** - A managed environment for Apache Airflow, to set up and run data pipelines in the cloud at scale.

###### Note

IAM domains supports only serverless workflows.

To deploy workflow applications across development, test, and production environments, see [CI/CD for Amazon SageMaker Unified Studio](cicd.md "cicd.md").
