# Amazon CloudWatch Logs in AWS GovCloud (US)

Use CloudWatch Logs to monitor, store, and access your log files from Amazon EC2 instances, AWS CloudTrail, or other sources.

## How Amazon CloudWatch Logs differs for AWS GovCloud (US)

- Use SSL (HTTPS) when you make calls to the service in AWS GovCloud (US) Regions. In other AWS Regions, you can use HTTP or HTTPS.
- The Live Tail feature is not available.
- The `logGroupNamePattern` parameter is not supported for use in the describe-log-groups AWS CLI command or the DescribeLogGroups API.

## Documentation for Amazon CloudWatch Logs

[Amazon CloudWatch Logs documentation](https://aws.amazon.com/documentation/cloudwatch/ "https://aws.amazon.com/documentation/cloudwatch/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- CloudWatch Log Group Names
- CloudWatch Log Stream Names
- Log group tags
