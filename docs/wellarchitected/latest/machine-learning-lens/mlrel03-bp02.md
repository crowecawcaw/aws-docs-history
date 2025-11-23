# MLREL03-BP02 Verify feature consistency across training and

inference

Provide consistent, scalable, and highly available features between
training and inference using a feature storage. This results in
reducing the training-serving skew by keeping feature consistency
between training and inference.

**Desired outcome:** You create a
centralized feature repository where feature definitions are stored,
versioned, and shared across your organization. This makes the same
features used during model training consistently available during
inference, which reduces training-serving skew. You can discover,
reuse, and share features across different ML projects, reducing
duplicate work and standardizing feature engineering practices.

**Common anti-patterns:**

- Recreating feature transformations separately for training and
  inference pipelines.
- Storing features in different formats or locations for training
  versus production.
- Lack of versioning for features, leading to inconsistencies when
  models are updated.
- Duplicating feature engineering work across different teams or
  projects.
- Using non-standardized approaches to feature storage and
  retrieval.

**Benefits of establishing this best
practice:**

- Reduces training-serving skew, leading to more reliable model
  performance in production.
- Increases developer productivity through feature reusability.
- Standardizes feature definitions across the organization.
- Improves model governance and auditability through feature
  versioning.
- Saves costs by avoiding redundant feature computation and
  storage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Feature consistency between training and inference is critical for
machine learning system reliability. When the features used to
train a model differ from those used during inference, model
performance can degrade, a problem known as training-serving skew.
To avoid this issue, you need a centralized feature repository
that provides consistent access to the same feature definitions
and transformations across both training and inference
environments.

A feature store serves as this centralized repository, enabling
you to define, store, and retrieve features consistently. It
provides mechanisms for versioning features, which verifies that
you can maintain compatibility between models and the features
they expect as your data and feature engineering processes evolve.
Additionally, a feature store allows for the sharing and reuse of
features across multiple ML projects, increasing efficiency and
standardizing feature engineering practices across your
organization.

### Implementation steps

1. **Set up Amazon SageMaker AI Feature
   Store**. Create and configure a
   [SageMaker AI
   Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") to serve as your centralized repository
   for ML features. SageMaker AI Feature Store provides both
   online and offline storage capabilities: the online store
   supports low-latency, real-time inference use cases, while
   the offline store supports training and batch inference
   processes. Create a feature group that defines your feature
   structure, data types, and storage configurations using the
   SageMaker AI SDK or console.
2. **Define feature groups and
   schemas**. Organize your features into logical
   groups based on business domains, data sources, or ML use
   cases. Define schemas for your features, including data
   types, descriptions, and metadata. This organization makes
   features more discoverable and more straightforward to
   manage across your organization.
3. **Implement feature ingestion
   pipelines**. Build automated pipelines to ingest
   and process raw data into features. Use
   [SageMaker AI
   Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md"),
   [AWS Glue](https://aws.amazon.com/glue/ "https://aws.amazon.com/glue/"), or
   [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") to transform raw data into feature values.
   Configure both batch ingestion for historical data and
   streaming ingestion for real-time updates using services
   like
   [Amazon Kinesis](https://aws.amazon.com/kinesis/ "https://aws.amazon.com/kinesis/") with SageMaker AI Feature Store.
4. **Develop feature retrieval
   mechanisms**. Create standardized ways to retrieve
   features for both training and inference. For training
   datasets, implement code that pulls features from the
   offline store, while for inference, develop services that
   query the online store. Verify that both paths use the same
   feature definitions and transformations.
5. **Integrate with ML
   workflows**. Connect your feature store to your ML
   pipelines by integrating it with
   [SageMaker AI
   Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/") or your custom ML workflows. This makes
   feature retrieval consistent throughout the ML lifecycle,
   from experimentation to production deployment.
6. **Monitor and validate
   features**. Implement monitoring for your feature
   store to detect data drift, missing values, or other quality
   issues. Use
   [SageMaker AI
   Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") or custom validation scripts for
   feature consistency and quality over time. Set up alerts for
   deviations in feature distributions.
7. **Enable feature discovery and
   sharing**. Document your features with metadata and
   descriptions to make them discoverable across your
   organization. Integrate with data catalogs like
   [AWSAWS Glue Data Catalog](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") to enhance discoverability and
   governance of features.

## Resources

**Related documents:**

- [Get
  started with Amazon SageMaker AI Feature Store](../../../sagemaker/latest/dg/feature-store-getting-started.md "../../../sagemaker/latest/dg/feature-store-getting-started.md")
- [Feature
  Store concepts](../../../sagemaker/latest/dg/feature-store-concepts.md "../../../sagemaker/latest/dg/feature-store-concepts.md")
- [Store,
  Discover, and Share Machine Learning Features with Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/ "https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/")
- [Unlock
  ML insights using the Amazon SageMaker AI Feature Store Feature
  Processor](https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/ "https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/")

**Related videos:**

- [Amazon SageMaker AI Feature Store: Store, discover, & share features
  for ML apps](https://www.youtube.com/watch?v=pEg5c6d4etI "https://www.youtube.com/watch?v=pEg5c6d4etI")
- [Deep
  dive on Amazon SageMaker AI Feature Store](https://www.youtube.com/watch?v=mHEUlPFT6xg "https://www.youtube.com/watch?v=mHEUlPFT6xg")

**Related examples:**

- [Introduction
  to Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html")
- [Amazon SageMaker AI Feature Store SageMaker AI Examples](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore")
- [Amazon SageMaker AI Feature Store: Streaming Aggregation](https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation "https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation")
