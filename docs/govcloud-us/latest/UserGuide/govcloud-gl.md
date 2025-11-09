# Amazon Glacier in AWS GovCloud (US)

Amazon Glacier is a storage service optimized for infrequently used data, or cold data. The service provides durable and extremely low-cost storage with security features for data archiving and backup.

## How Amazon Glacier differs for AWS GovCloud (US)

This service has no differences between the AWS GovCloud (US) and the standard AWS Regions.

## Documentation for Amazon Glacier

[Amazon Glacier documentation](http://aws.amazon.com/documentation/glacier/ "http://aws.amazon.com/documentation/glacier/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Glacier metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your Amazon Glacier vaults names.
- Do not enter export-controlled data in the following fields:
  - Resource tags: Key
  - Resource tags: Value
