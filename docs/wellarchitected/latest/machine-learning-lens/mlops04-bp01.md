# MLOPS04-BP01 Automate operations through MLOps and

CI/CD

Automate ML workload operations using infrastructure as code (IaC)
and configuration as code (CaC). Select appropriate MLOps mechanisms
to orchestrate your ML workflows and integrate with CI/CD pipelines
for automated deployments. This approach creates consistency across
your staging and production deployment environments. Enable model
observability and version control across your hosting
infrastructure.

**Desired outcome:** You establish
automated ML operations through MLOps practices and CI/CD pipelines
for repeatable, consistent deployments across environments. Your ML
workflows are orchestrated through infrastructure as code, providing
traceability, version control, and model observability. This enables
your teams to deliver ML models faster, with higher quality, and
maintain governance throughout the model lifecycle from development
to production.

**Common anti-patterns:**

- Manually deploying ML models to production environments.
- Using different tools and processes across development and
  production environments.
- Not versioning infrastructure, configuration, or model
  artifacts.
- Lacking automated testing for ML models before deployment.
- Creating one-off scripts for deployment instead of reusable
  templates.

**Benefits of establishing this best
practice:**

- Accelerated ML model development and deployment cycles.
- Consistent, reproducible environments across development and
  production.
- Improved collaboration between data scientists and operations
  teams.
- Enhanced governance and traceability for model artifacts and
  infrastructure.
- Improved rollbacks and version management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

MLOps combines machine learning, DevOps practices, and data
engineering to streamline and automate the end-to-end ML
lifecycle. By implementing infrastructure as code and
configuration as code principles, you create consistent,
reproducible environments while minimizing manual steps that can
introduce errors. This approach makes ML operations more reliable,
scalable, and maintainable.

Creating automated CI/CD pipelines for ML workloads requires
special consideration compared to traditional software
applications. You need to track not only code changes but also
data, model parameters, and training configurations. Using AWS
services for MLOps provides integrated tools to manage these
complexities while maintaining proper governance and
observability.

When implementing MLOps practices, start by defining your workflow
patterns and choosing appropriate orchestration tools based on
your specific requirements. AWS offers multiple options for ML
workflow orchestration, from purpose-built services like SageMaker AI
Pipelines to more general workflow engines like AWS Step Functions. Each provides different levels of abstraction, control,
and integration capabilities.

Model observability is crucial for ML systems in production,
allowing you to monitor model performance, detect drift, and run
retraining when necessary. Implementing comprehensive monitoring
assists you to quickly identify and respond to changes in model
behavior or data distributions.

### Implementation steps

1. **Define your ML workflow
   architecture**. Begin by mapping out your
   end-to-end ML workflow, including data preparation, feature
   engineering, model training, evaluation, deployment, and
   monitoring stages. Identify which steps can be automated and
   which require human intervention. Determine the appropriate
   level of separation between development, testing, and
   production environments based on your requirements.
2. **Select an infrastructure as code
   approach**. Choose either AWS CloudFormation or AWS CDK to define your infrastructure.
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") enables you to create and provision
   AWS deployments predictably and repeatedly using template
   files. For teams more comfortable with programming
   languages,
   [AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") allows you to define cloud
   resources using familiar languages like Python, TypeScript,
   or Java.
3. **Implement version control for
   assets**. Establish a version control strategy for
   ML assets including code, configurations, infrastructure
   definitions, and model artifacts. Use AWS CodeCommit or
   third-party repositories to store and version these assets.
   Implement branching strategies that allow for
   experimentation while maintaining stable production
   environments. Version control enables you to track changes,
   collaborate effectively, and roll back to previous versions
   when needed.
4. **Choose an MLOps orchestration
   strategy**. Based on your workflow needs, select an
   appropriate orchestration mechanism:
   - Use
     [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") to create ML workflows with
     Python SDK, visualize, and manage them in Amazon SageMaker AI Studio. SageMaker AI Pipelines automatically logs
     every step, creating an audit trail of model components
     including training data, configurations, parameters, and
     learning gradients.
   - Use
     [AWS Step Functions Data Science SDK](../../../step-functions/latest/dg/concepts-python-sdk.md "../../../step-functions/latest/dg/concepts-python-sdk.md") to automate ML
     workflows with more complex orchestration requirements
     or when integrating with other AWS services beyond
     SageMaker AI.
   - Use third-party tools such as
     [Amazon
     Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/ "https://aws.amazon.com/managed-workflows-for-apache-airflow/") to
     orchestrate workflows using Directed Acyclic Graphs
     (DAGs) written in Python, especially when you need to
     integrate with existing Apache Airflow deployments.

5. **Build CI/CD pipelines for ML
   models**. Implement CI/CD pipelines using
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") to automate the building, testing, and
   deployment of ML models. Include automated tests for data
   quality, model performance, and API functionality. Configure
   the pipeline to deploy to staging environments before
   production and implement approval gates where needed.
   Integrate model registration and versioning using Amazon SageMaker AI Model Registry.
6. **Set up model monitoring and
   observability**. Implement comprehensive monitoring
   for your deployed models using
   [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/"). Configure data quality
   monitoring, model quality monitoring, bias drift monitoring,
   and feature attribution drift monitoring. Use
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to create dashboards and alerts for model
   performance metrics.
7. **Establish automated rollback
   mechanisms**. Configure your deployment pipelines
   to support automated rollbacks when quality thresholds are
   not met. Implement canary or blue/green deployment
   strategies using
   [AWS CodeDeploy](https://aws.amazon.com/codedeploy/ "https://aws.amazon.com/codedeploy/") to gradually shift traffic to new model
   versions while monitoring for issues. This minimizes the
   impact of problematic deployments and provides service
   continuity.
8. **Integrate security and governance
   controls**. Implement security checks throughout
   your MLOps pipeline. Use
   [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") to control access to
   resources and
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to log API calls for auditing. Configure
   [Amazon SageMaker AI Model Cards](https://aws.amazon.com/sagemaker/ml-governance/ "https://aws.amazon.com/sagemaker/ml-governance/") to document model information,
   intended uses, limitations, and performance characteristics.
9. **Create environments for
   experimentation and testing**. Set up isolated
   environments for experimentation that don't impact
   production systems. Use
   [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/") to provide data scientists
   with self-service environments for exploration while
   maintaining governance through integrated data and AI
   workflows. Implement environment-specific configurations
   through parameter files or environment variables managed in
   your IaC templates.

## Resources

**Related documents:**

- [Pipelines
  overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [What
  is AWS CodePipeline?](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md")
- [Amazon
  Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/ "https://aws.amazon.com/managed-workflows-for-apache-airflow/")
- [AWS CloudFormation Documentation](../../../cloudformation/index.md "../../../cloudformation/index.md")
- [What
  is the AWS CDK?](../../../cdk/latest/guide/home.md "../../../cdk/latest/guide/home.md")
- [Step
  Functions Data Science SDK](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/ "https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/")
- [Infrastructure
  as code](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")

**Related videos:**

- [AWS re:Invent 2024 - Accelerate ML workflows with Amazon SageMaker AI
  Studio](https://www.youtube.com/watch?v=SAeZMA0KaFA "https://www.youtube.com/watch?v=SAeZMA0KaFA")
