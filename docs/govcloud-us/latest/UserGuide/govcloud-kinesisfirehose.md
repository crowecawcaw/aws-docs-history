# Amazon Data Firehose in AWS GovCloud (US)

Amazon Kinesis Data Firehose is a fully managed service for delivering real-time streaming data to destinations such as Amazon Simple Storage Service (Amazon S3), Amazon Redshift, Amazon OpenSearch Service, and Splunk. Kinesis Data Firehose is part of the Kinesis streaming data platform, along with Kinesis Data Streams, Kinesis Video Streams, and Amazon Kinesis Data Analytics. With Kinesis Data Firehose, you don't need to write applications or manage resources. You configure your data producers to send data to Kinesis Data Firehose, and it automatically delivers the data to the destination that you specified. You can also configure Kinesis Data Firehose to transform your data before delivering it.

## How Amazon Data Firehose differs for AWS GovCloud (US)

This service has no differences between the AWS GovCloud (US) and the standard AWS Regions.

## Documentation for Amazon Data Firehose

[Amazon Data Firehose documentation](https://aws.amazon.com/documentation/kinesis/ "https://aws.amazon.com/documentation/kinesis/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Do not enter export-controlled data in the following fields:
  - Stream names

If you are processing export-controlled data with this service,
use the SSL (HTTPS) endpoint to maintain export compliance. For more information, see [Service Endpoints](using-govcloud-endpoints.md "using-govcloud-endpoints.md").
