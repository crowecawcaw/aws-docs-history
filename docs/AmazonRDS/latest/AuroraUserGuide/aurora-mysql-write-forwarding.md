# Using local write forwarding in an Amazon Aurora MySQL DB cluster

_Local (in-cluster) write forwarding_ allows your applications to issue read/write transactions directly on an
Aurora Replica. These transactions are then forwarded to the writer DB instance to be committed. You can use local write forwarding
when your applications require _read-after-write consistency_, which is the ability to read the latest write in a
transaction.

Read replicas receive updates asynchronously from the writer. Without write forwarding, you have to transact any reads that
require read-after-write consistency on the writer DB instance. Or you have to develop complex custom application logic to take
advantage of multiple read replicas for scalability. Your applications must fully split all read and write traffic, maintaining two
sets of database connections to send the traffic to the correct endpoint. This development overhead complicates application design
when the queries are part of a single logical session, or transaction, within the application. Moreover, because replication lag can
differ among read replicas, it's difficult to achieve global read consistency across all instances in the database.

Write forwarding avoids the need to split those transactions or send them exclusively to the writer, which simplifies application
development. This new capability makes it easy to achieve read scale for workloads that need to read the latest write in a
transaction and aren't sensitive to write latency.

Local write forwarding is different from global write forwarding, which forwards writes from a secondary
DB cluster to the primary DB cluster in an Aurora global database. You can use local write forwarding in a DB cluster that is part of an Aurora global
database. For more information, see [Using write forwarding in an Amazon Aurora global database](aurora-global-database-write-forwarding.md "aurora-global-database-write-forwarding.md").

Local write forwarding requires Aurora MySQL version 3.04 or higher.

###### Topics

