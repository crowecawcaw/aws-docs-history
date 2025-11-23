# How AWS Schema Conversion Tool uses AWS Secrets Manager

You can use the AWS Schema Conversion Tool (AWS SCT) to convert your existing database schema from
one database engine to another. You can convert relational OLTP schema, or data
warehouse schema. Your converted schema is suitable for an Amazon Relational Database Service (Amazon RDS) MySQL,
MariaDB, Oracle, SQL Server, PostgreSQL DB, an Amazon Aurora DB cluster, or an Amazon Redshift
cluster. The converted schema can also be used with a database on an Amazon Elastic Compute Cloud instance
or stored as data on an S3 bucket.

When you convert a database schema, AWS SCT can use database credentials that you
store in AWS Secrets Manager. For more information, see [Using AWS Secrets Manager in the AWS SCT user interface](../../../SchemaConversionTool/latest/userguide/CHAP_UserInterface.md#CHAP_UserInterface.SecretsManager "../../../SchemaConversionTool/latest/userguide/CHAP_UserInterface.md#CHAP_UserInterface.SecretsManager") in the
_AWS Schema Conversion Tool User Guide_.
