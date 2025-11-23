# MLSEC03-BP04 Enforce data lineage

Data lineage tracking allows you to monitor and track data origins
and transformations over time, enabling better visibility into your
machine learning workflows. By enforcing data lineage, you can trace
the root cause of data processing errors and and protect the
integrity of your ML models.

**Desired outcome:** You can trace a
data element back to its source, verify the transformations it
underwent, and verify data integrity throughout the ML lifecycle.
You have visibility into your entire ML workflow from data
preparation to model deployment, enabling you to reproduce
workflows, establish model governance standards, and demonstrate
audit adherence.

**Common anti-patterns:**

- Treating data lineage as an afterthought rather than a core
  requirement.
- Failing to maintain records of data transformations during
  preprocessing.
- Not implementing integrity checks for detecting data
  manipulation or corruption.
- Neglecting to document code and infrastructure changes that
  affect the ML pipeline.
- Relying on manual tracking methods that are prone to errors and
  inconsistencies.

**Benefits of establishing this best
practice:**

- Improved troubleshooting through the ability to trace issues
  back to their source.
- Improves adherence to regulatory requirements through
  comprehensive audit trails.
- Greater confidence in model outputs by understanding the
  provenance of training data.
- Faster iteration cycles by being able to reproduce workflows
  efficiently.
- Better governance and risk management across ML operations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data lineage is a critical component of responsible ML operations.
By tracking the journey of your data from its source through
various transformations to model deployment, you create
accountability and transparency in your ML systems. Enforcing data
lineage involves implementing mechanisms to record metadata about
data origins, transformations, and access controls throughout the
ML lifecycle.

[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") provides built-in capabilities to track and
maintain data lineage through its MLflow tracking capabilities.
This system allows you to record the relationships between various
ML artifacts such as datasets, algorithms, hyperparameters, and
model artifacts. By utilizing these tracking capabilities, you can
establish a clear audit trail that assists with reproducibility,
governance, and troubleshooting.

Proper data lineage implementation also requires strict access
controls to block unauthorized data manipulation. Your tracking
system should record who accessed the data, what changes were
made, and when those changes occurred. Additionally, implement
integrity checks against your training data to detect unexpected
deviations caused by data corruption or malicious manipulation.

### Implementation steps

1. **Set up Amazon SageMaker AI MLflow
   Tracking**. Enable tracking capabilities in your
   SageMaker AI environment to automatically capture metadata
   about your ML workflows. Configure SageMaker AI to track
   artifacts, associations, and context information using
   [Amazon SageMaker AI MLflow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md"). MLflow in SageMaker AI allows you to
   create, manage, analyze, and compare experiments, providing
   comprehensive tracking of training runs, model versions, and
   associated metadata.
2. **Implement automated metadata
   collection**. Configure your ML pipelines to
   automatically record metadata at each stage of processing.
   Use
   [SageMaker AI
   Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md") jobs to track data transformations and
   record preprocessing steps. Apply
   [SageMaker AI
   Pipeline](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") steps to document the flow of data from one
   stage to another, creating a complete record of the data
   journey.
3. **Establish data access
   controls**. Implement strict access controls to
   protect data integrity. Use
   [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") roles and policies to
   restrict access to specific datasets and models. Configure
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to detect unauthorized access
   or changes to your data.
4. **Create integrity verification
   mechanisms**. Implement data validation steps in
   your pipeline to detect anomalies or unexpected changes. Use
   checksums, statistical analysis, or machine learning-based
   anomaly detection to identify potential data corruption.
   Store integrity verification results as part of your lineage
   tracking records.
5. **Document code and infrastructure
   changes**. Track changes to your code repositories
   and infrastructure configurations that affect the ML
   workflow. Use version control systems like Git integrated
   with
   [AWS CodeCommit](https://aws.amazon.com/codecommit/ "https://aws.amazon.com/codecommit/") to maintain a history of code changes, and
   [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") or
   [AWS CDK](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") to version your infrastructure as code.
6. **Implement end-to-end
   traceability**. Verify that your lineage tracking
   system can trace model predictions back to the original data
   sources used for training. Use
   [SageMaker AI
   MLflow Model Registry](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to catalog your models and
   associate them with their training data lineage. This
   enables you to understand exactly which data influenced
   specific model behaviors.
7. **Establish audit and
   compliance-aligned reporting**. Create automated
   reports that demonstrate data lineage for compliance-aligned
   purposes. Use
   [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") to visualize data lineage graphs and
   [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") to query lineage metadata for audit reports.
   Regularly review these reports to improve your adherence to
   your governance requirements.
8. **Implement foundation model
   tracking**. For foundation model workflows, track
   not only the data but also the foundation models used, their
   versions, and fine-tuning parameters. Use
   [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md") to document model
   characteristics and
   [Amazon SageMaker AI Model Dashboard](../../../sagemaker/latest/dg/model-dashboard.md "../../../sagemaker/latest/dg/model-dashboard.md") to monitor model
   performance. Implement comprehensive traceability features
   to document model provenance and usage.
9. **Track model input
   variations**. Maintain a record of input variations
   used with models, as these influence model outputs. Use
   [Amazon SageMaker AI MLflow tracking server](../../../sagemaker/latest/dg/mlflow-create-tracking-server.md "../../../sagemaker/latest/dg/mlflow-create-tracking-server.md") with enhanced MLflow
   3.0 capabilities to track different input variations and
   their effectiveness, treating inputs as critical components
   of your data lineage system. The managed MLflow service
   provides robust experiment management at scale for ML
   projects with comprehensive tracking of training runs, model
   versions, and associated metadata.

## Resources

**Related documents:**

- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [SageMaker AI
  MLflow Tracking Server](../../../sagemaker/latest/dg/mlflow-create-tracking-server.md "../../../sagemaker/latest/dg/mlflow-create-tracking-server.md")
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/")
- [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md")
- [Accelerating
  generative AI development with fully managed MLflow 3.0 on
  Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/ "https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")

**Related videos:**

- [How
  To Efficiently Manage ML experiments using Amazon SageMaker AI ML
  Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k "https://www.youtube.com/watch?v=3xkz_5HOP6k")
