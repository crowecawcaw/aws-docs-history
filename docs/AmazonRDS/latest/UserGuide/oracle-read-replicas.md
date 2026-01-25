# Requirements and considerations for

RDS for Oracle replicas

Before creating an Oracle replica, familiarize yourself with the following requirements
and considerations.

###### Topics

- [Version and
  licensing requirements for RDS for Oracle replicas](#oracle-read-replicas.limitations.versions-and-licenses "#oracle-read-replicas.limitations.versions-and-licenses")
- [Option group limitations for
  RDS for Oracle replicas](#oracle-read-replicas.limitations.options "#oracle-read-replicas.limitations.options")
- [Backup and restore considerations for RDS for Oracle replicas](#oracle-read-replicas.limitations.backups "#oracle-read-replicas.limitations.backups")
- [Oracle Data Guard
  requirements and limitations for RDS for Oracle replicas](#oracle-read-replicas.data-guard.requirements "#oracle-read-replicas.data-guard.requirements")
- [Multi-tenant configuration limitations for RDS for Oracle replicas](#oracle-read-replicas.limitations.multitenant "#oracle-read-replicas.limitations.multitenant")
- [Miscellaneous considerations for RDS for Oracle replicas](#oracle-read-replicas.limitations.miscellaneous "#oracle-read-replicas.limitations.miscellaneous")

## Version and

licensing requirements for RDS for Oracle replicas

Before you create an RDS for Oracle replica, consider the following:

- If the replica is in read-only mode, make sure that you have an Active Data Guard license. If you
  place the replica in mounted mode, you don't need an Active Data Guard license. Only the Oracle
  DB engine supports mounted replicas.
- Oracle replicas are supported only for Oracle Enterprise Edition (EE).
- Oracle replicas of non-CDBs are supported only for DB instances created using
  non-CDB instances running Oracle Database 19c.
- Oracle replicas are available for DB instances running only on DB instance classes with
  two or more vCPUs. A source DB instance can't use the db.t3.small instance
  class.
- The Oracle DB engine version of the source DB instance and all its replicas must be the
  same. Amazon RDS upgrades the replicas immediately after upgrading the source DB instance,
  regardless of a replica's maintenance window. For major version upgrades of
  cross-Region replicas, Amazon RDS automatically does the following:

      + Generates an option group for the target version.
      + Copies all options and option settings from the original option group to the new option
       group.
      + Associates the upgraded cross-Region replica with the new option group.

  For more information about upgrading the DB engine version, see [Upgrading the RDS for Oracle DB engine](USER_UpgradeDBInstance.md "USER_UpgradeDBInstance.md").

## Option group limitations for

RDS for Oracle replicas

When working with option groups for your RDS for Oracle replica, consider the
following:

- You can't use a replica option group different from the source DB instance option
  group when the source and replica are in the same AWS Region.

Modifications to the source option group or source option group membership
propagate to Oracle replicas. These changes are applied to the replicas
immediately after they are applied to the source DB instance, regardless of the
replica's maintenance window. For more information about option groups, see
[Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

- You can't remove an RDS for Oracle cross-Region replica from its dedicated
  option group, which is automatically created for the replica.
- You can't add the dedicated option group for an RDS for Oracle cross-Region replica
  to a different DB instance.
- You can't add or remove nonreplicated options from a dedicated option group
  for an RDS for Oracle cross-Region replica, with the exception of the following
  options:

      + `NATIVE_NETWORK_ENCRYPTION`
      + `OEM`
      + `OEM_AGENT`
      + `SSL`

  To add other options to an RDS for Oracle cross-Region replica, add them to the
  source DB instance's option group. The option is also installed on all of the source
  DB instance's replicas. For licensed options, make sure that there are sufficient
  licenses for the replicas.

When you promote an RDS for Oracle cross-Region replica, the promoted replica
behaves the same as other Oracle DB instances, including the management of its
options. You can promote a replica explicitly or implicitly by deleting its
source DB instance.

For more information about option groups, see [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

- You can't add the `EFS_INTEGRATION` option to RDS for Oracle cross-Region
  replicas.

## Backup and restore considerations for RDS for Oracle replicas

Before you create an RDS for Oracle replica, consider the following:

- To create snapshots of RDS for Oracle replicas or turn on automatic backups, make sure to set the backup retention period manually.
  Automatic backups aren't turned on by default.
- When you restore a replica backup, you restore to the database time, not the
  time that the backup was taken. The _database time_ refers
  to the latest applied transaction time of the data in the backup. The difference
  is significant because a replica can lag behind the primary for minutes or
  hours.

To find the difference, use the `describe-db-snapshots` command. Compare the `snapshotDatabaseTime`, which
is the database time of the replica backup, and the `OriginalSnapshotCreateTime` field, which is the latest applied
transaction on the primary database.

## Oracle Data Guard

requirements and limitations for RDS for Oracle replicas

Before you create an RDS for Oracle replica, note the following requirements and
limitations:

- If your primary DB instance uses the single-tenant or multi-tenant configuration of the multitenant
  architecture, consider the following:
  - You must use Oracle Database 19c or higher with the Enterprise
    Edition.
  - Your primary CDB instance must be in an `ACTIVE`
    lifecycle.
  - You can't convert a non-CDB primary instance to a CDB instance and
    convert its replicas in the same operation. Instead, delete the non-CDB
    replicas, convert the primary DB instance to a CDB, and then create new
    replicas

- Make sure that a logon trigger on a primary DB instance permits access to the
  `RDS_DATAGUARD` user and to any user whose
  `AUTHENTICATED_IDENTITY` value is `RDS_DATAGUARD` or
  `rdsdb`. Also, the trigger must not set the current schema for
  the `RDS_DATAGUARD` user.
- To avoid blocking connections from the Data Guard broker process, don't enable
  restricted sessions. For more information about restricted sessions, see [Enabling and
  disabling restricted sessions](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").

## Multi-tenant configuration limitations for RDS for Oracle replicas

When using the multi-tenant configuration on an RDS for Oracle replica, note the following
limitations:

- You can only create, delete, or modify tenant databases on the primary DB instance. These changes automatically propagate to the replicas.
- Tenant databases on an RDS for Oracle primary, source, or replica cannot be created with a custom character set.
  If you require a custom character set, create the tenant databases before creating read replicas for the DB instance.

## Miscellaneous considerations for RDS for Oracle replicas

Before you create an RDS for Oracle replica, consider the following:

- When you are creating an RDS for Oracle replica for a DB instance that has additional storage volumes,
  RDS automatically configure additional storage volumes on the replica. However, any subsequent
  modifications made in storage volumes of your primary DB instance are not automatically applied to the replica.
- If you add additional storage volumes in your primary DB instance,
  RDS does not automatically add additional storage volumes to the replica.
  You need to modify your replica to add additional storage volumes.
- If you modify storage volumes configuration such as storage size and IOPS in your primary
  DB instance, RDS does not automatically modify storage volumes in the replica. You need
  to modify your replica to update storage volume configurations.
- When managing datafile locations across volumes, note that changes made on your primary instance don't automatically sync to replicas.
  - For read-only replicas: You can either use parameter group settings
    to control default file locations, or manually move files after they're created.
  - For mounted replicas: Manual changes to datafile locations in the primary database
    require recreating the mounted replica to reflect those changes. To avoid this, we
    recommend using parameter group settings to manage default file locations.

- If your DB instance is a source for one or more cross-Region replicas, the source DB
  retains its archived redo log files until they are applied on all cross-Region
  replicas. The archived redo logs might result in increased storage
  consumption.
- To avoid disrupting RDS automation, system triggers must permit specific users to log on to the
  primary and replica database. [System triggers](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-triggers.html#GUID-FE23FCE8-DE36-41EF-80A9-6B4B49E80E5B "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/plsql-triggers.html#GUID-FE23FCE8-DE36-41EF-80A9-6B4B49E80E5B") include DDL, logon, and database role triggers. We recommend that you
  add code to your triggers to exclude the users listed in the following sample code:

```
-- Determine who the user is
SELECT SYS_CONTEXT('USERENV','AUTHENTICATED_IDENTITY') INTO CURRENT_USER FROM DUAL;
-- The following users should always be able to login to either the Primary or Replica
IF CURRENT_USER IN ('`master_user`', 'SYS', 'SYSTEM', 'RDS_DATAGUARD', 'rdsdb') THEN
RETURN;
END IF;
```

- Block change tracking is supported for read-only replicas, but not for mounted replicas. You can
  change a mounted replica to a read-only replica, and then enable block change tracking. For more
  information, see [Enabling and
  disabling block change tracking](Appendix.Oracle.CommonDBATasks.md "Appendix.Oracle.CommonDBATasks.md").
- You can't create an Oracle read replica when the source database manages
  master user credentials with Secrets Manager.
