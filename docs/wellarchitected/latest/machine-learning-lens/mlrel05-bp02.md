# MLREL05-BP02 Create a recoverable endpoint with a managed

version control strategy

Establish a fully recoverable system for model prediction endpoints
by implementing proper version control and lineage tracking for
components that generate these endpoints.

**Desired outcome:** You have a
robust infrastructure where components related to model deployment,
including model artifacts, container images, and endpoint
configurations, are version controlled and traceable. You can
recover quickly from issues by identifying and reverting to previous
stable versions, and you can audit the full lineage of model
deployments for governance and regulatory requirements.

**Common anti-patterns:**

- Storing model artifacts without proper versioning.
- Using deployment processes only when needed without
  infrastructure as code.
- Failing to track dependencies between model artifacts,
  containers, and configurations.
- Not maintaining a centralized registry for models.
- Relying on manual processes for endpoint recovery.

**Benefits of establishing this best
practice:**

- Reduces recovery time when endpoint issues occur.
- Improves auditability and adherence through comprehensive
  lineage tracking.
- Enhances collaboration between data scientists and operations
  teams.
- Improves the consistency and reliability of model deployments.
- Enables reproduction of model endpoints exactly as they were at
  specific points in time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning model endpoints represent the interface where
your business delivers value from AI/ML investments. Verifying
that these endpoints are recoverable is critical for business
continuity. Recoverability depends on having comprehensive version
control for components involved in creating the endpoint.

A properly implemented MLOps framework for endpoint recoverability
tracks not just the model artifacts, but components that influence
the prediction service—training data, feature transformations,
container definitions, and infrastructure configurations. When
incidents occur, you need to understand the complete lineage of
your model endpoint, including which data trained the model, which
code created the container, and which configurations defined the
infrastructure.

By implementing proper version control and lineage tracking, you
create a system that is both resilient to failures and compatible
with governance requirements. You can trace exactly how each
endpoint was created and recreate it precisely when needed.

### Implementation steps

1. **Implement MLOps with Amazon SageMaker AI Pipelines and Projects**.
   [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") automates ML workflows by
   providing a service for building, running, and managing ML
   pipelines. It handles every step from data preparation to
   model deployment in a versioned, predictable manner.
2. **Implement a model registry
   system**. Use
   [Amazon SageMaker AI Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") to catalog your models for
   production. The registry tracks model versions and their
   approval status, creating a system of record for models in
   your organization. Define a clear approval workflow for
   moving models from development to production for proper
   governance at each stage. For each model, register metadata
   including performance metrics, training datasets, and
   intended use cases.
3. **Track experiments with SageMaker AI
   MLflow**. MLflow in SageMaker AI allows you to create,
   manage, analyze, and compare experiments. This way, data
   scientists can view and track the experiments for the
   current project. Each experiment logs every metric and
   hyperparameter automatically, along with model artifacts and
   dataset information.
4. **Use infrastructure as code (IaC)
   tools**. Define and build your infrastructure,
   including model endpoints, using
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/"). IaC makes your infrastructure version
   controlled, repeatable, and able to be reverted to previous
   states if needed. Store your infrastructure code in git
   repositories alongside your model code, creating a unified
   version history. This approach reduces configuration drift
   between environments and verifies that your production
   deployment exactly matches your tested configuration.
5. **Store containers in Amazon Elastic Container Registry**. Use
   [Amazon ECR](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md") to version and store the Docker containers that
   serve your models. Amazon ECR automatically creates version
   hashes for containers as you update them, enabling rollbacks
   to previous versions. Implement image scanning to detect
   security vulnerabilities, and apply lifecycle policies to
   manage older versions of your containers.
6. **Implement automated testing and
   deployment pipelines**. Create CI/CD pipelines
   using
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") to automate the testing and deployment
   of your models. These pipelines should validate models
   before deployment, deploy infrastructure changes through
   CloudFormation, and update model endpoints with minimal
   downtime. Integrate automated quality checks to avoid
   problematic models from reaching production.
7. **Configure automated backups and
   recovery processes**. Establish automated backup
   procedures for your model artifacts, container images, and
   endpoint configurations. Use
   [Amazon S3 versioning](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md") for model artifacts and
   [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/") to protect configuration data. Document and
   test recovery procedures regularly to verify that they work
   when needed.

## Resources

**Related documents:**

- [AWS CloudFormation Documentation](../../../cloudformation/index.md "../../../cloudformation/index.md")
- [Infrastructure
  as code](../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md "../../../whitepapers/latest/introduction-devops-aws/infrastructure-as-code.md")
- [Pipelines
  overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [What
  is Amazon Elastic Container Registry?](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Fully
  managed MLflow 3.0 on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/ "https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")
- [Multi-account
  model deployment with Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/multi-account-model-deployment-with-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/multi-account-model-deployment-with-amazon-sagemaker-pipelines/")
- [Automate
  feature engineering pipelines with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/automate-feature-engineering-pipelines-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automate-feature-engineering-pipelines-with-amazon-sagemaker/")

**Related videos:**

- [Next-generation
  CDK development with Amazon Q Developer](https://www.youtube.com/watch?v=WEYuvh3YqkI "https://www.youtube.com/watch?v=WEYuvh3YqkI")
- [Infrastructure
  as Code on AWS - AWS Online Tech Talks](https://www.youtube.com/watch?v=cKQtPZwf97s "https://www.youtube.com/watch?v=cKQtPZwf97s")
- [How
  to create fully automated ML workflows with Amazon SageMaker AI
  Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg "https://www.youtube.com/watch?v=W7uabCTfLrg")

**Related examples:**

- [Amazon SageMaker AI MLOps](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops")
