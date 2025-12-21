# Preparing to create an RDS for Db2

replica

Before creating an RDS for Db2 replica, you must complete the following tasks for successful
replication. These tasks help prevent common issues and ensure optimal performance.

## Task 1: Enable automatic

backups

Before a DB instance can serve as a source DB instance, you must enable automatic
backups on the source DB instance. This is a prerequisite for all replica creation
operations. To learn how to perform this procedure, see [Enabling automated
backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").

For information about backups specific to Db2 replicas, see [Working with RDS for Db2 replica backups](db2-read-replicas.md "db2-read-replicas.md").

## Task 2: Plan

compute and storage resources

Ensure that the source DB instance and its replicas are sized properly, in terms of
compute and storage, to suit their operational load. If a replica reaches compute,
network, or storage resource capacity, the replica stops receiving or applying changes
from its source. For information about monitoring replica performance and resource
utilization, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md").

RDS for Db2 doesn't intervene to mitigate high replica lag between a source DB instance
and its replicas. If you experience high replica lag, see [Monitoring Db2 replication
lag](db2-troubleshooting-replicas.md#db2-troubleshooting-replicas-lag "db2-troubleshooting-replicas.md#db2-troubleshooting-replicas-lag") for troubleshooting guidance.

You can modify the storage and CPU resources of a replica independently from its
source and other replicas. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Task 3: Prepare

databases

Before creating a replica, confirm that your databases are ready based on the
following points:

- The DB instance contains all databases that you want present on the DB
  instance. After replica creation, you can't create, drop, or native restore a
  database on the DB instance. Any calls to the [rdsadmin.create_database](db2-sp-managing-databases.md#db2-sp-create-database "db2-sp-managing-databases.md#db2-sp-create-database"),
  [rdsadmin.drop_database](db2-sp-managing-databases.md#db2-sp-drop-database "db2-sp-managing-databases.md#db2-sp-drop-database"),
  or [rdsadmin.restore_database](db2-sp-managing-databases.md#db2-sp-restore-database "db2-sp-managing-databases.md#db2-sp-restore-database") stored procedures fail.
- All databases on the DB instance are in an active state. If any database is in
  an inactive state, replica creation will fail. For information about activating
  databases, see [Stored procedures for databases for
  RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").

## Next steps

After completing all the preparation tasks, you are ready to create a Db2
replica.

- To create a read-only replica, see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").
- To create a standby replica, see [Creating a standby
  Db2 replica](db2-read-replicas.md "db2-read-replicas.md").
