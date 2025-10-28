# Replicating transactions using GTIDs

The following stored procedures control how transactions are replicated
using global transaction identifiers (GTIDs) with Aurora MySQL. To learn how to use
replication based on GTIDs with Aurora MySQL, see [Using GTID-based replication](mysql-replication-gtid.md "mysql-replication-gtid.md").

###### Topics

- [mysql.rds_assign_gtids_to_anonymous_transactions (Aurora MySQL version 3)](#mysql_assign_gtids_to_anonymous_transactions "#mysql_assign_gtids_to_anonymous_transactions")
- [mysql.rds_gtid_purged (Aurora MySQL version 3)](#mysql_rds_gtid_purged "#mysql_rds_gtid_purged")
- [mysql.rds_skip_transaction_with_gtid (Aurora MySQL
  version 2 and 3)](#mysql_rds_skip_transaction_with_gtid "#mysql_rds_skip_transaction_with_gtid")
- [mysql.rds_start_replication_until_gtid (Aurora MySQL
  version 3)](#mysql_rds_start_replication_until_gtid "#mysql_rds_start_replication_until_gtid")

## mysql.rds_assign_gtids_to_anonymous_transactions (Aurora MySQL version 3)

Configures the `ASSIGN_GTIDS_TO_ANONYMOUS_TRANSACTIONS` option of the
`CHANGE REPLICATION SOURCE TO` statement. It makes the replication
channel assign a GTID to replicated transactions that don't have one. That way, you can
perform binary log replication from a source that doesn't use GTID-based replication to
a replica that does. For more information, see [CHANGE REPLICATION SOURCE TO Statement](https://dev.mysql.com/doc/refman/8.0/en/change-replication-source-to.html "https://dev.mysql.com/doc/refman/8.0/en/change-replication-source-to.html") and [Replication From a Source Without GTIDs to a Replica With GTIDs](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-assign-anon.html "https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-assign-anon.html") in the
_MySQL Reference Manual_.

### Syntax

```
CALL mysql.rds_assign_gtids_to_anonymous_transactions(`gtid_option`);

```

### Parameters

`gtid_option`

String value. The allowed values are `OFF`,
`LOCAL`, or a specified UUID.

### Usage

notes

This procedure has the same effect as issuing the statement `CHANGE
 REPLICATION SOURCE TO ASSIGN_GTIDS_TO_ANONYMOUS_TRANSACTIONS =
 `gtid_option`` in community MySQL.

GTID must be turned to `ON` for `gtid_option`
to be set to `LOCAL` or a specific UUID.

The default is `OFF`, meaning that the feature isn't used.

`LOCAL` assigns a GTID including the replica's own UUID (the
`server_uuid` setting).

Passing a parameter that is a UUID assigns a GTID that includes the specified
UUID, such as the `server_uuid` setting for the replication source
server.

### Examples

To turn off this feature:

````
mysql> call mysql.rds_assign_gtids_to_anonymous_transactions('OFF');
+-------------------------------------------------------------+
| Message  | +-------------------------------------------------------------+
| ASSIGN_GTIDS_TO_ANONYMOUS_TRANSACTIONS has been set to: OFF | +-------------------------------------------------------------+ 1 row in set (0.07 sec) ``` To use the replica's own UUID: ``` mysql> call mysql.rds_assign_gtids_to_anonymous_transactions('LOCAL'); +---------------------------------------------------------------+
| Message  | +---------------------------------------------------------------+
| ASSIGN_GTIDS_TO_ANONYMOUS_TRANSACTIONS has been set to: LOCAL | +---------------------------------------------------------------+ 1 row in set (0.07 sec) ``` To use a specified UUID: ``` mysql> call mysql.rds_assign_gtids_to_anonymous_transactions('317a4760-f3dd-3b74-8e45-0615ed29de0e'); +----------------------------------------------------------------------------------------------+
| Message | +----------------------------------------------------------------------------------------------+
| ASSIGN_GTIDS_TO_ANONYMOUS_TRANSACTIONS has been set to: 317a4760-f3dd-3b74-8e45-0615ed29de0e | +----------------------------------------------------------------------------------------------+ 1 row in set (0.07 sec) ``` ## mysql.rds\_gtid\_purged (Aurora MySQL version 3) Sets the global value of the system variable `gtid_purged` to a given global transaction identifier (GTID) set. The `gtid_purged` system variable is a GTID set that consists of the GTIDs of all transactions that have been committed on the server, but don't exist in any binary log file on the server. To allow compatibility with MySQL 8.0, there are two ways to set the value of `gtid_purged`: <br>• Replace the value of `gtid_purged` with your specified GTID set. <br>• Append your specified GTID set to the GTID set that `gtid_purged` already contains. ### Syntax To replace the value of `gtid_purged` with your specified GTID set: ``` CALL mysql.rds_gtid_purged (`gtid_set`); ``` To append the value of `gtid_purged` to your specified GTID set: ``` CALL mysql.rds_gtid_purged (+`gtid_set`); ``` ### Parameters `gtid_set` The value of `gtid_set` must be a superset of the current value of `gtid_purged`, and can't intersect with `gtid_subtract(gtid_executed,gtid_purged)`. That is, the new GTID set must include any GTIDs that were already in `gtid_purged`, and can't include any GTIDs in `gtid_executed` that haven't yet been purged. The `gtid_set` parameter also can't include any GTIDs that are in the global `gtid_owned` set, the GTIDs for transactions that are currently being processed on the server. ### Usage notes The master user must run the `mysql.rds_gtid_purged` procedure. This procedure is supported for Aurora MySQL version 3.04 and higher. ### Examples The following example assigns the GTID `3E11FA47-71CA-11E1-9E33-C80AA9429562:23` to the `gtid_purged` global variable. ``` CALL mysql.rds_gtid_purged('3E11FA47-71CA-11E1-9E33-C80AA9429562:23'); ``` ## mysql.rds\_skip\_transaction\_with\_gtid (Aurora MySQL version 2 and 3) Skips replication of a transaction with the specified global transaction identifier (GTID) on an Aurora primary instance. You can use this procedure for disaster recovery when a specific GTID transaction is known to cause a problem. Use this stored procedure to skip the problematic transaction. Examples of problematic transactions include transactions that disable replication, delete important data, or cause the DB instance to become unavailable. ### Syntax ``` CALL mysql.rds_skip_transaction_with_gtid ( `gtid_to_skip` ); ``` ### Parameters `gtid_to_skip` The GTID of the replication transaction to skip. ### Usage notes The master user must run the `mysql.rds_skip_transaction_with_gtid` procedure. This procedure is supported for Aurora MySQL version 2 and 3. ### Examples The following example skips replication of the transaction with the GTID `3E11FA47-71CA-11E1-9E33-C80AA9429562:23`. ``` CALL mysql.rds_skip_transaction_with_gtid('3E11FA47-71CA-11E1-9E33-C80AA9429562:23'); ``` ## mysql.rds\_start\_replication\_until\_gtid (Aurora MySQL version 3) Initiates replication from an Aurora MySQL DB cluster and stops replication immediately after the specified global transaction identifier (GTID). ### Syntax ``` CALL mysql.rds_start_replication_until_gtid(`gtid`); ``` ### Parameters `gtid` The GTID after which replication is to stop. ### Usage notes The master user must run the `mysql.rds_start_replication_until_gtid` procedure. This procedure is supported for Aurora MySQL version 3.04 and higher. The `mysql.rds_start_replication_until_gtid` stored procedure isn't supported for managed replication, which includes the following: <br>• [Replicating Amazon Aurora MySQL DB clusters across AWS Regions](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md") <br>• [Migrating data from an RDS for MySQL DB instance to an Amazon Aurora MySQL DB cluster by using an Aurora read replica](AuroraMySQL.Migrating.RDSMySQL.md "AuroraMySQL.Migrating.RDSMySQL.md") When the `gtid` parameter specifies a transaction that has already been run by the replica, replication is stopped immediately. ### Examples The following example initiates replication and replicates changes until it reaches GTID `3E11FA47-71CA-11E1-9E33-C80AA9429562:23`. ``` call mysql.rds_start_replication_until_gtid('3E11FA47-71CA-11E1-9E33-C80AA9429562:23'); ```
````
