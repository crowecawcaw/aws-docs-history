# Using GTID-based replication

The following content explains how to use global transaction identifiers (GTIDs) with
binary log (binlog) replication
between an Aurora MySQL cluster and an external source.

###### Note

For Aurora, you can use this feature only with Aurora MySQL clusters that use binlog
replication to or from an external MySQL database. The other database might be an Amazon RDS
MySQL instance, an on-premises MySQL database, or an Aurora DB cluster in a different
AWS Region. To learn how to configure that kind of replication, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

If you use binlog replication and aren't familiar with GTID-based replication with MySQL,
see [Replication
with global transaction identifiers](https://dev.mysql.com/doc/refman/5.7/en/replication-gtids.html "https://dev.mysql.com/doc/refman/5.7/en/replication-gtids.html") in the MySQL documentation.

GTID-based replication is supported for Aurora MySQL version 2 and 3.

###### Topics

- [Overview of global transaction identifiers (GTIDs)](#mysql-replication-gtid.overview "#mysql-replication-gtid.overview")
- [Parameters for GTID-based replication](#mysql-replication-gtid.parameters "#mysql-replication-gtid.parameters")
- [Enabling GTID-based replication for an Aurora MySQL cluster](mysql-replication-gtid.md "mysql-replication-gtid.md")
- [Disabling GTID-based replication for
  an Aurora MySQL DB
  cluster](mysql-replication-gtid.md "mysql-replication-gtid.md")

## Overview of global transaction identifiers (GTIDs)

_Global transaction identifiers (GTIDs)_ are unique
identifiers generated for committed MySQL transactions. You can use GTIDs to make binlog
replication simpler and easier to troubleshoot.

###### Note

When Aurora synchronizes data among the DB instances in a cluster, that replication
mechanism doesn't involve the binary log (binlog). For Aurora MySQL,
GTID-based replication only applies when you also use binlog replication to
replicate into or out of an Aurora MySQL DB cluster from an external MySQL-compatible
database.

MySQL uses two different types of transactions for binlog replication:

- _GTID transactions_ – Transactions that are identified by a GTID.
- _Anonymous transactions_ – Transactions that
  don't have a GTID assigned.

In a replication configuration, GTIDs are unique across all DB instances. GTIDs simplify
replication configuration because when you use them, you don't have to refer to log
file positions. GTIDs also make it easier to track replicated transactions and determine
whether the source instance and replicas are consistent.

You typically use GTID-based replication with Aurora when replicating from an external MySQL-compatible database
into an Aurora cluster. You can set up this replication configuration as part of a migration from an on-premises or
Amazon RDS database into Aurora MySQL. If the external database already uses GTIDs, enabling GTID-based replication for the
Aurora cluster simplifies the replication process.

You configure GTID-based replication for an Aurora MySQL cluster by
first setting the relevant configuration parameters in a DB cluster parameter group. You
then associate that parameter group with the cluster.

## Parameters for GTID-based replication

Use the following parameters to configure GTID-based replication.

| Parameter                  | Valid values                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `gtid_mode`                | `OFF`, `OFF_PERMISSIVE`,<br>`ON_PERMISSIVE`, `ON` | `OFF` specifies that new transactions are anonymous<br>transactions (that is, don't have GTIDs), and a transaction<br>must be anonymous to be replicated.<br>`OFF_PERMISSIVE` specifies that new transactions<br>are anonymous transactions, but all transactions can be<br>replicated.<br>`ON_PERMISSIVE` specifies that new transactions are<br>GTID transactions, but all transactions can be replicated.<br>`ON` specifies that new transactions are GTID<br>transactions, and a transaction must be a GTID transaction to be<br>replicated. |
| `enforce_gtid_consistency` | `OFF`, `ON`, `WARN`                               | `OFF` allows transactions to violate GTID<br>consistency.<br>`ON` prevents transactions from violating GTID<br>consistency.<br>`WARN` allows transactions to violate GTID<br>consistency but generates a warning when a violation occurs.                                                                                                                                                                                                                                                                                                        |

###### Note

In the AWS Management Console, the `gtid_mode` parameter appears as `gtid-mode`.

For GTID-based replication, use these settings for the DB cluster
parameter group for your Aurora MySQL DB cluster:

- `ON` and `ON_PERMISSIVE` apply only to outgoing replication
  from an Aurora MySQL cluster. Both of these values cause your Aurora DB cluster to
  use GTIDs for transactions that are replicated to an external database.
  `ON` requires that the external database also use GTID-based
  replication. `ON_PERMISSIVE` makes GTID-based replication optional on
  the external database.
- `OFF_PERMISSIVE`, if set, means that your Aurora DB
  cluster can accept incoming replication from an external database. It can do
  this whether the external database uses GTID-based replication or not.
- `OFF`, if set, means that your Aurora DB cluster
  only accepts incoming replication from external databases that don't use
  GTID-based replication.

###### Tip

Incoming replication is the most common binlog replication scenario for Aurora MySQL
clusters. For incoming replication, we recommend that you set the GTID mode to
`OFF_PERMISSIVE`. That setting allows incoming replication from
external databases regardless of the GTID settings at the replication source.

For more information about parameter groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
