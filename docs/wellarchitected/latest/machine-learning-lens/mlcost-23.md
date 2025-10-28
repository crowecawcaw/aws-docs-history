# MLCOST-23: Enable debugging and logging

Ensure that there are sufficient logs and metrics recorded to
capture the runtime and resource consumption. The collected logs
and metrics can be analyzed to identify the areas for
improvement. Monitor compute and data storage consumption.
Instrument the machine learning code, and use debugging tools to
capture metrics at runtime.

## Implementation plan

- **Use Amazon SageMaker AI
  Debugger** -
  [Amazon SageMaker AI Debugger](../../../sagemaker/latest/dg/train-debugger.md "../../../sagemaker/latest/dg/train-debugger.md") captures the state of a training
  job at periodic intervals. It provides visibility into the
  ML training process by monitoring, recording, and
  analyzing data with the ability to perform interactive
  exploration of data captured during training. The debugger
  has an alerting capability for errors detected during
  training. For example, it can automatically detect and
  alert you to commonly occurring errors, such as gradient
  values getting too large or too small.
- **Use Amazon CloudWatch**
  -Logs generated during training by Amazon SageMaker AI are
  logged to
  [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md"). Use an
  [AWS KMS key](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") to encrypt log data ingested by Amazon CloudWatch Logs.

## Documents

- [Logging
  and Monitoring](../../../sagemaker/latest/dg/sagemaker-incident-response.md "../../../sagemaker/latest/dg/sagemaker-incident-response.md")
- [Logging
  Amazon ML API Calls with AWS CloudTrail](../../../machine-learning/latest/dg/logging-using-cloudtrail.md "../../../machine-learning/latest/dg/logging-using-cloudtrail.md")
- [Amazon SageMaker AI Debugger - Setup and Use](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_debugger.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_debugger.html")

## Blogs

- [Build
  Your Own Log Analytics Solution on AWS](https://www.youtube.com/watch?v=isGPTlMaHLg "https://www.youtube.com/watch?v=isGPTlMaHLg")
- [Profile
  Your Machine Learning Training Jobs with Amazon SageMaker AI
  Debugger](https://aws.amazon.com/blogs/aws/profile-your-machine-learning-training-jobs-with-amazon-sagemaker-debugger/ "https://aws.amazon.com/blogs/aws/profile-your-machine-learning-training-jobs-with-amazon-sagemaker-debugger/")
- [Amazon SageMaker AI Debugger – Debug Your Machine Learning
  Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-debugger-debug-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-debugger-debug-your-machine-learning-models/")
- [ML
  Explainability with Amazon SageMaker AI Debugger](https://aws.amazon.com/blogs/machine-learning/ml-explainability-with-amazon-sagemaker-debugger/ "https://aws.amazon.com/blogs/machine-learning/ml-explainability-with-amazon-sagemaker-debugger/")
- [The
  science behind SageMaker AI’s cost-saving Debugger](https://www.amazon.science/blog/the-science-behind-sagemakers-cost-saving-debugger "https://www.amazon.science/blog/the-science-behind-sagemakers-cost-saving-debugger")

## Examples

- [Debugger
  example notebooks](../../../sagemaker/latest/dg/debugger-notebooks.md "../../../sagemaker/latest/dg/debugger-notebooks.md")

Video

- [Train
  ML models faster with better insights using Amazon SageMaker AI Debugger](https://www.youtube.com/watch?v=XPY-ZCzKEbI "https://www.youtube.com/watch?v=XPY-ZCzKEbI")
- [Debugging
  a Customer Churn Model Using SageMaker AI Debugger](https://www.youtube.com/watch?v=8b5-lyRaFgA "https://www.youtube.com/watch?v=8b5-lyRaFgA")
