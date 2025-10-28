# Prerequisties for migrating PostgreSQL databases

The following prerequisites are also required to complete this walkthrough:

- Familiarity with the Amazon Relational Database Service (Amazon RDS), AWS Database Migration Service (AWS DMS), and SQL.
- Create an AWS account with an AWS Identity and Access Management (IAM) credentials. This account should allow you to launch Amazon RDS instances and run AWS DMS data migrations in your and AWS Region. For more information, see [Create an IAM User](../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM "../../../AmazonRDS/latest/UserGuide/CHAP_SettingUp.md#CHAP_SettingUp.IAM").
- Basic knowledge of the Amazon Virtual Private Cloud (Amazon VPC) service and of security groups. For information about using Amazon VPC with Amazon RDS, see [Amazon Virtual Private Cloud (VPCs) and Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_VPC.md "../../../AmazonRDS/latest/UserGuide/USER_VPC.md"). For information about Amazon RDS security groups, see [Controlling access with security groups](../../../AmazonRDS/latest/UserGuide/Overview.md "../../../AmazonRDS/latest/UserGuide/Overview.md").
- An understanding of the supported features and limitations of homogeneous data migrations in AWS DMS. For example, you can’t apply table mapping rules to your homogeneous data migration. For more information, see [Limitations for homogeneous data migrations](../userguide/data-migrations.md#data-migrations-limitations "../userguide/data-migrations.md#data-migrations-limitations").
  We recommend that you don’t use your production workloads for the migration in this walkthrough. After you get familiar with migration tools and AWS services, you can migrate your production workloads. Also, make sure that you use a source PostgreSQL database that is version 10.5 or later.

Make sure that you create all your resources in the AWS Regions that support homogeneous data migrations in AWS DMS. For more information, see the [list of supported Regions](../userguide/data-migrations.md#data-migrations-supported-regions "../userguide/data-migrations.md#data-migrations-supported-regions").

For more information about migrating self-managed PostgreSQL databases to the AWS Cloud, [Migrating PostgreSQL Databases to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL](chap-manageddatabases.md "chap-manageddatabases.md").
