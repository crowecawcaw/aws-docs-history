# Resolving unidentifiable vacuum blockers in RDS for PostgreSQL

This section explores additional reasons that can prevent vacuuming from making progress.
These issues are currently not directly identifiable by the
`postgres_get_av_diag()` function.

###### Topics

- [Invalid pages](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Invalid_pages "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Invalid_pages")
- [Index inconsistency](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Index_inconsistency "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Index_inconsistency")
- [Exceptionally high transaction rate](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.High_transaction_rate "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.High_transaction_rate")

## Invalid pages

An invalid page error occurs when PostgreSQL detects a mismatch in a page’s checksum
while accessing that page. The contents are unreadable, preventing autovacuum from freezing
tuples. This effectively stops the cleanup process. The following error is written into
PostgreSQL’s log:

```
WARNING:  page verification failed, calculated checksum YYYYY but expected XXXX
ERROR:  invalid page in block ZZZZZ of relation base/XXXXX/XXXXX
CONTEXT:  automatic vacuum of table `myschema.mytable`
```

**Determine the object type**

```
ERROR: invalid page in block 4305910 of relation base/16403/186752608
WARNING: page verification failed, calculated checksum 50065 but expected 60033
```

From the error message, the path `base/16403/186752608` provides the
following information:

- "base" is the directory name under the PostgreSQL data directory.
- "16403" is the database OID, which you can look up in the `pg_database`
  system catalog.
- "186752608" is the `relfilenode`, which you can use to look up the schema
  and object name in the `pg_class` system catalog.

By checking the output of the following query in the impacted database, you can
determine the object type. The following query retrieves object information for oid: 186752608. Replace the OID with the one relevant to the error you encountered.

```
SELECT
    relname AS object_name,
    relkind AS object_type,
    nspname AS schema_name
FROM
    pg_class c
    JOIN pg_namespace n ON c.relnamespace = n.oid
WHERE
    c.oid = 186752608;
```

