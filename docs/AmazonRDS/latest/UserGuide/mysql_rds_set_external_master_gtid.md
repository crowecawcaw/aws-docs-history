# mysql.rds_set_external_master_gtid

Configures GTID-based replication from a MariaDB instance running external to Amazon RDS
to a MariaDB DB instance. This stored procedure is supported only where the
external MariaDB instance is version 10.0.24 or higher. When setting up replication
where one or both instances do not support MariaDB global transaction identifiers
(GTIDs), use [mysql.rds_set_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](mysql-stored-proc-replicating.md#mysql_rds_set_external_master "mysql-stored-proc-replicating.md#mysql_rds_set_external_master").

Using GTIDs for replication provides crash-safety features not offered by binary log
replication, so we recommend it in cases where the replicating instances support it.

## Syntax

```
CALL mysql.rds_set_external_master_gtid(
  *host\_name*
  , *host\_port*
  , *replication\_user\_name*
  , *replication\_user\_password*
  , *gtid*
  , *ssl\_encryption*
);
```

## Parameters

_host_name_

String. The host name or IP address of the MariaDB instance running
external to Amazon RDS that will become the source instance.

_host_port_

Integer. The port used by the MariaDB instance running external to
Amazon RDS to be configured as the source instance. If your network
configuration includes SSH port replication that converts the port
number, specify the port number that is exposed by SSH.

_replication_user_name_

String. The ID of a user with `REPLICATION SLAVE` permissions in the
MariaDB DB instance to be configured as the read replica.

_replication_user_password_

String. The password of the user ID specified in
`replication_user_name`.

_gtid_

String. The global transaction ID on the source instance that replication
should start from.

You can use `@@gtid_current_pos` to get the current GTID if
the source instance has been locked while you are configuring
replication, so the binary log doesn't change between the points when
you get the GTID and when replication starts.

Otherwise, if you are using `mysqldump` version 10.0.13 or
greater to populate the replica instance prior to starting replication,
you can get the GTID position in the output by using the
`--master-data` or `--dump-slave` options. If
you are not using `mysqldump` version 10.0.13 or greater, you
can run the `SHOW MASTER STATUS` or use those same
`mysqldump` options to get the binary log file name and
position, then convert them to a GTID by running
`BINLOG_GTID_POS` on the external MariaDB
instance:

```
SELECT BINLOG_GTID_POS('<binary log file name>', <binary log file position>);
```

For more information about the MariaDB implementation of GTIDs, go to
[Global transaction ID](http://mariadb.com/kb/en/mariadb/global-transaction-id/ "http://mariadb.com/kb/en/mariadb/global-transaction-id/") in the MariaDB documentation.

_ssl_encryption_

A value that specifies whether Secure Socket Layer (SSL) encryption is
used on the replication connection. 1 specifies to use SSL encryption, 0
specifies to not use encryption. The default is 0.

###### Note

The `MASTER_SSL_VERIFY_SERVER_CERT` option isn't supported.
This option is set to 0, which means that the connection is encrypted, but the
certificates aren't verified.

## Usage notes

The `mysql.rds_set_external_master_gtid` procedure must be run by the
master user. It must be run on the MariaDB DB instance that you are configuring as
the replica of a MariaDB instance running external to Amazon RDS. Before
running `mysql.rds_set_external_master_gtid`, you must have configured
the instance of MariaDB running external to Amazon RDS as a source instance. For more
information, see [Importing data into an Amazon RDS for MariaDB DB instance](MariaDB.Procedural.md "MariaDB.Procedural.md").

###### Warning

Do not use `mysql.rds_set_external_master_gtid` to manage replication between two
Amazon RDS DB instances. Use it only when replicating with a MariaDB instance running
external to RDS. For information about managing replication between Amazon RDS DB
instances, see [Working with DB instance read replicas](USER_ReadRepl.md "USER_ReadRepl.md").

After calling `mysql.rds_set_external_master_gtid` to configure an
Amazon RDS DB instance as a read replica, you can call [mysql.rds_start_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication "mysql-stored-proc-replicating.md#mysql_rds_start_replication") on the replica to start the
replication process. You can call [mysql.rds_reset_external_master (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](mysql-stored-proc-replicating.md#mysql_rds_reset_external_master "mysql-stored-proc-replicating.md#mysql_rds_reset_external_master") to remove the read replica
configuration.

When `mysql.rds_set_external_master_gtid` is called, Amazon RDS records the
time, user, and an action of "set master" in the `mysql.rds_history` and
`mysql.rds_replication_status` tables.

## Examples

When run on a MariaDB DB instance, the following example configures it as the
replica of an instance of MariaDB running external to Amazon RDS.

```
call mysql.rds_set_external_master_gtid ('Sourcedb.some.com',3306,'ReplicationUser','SomePassW0rd','0-123-456',0);
```
