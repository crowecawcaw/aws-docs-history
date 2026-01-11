# Using GTID-based replication

The following content explains how to use global transaction identifiers (GTIDs) with
binary log (binlog) replication among Amazon RDS for MySQL DB
instances.

If you use binlog replication and aren't familiar with GTID-based replication with MySQL,
see [Replication
with global transaction identifiers](https://dev.mysql.com/doc/refman/5.7/en/replication-gtids.html "https://dev.mysql.com/doc/refman/5.7/en/replication-gtids.html") in the MySQL documentation.

GTID-based replication is supported for the following
versions:

- All RDS for MySQL 8.4 versions
- All RDS for MySQL 8.0 versions
- All RDS for MySQL 5.7 versions
  All MySQL DB instances in a replication configuration must meet this
  version requirement.

###### Topics

- [Overview of global transaction identifiers (GTIDs)](#mysql-replication-gtid.overview "#mysql-replication-gtid.overview")
- [Parameters for GTID-based replication](#mysql-replication-gtid.parameters "#mysql-replication-gtid.parameters")
- [Enabling
  GTID-based replication for new read replicas for RDS for MySQL](mysql-replication-gtid.md "mysql-replication-gtid.md")
- [Enabling
  GTID-based replication for existing read replicas for RDS for MySQL](mysql-replication-gtid.md "mysql-replication-gtid.md")
- [Disabling GTID-based replication for
  a MySQL DB instance with read
  replicas](mysql-replication-gtid.md "mysql-replication-gtid.md")

## Overview of global transaction identifiers (GTIDs)

_Global transaction identifiers (GTIDs)_ are unique
identifiers generated for committed MySQL transactions. You can use GTIDs to make binlog
replication simpler and easier to troubleshoot.

MySQL uses two different types of transactions for binlog replication:

- _GTID transactions_ – Transactions that are identified by a GTID.
- _Anonymous transactions_ – Transactions that
  don't have a GTID assigned.

In a replication configuration, GTIDs are unique across all DB instances. GTIDs simplify
replication configuration because when you use them, you don't have to refer to log
file positions. GTIDs also make it easier to track replicated transactions and determine
whether the source instance and replicas are consistent.

You can use GTID-based replication to replicate data with RDS for MySQL
read replicas. You can configure GTID-based replication when you are creating new read replicas, or you can
convert existing read replicas to use GTID-based replication.

You can also use GTID-based replication in a delayed replication configuration with RDS for MySQL. For more information,
see [Configuring delayed replication with MySQL](USER_MySQL.Replication.ReadReplicas.md "USER_MySQL.Replication.ReadReplicas.md").

## Parameters for GTID-based replication

Use the following parameters to configure GTID-based replication.

| Parameter                  | Valid values                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `gtid_mode`                | `OFF`, `OFF_PERMISSIVE`,<br>`ON_PERMISSIVE`, `ON` | `OFF` specifies that new transactions are anonymous<br>transactions (that is, don't have GTIDs), and a transaction<br>must be anonymous to be replicated.<br>`OFF_PERMISSIVE` specifies that new transactions<br>are anonymous transactions, but all transactions can be<br>replicated.<br>`ON_PERMISSIVE` specifies that new transactions are<br>GTID transactions, but all transactions can be replicated.<br>`ON` specifies that new transactions are GTID<br>transactions, and a transaction must be a GTID transaction to be<br>replicated. |
| `enforce_gtid_consistency` | `OFF`, `ON`, `WARN`                               | `OFF` allows transactions to violate GTID<br>consistency.<br>`ON` prevents transactions from violating GTID<br>consistency.<br>`WARN` allows transactions to violate GTID<br>consistency but generates a warning when a violation occurs.                                                                                                                                                                                                                                                                                                        |

###### Note

In the AWS Management Console, the `gtid_mode` parameter appears as `gtid-mode`.

For GTID-based replication, use these settings for the parameter
group for your DB instance or read replica:

- `ON` and `ON_PERMISSIVE` apply only to outgoing replication
  from an RDS DB instance. Both of these values cause your RDS DB instance to
  use GTIDs for transactions that are replicated. `ON` requires that
  the target database also use GTID-based replication. `ON_PERMISSIVE`
  makes GTID-based replication optional on the target database.
- `OFF_PERMISSIVE`, if set, means that your RDS DB instances can accept
  incoming replication from a source database. They can do this regardless of
  whether the source database uses GTID-based replication.
- `OFF`, if set, means that your RDS DB instance only accepts incoming replication
  from source databases that don't use GTID-based replication.

For more information about parameter groups, see [Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