For more information, see the PostgreSQL documentation [`pg_class`](https://www.postgresql.org/docs/current/catalog-pg-class.html "https://www.postgresql.org/docs/current/catalog-pg-class.html") for all the supported object types, noted by the
`relkind` column in `pg_class`.

**Guidance**

The most effective solution for this issue depends on the configuration of your specific
Amazon RDS instance and the type of data impacted by the inconsistent page.

**If the object type is an index:**

Rebuilding the index is recommended.

- **Using the `CONCURRENTLY` option** –
  Prior to PostgreSQL version 12, rebuilding an index required an exclusive table lock,
  restricting access to the table. With PostgreSQL version 12, and later versions, the
  `CONCURRENTLY` option allows for row-level locking, significantly improving
  the table's availability. Following is the command:

```
REINDEX INDEX `ix_name` CONCURRENTLY;
```

While `CONCURRENTLY` is less disruptive, it can be slower on busy tables.
Consider building the index during low-traffic periods if possible.

For more information, see the PostgreSQL [REINDEX](https://www.postgresql.org/docs/current/sql-reindex.html "https://www.postgresql.org/docs/current/sql-reindex.html")
documentation.

- **Using the `INDEX_CLEANUP FALSE` option**
  – If the indexes are large and estimated to require a significant amount of time
  to finish, you can unblock autovacuum by executing a manual `VACUUM FREEZE`
  while excluding indexes. This functionality is available in PostgreSQL version 12 and
  later versions.

Bypassing indexes will allow you to skip the vacuum process of the inconsistent
index and mitigate the wraparound issue. However, this will not resolve the underlying
invalid page problem. To fully address and resolve the invalid page issue, you will
still need to rebuild the index.

**If the object type is a materialized view:**

If an invalid page error occurs on a materialized view, login to the impacted database
and refresh it to resolve the invalid page:

Refresh the materialized view:

```
REFRESH MATERIALIZED VIEW schema_name.materialized_view_name;
```

If refreshing fails, try recreating:

```
DROP MATERIALIZED VIEW schema_name.materialized_view_name;
CREATE MATERIALIZED VIEW schema_name.materialized_view_name AS query;
```

Refreshing or recreating the materialized view restores it without impacting the
underlying table data.

**For all other object types:**

For all other object types, reach out to AWS support.

## Index inconsistency

A logically inconsistent index can prevent autovacuum from making progress. The
following errors or similar errors are logged during either the vacuum phase of the index or
when the index is accessed by SQL statements.

```
ERROR: right sibling's left-link doesn't match:block 5 links to 10 instead of expected 2 in index `ix_name`
```

```
ERROR: failed to re-find parent key in index "XXXXXXXXXX" for deletion target page XXX
CONTEXT:  while vacuuming index `index_name` of relation `schema.table`
```

**Guidance**

Rebuild the index or skip indexes using `INDEX_CLEANUP` on manual
`VACUUM FREEZE`. For information about how to
rebuild the index, see [If the
object type is an index](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Invalid_pages "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Invalid_pages").

- **Using the CONCURRENTLY option** – Prior to
  PostgreSQL version 12, rebuilding an index required an exclusive table lock, restricting
  access to the table. With PostgreSQL version 12, and later versions, the CONCURRENTLY
  option allows for row-level locking, significantly improving the table's availability.
  Following is the command:

```
REINDEX INDEX ix_name CONCURRENTLY;
```

While CONCURRENTLY is less disruptive, it can be slower on busy tables. Consider
building the index during low-traffic periods if possible. For more information, see
[REINDEX](https://www.postgresql.org/docs/current/sql-reindex.html "https://www.postgresql.org/docs/current/sql-reindex.html")
in _PostgreSQL_ documentation.

- **Using the INDEX_CLEANUP FALSE option** – If
  the indexes are large and estimated to require a significant amount of time to finish,
  you can unblock autovacuum by executing a manual VACUUM FREEZE while excluding indexes.
  This functionality is available in PostgreSQL version 12 and later versions.

Bypassing indexes will allow you to skip the vacuum process of the inconsistent
index and mitigate the wraparound issue. However, this will not resolve the underlying
invalid page problem. To fully address and resolve the invalid page issue, you will
still need to rebuild the index.

## Exceptionally high transaction rate

In PostgreSQL, high transaction rates can significantly impact autovacuum's performance,
leading to slower cleanup of dead tuples and increased risk of transaction ID wraparound.
You can monitor the transaction rate by measuring the difference in
`max(age(datfrozenxid))` between two time periods, typically per second.
Additionally, you can use the following counter metrics from RDS Performance Insights to
measure the transaction rate (the sum of xact_commit and xact_rollback) which is the total
number of transactions.

| Counter       | Type         | Unit                 | Metric                        |
| ------------- | ------------ | -------------------- | ----------------------------- |
| xact_commit   | Transactions | Commits per second   | db.Transactions.xact_commit   |
| xact_rollback | Transactions | Rollbacks per second | db.Transactions.xact_rollback |

A rapid increase indicates a high transaction load, which can overwhelm autovacuum,
causing bloat, lock contention, and potential performance issues. This can negatively impact
the autovacuum process in a couple of ways:

- **Table Activity:** The specific table being vacuumed
  could be experiencing a high volume of transactions, causing delays.
- **System Resources** The overall system might be
  overloaded, making it difficult for autovacuum to access the necessary resources to
  function efficiently.

Consider the following strategies for allowing autovacuum to operate more effectively
and keep up with its tasks:

1. Reduce the transaction rate if possible. Consider to batch or group similar
   transactions where feasible.
2. Target frequently updated tables with manual `VACUUM FREEZE` operation
   nightly, weekly, or biweekly during off-peak hours.
3. Consider scaling up your instance class to allocate more system resources to handle
   the high transaction volume and autovacuum.
