# MLREL-08: Ensure model validation with relevant data

Put processes in place to include real and representative data
for testing and validation. Data that does not include all
possible patterns and scenarios will result in failures once
model is in production. Check for a _distribution
mismatch_ between training, validation, and test data
as well as the inference data.

## Implementation plan

- **Use Amazon SageMaker AI
  Experiments** - Your models should be tested and
  validated using data that is representative of what they
  will encounter in production. This data can include both
  real-world data and engineered data. You should account
  for all scenarios in your training data so that you can
  avoid errors when your model is deployed to production.
  Use
  [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to organize, track, compare,
  and evaluate your machine learning experiments.
- **Use Amazon SageMaker AI Model
  Monitor** - Consider implementing a plan to
  periodically test endpoints for deviations in model
  quality. Early detection of deviations can help you
  determine when to take corrective actions.
  [SageMaker AI
  Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") continually monitors the quality of
  Amazon SageMaker AI ML models in production. With Model
  Monitor, you can set alerts that notify you when there are
  deviations in the model quality.

## Blogs

- [Test
  data quality at scale with Deequ](https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/ "https://aws.amazon.com/blogs/big-data/test-data-quality-at-scale-with-deequ/")
- [Amazon SageMaker AI Model Monitor– Fully Managed Automatic
  Monitoring for Your Machine Learning](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
  [Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")

## Examples

- [Amazon SageMaker AI Model Monitor](https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.ipynb")
