# Troubleshooting RDS Protection monitoring issues

GuardDuty RDS Protection analyzes and profiles your RDS login activity for potential access threats to the
[Supported databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db"). To collect security telemetry effectively, GuardDuty requires your
database configured and operating without issues. If your database is
misconfigured or experiencing issues, then security monitoring may be impacted.

The following section provides common issues and steps to troubleshoot them.

## RDS storage full

When your RDS instance runs out of storage, GuardDuty may not collect security telemetry. Reaching DB instance storage capacity
allocation (`storage-full`) is a critical status, and RDS recommends fixing this issue immediately. For more information, see
[Viewing instance status](../../../AmazonRDS/latest/UserGuide/accessing-monitoring.md "../../../AmazonRDS/latest/UserGuide/accessing-monitoring.md") in the
_Amazon RDS User Guide_.

To resolve the `storage-full` status, you can perform one of the following actions:

- **Enable storage autoscaling (recommended)** – Enable Amazon RDS
  storage autoscaling to automatically manage storage capacity and prevent future `storage-full`
  conditions. For more information, see
  [Managing capacity automatically with Amazon RDS storage autoscaling](../../../AmazonRDS/latest/UserGuide/USER_PIOPS.md "../../../AmazonRDS/latest/UserGuide/USER_PIOPS.md")
  in the _Amazon RDS User Guide_.
- **Monitor your storage utilization** – Check your
  storage utilization using one of the following methods:
  - Use CloudWatch metrics to view details about the storage. For more information, see [CloudWatch Database Insights](../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md "../../../AmazonCloudWatch/latest/monitoring/Database-Insights.md")
    in the _Amazon CloudWatch User Guide_.
  - View storage metrics by following the steps in [Monitor
    metrics in an Amazon RDS instance](../../../AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.md "../../../AmazonRDS/latest/UserGuide/Viewing_Unifiedmetrics.md") in the _Amazon RDS User Guide_.

- **Modify storage capacity** – For information about increasing your instance's
  storage capacity, see [Increasing DB instance storage capacity](../../../AmazonRDS/latest/UserGuide/USER_PIOPS.md "../../../AmazonRDS/latest/UserGuide/USER_PIOPS.md")
  in the _Amazon RDS User Guide_.

## Unsupported

versions on primary database for RDS for PostgreSQL

RDS for PostgreSQL read replica instances require the primary database instance to be on supported database version and
to be successfully replicated from the primary database. GuardDuty monitors your instances only when these
requirements are met.

To resolve the unsupported version issue, do one of the following:

- **Verify database version compatibility** – Check that your primary
  RDS for PostgreSQL database is running one of the supported versions. For more information, see
  [Supported databases](rds-protection.md#rds-pro-supported-db "rds-protection.md#rds-pro-supported-db").
- **Address potential replication issue** – Review and resolve any replication
  issues between primary and replica instances. For more information about doing this, see
  [Working with
  read replicas for RDS for PostgreSQL](../../../AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.md "../../../AmazonRDS/latest/UserGuide/USER_PostgreSQL.Replication.md") in the _Amazon RDS User Guide_.

## Additional security considerations

If your organization has strict compliance requirements, we recommend implementing database auditing in addition to
using RDS Protection. For more information about your security responsibilities and shared responsibility model,
see [Security in Amazon RDS](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md") in the
_Amazon RDS User Guide_.
