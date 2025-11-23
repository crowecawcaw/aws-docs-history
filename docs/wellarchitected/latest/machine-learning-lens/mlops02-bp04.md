# MLOPS02-BP04 Establish a lineage tracker system

Maintain a system that tracks changes for each release to enable
reproducibility, speed up problem diagnosis, and improve regulatory
adherence. Tracking lineage for model development includes changes
in documentation, environment, model, data, code, and
infrastructure.

**Desired outcome:** You have a
comprehensive lineage tracking system that records the history of
artifacts involved in your ML model development and deployment
lifecycle. This system enables you to reproduce previous model
versions, diagnose issues quickly, roll back to stable versions when
needed, and improve your regulatory adherence. Your organization can
trace model results back to their originating data sources, code
versions, and infrastructure configurations.

**Common anti-patterns:**

- Manually tracking changes in spreadsheets or documents.
- Not capturing all dependent artifacts necessary for model
  reproduction.
- Inconsistent tracking practices across teams.
- Lacking integration between different components of the ML
  pipeline.
- Failing to track infrastructure and environment configurations.

**Benefits of establishing this best
practice:**

- Enables reproducibility of model versions for debugging.
- Accelerates problem diagnosis and resolution when issues arise.
- Supports regulatory adherence and audit requirements.
- Facilitates rollback to previous stable versions when needed.
- Improves collaboration among team members with transparent
  tracking.
- Enhances model governance and responsible AI practices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing a comprehensive lineage tracker system is essential
for maintaining the traceability and reproducibility of your
machine learning models. Without proper lineage tracking, your
organization may struggle to debug issues, comply with
regulations, or reproduce previous model versions when needed. The
lineage tracker should capture information about components that
influence your model's behavior, including the data used for
training, preprocessing steps, hyperparameters, model
architecture, evaluation metrics, and deployment environment.

A robust lineage tracking system starts with identifying the key
artifacts that need to be tracked throughout the ML lifecycle.
Once identified, you can use AWS services like SageMaker AI ML
Lineage Tracking to automatically record and store the
relationships between these artifacts. This information becomes
invaluable when you need to audit your models, reproduce results,
or diagnose issues in production.

For example, if a model suddenly begins producing unexpected
results in production, your lineage tracking system should allow
you to trace back to the exact version of the model, the data it
was trained on, the code used to train it, and the infrastructure
configuration at the time of deployment. This comprehensive
tracking enables faster problem resolution and maintains trust in
your ML systems.

### Implementation steps

