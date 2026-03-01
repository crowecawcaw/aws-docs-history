# Best practices for Amazon Aurora blue/green deployments

The following are best practices for blue/green deployments.

###### Topics

- [General best practices for blue/green deployments](#blue-green-deployments-best-practices-general "#blue-green-deployments-best-practices-general")
- [Aurora MySQL best practices for blue/green deployments](#blue-green-deployments-best-practices-mysql "#blue-green-deployments-best-practices-mysql")
- [Aurora PostgreSQL best practices for blue/green deployments](#blue-green-deployments-best-practices-postgres "#blue-green-deployments-best-practices-postgres")
- [Aurora Global Database best practices for blue/green deployments](#blue-green-deployments-best-practices-agd "#blue-green-deployments-best-practices-agd")

## General best practices for blue/green deployments

Consider the following general best practices when you create a blue/green
deployment.

- Thoroughly test the Aurora DB cluster
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

- Use the cluster endpoint, reader endpoint, or custom endpoint for all connections in both environments.
  Don't use instance endpoints or custom endpoints with static or exclusion lists.
- When you switch over a blue/green deployment, follow the switchover best practices.
  For more information, see [Switchover best practices](blue-green-deployments-switching.md#blue-green-deployments-switching-best-practices "blue-green-deployments-switching.md#blue-green-deployments-switching-best-practices").

## Aurora MySQL best practices for blue/green deployments

Consider the following best practices when you create a blue/green deployment from an
Aurora MySQL
DB cluster.

- If the green environment experiences replica lag, consider the following:
  - Disable binary log retention if it's not needed, or temporarily disable it until
    replication catches up. To do so, set the `binlog_format` DB cluster
    parameter back to `0` and reboot the green writer DB instance.
  - Temporarily set the `innodb_flush_log_at_trx_commit` parameter to
    `0` in the green DB parameter group. After replication
    catches up, revert to the default value of `1` before switchover. If an
    unexpected shutdown or crash occurs with the temporary parameter value, rebuild the
    green environment to avoid undetected data corruption. For more information, see [Configuring how frequently the log buffer is flushed](AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.Flush "AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.Flush").

## Aurora PostgreSQL best practices for blue/green deployments

Consider the following best practices when you create a blue/green deployment from an
Aurora PostgreSQL DB cluster.

- Monitor the Aurora PostgreSQL logical replication write-through cache
  and make adjustments to the cache buffer if necessary. For more information, see [Monitoring the Aurora PostgreSQL logical replication write-through cache](AuroraPostgreSQL.Replication.md#AuroraPostgreSQL.Replication.Logical-write-through-cache "AuroraPostgreSQL.Replication.md#AuroraPostgreSQL.Replication.Logical-write-through-cache").
- Increase the value of the `logical_decoding_work_mem` DB parameter in the
  blue environment. Doing so allows for less decoding on disk and instead uses memory. For
  more information, see [Adjusting working memory for logical decoding](AuroraPostgreSQL.BestPractices.md#AuroraPostgreSQL.BestPractices.Tuning-memory-parameters.logical-decoding-work-mem "AuroraPostgreSQL.BestPractices.md#AuroraPostgreSQL.BestPractices.Tuning-memory-parameters.logical-decoding-work-mem").
  - You can monitor transaction overflow being written to disk using the
    `ReplicationSlotDiskUsage` CloudWatch metric. This metric offers insights
    into the disk usage of replication slots, helping identify when transaction data
    exceeds memory capacity and is stored on disk. You can monitor freeable memory with
    the `FreeableMemory` CloudWatch metric. For more information, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").
  - In Aurora PostgreSQL version 14 and higher, you can monitor the size of logical
    overflow files using the `pg_stat_replication_slots` system view.

- Update all of your PostgreSQL extensions to the latest version before you create a
  blue/green deployment. For more information, see [Upgrading PostgreSQL extensions](USER_UpgradeDBInstance.Upgrading.md "USER_UpgradeDBInstance.Upgrading.md").
- If you’re using the `aws_s3` extension, give the green DB cluster access to
  Amazon S3 through an IAM role after the green environment is created. This allows the
  import and export commands to continue functioning after switchover. For instructions,
  see [Setting up access to an Amazon S3 bucket](postgresql-s3-export-access-bucket.md "postgresql-s3-export-access-bucket.md").
- If you specify a higher engine version for the green environment, run the
  `ANALYZE` operation on all databases to refresh the
  `pg_statistic` table. Optimizer statistics aren't transferred during a
  major version upgrade, so you must regenerate all statistics to avoid performance
  issues. For additional best practices during major version upgrades, see [Performing a major version upgrade](USER_UpgradeDBInstance.PostgreSQL.md "USER_UpgradeDBInstance.PostgreSQL.md").
- Avoid configuring triggers as `ENABLE REPLICA` or `ENABLE
ALWAYS` if the trigger is used on the source to manipulate data. Otherwise, the
  replication system propagates changes and executes the trigger, which leads to
  duplication.
- Long-running transactions can cause significant replica lag. To reduce replica lag,
  consider doing the following:
  - Reduce long-running transactions and subtransactions that can be delayed until
    after the green environment catches up to the blue environment.
  - Reduce bulk operations on the blue environment until after the green environment
    catches up to the blue environment.
  - Initiate a manual vacuum freeze operation on busy tables prior to creating the
    blue/green deployment. For instructions, see [Performing a manual vacuum freeze](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md").
  - In PostgreSQL version 12 and higher, disable the `index_cleanup`
    parameter on large or busy tables to improve the efficiency of regular maintenance
    on blue databases. For more information, see [Vacuuming a table as quickly as possible](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.Executing "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.LargeIndexes.Executing").

  ###### Note

  Regularly skipping index cleanup during vacuuming can lead to index bloat,
  which might degrade scan performance. As a best practice, use this approach only
  while using a blue/green deployment. Once the deployment is complete, we recommend
  resuming regular index maintenance and cleanup.
  - Replica lag can occur if the blue and green DB instances are undersized for the
    workload. Ensure that your DB instances are not reaching their resource limits for the
    instance type. For more information, see [Using Amazon CloudWatch metrics to analyze resource usage for Aurora PostgreSQL](AuroraPostgreSQL_AnayzeResourceUsage.md "AuroraPostgreSQL_AnayzeResourceUsage.md").

- Slow replication can cause senders and receivers to restart often, which delays
  synchronization. To ensure that they remain active, disable timeouts by setting the
  `wal_sender_timeout` parameter to `0` in the blue environment,
  and the `wal_receiver_timeout` parameter to `0` in the green
  environment.
- Review the performance of your UPDATE and DELETE statements and evaluate whether
  creating an index on the column used in the WHERE clause can optimize these queries.
  This can enhance performance when the operations are replayed in the green environment.
  For more information, see [Check predicate filters for queries that generate waits](apg-waits.md#apg-waits.iodatafileread.actions.filters "apg-waits.md#apg-waits.iodatafileread.actions.filters").
- If you're using triggers, make sure they don't interfere with the creating,
  updating, and dropping of `pg_catalog.pg_publication`,
  `pg_catalog.pg_subscription`, and
  `pg_catalog.pg_replication_slots` objects whose names start with
  'rds'.
- If Babelfish is enabled on the source DB cluster, the following parameters must
  have the same settings in the target DB cluster parameter group for the green environment as
  in the source DB cluster parameter group:

      + rds.babelfish\_status
      + babelfishpg\_tds.tds\_default\_numeric\_precision
      + babelfishpg\_tds.tds\_default\_numeric\_scale
      + babelfishpg\_tsql.default\_locale
      + babelfishpg\_tsql.migration\_mode
      + babelfishpg\_tsql.server\_collation\_name

  For more information about these parameters, see [DB cluster parameter group settings for Babelfish](babelfish-configuration.md "babelfish-configuration.md").

## Aurora Global Database best practices for blue/green deployments

In addition to the above listed general and engine specific best practices, consider the following best practices for
Aurora Global Database.

- Monitor the following CloudWatch metrics to identify periods of low activity in your production environment:

      + `DatabaseConnections`
      + `ActiveTransactions`

  Schedule the blue/green switchover during your planned maintenance window or during a period of low activity.

- Blue/Green switchover duration varies based on your workload and the number of secondary regions. When you initiate a blue/green switchover, the service waits for replica lag to reach zero before proceeding. We recommend checking replica lag before initiating a switchover.
- If you intend to use a DB parameter or DB Cluster parameter group other than the default one for your green environment, create the desired parameter group with the same name in all secondary regions before initiating the blue/green deployment.
