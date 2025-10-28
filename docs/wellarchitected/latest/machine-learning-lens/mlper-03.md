# MLPER-03: Define relevant evaluation metrics

To validate and monitor model performance, establish numerical
metrics that directly relate to the KPIs. These KPIs are
established in the business goal identification phase. Evaluate
whether the performance metrics accurately reflect the business’
tolerance for the error. For instance, false positives might
lead to excessive maintenance costs in predictive maintenance
use cases. Numerical metrics, such as precision and recall,
would help differentiate the business requirements and be closer
aligned to business value. Consider developing custom metrics
that tune the model directly for the business objectives.
Examples of standard metrics for ML models include:

- Classification
  - Confusion matrix (precision, recall, accuracy, F1 score)
  - Receiver operating characteristic-area under curve
    (AUC)
  - Logarithmic loss (log-loss)

- Regression
  - Root mean square error (RMSE)
  - Mean absolute percentage error (MAPE)

## Implementation plan

- **Optimize business-related
  metrics** - Identify performance metrics relevant
  to use-case and model type. Implement the metric as a loss
  function or use the loss function included in
  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/"). Use
  [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to evaluate the metrics with
  consideration to the business use case to maximize
  business value. Track model and concept drift in real time
  with
  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/")
  [Model
  Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/") to estimate errors.

      + Calculate the maximum probability of error that will
       be required for the ML model to produce results
       considering the tolerance set by the business.
      + Select and train ML models on the available data to
       make prediction within the probability bounds.
       Organize tests on different models with Amazon SageMaker AI Experiments.

## Documents

- [Monitor
  and Analyze Training Jobs Using Metrics](../../../sagemaker/latest/dg/training-metrics.md "../../../sagemaker/latest/dg/training-metrics.md")
- [Manage
  Machine Learning with Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md")

## Blogs

- [Training
  models with unequal economic error costs using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/training-models-with-unequal-economic-error-costs-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/training-models-with-unequal-economic-error-costs-using-amazon-sagemaker/")
- [Amazon SageMaker AI Experiments – Organize, Track, and Compare Your
  Machine Learning Trainings](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/")

## Videos

- [Organize,
  Track, and Evaluate ML Training Runs with Amazon SageMaker AI
  Experiments](https://www.youtube.com/watch?v=zLOMYKZGxK0 "https://www.youtube.com/watch?v=zLOMYKZGxK0")

## Examples

- [Scikit-Learn
  Data Processing and Model Evaluation](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation")
