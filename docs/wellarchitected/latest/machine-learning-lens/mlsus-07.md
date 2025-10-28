# MLSUS-07: Define sustainable performance criteria

Make trade-offs between your model’s accuracy and its
environmental impacts. When we focus only on the model’s
accuracy, we
“[ignore the
economic, environmental, or social cost of reaching the reported
accuracy](https://arxiv.org/abs/1907.10597 "https://arxiv.org/abs/1907.10597").” Because the
[relationship
between model accuracy and complexity is at best
logarithmic](https://arxiv.org/pdf/1611.10012.pdf "https://arxiv.org/pdf/1611.10012.pdf"), training a model longer or looking for
better hyperparameters only leads to a
[small
increase in performance](https://arxiv.org/pdf/1611.10012.pdf "https://arxiv.org/pdf/1611.10012.pdf").

## Implementation plan

- **Establish sustainable performance
  criteria** - Define performance criteria that
  support your sustainability goals while meeting your
  business requirements, but not exceeding them.
- **Make trade-offs** -
  Acceptable decreases in model performance can
  significantly reduce sustainability impacts of your
  models.
- **Stop training early** -
  In Automatic Model Tuning, early stopping stops the
  training jobs that a hyperparameter tuning job launches
  early when they are not improving significantly as
  measured by the objective metric. Similarly, SageMaker AI
  Debugger provides rules to automatically stop a training
  job as soon as it detects an issue (such as bug, job
  failing to converge...).

## Documents

- [Automatic
  Model Tuning with SageMaker AI - Stop Training Jobs
  Early](../../../sagemaker/latest/dg/automatic-model-tuning-early-stopping.md "../../../sagemaker/latest/dg/automatic-model-tuning-early-stopping.md")
- [Amazon SageMaker AI Debugger - Built-in Rules:
  LossNotDecreasing](../../../sagemaker/latest/dg/debugger-built-in-rules.md#loss-not-decreasing "../../../sagemaker/latest/dg/debugger-built-in-rules.md#loss-not-decreasing")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 2, model
  development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/")
- [Amazon SageMaker AI Automatic Model Tuning now supports early
  stopping of training jobs](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-now-supports-early-stopping-of-training-jobs/ "https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-now-supports-early-stopping-of-training-jobs/")

## Metrics

- Track the metrics related to the
  [resources
  provisioned for your training jobs](../../../sagemaker/latest/APIReference/API_DescribeTrainingJob.md#sagemaker-DescribeTrainingJob-response-ResourceConfig "../../../sagemaker/latest/APIReference/API_DescribeTrainingJob.md#sagemaker-DescribeTrainingJob-response-ResourceConfig") (InstanceCount,
  InstanceType, and VolumeSizeInGB)
- Measure the
  [efficient
  use of these resources](../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs "../../../sagemaker/latest/dg/monitoring-cloudwatch.md#cloudwatch-metrics-jobs") (CPUUtilization,
  GPUUtilization, GPUMemoryUtilization, MemoryUtilization,
  and DiskUtilization) in the
  [SageMaker AI
  Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-sm"), the
  [CloudWatch
  Console](../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw "../../../sagemaker/latest/dg/training-metrics.md#view-train-metrics-cw") or your
  [SageMaker AI
  Debugger Profiling Report](../../../sagemaker/latest/dg/debugger-profiling-report.md#debugger-profiling-report-walkthrough-system-usage "../../../sagemaker/latest/dg/debugger-profiling-report.md#debugger-profiling-report-walkthrough-system-usage")
