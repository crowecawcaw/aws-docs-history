# Amazon CloudWatch in AWS GovCloud (US)

Use CloudWatch Events to send system events from AWS resources to AWS Lambda functions, Amazon SNS topics, streams in Amazon Kinesis, and other target types.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Amazon CloudWatch differs

The following differences apply to Amazon CloudWatch:

- Transaction Search is not available.
- The GetMetricWidgetImage API is not available.
- [Dashboard sharing](../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.md") is not available.
- You cannot create CloudWatch alarms for Trusted Advisor metrics.
- Amazon CloudWatch cross-account observability is not available.

## Documentation

- [Amazon CloudWatch documentation](../../../documentation/cloudwatch.md "../../../documentation/cloudwatch.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Alarm Name and Description
- Alarm configuration
- Alarm tags
- Metric Name
- Metric Namespace
- Metric Dimensions
