# Managing multi-source replication

The following stored procedures set up and manage replication channels on a
RDS for MySQL multi-source replica. For more information, see [Configuring multi-source-replication for Amazon RDS for MySQL](mysql-multi-source-replication.md "mysql-multi-source-replication.md").

These stored procedures are only available with RDS for MySQL DB instances running the
following engine versions:

- All 8.4 versions
- 8.0.35 and higher minor versions
- 5.7.44 and higher minor versions
  When using stored procedures to manage replication with a replication user configured with
  `caching_sha2_passwword`, you must configure TLS by specifying
  `SOURCE_SSL=1`. `caching_sha2_password` is the default
  authentication plugin for RDS for MySQL 8.4.

###### Note

Although this documentation refers to source DB instances as RDS for MySQL DB instances, these
procedures also work for MySQL instances running external to Amazon RDS.

###### Topics

- [mysql.rds_next_source_log_for_channel](#mysql_rds_next_source_log_for_channel "#mysql_rds_next_source_log_for_channel")
- [mysql.rds_reset_external_source_for_channel](#mysql_rds_reset_external_source_for_channel "#mysql_rds_reset_external_source_for_channel")
- [mysql.rds_set_external_source_for_channel](#mysql_rds_set_external_source_for_channel "#mysql_rds_set_external_source_for_channel")
- [mysql.rds_set_external_source_with_auto_position_for_channel](#mysql_rds_set_external_source_with_auto_position_for_channel "#mysql_rds_set_external_source_with_auto_position_for_channel")
- [mysql.rds_set_external_source_with_delay_for_channel](#mysql_rds_set_external_source_with_delay_for_channel "#mysql_rds_set_external_source_with_delay_for_channel")
- [mysql.rds_set_source_auto_position_for_channel](#mysql_rds_set_source_auto_position_for_channel "#mysql_rds_set_source_auto_position_for_channel")
- [mysql.rds_set_source_delay_for_channel](#mysql_rds_set_source_delay_for_channel "#mysql_rds_set_source_delay_for_channel")
- [mysql.rds_skip_repl_error_for_channel](#mysql_rds_skip_repl_error_for_channel "#mysql_rds_skip_repl_error_for_channel")
- [mysql.rds_start_replication_for_channel](#mysql_rds_start_replication_for_channel "#mysql_rds_start_replication_for_channel")
- [mysql.rds_start_replication_until_for_channel](#mysql_rds_start_replication_until_for_channel "#mysql_rds_start_replication_until_for_channel")
- [mysql.rds_start_replication_until_gtid_for_channel](#mysql_rds_start_replication_until_gtid_for_channel "#mysql_rds_start_replication_until_gtid_for_channel")
- [mysql.rds_stop_replication_for_channel](#mysql_rds_stop_replication_for_channel "#mysql_rds_stop_replication_for_channel")

## mysql.rds_next_source_log_for_channel

Changes the source DB instance log position to the start of the next binary log on the
source DB instance for the channel. Use this procedure only if you are receiving
replication I/O error 1236 on a multi-source replica.

### Syntax

```
CALL mysql.rds_next_source_log_for_channel(
`curr_master_log`,
`channel_name`
);
```

### Parameters

`curr_master_log`

The index of the current source log file. For example, if the current
file is named `mysql-bin-changelog.012345`, then the index is 12345. To determine the current source log file name, run the `SHOW
 REPLICA STATUS FOR CHANNEL '`channel_name`'` command and view the
`Source_Log_File` field.

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_next_source_log_for_channel`
procedure. If there is an IO_Thread error, for example, you can use this procedure
to skip all the events in the current binary log file and resume the replication
from the next binary log file for the channel specified in
`channel_name`.

### Example

Assume replication fails on a channel on a multi-source replica. Running
`SHOW REPLICA STATUS FOR CHANNEL 'channel_1'\G` on the multi-source
replica returns the following result:

```
mysql> SHOW REPLICA STATUS FOR CHANNEL 'channel_1'\G
*************************** 1. row ***************************
             Replica_IO_State: Waiting for source to send event
                  Source_Host: myhost.XXXXXXXXXXXXXXX.rr-rrrr-1.rds.amazonaws.com
                  Source_User: ReplicationUser
                  Source_Port: 3306
                Connect_Retry: 60
              Source_Log_File: mysql-bin-changelog.012345
          Read_Source_Log_Pos: 1219393
               Relay_Log_File: replica-relay-bin.000003
                Relay_Log_Pos: 30223388
        Relay_Source_Log_File: mysql-bin-changelog.012345
           Replica_IO_Running: No
          Replica_SQL_Running: Yes
              Replicate_Do_DB:.
              .
              .
                Last_IO_Errno: 1236
                Last_IO_Error: Got fatal error 1236 from master when reading data from binary log: 'Client requested master to start replication from impossible position; the first event 'mysql-bin-changelog.013406' at 1219393, the last event read from '/rdsdbdata/log/binlog/mysql-bin-changelog.012345' at 4, the last byte read from '/rdsdbdata/log/binlog/mysql-bin-changelog.012345' at 4.'
               Last_SQL_Errno: 0
               Last_SQL_Error:
               .
               .
                 Channel_name: channel_1
              .
              .
 -- Some fields are omitted in this example output

```

The `Last_IO_Errno` field shows that the instance is receiving
I/O error 1236. The `Source_Log_File` field shows that the file
name is `mysql-bin-changelog.012345`, which means that the log file index is `12345`. To resolve the error, you can
call `mysql.rds_next_source_log_for_channel` with the following
parameters:

```
CALL mysql.rds_next_source_log_for_channel(12345,'channel_1');
```

## mysql.rds_reset_external_source_for_channel

Stops the replication process on the specified channel, and removes the channel and
associated configurations from the multi-source replica.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set the `autocommit`
parameter to `1`. For information about modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_reset_external_source_for_channel (`channel_name`);
```

### Parameters

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_reset_external_source_for_channel`
procedure. This procedure deletes all relay logs that belong to the channel being removed.

## mysql.rds_set_external_source_for_channel

Configures a replication channel on an RDS for MySQL DB instance to replicate the data
from another RDS for MySQL DB instance.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set the `autocommit`
parameter to `1`. For information about modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### Note

You can use the [mysql.rds_set_external_source_with_delay_for_channel](#mysql_rds_set_external_source_with_delay_for_channel "#mysql_rds_set_external_source_with_delay_for_channel") stored
procedure instead to configure this channel with delayed replication.

### Syntax

```
CALL mysql.rds_set_external_source_for_channel (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `mysql_binary_log_file_name`
  , `mysql_binary_log_file_location`
  , `ssl_encryption`
  , `channel_name`
);
```

### Parameters

`host_name`

The host name or IP address of the RDS for MySQL source DB instance.

`host_port`

The port used by the RDS for MySQL source DB instance. If your network configuration
includes Secure Shell (SSH) port replication that converts the port
number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and `REPLICATION SLAVE` permissions on the RDS for MySQL source DB instance.
We recommend that you provide an account that is used solely for replication with the source DB instance.

`replication_user_password`

The password of the user ID specified in `replication_user_name`.

`mysql_binary_log_file_name`

The name of the binary log on the source DB instance that contains the
replication information.

`mysql_binary_log_file_location`

The location in the `mysql_binary_log_file_name` binary log
at which replication starts reading the replication information.

You can determine the binlog file name and location by running
`SHOW BINARY LOG STATUS` on the source DB instance.

###### Note

Previous versions of MySQL used `SHOW MASTER STATUS`
instead of `SHOW BINARY LOG STATUS`. If you are using a
MySQL version before 8.4, then use `SHOW MASTER
 STATUS`.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`channel_name`

The name of the replication channel. Each replication channel receives
the binary log events from a single source RDS for MySQL DB instance
running on a specific host and port.

### Usage notes

The master user must run the
`mysql.rds_set_external_source_for_channel` procedure. This procedure
must be run on the target RDS for MySQL DB instance on which you're creating the
replication channel.

Before you run `mysql.rds_set_external_source_for_channel`, configure
a replication user on the source DB instance with the privileges required for the
multi-source replica. To connect the multi-source replica to the source DB instance,
you must specify `replication_user_name` and
`replication_user_password` values of a replication user that has
`REPLICATION CLIENT` and `REPLICATION SLAVE` permissions
on the source DB instance.

###### To configure a replication user on the source DB instance

1. Using the MySQL client of your choice, connect to the source DB instance and create a
   user account to be used for replication. The following is an example.

###### Important

As a security best practice, specify a password other than the placeholder value shown in the following examples.

```
CREATE USER 'repl_user'@'example.com' IDENTIFIED BY '`password`';
```

2. On the source DB instance, grant `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   'repl_user' user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'example.com';
```

To use encrypted replication, configure the source DB instance to use SSL connections.

After calling `mysql.rds_set_external_source_for_channel` to configure
this replication channel, you can call [mysql.rds_start_replication_for_channel](#mysql_rds_start_replication_for_channel "#mysql_rds_start_replication_for_channel") on the replica to
start the replication process on the channel. You can call [mysql.rds_reset_external_source_for_channel](#mysql_rds_reset_external_source_for_channel "#mysql_rds_reset_external_source_for_channel") to stop replication on
the channel and remove the channel configuration from the replica.

When you call `mysql.rds_set_external_source_for_channel`, Amazon RDS records
the time, user, and an action of `set channel source` in the `mysql.rds_history` table without channel-specific details, and
in the `mysql.rds_replication_status` table, with the channel name.
This information is recorded only for internal usage and monitoring purposes. To record the complete procedure call for auditing purpose, consider
enabling audit logs or general logs, based on the specific requirements of your application.

### Examples

When run on a RDS for MySQL DB instance, the following example configures a
replication channel named `channel_1` on this DB instance to replicate
data from the source specified by host `sourcedb.example.com` and port
`3306`.

```
call mysql.rds_set_external_source_for_channel(
  'sourcedb.example.com',
  3306,
  'repl_user',
  '`password`',
  'mysql-bin-changelog.0777',
  120,
  0,
  'channel_1');

```

## mysql.rds_set_external_source_with_auto_position_for_channel

Configures a replication channel on an RDS for MySQL DB instance with an optional replication delay. The replication is based on global transaction identifiers (GTIDs).

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_source_with_auto_position_for_channel (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `ssl_encryption`
  , `delay`
  , `channel_name`
);
```

### Parameters

`host_name`

The host name or IP address of the RDS for MySQL source DB instance.

`host_port`

The port used by the RDS for MySQL source DB instance. If your network configuration
includes Secure Shell (SSH) port replication that converts the port
number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and `REPLICATION SLAVE` permissions on the RDS for MySQL source DB instance.
We recommend that you provide an account that is used solely for replication with the source DB instance.

`replication_user_password`

The password of the user ID specified in `replication_user_name`.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`delay`

The minimum number of seconds to delay replication from source DB instance.

The limit for this parameter is one day (86,400 seconds).

`channel_name`

The name of the replication channel. Each replication channel receives
the binary log events from a single source RDS for MySQL DB instance
running on a specific host and port.

### Usage notes

The master user must run the
`mysql.rds_set_external_source_with_auto_position_for_channel`
procedure. This procedure must be run on the target RDS for MySQL DB instance on which you're creating the replication channel.

Before you run `rds_set_external_source_with_auto_position_for_channel`, configure
a replication user on the source DB instance with the privileges required for the
multi-source replica. To connect the multi-source replica to the source DB instance,
you must specify `replication_user_name` and
`replication_user_password` values of a replication user that has
`REPLICATION CLIENT` and `REPLICATION SLAVE` permissions
on the source DB instance.

###### To configure a replication user on the source DB instance

1. Using the MySQL client of your choice, connect to the source DB instance and create a
   user account to be used for replication. The following is an example.

###### Important

As a security best practice, specify a password other than the placeholder value shown in the following examples.

```
CREATE USER 'repl_user'@'example.com' IDENTIFIED BY '`password`';
```

2. On the source DB instance, grant `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   'repl_user' user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'example.com';
```

To use encrypted replication, configure the source DB instance to use SSL connections.

Before you call `mysql.rds_set_external_source_with_auto_position_for_channel`,
make sure to call [mysql.rds_set_external_source_gtid_purged](mysql-stored-proc-replicating.md#mysql_rds_set_external_source_gtid_purged "mysql-stored-proc-replicating.md#mysql_rds_set_external_source_gtid_purged") to set
the `gtid_purged` system variable with a specified GTID range from an
external source.

After calling
`mysql.rds_set_external_source_with_auto_position_for_channel` to
configure an Amazon RDS DB instance as a read replica on a specific channel, you can call
[mysql.rds_start_replication_for_channel](#mysql_rds_start_replication_for_channel "#mysql_rds_start_replication_for_channel") on the read replica to
start the replication process on that channel.

After calling `mysql.rds_set_external_source_with_auto_position_for_channel` to configure
this replication channel, you can call [mysql.rds_start_replication_for_channel](#mysql_rds_start_replication_for_channel "#mysql_rds_start_replication_for_channel") on the replica to
start the replication process on the channel. You can call [mysql.rds_reset_external_source_for_channel](#mysql_rds_reset_external_source_for_channel "#mysql_rds_reset_external_source_for_channel") to stop replication on
the channel and remove the channel configuration from the replica.

### Examples

When run on a RDS for MySQL DB instance, the following example configures a
replication channel named `channel_1` on this DB instance to replicate
data from the source specified by host `sourcedb.example.com` and port
`3306` It sets the minimum replication delay to one hour (3,600
seconds). This means that a change from the source RDS for MySQL DB instance isn't
applied on the multi-source replica for at least one hour.

```
call mysql.rds_set_external_source_with_auto_position_for_channel(
  'sourcedb.example.com',
  3306,
  'repl_user',
  'password',
  1,
  3600,
  'channel_1');

```

## mysql.rds_set_external_source_with_delay_for_channel

Configures a replication channel on an RDS for MySQL DB instance with a specified replication delay.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_source_with_delay_for_channel (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `mysql_binary_log_file_name`
  , `mysql_binary_log_file_location`
  , `ssl_encryption`
  , `delay`
  , `channel_name`
);
```

### Parameters

`host_name`

The host name or IP address of the RDS for MySQL source DB instance.

`host_port`

The port used by the RDS for MySQL source DB instance. If your network configuration
includes Secure Shell (SSH) port replication that converts the port
number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and `REPLICATION SLAVE` permissions on the RDS for MySQL source DB instance.
We recommend that you provide an account that is used solely for replication with the source DB instance.

`replication_user_password`

The password of the user ID specified in `replication_user_name`.

`mysql_binary_log_file_name`

The name of the binary log on the source DB instance contains the replication information.

`mysql_binary_log_file_location`

The location in the `mysql_binary_log_file_name` binary log at which replication will start reading
the replication information.

You can determine the binlog file name and location by running
`SHOW BINARY LOG STATUS` on the source database
instance.

###### Note

Previous versions of MySQL used `SHOW MASTER STATUS`
instead of `SHOW BINARY LOG STATUS`. If you are using a
MySQL version before 8.4, then use `SHOW MASTER
 STATUS`.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is used on the replication connection. 1
specifies to use SSL encryption, 0 specifies to not use encryption. The default is 0.

###### Note

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`delay`

The minimum number of seconds to delay replication from source DB instance.

The limit for this parameter is one day (86400 seconds).

`channel_name`

The name of the replication channel. Each replication channel receives
the binary log events from a single source RDS for MySQL DB instance
running on a specific host and port.

### Usage notes

The master user must run the
`mysql.rds_set_external_source_with_delay_for_channel` procedure.
This procedure must be run on the target RDS for MySQL DB instance on which you're creating the replication channel.

Before you run `mysql.rds_set_external_source_with_delay_for_channel`, configure
a replication user on the source DB instance with the privileges required for the
multi-source replica. To connect the multi-source replica to the source DB instance,
you must specify `replication_user_name` and
`replication_user_password` values of a replication user that has
`REPLICATION CLIENT` and `REPLICATION SLAVE` permissions
on the source DB instance.

###### To configure a replication user on the source DB instance

1. Using the MySQL client of your choice, connect to the source DB instance and create a
   user account to be used for replication. The following is an example.

###### Important

As a security best practice, specify a password other than the placeholder value shown in the following examples.

```
CREATE USER 'repl_user'@'example.com' IDENTIFIED BY '`password`';
```

2. On the source DB instance, grant `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   'repl_user' user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'example.com';
```

To use encrypted replication, configure the source DB instance to use SSL connections.

After calling `mysql.rds_set_external_source_with_delay_for_channel` to configure
this replication channel, you can call [mysql.rds_start_replication_for_channel](#mysql_rds_start_replication_for_channel "#mysql_rds_start_replication_for_channel") on the replica to
start the replication process on the channel. You can call [mysql.rds_reset_external_source_for_channel](#mysql_rds_reset_external_source_for_channel "#mysql_rds_reset_external_source_for_channel") to stop replication on
the channel and remove the channel configuration from the replica.

When you call `mysql.rds_set_external_source_with_delay_for_channel`, Amazon RDS records
the time, user, and an action of `set channel source` in the `mysql.rds_history` table without channel-specific details, and
in the `mysql.rds_replication_status` table, with the channel name.
This information is recorded only for internal usage and monitoring purposes. To record the complete procedure call for auditing purpose, consider
enabling audit logs or general logs, based on the specific requirements of your application.

### Examples

When run on a RDS for MySQL DB instance, the following example configures a
replication channel named `channel_1` on this DB instance to replicate
data from the source specified by host `sourcedb.example.com` and port
`3306` It sets the minimum replication delay to one hour (3,600
seconds). This means that a change from the source RDS for MySQL DB instance isn't
applied on the multi-source replica for at least one hour.

```
call mysql.rds_set_external_source_with_delay_for_channel(
  'sourcedb.example.com',
  3306,
  'repl_user',
  'password',
  'mysql-bin-changelog.000777',
  120,
  1,
  3600,
  'channel_1');

```

## mysql.rds_set_source_auto_position_for_channel

Sets the replication mode for the specified channel to be based on either binary log file positions or on global transaction identifiers (GTIDs).

### Syntax

```
CALL mysql.rds_set_source_auto_position_for_channel (
`auto_position_mode`
 , `channel_name`
);
```

### Parameters

`auto_position_mode`

A value that indicates whether to use log file position replication or
GTID-based replication:

- `0` – Use the replication method based on
  binary log file position. The default is `0`.
- `1` – Use the GTID-based replication method.

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_set_source_auto_position_for_channel`
procedure. This procedure restarts replication on the specified channel to apply the specified auto position mode.

### Examples

The following example sets the auto position mode for channel_1 to use the GTID-based replication method.

```
call mysql.rds_set_source_auto_position_for_channel(1,'channel_1');

```

## mysql.rds_set_source_delay_for_channel

Sets the minimum number of seconds to delay replication from the source database
instance to the multi-source replica for the specified channel.

### Syntax

```
CALL mysql.rds_set_source_delay_for_channel(`delay`, `channel_name`);
```

### Parameters

`delay`

The minimum number of seconds to delay replication from the source DB instance.

The limit for this parameter is one day (86400 seconds).

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_set_source_delay_for_channel`
procedure. To use this procedure, first call
`mysql.rds_stop_replication_for_channel` to stop the replication.
Then, call this procedure to set the replication delay value. When the delay is set,
call `mysql.rds_start_replication_for_channel` to restart the
replication.

### Examples

The following example sets the delay for replication from the source database
instance on `channel_1` of the multi-source replica for at least one hour
(3,600 seconds).

```
CALL mysql.rds_set_source_delay_for_channel(3600,'channel_1');
```

## mysql.rds_skip_repl_error_for_channel

Skips a binary log event and deletes a replication error on a MySQL DB multi-source
replica for the specified channel.

### Syntax

```
CALL mysql.rds_skip_repl_error_for_channel(`channel_name`);
```

### Parameters

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_skip_repl_error_for_channel`
procedure on a read replica. You can use this procedure in a similar way
`mysql.rds_skip_repl_error` is used to skip an error on a read
replica. For more information, see [Calling the
mysql.rds_skip_repl_error procedure](Appendix.MySQL.CommonDBATasks.md#Appendix.MySQL.CommonDBATasks.SkipError.procedure "Appendix.MySQL.CommonDBATasks.md#Appendix.MySQL.CommonDBATasks.SkipError.procedure").

###### Note

To skip errors in GTID-based replication, we recommend that you use the procedure [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") instead.

To determine if there are errors, run the MySQL `SHOW REPLICA STATUS FOR CHANNEL '`channel_name`'\G`
command. If a replication error isn't critical, you can run
`mysql.rds_skip_repl_error_for_channel` to skip the error. If there are multiple
errors, `mysql.rds_skip_repl_error_for_channel` deletes the first error on the specified replication channel, then warns
that others are present. You can then use `SHOW REPLICA STATUS FOR CHANNEL '`channel_name`'\G` to
determine the correct course of action for the next error. For information about the
values returned, see
[SHOW REPLICA STATUS
statement](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html") in the MySQL documentation.

## mysql.rds_start_replication_for_channel

Initiates replication from an RDS for MySQL DB instance to a multi-source replica on the specified channel.

###### Note

You can use the [mysql.rds_start_replication_until_for_channel](#mysql_rds_start_replication_until_for_channel "#mysql_rds_start_replication_until_for_channel") or
[mysql.rds_start_replication_until_gtid_for_channel](#mysql_rds_start_replication_until_gtid_for_channel "#mysql_rds_start_replication_until_gtid_for_channel")
stored procedure to initiate replication from an RDS for MySQL DB instance and stop replication at the specified binary log file location.

### Syntax

```
CALL mysql.rds_start_replication_for_channel(`channel_name`);
```

### Parameters

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_start_replication_for_channel`
procedure. After you import the data from the source RDS for MySQL DB instance, run
this command on the multi-source replica to start replication on the specified
channel.

### Examples

The following example starts replication on `channel_1` of the
multi-source replica.

```
CALL mysql.rds_start_replication_for_channel('channel_1');
```

## mysql.rds_start_replication_until_for_channel

Initiates replication from an RDS for MySQL DB instance on the specified channel and stops replication at the specified binary log file location.

### Syntax

```
CALL mysql.rds_start_replication_until_for_channel (
`replication_log_file`
  , `replication_stop_point`
  , `channel_name`
);
```

### Parameters

`replication_log_file`

The name of the binary log on the source DB instance contains the
replication information.

`replication_stop_point`

The location in the `replication_log_file`
binary log at which replication will stop.

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the
`mysql.rds_start_replication_until_for_channel` procedure. With this
procedure, replication starts and then stops when the specified binlog file position
is reached. This procedure stops both the `SQL_THREAD` and
`IO_THREAD`.

The file name specified for the `replication_log_file` parameter must match the source DB instance binlog file name.

When the `replication_stop_point` parameter specifies a stop location
that's in the past, replication is stopped immediately.

### Examples

The following example initiates replication on `channel_1`, and replicates changes until it reaches location `120` in the
`mysql-bin-changelog.000777` binary log file.

```
call mysql.rds_start_replication_until_for_channel(
  'mysql-bin-changelog.000777',
  120,
  'channel_1'
  );

```

## mysql.rds_start_replication_until_gtid_for_channel

Initiates replication on the specified channel from an RDS for MySQL DB instance and stops replication at the specified global transaction identifier (GTID).

### Syntax

```
CALL mysql.rds_start_replication_until_gtid_for_channel(`gtid`,`channel_name`);
```

### Parameters

`gtid`

The GTID after which to stop replication.

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_start_replication_until_gtid_for_channel`
procedure. The procedure starts replication on the specified channel and applies all changes up to the specified GTID value. Then, it stops replication on the channel.

When the `gtid` parameter specifies a transaction that has already been run by the replica, replication is stopped immediately.

Before you run this procedure, you must disable multi-threaded replication by setting the value of `replica_parallel_workers` or `slave_parallel_workers`
to `0`.

### Examples

The following example initiates replication on `channel_1`, and replicates changes until it reaches GTID `3E11FA47-71CA-11E1-9E33-C80AA9429562:23`.

```
call mysql.rds_start_replication_until_gtid_for_channel('3E11FA47-71CA-11E1-9E33-C80AA9429562:23','channel_1');

```

## mysql.rds_stop_replication_for_channel

Stops replication from a MySQL DB instance on the specified channel.

### Syntax

```
CALL mysql.rds_stop_replication_for_channel(`channel_name`);
```

### Parameters

`channel_name`

The name of the replication channel on the multi-source replica. Each replication channel receives the binary log events from a
single source RDS for MySQL DB instance running on a specific host and port.

### Usage notes

The master user must run the `mysql.rds_stop_replication_for_channel` procedure.

### Examples

The following example stops replication on `channel_1` of the
multi-source replica.

```
CALL mysql.rds_stop_replication_for_channel('channel_1');
```
