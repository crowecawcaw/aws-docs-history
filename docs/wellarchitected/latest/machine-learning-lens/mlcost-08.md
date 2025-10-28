# MLCOST-08: Enable feature reusability

Reduce duplication and the rerunning of feature engineering code
across teams and projects by using feature storage. The store
should have online and oﬄine storage, and data encryption
capabilities. An online store with low-latency retrieval
capabilities is ideal for real-time inference. An oﬄine store
maintains a history of feature values and is suited for training
and batch scoring.

## Implementation plan

- **Use Amazon SageMaker AI Feature
  Store** -
  [Amazon SageMaker AI Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md") is a fully managed,
  purpose-built repository to store, update, retrieve, and
  share ML features. Feature Store makes it easy for data
  scientists, machine learning engineers, and general
  practitioners to create, share, and manage features for ML
  development. The online store is used for low latency,
  real-time inference use cases. The oﬄine store is used for
  training and batch inference. The Feature Store reduces
  the repetitive data processing and curation work required
  to convert raw data into features for training an ML
  algorithm.

You can use Feature Store in the following modes:

- **Online** - Features are
  read with low latency reads (milliseconds) and used for
  high throughput predictions.
- **Oﬄine** - Large streams
  of data are fed to an oﬄine store, which is used for
  training and batch inference. This mode requires a feature
  group to be stored in an oﬄine store. The oﬄine store uses
  your S3 bucket for storage and can also fetch data using
  Amazon Athena queries.
- **Online and oﬄine** - This
  includes both online and oﬄine modes.

## Documents

- [Create,
  Store, and Share Features with Amazon SageMaker AI Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")

## Blogs

- [Getting
  started with Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-sagemaker-feature-store/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-amazon-sagemaker-feature-store/")
- [Store,
  Discover, and Share Machine Learning Features with Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/aws/new-store-discover-and-share-machine-learning-features-with-amazon-sagemaker-feature-store/ "https://aws.amazon.com/blogs/aws/new-store-discover-and-share-machine-learning-features-with-amazon-sagemaker-feature-store/")
- [Enable
  feature reuse across accounts and teams using Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/enable-feature-reuse-across-accounts-and-teams-using-amazon-sagemaker-feature-store/ "https://aws.amazon.com/blogs/machine-learning/enable-feature-reuse-across-accounts-and-teams-using-amazon-sagemaker-feature-store/")
- [Understanding
  the key capabilities of Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/understanding-the-key-capabilities-of-amazon-sagemaker-feature-store/ "https://aws.amazon.com/blogs/machine-learning/understanding-the-key-capabilities-of-amazon-sagemaker-feature-store/")
- [Using
  Amazon SageMaker AI Feature Store with streaming feature aggregation](https://aws.amazon.com/blogs/machine-learning/using-streaming-ingestion-with-amazon-sagemaker-feature-store-to-make-ml-backed-decisions-in-near-real-time/ "https://aws.amazon.com/blogs/machine-learning/using-streaming-ingestion-with-amazon-sagemaker-feature-store-to-make-ml-backed-decisions-in-near-real-time/")
- [Extend
  model lineage to include ML features using Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/extend-model-lineage-to-include-ml-features-using-amazon-sagemaker-feature-store/ "https://aws.amazon.com/blogs/machine-learning/extend-model-lineage-to-include-ml-features-using-amazon-sagemaker-feature-store/")

## Videos

- [Amazon SageMaker AI Feature Store Deep Dive Demo](https://www.youtube.com/watch?v=mHEUlPFT6xg "https://www.youtube.com/watch?v=mHEUlPFT6xg")

## Examples

- [Using
  Amazon SageMaker AI Feature Store with streaming feature
  aggregation](https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation "https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation")
- [Amazon SageMaker AI Feature Store Notebook Examples](../../../sagemaker/latest/dg/feature-store-notebooks.md "../../../sagemaker/latest/dg/feature-store-notebooks.md")
