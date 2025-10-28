# Configuring, starting, and stopping binary

log (binlog) replication

You can call the following stored procedures while connected to the
primary instance in an Aurora MySQL cluster. These procedures control how transactions are
replicated from an external database into Aurora MySQL, or from Aurora MySQL to an external
database.

###### Topics

- [mysql.rds_disable_session_binlog
  (Aurora MySQL version 2)](#mysql_rds_disable_session_binlog "#mysql_rds_disable_session_binlog")
- [mysql.rds_enable_session_binlog
  (Aurora MySQL version 2)](#mysql_rds_enable_session_binlog "#mysql_rds_enable_session_binlog")
- [mysql.rds_import_binlog_ssl_material](#mysql_rds_import_binlog_ssl_material "#mysql_rds_import_binlog_ssl_material")
- [mysql.rds_next_master_log (Aurora MySQL version 2)](#mysql_rds_next_master_log "#mysql_rds_next_master_log")
- [mysql.rds_next_source_log (Aurora MySQL version 3)](#mysql_rds_next_source_log "#mysql_rds_next_source_log")
- [mysql.rds_remove_binlog_ssl_material](#mysql_rds_remove_binlog_ssl_material "#mysql_rds_remove_binlog_ssl_material")
- [mysql.rds_reset_external_master
  (Aurora MySQL version 2)](#mysql_rds_reset_external_master "#mysql_rds_reset_external_master")
- [mysql.rds_reset_external_source
  (Aurora MySQL version 3)](#mysql_rds_reset_external_source "#mysql_rds_reset_external_source")
- [mysql.rds_set_binlog_source_ssl
  (Aurora MySQL version 3)](#mysql_rds_set_binlog_source_ssl "#mysql_rds_set_binlog_source_ssl")
- [mysql.rds_set_external_master (Aurora MySQL version 2)](#mysql_rds_set_external_master "#mysql_rds_set_external_master")
- [mysql.rds_set_external_source (Aurora MySQL version 3)](#mysql_rds_set_external_source "#mysql_rds_set_external_source")
- [mysql.rds_set_external_master_with_auto_position (Aurora MySQL version 2)](#mysql_rds_set_external_master_with_auto_position "#mysql_rds_set_external_master_with_auto_position")
- [mysql.rds_set_external_source_with_auto_position (Aurora MySQL version 3)](#mysql_rds_set_external_source_with_auto_position "#mysql_rds_set_external_source_with_auto_position")
- [mysql.rds_set_master_auto_position
  (Aurora MySQL version 2)](#mysql_rds_set_master_auto_position "#mysql_rds_set_master_auto_position")
- [mysql.rds_set_read_only (Aurora MySQL version 3)](#mysql_rds_set_read_only "#mysql_rds_set_read_only")
- [mysql.rds_set_session_binlog_format (Aurora MySQL version 2)](#mysql_rds_set_session_binlog_format "#mysql_rds_set_session_binlog_format")
- [mysql.rds_set_source_auto_position
  (Aurora MySQL version 3)](#mysql_rds_set_source_auto_position "#mysql_rds_set_source_auto_position")
- [mysql.rds_skip_repl_error](#mysql_rds_skip_repl_error "#mysql_rds_skip_repl_error")
- [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication")
- [mysql.rds_start_replication_until (Aurora MySQL
  version 3)](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until")
- [mysql.rds_stop_replication](#mysql_rds_stop_replication "#mysql_rds_stop_replication")

## mysql.rds_disable_session_binlog

(Aurora MySQL version 2)

Turns off binary logging for the current session by setting the
`sql_log_bin` variable to `OFF`.

### Syntax

```
CALL mysql.rds_disable_session_binlog;
```

### Parameters

None

### Usage notes

For an Aurora MySQL DB cluster, you call this stored procedure while connected to
the primary instance.

For Aurora, this procedure is supported for Aurora MySQL version 2.12 and higher
MySQL 5.7–compatible versions.

###### Note

In Aurora MySQL version 3, you can use the following command to disable binary
logging for the current session if you have the
`SESSION_VARIABLES_ADMIN` privilege:

```
SET SESSION sql_log_bin = OFF;
```

## mysql.rds_enable_session_binlog

(Aurora MySQL version 2)

Turns on binary logging for the current session by setting the
`sql_log_bin` variable to `ON`.

### Syntax

```
CALL mysql.rds_enable_session_binlog;
```

### Parameters

None

### Usage notes

For an Aurora MySQL DB cluster, you call this stored procedure while connected to
the primary instance.

For Aurora, this procedure is supported for Aurora MySQL version 2.12 and higher
MySQL 5.7–compatible versions.

###### Note

In Aurora MySQL version 3, you can use the following command to enable binary
logging for the current session if you have the
`SESSION_VARIABLES_ADMIN` privilege:

```
SET SESSION sql_log_bin = ON;
```

## mysql.rds_import_binlog_ssl_material

Imports the certificate authority certificate, client certificate, and client key into
an Aurora MySQL DB cluster. The information is required for
SSL communication and encrypted replication.

###### Note

Currently, this procedure is supported for Aurora MySQL version 2: 2.09.2, 2.10.0,
2.10.1, and 2.11.0; and version 3: 3.01.1 and higher.

### Syntax

```
CALL mysql.rds_import_binlog_ssl_material (
  `ssl_material`
);
```

### Parameters

`ssl_material`

JSON payload that contains the contents of the following .pem format
files for a MySQL client:

- "ssl_ca":"`Certificate authority
certificate`"
- "ssl_cert":"`Client
certificate`"
- "ssl_key":"`Client key`"

### Usage

notes

Prepare for encrypted replication before you run this procedure:

- If you don't have SSL enabled on the external MySQL source database
  instance and don't have a client key and client certificate prepared,
  enable SSL on the MySQL database server and generate the required client key
  and client certificate.
- If SSL is enabled on the external source database instance, supply a
  client key and certificate for the Aurora MySQL DB cluster. If you don't
  have these, generate a new key and certificate for the Aurora MySQL DB
  cluster. To sign the client certificate, you must have the certificate
  authority key you used to configure SSL on the external MySQL source
  database instance.

For more information, see [Creating SSL certificates and keys using openssl](https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-files-using-openssl.html "https://dev.mysql.com/doc/refman/8.0/en/creating-ssl-files-using-openssl.html") in the MySQL
documentation.

###### Important

After you prepare for encrypted replication, use an SSL connection to run this
procedure. The client key must not be transferred across an insecure connection.

This procedure imports SSL information from an external MySQL
database into an Aurora MySQL DB cluster. The SSL information is in .pem format files
that contain the SSL information for the Aurora MySQL DB cluster. During encrypted
replication, the Aurora MySQL DB cluster acts a client to the MySQL database server.
The certificates and keys for the Aurora MySQL client are in files in .pem
format.

You can copy the information from these files into the
`ssl_material` parameter in the correct JSON payload. To support
encrypted replication, import this SSL information into the Aurora MySQL DB
cluster.

The JSON payload must be in the following format.

```

'{"ssl_ca":"-----BEGIN CERTIFICATE-----
`ssl_ca_pem_body_code`
-----END CERTIFICATE-----\n","ssl_cert":"-----BEGIN CERTIFICATE-----
`ssl_cert_pem_body_code`
-----END CERTIFICATE-----\n","ssl_key":"-----BEGIN RSA PRIVATE KEY-----
`ssl_key_pem_body_code`
-----END RSA PRIVATE KEY-----\n"}'

```

### Examples

The following example imports SSL information into an Aurora MySQL. In .pem format files, the body code typically is longer
than the body code shown in the example.

```
call mysql.rds_import_binlog_ssl_material(
'{"ssl_ca":"-----BEGIN CERTIFICATE-----
AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6V
hz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXr
lsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZ
qaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3Rb
BQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
-----END CERTIFICATE-----\n","ssl_cert":"-----BEGIN CERTIFICATE-----
AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6V
hz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXr
lsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZ
qaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3Rb
BQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
-----END CERTIFICATE-----\n","ssl_key":"-----BEGIN RSA PRIVATE KEY-----
AAAAB3NzaC1yc2EAAAADAQABAAABAQClKsfkNkuSevGj3eYhCe53pcjqP3maAhDFcvBS7O6V
hz2ItxCih+PnDSUaw+WNQn/mZphTk/a/gU8jEzoOWbkM4yxyb/wB96xbiFveSFJuOp/d6RJhJOI0iBXr
lsLnBItntckiJ7FbtxJMXLvvwJryDUilBMTjYtwB+QhYXUMOzce5Pjz5/i8SeJtjnV3iAoG/cQk+0FzZ
qaeJAAHco+CY/5WrUBkrHmFJr6HcXkvJdWPkYQS3xqC0+FmUZofz221CBt5IMucxXPkX4rWi+z7wB3Rb
BQoQzd8v7yeb7OzlPnWOyN0qFU0XA246RA8QFYiCNYwI3f05p6KLxEXAMPLE
-----END RSA PRIVATE KEY-----\n"}');

```

## mysql.rds_next_master_log (Aurora MySQL version

2.

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
binary log on disk before the failover event occurred.

### Examples

Assume replication fails on an Aurora MySQL read replica.
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

## mysql.rds_next_source_log (Aurora MySQL version 3)

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
`1`, even though this might reduce performance.

### Examples

Assume replication fails on an Aurora MySQL read replica.
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

## mysql.rds_remove_binlog_ssl_material

Removes the certificate authority certificate, client certificate, and client key for
SSL communication and encrypted replication. This information is imported by using [mysql.rds_import_binlog_ssl_material](#mysql_rds_import_binlog_ssl_material "#mysql_rds_import_binlog_ssl_material").

### Syntax

```
CALL mysql.rds_remove_binlog_ssl_material;
```

## mysql.rds_reset_external_master

(Aurora MySQL version 2)

Reconfigures an Aurora MySQL DB instance to no longer be a read replica of
an instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_reset_external_master;
```

### Usage notes

The master user must run the `mysql.rds_reset_external_master`
procedure. This procedure must be run on the MySQL DB instance to be removed as a
read replica of a MySQL instance running external to Amazon RDS.

###### Note

We offer these stored procedures primarily to enable replication with MySQL
instances running external to Amazon RDS. We recommend that you use Aurora Replicas to
manage replication within an Aurora MySQL DB cluster when possible. For
information about managing replication in Aurora MySQL DB clusters, see [Using Aurora Replicas](AuroraMySQL.md#AuroraMySQL.Replication.Replicas "AuroraMySQL.md#AuroraMySQL.Replication.Replicas").

For more information about using replication to import data
from an instance of MySQL running external to Aurora MySQL, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

## mysql.rds_reset_external_source

(Aurora MySQL version 3)

Reconfigures an Aurora MySQL DB instance to no longer be a read replica of
an instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Syntax

```
CALL mysql.rds_reset_external_source;
```

### Usage notes

The administrative user must run the `mysql.rds_reset_external_source`
procedure. This procedure must be run on the MySQL DB instance to be removed as a
read replica of a MySQL instance running external to Amazon RDS.

###### Note

We offer these stored procedures primarily to enable replication with MySQL
instances running external to Amazon RDS. We recommend that you use Aurora Replicas to
manage replication within an Aurora MySQL DB cluster when possible. For
information about managing replication in Aurora MySQL DB clusters, see [Using Aurora Replicas](AuroraMySQL.md#AuroraMySQL.Replication.Replicas "AuroraMySQL.md#AuroraMySQL.Replication.Replicas").

## mysql.rds_set_binlog_source_ssl

(Aurora MySQL version 3)

Enables `SOURCE_SSL` encryption for binlog replication. For more
information, see [CHANGE REPLICATION SOURCE TO statement](https://dev.mysql.com/doc/refman/8.0/en/change-replication-source-to.html "https://dev.mysql.com/doc/refman/8.0/en/change-replication-source-to.html") in the MySQL documentation.

### Syntax

```
CALL mysql.rds_set_binlog_source_ssl(`mode`);
```

### Parameters

`mode`

A value that indicates whether `SOURCE_SSL` encryption is
enabled:

- `0` – `SOURCE_SSL` encryption is
  disabled. The default is `0`.
- `1` – `SOURCE_SSL` encryption is
  enabled. You can configure encryption using SSL or TLS.

### Usage notes

This procedure is supported for Aurora MySQL version 3.06 and
higher.

## mysql.rds_set_external_master (Aurora MySQL version

2.

Configures an Aurora MySQL DB instance to be a read replica of an
instance of MySQL running external to Amazon RDS.

The `mysql.rds_set_external_master` procedure is
deprecated and will be removed in a future release. Use `mysql.rds_set_external_source` instead.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

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

###### To configure an external instance of MySQL as a source database

instance

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
connections. Also, import the certificate authority
certificate, client certificate, and client key into the DB instance or DB
cluster using the [mysql.rds_import_binlog_ssl_material](#mysql_rds_import_binlog_ssl_material "#mysql_rds_import_binlog_ssl_material")
procedure.

###### Note

We offer these stored procedures primarily to enable replication with MySQL
instances running external to Amazon RDS. We recommend that you use Aurora Replicas to
manage replication within an Aurora MySQL DB cluster when possible. For
information about managing replication in Aurora MySQL DB clusters, see [Using Aurora Replicas](AuroraMySQL.md#AuroraMySQL.Replication.Replicas "AuroraMySQL.md#AuroraMySQL.Replication.Replicas").

After calling `mysql.rds_set_external_master` to configure an Amazon RDS DB
instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_master
(Aurora MySQL version 2)](#mysql_rds_reset_external_master "#mysql_rds_reset_external_master") to remove the read replica
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

## mysql.rds_set_external_source (Aurora MySQL version 3)

Configures an Aurora MySQL DB instance to be a read replica of an
instance of MySQL running external to Amazon RDS.

###### Important

To run this procedure, `autocommit` must be enabled. To enable it, set
the `autocommit` parameter to `1`. For information about
modifying parameters, see [Modifying parameters in a DB parameter group
in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

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

You must have imported a custom SSL certificate
using [mysql.rds_import_binlog_ssl_material](#mysql_rds_import_binlog_ssl_material "#mysql_rds_import_binlog_ssl_material") to enable
this option. If you haven't imported an custom SSL certificate, then
set this parameter to 0 and use [mysql.rds_set_binlog_source_ssl
(Aurora MySQL version 3)](#mysql_rds_set_binlog_source_ssl "#mysql_rds_set_binlog_source_ssl") to enable SSL
for binary log replication.

The `SOURCE_SSL_VERIFY_SERVER_CERT` option isn't
supported. This option is set to 0, which means that the connection
is encrypted, but the certificates aren't verified.

### Usage notes

The administrative user must run the `mysql.rds_set_external_source`
procedure. This procedure must be run on the Aurora MySQL DB
instance to be configured as the read replica of a MySQL instance running external
to Amazon RDS.

Before you run `mysql.rds_set_external_source`, you must configure the
instance of MySQL running external to Amazon RDS to be a source database instance. To
connect to the MySQL instance running external to Amazon RDS, you must specify
`replication_user_name` and `replication_user_password`
values that indicate a replication user that has `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the external instance of
MySQL.

###### To configure an external instance of MySQL as a source database

instance

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

We offer these stored procedures primarily to enable
replication with MySQL instances running external to Amazon RDS. We recommend that
you use Aurora Replicas to manage replication within an Aurora MySQL DB cluster
when possible. For information about managing replication in Aurora MySQL DB
clusters, see [Using Aurora Replicas](AuroraMySQL.md#AuroraMySQL.Replication.Replicas "AuroraMySQL.md#AuroraMySQL.Replication.Replicas").

After calling `mysql.rds_set_external_source` to configure an Aurora MySQL DB instance as a read replica, you can call [mysql.rds_start_replication](#mysql_rds_start_replication "#mysql_rds_start_replication") on the read replica to start the
replication process. You can call [mysql.rds_reset_external_source
(Aurora MySQL version 3)](#mysql_rds_reset_external_source "#mysql_rds_reset_external_source") to remove the read replica
configuration.

When `mysql.rds_set_external_source` is called, Amazon RDS records the time,
user, and an action of `set master` in the `mysql.rds_history`
and `mysql.rds_replication_status` tables.

### Examples

When run on an Aurora MySQL DB instance, the following example
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

## mysql.rds_set_external_master_with_auto_position (Aurora MySQL version 2)

Configures an Aurora MySQL primary instance to accept incoming replication from an
external MySQL instance. This procedure also configures replication based on global
transaction identifiers (GTIDs).

This procedure doesn't configure delayed replication, because Aurora MySQL
doesn't support delayed replication.

### Syntax

```
CALL mysql.rds_set_external_master_with_auto_position (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `ssl_encryption`
);

```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to
Aurora to become the replication source.

`host_port`

The port used by the MySQL instance running external to Aurora to be
configured as the replication source. If your network configuration
includes Secure Shell (SSH) port replication that converts the port
number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and
`REPLICATION SLAVE` permissions on the MySQL instance
running external to Aurora. We recommend that you provide an account that
is used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in
`replication_user_name`.

`ssl_encryption`

This option isn't currently implemented. The default is 0.

### Usage

notes

For an Aurora MySQL DB cluster, you call this stored procedure while connected to
the primary instance.

The master user must run the
`mysql.rds_set_external_master_with_auto_position` procedure. The
master user runs this procedure on the primary instance of an Aurora MySQL DB cluster
that acts as a replication target. This can be the replication target of an external
MySQL DB instance or an Aurora MySQL DB cluster.

This procedure is supported for Aurora MySQL version 2. For Aurora MySQL version 3,
use the procedure [mysql.rds_set_external_source_with_auto_position (Aurora MySQL version 3)](#mysql_rds_set_external_source_with_auto_position "#mysql_rds_set_external_source_with_auto_position")
instead.

Before you run `mysql.rds_set_external_master_with_auto_position`,
configure the external MySQL DB instance to be a replication source. To connect to
the external MySQL instance, specify values for `replication_user_name`
and `replication_user_password`. These values must indicate a replication
user that has `REPLICATION CLIENT` and `REPLICATION SLAVE`
permissions on the external MySQL instance.

###### To configure an external MySQL instance as a replication source

1. Using the MySQL client of your choice, connect to the external MySQL
   instance and create a user account to be used for replication. The following
   is an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY 'SomePassW0rd'

```

2. On the external MySQL instance, grant `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges to your replication user. The
   following example grants `REPLICATION CLIENT` and
   `REPLICATION SLAVE` privileges on all databases for the
   `'repl_user'` user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com'
IDENTIFIED BY 'SomePassW0rd'

```

When you call `mysql.rds_set_external_master_with_auto_position`, Amazon RDS
records certain information. This information is the time, the user, and an action
of `"set master"` in the `mysql.rds_history` and
`mysql.rds_replication_status` tables.

To skip a specific GTID-based transaction that is known to cause a problem, you
can use the [mysql.rds_skip_transaction_with_gtid (Aurora MySQL
version 2 and 3)](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For
more information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

### Examples

When run on an Aurora primary instance, the following example configures the Aurora
cluster to act as a read replica of an instance of MySQL running external to Aurora.

```
call mysql.rds_set_external_master_with_auto_position(
  'Externaldb.some.com',
  3306,
  'repl_user'@'mydomain.com',
  'SomePassW0rd');

```

## mysql.rds_set_external_source_with_auto_position (Aurora MySQL version 3)

Configures an Aurora MySQL primary instance to accept incoming replication from an external MySQL instance. This procedure also
configures replication based on global transaction identifiers (GTIDs).

### Syntax

```
CALL mysql.rds_set_external_source_with_auto_position (
  `host_name`
  , `host_port`
  , `replication_user_name`
  , `replication_user_password`
  , `ssl_encryption`
);

```

### Parameters

`host_name`

The host name or IP address of the MySQL instance running external to Aurora to become the
replication source.

`host_port`

The port used by the MySQL instance running external to Aurora to be configured as the replication
source. If your network configuration includes Secure Shell (SSH) port replication that converts the
port number, specify the port number that is exposed by SSH.

`replication_user_name`

The ID of a user with `REPLICATION CLIENT` and `REPLICATION SLAVE` permissions
on the MySQL instance running external to Aurora. We recommend that you provide an account that is
used solely for replication with the external instance.

`replication_user_password`

The password of the user ID specified in `replication_user_name`.

`ssl_encryption`

This option isn't currently implemented. The default is 0.

###### Note

Use [mysql.rds_set_binlog_source_ssl
(Aurora MySQL version 3)](#mysql_rds_set_binlog_source_ssl "#mysql_rds_set_binlog_source_ssl") to
enable SSL for binary log replication.

### Usage notes

For an Aurora MySQL DB cluster, you call this stored procedure while connected to the primary instance.

The administrative user must run the `mysql.rds_set_external_source_with_auto_position`
procedure. The administrative user runs this procedure on the primary instance of an Aurora MySQL DB cluster
that acts as a replication target. This can be the replication target of an external MySQL DB instance or
an Aurora MySQL DB cluster.

This procedure is supported for Aurora MySQL version 3. This procedure doesn't configure delayed replication, because
Aurora MySQL doesn't support delayed replication.

Before you run `mysql.rds_set_external_source_with_auto_position`, configure the external MySQL
DB instance to be a replication source. To connect to the external MySQL instance, specify values for
`replication_user_name` and `replication_user_password`. These values must indicate
a replication user that has `REPLICATION CLIENT` and `REPLICATION SLAVE` permissions
on the external MySQL instance.

###### To configure an external MySQL instance as a replication source

1. Using the MySQL client of your choice, connect to the external MySQL instance and create a user
   account to be used for replication. The following is an example.

```
CREATE USER 'repl_user'@'mydomain.com' IDENTIFIED BY 'SomePassW0rd'

```

2. On the external MySQL instance, grant `REPLICATION CLIENT` and `REPLICATION
SLAVE` privileges to your replication user. The following example grants `REPLICATION
CLIENT` and `REPLICATION SLAVE` privileges on all databases for the
   `'repl_user'` user for your domain.

```
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'mydomain.com'
IDENTIFIED BY 'SomePassW0rd'

```

When you call `mysql.rds_set_external_source_with_auto_position`, Amazon RDS records certain
information. This information is the time, the user, and an action of `"set master"` in the
`mysql.rds_history` and `mysql.rds_replication_status` tables.

To skip a specific GTID-based transaction that is known to cause a problem, you can
use the [mysql.rds_skip_transaction_with_gtid (Aurora MySQL
version 2 and 3)](mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid "mysql-stored-proc-gtid.md#mysql_rds_skip_transaction_with_gtid") stored procedure. For more
information about working with GTID-based replication, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

### Examples

When run on an Aurora primary instance, the following example configures the Aurora cluster to act as a read
replica of an instance of MySQL running external to Aurora.

```
call mysql.rds_set_external_source_with_auto_position(
  'Externaldb.some.com',
  3306,
  'repl_user'@'mydomain.com',
  'SomePassW0rd');

```

## mysql.rds_set_master_auto_position

(Aurora MySQL version 2)

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

This procedure is supported for Aurora MySQL version 2.

## mysql.rds_set_read_only (Aurora MySQL version

3.

Turns `read_only` mode on or off globally for the DB instance.

### Syntax

```
CALL mysql.rds_set_read_only(`mode`);
```

### Parameters

`mode`

A value that indicates whether `read_only` mode is on or
off globally for the DB instance:

- `0` – `OFF`. The default is
  `0`.
- `1` – `ON`

### Usage notes

The `mysql.rds_set_read_only` stored procedure modifies only the
`read_only` parameter. The `innodb_read_only` parameter
can't be changed on reader DB instances.

The `read_only` parameter change doesn't persist on rebooting. To make
permanent changes to `read_only`, you must use the `read_only`
DB cluster parameter.

This procedure is supported for Aurora MySQL version 3.06 and
higher.

## mysql.rds_set_session_binlog_format (Aurora MySQL version 2)

Sets the binary log format for the current session.

### Syntax

```
CALL mysql.rds_set_session_binlog_format(`format`);
```

### Parameters

`format`

A value that indicates the binary log format for the current
session:

- `STATEMENT` – The replication source writes
  events to the binary log based on SQL statements.
- `ROW` – The replication source writes events
  to the binary log that indicate changes to individual table
  rows.
- `MIXED` – Logging is generally based on SQL
  statements, but switches to rows under certain conditions. For
  more information, see [Mixed Binary Logging Format](https://dev.mysql.com/doc/refman/8.0/en/binary-log-mixed.html "https://dev.mysql.com/doc/refman/8.0/en/binary-log-mixed.html") in the MySQL
  documentation.

### Usage notes

For an Aurora MySQL DB cluster, you call this stored procedure while connected to
the primary instance.

To use this stored procedure, you must have binary logging configured for the
current session.

For Aurora, this procedure is supported for Aurora MySQL version 2.12 and higher
MySQL 5.7–compatible versions.

## mysql.rds_set_source_auto_position

(Aurora MySQL version 3)

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

For an Aurora MySQL DB cluster, you call this stored procedure
while connected to the primary instance.

The administrative user must run the
`mysql.rds_set_source_auto_position` procedure.

## mysql.rds_skip_repl_error

Skips and deletes a replication error on a MySQL DB read replica.

### Syntax

```
CALL mysql.rds_skip_repl_error;
```

### Usage notes

The master user must run the `mysql.rds_skip_repl_error` procedure on a
read replica. For more information about this procedure, see [Skipping the current replication
error](../UserGuide/Appendix.MySQL.md#Appendix.MySQL.CommonDBATasks.SkipError "../UserGuide/Appendix.MySQL.md#Appendix.MySQL.CommonDBATasks.SkipError").

To determine if there are errors, run the MySQL `SHOW REPLICA STATUS\G`
command. If a replication error isn't critical, you can run
`mysql.rds_skip_repl_error` to skip the error. If there are multiple
errors, `mysql.rds_skip_repl_error` deletes the first error, then warns
that others are present. You can then use `SHOW REPLICA STATUS\G` to
determine the correct course of action for the next error. For information about the
values returned, see [SHOW
REPLICA STATUS statement](https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html "https://dev.mysql.com/doc/refman/8.0/en/show-replica-status.html") in the MySQL documentation.

For more information about addressing replication errors with
Aurora MySQL, see [Diagnosing and resolving a
MySQL read replication
failure](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.RR "CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.RR").

#### Replication stopped

error

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

Initiates replication from an Aurora MySQL DB cluster.

###### Note

You can use the [mysql.rds_start_replication_until (Aurora MySQL
version 3)](#mysql_rds_start_replication_until "#mysql_rds_start_replication_until") or [mysql.rds_start_replication_until_gtid (Aurora MySQL
version 3)](mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid "mysql-stored-proc-gtid.md#mysql_rds_start_replication_until_gtid") stored procedure to
initiate replication from an Aurora MySQL DB instance
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
replication process after you call [mysql.rds_set_external_master (Aurora MySQL version 2)](#mysql_rds_set_external_master "#mysql_rds_set_external_master") or [mysql.rds_set_external_source (Aurora MySQL version 3)](#mysql_rds_set_external_source "#mysql_rds_set_external_source") to build the replication
configuration. For more information, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

To export data to an instance of MySQL external to Amazon RDS, call
`mysql.rds_start_replication` and
`mysql.rds_stop_replication` on the read replica to control some
replication actions, such as purging binary logs. For more information, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

You can also call `mysql.rds_start_replication` on the read replica to
restart any replication process that you previously stopped by calling
`mysql.rds_stop_replication`. For more information, see [Replication stopped
error](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicationStopped "CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicationStopped").

## mysql.rds_start_replication_until (Aurora MySQL

version 3)

Initiates replication from an Aurora MySQL DB cluster and stops
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

This procedure is supported for Aurora MySQL version 3.04 and
higher.

The `mysql.rds_start_replication_until` stored
procedure isn't supported for managed replication, which includes the
following:

- [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md")
- [Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL
  DB cluster by using an Aurora read replica](AuroraMySQL.Migrating.RDSMySQL.md "AuroraMySQL.Migrating.RDSMySQL.md")

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
more information, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

If you are configuring replication to export data to an instance of MySQL external
to Amazon RDS, you call `mysql.rds_start_replication` and
`mysql.rds_stop_replication` on the read replica to control some
replication actions, such as purging binary logs. For more information, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

The `mysql.rds_stop_replication` stored procedure
isn't supported for managed replication, which includes the following:

- [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md")
- [Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL
  DB cluster by using an Aurora read replica](AuroraMySQL.Migrating.RDSMySQL.md "AuroraMySQL.Migrating.RDSMySQL.md")
