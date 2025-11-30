# Prerequisties for migrating from an Amazon RDS for SQL Server database to an Amazon S3 data lake

The following prerequisites are required to complete this walkthrough:

- Understand Amazon Relational Database Service (Amazon RDS), the applicable database technologies, and SQL.
- Create a user with AWS Identity and Access Management (IAM) credentials that allows you to launch Amazon RDS and AWS Database Migration Service (AWS DMS) instances in your AWS Region. For information about IAM credentials, see [Create an IAM user](../userguide/CHAP_GettingStarted.md#CHAP_SettingUp.IAM "../userguide/CHAP_GettingStarted.md#CHAP_SettingUp.IAM").
- Understand the Amazon Virtual Private Cloud (Amazon VPC) service and security groups. For information about using Amazon VPC with Amazon RDS, see [Amazon Virtual Private Cloud (VPCs) and Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md"). For information about Amazon RDS security groups, see [Controlling access with security groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md").
- Understand the supported features and limitations of AWS DMS. For information about AWS DMS, see [What is Database Migration Service](../userguide/Welcome.md "../userguide/Welcome.md").
- Understand how to work with Microsoft SQL Server as a source and Amazon S3 data lake as a target. For information about working with SQL Server as a source, see [Using a Microsoft SQL Server database as a source](../userguide/CHAP_Source.md "../userguide/CHAP_Source.md"). For information about working with Amazon S3 as a target, see [Using Amazon S3 as a target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md").
- Understand the supported data type conversion options for SQL Server and Amazon S3. For information about data types for SQL Server as a source, see [Source data types for SQL Server](../userguide/CHAP_Source.md#CHAP_Source.SQLServer.DataTypes "../userguide/CHAP_Source.md#CHAP_Source.SQLServer.DataTypes"). For information about data types for Amazon S3 as a target (Parquet only), see [Target data types for S3 Parquet](../userguide/CHAP_Target.md#CHAP_Target.S3.DataTypes "../userguide/CHAP_Target.md#CHAP_Target.S3.DataTypes").
- Audit your source SQL Server database. For each schema and all the objects under each schema, determine whether any of the objects are no longer being used. Deprecate these objects on the source SQL Server database, because there’s no need to migrate them if they aren’t being used.
  For more information about AWS DMS, see [Getting started with Database Migration Service](../userguide/CHAP_GettingStarted.md "../userguide/CHAP_GettingStarted.md").

To estimate what it will cost to run this walkthrough on AWS, you can use the AWS Pricing Calculator. For more information, see [https://calculator.aws/](https://calculator.aws/ "https://calculator.aws/").

To avoid additional charges, delete all resources after you complete the walkthrough.
