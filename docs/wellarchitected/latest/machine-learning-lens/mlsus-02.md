# MLSUS-02: Consider AI services and pre-trained models

Consider whether the workload needs to be developed as a custom
model. Many workloads can use managed AI services accessible
through an API. Using these services means that you won’t need
to provision your own resources to collect, store, and process
training data and to prepare, train, tune, and deploy an ML
model.

If adopting a fully managed AI service is not appropriate,
evaluate if you can use pre-existing datasets, algorithms, or
models. You can also fine-tune an existing model starting from a
pre-trained model. Using pre-trained models from third parties
can reduce the resources needed for data preparation and model
training.

## Implementation plan

- **Use pre-trained AWS AI
  services** -
  [AWS AI services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/") integrate with applications through
  APIs to address common use cases such as personalized
  recommendations, image recognition, language analysis and
  translation, modernizing contact centers, improving safety
  and security, and increasing customer engagement.
- **Use pre-trained models from AWS Marketplace** -
  [AWS Marketplace](https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1 "https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1") offers over 1,400 ML-related assets
  that you can subscribe to.
- **Use pre-trained models from
  SageMaker AI JumpStart** - [SageMaker AI JumpStart](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
  provides pre-trained, open-source models for a
  wide range of problem types to help you get started with
  machine learning. You can incrementally train and tune
  these models before deployment.

## Documents

- [Explore
  AWS AI services](https://aws.amazon.com/machine-learning/ai-services/ "https://aws.amazon.com/machine-learning/ai-services/")
- [Pre-trained
  machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models "https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models")
- [Use
  Hugging Face with Amazon SageMaker AI](../../../sagemaker/latest/dg/hugging-face.md "../../../sagemaker/latest/dg/hugging-face.md")
- [Use
  SageMaker AI JumpStart algorithms with pre-trained
  models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 1, identify
  business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/")
- [Fine-tune
  and host Hugging Face BERT models on Amazon SageMaker AI](https://aws.amazon.com/fr/blogs/machine-learning/fine-tune-and-host-hugging-face-bert-models-on-amazon-sagemaker/ "https://aws.amazon.com/fr/blogs/machine-learning/fine-tune-and-host-hugging-face-bert-models-on-amazon-sagemaker/")

## Videos

- [Introduction
  to Hugging Face on Amazon SageMaker AI](https://www.youtube.com/watch?v=80ix-IyNnQI "https://www.youtube.com/watch?v=80ix-IyNnQI")
