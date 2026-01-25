# Amazon RDS for Db2 features

Amazon RDS for Db2 supports most of the features and capabilities of the IBM Db2 database. Some
features might have limited support or restricted privileges. For more information about the
Db2 database features for specific Db2 versions, see the [IBM Db2 documentation](https://www.ibm.com/docs/en/db2 "https://www.ibm.com/docs/en/db2").

You can filter new Amazon RDS features on the [What's New with Database?](https://aws.amazon.com/about-aws/whats-new/database/ "https://aws.amazon.com/about-aws/whats-new/database/") page. For
**Products**, choose **Amazon RDS**. Then, you can search
by using keywords such as `Db2 2023`.

###### Note

The following lists aren't exhaustive.

###### Topics

- [Supported features in RDS for Db2](#db2-supported-features "#db2-supported-features")
- [Unsupported features in RDS for Db2](#db2-unsupported-features "#db2-unsupported-features")

## Supported features in RDS for Db2

RDS for Db2 supports features that include features that are native to IBM Db2 and features
that are core to Amazon RDS.

### Features native to IBM Db2

RDS for Db2 supports the following Db2 database features:

- Creation
  of a standard database that uses a customer-defined code set, collation,
  page size, and territory. Use the Amazon RDS [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database") stored procedure.
- Addition, deletion, or modification of local users and groups. Use the
  Amazon RDS stored procedures for [Stored procedures for granting and
  revoking privileges for RDS for Db2](db2-sp-granting-revoking-privileges.md "db2-sp-granting-revoking-privileges.md").
- Creation of roles with the Amazon RDS [rdsadmin.create_role](db2-sp-granting-revoking-privileges.md#db2-sp-create-role "db2-sp-granting-revoking-privileges.md#db2-sp-create-role") stored procedure.
- Support for standard row-organized tables.
- Support for analytic workload for column-organized tables.
- Ability to define Db2-compatibility features such as Oracle
  and MySQL.
- Support for Java-based external stored procedures.
- Support for data encryption in transit by using SSL/TLS.
- Monitoring the status of a database (`ALIVE`,
  `DOWN`, `STORAGE_FULL`, `UNKNOWN`, and
  `STANDBY_CONNECTABLE`).
- Restoration of a customer-provided offline or online Linux
  (LE) database. Use Amazon RDS stored procedures for [Stored procedures for databases for
  RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").
- Application of customer-provided Db2 archive logs to keep the database synchronized with self-managed Db2 databases. Use Amazon RDS stored procedures for [Stored procedures for databases for
  RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").
- Support for Db2 instance-level and database-level auditing.
- Support for homogeneous federation.
- Ability to load a table from data files in Amazon Simple Storage Service (Amazon S3).
- Authorizations granted to users, groups or roles, such as
  `CONNECT`, `SYSMON`, `ACCESSCTRL`,
  `DATAACCESS`, `SQLADM`, `WLMADM`,
  `EXPLAIN`, `LOAD`, or
  `IMPLICIT_SCHEMA`.
- Creation of multiple databases.

###### Note

An RDS for Db2 DB instance can contain up to 50 databases. For more
information, see [Multiple databases on an Amazon RDS for Db2 DB
instance](db2-multiple-databases.md "db2-multiple-databases.md").

### Features core to Amazon RDS

RDS for Db2 supports the following core Amazon RDS features:

- Custom parameter groups to assign to DB instances
- Creation, modification, and deletion of DB instances
- Restoration of a self-managed Db2 offline or online Linux
  (LE) database backup

###### Note

To be able to restore your backup, don't provide a name for your
database when you create a DB instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

- Support of gp3, io2, and io1 storage types
- Use of AWS Managed Microsoft AD for Kerberos authentication, and LDAP
  group authorization for RDS for Db2
- Modification of security groups, ports, instance types, storage, backup
  retention periods, and other settings for existing Db2 instances
- Deletion protection for DB instances
- Cross-Region point-in-time recovery (PITR), including for encrypted
  backups
- Use of AWS Key Management Service (AWS KMS) for storage encryption and encryption at
  rest
- Multi-AZ DB instances with one standby for high availability
- Reboots of DB instances
- Updates to master passwords
- Restoration of DB instances to a specific time
- Backup
  and restoration of DB instances by using storage-level backups
- Start and stop of DB instances
- Maintenance of DB instances
- Same-Region and cross-Region standby and read replicas

## Unsupported features in RDS for Db2

RDS for Db2 doesn't support the following Db2 database features:

- `SYSADM`, `SECADM`, and `SYSMAINT` access for
  the master user.
- External stored procedures written in C, C++, or Cobol.
- Multiple Db2 DB instances on a single host.
- External GSS-API plugins for authentication.
- External third-party plugins to back up or restore Db2 databases.
- Multi-node massively parallel processing (MPP), such as IBM Db2
  Warehouse.
- IBM Db2 pureScale.
- Manual setup of High Availability Disaster Recovery (HADR) for
  RDS for Db2.

###### Note

Amazon RDS supports and manages HADR for RDS for Db2 through replicas. For more
information, see [Working with replicas for Amazon RDS for Db2](db2-replication.md "db2-replication.md").

RDS for Db2 supports Multi-AZ deployments, cross-Region automated backups, and
replication. For more information, see [Multi-AZ DB instance deployments for Amazon RDS](Concepts.md "Concepts.md") and [Replicating automated backups to another AWS Region](USER_ReplicateBackups.md "USER_ReplicateBackups.md").

- Native database encryption.
- Heterogeneous federation to Informix, Sybase, and Teradata. For more
  information, see [Amazon RDS for Db2 federation](db2-federation.md "db2-federation.md").
- Creation of non-fenced routines and migration of existing non-fenced routines
  by backing up and restoring data. For more information, see [Non-fenced
  routines](db2-known-issues-limitations.md#db2-known-issues-limitations-non-fenced-routines "db2-known-issues-limitations.md#db2-known-issues-limitations-non-fenced-routines").
- Creation of new non-automatic storage tablespaces. For more information, see
  [Non-automatic storage tablespaces during migration](db2-known-issues-limitations.md#db2-known-issues-limitations-non-automatic-storage-tablespaces "db2-known-issues-limitations.md#db2-known-issues-limitations-non-automatic-storage-tablespaces").
- External tables.
