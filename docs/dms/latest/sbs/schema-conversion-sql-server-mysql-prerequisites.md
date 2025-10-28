# Prerequisites for migrating SQL Server databases to Amazon RDS for MySQL with DMS schema conversion

The following prerequisites are also required to complete this walkthrough:

- Familiarity with the AWS Management Console, AWS Database Migration Service, and SQL.
- A user with AWS Identity and Access Management (IAM) credentials. Make sure that you can use these credentials to create an Amazon S3 bucket in your AWS Region.
- Basic knowledge of the Amazon Virtual Private Cloud (Amazon VPC) service and of security groups.
- An understanding of the supported features and limitations of DMS Schema Conversion. For more information, see [Schema conversion limitations](../userguide/CHAP_SchemaConversion.md#schema-conversion-limitations "../userguide/CHAP_SchemaConversion.md#schema-conversion-limitations").
  We recommend that you don’t use your production workloads for the migration in this walkthrough. After you get familiar with migration tools and AWS services, you can migrate your production workloads.

Make sure that you create all your AWS and DMS Schema Conversion resources in the AWS Regions that support DMS Schema Conversion. For more information, see the [list of supported Regions](../userguide/CHAP_SchemaConversion.md#schema-conversion-supported-regions "../userguide/CHAP_SchemaConversion.md#schema-conversion-supported-regions"). In other Regions, you can use the AWS Schema Conversion Tool (AWS SCT). For an example of migration from SQL Server to MySQL with AWS SCT, see [Use Schema Conversion Tool to Convert the SQL Server Schema to MySQL](chap-rdsoracle2postgresql.steps.md "chap-rdsoracle2postgresql.steps.md"). To download AWS SCT, see [Installing, verifying, and updating](../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md "../../../SchemaConversionTool/latest/userguide/CHAP_Installing.md") in the _Schema Conversion Tool User Guide_.

For more information about DMS Schema Conversion, see the [user guide](../userguide/CHAP_SchemaConversion.md "../userguide/CHAP_SchemaConversion.md").
