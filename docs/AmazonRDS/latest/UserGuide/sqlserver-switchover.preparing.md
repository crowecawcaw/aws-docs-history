

# Preparing for a SQL Server switchover
<a name="sqlserver-switchover.preparing"></a>

In these requirements, the *original primary* DB instance and the *original read replica* are the roles that exist before the switchover. For more information, see [Overview of the SQL Server switchover](sqlserver-replication-switchover.md#sqlserver-replication-switchover.overview).

Some switchover requirements involve Multi-AZ deployments and option groups. For more information, see [Configuring and managing a Multi-AZ deployment for Amazon RDS](Concepts.MultiAZ.md) and [Working with option groups](USER_WorkingWithOptionGroups.md).

Before initiating the SQL Server switchover, make sure that your replication environment meets the requirements in the following sections.

**Topics**
+ [Engine and feature requirements](#sqlserver-switchover.preparing.engine)
+ [DB instance state requirements](#sqlserver-switchover.preparing.state)
+ [Configuration requirements](#sqlserver-switchover.preparing.configuration)

## Engine and feature requirements
<a name="sqlserver-switchover.preparing.engine"></a>
+ The original primary DB instance and the original read replica run SQL Server versions 2022–2025, on the Enterprise Edition (EE) engine.
+ The original primary DB instance and the original read replica don't use the following features:
  + Native backup and restore with cross-Region read replicas. For more information, see [Importing and exporting SQL Server databases using native backup and restore](SQLServer.Procedural.Importing.md).
  + Amazon S3 integration. For more information, see [Integrating an Amazon RDS for SQL Server DB instance with Amazon S3](User.SQLServer.Options.S3-integration.md).
  + Database activity streams. For more information, see [Monitoring Amazon RDS with Database Activity Streams](DBActivityStreams.md).
+ Automatic backups are enabled on the original read replica. To enable automatic backups on the read replica, set its backup retention period to a value other than 0.

## DB instance state requirements
<a name="sqlserver-switchover.preparing.state"></a>
+ The original primary DB instance and the original read replica are in the `available` state.
+ Neither DB instance has pending maintenance actions in the `required`, `next window`, or `in progress` state. Actions in these states block a switchover. To learn how to check the status of pending maintenance updates, see [Viewing pending maintenance updates](USER_UpgradeDBInstance.Maintenance.md#USER_UpgradeDBInstance.Maintenance.Viewing).

  Pending maintenance actions in the `available` state don't block switchover. Amazon RDS frequently releases operating system (OS) updates in the `available` state. These pending OS updates won't block a switchover unless you schedule them for the next maintenance window, which puts them in the `next window` state.
**Note**  
If you want to defer a scheduled maintenance action so that you can execute a switchover, choose **Actions** and then **Defer upgrade** in the RDS console. You can also prevent a switchover from being blocked by applying a pending maintenance action or moving the maintenance window to an interval before your switchover.
+ The original read replica is in the `replicating` state.
+ You aren't attempting to initiate a switchover when either the primary DB instance or read replica is currently in a switchover lifecycle. If a read replica is reconfiguring after a switchover, Amazon RDS prevents you from initiating another switchover.

## Configuration requirements
<a name="sqlserver-switchover.preparing.configuration"></a>
+ The original read replica has a configuration that is as close as desired to the original primary DB instance. After the switchover completes, Amazon RDS doesn't automatically reconfigure the new primary DB instance to have the same configuration as the original primary DB instance.
+ The original primary DB instance isn't in a Multi-AZ deployment. You can't perform a switchover when the primary DB instance uses a Multi-AZ deployment.
+ The original primary DB instance has only one read replica. You can't perform a switchover when the primary DB instance has multiple read replicas.
+ Before you perform a cross-Region switchover, verify that no DB instance outside your replication configuration uses the same option group as the primary DB instance. Only the current primary DB instance and its read replica can use that option group. Otherwise, Amazon RDS prevents the switchover.