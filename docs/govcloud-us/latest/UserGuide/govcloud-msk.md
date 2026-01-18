# Amazon Managed Streaming for Apache Kafka (MSK) in AWS GovCloud (US)

Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data. Amazon MSK provides the control-plane operations, such as those for creating, updating, and deleting clusters. It lets you use Apache Kafka data-plane operations, such as those for producing and consuming data. It runs open-source versions of Apache Kafka. This means existing applications, tooling, and plugins from partners and the Apache Kafka community are supported without requiring changes to application code.

## How Managed Streaming for Apache Kafka differs for AWS GovCloud (US)

- Firehose isn’t available as a destination for broker logs in AWS GovCloud (US).
- Amazon Managed Streaming for Apache Kafka (MSK) Serverless is not available in AWS GovCloud (US).

## Documentation for Managed Streaming for Apache Kafka

[Amazon Managed Streaming for Apache Kafka (MSK) documentation](../../../msk/latest/developerguide/what-is-msk.md "../../../msk/latest/developerguide/what-is-msk.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- This service can generate metadata from customer-defined configurations. AWS suggests customers do not enter export-controlled information in console fields, descriptions, resource names, and tagging information.
