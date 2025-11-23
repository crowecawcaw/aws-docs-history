# Resource requirements

This page provides you with an overview of the resource requirements needed for AWS Compute Optimizer to generate optimization recommendations.
For Compute Optimizer to generate recommendations, your AWS resources must meet Amazon CloudWatch metric and
resource-specific requirements. Compute Optimizer has different CloudWatch metric data requirements for each resource type.

If your resources don't have enough metric data, allow for more time before the
recommendations start appearing in the Compute Optimizer console. For example, if your resources
have enough metric data but the recommendations aren't
showing up, this probably means that Compute Optimizer is still analyzing your resources. It can take up to
24 hours to complete the analysis. After the analysis is complete, resource recommendations
appear in the Compute Optimizer console.

###### Topics

- [Amazon EC2 instance and EC2 Amazon EC2 Auto Scaling group requirements](#requirements-ec2-instances "#requirements-ec2-instances")
- [Amazon EBS volume requirements](#requirements-ebs-volumes "#requirements-ebs-volumes")
- [Lambda function requirements](#requirements-lambda-functions "#requirements-lambda-functions")
- [Requirements for Amazon ECS services on Fargate](#requirements-ecs-fargate "#requirements-ecs-fargate")
- [Commercial software license requirements](#requirements-license "#requirements-license")
- [Amazon Aurora and RDS database requirements](#requirements-rds "#requirements-rds")
- [Additional resources](#requirements-resources "#requirements-resources")

## Amazon EC2 instance and EC2 Amazon EC2 Auto Scaling group requirements

Amazon EC2 instances and EC2 Amazon EC2 Auto Scaling groups both require at least 30 hours of CloudWatch metric data in the past 14 days.

If you enabled the enhanced infrastructure metrics feature, both EC2 instances and EC2 Amazon EC2 Auto Scaling require at least 30 hours of
CloudWatch metric data over the past 93 days. For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md").

For a list of the instance types supported by Compute Optimizer, see [Supported Amazon EC2 instance types](supported-resources.md#supported-ec2-instances "supported-resources.md#supported-ec2-instances").
For information about the EC2 Amazon EC2 Auto Scaling groups that Compute Optimizer supports, see [Supported Amazon EC2 Amazon EC2 Auto Scaling groups](supported-resources.md#supported-asg "supported-resources.md#supported-asg").

###### Important

You must enable Cost Explorer to allow Compute Optimizer to use Cost Explorer's billing data to calculate savings
and populate pricing information for your recommendations. We recommend that you also opt in to Cost
Optimization Hub to receive rightsizing recommendations that consider any Reserved Instances or Savings
Plans pricing models that are active in your accounts. For more information, see
[Enabling
Cost Explorer](../../../cost-management/latest/userguide/ce-enable.md "../../../cost-management/latest/userguide/ce-enable.md") and [Getting started with Cost Optimization Hub](../../../cost-management/latest/userguide/coh-getting-started.md "../../../cost-management/latest/userguide/coh-getting-started.md") in the _AWS Cost Management User Guide_.

## Amazon EBS volume requirements

Compute Optimizer generates recommendations for EBS volume types that are attached to a running
instance for at least 30 consecutive hours. Data is only reported to CloudWatch when the volume is attached to a running instance.
If you detach an EBS volume from an EC2 instance, the recommendations
for that volume will no longer be available.

For a list of Amazon EBS volume types supported by Compute Optimizer, see [Supported Amazon EBS volume types](supported-resources.md#supported-ebs-volumes "supported-resources.md#supported-ebs-volumes").

## Lambda function requirements

Compute Optimizer generates memory size recommendations only for Lambda functions that meet the
following requirements:

- The configured memory is less than or equal to 1,792 MB.
- The functions were invoked at least 50 times in the last 14 days.

Functions that don't meet these requirements are given a finding of
**Unavailable**. The reason code of **Inconclusive**
applies to functions that have configured memory greater than 1,792 MB. **Insufficient
data** applies to functions that have been invoked fewer than 50 times in the last
14 days.

Functions with a finding of **Unavailable** don't appear in the Compute Optimizer
console and don't receive recommendations.

###### Note

Lambda functions don't require CloudWatch metric data.

## Requirements for Amazon ECS services on Fargate

To generate recommendations for Amazon ECS services on Fargate, Compute Optimizer requires the following:

- Your services have at least 24 hours of CloudWatch and Amazon ECS utilization metrics in the past 14 days.
- No step scaling policy is attached.
- No target scaling policy is attached to CPU and memory.

###### Note

If a target tracking policy is attached to the service’s CPU only, Compute Optimizer only
generates memory size recommendations. Or, if a target tracking policy is attached to the service’s
memory only, Compute Optimizer only generates CPU size recommendations.

- The service run status is **SteadyState** or **MoreWork**.

For more information about the metrics analyzed, see [Metrics for Amazon ECS services on Fargate](ecs-fargate-metrics-analyzed.md "ecs-fargate-metrics-analyzed.md").

## Commercial software license requirements

Compute Optimizer only generates license recommendations for Microsoft SQL Server on Amazon EC2.

To generate recommendations for commercial software licenses, Compute Optimizer requires the following:

- At least 30 _consecutive_ hours of CloudWatch metric data.
- Enable CloudWatch Application Insights using your Microsoft SQL Server database credentials.

For more information about how to enable CloudWatch Application Insights, see [Set up
Amazon CloudWatch Application Insights for monitoring](../../../AmazonCloudWatch/latest/monitoring/appinsights-setting-up.md "../../../AmazonCloudWatch/latest/monitoring/appinsights-setting-up.md") in the _Amazon CloudWatch User Guide_.

- Attach the required instance role and policy for CloudWatch Application Insights. For more information,
  see [Policies to enable commercial software license
  recommendations](security-iam.md#license-access "security-iam.md#license-access").

For more information about the metrics analyzed, see [Metrics for commercial software licenses](license-metrics-analyzed.md "license-metrics-analyzed.md").

## Amazon Aurora and RDS database requirements

Compute Optimizer generates Aurora and RDS DB instances, RDS DB instance storage, and Aurora DB cluster recommendations for RDS for MySQL, RDS for PostgreSQL, and
Amazon Aurora databases.

### Amazon Aurora and RDS instances

To generate recommendations for your Aurora and RDS DB instances, Compute Optimizer requires the following:

- At least 30 hours of CloudWatch metric data in the past 14 days.
  If you enabled the enhanced infrastructure metrics feature, DB instances require at least 30 hours of metric data
  over the past 93 days. For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md").
- To receive recommendations for RDS DB instances that are over-provisioned, you need to enable
  Amazon RDS Performance Insights. To enable Performance Insights for your DB instances, see
  [Turning Performance Insights on and off for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md")
  in the _Amazon Relational Database Service User Guide_.

### Aurora DB clusters

To generate recommendations for your Aurora DB clusters, Compute Optimizer requires the following:

- No application Amazon EC2 Auto Scaling policy is attached to the Aurora DB cluster. For more information about Aurora
  Auto Scaling, see [Amazon Aurora Auto Scaling
  with Aurora Replicas](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Integrations.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Integrations.md") in the _Amazon Aurora User Guide_.
- The Aurora DB cluster has at least 14 days of cost usage data.
- The Aurora DB cluster has not used Aurora Parallel Query over the lookback period.
- The Aurora DB cluster has not changed storage configuration in the last 30 days.

## Additional resources

- [AWS resources supported by Compute Optimizer](supported-resources.md "supported-resources.md")
- [Metrics analyzed by AWS Compute Optimizer](metrics.md "metrics.md")
- [Getting started with AWS Compute Optimizer](getting-started.md "getting-started.md")
