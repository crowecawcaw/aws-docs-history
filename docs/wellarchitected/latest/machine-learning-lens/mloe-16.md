# MLOE-16: Synchronize architecture and configuration, and check for skew across environments

Ensure that all systems and configurations are identical across
development and deployment phases. Otherwise, the same
algorithm can result in different inference results depending
on differences in system architectures. Ensure that the model
gets the same range of accuracy in development, staging, and
production environments. Perform this check as part of the
normal promotion process.

## Implementation plan

- **Use AWS CloudFormation** -
  [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") gives you an easy way to model a
  collection of related AWS and third-party resources.
  CloudFormation provisions these resources quickly
  and consistently, and manages them throughout their
  lifecycles by treating infrastructure as code. You can
  use a CloudFormation template to create, update, and
  delete an entire stack as a single unit, as often as you
  need to, instead of managing resources individually. You
  also can manage and provision stacks across multiple AWS accounts and AWS Regions. This will synchronize your
  architecture and configuration across environments.
- **Use Amazon SageMaker AI Model
  Monitor** -Continually monitor the quality of
  Amazon SageMaker AI machine learning models in production
  and compare with the results from training using
  [SageMaker AI
  Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md"). Set alerts that notify you when
  there are deviations in the model quality. Early and
  proactive detection of these deviations enables you to
  take corrective actions. These actions can include
  retraining models, auditing upstream systems, and fixing
  quality issues without having to monitor models manually
  or build additional tools. Model Monitor provides
  monitoring capabilities that do not require coding; you
  also have the ﬂexibility to monitor models by adding
  code to provide custom analysis.

## Documents

- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Implement
  infrastructure as code](../financial-services-industry-lens/implement-infrastructure-as-code.md "../financial-services-industry-lens/implement-infrastructure-as-code.md")

## Blogs

- [Amazon SageMaker AI Model Monitor – Fully Managed Automatic
  Monitoring for your Machine Learning](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
  [Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
- [AWS CloudFormation – Create Your AWS Stack From a
  Recipe](https://aws.amazon.com/blogs/aws/cloudformation-create-your-aws-stack-from-a-recipe/ "https://aws.amazon.com/blogs/aws/cloudformation-create-your-aws-stack-from-a-recipe/")

## Examples

- [Introduction
  to Amazon SageMaker AI Model Monitor](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.html")
- [Model
  Monitor Visualization](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/visualization/SageMaker AI-Model-Monitor-Visualize.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/visualization/SageMaker AI-Model-Monitor-Visualize.html")
