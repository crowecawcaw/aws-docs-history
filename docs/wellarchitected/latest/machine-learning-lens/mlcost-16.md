# MLCOST-16: Stop resources when not in use

Stop resources that are not in use to reduce cost. For example,
hosted Jupyter environments used to explore small samples of
data, can be stopped when not actively in use. Where practical,
commit the work, stop them, and restart when needed. The same
approach can be used to stop the computing and the data storage
services.

## Implementation plan

- **Use CloudWatch Billing
  Alarms** - You can monitor your estimated AWS
  charges by using
  [Amazon](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md")
  [CloudWatch](../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md "../../../AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.md").
  When you enable the monitoring of estimated charges for
  your AWS account, the estimated charges are calculated and
  sent several times daily to CloudWatch as metric data. Use
  this feature to receive notifications when your resource
  charge exceeds a threshold amount.
- **Use SageMaker AI Lifecycle
  Configuration** - A
  [lifecycle
  configuration](../../../sagemaker/latest/dg/notebook-lifecycle-config.md "../../../sagemaker/latest/dg/notebook-lifecycle-config.md") provides shell scripts that run when
  you create the notebook instance or whenever you start
  one. When you create a notebook instance, you can create a
  new lifecycle configuration and its scripts or apply ones
  that you already have. Use a lifecycle configuration script
  to access AWS services from your notebook. These scripts
  enable checking notebook instance activities and shut them
  down if idle.
- **Use Amazon SageMaker AI Studio auto
  shutdown**-
  [Amazon SageMaker AI Studio](../../../sagemaker/latest/dg/studio.md "../../../sagemaker/latest/dg/studio.md") provides a unified, web-based
  visual interface for performing all ML development steps,
  making data science teams more productive. Idle SageMaker AI
  Studio notebooks can be detected and stopped using an
  auto-shutdown JupyterLab extension that can be
  [installed
  manually or automatically](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension "https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension"). You can shut down
  individual resources, including notebooks, terminals,
  kernels, applications, and instances.

## Documents

- [Shut
  Down Resources](../../../sagemaker/latest/dg/notebooks-run-and-manage-shut-down.md "../../../sagemaker/latest/dg/notebooks-run-and-manage-shut-down.md")

## Blogs

- [Save
  costs by automatically shutting down idle resources within
  Amazon SageMaker AIStudio](https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/ "https://aws.amazon.com/blogs/machine-learning/save-costs-by-automatically-shutting-down-idle-resources-within-amazon-sagemaker-studio/")

## Examples

- [Sagemaker-studio-auto-shutdown-extension](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension "https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension")
