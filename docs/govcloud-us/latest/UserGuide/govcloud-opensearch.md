# Amazon OpenSearch Service in AWS GovCloud (US)

Amazon OpenSearch Service is a managed service that makes it easy to deploy, operate, and scale OpenSearch, a popular open-source search and analytics engine. OpenSearch Service also offers security options, high availability, data durability, and direct access to the OpenSearch API.

## How Amazon OpenSearch Service differs for AWS GovCloud (US)

- Amazon Cognito authentication for OpenSearch Dashboards is not supported in the AWS GovCloud (US-East) Region.
- OpenSearch ingestion is not available in AWS GovCloud (US).

## Documentation for Amazon OpenSearch Service

[Amazon OpenSearch Service documentation](../../../opensearch-service.md "../../../opensearch-service.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon OpenSearch Service metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you specify when creating and maintaining your OpenSearch clusters and indices, such as index names, alias names, tags, snapshot names, and repository names.
- Do not enter export-controlled data in the following fields:
  - Domain name
  - Index names
  - Type names
  - Document IDs
  - Snapshot names
  - Resource tags
  - Repository names
  - Alias names
  - CloudWatch log group names
