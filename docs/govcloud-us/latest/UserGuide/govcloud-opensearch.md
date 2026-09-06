

# Amazon OpenSearch Service in AWS GovCloud (US)
<a name="govcloud-opensearch"></a>

{eslong} is a managed service that makes it easy to deploy, operate, and scale {opensearch}, a popular open-source search and analytics engine. {es} also offers security options, high availability, data durability, and direct access to the {opensearch} API.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon OpenSearch Service differs
<a name="govcloud-diffs-21"></a>

The following differences apply to Amazon OpenSearch Service:
+  Amazon Cognito authentication for OpenSearch Dashboards is not available in the AWS GovCloud (US-East) Region.

The following differences apply to Amazon OpenSearch Ingestion:
+ S3 vector source is not available.
+ The RDS source with Aurora PostgreSQL is not available. Aurora MySQL, RDS MySQL, and RDS PostgreSQL sources are supported.
+ MSK Serverless source is not available.

## Documentation
<a name="govcloud-docs-59"></a>
+  [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/) 

## Export-controlled content
<a name="govcloud-itar-content-99"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon OpenSearch Service metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you specify when creating and maintaining your OpenSearch clusters and indices, such as index names, alias names, tags, snapshot names, and repository names.
+ Do not enter export-controlled data in the following fields:
  + Domain name
  + Index names
  + Type names
  + Document IDs
  + Snapshot names
  + Resource tags
  + Repository names
  + Alias names
  +  CloudWatch log group names