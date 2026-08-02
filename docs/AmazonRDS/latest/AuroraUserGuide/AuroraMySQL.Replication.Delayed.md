# Configure delayed replication with Amazon Aurora MySQL

You can use delayed replication as a strategy for disaster recovery with Aurora MySQL. With
delayed replication, you specify the minimum amount of time, in seconds, to delay replication
from the source to the read replica. In the event of a disaster, such as a table deleted
unintentionally, you complete the following steps to recover from the disaster quickly:

1. Stop replication to the read replica before the source sends the change that caused
   the disaster. Use the
   [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication")
   stored procedure to stop replication.
2. Start replication and specify that replication stops automatically at a log file
   location. You specify a location just before the disaster using the
   [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until")
   stored procedure.
3. Promote the read replica to be the new source DB cluster by using the instructions
   in [Promoting a read replica to a DB cluster for Aurora MySQL](AuroraMySQL.Replication.CrossRegion.Promote.md "AuroraMySQL.Replication.CrossRegion.Promote.md").

###### Note

Aurora MySQL supports delayed replication for version 8.4.8 and higher.

- Use stored procedures to configure delayed replication. You can't configure delayed
  replication with the AWS Management Console, the AWS CLI, or the Amazon RDS API.
- You can use replication based on global transaction identifiers (GTIDs) in a delayed
  replication configuration on Aurora MySQL version 8.4.8 and higher.
- If you use GTID-based replication, use the
  [mysql.rds\_start\_replication\_until\_gtid(Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid")
  stored procedure instead of the
  [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until")
  stored procedure.
- Aurora MySQL supports multi-source replication with up to 15 channels. Use the
  `_for_channel` procedure variants to configure delayed replication on specific channels.

###### Topics

- [Use cases for delayed replication](#AuroraMySQL.Replication.Delayed.UseCases "#AuroraMySQL.Replication.Delayed.UseCases")
- [Configure external replication with a delay](#AuroraMySQL.Replication.Delayed.Configuring "#AuroraMySQL.Replication.Delayed.Configuring")
- [Modify delayed replication for an existing read replica](#AuroraMySQL.Replication.Delayed.Modifying "#AuroraMySQL.Replication.Delayed.Modifying")
- [Set a location to stop replication to a read replica](#AuroraMySQL.Replication.Delayed.StopAt "#AuroraMySQL.Replication.Delayed.StopAt")
- [Promote a read replica](#AuroraMySQL.Replication.Delayed.Promote "#AuroraMySQL.Replication.Delayed.Promote")
- [Related topics](#AuroraMySQL.Replication.Delayed.RelatedTopics "#AuroraMySQL.Replication.Delayed.RelatedTopics")

## Use cases for delayed replication

Delayed replication on Aurora MySQL applies to binary log based replication. This includes replication from
an Aurora MySQL writer DB cluster to a binlog replica, from an external MySQL source into an Aurora MySQL
DB cluster, or across multi-source replication channels. It does not apply to Aurora Replicas within a
single DB cluster, because those read from shared cluster storage rather than from the binary log.
Common use cases include the following:

- **Disaster recovery from operator error** – Maintain a binlog
  replica that lags the source by a set interval. If a destructive statement runs
  unintentionally (for example, dropping a table), stop replication on the delayed replica
  before the source applies the change. Then roll forward to just before the event using
  [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") or
  [mysql.rds\_start\_replication\_until\_gtid(Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid"). Finally, promote the replica. This approach
  provides a faster recovery path than point-in-time recovery, which requires crash recovery and
  binary log replay.
- **Protection against logical data corruption** – A delayed
  replica also guards against a faulty application deployment or migration that gradually corrupts data.
  Because the replica holds the pre-corruption state for the length of the delay, you can recover before
  the faulty transactions are applied.
- **Major version and blue/green upgrades** – Keep a delayed binlog
  replica during an upgrade or blue/green deployment as a safety net, so that you can fall back to a
  known-good state if the upgrade introduces problems.
- **Change data capture (CDC) from an external source** – When you
  ingest changes into an Aurora MySQL DB cluster from an external MySQL source, an intentional delay gives
  you a controlled buffer before changes are applied downstream.
- **Historical inspection without a restore** – Query the delayed
  replica to see what your data looked like at an earlier time. This is useful for debugging, auditing, or
  investigating what changed, without provisioning a clone or running a point-in-time restore.
- **Testing application behavior under replication lag** – Use an
  artificially inflated delay to validate how your application behaves when a replica lags, and to run
  regression tests for lag-sensitive conditions, without having to generate heavy load to reproduce the lag.

## Configure external replication with a delay

To configure an external source with delayed replication, use the
[mysql.rds\_set\_external\_source\_with\_delay (Aurora MySQL version 8.4.8 and higher)](mysql-stored-proc-replicating.md#mysql_rds_set_external_source_with_delay "mysql-stored-proc-replicating.md#mysql_rds_set_external_source_with_delay")
stored procedure. For more information about all replication stored procedures, see
[Configuring, starting, and stopping binary log (binlog) replication](mysql-stored-proc-replicating.md "mysql-stored-proc-replicating.md").

**Example (default channel):**

```
CALL mysql.rds_set_external_source_with_delay(
  '`source-host.example.com`',
  3306,
  '`repl_user`',
  '`repl_password`',
  '`mysql-bin-changelog.000001`',
  120,
  0,
  3600);
```

**Example (specific channel):**

```
CALL mysql.rds_set_external_source_with_delay_for_channel(
  '`source-host.example.com`',
  3306,
  '`repl_user`',
  '`repl_password`',
  '`mysql-bin-changelog.000001`',
  120,
  0,
  3600,
  '`channel_1`');
```

**Parameters:**

`host_name`

The host name or IP address of the external source.

`host_port`

The port number of the external source.

`replication_user_name`

The replication user on the external source.

`replication_user_password`

The password for the replication user.

`mysql_binary_log_file_name`

The name of the binary log file on the external source.

`mysql_binary_log_file_location`

The position in the binary log file to begin replication.

`ssl_encryption`

Set this parameter to `1` to enable SSL encryption for the
replication connection, or to `0` to disable SSL encryption.

`delay`

The minimum delay in seconds (0–259,200).

`channel`

(for\_channel variant only) The channel name for multi-source replication.

**Constraints:**

- Aurora MySQL supports a maximum of 15 replication channels.
- Each channel must replicate from a different source (host:port combination).
- The delay must be between 0 and 259,200 seconds (72 hours).
- Stop replication before modifying the channel configuration.

## Modify delayed replication for an existing read replica

To modify delayed replication for an existing read replica, run the
[mysql.rds\_set\_source\_delay (Aurora MySQL version 8.4.8 and higher)](mysql-stored-proc-replicating.md#mysql_rds_set_source_delay "mysql-stored-proc-replicating.md#mysql_rds_set_source_delay")
stored procedure. For more information about all replication stored procedures, see
[Configuring, starting, and stopping binary log (binlog) replication](mysql-stored-proc-replicating.md "mysql-stored-proc-replicating.md").

**To modify delayed replication for an existing read replica:**

1. Using a MySQL client, connect to the read replica as the admin user.
2. Use the [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication")
   stored procedure to stop replication.
3. Run the [mysql.rds\_set\_source\_delay (Aurora MySQL version 8.4.8 and higher)](mysql-stored-proc-replicating.md#mysql_rds_set_source_delay "mysql-stored-proc-replicating.md#mysql_rds_set_source_delay")
   stored procedure.
4. Use the [mysql.rds\_start\_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication")
   stored procedure to start replication.

**Example (default channel):**

```
CALL mysql.rds_set_source_delay(3600);
```

**Example (specific channel):**

```
CALL mysql.rds_set_source_delay_for_channel(3600, '`channel_1`');
```

This specifies that replication to the read replica is delayed by at least one hour (3,600 seconds).
The delay value must be between 0 and 259,200 seconds (72 hours).

###### Note

Stop replication before setting the delay. If replication is running, you receive
an error that asks you to call
[mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication "mysql-stored-proc-replicating.md#mysql_rds_stop_replication") (or
`mysql.rds_stop_replication_for_channel` for a specific channel) first.

## Set a location to stop replication to a read replica

After stopping replication to the read replica, you can start replication and then stop it at a
specified binary log file location using the
[mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until")
stored procedure.

**To start replication and stop at a specific location:**

1. Using a MySQL client, connect to the read replica as the admin user.
2. Run the
   [mysql.rds\_start\_replication\_until(Aurora MySQL version 3)](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until")
   stored procedure.

**Example:**

```
CALL mysql.rds_start_replication_until(
  'mysql-bin-changelog.000777',
  120);
```

This initiates replication and replicates changes until it reaches location 120 in the
`mysql-bin-changelog.000777` binary log file. In a disaster recovery scenario, assume
that location 120 is just before the disaster.

Replication stops automatically when Aurora MySQL reaches the stop point. Aurora MySQL generates the following event:
`Replication has been stopped since the replica reached the stop point specified by the
 rds_start_replication_until stored procedure`.

If you are using GTID-based replication, use the
[mysql.rds\_start\_replication\_until\_gtid(Aurora MySQL version 3)](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid")
stored procedure instead.

## Promote a read replica

After replication is stopped, in a disaster recovery scenario, you can promote a read replica to be
the new source DB cluster. For information about promoting a read replica, see
[Promoting a read replica to a DB cluster for Aurora MySQL](AuroraMySQL.Replication.CrossRegion.Promote.md "AuroraMySQL.Replication.CrossRegion.Promote.md").

## Related topics

- For a complete reference of all replication stored procedures, see
  [Configuring, starting, and stopping binary log (binlog) replication](mysql-stored-proc-replicating.md "mysql-stored-proc-replicating.md").
