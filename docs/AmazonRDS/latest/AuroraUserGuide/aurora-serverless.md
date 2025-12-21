# Aurora Serverless v1 and Aurora database engine versions

###### Important

AWS has [announced the end-of-life date for Aurora Serverless v1: March 31st, 2025](https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon "https://repost.aws/questions/QUhcMVoChXRm2HLi8F-yih1g/announcement-support-for-aurora-s/announcement-support-for-aurora-serverless-v1-ending-soon"). All Aurora Serverless v1 clusters that are
not migrated by March 31, 2025 will be migrated to Aurora Serverless v2 during the maintenance window. If the upgrade fails, Amazon Aurora converts the Serverless v1
cluster to a provisioned cluster with the equivalent engine version during the maintenance window. If applicable, Amazon Aurora will enroll the
converted provisioned cluster in Amazon RDS Extended Support. For more information, see [Amazon RDS Extended Support with Amazon Aurora](extended-support.md "extended-support.md").

Aurora Serverless v1 is available in certain AWS Regions and for specific Aurora MySQL and Aurora PostgreSQL versions only. For the
current list of AWS Regions that support Aurora Serverless v1 and the specific Aurora MySQL and Aurora PostgreSQL versions available
in each Region, see [Aurora Serverless v1](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md").

Aurora Serverless v1 uses its associated Aurora database engine to identify specific supported releases for each database engine
supported, as follows:

- Aurora MySQL Serverless
- Aurora PostgreSQL Serverless
  When minor releases of the database engines become available for Aurora Serverless v1, they are applied automatically in the various
  AWS Regions where Aurora Serverless v1 is available. In other words, you don't need to upgrade your Aurora Serverless v1 DB
  cluster to get a new minor release for your cluster's DB engine when it's available for Aurora Serverless v1.

## Aurora MySQL Serverless

Aurora Serverless v1 is available in certain AWS Regions and for specific Aurora MySQL versions only. For the
current list of AWS Regions that support Aurora Serverless v1 and the specific Aurora MySQL versions available
in each Region, see [Aurora Serverless v1 with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.amy "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.amy").

To learn about enhancements
and bug fixes for Aurora MySQL version 2, see
[Database engine updates for Amazon Aurora MySQL version 2](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md")
in the _Release Notes for Aurora MySQL_.

To use a more recent version of Aurora MySQL, you can use Aurora Serverless v2.
For the AWS Regions and Aurora MySQL versions that you can use with Aurora Serverless v2, see
[Aurora Serverless v2 with Aurora MySQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.amy").
For usage information about Aurora Serverless v2, see
[Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

## Aurora PostgreSQL Serverless

Aurora Serverless v1 is available in certain AWS Regions and for specific Aurora PostgreSQL versions only. For the
current list of AWS Regions that support Aurora Serverless v1 and the specific Aurora PostgreSQL versions available
in each Region, see
[Aurora Serverless v1 with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV1.apg").

If you want to use Aurora PostgreSQL for your Aurora Serverless v1 DB cluster, you can use the Aurora PostgreSQL 13-compatible
versions. Minor releases for Aurora PostgreSQL-Compatible Edition include only changes that are backward-compatible. Your
Aurora Serverless v1 DB cluster is transparently upgraded when an Aurora PostgreSQL minor release becomes available for
Aurora Serverless v1 in your AWS Region.

To use a more recent version of Aurora PostgreSQL, you can use Aurora Serverless v2.
For the AWS Regions and Aurora PostgreSQL versions that you can use with Aurora Serverless v2, see
[Aurora Serverless v2 with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.ServerlessV2.apg").
For usage information about Aurora Serverless v2, see
[Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

##

Automatic minor version upgrades for Aurora Serverless v1

When minor releases of the database engines become available for Aurora Serverless v1,
they are applied automatically in the various AWS Regions where Aurora Serverless v1 is available.
In other words, you don't need to upgrade your Aurora Serverless v1 DB cluster to get a new
minor release for your cluster's DB engine when it's available for Aurora Serverless v1.
