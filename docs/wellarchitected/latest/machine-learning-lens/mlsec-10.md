# MLSEC-10: Protect against data poisoning threats

Protect against data injection and data manipulation that
pollutes the training dataset. Data injections can add corrupt
training data that can result in incorrect model and outputs.
Data manipulations can change existing data (for example,
labels) that can result in inaccurate and weak predictive
models. Identify and address corrupt data and inaccurate models
using security methods and anomaly detection algorithms. Ensure
immutability of datasets by providing protection against
ransomware and malicious code in installed third-party packages.

## Implementation plan

- **Use only trusted data sources for
  training data** - Verify that you have sufficient
  audit controls to replay activity and determine where a
  change occurred, by whom, and at what time. Before
  training, validate the quality of training data to look
  for strong outliers and potentially incorrect labels.
- **Look for underlying shifts in the
  patterns and distributions in training data** -
  Using monitoring of data drift, derive the impact to
  prediction variance. These skews can be an indicator of
  underlying data drift, and can provide an early warning of
  unauthorized access targeting the training data.
- **Identify model updates that
  negatively impact the results before moving them to
  production** - Determine if the retrained model
  results are different from the past model iteration. Use
  past test data and previous model iterations as a
  baseline.
- **Have a rollback plan** -
  Using versioned training data and versioned models, make
  sure you can revert to a known good working model in a
  failure scenario. Use a fully managed service to store
  features, such as the
  [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store "https://aws.amazon.com/sagemaker/feature-store"). See more details of the
  Amazon SageMaker AI Feature Store under the Reliability
  pillar section (MLREL-07).
- **Use low-entropy classification
  cases** - Look for significant, unexpected
  changes. Determine the bounds of thresholds, identify
  classifications that you do not expect to see, and alert if
  the retrained model exceeds them.

## Documents

- [Monitor
  Bias Drift for models in production](../../../sagemaker/latest/dg/clarify-model-monitor-bias-drift.md "../../../sagemaker/latest/dg/clarify-model-monitor-bias-drift.md")
- [Amazon SageMaker AI model registry now supports rollback of deployed
  models](https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-sagemaker-model-registry-now-supports-rollback-of-deployed-models/ "https://aws.amazon.com/about-aws/whats-new/2021/05/amazon-sagemaker-model-registry-now-supports-rollback-of-deployed-models/")
- [SageMaker AI
  Model Registry - Approve](../../../sagemaker/latest/dg/model-registry-approve.md "../../../sagemaker/latest/dg/model-registry-approve.md")

## Blogs

- [Automated
  monitoring of your machine learning models with Amazon SageMaker AIModel Monitor and](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/")
  [sending
  predictions to human review workflows using Amazon
  A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/")
- [Amazon SageMaker AI Model Monitor– Fully Managed Automatic
  Monitoring for Your Machine Learning](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
  [Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
- [7
  ways to improve security of your machine learning
  workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")

## Videos

- [AWS re:Invent 2020: Detect machine learning (ML) model drift
  in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

## Examples

- [Inawisdom:
  Machine Learning and Automated Model Retraining with
  SageMaker AI](https://www.youtube.com/watch?v=1kbWvlHBYLk&t=7s "https://www.youtube.com/watch?v=1kbWvlHBYLk&t=7s")
