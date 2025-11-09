# Amazon SNS in AWS GovCloud (US)

Amazon Simple Notification Service (Amazon SNS) is a web service that enables applications, end-users, and devices to instantly send and receive notifications from the cloud.

## How Amazon Simple Notification Service differs for AWS GovCloud (US)

- You cannot use Amazon SNS to send SMS messages while using the AWS GovCloud (US-East) Region.
- Amazon Data Firehose subscriptions are not supported.
- Kinesis Firehose protocol option for the Amazon SNS topics is not available.
- Message Data Protection is not supported.
- Custom data identifiers are not supported.
- Amazon SNS message archiving and replay is not supported.
- IPv6 is not supported.

## Documentation for Amazon Simple Notification Service

[Amazon SNS documentation](http://aws.amazon.com/documentation/sns/ "http://aws.amazon.com/documentation/sns/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Export-controlled data may not be entered, stored, or processed in Amazon SNS notification messages when the following notification endpoints are being used:

Notification Endpoints

    + Mobile push notifications – not permitted to contain export-controlled data
    + Email – not permitted to contain export-controlled data
    + Amazon SQS queues outside of AWS GovCloud (US) Regions – not permitted to contain export-controlled data
    + HTTP URL endpoint – not permitted to contain export-controlled data

- Amazon SNS metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when setting up and maintaining your topics.

For example, do not enter export-controlled data in the following fields:

    + Topic Name
    + Display Name
    + Topic Policy
    + Topic Delivery Policy
    + Topic ARN
    + Endpoint
    + Subject
    + Application Name
