# Amazon Athena in AWS GovCloud (US)

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds. Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically—executing queries in parallel—so results are fast, even with large datasets and complex queries.

## How Athena differs for AWS GovCloud (US)

- Granting AWS Lake Formation permissions to Amazon Athena users who authenticate through the
  JDBC or ODBC driver using a SAML identity provider is not supported.

## Documentation for Amazon Athena

[Amazon Athena documentation](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon Athena metadata is not permitted
  to contain export-controlled data. This metadata includes:
  - Database Name
  - Table Name
  - Partitions
  - Query Names
  - Query Strings
