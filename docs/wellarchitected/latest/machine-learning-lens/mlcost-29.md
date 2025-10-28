# MLCOST-29: Monitor endpoint usage and right-size the instance fleet

Ensure efficient compute resources are used to run models in
production. Monitor your endpoint usage and right-size the
instance fleet. Use automatic scaling (autoscaling) for your
hosted models. _Autoscaling_ dynamically
adjusts the number of instances provisioned for a model in
response to changes in your workload. 

## Implementation plan

- **Monitor Amazon SageMaker AI
  endpoints with Amazon CloudWatch**
  -You can monitor
  Amazon SageMaker AI using Amazon CloudWatch, which collects
  raw data and processes it into readable, near real-time
  metrics. Use metrics such
  as CPUUtilization, GPUUtilization, MemoryUtilization, GPUUtilization
  to view your endpoint's resource utilization and use the
  information to right-size the endpoint instance.
- **Use autoscaling with Amazon SageMaker AI** - Amazon SageMaker AI supports
  autoscaling that monitors your workloads and dynamically
  adjusts the capacity to maintain steady and predictable
  performance at the lowest possible cost. When the
  workload increases, autoscaling brings more instances
  online. When the workload decreases, autoscaling removes
  unnecessary instances, helping you reduce your compute
  cost. SageMaker AI automatically attempts to distribute
  your instances across Availability Zones. So, we
  strongly recommend that you deploy multiple instances
  for each production endpoint for high availability. If
  you’re using a VPC, configure at least two subnets in
  different Availability Zones so Amazon SageMaker AI can
  distribute your instances across those Availability
  Zones.
- **Determine the resource placement carefully** – Amazon FSx for Lustre can be an input data source for Amazon SageMaker AI. When FSx for Lustre is used as an input data source, Amazon SageMaker AI ML training jobs are accelerated by eliminating the initial Amazon S3 download step. However, as a best practice, it is recommended that customers deploy FSx for Lustre and SageMaker AI in the same Availability Zone. Deploying them across Availability Zones or VPC can result in a significant cost.

## Documents

- [Automatically
  Scale Amazon SageMaker AI Model](../../../sagemaker/latest/dg/endpoint-auto-scaling.md "../../../sagemaker/latest/dg/endpoint-auto-scaling.md")
- [Monitor
  Amazon SageMaker AI endpoints with Amazon CloudWatch](../../../sagemaker/latest/dg/monitoring-cloudwatch.md "../../../sagemaker/latest/dg/monitoring-cloudwatch.md")

## Blogs

- [Use
  Amazon CloudWatch custom metrics for real-time
  monitoring of Amazon SageMaker AI model performance](https://aws.amazon.com/blogs/machine-learning/use-amazon-cloudwatch-custom-metrics-for-real-time-monitoring-of-amazon-sagemaker-model-performance/ "https://aws.amazon.com/blogs/machine-learning/use-amazon-cloudwatch-custom-metrics-for-real-time-monitoring-of-amazon-sagemaker-model-performance/")
- [Speed up training on Amazon SageMaker AI using Amazon FSx for Lustre and Amazon EFS file systems](https://aws.amazon.com/blogs/machine-learning/speed-up-training-on-amazon-sagemaker-using-amazon-efs-or-amazon-fsx-for-lustre-file-systems/ "https://aws.amazon.com/blogs/machine-learning/speed-up-training-on-amazon-sagemaker-using-amazon-efs-or-amazon-fsx-for-lustre-file-systems/")
