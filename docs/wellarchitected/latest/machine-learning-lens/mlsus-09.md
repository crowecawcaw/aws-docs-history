# MLSUS-09: Archive or delete unnecessary training artifacts

Remove training artifacts that are unused and no longer required
to limit wasted resources. Determine when you can archive
training artifacts to more energy-efficient storage or safely
delete them. 

## Implementation plan

- **Clean up unneeded training
  resources** - Organize your ML experiments with
  [SageMaker AI
  Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to
  [clean
  up training resources](../../../sagemaker/latest/dg/experiments-cleanup.md "../../../sagemaker/latest/dg/experiments-cleanup.md") you no longer need.
- **Reduce the volume of logs you
  keep** - By default, CloudWatch retains logs
  indefinitely. By
  [setting
  limited retention time](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention") for your notebooks and
  training logs, you’ll avoid the environmental impact of
  unnecessary log storage.

## Documents

- [Clean
  Up Amazon SageMaker AI Experiment Resources](../../../sagemaker/latest/dg/experiments-cleanup.md "../../../sagemaker/latest/dg/experiments-cleanup.md")
- [Change
  log data retention in CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#SettingLogRetention")

## Blogs

- [Optimize
  AI/ML workloads for sustainability: Part 2, model
  development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/ "https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/")
- [Clean
  up Your Container Images with Amazon ECR Lifecycle
  Policies](https://aws.amazon.com/blogs/compute/clean-up-your-container-images-with-amazon-ecr-lifecycle-policies/ "https://aws.amazon.com/blogs/compute/clean-up-your-container-images-with-amazon-ecr-lifecycle-policies/")

## Metrics

- Measure and optimize the total size of your
  [Amazon S3](https://aws.amazon.com/s3 "https://aws.amazon.com/s3") buckets and storage class distribution, using
  [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/ "https://aws.amazon.com/s3/storage-analytics-insights/")
- Measure and optimize the
  [size
  your of CloudWatch log groups](../../../AmazonCloudWatchLogs/latest/APIReference/API_LogGroup.md#CWL-Type-LogGroup-storedBytes "../../../AmazonCloudWatchLogs/latest/APIReference/API_LogGroup.md#CWL-Type-LogGroup-storedBytes")
