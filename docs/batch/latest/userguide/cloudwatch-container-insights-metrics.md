# Container Insights metrics

By default, the following metrics are displayed in the AWS Batch console under the
**Container insights** tab on a compute environment detail page. For a full list of Amazon ECS Container Insights
metrics, see [Amazon ECS Container
Insights Metrics](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-metrics-ECS.md") in the _Amazon CloudWatch User Guide_.

###### Note

These metrics are emitted for the Amazon ECS cluster associated with the AWS Batch compute
environment. AWS Batch jobs run as Amazon ECS tasks on this cluster.

- `TaskCount` – The number of Amazon ECS tasks running
  in the cluster. In the AWS Batch console, this metric is displayed as
  "Job Count".
- `ContainerInstanceCount` – The number of
  Amazon Elastic Compute Cloud instances that run the Amazon ECS agent and are registered in the Amazon ECS cluster.
- `MemoryReserved` – The memory that's
  reserved by Amazon ECS tasks in the cluster.
- `MemoryUtilized` – The memory that's
  being used by Amazon ECS tasks in the cluster.
- `CpuReserved` – The CPU units that are
  reserved by Amazon ECS tasks in the cluster.
- `CpuUtilized` – The CPU units used by Amazon ECS
  tasks in the cluster.
- `NetworkRxBytes` – The number of bytes that
  are received by Amazon ECS tasks in the cluster.
- `NetworkTxBytes` – The number of bytes
  that are transmitted by Amazon ECS tasks in the cluster.
- `StorageReadBytes` – The number of bytes
  that are read from storage.
- `StorageWriteBytes` – The number of bytes
  that are written to storage.
