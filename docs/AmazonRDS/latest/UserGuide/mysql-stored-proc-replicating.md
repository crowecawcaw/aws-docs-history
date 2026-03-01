# Configuring, starting, and stopping binary log (binlog) replication

The following stored procedures control how transactions are
replicated from an external database into RDS for MySQL, or from RDS for MySQL to an external
database.

When using these stored procedures to manage replication with a
replication user configured with `caching_sha2_password`, you must configure TLS
by specifying `SOURCE_SSL=1`. `caching_sha2_password` is the default
authentication plugin for RDS for MySQL 8.4 For more information, see [Encrypting with SSL/TLS](mysql-ssl-connections.md "mysql-ssl-connections.md").

For information about configuring, using, and managing read replicas, see [Working with MySQL read replicas](USER_MySQL.Replication.md "USER_MySQL.Replication.md").

###### Topics

- [mysql.rds_next_master_log (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_next_master_log "#mysql_rds_next_master_log")
- [mysql.rds_next_source_log (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_next_source_log "#mysql_rds_next_source_log")
- [mysql.rds_reset_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_reset_external_master "#mysql_rds_reset_external_master")
- [mysql.rds_reset_external_source (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_reset_external_source "#mysql_rds_reset_external_source")
- [mysql.rds_set_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master "#mysql_rds_set_external_master")
- [mysql.rds_set_external_source (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_external_source "#mysql_rds_set_external_source")
- [mysql.rds_set_external_master_with_auto_position (RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master_with_auto_position "#mysql_rds_set_external_master_with_auto_position")
- [mysql.rds_set_external_source_with_auto_position (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_external_source_with_auto_position "#mysql_rds_set_external_source_with_auto_position")
- [mysql.rds_set_external_master_with_delay (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master_with_delay "#mysql_rds_set_external_master_with_delay")
- [mysql.rds_set_external_source_with_delay (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_external_source_with_delay "#mysql_rds_set_external_source_with_delay")
- [mysql.rds_set_external_source_gtid_purged](#mysql_rds_set_external_source_gtid_purged "#mysql_rds_set_external_source_gtid_purged")
- [mysql.rds_set_master_auto_position (RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_master_auto_position "#mysql_rds_set_master_auto_position")
- [mysql.rds_set_source_auto_position (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_source_auto_position "#mysql_rds_set_source_auto_position")
- [mysql.rds_set_source_delay](#mysql_rds_set_source_delay "#mysql_rds_set_source_delay")
- [mysql.rds_skip_repl_error](#mysql_rds_skip_repl_error "#mysql_rds_skip_repl_error")
- [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication")
- [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until")
- [mysql.rds_stop_replication](#mysql_rds_stop_replication "#mysql_rds_stop_replication")

## mysql.rds_next_master_log (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)

Changes the source database instance log position to the start of the next binary log
on the source database instance. Use this procedure only if you are receiving
replication I/O error 1236 on a read replica.

### Syntax

```
CALL mysql.rds_next_master_log(
`curr_master_log`
);
```

### Parameters

`curr_master_log`

The index of the current master log file. For example, if the current
file is named `mysql-bin-changelog.012345`, then the index is 12345. To determine the current master log file name, run the `SHOW
 REPLICA STATUS` command and view the
`Master_Log_File` field.

### Usage notes

The master user must run the `mysql.rds_next_master_log` procedure.

###### Warning

Call `mysql.rds_next_master_log` only if replication fails after a
failover of a Multi-AZ DB instance that is the replication source, and the
`Last_IO_Errno` field of `SHOW REPLICA STATUS` reports
I/O error 1236.

Calling `mysql.rds_next_master_log` can result in data loss in the
read replica if transactions in the source instance were not written to the
binary log on disk before the failover event occurred. You can reduce the chance of this happening by setting the
source instance parameters `sync_binlog` and
`innodb_support_xa` to `1`, even though this might
reduce performance. For more information, see [Troubleshooting a MySQL read replica problem](USER_ReadRepl.md "USER_ReadRepl.md").

### Examples

Assume replication fails on an RDS for MySQL read replica.
Running `SHOW REPLICA STATUS\G` on the read replica returns the following
result:

```
*************************** 1. row ***************************
             Replica_IO_State:
                  Source_Host: myhost.XXXXXXXXXXXXXXX.rr-rrrr-1.rds.amazonaws.com
                  Source_User: MasterUser
                  Source_Port: 3306
                Connect_Retry: 10
              Source_Log_File: mysql-bin-changelog.012345
          Read_Source_Log_Pos: 1219393
               Relay_Log_File: relaylog.012340
                Relay_Log_Pos: 30223388
        Relay_Source_Log_File: mysql-bin-changelog.012345
           Replica_IO_Running: No
          Replica_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Source_Log_Pos: 30223232
              Relay_Log_Space: 5248928866
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Source_SSL_Allowed: No
           Source_SSL_CA_File:
           Source_SSL_CA_Path:
              Source_SSL_Cert:
            Source_SSL_Cipher:
               Source_SSL_Key:
        Seconds_Behind_Master: NULL
Source_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 1236
                Last_IO_Error: Got fatal error 1236 from master when reading data from binary log: 'Client requested master to start replication from impossible position; the first event 'mysql-bin-changelog.013406' at 1219393, the last event read from '/rdsdbdata/log/binlog/mysql-bin-changelog.012345' at 4, the last byte read from '/rdsdbdata/log/binlog/mysql-bin-changelog.012345' at 4.'
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Source_Server_Id: 67285976

```

The `Last_IO_Errno` field shows that the instance is receiving I/O
error 1236. The `Master_Log_File` field shows that the file name is
`mysql-bin-changelog.012345`, which means that the log file index is
`12345`. To resolve the error, you can call
`mysql.rds_next_master_log` with the following parameter:

```
CALL mysql.rds_next_master_log(12345);
```

## mysql.rds_next_source_log (RDS for MySQL major versions 8.4 and higher)

Changes the source database instance log position to the start of the next binary log
on the source database instance. Use this procedure only if you are receiving
replication I/O error 1236 on a read replica.

### Syntax

```
CALL mysql.rds_next_source_log(
`curr_source_log`
);
```

### Parameters

`curr_source_log`

The index of the current source log file. For example, if the current
file is named `mysql-bin-changelog.012345`, then the index is 12345. To determine the current source log file name, run the `SHOW
 REPLICA STATUS` command and view the
`Source_Log_File` field.

### Usage notes

The administrative user must run the `mysql.rds_next_source_log`
procedure.

###### Warning

Call `mysql.rds_next_source_log` only if replication fails after a
failover of a Multi-AZ DB instance that is the replication source, and the
`Last_IO_Errno` field of `SHOW REPLICA STATUS` reports
I/O error 1236.

Calling `mysql.rds_next_source_log` can result in data loss in the
read replica if transactions in the source instance were not written to the
binary log on disk before the failover event occurred. You can reduce the chance
of this happening by setting the source instance parameters
`sync_binlog` and `innodb_support_xa` to
`1`, even though this might reduce performance. For more information, see [Troubleshooting a MySQL read replica problem](USER_ReadRepl.md "USER_ReadRepl.md").

### Examples

Assume replication fails on an RDS for MySQL read replica.
Running `SHOW REPLICA STATUS\G` on the read replica returns the following
result:

```
*************************** 1. row ***************************
             Replica_IO_State:
                  Source_Host: myhost.XXXXXXXXXXXXXXX.rr-rrrr-1.rds.amazonaws.com
                  Source_User: MasterUser
                  Source_Port: 3306
                Connect_Retry: 10
              Source_Log_File: mysql-bin-changelog.012345
          Read_Source_Log_Pos: 1219393
               Relay_Log_File: relaylog.012340
                Relay_Log_Pos: 30223388
        Relay_Source_Log_File: mysql-bin-changelog.012345
           Replica_IO_Running: No
          Replica_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Source_Log_Pos: 30223232
              Relay_Log_Space: 5248928866
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Source_SSL_Allowed: No
           Source_SSL_CA_File:
           Source_SSL_CA_Path:
              Source_SSL_Cert:
            Source_SSL_Cipher:
               Source_SSL_Key:
        Seconds_Behind_Source: NULL
Source_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 1236
                Last_IO_Error: Got fatal error 1236 from source when reading data from binary log: 'Client requested source to start replication from impossible position; the first event 'mysql-bin-changelog.013406' at 1219393, the last event read from '/rdsdbdata/log/binlog/mysql-bin-changelog.012345' at 4, the last byte read from '/rdsdbdata/log/binlog/mysql-bin-changelog.012345' at 4.'
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Source_Server_Id: 67285976

```

The `Last_IO_Errno` field shows that the instance is receiving I/O
error 1236. The `Source_Log_File` field shows that the file name is
`mysql-bin-changelog.012345`, which means that the log file index is
`12345`. To resolve the error, you can call
`mysql.rds_next_source_log` with the following parameter:

```
CALL mysql.rds_next_source_log(12345);
```

## mysql.rds_reset_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)

Reconfigures an RDS for MySQL DB instance to no longer be a read replica of
an instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_reset_external_master;
```

### Usage notes

The master user must run the `mysql.rds_reset_external_master`
procedure. This procedure must be run on the MySQL DB instance to be removed as a
read replica of a MySQL instance running external to Amazon RDS.

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

For more information about using replication to import data
from an instance of MySQL running external to Amazon RDS, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

## mysql.rds_reset_external_source (RDS for MySQL major versions 8.4 and higher)

Reconfigures an RDS for MySQL DB instance to no longer be a read replica of
an instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_reset_external_source;
```

### Usage notes

The administrative user must run the `mysql.rds_reset_external_source`
procedure. This procedure must be run on the MySQL DB instance to be removed as a
read replica of a MySQL instance running external to Amazon RDS.

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS.

For information about managing replication between Amazon RDS DB instances, see
[Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md"). For more
information about using replication to import data from an instance of MySQL
running external to Amazon RDS, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

## mysql.rds_set_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)

Configures an RDS for MySQL DB instance to be a read replica of an
instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### Note

You can use the [mysql.rds_set_external_master_with_delay (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master_with_delay "#mysql_rds_set_external_master_with_delay") stored procedure to
configure an external source database instance and delayed replication.

### Syntax

```
CALL mysql.rds_set_external_master (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `mysql_binary_log_file_name`
  , `mysql_binary_log_file_location`
  , `ssl_encryption`
);
```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Amazon RDS to become the source database instance.

`host_port`

The port used by the MySQL instance running external to Amazon RDS to be
configured as the source database instance. If your network
configuration includes Secure Shell (SSH) port replication that converts
the port number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Amazon RDS. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`mysql_binary_log_file_name`

The name of the binary log on the source database instance that
contains the replication information.

`mysql_binary_log_file_location`

The location in the `mysql_binary_log_file_name` binary log
at which replication starts reading the replication information.

You can determine the binlog file name and location by running
`SHOW MASTER STATUS` on the source database
instance.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `MASTER_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

### Usage notes

The master user must run the `mysql.rds_set_external_master` procedure.
This procedure must be run on the MySQL DB instance to be configured as the read
replica of a MySQL instance running external to Amazon RDS.

Before you run `mysql.rds_set_external_master`, you must configure the
instance of MySQL running external to Amazon RDS to be a source database instance. To
connect to the MySQL instance running external to Amazon RDS, you must specify
`replication_user_name` and `replication_user_password`
values that indicate a replication user that has `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the external instance of MySQL.

###### To configure an external instance of MySQL as a source database instance

1. Using the MySQL client of your choice, connect to the external instance of
   MySQL and create a user account to be used for replication. The following is
   an example.

**MySQL 5.7**

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY '`password`';
```

**MySQL 8.0**

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED WITH mysql_native_password BY '`password`';
```

###### Note

Specify a password other than the prompt shown here as a security best
practice. 2. On the external instance of MySQL, grant `REPLICATION CLIENT`
and `REPLICATION SLAVE` privileges to your replication user. The
following example grants `REPLICATION CLIENT` and
`REPLICATION SLAVE` privileges on all databases for the
'repl_user' user for your domain.

**MySQL 5.7**

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com' IDENTIFIED BY '`password`';
```

**MySQL 8.0**

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com';
```

To use encrypted replication, configure source database instance to use SSL
connections.

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

After calling `mysql.rds_set_external_master` to configure an Amazon RDS DB
instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_reset_external_master "#mysql_rds_reset_external_master") to remove the read replica
configuration.

When `mysql.rds_set_external_master` is called, Amazon RDS records the time,
user, and an action of `set master` in the `mysql.rds_history`
and `mysql.rds_replication_status` tables.

### Examples

When run on a MySQL DB instance, the following example configures the DB instance
to be a read replica of an instance of MySQL running external to Amazon RDS.

```
call mysql.rds_set_external_master(
  'Externaldb.some.com',
  3306,
  'repl_user',
  '`password`',
  'mysql-bin-changelog.0777',
  120,
  1);

```

## mysql.rds_set_external_source (RDS for MySQL major versions 8.4 and higher)

Configures an RDS for MySQL DB instance to be a read replica of an
instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_source (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `mysql_binary_log_file_name`
  , `mysql_binary_log_file_location`
  , `ssl_encryption`
);
```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Amazon RDS to become the source database instance.

`host_port`

The port used by the MySQL instance running external to Amazon RDS to be
configured as the source database instance. If your network
configuration includes Secure Shell (SSH) port replication that converts
the port number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Amazon RDS. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`mysql_binary_log_file_name`

The name of the binary log on the source database instance that
contains the replication information.

`mysql_binary_log_file_location`

The location in the `mysql_binary_log_file_name` binary log
at which replication starts reading the replication information.

You can determine the binlog file name and location by running
`SHOW MASTER STATUS` on the source database
instance.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

### Usage notes

The administrative user must run the `mysql.rds_set_external_source`
procedure. This procedure must be run on the RDS for MySQL DB
instance to be configured as the read replica of a MySQL instance running external
to Amazon RDS.

Before you run `mysql.rds_set_external_source`, you must configure the
instance of MySQL running external to Amazon RDS to be a source database instance. To
connect to the MySQL instance running external to Amazon RDS, you must specify
`replication_user_name` and `replication_user_password`
values that indicate a replication user that has `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the external instance of
MySQL.

###### To configure an external instance of MySQL as a source database instance

1. Using the MySQL client of your choice, connect to the external instance of
   MySQL and create a user account to be used for replication. The following is
   an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY '`password`';
```

###### Note

Specify a password other than the prompt shown here as a security best
practice. 2. On the external instance of MySQL, grant `REPLICATION CLIENT`
and `REPLICATION SLAVE` privileges to your replication user. The
following example grants `REPLICATION CLIENT` and
`REPLICATION SLAVE` privileges on all databases for the
'repl_user' user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com';
```

To use encrypted replication, configure source database instance to use SSL
connections. Also, import the certificate authority certificate, client certificate,
and client key into the DB instance or DB cluster using the [mysql.rds_import_binlog_ssl_material](url-rds-user.md "url-rds-user.md") procedure.

###### Note

We recommend that you use read replicas to manage
replication between two Amazon RDS DB instances when possible. When you do so, we
recommend that you use only this and other replication-related stored
procedures. These practices enable more complex replication topologies between
Amazon RDS DB instances. We offer these stored procedures primarily to enable
replication with MySQL instances running external to Amazon RDS. For information
about managing replication between Amazon RDS DB instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

After calling `mysql.rds_set_external_source` to configure an RDS for MySQL DB instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_source (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_reset_external_source "#mysql_rds_reset_external_source") to remove the read replica
configuration.

When `mysql.rds_set_external_source` is called, Amazon RDS records the time,
user, and an action of `set master` in the `mysql.rds_history`
and `mysql.rds_replication_status` tables.

### Examples

When run on an RDS for MySQL DB instance, the following example
configures the DB instance to be a read replica of an instance of MySQL running
external to Amazon RDS.

```
call mysql.rds_set_external_source(
  'Externaldb.some.com',
  3306,
  'repl_user',
  '`password`',
  'mysql-bin-changelog.0777',
  120,
  1);

```

## mysql.rds_set_external_master_with_auto_position (RDS for MySQL major versions 8.0 and lower)

Configures an RDS for MySQL DB instance to be a read replica of an instance of MySQL
running external to Amazon RDS. This procedure also configures delayed replication and
replication based on global transaction identifiers (GTIDs).

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_master_with_auto_position (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `ssl_encryption`
  , `delay`
);
```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Amazon RDS to become the source database instance.

`host_port`

The port used by the MySQL instance running external to Amazon RDS to be
configured as the source database instance. If your network
configuration includes Secure Shell (SSH) port replication that converts
the port number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Amazon RDS. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `MASTER_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`delay`

The minimum number of seconds to delay replication from source
database instance.

The limit for this parameter is one day (86,400 seconds).

### Usage notes

The master user must run the
`mysql.rds_set_external_master_with_auto_position` procedure. This
procedure must be run on the MySQL DB instance to be configured as the read replica
of a MySQL instance running external to Amazon RDS.

This procedure is supported for all RDS for MySQL 5.7 versions, and RDS for MySQL 8.0.26
and higher 8.0 versions.

Before you run `mysql.rds_set_external_master_with_auto_position`, you
must configure the instance of MySQL running external to Amazon RDS to be a source
database instance. To connect to the MySQL instance running external to Amazon RDS, you
must specify values for `replication_user_name` and
`replication_user_password`. These values must indicate a replication
user that has `REPLICATION CLIENT` and `REPLICATION SLAVE`
permissions on the external instance of MySQL.

###### To configure an external instance of MySQL as a source database instance

1. Using the MySQL client of your choice, connect to the external instance of
   MySQL and create a user account to be used for replication. The following is
   an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY 'SomePassW0rd'
```

2. On the external instance of MySQL, grant `REPLICATION CLIENT`
   and `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   `'repl_user'` user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com'
IDENTIFIED BY 'SomePassW0rd'
```

For more information, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

Before you call `mysql.rds_set_external_master_with_auto_position`,
make sure to call [mysql.rds_set_external_source_gtid_purged](#mysql_rds_set_external_source_gtid_purged "#mysql_rds_set_external_source_gtid_purged") to set
the `gtid_purged` system variable with a specified GTID range from an
external source.

After calling `mysql.rds_set_external_master_with_auto_position` to
configure an Amazon RDS DB instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_reset_external_master "#mysql_rds_reset_external_master") to remove the read replica
configuration.

When you call `mysql.rds_set_external_master_with_auto_position`, Amazon RDS
records the time, the user, and an action of `set master` in the
`mysql.rds_history` and `mysql.rds_replication_status`
tables.

For disaster recovery, you can use this procedure with the [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") or [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure. To
roll forward changes to a delayed read replica to the time just before a disaster,
you can run the `mysql.rds_set_external_master_with_auto_position`
procedure. After the `mysql.rds_start_replication_until_gtid` procedure
stops replication, you can promote the read replica to be the new primary DB
instance by using the instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

To use the `mysql.rds_rds_start_replication_until_gtid` procedure,
GTID-based replication must be enabled. To skip a specific GTID-based transaction
that is known to cause disaster, you can use the [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For
more information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

### Examples

When run on a MySQL DB instance, the following example configures the DB instance
to be a read replica of an instance of MySQL running external to Amazon RDS. It sets the
minimum replication delay to one hour (3,600 seconds) on the MySQL DB instance. A
change from the MySQL source database instance running external to Amazon RDS isn't
applied on the MySQL DB instance read replica for at least one hour.

```
call mysql.rds_set_external_master_with_auto_position(
  'Externaldb.some.com',
  3306,
  'repl_user',
  'SomePassW0rd',
  1,
  3600);

```

## mysql.rds_set_external_source_with_auto_position (RDS for MySQL major versions 8.4 and higher)

Configures an RDS for MySQL DB instance to be a read replica of an instance of MySQL
running external to Amazon RDS. This procedure also configures delayed replication and
replication based on global transaction identifiers (GTIDs).

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_source_with_auto_position (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `ssl_encryption`
  , `delay`
);
```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Amazon RDS to become the source database instance.

`host_port`

The port used by the MySQL instance running external to Amazon RDS to be
configured as the source database instance. If your network
configuration includes Secure Shell (SSH) port replication that converts
the port number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Amazon RDS. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`delay`

The minimum number of seconds to delay replication from source
database instance.

The limit for this parameter is one day (86,400 seconds).

### Usage notes

The administrative user must run the
`mysql.rds_set_external_source_with_auto_position` procedure. This
procedure must be run on the MySQL DB instance to be configured as the read replica
of a MySQL instance running external to Amazon RDS.

Before you run `mysql.rds_set_external_source_with_auto_position`, you
must configure the instance of MySQL running external to Amazon RDS to be a source
database instance. To connect to the MySQL instance running external to Amazon RDS, you
must specify values for `replication_user_name` and
`replication_user_password`. These values must indicate a replication
user that has `REPLICATION CLIENT` and `REPLICATION SLAVE`
permissions on the external instance of MySQL.

###### To configure an external instance of MySQL as a source database instance

1. Using the MySQL client of your choice, connect to the external instance of
   MySQL and create a user account to be used for replication. The following is
   an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY 'SomePassW0rd'
```

2. On the external instance of MySQL, grant `REPLICATION CLIENT`
   and `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   `'repl_user'` user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com'
IDENTIFIED BY 'SomePassW0rd'
```

For more information, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

Before you call `mysql.rds_set_external_source_with_auto_position`,
make sure to call [mysql.rds_set_external_source_gtid_purged](#mysql_rds_set_external_source_gtid_purged "#mysql_rds_set_external_source_gtid_purged") to set
the `gtid_purged` system variable with a specified GTID range from an
external source.

After calling `mysql.rds_set_external_source_with_auto_position` to
configure an Amazon RDS DB instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_source (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_reset_external_source "#mysql_rds_reset_external_source") to remove the read replica
configuration.

When you call `mysql.rds_set_external_source_with_auto_position`, Amazon RDS
records the time, the user, and an action of `set master` in the
`mysql.rds_history` and `mysql.rds_replication_status`
tables.

For disaster recovery, you can use this procedure with the [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") or [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure. To
roll forward changes to a delayed read replica to the time just before a disaster,
you can run the `mysql.rds_set_external_source_with_auto_position`
procedure. After the `mysql.rds_start_replication_until_gtid` procedure
stops replication, you can promote the read replica to be the new primary DB
instance by using the instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

To use the `mysql.rds_rds_start_replication_until_gtid` procedure,
GTID-based replication must be enabled. To skip a specific GTID-based transaction
that is known to cause disaster, you can use the [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For
more information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

### Examples

When run on a MySQL DB instance, the following example configures the DB instance
to be a read replica of an instance of MySQL running external to Amazon RDS. It sets the
minimum replication delay to one hour (3,600 seconds) on the MySQL DB instance. A
change from the MySQL source database instance running external to Amazon RDS isn't
applied on the MySQL DB instance read replica for at least one hour.

```
call mysql.rds_set_external_source_with_auto_position(
  'Externaldb.some.com',
  3306,
  'repl_user',
  'SomePassW0rd',
  1,
  3600);

```

## mysql.rds_set_external_master_with_delay (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)

Configures an RDS for MySQL DB instance to be a read replica of an instance of MySQL
running external to Amazon RDS and configures delayed replication.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_master_with_delay(
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `mysql_binary_log_file_name`
  , `mysql_binary_log_file_location`
  , `ssl_encryption`
  , `delay`
);
```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Amazon RDS that will become the source database instance.

`host_port`

The port used by the MySQL instance running external to Amazon RDS to be
configured as the source database instance. If your network
configuration includes SSH port replication that converts the port
number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Amazon RDS. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`mysql_binary_log_file_name`

The name of the binary log on the source database instance contains
the replication information.

`mysql_binary_log_file_location`

The location in the `mysql_binary_log_file_name` binary log
at which replication will start reading the replication
information.

You can determine the binlog file name and location by running
`SHOW MASTER STATUS` on the source database
instance.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `MASTER_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`delay`

The minimum number of seconds to delay replication from source
database instance.

The limit for this parameter is one day (86400 seconds).

### Usage notes

The master user must run the
`mysql.rds_set_external_master_with_delay` procedure. This procedure
must be run on the MySQL DB instance to be configured as the read replica of a MySQL
instance running external to Amazon RDS.

Before you run `mysql.rds_set_external_master_with_delay`, you must
configure the instance of MySQL running external to Amazon RDS to be a source database
instance. To connect to the MySQL instance running external to Amazon RDS, you must
specify values for `replication_user_name` and
`replication_user_password`. These values must indicate a replication
user that has `REPLICATION CLIENT` and `REPLICATION SLAVE`
permissions on the external instance of MySQL.

###### To configure an external instance of MySQL as a source database instance

1. Using the MySQL client of your choice, connect to the external instance of
   MySQL and create a user account to be used for replication. The following is
   an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY 'SomePassW0rd'
```

2. On the external instance of MySQL, grant `REPLICATION CLIENT`
   and `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   `'repl_user'` user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com'
IDENTIFIED BY 'SomePassW0rd'
```

For more information, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

After calling `mysql.rds_set_external_master_with_delay` to configure
an Amazon RDS DB instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_reset_external_master "#mysql_rds_reset_external_master") to remove the read replica
configuration.

When you call `mysql.rds_set_external_master_with_delay`, Amazon RDS records
the time, the user, and an action of `set master` in the
`mysql.rds_history` and `mysql.rds_replication_status`
tables.

For disaster recovery, you can use this procedure with the [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") or [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure. To
roll forward changes to a delayed read replica to the time just before a disaster,
you can run the `mysql.rds_set_external_master_with_delay` procedure.
After the `mysql.rds_start_replication_until` procedure stops
replication, you can promote the read replica to be the new primary DB instance by
using the instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

To use the `mysql.rds_rds_start_replication_until_gtid` procedure,
GTID-based replication must be enabled. To skip a specific GTID-based transaction
that is known to cause disaster, you can use the [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For
more information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

The `mysql.rds_set_external_master_with_delay` procedure is available
in these versions of RDS for MySQL:

- MySQL 8.0.26 and higher 8.0 versions
- All 5.7 versions

### Examples

When run on a MySQL DB instance, the following example configures the DB instance
to be a read replica of an instance of MySQL running external to Amazon RDS. It sets the
minimum replication delay to one hour (3,600 seconds) on the MySQL DB instance. A
change from the MySQL source database instance running external to Amazon RDS isn't
applied on the MySQL DB instance read replica for at least one hour.

```
call mysql.rds_set_external_master_with_delay(
  'Externaldb.some.com',
  3306,
  'repl_user',
  'SomePassW0rd',
  'mysql-bin-changelog.000777',
  120,
  1,
  3600);

```

## mysql.rds_set_external_source_with_delay (RDS for MySQL major versions 8.4 and higher)

Configures an RDS for MySQL DB instance to be a read replica of an instance of MySQL
running external to Amazon RDS and configures delayed replication.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_source_with_delay (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `mysql_binary_log_file_name`
  , `mysql_binary_log_file_location`
  , `ssl_encryption`
  , `delay`
);
```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Amazon RDS that will become the source database instance.

`host_port`

The port used by the MySQL instance running external to Amazon RDS to be
configured as the source database instance. If your network
configuration includes SSH port replication that converts the port
number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Amazon RDS. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`mysql_binary_log_file_name`

The name of the binary log on the source database instance contains
the replication information.

`mysql_binary_log_file_location`

The location in the `mysql_binary_log_file_name` binary log
at which replication will start reading the replication
information.

You can determine the binlog file name and location by running
`SHOW MASTER STATUS` on the source database
instance.

`ssl_encryption`

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

`delay`

The minimum number of seconds to delay replication from source
database instance.

The limit for this parameter is one day (86400 seconds).

### Usage notes

The administrative user must run the
`mysql.rds_set_external_source_with_delay` procedure. This procedure
must be run on the MySQL DB instance to be configured as the read replica of a MySQL
instance running external to Amazon RDS.

Before you run `mysql.rds_set_external_source_with_delay`, you must
configure the instance of MySQL running external to Amazon RDS to be a source database
instance. To connect to the MySQL instance running external to Amazon RDS, you must
specify values for `replication_user_name` and
`replication_user_password`. These values must indicate a replication
user that has `REPLICATION CLIENT` and `REPLICATION SLAVE`
permissions on the external instance of MySQL.

###### To configure an external instance of MySQL as a source database instance

1. Using the MySQL client of your choice, connect to the external instance of
   MySQL and create a user account to be used for replication. The following is
   an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY 'SomePassW0rd'
```

2. On the external instance of MySQL, grant `REPLICATION CLIENT`
   and `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   `'repl_user'` user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com'
IDENTIFIED BY 'SomePassW0rd'
```

For more information, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

###### Note

We recommend that you use read replicas to manage replication between two
Amazon RDS DB instances when possible. When you do so, we recommend that you use only
this and other replication-related stored procedures. These practices enable
more complex replication topologies between Amazon RDS DB instances. We offer these
stored procedures primarily to enable replication with MySQL instances running
external to Amazon RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

After calling `mysql.rds_set_external_source_with_delay` to configure
an Amazon RDS DB instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_source (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_reset_external_source "#mysql_rds_reset_external_source") to remove the read replica
configuration.

When you call `mysql.rds_set_external_source_with_delay`, Amazon RDS records
the time, the user, and an action of `set master` in the
`mysql.rds_history` and `mysql.rds_replication_status`
tables.

For disaster recovery, you can use this procedure with the [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") or [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure. To
roll forward changes to a delayed read replica to the time just before a disaster,
you can run the `mysql.rds_set_external_source_with_delay` procedure.
After the `mysql.rds_start_replication_until` procedure stops
replication, you can promote the read replica to be the new primary DB instance by
using the instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

To use the `mysql.rds_rds_start_replication_until_gtid` procedure,
GTID-based replication must be enabled. To skip a specific GTID-based transaction
that is known to cause disaster, you can use the [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For
more information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

### Examples

When run on a MySQL DB instance, the following example configures the DB instance
to be a read replica of an instance of MySQL running external to Amazon RDS. It sets the
minimum replication delay to one hour (3,600 seconds) on the MySQL DB instance. A
change from the MySQL source database instance running external to Amazon RDS isn't
applied on the MySQL DB instance read replica for at least one hour.

```
call mysql.rds_set_external_source_with_delay(
  'Externaldb.some.com',
  3306,
  'repl_user',
  'SomePassW0rd',
  'mysql-bin-changelog.000777',
  120,
  1,
  3600);

```

## mysql.rds_set_external_source_gtid_purged

Sets the [gtid_purged](https://dev.mysql.com/doc/refman/8.0/en/replication-options-gtids.html#sysvar_gtid_purged "https://dev.mysql.com/doc/refman/8.0/en/replication-options-gtids.html#sysvar_gtid_purged") system variable with a specified GTID range from an external
source. The `gtid_purged` value is required for configuring GTID-based
replication to resume the replication using auto positioning.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_set_external_source_gtid_purged(
  `server_uuid`
  , `start_pos`
  , `end_pos`
);
```

### Parameters

`server_uuid`

The universally unique identifier (UUID) of the external server from
which the GTID range is being imported.

`start_pos`

The starting position of the GTID range to be set.

`end_pos`

The ending position of the GTID range to be set.

### Usage notes

The `mysql.rds_set_external_source_gtid_purged` procedure is only
available with MySQL 8.0.37 and higher 8.0 versions.

Call `mysql.rds_set_external_source_gtid_purged` before you call [mysql.rds_set_external_master_with_auto_position (RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master_with_auto_position "#mysql_rds_set_external_master_with_auto_position"), [mysql.rds_set_external_source_with_auto_position (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_external_source_with_auto_position "#mysql_rds_set_external_source_with_auto_position"), or [mysql.rds_set_external_source_with_auto_position_for_channel](mysql-stored-proc-multi-source-replication.md#mysql_rds_set_external_source_with_auto_position_for_channel "mysql-stored-proc-multi-source-replication.md#mysql_rds_set_external_source_with_auto_position_for_channel").

Before you call `mysql.rds_set_external_source_gtid_purged`, make sure
to stop all active replication channels for the database. To check the status of a
channel, use the `SHOW REPLICA STATUS` MySQL statement. To stop
replication on a channel, call [mysql.rds_stop_replication_for_channel](mysql-stored-proc-multi-source-replication.md#mysql_rds_stop_replication_for_channel "mysql-stored-proc-multi-source-replication.md#mysql_rds_stop_replication_for_channel").

The GTID range that you specify must be a superset of the existing
`GTID_PURGED` value. This stored procedure checks the following
values before it sets the `GTID_PURGED` value:

- The `server_uuid` is valid.
- The value of `start_pos` is greater than `0` and
  less than the value of `end_pos`.
- The value of `end_pos` is greater than or equal to the value of
  `start_pos`.

If the GTID set on your external server contains multiple ranges of values,
consider calling the procedure multiple times with different GTID set values.

When you call `mysql.rds_set_external_source_gtid_purged`, Amazon RDS
records the time, the user, and an action of `set gtid_purged` in the
`mysql.rds_history` table.

If you don't set the `gtid_purged` value appropriately for the backup
that you use for replication, this can result in missing or duplicated transactions
during the replication process. Perform the following steps to set the correct
`gtid_purged` value.

###### To set the gtid_purged value on the replica

1. Determine the point in time or the specific backup file to use as the
   starting point for replication. This could be a logical backup (a mysqldump
   file) or a physical backup (an Amazon RDS snapshot).
2. Determine the `gtid_executed` value. This value represents the
   set of all GTIDs that were committed on the server. To retrieve this value,
   on the source instance, do one of the following:
   - Run the SQL statement `SELECT @@GLOBAL.GTID_EXECUTED;`
     at the time the backup was taken.
   - If any related options are included in the respective backup
     utility, extract the value from the backup file. For more
     information, see the [set-gtid-purged](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html#option_mysqldump_set-gtid-purged "https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html#option_mysqldump_set-gtid-purged") option in the MySQL
     documentation.

3. Determine the `gtid_purged` value to use for the call to
   `mysql.rds_set_external_source_gtid_purged`. The
   `gtid_purged` value should include all the GTIDs that were
   executed on the source instance and are no longer needed for replication.
   Therefore, the `gtid_purged` value should be a subset of the
   `gtid_executed` value that you retrieved in the previous
   step.

To determine the `gtid_purged` value, identify the GTIDs that
aren't included in the backup and are no longer needed for replication. You
can do so by analyzing the binary logs or by using a tool such as
mysqlbinlog to find the GTIDs that were purged from the binary logs.

Alternatively, if you have a consistent backup that includes all of the
binary logs up to the backup point, you can set the `gtid_purged`
value to be the same as the `gtid_executed` value at the backup
point. 4. After you determine the appropriate `gtid_purged` value that's
consistent with your backup, call the
`mysql.rds_set_external_source_gtid_purged` stored procedure
on your RDS for MySQL DB instance to set the value.

### Examples

When run on a MySQL DB instance, the following example sets the GTID range from an
external MySQL server with the UUID
`12345678-abcd-1234-efgh-123456789abc`, a starting position of
`1`, and an ending position of `100`. The resulting GTID
value is set to `+12345678-abcd-1234-efgh-123456789abc:1-100`.

```
CALL mysql.rds_set_external_source_gtid_purged('12345678-abcd-1234-efgh-123456789abc', 1, 100);

```

## mysql.rds_set_master_auto_position (RDS for MySQL major versions 8.0 and lower)

Sets the replication mode to be based on either binary log file positions or on global
transaction identifiers (GTIDs).

### Syntax

```
CALL mysql.rds_set_master_auto_position (
`auto_position_mode`
);
```

### Parameters

`auto_position_mode`

A value that indicates whether to use log file position replication or
GTID-based replication:

- `0` – Use the replication method based on
  binary log file position. The default is `0`.
- `1` – Use the GTID-based replication
  method.

### Usage notes

The master user must run the `mysql.rds_set_master_auto_position`
procedure.

This procedure is supported for all RDS for MySQL 5.7 versions
and RDS for MySQL 8.0.26 and higher 8.0 versions.

## mysql.rds_set_source_auto_position (RDS for MySQL major versions 8.4 and higher)

Sets the replication mode to be based on either binary log file positions or on global
transaction identifiers (GTIDs).

### Syntax

```
CALL mysql.rds_set_source_auto_position (`auto_position_mode`);

```

### Parameters

`auto_position_mode`

A value that indicates whether to use log file position replication or
GTID-based replication:

- `0` – Use the replication method based on
  binary log file position. The default is `0`.
- `1` – Use the GTID-based replication method.

### Usage notes

The administrative user must run the
`mysql.rds_set_source_auto_position` procedure.

## mysql.rds_set_source_delay

Sets the minimum number of seconds to delay replication from source database instance
to the current read replica. Use this procedure when you are connected to a read replica
to delay replication from its source database instance.

### Syntax

```
CALL mysql.rds_set_source_delay(
`delay`
);
```

### Parameters

`delay`

The minimum number of seconds to delay replication from the source
database instance.

The limit for this parameter is one day (86400 seconds).

### Usage notes

The master user must run the `mysql.rds_set_source_delay`
procedure.

For disaster recovery, you can use this procedure with the [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") stored procedure or the
[mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure. To
roll forward changes to a delayed read replica to the time just before a disaster,
you can run the `mysql.rds_set_source_delay` procedure. After the
`mysql.rds_start_replication_until` or
`mysql.rds_start_replication_until_gtid` procedure stops replication,
you can promote the read replica to be the new primary DB instance by using the
instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

To use the `mysql.rds_rds_start_replication_until_gtid` procedure,
GTID-based replication must be enabled. To skip a specific GTID-based transaction
that is known to cause disaster, you can use the [mysql.rds_skip_transaction_with_gtid](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For
more information on GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

The `mysql.rds_set_source_delay` procedure is available in these
versions of RDS for MySQL:

- All RDS for MySQL 8.4 versions
- MySQL 8.0.26 and higher 8.0 versions
- All 5.7 versions

### Examples

To delay replication from source database instance to the current read replica for
at least one hour (3,600 seconds), you can call
`mysql.rds_set_source_delay` with the following parameter:

```
CALL mysql.rds_set_source_delay(3600);
```

## mysql.rds_skip_repl_error

Skips and deletes a replication error on a MySQL DB read replica.

### Syntax

```
CALL mysql.rds_skip_repl_error;
```

### Usage notes

The master user must run the `mysql.rds_skip_repl_error` procedure on a
read replica. For more information about this procedure, see [Calling the mysql.rds_skip_repl_error procedure](Appendix.MySQL.CommonDBATasks.md#Appendix.MySQL.CommonDBATasks.SkipError.procedure "Appendix.MySQL.CommonDBATasks.md#Appendix.MySQL.CommonDBATasks.SkipError.procedure").

To determine if there are errors, run the MySQL `SHOW REPLICA STATUS\G`
command. If a replication error isn't critical, you can run
`mysql.rds_skip_repl_error` to skip the error. If there are multiple
errors, `mysql.rds_skip_repl_error` deletes the first error, then warns
that others are present. You can then use `SHOW REPLICA STATUS\G` to
determine the correct course of action for the next error. For information about the
values returned, see [SHOW
REPLICA STATUS statement](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html") in the MySQL documentation.

For more information about addressing replication errors
with Amazon RDS, see [Troubleshooting a MySQL read replica problem](USER_ReadRepl.md "USER_ReadRepl.md").

#### Replication stopped error

When you call the `mysql.rds_skip_repl_error` procedure, you might
receive an error message stating that the replica is down or disabled.

This error message appears if you run the procedure on the primary instance
instead of the read replica. You must run this procedure on the read replica for
the procedure to work.

This error message might also appear if you run the procedure on the read
replica, but replication can't be restarted successfully.

If you need to skip a large number of errors, the replication lag can increase
beyond the default retention period for binary log (binlog) files. In this case,
you might encounter a fatal error because of binlog files being purged before
they have been replayed on the read replica. This purge causes replication to
stop, and you can no longer call the `mysql.rds_skip_repl_error`
command to skip replication errors.

You can mitigate this issue by increasing the number of hours that binlog
files are retained on your source database instance. After you have increased
the binlog retention time, you can restart replication and call the
`mysql.rds_skip_repl_error` command as needed.

To set the binlog retention time, use the [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration") procedure and specify a
configuration parameter of `'binlog retention hours'` along with the
number of hours to retain binlog files on the DB cluster. The following example
sets the retention period for binlog files to 48 hours.

```
CALL mysql.rds_set_configuration('binlog retention hours', 48);
```

## mysql.rds_start_replication

Initiates replication from an RDS for MySQL DB
instance.

###### Note

You can use the [mysql.rds_start_replication_until](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") or [mysql.rds_start_replication_until_gtid](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure to
initiate replication from an RDS for MySQL DB instance
and stop replication at the specified binary log file location.

### Syntax

```
CALL mysql.rds_start_replication;
```

### Usage notes

The master user must run the `mysql.rds_start_replication`
procedure.

To import data from an instance of MySQL external to Amazon RDS, call
`mysql.rds_start_replication` on the read replica to start the
replication process after you call [mysql.rds_set_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master "#mysql_rds_set_external_master") or [mysql.rds_set_external_source (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_external_source "#mysql_rds_set_external_source") to build the replication
configuration. For more information, see [Restoring a backup into an Amazon RDS for MySQL DB instance](MySQL.Procedural.md "MySQL.Procedural.md").

To export data to an instance of MySQL external to Amazon RDS, call
`mysql.rds_start_replication` and
`mysql.rds_stop_replication` on the read replica to control some
replication actions, such as purging binary logs. For more information, see [Exporting data from a MySQL DB instance by using replication](MySQL.Procedural.Exporting.md "MySQL.Procedural.Exporting.md").

You can also call `mysql.rds_start_replication` on the read replica to
restart any replication process that you previously stopped by calling
`mysql.rds_stop_replication`. For more information, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

## mysql.rds_start_replication_until

Initiates replication from an RDS for MySQL DB
instance and stops
replication at the specified binary log file location.

### Syntax

```
CALL mysql.rds_start_replication_until (
`replication_log_file`
  , `replication_stop_point`
);
```

### Parameters

`replication_log_file`

The name of the binary log on the source database instance that
contains the replication information.

`replication_stop_point`

The location in the `replication_log_file` binary log at
which replication will stop.

### Usage notes

The master user must run the `mysql.rds_start_replication_until`
procedure.

The `mysql.rds_start_replication_until` procedure
is available in these versions of RDS for MySQL:

- All RDS for MySQL 8.4 versions
- MySQL 8.0.26 and higher 8.0 versions
- All 5.7 versions

You can use this procedure with delayed replication for
disaster recovery. If you have delayed replication configured, you can use this
procedure to roll forward changes to a delayed read replica to the time just before
a disaster. After this procedure stops replication, you can promote the read replica
to be the new primary DB instance by using the instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

You can configure delayed replication using the following
stored procedures:

- [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration")
- [mysql.rds_set_external_master_with_delay (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](#mysql_rds_set_external_master_with_delay "#mysql_rds_set_external_master_with_delay")
- [mysql.rds_set_external_source_with_delay (RDS for MySQL major versions 8.4 and higher)](#mysql_rds_set_external_source_with_delay "#mysql_rds_set_external_source_with_delay")
- [mysql.rds_set_source_delay](#mysql_rds_set_source_delay "#mysql_rds_set_source_delay")

The file name specified for the `replication_log_file` parameter must
match the source database instance binlog file name.

When the `replication_stop_point` parameter specifies a stop location
that is in the past, replication is stopped immediately.

### Examples

The following example initiates replication and replicates changes until it
reaches location `120` in the `mysql-bin-changelog.000777`
binary log file.

```
call mysql.rds_start_replication_until(
  'mysql-bin-changelog.000777',
  120);

```

## mysql.rds_stop_replication

Stops replication from a MySQL DB instance.

### Syntax

```
CALL mysql.rds_stop_replication;
```

### Usage notes

The master user must run the `mysql.rds_stop_replication` procedure.

If you are configuring replication to import data from an instance of MySQL
running external to Amazon RDS, you call `mysql.rds_stop_replication` on the
read replica to stop the replication process after the import has completed. For
more information, see [Restoring a backup into an Amazon RDS for MySQL DB instance](MySQL.Procedural.md "MySQL.Procedural.md").

If you are configuring replication to export data to an instance of MySQL external
to Amazon RDS, you call `mysql.rds_start_replication` and
`mysql.rds_stop_replication` on the read replica to control some
replication actions, such as purging binary logs. For more information, see [Exporting data from a MySQL DB instance by using replication](MySQL.Procedural.Exporting.md "MySQL.Procedural.Exporting.md").

You can also use `mysql.rds_stop_replication` to
stop replication between two Amazon RDS DB instances. You typically stop replication to
perform a long running operation on the read replica, such as creating a large index
on the read replica. You can restart any replication process that you stopped by
calling [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica. For more
information, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").
