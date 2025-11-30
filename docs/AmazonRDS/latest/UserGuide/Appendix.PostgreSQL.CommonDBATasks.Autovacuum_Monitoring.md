# Resolving identifiable vacuum blockers in RDS for PostgreSQL

Autovacuum performs aggressive vacuums and lowers the age of transaction IDs to below the
threshold specified by the `autovacuum_freeze_max_age` parameter of your RDS
instance. You can track this age using the Amazon CloudWatch metric
`MaximumUsedTransactionIDs`.

To find the setting of `autovacuum_freeze_max_age` (which has a default of 200
million transaction IDs) for your Amazon RDS instance, you can use the following query:

```
SELECT
    TO_CHAR(setting::bigint, 'FM9,999,999,999') autovacuum_freeze_max_age
FROM
    pg_settings
WHERE
    name = 'autovacuum_freeze_max_age';
```

Note that `postgres_get_av_diag()` only checks for aggressive vacuum blockers
when the age exceeds Amazon RDS’ [adaptive
autovacuum](Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptiveAutoVacuuming "Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.Autovacuum.AdaptiveAutoVacuuming") threshold of 500 million transaction IDs. For
`postgres_get_av_diag()` to detect blockers, the blocker must be at least 500
million transactions old.

The `postgres_get_av_diag()` function identifies the following types of
blockers:

###### Topics

- [Active statement](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Active_statement "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Active_statement")
- [Idle in transaction](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Idle_in_transaction "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Idle_in_transaction")
- [Prepared transaction](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Prepared_transaction "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Prepared_transaction")
- [Logical replication slot](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Logical_replication_slot "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Logical_replication_slot")
- [Read replicas](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Read_replicas "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Read_replicas")
- [Temporary tables](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Temporary_tables "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Temporary_tables")

## Active statement

In PostgreSQL, an active statement is an SQL statement that is currently being executed
by the database. This includes queries, transactions, or any operations in progress. When
monitoring via `pg_stat_activity`, the state column indicates that the process
with the corresponding PID is active.

The `postgres_get_av_diag()` function displays output similar to the
following when it identifies a statement that is an active statement.

```
blocker               | Active statement
database              | my_database
blocker_identifier    | SELECT pg_sleep(20000);
wait_event            | Timeout:PgSleep
autovacuum_lagging_by | 568,600,871
suggestion            | Connect to database "my_database", review carefully and you may consider terminating the process using suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.
suggested_action      | {"SELECT pg_terminate_backend (29621);"}
```

**Suggested action**

Following the guidance in the `suggestion` column, the user can connect to
the database where the active statement is present and, as specified in the
`suggested_action` column, it's advisable to carefully review the option to
terminate the session. If termination is safe, you may use the
`pg_terminate_backend()` function to terminate the session. This action can be
performed by an administrator (such as the RDS master account) or a user with the required
`pg_terminate_backend()` privilege.

###### Warning

A terminated session will undo (`ROLLBACK`) changes it made. Depending on
your requirements, you may want to rerun the statement. However, it is recommended to do
so only after the autovacuum process has finished its aggressive vacuum operation.

## Idle in transaction

An idle in transaction statement refers to any session that has opened an explicit
transaction (such as by issuing a `BEGIN` statement), performed some work, and is
now waiting for the client to either pass more work or signal the end of the transaction by
issuing a `COMMIT`, `ROLLBACK`, or `END` (which would
result in an implicit `COMMIT`).

The `postgres_get_av_diag()` function displays output similar to the
following when it identifies an `idle in transaction` statement as a
blocker.

```
blocker               | idle in transaction
database              | my_database
blocker_identifier    | INSERT INTO tt SELECT * FROM tt;
wait_event            | Client:ClientRead
autovacuum_lagging_by | 1,237,201,759
suggestion            | Connect to database "my_database", review carefully and you may consider terminating the process using suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.
suggested_action      | {"SELECT pg_terminate_backend (28438);"}
```

**Suggested action**

As indicated in the `suggestion` column, you can connect to the database
where the idle in transaction session is present and terminate the session using the
`pg_terminate_backend()` function. The user can be your admin (RDS master
account) user or a user with the `pg_terminate_backend()` privilege.

###### Warning

A terminated session will undo (`ROLLBACK`) changes it made. Depending on
your requirements, you may want to rerun the statement. However, it is recommended to do
so only after the autovacuum process has finished its aggressive vacuum operation.

