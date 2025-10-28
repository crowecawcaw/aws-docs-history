# Best practices for Amazon RDS

blue/green deployments

The following are best practices for blue/green deployments.

###### Topics

- [General best practices for
  blue/green deployments](#blue-green-deployments-best-practices-general "#blue-green-deployments-best-practices-general")
- [RDS for MySQL best practices for blue/green deployments](#blue-green-deployments-best-practices-mysql "#blue-green-deployments-best-practices-mysql")
- [RDS for PostgreSQL best
  practices for blue/green deployments](#blue-green-deployments-best-practices-postgres "#blue-green-deployments-best-practices-postgres")

## General best practices for

blue/green deployments

Consider the following general best practices when you create a blue/green
deployment.

- Thoroughly test the DB instances
  in the green environment before switching over.
- Keep your databases in the green environment read only. We recommend that you enable
  write operations on the green environment with caution because they can result in
  replication conflicts. They can also result in unintended data in the production
  databases after switchover.
- If you use a blue/green deployment to implement schema changes, make only
  replication-compatible changes.

For example, you can add new columns at the end of a table without disrupting
replication from the blue deployment to the green deployment. However, schema changes,
such as renaming columns or renaming tables, break replication to the green
deployment.

For more information about replication-compatible changes, see [Replication with Differing Table Definitions on Source and Replica](https://dev.mysql.com/doc/refman/8.0/en/replication-features-differing-tables.html "https://dev.mysql.com/doc/refman/8.0/en/replication-features-differing-tables.html") in the
MySQL documentation and [Restrictions](https://www.postgresql.org/docs/current/logical-replication-restrictions.html "https://www.postgresql.org/docs/current/logical-replication-restrictions.html") in the PostgreSQL logical replication documentation.

###### Note

This limitation doesn't apply to RDS for PostgreSQL blue/green deployments that use
physical replication. For more information, see [RDS for PostgreSQL limitations for
blue/green deployments with physical replication](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres-physical "blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres-physical").

- After you create the blue/green deployment, handle lazy loading if necessary. Make sure
  data loading is complete before switching over. For more information, see
  [Lazy loading and storage
  initialization for blue/green deployments](blue-green-deployments-creating.md#blue-green-deployments-creating-lazy-loading "blue-green-deployments-creating.md#blue-green-deployments-creating-lazy-loading").
- When you switch over a blue/green deployment, follow the switchover best practices.
  For more information, see [Switchover best practices](blue-green-deployments-switching.md#blue-green-deployments-switching-best-practices "blue-green-deployments-switching.md#blue-green-deployments-switching-best-practices").

## RDS for MySQL best practices for blue/green deployments

Consider the following best practices when you create a blue/green deployment from an
RDS for MySQL DB instance.

- Avoid using non-transactional storage engines, such as MyISAM, that aren't optimized
  for replication.
- Optimize read replicas and the green environment for binary log replication. If
  supported by your DB engine, enable GTID, parallel, and crash-safe replication to ensure
  data consistency and durability before you create your blue/green deployment. For more
  information, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").
- If the green environment experiences replica lag, consider the following:
  - Temporarily set the `innodb_flush_log_at_trx_commit` parameter to
    `2` in the green DB parameter group. After replication
    catches up, revert to the default value of `1` before switchover. If an
    unexpected shutdown or crash occurs with the temporary parameter value, rebuild the
    green environment to avoid undetected data corruption.
  - To reduce write latency and improve replication throughput, temporarily change
    green Multi-AZ DB instances to Single-AZ DB instances. Re-enable Multi-AZ right
    before switchover.

## RDS for PostgreSQL best

practices for blue/green deployments

Consider the following best practices when you create a blue/green deployment from an
RDS for PostgreSQL DB instance.

###### Topics

- [RDS for PostgreSQL
  general best practices for blue/green deployments](#blue-green-deployments-best-practices-postgres-general "#blue-green-deployments-best-practices-postgres-general")
- [RDS for PostgreSQL
  best practices for blue/green deployments with physical replication](#blue-green-deployments-best-practices-postgres-physical "#blue-green-deployments-best-practices-postgres-physical")
- [RDS for PostgreSQL
  best practices for blue/green deployments with logical replication](#blue-green-deployments-best-practices-postgres-logical "#blue-green-deployments-best-practices-postgres-logical")

### RDS for PostgreSQL

general best practices for blue/green deployments

Consider the following general best practices when you create a blue/green deployment
from an RDS for PostgreSQL DB instance.

- Update all of your PostgreSQL extensions to the latest version before you create a
  blue/green deployment. For more information, see [Upgrading PostgreSQL extensions in RDS for PostgreSQL databases](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").
- Long-running transactions can cause significant replica lag. To reduce replica
  lag, consider doing the following:
  - Reduce long-running transactions that can be delayed until after the green
    environment catches up to the blue environment.
  - Reduce bulk operations on the blue environment until after the green
    environment catches up to the blue environment.
  - Initiate a manual vacuum freeze operation on busy tables prior to creating the
    blue/green deployment.
  - For PostgreSQL version 12 and higher, disable the `index_cleanup`
    parameter on large or busy tables to increase the rate of normal maintenance on
    blue databases. For more information, see [Vacuuming a table as quickly as possible](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.Executing "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.Executing").

  ###### Note

  Regularly skipping index cleanup during vacuuming can lead to index bloat,
  which might degrade scan performance. As a best practice, use this approach only
  while using a blue/green deployment. Once the deployment is complete, we
  recommend resuming regular index maintenance and cleanup.

- Slow replication can cause senders and receivers to restart often, which delays
  synchronization. To ensure that they remain active, disable timeouts by setting the
  `wal_sender_timeout` parameter to `0` in the blue environment,
  and the `wal_receiver_timeout` parameter to `0` in the green
  environment.
- To prevent write-ahead log (WAL) segments from being removed from the blue
  environment, set the `wal_keep_segments` parameter to 15625 for PostgreSQL
  version 13 and lower. For version 14 and higher, set the `wal_keep_size`
  parameter too 1 TiB, if there's enough free storage space.

### RDS for PostgreSQL

best practices for blue/green deployments with physical replication

With physical replication, Amazon RDS creates a read replica of the source DB instance. For
related parameters, monitoring, tuning, and troubleshooting, see [Working with read replicas for
Amazon RDS for PostgreSQL](USER_PostgreSQL.Replication.md "USER_PostgreSQL.Replication.md").

For an explanation of when blue/green deployments use physical replication instead of
logical replication, see [PostgreSQL replication methods for
blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

### RDS for PostgreSQL

best practices for blue/green deployments with logical replication

Consider the following best practices when you create a blue/green deployment that
uses logical replication. For an explanation of when blue/green deployments use logical
replication instead of physical replication, see [PostgreSQL replication methods for
blue/green deployments](blue-green-deployments-replication-type.md "blue-green-deployments-replication-type.md").

- If your database has sufficient freeable memory, increase the value of the
  `logical_decoding_work_mem` DB parameter in the blue environment. Doing so
  allows for less decoding on disk and instead uses memory. For more information, see
  the [PostgreSQL documentation](https://www.postgresql.org/docs/13/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM "https://www.postgresql.org/docs/13/runtime-config-resource.html#GUC-LOGICAL-DECODING-WORK-MEM").
  - You can monitor transaction overflow being written to disk using the
    `ReplicationSlotDiskUsage` CloudWatch metric. This metric offers insights
    into the disk usage of replication slots, helping identify when transaction data
    exceeds memory capacity and is stored on disk. You can monitor freeable memory with
    the `FreeableMemory` CloudWatch metric. For more information, see [Amazon CloudWatch instance-level metrics for Amazon RDS](rds-metrics.md#rds-cw-metrics-instance "rds-metrics.md#rds-cw-metrics-instance").
  - In RDS for PostgreSQL version 14 and higher, you can monitor the size of logical
    overflow files using the `pg_stat_replication_slots` system view.

- If you’re using the `aws_s3` extension, give the green DB instance access to
  Amazon S3 through an IAM role after the green environment is created. This allows the
  import and export commands to continue functioning after switchover. For instructions,
  see [Setting up access to an Amazon S3
  bucket](postgresql-s3-export-access-bucket.md "postgresql-s3-export-access-bucket.md").
- Review the performance of your UPDATE and DELETE statements and evaluate whether
  creating an index on the column used in the WHERE clause can optimize these queries.
  This can enhance performance when the operations are replayed in the green
  environment.
- If you're using triggers, make sure they don't interfere with the creating,
  updating, and dropping of `pg_catalog.pg_publication`,
  `pg_catalog.pg_subscription`, and
  `pg_catalog.pg_replication_slots` objects whose names start with
  'rds'.
- If you specify a higher engine version for the green environment, run the
  `ANALYZE` operation on all databases to refresh the
  `pg_statistic` table. Optimizer statistics aren't transferred during a
  major version upgrade, so you must regenerate all statistics to avoid performance
  issues. For additional best practices during major version upgrades, see [How
  to perform a major version upgrade for RDS for PostgreSQL](USER_UpgradeDBInstance.PostgreSQL.MajorVersion.md "USER_UpgradeDBInstance.PostgreSQL.MajorVersion.md").
- Avoid configuring triggers as `ENABLE REPLICA` or `ENABLE
ALWAYS` if the trigger is used on the source to manipulate data. Otherwise, the
  replication system propagates changes and executes the trigger, which leads to
  duplication.
