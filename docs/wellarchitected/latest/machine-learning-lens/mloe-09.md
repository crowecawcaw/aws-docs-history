# MLOE-09: Review fairness and explainability

Consider fairness and explainability during each stage of the ML
lifecycle. Compile a list of questions to review for each stage
including:

- **Problem framing** - Is an
  algorithm an ethical solution to the problem?
- **Data management** - Is the
  training data representative of different groups? Are there
  biases in labels or features? Does the data need to be
  modified to mitigate bias?
- **Training and evaluation** -
  Do fairness constraints need to be included in the objective
  function? Does changing the number of models to train needed
  to mitigate bias? Has the model been evaluated using
  relevant fairness metrics?
- **Deployment** - Is the model
  deployed on a population for which it was not trained or
  evaluated?
- **Monitoring** - Are there
  unequal effects across users?

## Implementation plan

- **Use Amazon SageMaker AI
  Clarify** - Understand model characteristics,
  debug predictions, and explain how ML models make
  predictions with
  [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/"). Amazon SageMaker AI Clarify uses a
  model-agnostic feature attribution approach that includes
  an efficient implementation of
  [SHAP](../../../sagemaker/latest/dg/clarify-shapley-values.md "../../../sagemaker/latest/dg/clarify-shapley-values.md")
  (Shapley Additive Explanations). SageMaker AI Clarify allows
  you to:
  - Understand the compliance requirements for fairness
    and explainability.
  - Determine whether training data is biased in its
    classes or population segments, particularly protected
    groups.
  - Develop a strategy for monitoring for bias in data
    when the model is in production.
  - Consider the trade-offs between model complexity and
    explainability, and select simpler models if
    explainability is required.

## Documents

- [What
  Is Fairness and Model Explainability for Machine Learning
  Predictions?](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md")
- [Amazon SageMaker AI Clarify: Detect bias in ML models and understand
  model predictions](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/")
- [Feature
  Attributions that Use Shapley Values](../../../sagemaker/latest/dg/clarify-shapley-values.md "../../../sagemaker/latest/dg/clarify-shapley-values.md")
- [Amazon SageMaker AI Clarify: Machine Learning Bias Detection and
  Explainability in the Cloud](https://assets.amazon.science/45/76/30bab4f14ccab96cfe8067ed2b4a/amazon-sagemaker-clarify-machine-learning-bias-detection-and-explainability-in-the-cloud.pdf "https://assets.amazon.science/45/76/30bab4f14ccab96cfe8067ed2b4a/amazon-sagemaker-clarify-machine-learning-bias-detection-and-explainability-in-the-cloud.pdf")

## Blogs

- [ML
  model explainability with Amazon SageMaker AI Clarify and the
  SK Learn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/ "https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/")
- [Explaining
  Amazon SageMaker AI Autopilot models with SHAP](https://aws.amazon.com/blogs/machine-learning/explaining-amazon-sagemaker-autopilot-models-with-shap/ "https://aws.amazon.com/blogs/machine-learning/explaining-amazon-sagemaker-autopilot-models-with-shap/")

## Videos

- [Machine
  learning and society: Bias, fairness, and
  explainability](https://www.youtube.com/watch?v=fme7fnIF-ls "https://www.youtube.com/watch?v=fme7fnIF-ls")
- [How
  Clarify helps machine learning developers detect
  unintended bias](https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias "https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias")
- [Interpretability
  and explainability in machine learning](https://www.youtube.com/watch?v=EBQOaqhsnqM "https://www.youtube.com/watch?v=EBQOaqhsnqM")
