# MLPER-13: Evaluate model explainability

Evaluate model performance as constrained by the
explainability requirements of the business. Compliance
requirements, business objectives, or both might require that
the inferences from a model be directly explainable. Evaluate
the explainability needs, and the trade-off between
explainability and model complexity. Then select the model
type or evaluation metrics. This approach provides
transparency into the reasons that a particular inference was
attained given the input data.

## Implementation plan

- **Use Amazon SageMaker AI Clarify to
  explain model results** -
  [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") helps improve your ML models by
  detecting potential bias and helping explain the
  predictions that models make. It helps you identify
  various types of bias in data that can emerge during
  model training or in production. SageMaker AI Clarify helps
  explain how these models make predictions using a
  feature attribution approach. It also monitors
  inferences that the models make in production for bias
  or feature attribution drift. The fairness and
  explainability functions provided by SageMaker AI Clarify
  help you build less biased and more understandable
  machine learning models. It also provides tools to help
  you generate model governance reports that you can use
  to inform risk and compliance teams, and external
  regulators.

## Documents

- [Amazon SageMaker AI Clarify Model Explainability](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md")
- [Feature
  Attributions that Use Shapley Values](../../../sagemaker/latest/dg/clarify-shapley-values.md "../../../sagemaker/latest/dg/clarify-shapley-values.md")
- [Fairness, model explainability and bias detection with SageMaker Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")

## Blogs

- [ML
  model explainability with Amazon SageMaker AIClarify and
  the SKLearn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/ "https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/")
- [Explaining
  Amazon SageMaker AIAutopilot models with SHAP](https://aws.amazon.com/blogs/machine-learning/explaining-amazon-sagemaker-autopilot-models-with-shap/ "https://aws.amazon.com/blogs/machine-learning/explaining-amazon-sagemaker-autopilot-models-with-shap/")
- [Human-in-the-loop
  review of model explanations with Amazon SageMaker AIClarify and Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/")

## Videos

- [Interpretability
  and explainability in machine learning](https://www.youtube.com/watch?v=EBQOaqhsnqM "https://www.youtube.com/watch?v=EBQOaqhsnqM")
- [Explaining
  Credit Decisions with Amazon SageMaker AI](https://www.youtube.com/watch?v=Nlwz4cU68T8 "https://www.youtube.com/watch?v=Nlwz4cU68T8")

## Examples

- [Fairness, model explainability and bias detection with SageMaker Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [Explainability
  with Amazon SageMaker AI Debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html")
