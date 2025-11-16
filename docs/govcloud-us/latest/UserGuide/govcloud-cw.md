# Amazon CloudWatch in AWS GovCloud (US)

Use CloudWatch Events to send system events from AWS resources to AWS Lambda functions, Amazon SNS topics, streams in Amazon Kinesis, and other target types.

## How Amazon CloudWatch differs for AWS GovCloud (US)

- Transaction Search is not available.
- The GetMetricWidgetImage API is not available.
- [Dashboard sharing](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md") is not available.
- You cannot create CloudWatch alarms for Trusted Advisor metrics in AWS GovCloud (US).
- Amazon CloudWatch cross-account observability is not available in AWS GovCloud (US).

## Documentation for Amazon CloudWatch

[Amazon CloudWatch documentation](https://aws.amazon.com/documentation/cloudwatch/ "https://aws.amazon.com/documentation/cloudwatch/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Alarm Name and Description
- Alarm configuration
- Alarm tags
- Metric Name
- Metric Namespace
- Metric Dimensions
