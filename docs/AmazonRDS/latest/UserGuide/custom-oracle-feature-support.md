# Feature availability and support for RDS Custom for Oracle

In this topic, you can find a summary of the RDS Custom for Oracle feature availability and support
for quick reference.

###### Topics

- [AWS Region and database version support for RDS Custom for Oracle](#custom-reqs-limits.RegionVersionAvailability "#custom-reqs-limits.RegionVersionAvailability")
- [Database version support for RDS Custom for Oracle](#custom-reqs-limits.db-version "#custom-reqs-limits.db-version")
- [Edition and licensing support for RDS Custom for Oracle](#custom-oracle-feature-support.editions "#custom-oracle-feature-support.editions")
- [DB instance class support for RDS Custom for Oracle](#custom-reqs-limits.instances "#custom-reqs-limits.instances")
- [Option group support for RDS Custom for Oracle](#custom-oracle-feature-support.option-groups "#custom-oracle-feature-support.option-groups")

## AWS Region and database version support for RDS Custom for Oracle

Feature availability and support vary across specific versions of each database
engine, and across AWS Regions. For more information on version and Region
availability of RDS Custom for Oracle, see [Supported Regions and DB engines for RDS Custom](Concepts.RDS_Fea_Regions_DB-eng.Feature.md "Concepts.RDS_Fea_Regions_DB-eng.Feature.md").

## Database version support for RDS Custom for Oracle

RDS Custom for Oracle supports the following Oracle database versions:

- Oracle Database 19c
- Oracle Database 18c
- Oracle Database 12c Release 2 (12.2)
- Oracle Database 12c Release 1 (12.1)

## Edition and licensing support for RDS Custom for Oracle

RDS Custom for Oracle supports Enterprise Edition (EE) and Standard Edition 2 (SE2) on the BYOL
model.

Note the following limitations for Standard Edition 2:

- Oracle Data Guard isn't supported. Thus, you can't create Oracle read
  replicas.
- You can only use DB instance classes that have 16 or fewer vCPUs (up to 4xlarge).
- A CDB instance on Standard Edition 2 supports a maximum of 3 tenant
  databases.
- You can't migrate data between Enterprise Edition and Standard Edition 2.

## DB instance class support for RDS Custom for Oracle

RDS Custom for Oracle supports the following DB instance classes. If you create a DB instance on
Standard Edition 2, you can only use instance classes with 16 or fewer vCPUs (up to 4x
large).

| Type      | Size                |
| --------- | ------------------- | ------------------- | ----------------------- | ------------------- | ------------------------ | -------------------- | ------------------------ | ----------------- | --------------------- | ------------------- | ----------------------- |
| db.m7i    | `db.m7i.large`      | `db.m7i.xlarge`     | <br>`db.m7i.2xlarge`    | `db.m7i.4xlarge`    | <br>`db.m7i.8xlarge`     | `db.m7i.12xlarge`    | <br>`db.m7i.16xlarge`    | `db.m7i.24xlarge` | <br>`db.m7i.48xlarge` | `db.m7i.metal-24xl` | <br>`db.m7i.metal-48xl` |
| db.m6i    | `db.m6i.large`      | `db.m6i.xlarge`     | <br>`db.m6i.2xlarge`    | `db.m6i.4xlarge`    | <br>`db.m6i.8xlarge`     | `db.m6i.12xlarge`    | <br>`db.m6i.16xlarge`    | `db.m6i.24xlarge` | <br>`db.m6i.32xlarge` | `db.m6i.metal`      |
| db.m6id   | `db.m6id.metal`     |
| db.m6in   | `db.m6in.metal`     |
| db.m5     | `db.m5.large`       | `db.m5.xlarge`      | <br>`db.m5.2xlarge`     | `db.m5.4xlarge`     | <br>`db.m5.8xlarge`      | `db.m5.12xlarge`     | <br>`db.m5.16xlarge`     | `db.m5.24xlarge`  |
| db.r7i    | `db.r7i.large`      | `db.r7i.xlarge`     | <br>`db.r7i.2xlarge`    | `db.r7i.4xlarge`    | <br>`db.r7i.8xlarge`     | `db.r7i.12xlarge`    | <br>`db.r7i.16xlarge`    | `db.r7i.24xlarge` | <br>`db.r7i.48xlarge` | `db.r7i.metal-24xl` | <br>`db.r7i.metal-48xl` |
| db.r6i    | `db.r6i.large`      | `db.r6i.xlarge`     | <br>`db.r6i.2xlarge`    | `db.r6i.4xlarge`    | <br>`db.r6i.8xlarge`     | `db.r6i.12xlarge`    | <br>`db.r6i.16xlarge`    | `db.r6i.24xlarge` | <br>`db.r6i.32xlarge` | `db.r6i.metal`      |
| db.r6id   | `db.r6id.metal`     |
| db.r6in   | `db.r6in.metal`     |
| db.r5b    | `db.r5b.large`      | `db.r5b.xlarge`     | <br>`db.r5b.2xlarge`    | `db.r5b.4xlarge`    | <br>`db.r5b.8xlarge`     | `db.r5b.12xlarge`    | <br>`db.r5b.16xlarge`    | `db.r5b.24xlarge` |
| db.r5     | `db.r5.large`       | `db.r5.xlarge`      | <br>`db.r5.2xlarge`     | `db.r5.4xlarge`     | <br>`db.r5.8xlarge`      | `db.r5.12xlarge`     | <br>`db.r5.16xlarge`     | `db.r5.24xlarge`  |
| db.x2iedn | `db.x2iedn.xlarge`  | `db.x2iedn.2xlarge` | <br>`db.x2iedn.4xlarge` | `db.x2iedn.8xlarge` | <br>`db.x2iedn.16xlarge` | `db.x2iedn.24xlarge` | <br>`db.x2iedn.32xlarge` | `db.x2iedn.metal` |
| db.x2idn  | `db.x2idn.metal`    |
| db.x2iezn | `db.x2iezn.2xlarge` | `db.x2iezn.4xlarge` | <br>`db.x2iezn.6xlarge` | `db.x2iezn.8xlarge` | <br>`db.x2iezn.12xlarge` | `db.x2iezn.metal`    |
| db.t3     | `db.t3.medium`      | `db.t3.large`       | <br>`db.t3.xlarge`      | `db.t3.2xlarge`     |

## Option group support for RDS Custom for Oracle

You can specify an option group when you create or modify an RDS Custom for Oracle DB instance. For more
information, see [Working with option groups in RDS Custom for Oracle](custom-oracle-option-groups.md "custom-oracle-option-groups.md").
