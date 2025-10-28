# Configuring multi-source-replication for Amazon RDS for MySQL

With multi-source replication, you can set up an Amazon RDS for MySQL DB instance as a replica that receives binary log events from more than one RDS for MySQL source DB instance.
Multi-source replication is supported for RDS for MySQL DB instances running the following engine versions:

- All MySQL 8.4 versions
- 8.0.35 and higher minor versions
- 5.7.44 and higher minor versions
  For information about MySQL multi-source replication, see [MySQL Multi-Source Replication](https://dev.mysql.com/doc/refman/8.0/en/replication-multi-source.html "https://dev.mysql.com/doc/refman/8.0/en/replication-multi-source.html") in the MySQL documentation. The MySQL documentation contains
  detailed information about this feature, while this topic describes how to configure and
  manage the multi-source replication channels on your RDS for MySQL DB instances.

## Use cases for multi-source replication

The following cases are good candidates for using multi-source replication on RDS for MySQL:

- Applications that need to merge or combine multiple shards on separate DB
  instances into a single shard.
- Applications that need to generate reports from data consolidated from multiple sources.
- Requirements to create consolidated long-term backups of data that's
  distributed among multiple RDS for MySQL DB instances.

## Prerequisites for multi-source replication

Before you configure multi-source replication, complete the following prerequisites.

- Make sure that each source RDS for MySQL DB instance has automatic backups enabled. Enabling automatic backups enables binary logging.
  To learn how to enable automatic backups, see [Enabling automated
  backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md").
- To avoid replication errors, we recommended that you block write operations to the source DB instances. You can do so by setting the
  `read-only` parameter to `ON` in a custom parameter group attached to the RDS for MySQL source DB instance.
  You can use the AWS Management Console or the AWS CLI to create a new custom parameter group or to modify an existing one. For more information,
  see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md") and [Modifying parameters in a DB parameter group
  in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
- For each source DB instance, add the IP address of the instance to the Amazon virtual private cloud (VPC) security group for the multi-source DB instance.
  To identify the IP address of a source DB instance, you can run the command `dig `RDS Endpoint``. Run the command from an
  Amazon EC2 instance in the same VPC as the destination multi-source DB instance.
- For each source DB instance, use a client to connect to the DB instance and create a database
  user with the required privileges for replication, as in the following
  example.

```
CREATE USER '`repl_user`' IDENTIFIED BY '`password`';
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO '`repl_user`';
```

###### Note

Starting with MySQL 8.4, the `REPLICATION SLAVE` privilege has been deprecated and replaced with `REPLICATION REPLICA`.
For MySQL 8.4 and later versions, use the following syntax instead:

```
CREATE USER '`repl_user`' IDENTIFIED BY '`password`';
GRANT REPLICATION CLIENT, REPLICATION REPLICA ON *.* TO '`repl_user`';
```

## Configuring multi-source replication channels on RDS for MySQL DB instances

Configuring multi-source replication channels is similar to configuring single source
replication. For multi-source replication, you first turn on binary logging on the
source instance. Then, you import data from the sources to the multi-source replica.
Then, you start replication from each source by using the binary log coordinates or by
using GTID auto-positioning.

To configure an RDS for MySQL DB instance as a multi-source replica of two or more RDS for MySQL DB instances, perform the following steps.

###### Topics

- [Step 1: Import data from the
  source DB instances to the multi-source replica](#mysql-multi-source-replication-import "#mysql-multi-source-replication-import")
- [Step 2: Start replication from the source DB instances to the multi-source
  replica](#mysql-multi-source-replication-setting-up-start-replication-other "#mysql-multi-source-replication-setting-up-start-replication-other")

### Step 1: Import data from the

source DB instances to the multi-source replica

Perform the following steps on each source DB instance.

Before you import the data from a source to the multi-source replica, determine
the current binary log file and position by running the `SHOW MASTER
 STATUS` command. Take note of these details for use in the next step.
In this example output, the file is `mysql-bin-changelog.000031` and the position is
`107`.

###### Note

Starting with MySQL 8.4, the `SHOW MASTER STATUS` command has been deprecated and replaced with `SHOW BINARY LOG STATUS`.
For MySQL 8.4 and later versions, use `SHOW BINARY LOG STATUS` instead.

```
File                        Position
-----------------------------------
mysql-bin-changelog.000031      107
-----------------------------------
```

Now copy the database from the source DB instance to the multi-source replica by
using `mysqldump`, as in the following example.

```
mysqldump --databases database_name \
 --single-transaction \
 --compress \
 --order-by-primary \
 -u `RDS_user_name` \
 -p `RDS_password` \
 --host=`RDS Endpoint` | mysql \
 --host=`RDS Endpoint` \
 --port=3306 \
 -u `RDS_user_name` \
-p `RDS_password`
```

After copying the database, you can set the read-only parameter to
`OFF` on the source DB instance.

### Step 2: Start replication from the source DB instances to the multi-source

replica

For each source DB instance, use the administrative user credentials to connect to the
instance, and run the following two stored procedures. These stored procedures
configure replication on a channel and start replication. This example uses the
binlog file name and position from the example output in the previous step.

```
CALL mysql.rds_set_external_source_for_channel('`mysourcehost.example.com`', 3306, '`repl_user`', '`password`', '`mysql-bin-changelog.000031`', `107`, 1, '`channel_1`');
CALL mysql.rds_start_replication_for_channel('`channel_1`');
```

For more information about using these stored procedures and others to set up and manage your replication channels, see [Managing multi-source replication](mysql-stored-proc-multi-source-replication.md "mysql-stored-proc-multi-source-replication.md").

## Using filters with multi-source

replication

You can use replication filters to specify which databases and tables are replicated with in multi-source replica. Replication filters can include databases and tables
in replication or exclude them from replication. For more information on replication filters, see [Configuring replication filters with MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md").

With multi-source replication, you can configure replication filters globally or at
the channel level. Channel-level filtering is available only with supported DB instances
running version 8.0 or version 8.4. The following examples show how to configure filters
globally or at the channel level.

Note the following requirements and behavior with filtering in multi-source replication:

- Back quotes (``) around the channel names are required.
- If you change replication filters in the parameter group, the multi-source replica's
  `sql_thread` for all channels with updates are restarted to apply
  the changes dynamically. If an update involves a global filter, then all
  replication channels in the running state are restarted.
- All global filters are applied before any channel-specific filters.
- If a filter is applied globally and at the channel level, then only the channel-level filter
  is applied. For example, if the filters are
  `replicate_ignore_db="db1,`channel_22`:db2"`, then
  `replicate_ignore_db` set to `db1` is applied to all
  channels except for `channel_22`, and only `channel_22`
  ignores changes from `db2`.

Example 1: Setting a global filter

In the following example, the `temp_data` database is excluded from replication in every channel.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
--db-parameter-group-name myparametergroup \
--parameters "ParameterName=replicate-ignore-db,ParameterValue='temp_data',ApplyMethod=immediate"
```

Example 2: Setting a channel-level filter

In the following example, changes from the `sample22` database are only
included in channel `channel_22`. Similarly, changes from the
`sample99` database are only included in channel
`channel_99`.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
--db-parameter-group-name myparametergroup \
--parameters "ParameterName=replicate-do-db,ParameterValue='\`channel_22\`:sample22,\`channel_99\`:sample99',ApplyMethod=immediate"
```

## Monitoring multi-source replication channels

You can monitor individual channels in a multi-source replica by using the following methods:

- To monitor the status of all channels or a specific channel, connect to the multi-source
  replica and run the `SHOW REPLICA STATUS` or `SHOW REPLICA
STATUS FOR CHANNEL '`channel_name`'` command.
  For more information, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.0/en/replication-administration-status.html "https://dev.mysql.com/doc/refman/8.0/en/replication-administration-status.html") in the MySQL documentation.
- To receive notification when a replication channel is started, stopped, or removed, use RDS event notification. For more information, see
  [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md").
- To monitor the lag for a specific channel, check the `ReplicationChannelLag` metric
  for it. Data points for this metric have a period of 60 seconds (1 minute) are available for 15 days. To locate the replication channel lag for a channel, use the instance
  identifier and the replication channel name. To receive notification when this
  lag exceeds a particular threshold, you can set up a CloudWatch alarm. For more
  information, see [Monitoring Amazon RDS metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## Considerations and best

practices for multi-source replication

Before you use multi-source replication on RDS for MySQL, review the following considerations
and best practices:

- Make sure that a DB instance configured as a multi-source replica has
  sufficient resources such as throughput, memory, CPU, and IOPS to handle the
  workload from multiple source instances.
- Regularly monitor resource utilization on your multi-source replica and adjust
  the storage or instance configuration to handle the workload without straining
  resources.
- You can configure multi-threaded replication on a multi-source replica by
  setting the system variable `replica_parallel_workers` to a value greater than `0`.
  In this case, the number of threads allocated to each channel is the value of this variable,
  plus one coordinator thread to manage the applier threads.
- Configure replication filters appropriately to avoid conflicts. To replicate an entire database to
  another database on a replica, you can use the `--replicate-rewrite-db` option. For example, you can replicate
  all tables in database A to database B on a replica instance. This approach can be helpful
  when all source instances are using the same schema naming convention.
  For information about the `--replicate-rewrite-db` option, see [Replica Server Options and Variables](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html "https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html")
  in the MySQL documentation.
- To avoid replication errors, avoid writing to the replica. We recommended that
  you enable the `read_only` parameter on multi-source replicas to
  block write operations. Doing so helps to eliminate replication issues caused by
  conflicting write operations.
- To increase the performance of read operations such as sorts and high-load
  joins that are executed on the multi-source replica, consider using RDS
  Optimized Reads. This feature can help with queries that depend on large
  temporary tables or sort files. For more information, see [Improving query performance for RDS for MySQL with Amazon RDS Optimized Reads](rds-optimized-reads.md "rds-optimized-reads.md").
- To minimize replication lag and improve the performance of a multi-source
  replica, consider enabling optimized writes. For more information, see [Improving write performance with RDS Optimized Writes for MySQL](rds-optimized-writes.md "rds-optimized-writes.md").
- Perform management operations (such as changing configuration) on one channel
  at a time, and avoid performing changes to multiple channels from multiple
  connections. These practices can lead to conflicts in replication operations.
  For example, simultaneously executing
  `rds_skip_repl_error_for_channel` and
  `rds_start_replication_for_channel` procedures from multiple
  connections can cause skipping of events on a different channel than
  intended.
- You can enable backups on a multi-source replication instance and export data
  from that instance to an Amazon S3 bucket to store it for long-term purposes.
  However, it's important to also configure backups with appropriate retention on
  the individual source instances. For information about exporting snapshot data
  to Amazon S3, see [Exporting DB snapshot data to Amazon S3 for Amazon RDS](USER_ExportSnapshot.md "USER_ExportSnapshot.md").
- To distribute the read workload on a multi-source replica, you can create read
  replicas from a multi-source replica. You can locate these read replicas in
  different AWS Regions based on your application's requirements. For more
  information about read replicas, see [Working with MySQL read replicas](USER_MySQL.Replication.md "USER_MySQL.Replication.md").

## Limitations for multi-source replication on RDS for MySQL

The following limitations apply to multi-source replication on RDS for MySQL:

- Currently, RDS for MySQL supports configuring a maximum of 15 channels for a
  multi-source replica.
- A read replica instance can't be configured as a multi-source replica.
- To configure multi-source replication on RDS for MySQL running engine version
  5.7, Performance Schema must be enabled on the replica instance. Enabling
  Performance Schema is optional on RDS for MySQL running engine version 8.0 or
  8.4.
- For RDS for MySQL running engine version 5.7, replication filters apply to all
  replication channels. For RDS for MySQL running engine version 8.0 or 8.4, you can
  configure filters that apply to all replication channels or to individual
  channels.
- Restoring an RDS snapshot or performing a Point-in-time-Restore (PITR) doesn't restore multi-source replica channel configurations.
- When you create a read replica of a multi-source replica, it only replicates
  data from the multi-source instance. It doesn't restore any channel
  configuration.
- MySQL doesn't support setting up a different number of parallel workers for each channel. Every channel gets the same number of parallel workers based on the `replica_parallel_workers` value.

The following additional limitations apply if your multi-source replication target is
a Multi-AZ DB cluster:

- A channel must be configured for a source RDS for MySQL instance before any writes to that
  instance occur.
- Each source RDS for MySQL instance must have GTID-based replication
  enabled.
- A failover event on the DB cluster removes the multi-source replication
  configuration. Restoring that configuration requires repeating the configuration
  steps.
