# Recommendations for MySQL features in Aurora MySQL

The following features are available in Aurora MySQL for MySQL compatibility. However, they have
performance, scalability, stability, or compatibility issues in the Aurora environment. Thus, we recommend
that you follow certain guidelines in your use of these features. For example, we recommend that you don't use
certain features for production Aurora deployments.

###### Topics

- [Using multithreaded replication in
  Aurora MySQL](#AuroraMySQL.BestPractices.MTReplica "#AuroraMySQL.BestPractices.MTReplica")
- [Invoking AWS Lambda functions using
  native MySQL functions](#AuroraMySQL.BestPractices.Lambda "#AuroraMySQL.BestPractices.Lambda")
- [Avoiding XA transactions with Amazon Aurora MySQL](#AuroraMySQL.BestPractices.XA "#AuroraMySQL.BestPractices.XA")
- [Keeping foreign keys turned on during DML statements](#Aurora.BestPractices.ForeignKeys "#Aurora.BestPractices.ForeignKeys")
- [Configuring how frequently the log buffer is flushed](#AuroraMySQL.BestPractices.Flush "#AuroraMySQL.BestPractices.Flush")
- [Minimizing and troubleshooting Aurora MySQL
  deadlocks](#AuroraMySQL.BestPractices.deadlocks "#AuroraMySQL.BestPractices.deadlocks")

## Using multithreaded replication in

Aurora MySQL

With multithreaded binary log replication, a SQL thread reads events from the
relay log and queues them up for SQL worker threads to apply. The SQL worker threads
are managed by a coordinator thread. The binary log events are applied in parallel
when possible.

Multithreaded replication is supported in Aurora MySQL version 3, and in Aurora MySQL
version 2.12.1 and higher.

For Aurora MySQL versions lower than 3.04, Aurora uses single-threaded replication by
default when an Aurora MySQL DB cluster is used as a read replica for binary log
replication.

Earlier versions of Aurora MySQL version 2 inherited several issues regarding
multithreaded replication from MySQL Community Edition. For those versions, we
recommend that you not use multithreaded replication in production.

If you do use multithreaded replication, we recommend that you test it
thoroughly.

For more information about using replication in Amazon Aurora, see [Replication with Amazon Aurora](Aurora.md "Aurora.md"). For more
information about multithreaded replication in Aurora MySQL, see [Multithreaded binary log
replication](binlog-optimization.md#binlog-optimization-multithreading "binlog-optimization.md#binlog-optimization-multithreading").

## Invoking AWS Lambda functions using

native MySQL functions

We recommend using the native MySQL functions `lambda_sync` and `lambda_async` to invoke Lambda
functions.

If you are using the deprecated `mysql.lambda_async` procedure, we
recommend that you wrap calls to the `mysql.lambda_async` procedure in a
stored procedure. You can call this stored procedure from different sources, such as
triggers or client code. This approach can help to avoid impedance mismatch issues and
make it easier for your database programmers to invoke Lambda functions.

For more information on invoking Lambda functions from Amazon Aurora, see [Invoking a Lambda function from an Amazon Aurora MySQL DB
cluster](AuroraMySQL.Integrating.md "AuroraMySQL.Integrating.md").

## Avoiding XA transactions with Amazon Aurora MySQL

We recommend that you don't use eXtended Architecture (XA) transactions with
Aurora MySQL, because they can cause long recovery times if the XA was in the
`PREPARED` state. If you must use XA transactions with Aurora MySQL, follow
these best practices:

- Don't leave an XA transaction open in the `PREPARED` state.
- Keep XA transactions as small as possible.

For more information about using XA transactions with MySQL, see
[XA transactions](https://dev.mysql.com/doc/refman/8.0/en/xa.html "https://dev.mysql.com/doc/refman/8.0/en/xa.html") in the
MySQL documentation.

## Keeping foreign keys turned on during DML statements

We strongly recommend that you don't run any data definition language (DDL)
statements when the `foreign_key_checks` variable is set to `0`
(off).

If you need to insert or update rows that require a transient violation of foreign
keys, follow these steps:

1. Set `foreign_key_checks` to `0`.
2. Make your data manipulation language (DML) changes.
3. Make sure that your completed changes don't violate any foreign key
   constraints.
4. Set `foreign_key_checks` to `1` (on).

In addition, follow these other best practices for foreign key constraints:

- Make sure that your client applications don't set the
  `foreign_key_checks` variable to `0` as a part of the
  `init_connect` variable.
- If a restore from a logical backup such as `mysqldump` fails or
  is incomplete, make sure that `foreign_key_checks` is set to
  `1` before starting any other operations in the same session. A
  logical backup sets `foreign_key_checks` to `0` when it
  starts.

## Configuring how frequently the log buffer is flushed

In MySQL Community Edition, to make transactions durable, the InnoDB log buffer must be flushed to durable storage. You
use the`innodb_flush_log_at_trx_commit` parameter to configure how frequently the log buffer is flushed to
disk.

When you set the `innodb_flush_log_at_trx_commit` parameter to the default value of 1, the log buffer is
flushed at each transaction commit. This setting helps to keep the database [ACID](https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_acid "https://dev.mysql.com/doc/refman/5.7/en/glossary.html#glos_acid") compliant. We recommend that you
keep the default setting of 1.

Changing `innodb_flush_log_at_trx_commit` to a nondefault value can help reduce data manipulation language
(DML) latency, but sacrifices the durability of the log records. This lack of durability makes the database ACID
noncompliant. We recommend that your databases be ACID compliant to avoid the risk of data loss in the event of a server
restart. For more information on this parameter, see [innodb_flush_log_at_trx_commit](https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit "https://dev.mysql.com/doc/refman/5.7/en/innodb-parameters.html#sysvar_innodb_flush_log_at_trx_commit") in the MySQL documentation.

In Aurora MySQL, redo log processing is offloaded to the storage layer, so no flushing to log files occurs on the DB
instance. When a write is issued, redo logs are sent from the writer DB instance directly to the Aurora cluster volume. The
only writes that cross the network are redo log records. No pages are ever written from the database tier.

By default, each thread committing a transaction waits for confirmation from the Aurora cluster volume. This confirmation
indicates that this record and all previous redo log records are written and have achieved [quorum](https://aws.amazon.com/blogs/database/amazon-aurora-under-the-hood-quorum-and-correlated-failure/ "https://aws.amazon.com/blogs/database/amazon-aurora-under-the-hood-quorum-and-correlated-failure/").
Persisting the log records and achieving quorum make the transaction durable, whether through autocommit or explicit commit.
For more information on the Aurora storage architecture, see [Amazon Aurora storage
demystified](https://d1.awsstatic.com/events/reinvent/2020/Amazon_Aurora_storage_demystified_DAT401.pdf "https://d1.awsstatic.com/events/reinvent/2020/Amazon_Aurora_storage_demystified_DAT401.pdf").

Aurora MySQL doesn't flush logs to data files as MySQL Community Edition does. However, you can use the
`innodb_flush_log_at_trx_commit` parameter to relax durability constraints when writing redo log records to
the Aurora cluster volume.

For Aurora MySQL version 2:

- `innodb_flush_log_at_trx_commit` = 0 or 2 – The database doesn't wait for confirmation that the
  redo log records are written to the Aurora cluster volume.
- `innodb_flush_log_at_trx_commit` = 1 – The database waits for confirmation that the redo log
  records are written to the Aurora cluster volume.

For Aurora MySQL version 3:

- `innodb_flush_log_at_trx_commit` = 0 – The database doesn't wait for confirmation that the redo
  log records are written to the Aurora cluster volume.
- `innodb_flush_log_at_trx_commit` = 1 or 2 – The database waits for confirmation that the redo
  log records are written to the Aurora cluster volume.

Therefore, to obtain the same nondefault behavior in Aurora MySQL version 3 that you would with the value set to 0 or 2 in
Aurora MySQL version 2, set the parameter to 0.

While these settings can lower DML latency to the client, they can also result in data loss in the event of a failover or
restart. Therefore, we recommend that you keep the `innodb_flush_log_at_trx_commit` parameter set to the default
value of 1.

While data loss can occur in both MySQL Community Edition and Aurora MySQL, behavior differs in each database because of
their different architectures. These architectural differences can lead to varying degrees of data loss. To make sure that
your database is ACID compliant, always set `innodb_flush_log_at_trx_commit` to 1.

###### Note

In Aurora MySQL version 3, before you can change `innodb_flush_log_at_trx_commit` to a value other than 1,
you must first change the value of `innodb_trx_commit_allow_data_loss` to 1. By doing so, you acknowledge the
risk of data loss.

## Minimizing and troubleshooting Aurora MySQL

deadlocks

Users running workloads that regularly experience constraint violations on unique secondary indexes or foreign keys, when
modifying records on the same data page concurrently, might experience increased deadlocks and lock wait timeouts. These
deadlocks and timeouts are because of a MySQL Community Edition [bug
fix](https://bugs.mysql.com/bug.php?id=98324 "https://bugs.mysql.com/bug.php?id=98324").

This fix is included in MySQL Community Edition versions 5.7.26 and higher, and was backported into Aurora MySQL versions
2.10.3 and higher. The fix is necessary for enforcing _serializability_, by implementing additional
locking for these types of data manipulation language (DML) operations, on changes made to records in an InnoDB table. This
issue was uncovered as part of an investigation into deadlock issues introduced by a previous MySQL Community Edition [bug fix](https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-26.html "https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-26.html").

The fix changed the internal handling for the _partial rollback_ of a tuple (row) update in the InnoDB
storage engine. Operations that generate constraint violations on foreign keys or unique secondary indexes cause partial
rollback. This includes, but isn't limited to, concurrent `INSERT...ON DUPLICATE KEY UPDATE`, `REPLACE
 INTO,` and `INSERT IGNORE` statements (_upserts_).

In this context, partial rollback doesn't refer to the rollback of application-level transactions, but rather an internal
InnoDB rollback of changes to a clustered index, when a constraint violation is encountered. For example, a duplicate key
value is found during an upsert operation.

In a normal insert operation, InnoDB atomically creates [clustered](https://dev.mysql.com/doc/refman/5.7/en/innodb-index-types.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-index-types.html") and secondary index entries for
each index. If InnoDB detects a duplicate value on a unique secondary index during an upsert operation, the inserted entry
in the clustered index has to be reverted (partial rollback), and the update then has to be applied to the existing
duplicate row. During this internal partial rollback step, InnoDB must lock each record seen as part of the operation. The
fix ensures transaction serializability by introducing additional locking after the partial rollback.

### Minimizing InnoDB deadlocks

You can take the following approaches to reduce the frequency of deadlocks in your database instance. More examples
can be found in the [MySQL documentation](https://bugs.mysql.com/bug.php?id=98324 "https://bugs.mysql.com/bug.php?id=98324").

1. To reduce the chances of deadlocks, commit transactions immediately after making a related set of changes. You
   can do this by breaking up large transactions (multiple row updates between commits) into smaller ones. If
   you're batch inserting rows, then try to reduce batch insert sizes, especially when using the upsert operations
   mentioned previously.

To reduce the number of possible partial rollbacks, you can try some of the following approaches:

    1. Replace batch insert operations with inserting one row at a time. This can reduce the amount of time
     where locks are held by transactions that might have conflicts.
    2. Instead of using `REPLACE INTO`, rewrite the SQL statement as a multistatement transaction
     such as the following:



    ```
    BEGIN;
    DELETE `conflicting rows`;
    INSERT `new rows`;
    COMMIT;
    ```
    3. Instead of using `INSERT...ON DUPLICATE KEY UPDATE`, rewrite the SQL statement as a
     multistatement transaction such as the following:



    ```
    BEGIN;
    SELECT `rows that conflict on secondary indexes`;
    UPDATE `conflicting rows`;
    INSERT `new rows`;
    COMMIT;
    ```

2. Avoid long-running transactions, active or idle, that might hold onto locks. This includes interactive MySQL
   client sessions that might be open for an extended period with an uncommitted transaction. When optimizing
   transaction sizes or batch sizes, the impact can vary depending on a number of factors such as concurrency,
   number of duplicates, and table structure. Any changes should be implemented and tested based on your
   workload.
3. In some situations, deadlocks can occur when two transactions attempt to access the same datasets, either in
   one or multiple tables, in different orders. To prevent this, you can modify the transactions to access the data
   in the same order, thereby serializing the access. For example, create a queue of transactions to be completed.
   This approach can help to avoid deadlocks when multiple transactions occur concurrently.
4. Adding carefully chosen indexes to your tables can improve selectivity and reduce the need to access rows,
   which leads to less locking.
5. If you encounter [gap
   locking](https://dev.mysql.com/doc/refman/5.7/en/innodb-locking.html#innodb-gap-locks "https://dev.mysql.com/doc/refman/5.7/en/innodb-locking.html#innodb-gap-locks"), you can modify the transaction isolation level to `READ COMMITTED` for the
   session or transaction to prevent it. For more information on InnoDB isolation levels and their behaviors, see
   [Transaction
   isolation levels](https://dev.mysql.com/doc/refman/5.7/en/innodb-transaction-isolation-levels.html "https://dev.mysql.com/doc/refman/5.7/en/innodb-transaction-isolation-levels.html") in the MySQL documentation.

###### Note

While you can take precautions to reduce the possibility of deadlocks occurring, deadlocks are an expected
database behavior and can still occur. Applications should have the necessary logic to handle deadlocks when they
are encountered. For example, implement retry and backing-off logic in the application. It’s best to address the
root cause of the issue but if a deadlock does occur, the application has the option to wait and retry.

### Monitoring InnoDB deadlocks

[Deadlocks](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_deadlock "https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_deadlock") can occur in MySQL when
application transactions try to take table-level and row-level locks in a way that results in circular waiting. An
occasional InnoDB deadlock isn't necessarily an issue, because the InnoDB storage engine detects the condition immediately
and rolls back one of the transactions automatically. If you encounter deadlocks frequently, we recommend reviewing and
modifying your application to alleviate performance issues and avoid deadlocks. When [deadlock detection](https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_deadlock_detection "https://dev.mysql.com/doc/refman/8.0/en/glossary.html#glos_deadlock_detection") is turned
on (the default), InnoDB automatically detects transaction deadlocks and rolls back a transaction or transactions to break
the deadlock. InnoDB tries to pick small transactions to roll back, where the size of a transaction is determined by the
number of rows inserted, updated, or deleted.

- `SHOW ENGINE` statement – The `SHOW ENGINE INNODB STATUS \G` statement contains
  [details](https://dev.mysql.com/doc/refman/5.7/en/show-engine.html "https://dev.mysql.com/doc/refman/5.7/en/show-engine.html") of the most recent
  deadlock encountered on the database since the last restart.
- MySQL error log – If you encounter frequent deadlocks where the output of the `SHOW ENGINE`
  statement is inadequate, you can turn on the [innodb_print_all_deadlocks](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_print_all_deadlocks "https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_print_all_deadlocks") DB cluster parameter.

When this parameter is turned on, information about all deadlocks in InnoDB user transactions is recorded in the
Aurora MySQL [error log](https://dev.mysql.com/doc/refman/8.0/en/error-log.html "https://dev.mysql.com/doc/refman/8.0/en/error-log.html").

- Amazon CloudWatch metrics – We also recommend that you proactively monitor deadlocks using the CloudWatch metric
  `Deadlocks`. For more information, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").
- Amazon CloudWatch Logs – With CloudWatch Logs, you can view metrics, analyze log data, and create real-time alarms. For more
  information, see [Monitor errors in Amazon Aurora MySQL and Amazon RDS for MySQL using Amazon CloudWatch and send notifications using
  Amazon SNS](https://aws.amazon.com/blogs/database/monitor-errors-in-amazon-aurora-mysql-and-amazon-rds-for-mysql-using-amazon-cloudwatch-and-send-notifications-using-amazon-sns/ "https://aws.amazon.com/blogs/database/monitor-errors-in-amazon-aurora-mysql-and-amazon-rds-for-mysql-using-amazon-cloudwatch-and-send-notifications-using-amazon-sns/").

Using CloudWatch Logs with `innodb_print_all_deadlocks` turned on, you can configure alarms to notify you when
the number of deadlocks exceeds a given threshold. To define a threshold, we recommend that you observe your trends
and use a value based on your normal workload.

- Performance Insights – When you use Performance Insights, you can monitor the `innodb_deadlocks` and
  `innodb_lock_wait_timeout` metrics. For more information on these metrics, see [Non-native counters for Aurora MySQL](USER_PerfInsights_Counters.md#USER_PerfInsights_Counters.Aurora_MySQL.NonNative "USER_PerfInsights_Counters.md#USER_PerfInsights_Counters.Aurora_MySQL.NonNative").
