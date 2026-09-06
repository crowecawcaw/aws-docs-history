

# Amazon CloudWatch in AWS GovCloud (US)
<a name="govcloud-cw"></a>

Use CloudWatch Events to send system events from AWS resources to AWS Lambda functions, Amazon SNS topics, streams in Amazon Kinesis, and other target types.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon CloudWatch differs
<a name="govcloud-cw-diffs"></a>

The following differences apply to Amazon CloudWatch:
+ Transaction Search is not available.
+ The GetMetricWidgetImage API is not available.
+  [Dashboard sharing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-dashboard-sharing.html) is not available.
+ You cannot create CloudWatch alarms for Trusted Advisor metrics.
+  Amazon CloudWatch cross-account observability is not available.

## Documentation
<a name="govcloud-cw-docs"></a>
+  [Amazon CloudWatch documentation](https://docs.aws.amazon.com/documentation/cloudwatch/) 

## Export-controlled content
<a name="govcloud-cw-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Alarm Name and Description
+ Alarm configuration
+ Alarm tags
+ Metric Name
+ Metric Namespace
+ Metric Dimensions