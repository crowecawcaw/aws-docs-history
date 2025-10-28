# MLPER-09: Perform a performance trade-off analysis

Perform alternative trade-off analysis to obtain optimal
performance and accuracy for a given use-case data and business
requirement.

- **Accuracy versus complexity
  trade-off**: The simpler a machine learning model
  is, the more explainable are its predictions. Deep learning
  predictions can potentially outperform linear regression or
  a decision tree algorithm, but at the cost of added
  complexity in interpretability and explainability.
- **Bias versus fairness
  trade-off**: Define a process for managing risks of
  bias and fairness in model performance. Business value most
  often aligns with models that have considered historical
  or sampling biases in the training data. Further
  consideration should be given to the disparate impact of
  inaccurate model predictions. For example, underrepresented
  groups are often more impacted by historical biases, which
  might perpetuate unfair practices.
- **Bias versus variance trade-off
  (supervised ML):** The goal is to achieve a trained
  model with the lowest bias versus variance tradeoff for a
  given data set. To help overcome bias and variance errors,
  you can use:
  - Cross validation
  - More data
  - Regularization
  - Simpler models
  - Dimension reduction (Principal Component Analysis)
  - Stop training early

- **Precision versus recall trade-off
  (supervised ML):** This analysis can be important
  when precision is more important than recall or vice versa.
  For example, optimization of precision is more important
  when the goal is to reduce false positives. However,
  optimization of recall is more important when the goal is to
  reduce false negatives. It’s not possible to have both high
  precision and high recall-if one is increased, the other
  decreases. A trade-off analysis helps identify the optimal
  option for analysis.

## Implementation plan

**Construct alternate workflows to
optimize all aspects of business value** - Complex
models can deliver high accuracy. If the business requirements
include low-latency, then the model might need to be simplified
with lower complexity. Identify how trade-offs affect accuracy
and the latency of inferences. Test these trade-offs using
[Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to keep track of each model type.
[Amazon SageMaker AIClarify](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md") provides explanations of the data,
models, and monitoring used to assess predictions. It can
measure biases during each stage of the ML lifecycle. Provided
explanations will help understanding how fairness affects the
business use case. Complex ML models can be slower to return
an inference and more difficult to deploy at the edge.
[Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/ "https://aws.amazon.com/sagemaker/neo/") enables developers to optimize ML models
for inference on SageMaker AI in the cloud and supported devices
at the edge.

## Documents

- [Evaluating
  ML Models](../../../machine-learning/latest/dg/evaluating_models.md "../../../machine-learning/latest/dg/evaluating_models.md")
- [AI
  Fairness and Explainability Whitepaper](https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf")
- [Optimize
  model performance using Amazon SageMaker AI Neo](../../../sagemaker/latest/dg/neo.md "../../../sagemaker/latest/dg/neo.md")

## Blogs

- [Amazon SageMaker AI Experiments – Organize, Track And Compare Your
  Machine Learning Trainings](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/")
- [Amazon SageMaker AI Clarify Detects Bias and Increases the
  Transparency of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/ "https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/")
- [Unlock
  near 3x performance gains with XGBoost and Amazon SageMaker AI Neo](https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/ "https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/")

## Videos

- [Machine
  learning and society: Bias, fairness, and
  explainability](https://www.youtube.com/watch?v=fme7fnIF-ls "https://www.youtube.com/watch?v=fme7fnIF-ls")
