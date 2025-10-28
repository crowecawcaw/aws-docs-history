# MLOE-08: Establish feedback loops across ML lifecycle phases

Establish a feedback mechanism to share and communicate
successful development experiments, analysis of failures, and
operational activities. This facilitates continuous improvement
on future iterations of the ML workload. ML feedback loops are
driven by model drifts and requires ML practitioners to analyze
and revisit monitoring and retraining strategies over time. ML
feedback loops allow experimentation with data augmentation, and
different algorithms and training approaches until an optimal
outcome is achieved. Document your findings to identify key
learnings and improve processes over time.

## Implementation plan

- **Establish SageMaker AI Model
  Monitoring** - The accuracy of ML models can
  deteriorate over time, a phenomenon known as model drift.
  Many factors can cause model drift, such as changes in
  model features. The accuracy of ML models can also be
  affected by concept drift, the difference between data
  used to train models and data used during inference.
  [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") continually monitors
  machine learning models for concept drift and model drift.
  SageMaker AI Model Monitor alerts you if there are any
  deviations so that you can take remedial action.
  - **Use Amazon CloudWatch** - Configure
    [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to receive notifications if a drift
    in model quality is observed. Monitoring jobs can be
    scheduled to run at a regular cadence (for example,
    hourly or daily) and push reports as well as metrics
    to
    [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") and
    [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/").
  - **Use Amazon SageMaker AI Model
    Dashboard** as the central interface to track
    models, monitor performance, and review historical
    behavior
  - **Automate retraining
    pipelines** - Create a
    [CloudWatch Events](../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md "../../../AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.md") rule that alerts on a events emitted by
    the SageMaker AI Model Monitoring system. The event rule
    can detect the drifts or anomalies, and start a
    retraining pipeline.

- **Use Amazon Augmented AI
  (A2I)** - Check accuracy by having human reviews
  to establish the _ground truth_, using
  tools such as
  [Amazon
  A2I](https://aws.amazon.com/augmented-ai/ "https://aws.amazon.com/augmented-ai/"), against which model performance can be
  compared.

## Documents

- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Creating
  a CloudWatch Events Rule That Triggers on an Event](../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md "../../../AmazonCloudWatch/latest/events/Create-CloudWatch-Events-Rule.md")
- SageMaker AI
  [Model
  Dashboard](../../../sagemaker/latest/dg/model-dashboard.md "../../../sagemaker/latest/dg/model-dashboard.md")
- [Monitoring
  Amazon ML with Amazon CloudWatch Metrics](../../../machine-learning/latest/dg/cw-doc.md "../../../machine-learning/latest/dg/cw-doc.md")

## Blogs

- [Automated
  monitoring of your machine learning models with Amazon SageMaker AIModel Monitor and sending predictions to human
  review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/")
- [Automating
  model retraining and deployment using the AWS Step Functions Data Science SDK for](https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/")
  [Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/automating-model-retraining-and-deployment-using-the-aws-step-functions-data-science-sdk-for-amazon-sagemaker/")
- [Monitoring
  in-production ML models at large scale using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")
- [Human-in-the-loop
  review of model explanations with Amazon SageMaker AI Clarify
  and Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/")
- [Amazon SageMaker AI Model Monitor now supports new capabilities to
  maintain model quality in](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-sagemaker-model-monitor-supports-capabilities-to-maintain-model-quality-production/ "https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-sagemaker-model-monitor-supports-capabilities-to-maintain-model-quality-production/")
  [production](https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-sagemaker-model-monitor-supports-capabilities-to-maintain-model-quality-production/ "https://aws.amazon.com/about-aws/whats-new/2020/12/amazon-sagemaker-model-monitor-supports-capabilities-to-maintain-model-quality-production/")

## Videos

- [Easily
  Implement Human in the Loop into Your Machine Learning
  Predictions with Amazon A2I](https://www.youtube.com/watch?v=jNUp1SO_0YU "https://www.youtube.com/watch?v=jNUp1SO_0YU")
