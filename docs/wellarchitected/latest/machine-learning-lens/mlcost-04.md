# MLCOST-04: Tradeoff analysis on custom versus pre-trained models

Optimize the cost through tradeoff analysis based on custom
versus pre-trained models. This tradeoff analysis should keep the
security and performance efficiency in perspective and within
the acceptable thresholds.

## Implementation plan

- **Use Amazon SageMaker AI built-in
  algorithms and AWS Marketplace** -
  [Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md") provides a suite of built-in algorithms
  to help data scientists and machine learning practitioners
  get started on training and deploying machine learning
  models. Pre-trained ML models are ready-to-use models that
  can be quickly deployed on Amazon SageMaker AI. By
  pre-training the ML models for you, solutions in the AWS Marketplace take care of the heavy lifting, helping you
  deliver AI- and ML-powered features faster and at a lower
  cost. Evaluate the cost of your data scientists’ time and
  other resource requirements to develop your own custom
  model vs. bringing a pre-trained model and deploying it on
  SageMaker AI for inferencing. The advantage of a custom model
  is the flexibility to fine-tune it to match the needs of
  your business use case. A pre-trained model can be
  difficult to modify and you might have to use it as is.
- **Use Amazon SageMaker AI
  Jumpstart** to access pre-trained models and
  accelerate the ML development process. SageMaker AI JumpStart
  provides a set of solutions for the most common use cases
  that can be deployed readily with just a few clicks. The
  solutions are fully customizable and showcase the use of
  AWS CloudFormation templates and reference architectures
  so you can accelerate your ML journey. Amazon SageMaker AI
  JumpStart also supports one-click deployment and
  fine-tuning of more than 150 popular open-source models
  such as natural language processing, object detection, and
  image classification models.

## Documents

- [Pre-trained
  machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models "https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models")
- [Amazon SageMaker AI Jumpstart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/")

## Blogs

- [Bring
  your own pre-trained MXNet or TensorFlow models into
  Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/bring-your-own-pre-trained-mxnet-or-tensorflow-models-into-amazon-sagemaker "https://aws.amazon.com/blogs/machine-learning/bring-your-own-pre-trained-mxnet-or-tensorflow-models-into-amazon-sagemaker")
- [How
  Startups Deploy Pretrained Models on Amazon SageMaker AI](https://aws.amazon.com/blogs/startups/how-startups-deploy-pretrained-models-on-amazon-sagemaker "https://aws.amazon.com/blogs/startups/how-startups-deploy-pretrained-models-on-amazon-sagemaker")
- [Amazon SageMaker AI JumpStart Simplifies Access to Pre-built Models
  and Machine Learning Solutions](https://aws.amazon.com/blogs/aws/amazon-sagemaker-jumpstart-simplifies-access-to-prebuilt-models-and-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-jumpstart-simplifies-access-to-prebuilt-models-and-machine-learning-models/")
- [Amazon SageMaker AI JumpStart models and algorithms now available
  via API](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-jumpstart-models-and-algorithms-now-available-via-api/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-jumpstart-models-and-algorithms-now-available-via-api/")
- [Machine
  Learning algorithms and model packages now available in
  AWS Marketplace](https://aws.amazon.com/blogs/aws/new-machine-learning-algorithms-and-model-packages-now-available-in-aws-marketplace/ "https://aws.amazon.com/blogs/aws/new-machine-learning-algorithms-and-model-packages-now-available-in-aws-marketplace/")
- [Using
  Amazon Augmented AI with AWS Marketplace machine learning
  models](https://aws.amazon.com/blogs/awsmarketplace/using-amazon-augmented-ai-with-aws-marketplace-machine-learning-models/ "https://aws.amazon.com/blogs/awsmarketplace/using-amazon-augmented-ai-with-aws-marketplace-machine-learning-models/")
- [Save costs by automatically shutting down idle resources within Amazon SageMaker AI Studio](https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/")
