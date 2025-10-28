# MLPER-14: Evaluate data drift

Understand the effects of data drift on model performance. In
cases where the data has drifted, the model could generate
inaccurate predictions. Consider a strategy that monitors and
adapts to data drift through re-training.

## Implementation plan

- **Use Amazon SageMaker AI Model
  Monitor, and SageMaker AI Clarify**-
  [Amazon SageMaker AI Model](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/")
  [Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/")
  helps you maintain high-quality ML models by detecting
  model and concept drift in real time, and sending you
  alerts so you can take immediate action. Model and
  concept drift are detected by monitoring the quality of
  the model. Independent variables (also known as
  features) are the inputs to an ML model, and dependent
  variables are the outputs of the model. Additionally,
  SageMaker AI Model Monitor is integrated with
  [Amazon SageMaker AI Clarify](https://www.amazonaws.cn/en/sagemaker/clarify/ "https://www.amazonaws.cn/en/sagemaker/clarify/") to help you identify potential
  bias in your ML models.

## Documents

- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Amazon SageMaker AI Clarify - Model Explainability](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md")

## Blogs

- [Amazon SageMaker AI Clarify Detects Bias and Increases the
  Transparency of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/ "https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/")

## Videos

- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

## Examples

- [Amazon SageMaker AI Clarify](https://github.com/aws/amazon-sagemaker-clarify "https://github.com/aws/amazon-sagemaker-clarify")