- [Enabling local write forwarding](aurora-mysql-write-forwarding-enabling.md "aurora-mysql-write-forwarding-enabling.md")
- [Checking if a DB cluster has write forwarding enabled](#aurora-mysql-write-forwarding-describing "#aurora-mysql-write-forwarding-describing")
- [Application and SQL compatibility with write forwarding](#aurora-mysql-write-forwarding-compatibility "#aurora-mysql-write-forwarding-compatibility")
- [Isolation levels for write forwarding](#aurora-mysql-write-forwarding-isolation "#aurora-mysql-write-forwarding-isolation")
- [Read consistency for write forwarding](aurora-mysql-write-forwarding-consistency.md "aurora-mysql-write-forwarding-consistency.md")
- [Running multipart statements with write forwarding](#aurora-mysql-write-forwarding-multipart "#aurora-mysql-write-forwarding-multipart")
- [Transactions with write forwarding](#aurora-mysql-write-forwarding-txns "#aurora-mysql-write-forwarding-txns")
- [Configuration parameters for write forwarding](#aurora-mysql-write-forwarding-params "#aurora-mysql-write-forwarding-params")
- [Amazon CloudWatch metrics and Aurora MySQL status variables for write
  forwarding](aurora-mysql-write-forwarding-cloudwatch.md "aurora-mysql-write-forwarding-cloudwatch.md")
- [Identifying forwarded transactions and queries](#aurora-write-forwarding-processlist "#aurora-write-forwarding-processlist")

## Checking if a DB cluster has write forwarding enabled

To determine that you can use write forwarding in a DB cluster, confirm that the cluster has the attribute
`LocalWriteForwardingStatus` set to `enabled`.

In the AWS Management Console, on the **Configuration** tab of the details page for the cluster, you see the status
**Enabled** for **Local read replica write forwarding**.

To see the status of the write forwarding setting for all of your clusters, run the following AWS CLI command.

```
aws rds describe-db-clusters \
--query '*[].{DBClusterIdentifier:DBClusterIdentifier,LocalWriteForwardingStatus:LocalWriteForwardingStatus}'

[
    {
        "LocalWriteForwardingStatus": "enabled",
        "DBClusterIdentifier": "write-forwarding-test-cluster-1"
    },
    {
        "LocalWriteForwardingStatus": "disabled",
        "DBClusterIdentifier": "write-forwarding-test-cluster-2"
    },
    {
        "LocalWriteForwardingStatus": "requested",
        "DBClusterIdentifier": "test-global-cluster-2"
    },
    {
        "LocalWriteForwardingStatus": "null",
        "DBClusterIdentifier": "aurora-mysql-v2-cluster"
    }
]
```

A DB cluster can have the following values for `LocalWriteForwardingStatus`:

- `disabled` – Write forwarding is disabled.
- `disabling` – Write forwarding is in the process of being disabled.
- `enabled` – Write forwarding is enabled.
- `enabling` – Write forwarding is in the process of being enabled.
- `null` – Write forwarding isn't available for this DB cluster.
- `requested` – Write forwarding has been requested, but is not yet active.

## Application and SQL compatibility with write forwarding

You can use the following kinds of SQL statements with write forwarding:

- Data manipulation language (DML) statements, such as `INSERT`, `DELETE`, and
  `UPDATE`. There are some restrictions on the properties of these statements that you can use with write
  forwarding, as described following.
- `SELECT ... LOCK IN SHARE MODE` and `SELECT FOR UPDATE` statements.
- `PREPARE` and `EXECUTE` statements.

Certain statements aren't allowed or can produce stale results when you use them in a
DB cluster with write forwarding. In addition, user defined functions and user defined
procedures aren't supported. Thus, the `EnableLocalWriteForwarding` setting
is disabled by default for DB clusters. Before enabling it, check to make sure that your
application code isn't affected by any of these restrictions.

The following restrictions apply to the SQL statements you use with write forwarding. In some cases, you can use the statements on
DB clusters with write forwarding enabled. This approach works if write forwarding isn't enabled within the session by the
`aurora_replica_read_consistency` configuration parameter. If you try to use a statement when it's not
allowed because of write forwarding, then you will see an error message similar to the following:

```
ERROR 1235 (42000): This version of MySQL doesn't yet support '`operation` with write forwarding'.

```

**Data definition language (DDL)**

Connect to the writer DB instance to run DDL statements. You can't run them from reader DB instances.

**Updating a permanent table using data from a temporary table**

You can use temporary tables on DB clusters with write forwarding enabled. However, you can't use a DML statement to
modify a permanent table if the statement refers to a temporary table. For example, you can't use an
`INSERT ... SELECT` statement that takes the data from a temporary table.

**XA transactions**

You can't use the following statements on a DB cluster when write forwarding is enabled within the session. You can use
these statements on DB clusters that don't have write forwarding enabled, or within sessions where the
`aurora_replica_read_consistency` setting is empty. Before enabling write forwarding within a
session, check if your code uses these statements.

```
XA {START|BEGIN} xid [JOIN|RESUME]
XA END xid [SUSPEND [FOR MIGRATE]]
XA PREPARE xid
XA COMMIT xid [ONE PHASE]
XA ROLLBACK xid
XA RECOVER [CONVERT XID]

```

**LOAD statements for permanent tables**

You can't use the following statements on a DB cluster with write forwarding enabled.

```
LOAD DATA INFILE 'data.txt' INTO TABLE t1;
LOAD XML LOCAL INFILE 'test.xml' INTO TABLE t1;

```

**Plugin statements**

You can't use the following statements on a DB cluster with write forwarding enabled.

```
INSTALL PLUGIN example SONAME 'ha_example.so';
UNINSTALL PLUGIN example;

```

**SAVEPOINT statements**

You can't use the following statements on a DB cluster when write forwarding is enabled within the session. You can use
these statements on DB clusters that don't have write forwarding enabled, or within sessions where the
`aurora_replica_read_consistency` setting is blank. Check if your code uses these statements before
enabling write forwarding within a session.

```
SAVEPOINT t1_save;
ROLLBACK TO SAVEPOINT t1_save;
RELEASE SAVEPOINT t1_save;

```

## Isolation levels for write forwarding

In sessions that use write forwarding, you can only use the `REPEATABLE READ` isolation level. Although you can
also use the `READ COMMITTED` isolation level with Aurora Replicas, that isolation level doesn't work with write
forwarding. For information about the `REPEATABLE READ` and `READ COMMITTED` isolation levels, see [Aurora MySQL isolation levels](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md").

## Running multipart statements with write forwarding

A DML statement might consist of multiple parts, such as an `INSERT ... SELECT` statement or a `DELETE ...
 WHERE` statement. In this case, the entire statement is forwarded to the writer DB instance and run there.

## Transactions with write forwarding

If the transaction access mode is set to read only, write forwarding isn't used. You can specify the access mode for the
transaction by using the `SET TRANSACTION` statement or the `START TRANSACTION` statement. You can also
specify the transaction access mode by changing the value of the [transaction_read_only](https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_transaction_read_only "https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html#sysvar_transaction_read_only") session variable. You can change this session value only while you're connected to a DB
cluster that has write forwarding enabled.

If a long-running transaction doesn't issue any statement for a substantial period of time, it might exceed the idle timeout
period. This period has a default of one minute. You can set the `aurora_fwd_writer_idle_timeout` parameter to
increase it up to one day. A transaction that exceeds the idle timeout is canceled by the writer instance. The next subsequent
statement you submit receives a timeout error. Then Aurora rolls back the transaction.

This type of error can occur in other cases when write forwarding becomes unavailable. For example, Aurora cancels any transactions
that use write forwarding if you restart the DB cluster or if you disable write forwarding.

When a writer instance in a cluster using local write forwarding is restarted, any
active, forwarded transactions and queries on reader instances using local write forwarding
are automatically closed. After the writer instance is available again, you can retry these
transactions.

## Configuration parameters for write forwarding

The Aurora DB parameter groups include settings for the write forwarding feature. Details about these parameters are summarized in
the following table, with usage notes after the table.

| Parameter                               | Scope               | Type                  | Default value | Valid values                    |
| --------------------------------------- | ------------------- | --------------------- | ------------- | ------------------------------- |
| `aurora_fwd_writer_idle_timeout`        | Cluster             | Unsigned integer      | 60            | 1–86,400                        |
| `aurora_fwd_writer_max_connections_pct` | Cluster             | Unsigned long integer | 10            | 0–90                            |
| `aurora_replica_read_consistency`       | Cluster or instance | Enum                  | '' (null)     | `EVENTUAL`, `SESSION`, `GLOBAL` |

To control incoming write requests, use these settings:

- `aurora_fwd_writer_idle_timeout` – The number of seconds the writer DB instance waits for activity on a
  connection that's forwarded from a reader instance before closing it. If the session remains idle beyond this
  period, Aurora cancels the session.
- `aurora_fwd_writer_max_connections_pct` – The upper limit on database connections that can be used on a
  writer DB instance to handle queries forwarded from reader instances. It's expressed as a percentage of the
  `max_connections` setting for the writer. For example, if `max_connections` is 800 and
  `aurora_fwd_master_max_connections_pct` or `aurora_fwd_writer_max_connections_pct` is 10, then
  the writer allows a maximum of 80 simultaneous forwarded sessions. These connections come from the same connection pool
  managed by the `max_connections` setting.

This setting applies only on the writer when it has write forwarding enabled. If you decrease the value, existing connections
aren't affected. Aurora takes the new value of the setting into account when attempting to create a new connection
from a DB cluster. The default value is 10, representing 10% of the `max_connections` value.

###### Note

Because `aurora_fwd_writer_idle_timeout` and `aurora_fwd_writer_max_connections_pct` are DB cluster
parameters, all DB instances in each cluster have the same values for these parameters.

For more information about `aurora_replica_read_consistency`, see [Read consistency for write forwarding](aurora-mysql-write-forwarding-consistency.md "aurora-mysql-write-forwarding-consistency.md").

For more information on DB parameter groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

## Identifying forwarded transactions and queries

You can use the `information_schema.aurora_forwarding_processlist` table to identify forwarded transactions and
queries. For more information on this table, see [information_schema.aurora_forwarding_processlist](AuroraMySQL.Reference.md#AuroraMySQL.Reference.ISTables.aurora_forwarding_processlist "AuroraMySQL.Reference.md#AuroraMySQL.Reference.ISTables.aurora_forwarding_processlist").

The following example shows all forwarded connections on a writer DB instance.

```
mysql> select * from information_schema.AURORA_FORWARDING_PROCESSLIST where IS_FORWARDED=1 order by REPLICA_SESSION_ID;

+-----+----------+--------------------+----------+---------+------+--------------+--------------------------------------------+--------------+--------------------+---------------------------------+----------------------+----------------+
| ID  | USER     | HOST               | DB       | COMMAND | TIME | STATE        | INFO                                       | IS_FORWARDED | REPLICA_SESSION_ID | REPLICA_INSTANCE_IDENTIFIER     | REPLICA_CLUSTER_NAME | REPLICA_REGION |
+-----+----------+--------------------+----------+---------+------+--------------+--------------------------------------------+--------------+--------------------+---------------------------------+---------------------------------------+
| 648 | myuser   | `IP_address:port1`   | sysbench | Query   |    0 | async commit | UPDATE sbtest58 SET k=k+1 WHERE id=4802579 |            1 |                637 | my-db-cluster-instance-2        | my-db-cluster        | us-west-2      |
| 650 | myuser   | `IP_address:port2`   | sysbench | Query   |    0 | async commit | UPDATE sbtest54 SET k=k+1 WHERE id=2503953 |            1 |                639 | my-db-cluster-instance-2        | my-db-cluster        | us-west-2      |
+-----+----------+--------------------+----------+---------+------+--------------+--------------------------------------------+--------------+--------------------+---------------------------------+----------------------+----------------+
```

On the forwarding reader DB instance, you can see the threads associated with these writer DB connections by running
`SHOW PROCESSLIST`. The `REPLICA_SESSION_ID` values on the writer, 637 and 639, are the same as the
`Id` values on the reader.

```
mysql> select @@aurora_server_id;

+---------------------------------+
| @@aurora_server_id              |
+---------------------------------+
| my-db-cluster-instance-2        |
+---------------------------------+
1 row in set (0.00 sec)

mysql> show processlist;

+-----+----------+--------------------+----------+---------+------+--------------+---------------------------------------------+
| Id  | User     | Host               | db       | Command | Time | State        | Info                                        |
+-----+----------+--------------------+----------+---------+------+--------------+---------------------------------------------+
| 637 | myuser   | `IP_address:port1`   | sysbench | Query   |    0 | async commit | UPDATE sbtest12 SET k=k+1 WHERE id=4802579  |
| 639 | myuser   | `IP_address:port2`   | sysbench | Query   |    0 | async commit | UPDATE sbtest61 SET k=k+1 WHERE id=2503953  |
+-----+----------+--------------------+----------+---------+------+--------------+---------------------------------------------+
12 rows in set (0.00 sec)
```
