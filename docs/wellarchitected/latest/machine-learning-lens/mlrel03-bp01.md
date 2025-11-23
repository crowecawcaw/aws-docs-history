# MLREL03-BP01 Enable CI/CD/CT automation with

traceability

Enable source code, data, and artifact version control of ML
workloads to enable roll back to a specific version. Incorporate
continuous integration (CI), continuous delivery (CD), and
continuous training (CT) practices to ML workload operations,
providing automation with added traceability.

**Desired outcome:** You establish
automated pipelines that handle the entire machine learning
lifecycle from development to deployment and continuous training.
You gain the ability to track every artifact, model version,
dataset, and code change throughout the ML workflow, enabling
transparent auditing, reproducibility of experiments, and the
capability to quickly roll back to previous versions when needed.

**Common anti-patterns:**

- Manual deployment and training processes without version
  control.
- Lack of documentation on model lineage and data provenance.
- Inability to reproduce ML experiments due to missing environment
  configurations.
- Performing model training only when necessary without automated
  testing and validation.
- Siloed development and operations teams working separately on ML
  workflows.

**Benefits of establishing this best
practice:**

- Increases productivity through automation of repetitive ML
  development tasks.
- Improves reproducibility of ML experiments and model training.
- Enhances collaboration between data scientists and operations
  teams.
- Accelerates time-to-market for ML-powered features and
  applications.
- Reduces risk through ability to quickly roll back problematic
  deployments.
- Improves adherence to audit requirements through comprehensive
  traceability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing CI/CD/CT for machine learning workloads requires a
different approach than traditional software development due to
the data-centric nature of ML systems. While software CI/CD
focuses primarily on code, ML pipelines must also track data,
model artifacts, and training environments for full
reproducibility.

MLOps combines DevOps practices with machine learning to automate
and streamline the entire lifecycle of ML systems. By implementing
MLOps with traceability, you create a foundation that supports
reproducible science, auditability, and operational excellence.
This allows your organization to deploy ML models with confidence
while maintaining the ability to understand exactly how each model
was created and what data influenced its behavior.

Amazon SageMaker AI provides a comprehensive solution to implement
MLOps practices with built-in version control, lineage tracking,
and pipeline automation. By using SageMaker AI and complementary AWS
services, you can establish a robust MLOps framework that makes
your ML workflows reproducible, traceable, and maintainable.

### Implementation steps

1. **Implement version control for ML
   artifacts**. Set up repositories for code, data,
   models, and configurations using version control systems.
   Use
   [AWS CodeCommit](https://aws.amazon.com/codecommit/ "https://aws.amazon.com/codecommit/") or integrate with GitHub to version your
   ML code and configurations. For data and models, use
   [Amazon SageMaker AI Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") to version and catalog your
   models, creating a system of record that tracks the lineage
   of each model.
2. **Set up data versioning and lineage
   tracking**. Implement data version control to track
   changes in your datasets over time. Use
   [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") to store, share, and manage
   features for ML development, which you can use to track and
   version feature values. Implement Lineage Tracking to track
   the relationships between ML artifacts including data,
   models, training jobs, and deployments.
3. **Establish continuous integration
   practices**. Configure automated tests that verify
   both code quality and model performance. Set up CI pipelines
   using
   [AWS CodeBuild](https://aws.amazon.com/codebuild/ "https://aws.amazon.com/codebuild/") that run unit tests, integration tests, and
   model quality tests when changes are pushed to your
   repositories. Implement automated code review practices to
   maintain quality standards across your ML codebase.
4. **Build continuous delivery pipelines
   for models**. Create automated deployment pipelines
   for ML models using
   [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") or
   [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/"). Configure pipelines to include stages
   for data preparation, model training, evaluation, and
   deployment. Implement approval gates for human validation
   before models are deployed to production environments.
5. **Implement continuous training
   mechanisms**. Set up automated retraining pipelines
   that can be triggered by data drift, scheduled intervals, or
   on-demand. Use Amazon SageMaker AI Pipelines to create
   end-to-end workflows for model retraining. Implement
   monitoring for model drift using
   [SageMaker AI
   Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") and trigger retraining when performance
   degrades below thresholds.
6. **Establish model governance and
   approval workflows**. Create a governance framework
   that requires appropriate reviews and approvals before
   models move to production. Use SageMaker AI Model Registry to
   implement model approval workflows with different approval
   stages. Configure integration with notification services
   like [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") to alert stakeholders when models need review.
7. **Implement immutable infrastructure
   for reproducibility**. Use infrastructure as code
   (IaC) to define your ML environments consistently. Leverage
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") to define your SageMaker AI environments,
   maintaining consistency across development, testing, and
   production. Create standardized container images for
   training and inference to improve environment
   reproducibility.
8. **Set up comprehensive monitoring and
   logging**. Implement monitoring for your ML
   pipelines and deployed models. Use
   [CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
   to track operational metrics of your pipeline runs and model
   endpoints. Configure SageMaker AI Model Monitor to track data
   drift, model drift, and prediction quality over time.
9. **Create rollback mechanisms for
   models and pipelines**. Establish automated
   rollback procedures that can quickly revert to previous
   model versions when issues are detected. Configure SageMaker AI
   endpoints with production variants to support blue/green
   deployments and canary testing, enabling safe rollbacks when
   needed.

## Resources

**Related documents:**

- [Implement
  MLOps](../../../sagemaker/latest/dg/mlops.md "../../../sagemaker/latest/dg/mlops.md")
- [Pipelines
  overview](../../../sagemaker/latest/dg/pipelines-sdk.md "../../../sagemaker/latest/dg/pipelines-sdk.md")
- [AWS DevOps Guidance](../devops-guidance/devops-guidance.md "../devops-guidance/devops-guidance.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")
- [Create
  Amazon SageMaker AI projects with image building CI/CD
  pipelines](https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/ "https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/")

**Related videos:**

- [Deliver
  high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc "https://www.youtube.com/watch?v=T9llSCYJXxc")
- [Accelerate
  production for gen AI using Amazon SageMaker AI MLOps &
  FMOps](https://www.youtube.com/watch?v=-3Otl7GVeCc "https://www.youtube.com/watch?v=-3Otl7GVeCc")

**Related examples:**

- [Amazon
  Sagemaker MLOps](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops")
- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops "https://github.com/aws-samples/amazon-sagemaker-secure-mlops")