1. **Identify artifacts needed for
   tracking**. Begin by identifying artifacts that
   contribute to your model's development and deployment. This
   includes raw data, processed data, feature sets, model
   parameters, code versions, training environments, and
   deployment configurations. Understanding what needs to be
   tracked is essential for meeting regulatory requirements and
   enabling reproducibility. Refer to
   [Data
   and artifacts lineage tracking](../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md") for guidance on the
   artifacts to include.
2. **Implement SageMaker AI ML Lineage
   Tracking**. Use
   [Amazon SageMaker AI ML Lineage Tracking](../../../sagemaker/latest/dg/lineage-tracking-entities.md "../../../sagemaker/latest/dg/lineage-tracking-entities.md") to automatically record
   information about the steps in your ML workflow. SageMaker AI
   tracks relationships between datasets, algorithms, training
   jobs, and model artifacts, enabling you to reproduce
   workflows, track model and dataset lineage, and establish
   governance standards. The service creates entities for your
   ML workflow components and stores their relationships,
   making it more straightforward to audit and verify model
   provenance.
3. **Set up SageMaker AI Unified
   Studio**. Use
   [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/") as your integrated
   development environment that unifies data and AI workflows.
   SageMaker AI Unified Studio provides enhanced collaborative
   features, team sharing capabilities, and visual tools to
   track the lineage of your ML pipelines, making it more
   straightforward to understand the relationships between
   different components across data and AI personas.
4. **Configure SageMaker AI Feature
   Store**. Implement
   [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") to create a centralized
   repository for storing, sharing, and managing features with
   enhanced feature management capabilities. This purpose-built
   repository enables you to organize features in a consistent
   way, making them easily accessible across teams. SageMaker AI
   Feature Store fosters feature consistency between training
   and inference phases without requiring additional code, and
   maintains a record of feature versions over time.
5. **Use SageMaker AI Model
   Registry**. Implement
   [Amazon SageMaker AI Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") to catalog models for
   production, manage model versions, and associate metadata
   with models. The Model Registry enables lineage tracking by
   maintaining a history of model versions, approval status,
   and deployment details. This creates a centralized
   repository for managing model lifecycles, which facilitates
   governance and improves adherence to regulations.
6. **Build ML pipelines with SageMaker AI
   Pipelines**. Create reproducible ML workflows using
   [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") to automate and standardize the
   steps in your ML process. SageMaker AI Pipelines allows you to
   track data history within the pipeline and integrates with
   SageMaker AI ML Lineage Tracking to analyze input data, its
   sources, and generated outputs. This integration creates
   comprehensive lineage tracking across your entire ML
   workflow.
7. **Implement version control
   practices**. Use version control systems like Git
   for code, model configurations, and pipeline definitions.
   Integrate these systems with your lineage tracking to
   properly link code changes to model versions and training
   runs. This practice maintains a complete history of how your
   models have evolved over time.
8. **Establish model attributes for
   training runs**. Use model attributes in SageMaker AI
   to track specific details about your training runs. This
   allows you to compare different experiments, understand
   which parameters led to better model performance, and
   maintain records of training decisions. For more detail, see
   [Using
   model attributes to track your training runs on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/").
9. **Implement access controls and
   auditing**. Set up appropriate access controls for
   your lineage data and implement auditing capabilities to
   track who accesses or modifies lineage information. Use
   [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/") with SageMaker AI Studio to control and
   audit data exploration activities, as demonstrated in this
   [example](https://github.com/aws-samples/amazon-sagemaker-studio-audit "https://github.com/aws-samples/amazon-sagemaker-studio-audit").
10. **Develop regular verification
    processes**. Establish procedures to regularly
    verify that your lineage tracking system is capturing
    necessary information for compliance-aligned purposes.
    Create automated reports that demonstrate the completeness
    of your lineage tracking to adhere to regulatory
    requirements.
11. **Foundation model lineage
    tracking**. Consider implementing
    [Amazon
    Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") for tracking lineage in generative AI
    applications. With foundation models becoming increasingly
    important, tracking prompt engineering changes, model
    parameters, and fine-tuning datasets is critical for
    reproducibility and governance of generative AI systems. Use
    Amazon Bedrock's governance features to maintain
    comprehensive lineage tracking when working with foundation
    models.

## Resources

**Related documents:**

- [Lineage
  Tracking Entities](../../../sagemaker/latest/dg/lineage-tracking-entities.md "../../../sagemaker/latest/dg/lineage-tracking-entities.md")
- [Track
  the lineage of a pipeline](../../../sagemaker/latest/dg/pipelines-lineage-tracking.md "../../../sagemaker/latest/dg/pipelines-lineage-tracking.md")
- [MLOps
  Automation With SageMaker AI Projects](../../../sagemaker/latest/dg/sagemaker-projects.md "../../../sagemaker/latest/dg/sagemaker-projects.md")
- [Data
  and artifacts lineage tracking](../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.md")
- [Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Create,
  store, and share features with Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")

**Related examples:**

- [End-to-End
  MLOps with Amazon SageMaker AI](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop "https://github.com/aws-samples/amazon-sagemaker-mlops-workshop")
- [Controlling
  and auditing data exploration activities with SageMaker AI Studio
  and AWS Lake Formation](https://github.com/aws-samples/amazon-sagemaker-studio-audit "https://github.com/aws-samples/amazon-sagemaker-studio-audit")
- [SageMaker AI
  Feature Store Examples](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore")
