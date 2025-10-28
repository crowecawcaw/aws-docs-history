# MLOE-15: Enable model observability and tracking

Establish model monitoring mechanisms to identify and
proactively avoid any inference issues. ML models can degrade
in performance over time due to drifts. Monitor metrics that
are attributed to your model’s performance. For real time
inference endpoints, measure the operational health of the
underlying compute resources hosting the endpoint and the
health of endpoint responses. Establish lineage to trace
hosted models back to versioned inputs and model artifacts for
analysis.

## Implementation plan

- **Use Amazon SageMaker AI Model
  Monitor** - Continually monitor the quality of
  Amazon SageMaker AI ML models in production and compare
  with the results from training using
  [SageMaker AI
  Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md").
- **Use Amazon CloudWatch**

* Amazon SageMaker AI Model Monitor automatically sends
  metrics to
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") so that you can gather and analyze
  usage statistics for your ML models.

- **Use SageMaker AI Model
  Dashboard** - View, search, and explore your
  models in a centralized portal from the SageMaker AI
  console. Set up monitors with
  [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") and track the performance
  of your models that are hosted on real-time inference
  endpoints. Find models that violate thresholds you have
  set for data quality, model quality, bias, and
  explainability
- **Use Amazon SageMaker AI
  Clarify** - Identify various types of bias that
  can emerge during model training or when the model is in
  production. This helps improve your ML models by
  detecting potential bias and helping explain the
  predictions that the models make.
  [SageMaker AI
  Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") helps explain how these models make
  predictions using a feature attribution approach. It
  also monitors inferences that the models make in
  production for bias drift or feature attribution drift.
  SageMaker AI Clarify provides tools to help you generate
  model governance reports that you can use to inform risk
  and compliance teams, and external regulators.
- **Track your model pipeline with
  SageMaker AI ML lineage Tracking** – Lineage
  tracking creates and stores information about the steps
  of a machine learning workflow from data preparation to
  model deployment. Keep a running history of model
  discovery experiments. Establish model governance by
  tracking model lineage artifacts for auditing and
  compliance verification.
- **Use SageMaker AI Model Cards to
  simplify model information gathering** –
  Documentation on model information, such as business
  requirements, key decisions, and observations during
  model development and evaluation, is required to support
  approval workflows, registration, audits, customer
  inquiries, and monitoring. Amazon SageMaker AI Model Cards
  provide a single location to store model information
  (for example, performance goals, and risk rating) and
  training and evaluation results (for example, bias or
  accuracy measurements) in the AWS Management Console,
  streamlining documentation throughout a model’s
  lifecycle.
- **Use the automated validation
  capability of Amazon SageMaker AI** – Amazon SageMaker AI Inference enables you to compare the
  performance of new models against production models,
  using the same real-world inference request data in real
  time. Amazon SageMaker AI can be used to route a copy of
  the inference requests received by the production model
  to the new model and generate a dashboard to display
  performance differences across key metrics in real time.

## Documents

- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Monitoring
  Amazon ML with Amazon CloudWatch Metrics](../../../machine-learning/latest/dg/cw-doc.md "../../../machine-learning/latest/dg/cw-doc.md")
- [How
  Amazon CloudWatch works](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.md")
- [Fairness, model explainability and bias detection with SageMaker Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [SageMaker AI
  Model Dashboard](../../../sagemaker/latest/dg/model-dashboard.md "../../../sagemaker/latest/dg/model-dashboard.md")
- [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md")
- [Amazon SageMaker AI Shadow Testing](https://aws.amazon.com/sagemaker/shadow-testing/ "https://aws.amazon.com/sagemaker/shadow-testing/")

## Blogs

- [Architect
  and build the full machine learning lifecycle with AWS:
  An end-to-end Amazon SageMaker AI demo](https://aws.amazon.com/blogs/machine-learning/architect-and-build-the-full-machine-learning-lifecycle-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/architect-and-build-the-full-machine-learning-lifecycle-with-amazon-sagemaker/")
- [Improve
  governance of your machine learning models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/improve-governance-of-your-machine-learning-models-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/improve-governance-of-your-machine-learning-models-with-amazon-sagemaker/")
- [New
  for Amazon SageMaker AI – Perform Shadow Tests to Compare
  Inference Performance Between ML Model Variants](https://aws.amazon.com/blogs/aws/new-for-amazon-sagemaker-perform-shadow-tests-to-compare-inference-performance-between-ml-model-variants/ "https://aws.amazon.com/blogs/aws/new-for-amazon-sagemaker-perform-shadow-tests-to-compare-inference-performance-between-ml-model-variants/")

## Videos

- [Introducing
  Amazon SageMaker AI Clarify, part 1 - Bias detection- AWS
  re:Invent 2020](https://youtu.be/jvcPZmnXaxo "https://youtu.be/jvcPZmnXaxo")
- [Introducing
  Amazon SageMaker AI Clarify, part 2 - Model explainability

* AWS re:Invent 2020](https://youtu.be/1IGMG_c280E "https://youtu.be/1IGMG_c280E")

- [AWS re:Invent 2020: Understand ML model predictions &
  biases with Amazon SageMaker AI Clarify](https://youtu.be/t2SJTYiTnYM "https://youtu.be/t2SJTYiTnYM")
- [AWS re:Invent 2022 - Minimizing the production impact of ML
  model updates with shadow testing](https://youtu.be/J1p0DvC-w1Q "https://youtu.be/J1p0DvC-w1Q")

## Examples

- [Fairness, model explainability and bias detection with SageMaker Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
