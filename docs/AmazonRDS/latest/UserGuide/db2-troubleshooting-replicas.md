# Troubleshooting RDS for Db2 replication

issues

This topic describes common RDS for Db2 replication issues and provides troubleshooting
guidance for both read-only and standby replicas. In addition to reviewing the following
troubleshooting information, make sure that you followed the [requirements and considerations](db2-read-replicas.md "db2-read-replicas.md"), and completed the [preparation steps](db2-read-replicas.md "db2-read-replicas.md") before creating
Db2 replicas.

## Replica creation

failures

Replica creation can fail for several reasons:

- **Inactive databases** – All databases on
  the source DB instance must be active before creating replicas.

For information about activating databases, see [Stored procedures for databases for
RDS for Db2](db2-sp-managing-databases.md "db2-sp-managing-databases.md").

- **Missing automatic backups** – The source
  DB instance must have automatic backups enabled.

For information about enabling backups, see [Enabling automatic backups for RDS for Db2 replicas](db2-read-replicas.md#db2-read-replicas.backups.turning-on "db2-read-replicas.md#db2-read-replicas.backups.turning-on").

- **Parameter group issues** – Custom
  parameter groups are required for replicas. For BYOL licensing, the parameter
  group must include the IBM Site ID and IBM Customer ID.

For more information, see [IBM IDs for bring your own
license (BYOL) for Db2](db2-licensing.md#db2-prereqs-ibm-info "db2-licensing.md#db2-prereqs-ibm-info").

## Monitoring Db2 replication

lag

To monitor replication lag in Amazon CloudWatch, view the Amazon RDS `ReplicaLag` metric.
For more information about replication lag time, see [Monitoring read replication](USER_ReadRepl.md "USER_ReadRepl.md") and
[Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md "rds-metrics.md"). For information about
setting up CloudWatch alarms for replica lag, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

For a read-only replica, if the lag time is too long, query the
`MON_GET_HADR` table for the status of the replica DB instance.

For a standby replica, if the lag time is too long, query the
`MON_GET_HADR` table for the status of the source DB instance. Don't
query the replica DB instance because replica DB instances don't accept user
connections.

Common causes of high replication lag include the following reasons:

- Insufficient compute resources on the replica
- Network connectivity issues between the source and the replica
- High write activity on the source database
- Storage performance limitations on the replica

If high replication lag persists, consider scaling your replica resources. For more
information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

## Db2 replication errors

Db2 replication can be in an error state for a number of reasons. Perform the
following actions:

- Monitor events and the DB instance state to make sure that the DB instance is
  replicating.

For more information, see [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").

- Check the diagnostic logs for the Db2 replica in the Amazon RDS console. In the
  logs, look for errors in HADR messages. Compare the log sequence number to the
  primary sequence number.

For information about accessing and interpreting Db2 diagnostic logs, see
[Amazon RDS for Db2 database log files](USER_LogAccess.Concepts.md "USER_LogAccess.Concepts.md"). For information about Db2
HADR configuration and troubleshooting, see [Working with replicas for Amazon RDS for Db2](db2-replication.md "db2-replication.md").

If replication errors persist, you might need to recreate the replica.

## Connection issues

If you can't connect to your replica, review the following information about the
replica modes:

- **Standby replicas** – They don't accept
  user connections by design. Use read-only replicas for read workloads.
- **Read-only replicas** – Check your
  security group settings, network ACLs, and parameter group configurations.

For more information, see [Control traffic to your
AWS resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") in the
_Amazon VPC User Guide_, [Control subnet traffic with
network access control lists](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") in the
_Amazon VPC User Guide_, and [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Performance issues

If replica performance is poor, review the following suggestions:

- Ensure the replica has adequate compute and storage resources.
- Monitor the `ReplicaLag` metric in Amazon CloudWatch.
- Consider scaling up the replica DB instance class.

For information about modifying resources or instance classes, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.md "Overview.DBInstance.md").

For information monitoring replication lag, see [Monitoring replication lag](USER_ReadRepl.md#USER_ReadRepl.Monitoring.Lag "USER_ReadRepl.md#USER_ReadRepl.Monitoring.Lag") and [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md "rds-metrics.md"). For information about
setting up CloudWatch alarms for replica lag, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
