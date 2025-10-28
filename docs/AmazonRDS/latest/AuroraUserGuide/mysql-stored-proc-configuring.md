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

The configuration parameters are stored permanently and survive any DB instance reboot or failover.

#### binlog retention hours

The `binlog retention hours` parameter is used to specify the number
of hours to retain binary log files. Amazon Aurora normally purges a binary log as soon as possible, but the binary log
might still be required for replication with a MySQL database external to Aurora.

The default value of `binlog retention hours` is
`NULL`. For Aurora MySQL, `NULL` means binary logs are
cleaned up lazily. Aurora MySQL binary logs might remain in the system for a
certain period, which is usually not longer than a day.

To specify the number of hours to retain binary logs on a DB cluster, use the `mysql.rds_set_configuration` stored procedure and specify a
period with enough time for replication to occur, as shown in the following example.

`call mysql.rds_set_configuration('binlog retention hours', 24);`

###### Note

You can't use the value `0` for `binlog retention hours`.

For Aurora MySQL version 2.11.0 and higher and version 3 DB clusters, the maximum `binlog retention
 hours` value is 2160 (90 days).

After you set the retention period, monitor storage usage for the DB instance to
make sure that the retained binary logs don't take up too much storage.

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
