# Replicating transactions using GTIDs

The following stored procedures control how transactions are
replicated using global transaction identifiers (GTIDs) with RDS for MySQL. For more
information about replication based on GTIDs with RDS for MySQL, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

When using stored procedures to manage replication with a
replication user configured with `caching_sha2_password`, you must configure TLS
by specifying `SOURCE_SSL=1`. `caching_sha2_password` is the default
authentication plugin for RDS for MySQL 8.4.

###### Topics

- [mysql.rds_skip_transaction_with_gtid](#mysql_rds_skip_transaction_with_gtid "#mysql_rds_skip_transaction_with_gtid")
- [mysql.rds_start_replication_until_gtid](#mysql_rds_start_replication_until_gtid "#mysql_rds_start_replication_until_gtid")

## mysql.rds_skip_transaction_with_gtid

Skips replication of a transaction with the specified global
transaction identifier (GTID) on a MySQL DB instance.

You can use this procedure for disaster recovery when a specific GTID transaction is
known to cause a problem. Use this stored procedure to skip the problematic transaction.
Examples of problematic transactions include transactions that disable replication,
delete important data, or cause the DB instance to become unavailable.

### Syntax

```
CALL mysql.rds_skip_transaction_with_gtid (
`gtid_to_skip`
);
```

### Parameters

`gtid_to_skip`

The GTID of the replication transaction to skip.

### Usage notes

The master user must run the `mysql.rds_skip_transaction_with_gtid`
procedure.

This procedure is supported for all RDS for MySQL 5.7 versions,
all RDS for MySQL 8.0 versions, and all RDS for MySQL 8.4 versions.

### Examples

The following example skips replication of the transaction with the GTID
`3E11FA47-71CA-11E1-9E33-C80AA9429562:23`.

```
CALL mysql.rds_skip_transaction_with_gtid('3E11FA47-71CA-11E1-9E33-C80AA9429562:23');

```

## mysql.rds_start_replication_until_gtid

Initiates replication from an RDS for MySQL DB
instance and stops
replication immediately after the specified global transaction identifier (GTID).

### Syntax

```
CALL mysql.rds_start_replication_until_gtid(`gtid`);
```

### Parameters

`gtid`

The GTID after which replication is to stop.

### Usage notes

The master user must run the `mysql.rds_start_replication_until_gtid`
procedure.

This procedure is supported for all RDS for MySQL 5.7 versions,
all RDS for MySQL 8.0 versions, and all RDS for MySQL 8.4 versions.

You can use this procedure with delayed replication for
disaster recovery. If you have delayed replication configured, you can use this
procedure to roll forward changes to a delayed read replica to the time just before
a disaster. After this procedure stops replication, you can promote the read replica
to be the new primary DB instance by using the instructions in [Promoting a read replica to be a standalone DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

You can configure delayed replication using the following
stored procedures:

- [mysql.rds_set_configuration](mysql-stored-proc-configuring.md#mysql_rds_set_configuration "mysql-stored-proc-configuring.md#mysql_rds_set_configuration")
- [mysql.rds_set_external_master_with_delay (RDS for MariaDB and RDS for MySQL major versions 8.0 and lower)](mysql-stored-proc-replicating.md#mysql_rds_set_external_master_with_delay "mysql-stored-proc-replicating.md#mysql_rds_set_external_master_with_delay")
- [mysql.rds_set_external_source_with_delay (RDS for MySQL major versions 8.4 and higher)](mysql-stored-proc-replicating.md#mysql_rds_set_external_source_with_delay "mysql-stored-proc-replicating.md#mysql_rds_set_external_source_with_delay")
- [mysql.rds_set_source_delay](mysql-stored-proc-replicating.md#mysql_rds_set_source_delay "mysql-stored-proc-replicating.md#mysql_rds_set_source_delay")

When the `gtid` parameter specifies a transaction that has already been
run by the replica, replication is stopped immediately.

### Examples

The following example initiates replication and replicates changes until it
reaches GTID `3E11FA47-71CA-11E1-9E33-C80AA9429562:23`.

```
call mysql.rds_start_replication_until_gtid('3E11FA47-71CA-11E1-9E33-C80AA9429562:23');

```
