

# Resolving unidentifiable vacuum blockers in Aurora PostgreSQL
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Unidentifiable_blockers"></a>

This section explores additional reasons that can prevent vacuuming from making progress. These issues are currently not directly identifiable by the `postgres_get_av_diag()` function. 

**Topics**
+ [Index inconsistency](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Index_inconsistency)
+ [Exceptionally high transaction rate](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.High_transaction_rate)

## Index inconsistency
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Index_inconsistency"></a>

A logically inconsistent index can prevent autovacuum from making progress. The following errors or similar errors are logged during either the vacuum phase of the index or when the index is accessed by SQL statements.

```
ERROR: right sibling's left-link doesn't match:block 5 links to 10 instead of expected 2 in index ix_name
```

```
ERROR: failed to re-find parent key in index "XXXXXXXXXX" for deletion target page XXX
CONTEXT:  while vacuuming index index_name of relation {{schema.table}}
```

**Guidance**

Rebuild the index or skip indexes using `INDEX_CLEANUP` on manual `VACUUM FREEZE`. 
+ **Using the CONCURRENTLY option** – Prior to PostgreSQL version 12, rebuilding an index required an exclusive table lock, restricting access to the table. With PostgreSQL version 12, and later versions, the CONCURRENTLY option allows for row-level locking, significantly improving the table's availability. Following is the command:

  ```
  REINDEX INDEX ix_name CONCURRENTLY;
  ```

  While CONCURRENTLY is less disruptive, it can be slower on busy tables. Consider building the index during low-traffic periods if possible. For more information, see [REINDEX](https://www.postgresql.org/docs/current/sql-reindex.html) in *PostgreSQL* documentation.
+ **Using the INDEX\_CLEANUP FALSE option** – If the indexes are large and estimated to require a significant amount of time to finish, you can unblock autovacuum by executing a manual VACUUM FREEZE while excluding indexes. This functionality is available in PostgreSQL version 12 and later versions.

  Bypassing indexes will allow you to skip the vacuum process of the inconsistent index and mitigate the wraparound issue. However, this will not resolve the underlying invalid page problem. To fully address and resolve the invalid page issue, you will still need to rebuild the index.

## Exceptionally high transaction rate
<a name="Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.High_transaction_rate"></a>

In PostgreSQL, high transaction rates can significantly impact autovacuum's performance, leading to slower cleanup of dead tuples and increased risk of transaction ID wraparound. You can monitor the transaction rate by measuring the difference in `max(age(datfrozenxid))` between two time periods, typically per second. Additionally, you can use the following database counter metrics, which are exposed through the Performance Insights API, to measure the transaction rate (the sum of xact\_commit and xact\_rollback) which is the total number of transactions.


|  Counter  |  Type  |  Unit  |  Metric  | 
| --- | --- | --- | --- | 
| xact\_commit | Transactions | Commits per second | db.Transactions.xact\_commit | 
| xact\_rollback | Transactions | Rollbacks per second | db.Transactions.xact\_rollback | 

A rapid increase indicates a high transaction load, which can overwhelm autovacuum, causing bloat, lock contention, and potential performance issues. This can negatively impact the autovacuum process in a couple of ways:
+ **Table Activity:** The specific table being vacuumed could be experiencing a high volume of transactions, causing delays.
+ **System Resources** The overall system might be overloaded, making it difficult for autovacuum to access the necessary resources to function efficiently.

Consider the following strategies for allowing autovacuum to operate more effectively and keep up with its tasks:

1. Reduce the transaction rate if possible. Consider to batch or group similar transactions where feasible.

1. Target frequently updated tables with manual `VACUUM FREEZE` operation nightly, weekly, or biweekly during off-peak hours. 

1. Consider scaling up your instance class to allocate more system resources to handle the high transaction volume and autovacuum.