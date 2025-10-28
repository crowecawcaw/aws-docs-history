# AWS Lake Formation in AWS GovCloud (US)

AWS Lake Formation helps you centrally govern, secure, and globally share data for analytics and machine learning.
With Lake Formation, you can manage fine-grained access control for your data lake data on Amazon Simple Storage Service (Amazon S3) and its metadata in
AWS Glue Data Catalog.

Lake Formation provides its own permissions model that augments the IAM permissions model.
Lake Formation permissions model enables fine-grained access to data stored in data lakes through a simple grant or revoke mechanism,
much like a relational database management system (RDBMS).
Lake Formation permissions are enforced using granular controls at the column, row, and cell-levels across AWS analytics and machine learning services,
including Amazon Athena, Quick Suite, Amazon Redshift Spectrum, Amazon EMR, and AWS Glue.

The Lake Formation hybrid access mode for AWS Glue crawler lets you secure and access the cataloged data using both Lake Formation permissions and IAM permissions policies
for Amazon S3 and AWS Glue actions.
With hybrid access mode, data administrators can onboard Lake Formation permissions selectively and incrementally, focusing on one data lake use case at a time.

Lake Formation also allows you to share data internally and externally across multiple AWS accounts, AWS organizations or directly with IAM principals in another account providing fine-grained access to the AWS Glue Data Catalog metadata and underlying data.

## How AWS Lake Formation differs for AWS GovCloud (US)

The AWS GovCloud (US) Region implementation of Lake Formation is unique in the following ways:

- Granting Lake Formation permissions to Amazon Athena users who authenticate through the JDBC or ODBC driver using a SAML identity provider is not supported.
- AWS Lake Formation blueprints are available in AWS GovCloud (US-West) only.
- AWS Lake Formation governed tables are not available.

## Documentation for AWS Lake Formation

[AWS Lake Formation documentation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No data will leave the AWS GovCloud (US) Regions for this service.
