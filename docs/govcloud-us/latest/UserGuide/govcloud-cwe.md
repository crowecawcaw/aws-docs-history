# Amazon CloudWatch Events in AWS GovCloud (US)

Use CloudWatch Events to send system events from AWS resources to AWS Lambda functions, Amazon SNS topics, streams in Amazon Kinesis, and other target types.

## How Amazon CloudWatch Events differs for AWS GovCloud (US)

- Use SSL (HTTPS) when you make calls to the service in AWS GovCloud (US) Regions. In other AWS Regions, you can use HTTP or HTTPS.

## Documentation for Amazon CloudWatch Events

[Amazon CloudWatch Events documentation](https://aws.amazon.com/documentation/cloudwatch/ "https://aws.amazon.com/documentation/cloudwatch/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No export-controlled data may be entered, stored, or processed by CloudWatch Events. For
  example, CloudWatch Events metadata is not permitted to contain export-controlled data. This
  metadata includes all the configuration data that you enter when creating and
  maintaining your CloudWatch Events alarms.

For example, do not enter export-controlled data in the following
fields:

    + Rule names
    + Rule descriptions
    + Event patterns
    + Data input to APIs
