# Supported DB engines for DB instance classes

The following are DB engine–specific considerations for DB instance classes:

**Db2**

DB instance class support varies according to the version and edition of Db2. For
instance class support by version and edition, see [Amazon RDS for Db2 instance classes](Db2.Concepts.General.md "Db2.Concepts.General.md").

**Microsoft SQL Server**

DB instance class support varies according to the version and edition of SQL
Server. For instance class support by version and edition, see [DB instance class support for Microsoft SQL Server](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md").

**Oracle**

DB instance class support varies according to the Oracle Database version and
edition. RDS for Oracle supports additional memory-optimized instance classes. These
classes have names of the form
db.r5.`instance_size`.tpc`threads_per_core`.mem`ratio`.
For the vCPU count and memory allocation for each optimized class, see [Supported RDS for Oracle DB instance
classes](Oracle.Concepts.md#Oracle.Concepts.InstanceClasses.Supported "Oracle.Concepts.md#Oracle.Concepts.InstanceClasses.Supported").

**RDS Custom**

For information about the DB instance classes supported in RDS Custom, see [DB instance class support for RDS Custom for Oracle](custom-oracle-feature-support.md#custom-reqs-limits.instances "custom-oracle-feature-support.md#custom-reqs-limits.instances") and [DB instance class support for RDS Custom for SQL Server](custom-reqs-limits.md "custom-reqs-limits.md").

In the following table, you can find details about supported Amazon RDS DB instance classes for each
Amazon RDS DB engine. The cell for each engine contains one of the following values:

Yes

The instance class is supported for all versions of the DB engine.

No

The instance class isn't supported for the DB engine.

`specific-versions`

The instance class is supported only for the specified database versions of
the DB engine.

Amazon RDS periodically deprecates major and minor DB engine versions. Not all AWS Regions might
have support for earlier engine versions. For information about current supported versions,
see topics for the individual DB engines: [Db2
versions](Db2.Concepts.md#Db2.Concepts.VersionMgmt.Supported "Db2.Concepts.md#Db2.Concepts.VersionMgmt.Supported"), [MariaDB
versions](MariaDB.Concepts.md#MariaDB.Concepts.VersionMgmt.Supported "MariaDB.Concepts.md#MariaDB.Concepts.VersionMgmt.Supported"), [Microsoft SQL
Server versions](SQLServer.Concepts.General.md "SQLServer.Concepts.General.md"), [MySQL
versions](MySQL.Concepts.md "MySQL.Concepts.md"), [Oracle versions](Oracle.Concepts.md "Oracle.Concepts.md"),
and [PostgreSQL
versions](PostgreSQL.Concepts.General.md "PostgreSQL.Concepts.General.md").

###### Topics

- [Supported DB engines for general-purpose instance
  classes](#gen-purpose-inst-classes "#gen-purpose-inst-classes")
- [Supported DB engines for memory-optimized instance
  classes](#mem-opt-inst-classes "#mem-opt-inst-classes")
- [Supported DB engines for compute-optimized instance
  classes](#compute-opt-inst-classes "#compute-opt-inst-classes")
- [Supported DB engines for burstable-performance instance
  classes](#burstable-inst-classes "#burstable-inst-classes")
- [Supported DB engines for Optimized Reads instance
  classes](#read-opt-inst-classes "#read-opt-inst-classes")

## Supported DB engines for general-purpose instance

classes

The following tables show the supported databases and database versions for the
general-purpose instance classes.

**db.m8g – general-purpose instance classes powered by AWS
Graviton4 processors**

| Instance class  | Db2 | MariaDB                                                                                                                          | Microsoft SQL Server | MySQL                   | Oracle | PostgreSQL                                                                                                     |
| --------------- | --- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------- | ------ | -------------------------------------------------------------------------------------------------------------- |
| db.m8g.48xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.24xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.16xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.12xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.8xlarge  | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.4xlarge  | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.2xlarge  | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.xlarge   | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m8g.large    | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |

**db.m7i – general-purpose instance classes powered by 4th
generation Intel Xeon Scalable processors**

| Instance class    | Db2      | MariaDB                                         | Microsoft SQL Server | MySQL                   | Oracle                             | PostgreSQL                                                                                                     |
| ----------------- | -------- | ----------------------------------------------- | -------------------- | ----------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| db.m7i.48xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, Enterprise Edition only | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.24xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, Enterprise Edition only | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.16xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, Enterprise Edition only | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.12xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, Enterprise Edition only | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.8xlarge    | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, Enterprise Edition only | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.4xlarge    | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.2xlarge    | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.xlarge     | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.large      | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.m7i.metal-48xl | No       | No                                              | No                   | No                      | BYOL only, Enterprise Edition only | No                                                                                                             |
| db.m7i.metal-24xl | No       | No                                              | No                   | No                      | BYOL only, Enterprise Edition only | No                                                                                                             |

**db.m7g – general-purpose instance classes powered by AWS
Graviton3 processors**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                           |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| db.m7g.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.m7g.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.m7g.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.m7g.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.m7g.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.m7g.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.m7g.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |

**db.m6g – general-purpose instance classes powered by AWS
Graviton2 processors**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                      |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------- |
| db.m6g.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.m6g.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.m6g.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.m6g.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.m6g.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.m6g.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.m6g.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |

**db.m6gd – general-purpose instance classes powered by AWS
Graviton2 processors and SSD storage**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                           |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------------ |
| db.m6gd.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |
| db.m6gd.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |
| db.m6gd.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |
| db.m6gd.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |
| db.m6gd.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |
| db.m6gd.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |
| db.m6gd.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, and 14 versions; 13.7 and higher 13 versions; and<br>13.4 |

**db.m6id – general-purpose instance classes powered by 3rd
generation Intel Xeon Scalable processors and SSD storage**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                                                                                           |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| db.m6id.32xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6id.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                                                                                   |

**db.m6idn – general-purpose instance classes with 3rd
Generation Intel Xeon Scalable processors, SSD storage, and network
optimization**

| Instance class    | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                           |
| ----------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| db.m6idn.32xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.m6idn.large    | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |

**db.m6in – general-purpose instance classes powered by 3rd
generation Intel Xeon Scalable processors and network optimization**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                                                                                                                                                          |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| db.m6in.32xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.large    | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.m6in.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                                                                                                                                                  |

**db.m6i – general-purpose instance classes powered by 3rd
generation Intel Xeon Scalable processors**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL             |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | ---------------------- |
| db.m6i.32xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.24xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.16xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.12xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.large    | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Oracle Database 19c                | All available versions |
| db.m6i.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                     |

**db.m5d – general-purpose instance classes powered by Intel
Xeon Platinum processors and SSD storage**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                                 |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| db.m5d.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.m5d.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |

**db.m5 – general-purpose instance classes 2.5 GHz Intel Xeon
Platinum processors**

| Instance class | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle | PostgreSQL                                                                                                             |
| -------------- | --- | ------- | -------------------- | ----- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| db.m5.24xlarge | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.16xlarge | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.12xlarge | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.8xlarge  | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.4xlarge  | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.2xlarge  | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.xlarge   | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.m5.large    | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |

**db.m4 – general-purpose instance classes with Intel Xeon
processors**

| Instance class | Db2 | MariaDB    | Microsoft SQL Server | MySQL      | Oracle     | PostgreSQL |
| -------------- | --- | ---------- | -------------------- | ---------- | ---------- | ---------- |
| db.m4.16xlarge | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.m4.10xlarge | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.m4.4xlarge  | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.m4.2xlarge  | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.m4.xlarge   | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.m4.large    | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |

**db.m3 – general-purpose instance classes**

| Instance class | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle     | PostgreSQL |
| -------------- | --- | ------- | -------------------- | ----- | ---------- | ---------- |
| db.m3.2xlarge  | No  | No      | Deprecated           | Yes   | Deprecated | Deprecated |
| db.m3.xlarge   | No  | No      | Deprecated           | Yes   | Deprecated | Deprecated |
| db.m3.large    | No  | No      | Deprecated           | Yes   | Deprecated | Deprecated |
| db.m3.medium   | No  | No      | Deprecated           | Yes   | Deprecated | Deprecated |

## Supported DB engines for memory-optimized instance

classes

The following tables show the supported databases and database versions for the
memory-optimized instance classes.

**db.z1d – memory-optimized instance classes**

| Instance class  | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle | PostgreSQL |
| --------------- | --- | ------- | -------------------- | ----- | ------ | ---------- |
| db.z1d.12xlarge | No  | No      | Yes                  | No    | Yes    | No         |
| db.z1d.6xlarge  | No  | No      | Yes                  | No    | Yes    | No         |
| db.z1d.3xlarge  | No  | No      | Yes                  | No    | Yes    | No         |
| db.z1d.2xlarge  | No  | No      | Yes                  | No    | Yes    | No         |
| db.z1d.xlarge   | No  | No      | Yes                  | No    | Yes    | No         |
| db.z1d.large    | No  | No      | Yes                  | No    | Yes    | No         |

**db.x2g – memory-optimized instance classes powered by AWS Graviton2 processors**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                      |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------- |
| db.x2g.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.x2g.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.x2g.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.x2g.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.x2g.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.x2g.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.x2g.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |

**db.x2idn – memory-optimized instance classes powered by 3rd generation Intel Xeon Scalable processors**

| Instance class    | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                             |
| ----------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | -------------------------------------- |
| db.x2idn.32xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | Enterprise Edition only            | PostgreSQL 15 versions, 14.6, and 13.9 |
| db.x2idn.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | Enterprise Edition only            | PostgreSQL 15 versions, 14.6, and 13.9 |
| db.x2idn.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | Enterprise Edition only            | PostgreSQL 15 versions, 14.6, and 13.9 |
| db.x2idn.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                     |

**db.x2iedn – memory-optimized instance classes with local NVMe-based SSDs, powered by
3rd generation Intel Xeon Scalable processors**

| Instance class     | Db2 | MariaDB                                         | Microsoft SQL Server                                                       | MySQL             | Oracle                                          | PostgreSQL                                                                                                 |
| ------------------ | --- | ----------------------------------------------- | -------------------------------------------------------------------------- | ----------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| db.x2iedn.32xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition only                         | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.24xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition only                         | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.16xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition only                         | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition only                         | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition and Standard Edition 2 (SE2) | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition and Standard Edition 2 (SE2) | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Enterprise and Standard Editions only, SQL Server 2014 12.00 and<br>higher | MySQL 8.4 and 8.0 | Enterprise Edition and Standard Edition 2 (SE2) | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.x2iedn.metal    | No  | No                                              | No                                                                         | No                | BYOL only, Enterprise Edition only              | No                                                                                                         |

**db.x2iezn – memory-optimized instance classes powered by 2nd generation Intel Xeon
Scalable processors**

| Instance class    | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle                                          | PostgreSQL |
| ----------------- | --- | ------- | -------------------- | ----- | ----------------------------------------------- | ---------- |
| db.x2iezn.metal   | No  | No      | No                   | No    | BYOL only, Enterprise Edition only              | No         |
| db.x2iezn.8xlarge | No  | No      | No                   | No    | Enterprise Edition only                         | No         |
| db.x2iezn.6xlarge | No  | No      | No                   | No    | Enterprise Edition only                         | No         |
| db.x2iezn.4xlarge | No  | No      | No                   | No    | Enterprise Edition and Standard Edition 2 (SE2) | No         |
| db.x2iezn.2xlarge | No  | No      | No                   | No    | Enterprise Edition and Standard Edition 2 (SE2) | No         |

**db.x1e – memory-optimized instance classes**

| Instance class  | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle      | PostgreSQL |
| --------------- | --- | ------- | -------------------- | ----- | ----------- | ---------- |
| db.x1e.32xlarge | No  | No      | Yes                  | No    | Deprecated1 | No         |
| db.x1e.16xlarge | No  | No      | Yes                  | No    | Deprecated1 | No         |
| db.x1e.8xlarge  | No  | No      | Yes                  | No    | Deprecated1 | No         |
| db.x1e.4xlarge  | No  | No      | Yes                  | No    | Deprecated1 | No         |
| db.x1e.2xlarge  | No  | No      | Yes                  | Nos   | Deprecated1 | No         |
| db.x1e.xlarge   | No  | No      | Yes                  | No    | Deprecated1 | No         |

1 You can no longer create RDS for Oracle DB instances using the X1
instance class family. If you currently use X1 classes, switch to a new generation instance
class as soon as possible. Starting on January 22, 2025, RDS begins automated upgrades in
your defined maintenance window. During the upgrade, RDS chooses the equivalent X2iedn
instance type and upgrades it. For more information, see the re:Post article [Amazon RDS for Oracle is ending
support for X1 Database Instances on January 22, 2025](https://repost.aws/articles/ARM9RDhfR2Tz2nFmKwpcjCSQ "https://repost.aws/articles/ARM9RDhfR2Tz2nFmKwpcjCSQ").

**db.x1 – memory-optimized instance classes**

| Instance class | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle      | PostgreSQL |
| -------------- | --- | ------- | -------------------- | ----- | ----------- | ---------- |
| db.x1.32xlarge | No  | No      | Yes                  | No    | Deprecated1 | No         |
| db.x1.16xlarge | No  | No      | Yes                  | No    | Deprecated1 | No         |

1 You can no longer create RDS for Oracle DB instances using the X1
instance class family. If you currently use X1 classes, switch to a new generation instance
class as soon as possible. Starting on January 22, 2025, RDS begins automated upgrades in
your defined maintenance window. During the upgrade, RDS chooses the equivalent X2iedn
instance type and upgrades it. For more information, see the re:Post article [Amazon RDS for Oracle is ending
support for X1 Database Instances on January 22, 2025](https://repost.aws/articles/ARM9RDhfR2Tz2nFmKwpcjCSQ "https://repost.aws/articles/ARM9RDhfR2Tz2nFmKwpcjCSQ").

**db.r8g – memory-optimized instance classes powered by AWS Graviton4
processors**

| Instance class  | Db2 | MariaDB                                                                                                                          | Microsoft SQL Server | MySQL                   | Oracle | PostgreSQL                                                                                                     |
| --------------- | --- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------- | ------ | -------------------------------------------------------------------------------------------------------------- |
| db.r8g.48xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.24xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.16xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.12xlarge | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.8xlarge  | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.4xlarge  | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.2xlarge  | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.xlarge   | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r8g.large    | No  | MariaDB 11.8.3 and higher, 11.4.3 and higher, 10.11.7 and higher, 10.6.13 and higher, 10.5.20 and higher, and 10.4.29 and higher | No                   | MySQL 8.0.32 and higher | No     | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |

**db.r7i – memory-optimized instance classes preconfigured for high memory,
storage, and I/O**

| Instance class            | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle                                               | PostgreSQL |
| ------------------------- | --- | ------- | -------------------- | ----- | ---------------------------------------------------- | ---------- |
| db.r7i.8xlarge.tpc2.mem3x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.8xlarge.tpc2.mem2x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.6xlarge.tpc2.mem4x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.6xlarge.tpc2.mem2x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.4xlarge.tpc2.mem4x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.4xlarge.tpc2.mem3x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.4xlarge.tpc2.mem2x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.3xlarge.tpc2.mem4x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.2xlarge.tpc2.mem8x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.2xlarge.tpc2.mem4x | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.xlarge.tpc2.mem4x  | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |
| db.r7i.xlarge.tpc2.mem2x  | No  | No      | No                   | No    | BYOL only, Enterprise Edition and Standard Edition 2 | No         |

**db.r7i – memory-optimized instance classes powered by 4th
generation Intel Xeon Scalable processors**

| Instance class    | Db2      | MariaDB                                         | Microsoft SQL Server | MySQL                   | Oracle                             | PostgreSQL                                                                                                     |
| ----------------- | -------- | ----------------------------------------------- | -------------------- | ----------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| db.r7i.48xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only                          | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.24xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only                          | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.16xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only                          | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.12xlarge   | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only                          | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.8xlarge    | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only                          | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.4xlarge    | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.2xlarge    | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.xlarge     | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.large      | Db2 11.5 | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.0.32 and higher | BYOL only, all editions            | PostgreSQL version 17.1 and higher, 16.1 and higher, 15.4 and higher, 14.9<br>and higher, and 13.11 and higher |
| db.r7i.metal-48xl | No       | No                                              | No                   | No                      | BYOL only, Enterprise Edition only | No                                                                                                             |
| db.r7i.metal-24xl | No       | No                                              | No                   | No                      | BYOL only, Enterprise Edition only | No                                                                                                             |

**db.r7g – memory-optimized instance classes powered by AWS Graviton3
processors**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                           |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| db.r7g.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.r7g.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.r7g.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.r7g.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.r7g.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.r7g.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |
| db.r7g.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.4 and higher 13 versions |

**db.r6g – memory-optimized instance classes powered by AWS Graviton2
processors**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                      |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------- |
| db.r6g.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r6g.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r6g.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r6g.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r6g.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r6g.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r6g.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |

**db.r6gd – memory-optimized instance classes powered by AWS Graviton2
processors**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                                   |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| db.r6gd.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |

**db.r6id – memory-optimized instance classes powered by 3rd generation Intel Xeon
Scalable processors**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                                                                                           |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| db.r6id.32xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                                                                                   |

**db.r6idn – memory-optimized instance classes powered by 3rd generation
Intel Xeon Scalable processors**

| Instance class    | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                           |
| ----------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| db.r6idn.32xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.24xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.16xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.12xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6idn.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |

**db.r6in – memory-optimized instance classes powered by 3rd generation Intel Xeon
Scalable processors**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                                                                                                                                                          |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| db.r6in.32xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.24xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.16xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.12xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.large    | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.3 and higher 14 versions, 13.7 and higher 13 versions,<br>12.11 and higher 12 versions, and 11.16 and higher 11 versions |
| db.r6in.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                                                                                                                                                  |

**db.r6i – memory-optimized instance classes preconfigured for high memory,
storage, and I/O**

| Instance class            | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle                  | PostgreSQL |
| ------------------------- | --- | ------- | -------------------- | ----- | ----------------------- | ---------- |
| db.r6i.8xlarge.tpc2.mem4x | No  | No      | No                   | No    | Enterprise Edition only | No         |
| db.r6i.8xlarge.tpc2.mem3x | No  | No      | No                   | No    | Enterprise Edition only | No         |
| db.r6i.6xlarge.tpc2.mem4x | No  | No      | No                   | No    | Enterprise Edition only | No         |
| db.r6i.4xlarge.tpc2.mem4x | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.4xlarge.tpc2.mem3x | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.4xlarge.tpc2.mem2x | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.2xlarge.tpc2.mem8x | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.2xlarge.tpc2.mem4x | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.2xlarge.tpc1.mem2x | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.xlarge.tpc2.mem4x  | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.xlarge.tpc2.mem2x  | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |
| db.r6i.large.tpc1.mem2x   | No  | No      | No                   | No    | EE and SE2 BYOL         | No         |

**db.r6i – memory-optimized instance classes**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                                                                                                                                                           |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| db.r6i.32xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.24xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.16xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.12xlarge | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.8xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.4xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.2xlarge  | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.xlarge   | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.large    | Yes | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes                                | All PostgreSQL 17, 16, 15, and 14 versions, 13.4 and higher 13 versions, 12.8 and higher 12 versions, 11.13 and higher 11 versions, and 10.21 and higher 10 versions |
| db.r6i.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                                                                                                                                                   |

**db.r5d – memory-optimized instance classes**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                                 |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| db.r5d.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |
| db.r5d.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and 13.4 |

**db.r5b – memory-optimized instance classes preconfigured for high memory,
storage, and I/O**

| Instance class            | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle | PostgreSQL |
| ------------------------- | --- | ------- | -------------------- | ----- | ------ | ---------- |
| db.r5b.8xlarge.tpc2.mem3x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.6xlarge.tpc2.mem4x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.4xlarge.tpc2.mem4x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.4xlarge.tpc2.mem3x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.4xlarge.tpc2.mem2x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.2xlarge.tpc2.mem8x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.2xlarge.tpc2.mem4x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.2xlarge.tpc1.mem2x | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.xlarge.tpc2.mem4x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.xlarge.tpc2.mem2x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5b.large.tpc1.mem2x   | No  | No      | No                   | No    | Yes    | No         |

**db.r5b – memory-optimized instance classes**

| Instance class  | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                      |
| --------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------- |
| db.r5b.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | >Yes   | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.r5b.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | Yes                  | MySQL 8.4 and 8.0 | Yes    | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |

**db.r5 – memory-optimized instance classes preconfigured for high memory,
storage, and I/O**

| Instance class            | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle | PostgreSQL |
| ------------------------- | --- | ------- | -------------------- | ----- | ------ | ---------- |
| db.r5.12xlarge.tpc2.mem2x | No  | No      | No                   | No    | Yes    | No         |
| db.r5.8xlarge.tpc2.mem3x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.6xlarge.tpc2.mem4x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.4xlarge.tpc2.mem4x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.4xlarge.tpc2.mem3x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.4xlarge.tpc2.mem2x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.2xlarge.tpc2.mem8x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.2xlarge.tpc2.mem4x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.2xlarge.tpc1.mem2x  | No  | No      | No                   | No    | Yes    | No         |
| db.r5.xlarge.tpc2.mem4x   | No  | No      | No                   | No    | Yes    | No         |
| db.r5.xlarge.tpc2.mem2x   | No  | No      | No                   | No    | Yes    | No         |
| db.r5.large.tpc1.mem2x    | No  | No      | No                   | No    | Yes    | No         |

**db.r5 – memory-optimized instance classes**

| Instance class | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle | PostgreSQL                                                                                                             |
| -------------- | --- | ------- | -------------------- | ----- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| db.r5.24xlarge | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.16xlarge | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.12xlarge | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.8xlarge  | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.4xlarge  | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.2xlarge  | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.xlarge   | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |
| db.r5.large    | No  | Yes     | Yes                  | Yes   | Yes    | All PostgreSQL 17, 16, 15, 14, 13, 12, and 11 versions; 10.17 and higher 10 versions; and 9.6.22 and higher 9 versions |

**db.r4 – memory-optimized instance classes**

| Instance class | Db2 | MariaDB    | Microsoft SQL Server | MySQL      | Oracle     | PostgreSQL |
| -------------- | --- | ---------- | -------------------- | ---------- | ---------- | ---------- |
| db.r4.16xlarge | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.r4.8xlarge  | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.r4.4xlarge  | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.r4.2xlarge  | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.r4.xlarge   | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.r4.large    | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |

**db.r3 – memory-optimized instance classes**

| Instance class    | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL | Oracle     | PostgreSQL |
| ----------------- | --- | ----------------------------------------------- | -------------------- | ----- | ---------- | ---------- |
| db.r3.8xlarge\*\* | No  | All MariaDB 10.6, 10.5, 10.4, and 10.3 versions | Deprecated           | Yes   | Deprecated | Deprecated |
| db.r3.4xlarge     | No  | All MariaDB 10.6, 10.5, 10.4, and 10.3 versions | Deprecated           | Yes   | Deprecated | Deprecated |
| db.r3.2xlarge     | No  | All MariaDB 10.6, 10.5, 10.4, and 10.3 versions | Deprecated           | Yes   | Deprecated | Deprecated |
| db.r3.xlarge      | No  | All MariaDB 10.6, 10.5, 10.4, and 10.3 versions | Deprecated           | Yes   | Deprecated | Deprecated |
| db.r3.large       | No  | All MariaDB 10.6, 10.5, 10.4, and 10.3 versions | Deprecated           | Yes   | Deprecated | Deprecated |

## Supported DB engines for compute-optimized instance

classes

The following tables show the supported databases and database versions for the
compute-optimized instance classes.

**db.c6gd – compute-optimized instance classes (for Multi-AZ DB cluster deployments
only)**

| Instance class   | Db2 | MariaDB | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                                   |
| ---------------- | --- | ------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| db.c6gd.16xlarge | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.12xlarge | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.8xlarge  | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.4xlarge  | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.2xlarge  | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.xlarge   | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.large    | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |
| db.c6gd.medium   | No  | No      | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, and 15 versions; 14.5 and higher 14 versions; 13.4 and<br>13.7 and higher 13 versions |

## Supported DB engines for burstable-performance instance

classes

The following tables show the supported databases and database versions for the
burstable-performance instance classes.

**db.t4g – burstable-performance instance classes powered by AWS Graviton2
processors**

| Instance class | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                      |
| -------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------- |
| db.t4g.2xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.t4g.xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.t4g.large   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.t4g.medium  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.t4g.small   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |
| db.t4g.micro   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16, 15, 14, and 13 versions; and 12.7 and higher 12 versions |

**db.t3 – burstable-performance instance classes**

| Instance class | Db2 | MariaDB | Microsoft SQL Server | MySQL | Oracle                                                                | PostgreSQL                                                                                   |
| -------------- | --- | ------- | -------------------- | ----- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| db.t3.2xlarge  | Yes | Yes     | Yes                  | Yes   | Yes                                                                   | All PostgreSQL 17, 16, 15, 14, 13, 12, 11, and 10 versions; and 9.6.22 and higher 9 versions |
| db.t3.xlarge   | Yes | Yes     | Yes                  | Yes   | Yes                                                                   | All PostgreSQL 17, 16, 15, 14, 13, 12, 11, and 10 versions; and 9.6.22 and higher 9 versions |
| db.t3.large    | Yes | Yes     | Yes                  | Yes   | Yes                                                                   | All PostgreSQL 17, 16, 15, 14, 13, 12, 11, and 10 versions; and 9.6.22 and higher 9 versions |
| db.t3.medium   | Yes | Yes     | Yes                  | Yes   | Yes                                                                   | All PostgreSQL 17, 16, 15, 14, 13, 12, 11, and 10 versions; and 9.6.22 and higher 9 versions |
| db.t3.small    | Yes | Yes     | Yes                  | Yes   | Yes                                                                   | All PostgreSQL 17, 16, 15, 14, 13, 12, 11, and 10 versions; and 9.6.22 and higher 9 versions |
| db.t3.micro    | No  | Yes     | Yes                  | Yes   | Only on Oracle Database 12c Release 1 (12.1.0.2), which is deprecated | All PostgreSQL 17, 16, 15, 14, 13, 12, 11, and 10 versions; and 9.6.22 and higher 9 versions |

**db.t2 – burstable-performance instance classes**

| Instance class | Db2 | MariaDB    | Microsoft SQL Server | MySQL      | Oracle     | PostgreSQL |
| -------------- | --- | ---------- | -------------------- | ---------- | ---------- | ---------- |
| db.t2.2xlarge  | No  | Deprecated | No                   | Deprecated | Deprecated | Deprecated |
| db.t2.xlarge   | No  | Deprecated | No                   | Deprecated | Deprecated | Deprecated |
| db.t2.large    | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.t2.medium   | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.t2.small    | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |
| db.t2.micro    | No  | Deprecated | Deprecated           | Deprecated | Deprecated | Deprecated |

## Supported DB engines for Optimized Reads instance

classes

The following tables show the supported databases and database versions for the Optimized
Reads instance classes.

**db.r6gd – memory-optimized instance classes that support Optimized Reads and are powered by AWS Graviton2
processors**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle | PostgreSQL                                                                                                   |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| db.r6gd.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |
| db.r6gd.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | No     | All PostgreSQL 17, 16 and 15 versions, 14.5 and higher 14 versions, 13.7 and higher 13 versions, and<br>13.4 |

**db.r6id – memory-optimized instance classes that support Optimized Reads and are powered by 3rd generation Intel Xeon
Scalable processors**

| Instance class   | Db2 | MariaDB                                         | Microsoft SQL Server | MySQL             | Oracle                             | PostgreSQL                                                                                           |
| ---------------- | --- | ----------------------------------------------- | -------------------- | ----------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| db.r6id.32xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.24xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.16xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.12xlarge | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.8xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | EE and BYOL only                   | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.4xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.2xlarge  | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.xlarge   | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.large    | No  | MariaDB 11.8, 11.4, 10.11, 10.6, 10.5, and 10.4 | No                   | MySQL 8.4 and 8.0 | BYOL only                          | All PostgreSQL 17, 16, and 15 versions, 14.5 and higher 14 versions, and 13.7 and higher 13 versions |
| db.r6id.metal    | No  | No                                              | No                   | No                | BYOL only, Enterprise Edition only | No                                                                                                   |
