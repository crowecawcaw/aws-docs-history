# MLREL-09: Establish data bias

detection and mitigation

Detect and mitigate bias to avoid inaccurate model results.
Establish bias detection methodologies at data preparation
stage before training starts. Monitor, detect, and mitigate
bias after the model is in production. Establish feedback
loops to track the drift over time and initiate a re-training.

## Implementation plan

- **Use Amazon SageMaker AI
  Clarify**-
  [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") helps improve your machine
  learning models by detecting potential bias and helping
  explain how these models make predictions. The fairness
  and explainability functionality provided by SageMaker AI
  Clarify takes a step towards enabling you to build
  trustworthy and understandable ML models. Clarify helps
  you with the following tasks:
  - Measure biases that can occur during each stage of the
    ML lifecycle. These stages include data collection,
    model training, model tuning, and model monitoring.
  - Generate model governance reports targeting risk and
    compliance teams and external regulators.
  - Provide explanations of the data, models, and
    monitoring used to assess predictions.

## Documents

- [Run
  SageMaker AI Clarify Processing Jobs for Bias Analysis and
  Explainability](../../../sagemaker/latest/dg/clarify-processing-job-run.md "../../../sagemaker/latest/dg/clarify-processing-job-run.md")

## Blogs

- [Amazon SageMaker AI Clarify Detects Bias and Increases the
  Transparency of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/ "https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/")

## Videos

- [Introducing
  Amazon SageMaker AIClarify, part 1 - Bias detection - AWS
  re:Invent2020](https://www.youtube.com/watch?v=jvcPZmnXaxo "https://www.youtube.com/watch?v=jvcPZmnXaxo")
- [Introducing
  Amazon SageMaker AIClarify, part 2 - Model explainability -
  AWS re:Invent2020](https://www.youtube.com/watch?v=1IGMG_c280E "https://www.youtube.com/watch?v=1IGMG_c280E")

## Examples

- [SageMaker AI
  Clarify](https://github.com/aws/amazon-sagemaker-clarify "https://github.com/aws/amazon-sagemaker-clarify")