## Prepared transaction

PostgreSQL allows transactions that are part of a two-phase commit strategy called
[prepared
transactions](https://www.postgresql.org/docs/current/sql-prepare-transaction.html "https://www.postgresql.org/docs/current/sql-prepare-transaction.html"). These are enabled by setting the
`max_prepared_transactions` parameter to a non-zero value. Prepared
transactions are designed to ensure that a transaction is durable and remains available even
after database crashes, restarts, or client disconnections. Like regular transactions, they
are assigned a transaction ID and can affect the autovacuum. If left in a prepared state,
autovacuum cannot perform freeezing and it can lead to transaction ID wraparound.

When transactions are left prepared indefinitely without being resolved by a transaction
manager, they become orphaned prepared transactions. The only way to fix this is to either
commit or rollback the transaction using the `COMMIT PREPARED` or `ROLLBACK
 PREPARED` commands, respectively.

###### Note

Be aware that a backup taken during a prepared transaction will still contain that
transaction after restoration. Refer to the following information about how to locate and
close such transactions.

The `postgres_get_av_diag()` function displays the following output when it
identifies a blocker that is a prepared transaction.

```
blocker               | Prepared transaction
database              | my_database
blocker_identifier    | myptx
wait_event            | Not applicable
autovacuum_lagging_by | 1,805,802,632
suggestion            | Connect to database "my_database" and consider either COMMIT or ROLLBACK the prepared transaction using suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.
suggested_action      | {"COMMIT PREPARED 'myptx';",[OR],"ROLLBACK PREPARED 'myptx';"}
```

**Suggested action**

As mentioned in the suggestion column, connect to the database where the prepared
transaction is located. Based on the `suggested_action` column, carefully review
whether to perform either `COMMIT` or `ROLLBACK`, and the the
appropiate the action.

To monitor prepared transactions in general, PostgreSQL offers a catalog view called
`pg_prepared_xacts`. You can use the following query to find prepared
transactions.

```
SELECT
    gid,
    prepared,
    owner,
    database,
    transaction AS oldest_xmin
FROM
    pg_prepared_xacts
ORDER BY
    age(transaction) DESC;
```

## Logical replication slot

The purpose of a replication slot is to hold unconsumed changes until they are
replicated to a target server. For more information, see PostgreSQL's [Logical
replication](https://www.postgresql.org/docs/current/logical-replication.html "https://www.postgresql.org/docs/current/logical-replication.html").

There are two types of logical replication slots.

**Inactive logical replication slots**

When replication is terminated, unconsumed transaction logs can't be removed, and the
replication slot becomes inactive. Although an inactive logical replication slot isn't
currently used by a subscriber, it remains on the server, leading to the retention of WAL
files and preventing the removal of old transaction logs. This can increase disk usage and
specifically block autovacuum from cleaning up internal catalog tables, as the system must
preserve LSN information from being overwritten. If not addressed, this can result in
catalog bloat, performance degradation, and an increased risk of wraparound vacuum,
potentially causing transaction downtime.

**Active but slow logical replication slots**

Sometimes removal of dead tuples of catalog is delayed due to the performance
degradation of logical replication. This delay in replication slows down updating the
`catalog_xmin` and can lead to catalog bloat and wraparound vacuum.

The `postgres_get_av_diag()` function displays output similar to the
following when it finds a logical replication slot as a blocker.

```
blocker               | Logical replication slot
database              | my_database
blocker_identifier    | slot1
wait_event            | Not applicable
autovacuum_lagging_by | 1,940,103,068
suggestion            | Ensure replication is active and resolve any lag for the slot if active. If inactive, consider dropping it using the command in suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.
suggested_action      | {"SELECT pg_drop_replication_slot('slot1') FROM pg_replication_slots WHERE active = 'f';"}
```

**Suggested action**

To resolve this problem, check the replication configuration for issues with the target
schema or data that might be terminating the apply process. The most common reasons are the
following:

- Missing columns
- Incompatible data type
- Data mismatch
- Missing table

If the problem is related to infrastructure issues:

- Network issues - [How do I resolve
  issues with an Amazon RDS DB in an incompatible network state?](https://repost.aws/knowledge-center/rds-incompatible-network "https://repost.aws/knowledge-center/rds-incompatible-network").
- Database or DB instance is not available due to the following reasons:
  - Replica instance is out of storage - Review [Amazon RDS DB instances
    run out of storage](https://repost.aws/knowledge-center/rds-out-of-storage "https://repost.aws/knowledge-center/rds-out-of-storage") for information about adding storage.
  - Incompatible-parameters - Review [How can I
    fix an Amazon RDS DB instance that is stuck in the incompatible-parameters
    status?](https://repost.aws/knowledge-center/rds-incompatible-parameters "https://repost.aws/knowledge-center/rds-incompatible-parameters") for more information about how you can resolve the issue.

If your instance is outside the AWS network or on AWS EC2, consult your
administrator on how to resolve the availability or infrastructure-related issues.

**Dropping the inactive slot**

###### Warning

Caution: Before dropping a replication slot, carefully ensure that it has no ongoing
replication, is inactive, and is in an unrecoverable state. Dropping a slot prematurely
could disrupt replication or cause data loss.

After confirming that the replication slot is no longer needed, drop it to allow
autovacuum to continue. The condition `active = 'f'` ensures that only an
inactive slot is dropped.

```
SELECT pg_drop_replication_slot('slot1') WHERE active ='f'
```

## Read replicas

When the `hot_standby_feedback` setting is enabled for [Amazon RDS read
replicas](USER_PostgreSQL.Replication.md "USER_PostgreSQL.Replication.md"), it prevents autovacuum on the primary database from removing
dead rows that might still be needed by queries running on the read replica. This affects
all types of physical read replicas including those managed with or without replication
slots. This behavior is necessary because queries running on the standby replica require
those rows to remain available on the primary preventing [query
conflicts](https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-CONFLICT "https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-CONFLICT") and cancellations.

###### Read replica with physical replication slot

Read replicas with physical replication slots significantly enhance the reliability
and stability of replication in RDS for PostgreSQL. These slots
ensure the primary database retains essential Write-Ahead Log files until the replica
processes them, maintaining data consistency even during network disruptions.

Beginning with RDS for PostgreSQL version 14, all replicas utilize replication
slots. In earlier versions, only cross-Region replicas used replication slots.

The `postgres_get_av_diag()` function displays output similar to the
following when it finds a read replica with physical replication slot as the blocker.

```
blocker               | Read replica with physical replication slot
database              |
blocker_identifier    | rds_us_west_2_db_xxxxxxxxxxxxxxxxxxxxx
wait_event            | Not applicable
autovacuum_lagging_by | 554,080,689
suggestion            | Run the following query on the replica "rds_us_west_2_db_xxxxxxxxxxxxxxxxxxxx" to find the long running query:
                      | SELECT * FROM pg_catalog.pg_stat_activity WHERE backend_xmin::text::bigint = 757989377;
                      | Review carefully and you may consdier terminating the query on read replica using suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.                                 +                      |
suggested_action      | {"SELECT pg_terminate_backend(pid) FROM pg_catalog.pg_stat_activity WHERE backend_xmin::text::bigint = 757989377;","                                                                                 +
                      | [OR]                                                                                                                                                                                                 +
                      | ","Disable hot_standby_feedback","                                                                                                                                                                   +
                      | [OR]                                                                                                                                                                                                 +
                      | ","Delete the read replica if not needed"}
```

###### Read replica with streaming replication

Amazon RDS allows setting up read replicas without a physical replication slot in older
versions, up to version 13. This approach reduces overhead by allowing the primary to
recycle WAL files more aggressively, which is advantageous in environments with limited
disk space and can tolerate occasional ReplicaLag. However, without a slot, the standby
must remain in sync to avoid missing WAL files. Amazon RDS uses archived WAL files to help the
replica catch up if it falls behind, but this process requires careful monitoring and can
be slow.

The `postgres_get_av_diag()` function displays output similar to the
following when it finds a streaming read replica as the blocker.

```
blocker               | Read replica with streaming replication slot
database              | Not applicable
blocker_identifier    | xx.x.x.xxx/xx
wait_event            | Not applicable
autovacuum_lagging_by | 610,146,760
suggestion            | Run the following query on the replica "xx.x.x.xxx" to find the long running query:                                                                                                                                                         +
                      | SELECT * FROM pg_catalog.pg_stat_activity WHERE backend_xmin::text::bigint = 348319343;                                                                                                                                                     +
                      | Review carefully and you may consdier terminating the query on read replica using suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.                                       +
                      |
suggested_action      | {"SELECT pg_terminate_backend(pid) FROM pg_catalog.pg_stat_activity WHERE backend_xmin::text::bigint = 348319343;","                                                                                                                        +
                      | [OR]                                                                                                                                                                                                                                        +
                      | ","Disable hot_standby_feedback","                                                                                                                                                                                                          +
                      | [OR]                                                                                                                                                                                                                                        +
                      | ","Delete the read replica if not needed"}
```

**Suggested action**

As recommended in the `suggested_action` column, carefully review these
options to unblock autovacuum.

- **Terminate the query** – Following the guidance
  in the suggestion column, you can connect to the read replica, as specified in the
  suggested_action column, it's advisable to carefully review the option to terminate the
  session. If termination is deemed safe, you may use the
  `pg_terminate_backend()` function to terminate the session. This action can
  be performed by an administrator (such as the RDS master account) or a user with the
  required pg_terminate_backend() privilege.

You may run the following SQL command on the read replica to terminate the query
that is preventing the vacuum on the primary from cleaning up old rows. The value of
`backend_xmin` is reported in the function’s output:

```
SELECT
    pg_terminate_backend(pid)
FROM
    pg_catalog.pg_stat_activity
WHERE
    backend_xmin::text::bigint = `backend_xmin;`

```

- **Disable hot standby feedback** – Consider
  disabling the `hot_standby_feedback` parameter if it's causing significant
  vacuum delays.

The `hot_standby_feedback` parameter allows a read replica to inform the
primary about its query activity, preventing the primary from vacuuming tables or rows
that are in use on the standby. While this ensures query stability on the standby, it
can significantly delay vacuuming on the primary. Disabling this feature allows the
primary to proceed with vacuuming without waiting for the standby to catch up. However,
this can lead to query cancellations or failures on the standby if it attempts to access
rows that have been vacuumed by the primary.

- **Delete the read replica if not needed** – If
  the read replica is no longer necessary, you can delete it. This will remove the
  associated replication overhead and allow the primary to recycle transaction logs
  without being held back by the replica.

## Temporary tables

[Temporary
tables](https://www.postgresql.org/docs/current/sql-createtable.html "https://www.postgresql.org/docs/current/sql-createtable.html"), created using the `TEMPORARY` keyword, reside in the temp
schema, for example pg_temp_xxx, and are only accessible to the session that created them.
Temporary tables are dropped when the session ends. However, these tables are invisible to
PostgreSQL's autovacuum process, and must be manually vacuumed by the session that created
them. Trying to vacuum the temp table from another session has no effect.

In unusual circumstances, a temporary table exists without an active session owning it.
If the owning session ends unexpectedly due to a fatal crash, network issue, or similar
event, the temporary table might not be cleaned up, leaving it behind as an "orphaned"
table. When the PostgreSQL autovacuum process detects an orphaned temporary table, it logs
the following message:

```
LOG: autovacuum: found orphan temp table \"%s\".\"%s\" in database \"%s\"
```

The `postgres_get_av_diag()` function displays output similar to the
following when it identifies a temporary table as a blocker. For the function to correctly
show the output related to temporary tables, it needs to be executed within the same
database where those tables exist.

```
blocker               | Temporary table
database              | my_database
blocker_identifier    | pg_temp_14.ttemp
wait_event            | Not applicable
autovacuum_lagging_by | 1,805,802,632
suggestion            | Connect to database "my_database". Review carefully, you may consider dropping temporary table using command in suggested_action. For more information, see Working with PostgreSQL autovacuum in the Amazon RDS User Guide.
suggested_action      | {"DROP TABLE ttemp;"}
```

**Suggested action**

Follow the instructions provided in the `suggestion` column of the output to
identify and remove the temporary table that is preventing autovacuum from running. Use the
following command to drop the temporary table reported by
`postgres_get_av_diag()`. Replace the table name based on the output provided
by the `postgres_get_av_diag()` function.

```
DROP TABLE `my_temp_schema`.`my_temp_table`;
```

The following query can be used to identify temporary tables:

```
SELECT
    oid,
    relname,
    relnamespace::regnamespace,
    age(relfrozenxid)
FROM
    pg_class
WHERE
relpersistence = 't'
ORDER BY
    age(relfrozenxid) DESC;
```
