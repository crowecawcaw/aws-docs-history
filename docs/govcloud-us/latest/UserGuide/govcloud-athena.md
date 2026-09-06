

# Amazon Athena in AWS GovCloud (US)
<a name="govcloud-athena"></a>

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds. Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically—executing queries in parallel—so results are fast, even with large datasets and complex queries.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Athena differs
<a name="govcloud-athena-diffs"></a>

The following differences apply to Athena:
+ Granting AWS Lake Formation permissions to Amazon Athena users who authenticate through the JDBC or ODBC driver using a SAML identity provider is not available.

## Documentation
<a name="govcloud-athena-docs"></a>
+  [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) 

## Export-controlled content
<a name="govcloud-athena-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Amazon Athena metadata is not permitted to contain export-controlled data. This metadata includes:
  + Database Name
  + Table Name
  + Partitions
  + Query Names
  + Query Strings