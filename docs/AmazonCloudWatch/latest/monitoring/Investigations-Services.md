# AWS services where investigations are

supported

You can launch investigations from telemetry data (such as CloudWatch metrics, alarms, and
logs), review generated anomaly signals, and explore hypotheses on investigations.
CloudWatch investigations work best when helping you with automated troubleshooting guidance on the AWS
services listed below:

- Amazon API Gateway
- AWS AppSync
- Amazon Data Firehose
- Amazon DynamoDB
- Amazon EBS1
- Amazon EC21
- Amazon ECS on Amazon EC22
- Amazon ECS on Fargate2
- Amazon EKS3
- Amazon Kinesis Data Streams
- AWS Lambda
- Amazon OpenSearch Service
- Amazon RDS4
- Amazon S3
- Amazon SNS
- Amazon SQS
- AWS Step Functions
  The list of services will continue to be expanded over time. CloudWatch investigations utilizes a wide
  range of data sources to determine dependency relationships and plan analysis paths,
  including telemetry data configurations, service configurations, and observed
  relationships through CloudWatch Application Signals and X-Ray. Where none of the above is
  available, CloudWatch investigations will attempt to infer dependency relationships through co-occurring
  telemetry anomalies.

**Best practice setup**

While CloudWatch investigations will continue to analyze telemetry data and provide suggestions without the
following features enabled, for optimal quality and performance for CloudWatch investigations, we recommend
you complete the following steps:

- 1For both Amazon EC2 and Amazon EBS, update your CloudWatch agent
  to version 1.30049.1 or later. For more information, see [Collect metrics, logs, and traces using the CloudWatch
  agent](Install-CloudWatch-Agent.md "Install-CloudWatch-Agent.md").
- 2For Amazon ECS, enable CloudWatch Container Insights. For
  more information, see [Container Insights](ContainerInsights.md "ContainerInsights.md").
- 3For Amazon EKS, enable CloudWatch Container Insights and
  configure Amazon EKS Access Entries. For more information, see [Container Insights](ContainerInsights.md "ContainerInsights.md") and [Integration with Amazon EKS](EKS-Integration.md "EKS-Integration.md").
- 4For Amazon RDS, enable CloudWatch Database Insights in the
  **Advanced mode**. For more information, see [Turning on the Advanced mode of Database Insights for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.md")
  in the _Aurora User Guide_.
- Enable CloudWatch Application Signals and X-Ray. For more information, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md") and [What is
  AWS X-Ray](../../../xray/latest/devguide/aws-xray.md "../../../xray/latest/devguide/aws-xray.md").
