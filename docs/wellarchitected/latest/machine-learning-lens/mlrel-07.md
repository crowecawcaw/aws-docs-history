# MLREL-07: Ensure feature consistency across training and inference

Ensure consistent, scalable, and highly available features
between training and inference using a feature storage. This
results in reducing the training-serving skew by keeping feature
consistency between training and inference.

## Implementation plan

- **Use Amazon SageMaker AI Feature
  Store** -Create, share, and manage features for
  ML development using
  [SageMaker AI
  Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/"). The Feature Store is a centralized
  store for features and associated metadata so features can
  be easily discovered and reused. The online store is used
  for low latency, real-time inference use cases. The oﬄine
  store is used for training and batch inference. The
  Feature Store reduces the repetitive data processing and
  curation work required to convert raw data into features
  for training an ML algorithm. Features generated will be
  used for both training and inference, reducing the
  training-serving skew. The Feature Store enables feature
  consistency, feature standardization, and the ability to
  integrate with
  [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/ "https://aws.amazon.com/sagemaker/pipelines/").

## Documents

- [Get
  started with Amazon SageMaker AIFeature Store](../../../sagemaker/latest/dg/feature-store-getting-started.md "../../../sagemaker/latest/dg/feature-store-getting-started.md")

## Blogs

- [Store,
  Discover, and Share Machine Learning Features with Amazon SageMaker AIFeature Store](https://aws.amazon.com/blogs/aws/new-store-discover-and-share-machine-learning-features-with-amazon-sagemaker-feature-store/ "https://aws.amazon.com/blogs/aws/new-store-discover-and-share-machine-learning-features-with-amazon-sagemaker-feature-store/")
- [Using
  streaming ingestion with Amazon SageMaker AIFeature Store to
  make ML-backed decisions in](https://aws.amazon.com/blogs/machine-learning/using-streaming-ingestion-with-amazon-sagemaker-feature-store-to-make-ml-backed-decisions-in-near-real-time/ "https://aws.amazon.com/blogs/machine-learning/using-streaming-ingestion-with-amazon-sagemaker-feature-store-to-make-ml-backed-decisions-in-near-real-time/")
  [near-real
  time](https://aws.amazon.com/blogs/machine-learning/using-streaming-ingestion-with-amazon-sagemaker-feature-store-to-make-ml-backed-decisions-in-near-real-time/ "https://aws.amazon.com/blogs/machine-learning/using-streaming-ingestion-with-amazon-sagemaker-feature-store-to-make-ml-backed-decisions-in-near-real-time/")

## Videos

- [AWS re:Invent 2020: Amazon SageMaker AIFeature Store: Store,
  discover, & share features for ML apps](https://www.youtube.com/watch?v=pEg5c6d4etI "https://www.youtube.com/watch?v=pEg5c6d4etI")
- [Introducing
  Amazon SageMaker AI Feature Store - AWS re:Invent2020](https://www.youtube.com/watch?v=-ydEYWhYlYw "https://www.youtube.com/watch?v=-ydEYWhYlYw")

## Examples

- [Amazon SageMaker AI Feature Store: Introduction to Feature
  Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html")
- [Amazon SageMaker AI Feature Store](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore")
- [Amazon SageMaker AI Feature Store Introduction](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-featurestore/feature_store_introduction.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker-featurestore/feature_store_introduction.ipynb")
- [Amazon SageMaker AI Feature Store: Streaming Aggregation](https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation "https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation")
