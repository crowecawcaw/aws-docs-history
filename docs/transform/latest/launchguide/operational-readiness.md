AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Operational readiness

A successful approach to operations is critical to the success of every organization and its
digital transformation. [Operational excellence](../../../wellarchitected/latest/operational-excellence-pillar/operational-excellence.md "../../../wellarchitected/latest/operational-excellence-pillar/operational-excellence.md") is required to ensure that your transformation achieves its
purpose and that applications consistently meet their business outcomes and the expectations of
their users. This topic is intended to help you get a head start on your operations.

## Managing your resources

Use an orchestration tool to manage, configure, patch, and use automation.

**AWS Systems Manager:** Use [AWS Systems Manager Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") to quickly configure required security roles and
commonly used Systems Manager capabilities on your Amazon Elastic Compute Cloud instances across your entire
organization.

The following are some of the capabilities of Systems Manager:

- [AWS Systems Manager Session Manager](../../../systems-manager/latest/userguide/session-manager.md "../../../systems-manager/latest/userguide/session-manager.md") allows you to SSH to
  Linux or RDP to Windows instances without the need to open inbound ports, maintain bastion
  hosts, or manage SSH keys.
- [AWS Systems Manager Distributor](../../../systems-manager/latest/userguide/distributor.md "../../../systems-manager/latest/userguide/distributor.md") allows you to package and
  publish your own software or to find and publish AWS-provided agent software packages,
  such as AmazonCloudWatchAgent, or third-party packages such as Trend Micro.
- [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/patch-manager.md "../../../systems-manager/latest/userguide/patch-manager.md") allows you to automate the
  process of patching managed nodes with both security-related updates and other types of
  updates.

## Monitoring and observability

Implement observability in infrastructure and applications so that you can understand
their state and make data-driven decisions based on business requirements.

- **Amazon CloudWatch Metrics**: Centralize performance
  data with basic monitoring metrics at no charge from AWS services such as Amazon EC2,
  Amazon Elastic Block Store (Amazon EBS), and Amazon Relational Database Service (Amazon RDS). For more information, see [AWS services that publish CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.md "../../../AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.md") in the Amazon
  CloudWatch User Guide.
- **CloudWatch Dashboards**: To learn how to see key
  metrics from all AWS services, refer to [See the pre-built cross-service dashboard](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.md") . To learn how to
  use automatic dashboards to focus on metrics and alarms in a single AWS service, refer to
  [See a pre-built dashboard for a single AWS service](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Focus_Service.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Focus_Service.md") . The
  metrics that are considered most important by service teams are used on automatic
  dashboards. Use these metrics as a starting point for your own dashboards.
- **CloudWatch Logs**: To learn how to centralize, manage,
  and analyze logs from AWS services, see [Enabling logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the Amazon CloudWatch
  Logs User Guide.
- **CloudWatch Alarms**: A metric alarm watches a single
  CloudWatch metric or the result of a math expression based on CloudWatch metrics. The
  alarm performs one or more actions based on the value of the metric or expression relative
  to a threshold over a number of time periods. To learn how to create and use alarms, see
  [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") .
- **CloudWatch Agent**: [Install the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md") as part of [AWS Systems Manager Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") to send instance metrics
  and logs to CloudWatch. Use these metrics and logs alongside AWS service metrics and logs
  to create dashboards and alarms for your infrastructure and applications.
- **AWS CloudTrail**: CloudTrail is active in your AWS account when you create it and doesn't require any manual setup. When activity occurs in
  your AWS account, that activity is recorded in a CloudTrail event. [Tutorial: Review AWS account activity in event history](../../../awscloudtrail/latest/userguide/tutorial-event-history.md "../../../awscloudtrail/latest/userguide/tutorial-event-history.md")

Set up a monitoring account for cross-account observability. To learn how, see [Link monitoring accounts with source accounts](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account-Setup.md") in the Amazon
CloudWatch User Guide.

## Security and compliance

Ensuring the security and compliance of your AWS environment is paramount.

- **AWS Security Hub CSPM**: Security Hub provides you with a
  comprehensive view of your security state in AWS and helps you assess your AWS environment
  against security industry standards and best practices. To learn how to set it up and use
  it, see [Enabling Security Hub](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md") in the AWS Security Hub User Guide.
- **AWS Config**: AWS Config provides a detailed view of
  the configuration of AWS resources in your AWS account. This includes how the resources
  are related to one another and how they were configured in the past so that you can see
  how the configurations and relationships change over time. Use AWS Config to assess,
  audit, and evaluate the configurations of your AWS resources. To learn how to set it up,
  see [Getting Started with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md") in the AWS Config Developer Guide.

Video: [Back to Basics: Using AWS Config; and Conformance Packs to Optimize Your AWS Resources](https://www.youtube.com/watch?v=tT8LXTztKjE "https://www.youtube.com/watch?v=tT8LXTztKjE")

## Backup

AWS Backup is a fully-managed service that helps you centralize and automate data
protection across AWS services, in the cloud, and on premises. To learn more, see [Getting started with AWS Backup](../../../aws-backup/latest/devguide/getting-started.md "../../../aws-backup/latest/devguide/getting-started.md") in the AWS Backup Developer Guide.

## Optimization and cost management

Optimize your AWS usage to ensure cost efficiency without compromising on performance and
security.

- **AWS Cost Explorer**: This is a tool that you can use to
  visualize, understand, and manage your AWS costs and usage over time. To learn how to
  enable it and use it, see [Analyzing your costs with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the AWS Cost Management User Guide.
- **AWS Trusted Advisor**: Trusted Advisor draws upon best
  practices learned from helping hundreds of thousands of AWS customers. It inspects your
  AWS environment, and then makes recommendations when opportunities exist to save money,
  improve system availability and performance, or help close security gaps. For more
  information, see [AWS Trusted Advisor](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md") in the AWS Support User Guide.
- **AWS Compute Optimizer**: This is a service that
  analyzes the configuration of your AWS resources and their utilization metrics to provide
  you with right-sizing recommendations. Use Compute Optimizer to right-size workloads
  according to your workload preferences through artificial intelligence and
  machine-learning-based analytics to reduce costs by up to 25%. By using [memory metrics](../../../compute-optimizer/latest/ug/metrics.md#cw-agent "../../../compute-optimizer/latest/ug/metrics.md#cw-agent") collected by the CloudWatch agent, the
  recommendations for right-sizing EC2 instances are improved. For more information, see
  [Getting started with AWS Compute Optimizer](../../../compute-optimizer/latest/ug/getting-started.md "../../../compute-optimizer/latest/ug/getting-started.md").
