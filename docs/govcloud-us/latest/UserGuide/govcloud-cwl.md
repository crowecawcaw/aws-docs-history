# Amazon CloudWatch Logs in AWS GovCloud (US)

Use CloudWatch Logs to monitor, store, and access your log files from Amazon EC2 instances, AWS CloudTrail, or other sources.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Amazon CloudWatch Logs differs

The following differences apply to Amazon CloudWatch Logs:

- Use SSL (HTTPS) when you make calls to the service in AWS GovCloud (US) Regions. In other AWS Regions, you can use HTTP or HTTPS.
- The Live Tail feature is not available.
- The `logGroupNamePattern` parameter is not available for use in the describe-log-groups AWS CLI command or the DescribeLogGroups API.

## Documentation

- [Amazon CloudWatch Logs documentation](../../../documentation/cloudwatch.md "../../../documentation/cloudwatch.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- CloudWatch Log Group Names
- CloudWatch Log Stream Names
- Log group tags
