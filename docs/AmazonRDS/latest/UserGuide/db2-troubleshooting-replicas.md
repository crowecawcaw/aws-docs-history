

# Troubleshooting RDS for Db2 replication issues
<a name="db2-troubleshooting-replicas"></a>

This topic describes common RDS for Db2 replication issues and provides troubleshooting guidance for both read-only and standby replicas. In addition to reviewing the following troubleshooting information, make sure that you followed the [requirements and considerations](db2-read-replicas.limitations.md), and completed the [preparation steps](db2-read-replicas.Configuration.md) before creating Db2 replicas.

## Replica creation failures
<a name="db2-troubleshooting-replicas-creation"></a>



Replica creation can fail for several reasons:
+ **Inactive databases** – All databases on the source DB instance must be active before creating replicas. 

  For information about activating databases, see [Stored procedures for databases for RDS for Db2](db2-sp-managing-databases.md).
+ **Missing automatic backups** – The source DB instance must have automatic backups enabled. 

  For information about enabling backups, see [Enabling automatic backups for RDS for Db2 replicas](db2-read-replicas.backups.md#db2-read-replicas.backups.turning-on).
+ **Parameter group issues** – Custom parameter groups are required for replicas. For BYOL licensing, the parameter group must include the IBM Site ID and IBM Customer ID. 

  For more information, see [IBM IDs for bring your own license (BYOL) for Db2](db2-licensing.md#db2-prereqs-ibm-info).

## Monitoring Db2 replication lag
<a name="db2-troubleshooting-replicas-lag"></a>

To monitor replication lag in Amazon CloudWatch, view the Amazon RDS `ReplicaLag` metric. For more information about replication lag time, see [Monitoring read replication](USER_ReadRepl.Monitoring.md) and [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md). For information about setting up CloudWatch alarms for replica lag, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md). 

For a read-only replica, if the lag time is too long, query the `MON_GET_HADR` table for the status of the replica DB instance. 

For a standby replica, if the lag time is too long, query the `MON_GET_HADR` table for the status of the source DB instance. Don't query the replica DB instance because replica DB instances don't accept user connections.

Common causes of high replication lag include the following reasons:
+ Insufficient compute resources on the replica
+ Network connectivity issues between the source and the replica
+ High write activity on the source database
+ Storage performance limitations on the replica

If high replication lag persists, consider scaling your replica resources. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

## Db2 replication errors
<a name="db2-troubleshooting-replicas-triggers"></a>

Db2 replication can be in an error state for a number of reasons. Perform the following actions:
+ Monitor events and the DB instance state to make sure that the DB instance is replicating. 

  For more information, see [Working with Amazon RDS event notification](USER_Events.md).
+ Check the diagnostic logs for the Db2 replica in the Amazon RDS console. In the logs, look for errors in HADR messages. Compare the log sequence number to the primary sequence number. 

  For information about accessing and interpreting Db2 diagnostic logs, see [Amazon RDS for Db2 database log files](USER_LogAccess.Concepts.Db2.md). For information about Db2 HADR configuration and troubleshooting, see [Working with replicas for Amazon RDS for Db2](db2-replication.md). 

If replication errors persist, you might need to recreate the replica. 

## Connection issues
<a name="db2-troubleshooting-replicas-connections"></a>

If you can't connect to your replica, review the following information about the replica modes:
+ **Standby replicas** – They don't accept user connections by design. Use read-only replicas for read workloads.
+ **Read-only replicas** – Check your security group settings, network ACLs, and parameter group configurations. 

  For more information, see [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*, [Control subnet traffic with network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon VPC User Guide*, and [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md).

## Performance issues
<a name="db2-troubleshooting-replicas-performance"></a>

If replica performance is poor, review the following suggestions:
+ Ensure the replica has adequate compute and storage resources. 
+ Monitor the `ReplicaLag` metric in Amazon CloudWatch. 
+ Consider scaling up the replica DB instance class. 

For information about modifying resources or instance classes, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md).

For information monitoring replication lag, see [Monitoring replication lag](USER_ReadRepl.Monitoring.md#USER_ReadRepl.Monitoring.Lag) and [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md). For information about setting up CloudWatch alarms for replica lag, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md). 