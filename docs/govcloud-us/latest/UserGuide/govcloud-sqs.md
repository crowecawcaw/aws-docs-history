

# Amazon SQS in AWS GovCloud (US)
<a name="govcloud-sqs"></a>

Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications. Amazon SQS moves data between distributed application components and helps you decouple these components.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Simple Queue Service differs
<a name="govcloud-sqs-diffs"></a>

The following differences apply to Amazon Simple Queue Service:
+ IPv6 is not available.

## Documentation
<a name="govcloud-sqs-docs"></a>
+  [Amazon SQS documentation](http://aws.amazon.com/documentation/sqs/) 

## Export-controlled content
<a name="govcloud-sqs-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon SQS metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when setting up and maintaining your queues.

  For example, do not enter export-controlled data in the following fields:
  + Queue Name
  + Queue Configuration
  + Queue Policy Document
  + Queue Permissions