

# Configure multi-source replication for Amazon Aurora MySQL
<a name="AuroraMySQL.Replication.MultiSource"></a>

With multi-source replication, you can set up an Amazon Aurora MySQL DB cluster as a replica that receives binary log events from more than one source MySQL database. Each source can be an RDS for MySQL DB instance, another Aurora MySQL DB cluster, or a MySQL database running external to Amazon RDS.

Multi-source replication is supported for Aurora MySQL DB clusters running the following engine versions:
+ Aurora MySQL 8.4.8 and above

For more information about MySQL multi-source replication, see [MySQL Multi-Source Replication](https://dev.mysql.com/doc/refman/8.4/en/replication-multi-source.html) in the MySQL documentation.

**Note**  
Multi-source replication on Aurora MySQL uses the writer (primary) instance of the Aurora DB cluster as the replication target. All replication stored procedures must be called while connected to the writer instance of the cluster.

## Use cases for multi-source replication
<a name="AuroraMySQL.Replication.MultiSource.UseCases"></a>

Consider using multi-source replication on Aurora MySQL in the following cases:
+ **Shard consolidation** – Applications that need to merge or combine data from multiple shards hosted on separate DB instances into a single Aurora MySQL DB cluster.
+ **Consolidated reporting** – Applications that need to generate reports from data consolidated from multiple sources, taking advantage of Aurora's read scaling capabilities.
+ **Long-term backups** – Requirements to create consolidated long-term backups of data that's distributed among multiple MySQL-compatible DB instances.
+ **Cross-engine migration** – Consolidating data from multiple RDS for MySQL instances or external MySQL servers into a single Aurora MySQL cluster during migration.
+ **Multi-tenant aggregation** – Consolidating multiple single-tenant databases into a multi-tenant Aurora cluster for cost optimization and simplified management.

## Prerequisites for multi-source replication
<a name="AuroraMySQL.Replication.MultiSource.Prerequisites"></a>

Before you configure multi-source replication on your Aurora MySQL DB cluster, complete the standard prerequisites for binary log replication as described in [Setting up binary log replication for Aurora MySQL](AuroraMySQL.Replication.MySQL.SettingUp.md). This includes enabling binary logging on each source, retaining binary logs, creating a replication user, and creating a copy or dump of each source. For multi-source replication, repeat these steps for each source DB instance.

In addition to the standard prerequisites, ensure that you meet the following requirements specific to multi-source replication.
+ Verify the Aurora MySQL target cluster version and configuration
  + The Aurora MySQL DB cluster must be running a supported engine version (Aurora MySQL 8.4.8 and above).
  + Enable autocommit on the Aurora MySQL writer instance. Set the `autocommit` parameter to `1` in your DB cluster parameter group.
+ Configure network connectivity for each source

  For each source DB instance, ensure that the Aurora MySQL writer instance can connect to the source on the specified port. Options include:
  + If both source and target are in the same VPC, configure the security group on the source DB instance to allow inbound connections on port 3306 (or your custom port) from the Aurora MySQL cluster's security group.
  + If they are in different VPCs, set up VPC peering or use a transit gateway. For more information, see [A DB cluster in a VPC accessed by an EC2 instance in a different VPC](USER_VPC.Scenarios.md#USER_VPC.Scenario3).
  + If the source is external to AWS, ensure network routes are available (for example, through or a VPN connection).

**Note**  
Because multi-source replication involves multiple sources, you must verify connectivity to each source independently. Ensure that security groups and routing accommodate all source endpoints simultaneously.

## Configure multi-source replication channels on Aurora MySQL DB clusters
<a name="AuroraMySQL.Replication.MultiSource.Configure"></a>

Configuring multi-source replication channels on Aurora MySQL is similar to configuring single-source replication. For multi-source replication, you first enable binary logging on the source instances, import data from the sources to the Aurora MySQL cluster, and then start replication from each source using the binary log coordinates or GTID auto-positioning.

**Important**  
All multi-source replication stored procedures must be called while connected to the **writer instance** of the Aurora MySQL DB cluster. If a failover occurs, you must reconnect to the new writer instance.

### Step 1: Import data from the source DB instances to the Aurora MySQL cluster
<a name="AuroraMySQL.Replication.MultiSource.Configure.Step1"></a>

Perform the following steps for each source DB instance.

1. Determine the current binary log file and position on the source DB instance.

   ```
   SHOW BINARY LOG STATUS;
   ```

   ```
   SHOW MASTER STATUS;
   ```

   Example output:

   ```
   +----------------------------+----------+
   | File                       | Position |
   +----------------------------+----------+
   | mysql-bin-changelog.000031 |      107 |
   +----------------------------+----------+
   ```

   Record the `File` and `Position` values. You need them in a later step.

1. Copy the database from the source DB instance to the Aurora MySQL cluster using `mysqldump`.

   ```
   mysqldump --databases {{database_name}} \
     --single-transaction \
     --compress \
     --order-by-primary \
     -u {{RDS_user_name}} \
     -p'{{RDS_password}}' \
     --host={{source-endpoint.region.rds.amazonaws.com}} | mysql \
     --host={{aurora-cluster-endpoint.cluster-xxxxxx.region.rds.amazonaws.com}} \
     --port=3306 \
     -u {{aurora_user_name}} \
     -p'{{aurora_password}}'
   ```
**Tip**  
For large databases, consider using AWS DMS or creating a snapshot and restoring to reduce data transfer time.

1. After the data import is complete, you can re-enable writes on the source DB instance if you had previously set it to read-only.

### Step 2: Start replication from the source DB instances to the Aurora MySQL cluster
<a name="AuroraMySQL.Replication.MultiSource.Configure.Step2"></a>

For each source DB instance, connect to the **writer instance** of the Aurora MySQL DB cluster and run the stored procedures to configure and start replication on a channel.

```
CALL mysql.rds_set_external_source_for_channel(
  '{{source-endpoint.region.rds.amazonaws.com}}',
  3306,
  '{{repl_user}}',
  '{{password}}',
  '{{mysql-bin-changelog.000031}}',
  107,
  0,
  '{{channel_1}}'
);

CALL mysql.rds_start_replication_for_channel('{{channel_1}}');
```

If your source DB instances use GTID-based replication, you can use auto-positioning instead of specifying binary log coordinates:

```
CALL mysql.rds_set_external_source_with_auto_position_for_channel(
  '{{source-endpoint.region.rds.amazonaws.com}}',
  3306,
  '{{repl_user}}',
  '{{password}}',
  0,
  0,
  '{{channel_1}}'
);

CALL mysql.rds_start_replication_for_channel('{{channel_1}}');
```

**Note**  
When using GTID auto-positioning, ensure that the `gtid_mode` and `enforce_gtid_consistency` parameters are configured consistently across all source instances and the Aurora MySQL cluster.

Repeat these steps for each source DB instance, specifying a unique channel name for each (for example, `channel_1`, `channel_2`, `channel_3`).

## Use filters with multi-source replication
<a name="AuroraMySQL.Replication.MultiSource.Filters"></a>

You can use replication filters to specify which databases and tables are replicated to the Aurora MySQL multi-source replica. For more information about replication filters, see [Configuring replication filters with Aurora MySQL](AuroraMySQL.Replication.Filters.md). The following describes additional channel-level filter capabilities available with multi-source replication.

With multi-source replication, you can configure replication filters at two levels:
+ **Global filters** – Apply to all channels. Set using the Aurora MySQL DB cluster parameter group (for example, `replicate-do-db`, `replicate-ignore-db`).
+ **Channel-level filters** – Apply only to specific channels, overriding global filters for that channel.
+ You must restart replication after changing channel-level filters.
+ If no channel-specific filter is configured, Aurora MySQL applies the global filters for that channel.
+ If a filter is applied both globally and at the channel level, only the channel-level filter is applied for that channel.

## Monitor multi-source replication channels
<a name="AuroraMySQL.Replication.MultiSource.Monitoring"></a>

You can monitor individual channels on an Aurora MySQL multi-source replica using the following methods.

### Use SHOW REPLICA STATUS
<a name="AuroraMySQL.Replication.MultiSource.Monitoring.ShowReplicaStatus"></a>

Connect to the writer instance of the Aurora MySQL DB cluster and run:

```
-- View status for all channels
SHOW REPLICA STATUS\G

-- View status for a specific channel
SHOW REPLICA STATUS FOR CHANNEL '{{channel_1}}'\G
```

Key fields to monitor:


| Field | Description | 
| --- | --- | 
| Replica\_IO\_Running | Whether the I/O thread for the channel is running | 
| Replica\_SQL\_Running | Whether the SQL thread for the channel is running | 
| Seconds\_Behind\_Source | Replication lag in seconds for the channel | 
| Last\_IO\_Error | Last I/O error encountered on the channel | 
| Last\_SQL\_Error | Last SQL error encountered on the channel | 
| Source\_Log\_File | The current binary log file being read from the source | 
| Exec\_Source\_Log\_Pos | The position in the binary log that the SQL thread has applied | 

### Use CloudWatch metrics
<a name="AuroraMySQL.Replication.MultiSource.Monitoring.CloudWatch"></a>

Monitor the `ReplicationChannelLag` CloudWatch metric for each replication channel. This metric provides per-channel replication lag data with a 60-second period and is available for 15 days. To locate the replication channel lag, use the Aurora DB cluster instance identifier and the replication channel name as dimensions. You can configure CloudWatch alarms to receive notification when the lag exceeds a specific threshold. For more information, see [Monitoring metrics in an Amazon Aurora cluster](MonitoringAurora.md).

## Manage multi-source replication stored procedures
<a name="AuroraMySQL.Replication.MultiSource.StoredProcedures"></a>

For information about using stored procedures to set up and manage your multi-source replication channels, see [Managing multi-source replication](mysql-stored-proc-multi-source-replication.md).

## Considerations and best practices
<a name="AuroraMySQL.Replication.MultiSource.Considerations"></a>

For general replication optimization recommendations including binary log format, parallel workers, and Enhanced Binlog, see [Optimizing binary log replication for Aurora MySQL](binlog-optimization.md). The following considerations are specific to multi-source replication.

### Resource planning
<a name="AuroraMySQL.Replication.MultiSource.Considerations.Resources"></a>

When running multiple replication channels, the total number of replication threads allocated on the replica is: (`replica_parallel_workers` \+ 1 coordinator thread) × number of channels. For example, with the default `replica_parallel_workers` value of 4 and 10 channels, Aurora MySQL allocates 50 replication threads. Consider using a larger DB instance class (such as db.r6g.2xlarge or larger) based on your total source throughput and channel count. Each channel receives the same number of parallel workers. MySQL does not support setting different parallel worker counts per channel.

### Avoiding conflicts
<a name="AuroraMySQL.Replication.MultiSource.Considerations.Conflicts"></a>

MySQL multi-source replication does not provide conflict detection or resolution. You must ensure that changes from different sources are non-conflicting. Common strategies include:
+ Each source writes to a different database or set of tables.
+ Use replication filters (`replicate-do-db`) to ensure each channel replicates only the databases it is responsible for.
+ Use the `replicate-rewrite-db` option to remap a schema name from the source to a different name on the replica, if needed.

To prevent conflicting writes from applications connecting directly to the multi-source replica, enable read-only mode on the Aurora MySQL cluster: `CALL mysql.rds_set_read_only(1);`

### Operational best practices
<a name="AuroraMySQL.Replication.MultiSource.Considerations.Operational"></a>
+ **One channel at a time** – Perform management operations (such as configuration changes, skipping errors, or starting/stopping replication) on one channel at a time. Avoid concurrent changes to multiple channels from different connections.
+ **Monitor per-channel lag** – Monitor replication lag for each channel using the `ReplicationChannelLag` CloudWatch metric.
+ **Source failover handling** – If a source DB instance fails over (for example, an Amazon RDS Multi-AZ failover), the replication channel may stop with an I/O error. After the source is available again:
  + Call `mysql.rds_start_replication_for_channel` to resume replication.
  + If error 1236 occurs (log file not found), call `mysql.rds_next_source_log_for_channel` to advance to the next binary log file.
+ **Aurora writer failover** – If the Aurora MySQL writer instance fails over to a reader, replication channel configurations are preserved on the cluster's shared storage. After failover completes, the replication threads are automatically restarted on the new writer instance.

## Limitations
<a name="AuroraMySQL.Replication.MultiSource.Limitations"></a>

The following limitations are specific to Aurora MySQL multi-source replication. For general MySQL multi-source replication limitations (such as parallel worker configuration per channel), see [MySQL Multi-Source Replication](https://dev.mysql.com/doc/refman/8.4/en/replication-multi-source.html) in the MySQL documentation.
+ Multi-source replication is supported only on Aurora MySQL version 8.4.8 and higher.
+ Aurora MySQL supports configuring a maximum of **15 channels** for a multi-source replica.

## Troubleshooting
<a name="AuroraMySQL.Replication.MultiSource.Troubleshooting"></a>

For general replication troubleshooting, see [ Amazon Aurora MySQL replication issues](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL). The following are multi-source replication specific troubleshooting notes.

### Channel configuration not restored after snapshot restore
<a name="AuroraMySQL.Replication.MultiSource.Troubleshooting.Snapshot"></a>

DB cluster snapshots don't include multi-source channel configurations. After you restore from a snapshot:
+ Reconfigure each channel using `mysql.rds_set_external_source_for_channel` or `mysql.rds_set_external_source_with_auto_position_for_channel`.
+ If using GTID auto-positioning, the replica can automatically resume from where it left off.
+ If using binary log file positions, determine the current position by comparing the source's binary log with the last applied transaction on the restored cluster.

### Replication lag increasing on one or more channels
<a name="AuroraMySQL.Replication.MultiSource.Troubleshooting.Lag"></a>
+ Check the writer instance's CPU and I/O metrics. If resource utilization is high, scale up the instance class.
+ Consider increasing `replica_parallel_workers` to improve SQL thread throughput.
+ Verify that there are no long-running transactions or DDL operations on the channel that might be blocking the SQL thread.
+ Check for conflicting filter configurations that might cause replication to process and then discard large numbers of events.

## Example: Complete multi-source setup with three sources
<a name="AuroraMySQL.Replication.MultiSource.Example"></a>

The following example demonstrates configuring an Aurora MySQL DB cluster as a multi-source replica of three RDS for MySQL source instances.

### Step 1: Record binary log positions on each source
<a name="AuroraMySQL.Replication.MultiSource.Example.Step1"></a>

Connect to each source and record the binary log coordinates:

```
-- On source 1 (orders-db.xxxxx.us-east-1.rds.amazonaws.com)
SHOW BINARY LOG STATUS;
-- Result: mysql-bin-changelog.000045, Position: 3892

-- On source 2 (inventory-db.xxxxx.us-east-1.rds.amazonaws.com)
SHOW BINARY LOG STATUS;
-- Result: mysql-bin-changelog.000012, Position: 1567

-- On source 3 (analytics-db.xxxxx.us-east-1.rds.amazonaws.com)
SHOW BINARY LOG STATUS;
-- Result: mysql-bin-changelog.000078, Position: 9421
```

### Step 2: Import data from each source
<a name="AuroraMySQL.Replication.MultiSource.Example.Step2"></a>

```
# Import from source 1
mysqldump --databases orders_db --single-transaction --compress \
 -u admin -p --host=orders-db.xxxxx.us-east-1.rds.amazonaws.com | \
 mysql --host=my-aurora-cluster.cluster-xxxxx.us-east-1.rds.amazonaws.com -u admin -p

# Import from source 2
mysqldump --databases inventory_db --single-transaction --compress \
 -u admin -p --host=inventory-db.xxxxx.us-east-1.rds.amazonaws.com | \
 mysql --host=my-aurora-cluster.cluster-xxxxx.us-east-1.rds.amazonaws.com -u admin -p

# Import from source 3
mysqldump --databases analytics_db --single-transaction --compress \
 -u admin -p --host=analytics-db.xxxxx.us-east-1.rds.amazonaws.com | \
 mysql --host=my-aurora-cluster.cluster-xxxxx.us-east-1.rds.amazonaws.com -u admin -p
```

### Step 3: Configure and start replication channels
<a name="AuroraMySQL.Replication.MultiSource.Example.Step3"></a>

Connect to the Aurora MySQL writer instance:

```
-- Configure channel for source 1 (orders)
CALL mysql.rds_set_external_source_for_channel(
 'orders-db.xxxxx.us-east-1.rds.amazonaws.com',
 3306, 'repl_user', 'password',
 'mysql-bin-changelog.000045', 3892, 0, 'orders_channel'
);

-- Configure channel for source 2 (inventory)
CALL mysql.rds_set_external_source_for_channel(
 'inventory-db.xxxxx.us-east-1.rds.amazonaws.com',
 3306, 'repl_user', 'password',
 'mysql-bin-changelog.000012', 1567, 0, 'inventory_channel'
);

-- Configure channel for source 3 (analytics)
CALL mysql.rds_set_external_source_for_channel(
 'analytics-db.xxxxx.us-east-1.rds.amazonaws.com',
 3306, 'repl_user', 'password',
 'mysql-bin-changelog.000078', 9421, 0, 'analytics_channel'
);

-- Start all channels
CALL mysql.rds_start_replication_for_channel('orders_channel');
CALL mysql.rds_start_replication_for_channel('inventory_channel');
CALL mysql.rds_start_replication_for_channel('analytics_channel');
```

### Step 4: Verify replication status
<a name="AuroraMySQL.Replication.MultiSource.Example.Step4"></a>

```
SHOW REPLICA STATUS\G
```

Confirm that for each channel:
+ `Replica_IO_Running: Yes`
+ `Replica_SQL_Running: Yes`
+ `Seconds_Behind_Source: 0` (or a low value)

## Related resources
<a name="AuroraMySQL.Replication.MultiSource.RelatedResources"></a>
+ [MySQL Multi-Source Replication](https://dev.mysql.com/doc/refman/8.4/en/replication-multi-source.html) – MySQL documentation
+ [Replication between Aurora and MySQL or between Aurora and another Aurora DB cluster (binary log replication)](AuroraMySQL.Replication.MySQL.md) – Aurora User Guide
+ [Optimizing binary log replication for Aurora MySQL](binlog-optimization.md) – Aurora User Guide
+ [Configuring replication filters with Aurora MySQL](AuroraMySQL.Replication.Filters.md) – Aurora User Guide
+ [Using GTID-based replication](mysql-replication-gtid.md) – Aurora User Guide