# Setting and showing binary log configuration

The following stored procedures set and show configuration parameters, such as for binary log file retention.

###### Topics

- [mysql.rds_set_configuration](#mysql_rds_set_configuration "#mysql_rds_set_configuration")
- [mysql.rds_show_configuration](#mysql_rds_show_configuration "#mysql_rds_show_configuration")

## mysql.rds_set_configuration

Specifies the number of hours to retain binary logs or the number of seconds to delay replication.

### Syntax

```
CALL mysql.rds_set_configuration(`name`,`value`);
```

### Parameters

`name`

The name of the configuration parameter to set.

`value`

The value of the configuration parameter.

### Usage notes

The `mysql.rds_set_configuration` procedure supports the following configuration parameters:

- [binlog retention hours](#mysql_rds_set_configuration-usage-notes.binlog-retention-hours "#mysql_rds_set_configuration-usage-notes.binlog-retention-hours")
- [source
  delay](#mysql_rds_set_configuration-usage-notes.source-delay "#mysql_rds_set_configuration-usage-notes.source-delay")
- [target delay](#mysql_rds_set_configuration-usage-notes.target-delay "#mysql_rds_set_configuration-usage-notes.target-delay")

The configuration parameters are stored permanently and survive any DB instance reboot or failover.

#### binlog retention hours

The `binlog retention hours` parameter is used to specify the number of hours to retain
binary log files. Amazon RDS normally purges a binary log as soon as possible, but the binary log might still be required for
replication with a MySQL database external to RDS.

The default value of `binlog retention hours` is `NULL`. For RDS for MySQL,
`NULL` means binary logs aren't retained (0 hours).

To specify the number of hours to retain binary logs on a DB instance, use the `mysql.rds_set_configuration` stored procedure and specify a
period with enough time for replication to occur, as shown in the following example.

`call mysql.rds_set_configuration('binlog retention hours', 24);`

###### Note

You can't use the value `0` for `binlog retention hours`.

For MySQL DB instances, the maximum `binlog retention hours` value is 168 (7 days).

After you set the retention period, monitor storage usage for the DB instance to
make sure that the retained binary logs don't take up too much storage.

For Multi-AZ DB cluster deployments, you can only configure binary log
retention from the writer DB instance, and the setting is propagated to all reader
DB instances asynchronously. If binary logs on the DB cluster exceed half of the total
local storage space, Amazon RDS automatically moves stale logs to the EBS volume.
However, the newest logs remain in local storage, so they're subject to be lost
if there's a failure that requires a host replacement, or if you scale the
database up or down.

#### source

delay

Use the `source delay` parameter in a read replica to specify the
number of seconds to delay replication from the read replica to its source DB
instance. Amazon RDS normally replicates changes as soon as possible, but you might
want some environments to delay replication. For example, when replication is
delayed, you can roll forward a delayed read replica to the time just before a
disaster. If a table is dropped accidentally, you can use delayed replication to
quickly recover it. The default value of `target delay` is
`0` (don't delay replication).

When you use this parameter, it runs [mysql.rds_set_source_delay](mysql-stored-proc-replicating.md#mysql_rds_set_source_delay "mysql-stored-proc-replicating.md#mysql_rds_set_source_delay") and applies CHANGE primary TO
MASTER_DELAY = input value. If successful, the procedure saves the `source
 delay` parameter to the `mysql.rds_configuration`
table.

To specify the number of seconds for Amazon RDS to delay replication to a source DB
instance, use the `mysql.rds_set_configuration` stored procedure and
specify the number of seconds to delay replication. In the following example,
the replication is delayed by at least one hour (3,600 seconds).

`call mysql.rds_set_configuration('source delay', 3600);`

The procedure then runs `mysql.rds_set_source_delay(3600)`.

The limit for the `source delay` parameter is one day (86400
seconds).

#### target delay

Use the `target delay` parameter to specify the number of seconds to delay replication between a DB
instance and any future RDS-managed read replicas created from this instance. This parameter is ignored for
non-RDS-managed read replicas. Amazon RDS normally replicates changes as soon as possible, but you might want some
environments to delay replication. For example, when replication is delayed, you can roll forward a delayed read replica
to the time just before a disaster. If a table is dropped accidentally, you can use delayed replication to recover it
quickly. The default value of `target delay` is `0` (don't delay replication).

For disaster recovery, you can use this configuration parameter with the [mysql.rds_start_replication_until](mysql-stored-proc-replicating.md#mysql_rds_start_replication_until "mysql-stored-proc-replicating.md#mysql_rds_start_replication_until") stored procedure or
the [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid")
stored procedure. To roll forward changes to a delayed read replica to the time just before a disaster, you can run the
`mysql.rds_set_configuration` procedure with this parameter set. After the
`mysql.rds_start_replication_until` or `mysql.rds_start_replication_until_gtid` procedure
stops replication, you can promote the read replica to be the new primary DB instance by using the instructions in [Promoting a read replica to be a standalone
DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

To use the `mysql.rds_rds_start_replication_until_gtid` procedure, GTID-based replication must be enabled.
To skip a specific GTID-based transaction that is known to cause disaster, you can use the [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored
procedure. For more information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

To specify the number of seconds for Amazon RDS to delay replication to a read replica, use the
`mysql.rds_set_configuration` stored procedure and specify the number of seconds to delay replication.
The following example specifies that replication is delayed by at least one hour (3,600 seconds).

`call mysql.rds_set_configuration('target delay', 3600);`

The limit for the `target delay` parameter is one day (86400 seconds).

## mysql.rds_show_configuration

The number of hours that binary logs are retained.

### Syntax

```
CALL mysql.rds_show_configuration;
```

### Usage notes

To verify the number of hours that Amazon RDS retains binary logs, use the
`mysql.rds_show_configuration` stored procedure.

### Examples

The following example displays the retention period:

```
call mysql.rds_show_configuration;
                name                         value     description
                binlog retention hours       24        binlog retention hours specifies the duration in hours before binary logs are automatically deleted.

```
