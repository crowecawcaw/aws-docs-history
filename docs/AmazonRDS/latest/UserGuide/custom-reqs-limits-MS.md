# Requirements and limitations for Amazon RDS Custom for SQL Server

Following, you can find a summary of the Amazon RDS Custom for SQL Server requirements and limitations
for quick reference. Requirements and limitations also appear in the relevant sections.

###### Topics

- [Region and version availability](#custom-reqs-limits-MS.RegionVersionAvailability "#custom-reqs-limits-MS.RegionVersionAvailability")
- [General requirements for
  RDS Custom for SQL Server](#custom-reqs-limits.reqsMS "#custom-reqs-limits.reqsMS")
- [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md")
- [Limitations for RDS Custom for SQL Server](#custom-reqs-limits.limitsMS "#custom-reqs-limits.limitsMS")
- [Setting character sets and collations for
  RDS Custom for SQL Server DB instances](custom-reqs-limits-MS.md "custom-reqs-limits-MS.md")
- [Local time zone for RDS Custom for SQL Server DB instances](custom-reqs-limits-MS.md "custom-reqs-limits-MS.md")
- [Using a Service Master Key with RDS Custom for SQL Server](custom-sqlserver-features.md "custom-sqlserver-features.md")
- [Change data capture (CDC) support with RDS Custom for SQL Server](custom-sqlserver-features.md "custom-sqlserver-features.md")

## Region and version availability

Feature availability and support varies across specific versions of each database engine, and across AWS Regions.
For more information on version and Region availability of Amazon RDS with Amazon RDS Custom for SQL Server, see
[Supported
Regions and DB engines for RDS Custom for SQL Server](Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq "Concepts.RDS_Fea_Regions_DB-eng.Feature.md#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.sq").

## General requirements for

RDS Custom for SQL Server

Make sure to follow these requirements for Amazon RDS Custom for SQL Server:

- Use the instance classes shown in [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md"). The only storage types supported are solid state drives (SSD) of types
  gp2, gp3, io1, and io2 Block Express. The maximum storage limit for io1, gp2, and gp3 is 16 TiB while io2 supports 64 TiB.
- Make sure that you have a symmetric encryption AWS KMS key to create an RDS Custom DB instance. For more information, see
  [Make sure that you have a symmetric encryption AWS KMS key](custom-setup-sqlserver.md#custom-setup-sqlserver.cmk "custom-setup-sqlserver.md#custom-setup-sqlserver.cmk").
- Make sure that you create an AWS Identity and Access Management (IAM) role and instance profile.
  For more information, see [Creating your IAM role and instance profile manually](custom-setup-sqlserver.md#custom-setup-sqlserver.iam "custom-setup-sqlserver.md#custom-setup-sqlserver.iam") and [Automated instance profile creation using the AWS Management Console](custom-setup-sqlserver.md#custom-setup-sqlserver.instanceProfileCreation "custom-setup-sqlserver.md#custom-setup-sqlserver.instanceProfileCreation").
- Make sure to supply a networking configuration that RDS Custom can use to access other AWS services. For specific
  requirements, see [Step 2: Configure networking, instance profile, and encryption](custom-setup-sqlserver.md#custom-setup-sqlserver.iam-vpc "custom-setup-sqlserver.md#custom-setup-sqlserver.iam-vpc").
- The combined number of RDS Custom and Amazon RDS DB instances can't exceed your quota limit. For example, if your quota is
  40 DB instances, you can have 20 RDS Custom for SQL Server DB instances and 20 Amazon RDS DB instances.
- RDS Custom automatically creates an AWS CloudTrail trail whose name begins with `do-not-delete-rds-custom-`.
  The RDS Custom support perimeter relies on the events from CloudTrail to determine whether your actions affect RDS Custom automation.
  RDS Custom creates the trail when you create your first DB instance.
  To use an already existing CloudTrail, contact AWS Support. For more information, see
  [AWS CloudTrail](custom-concept.md#custom-concept.components.CloudTrail "custom-concept.md#custom-concept.components.CloudTrail").

## Limitations for RDS Custom for SQL Server

The following limitations apply to RDS Custom for SQL Server:

- You can't create read replicas in Amazon RDS for RDS Custom for SQL Server DB instances. However, you can configure high
  availability automatically with a Multi-AZ deployment. For more information, see [Managing a Multi-AZ deployment for RDS Custom for SQL Server](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md").
- You can't modify the DB instance identifier of an existing RDS Custom for SQL Server DB instance.
- For an RDS Custom for SQL Server DB instance that wasn't created with a custom engine version
  (CEV), changes to the Microsoft Windows operating system aren't
  guaranteed to persist. For example, you lose these changes when you
  initiate a snapshot or point-in-time restore operation. If the RDS Custom for SQL Server DB instance
  was created with a CEV, then those changes are persisted.
- Not all options are supported. For example, when you create an RDS Custom for SQL Server DB instance, you can't do the following:
  - Change the number of CPU cores and threads per core on the DB instance class.
  - Turn on storage autoscaling.
  - Specify your own DB parameter group, option group, or character set.
  - Turn on Performance Insights or Database Insights.
  - Turn on automatic minor version upgrade.

- The maximum DB instance storage is 64 TiB.
- You can't use RDS Proxy with RDS Custom for SQL Server.
- You can't use the `describe-reserved-db-instances` API for RDS Custom for SQL Server
  DB instances.
