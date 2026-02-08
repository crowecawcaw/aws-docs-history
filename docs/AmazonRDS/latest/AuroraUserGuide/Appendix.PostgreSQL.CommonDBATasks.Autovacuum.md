# Managing

autovacuum with large indexes

As part of its operation, _autovacuum_ performs several [vacuum phases](https://www.postgresql.org/docs/current/progress-reporting.html#VACUUM-PHASES "https://www.postgresql.org/docs/current/progress-reporting.html#VACUUM-PHASES") while running on a table. Before the table is cleaned up, all of
its indexes are first vacuumed. When removing multiple large indexes, this phase consumes a
significant amount of time and resources. Therefore, as a best practice, be sure to control
the number of indexes on a table and eliminate unused indexes.

For this process, first check the overall index size. Then, determine if there are
potentially unused indexes that can be removed as shown in the following examples.

**To check the size of the table and its indexes**

```
postgres=> select pg_size_pretty(pg_relation_size('pgbench_accounts'));
`pg_size_pretty
6404 MB
(1 row)`
```

```
postgres=> select pg_size_pretty(pg_indexes_size('pgbench_accounts'));
`pg_size_pretty
11 GB
(1 row)`
```

In this example, the size of indexes is larger than the table. This difference can cause
performance issues as the indexes are bloated or unused, which impacts the autovacuum as
well as insert operations.

**To check for unused indexes**

Using the [`pg_stat_user_indexes`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-INDEXES-VIEW "https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-ALL-INDEXES-VIEW") view, you can check how frequently an index is
used with the `idx_scan` column. In the following example, the unused indexes
have the `idx_scan` value of `0`.

```
postgres=> select * from pg_stat_user_indexes where relname = 'pgbench_accounts' order by idx_scan desc;
    `relid | indexrelid | schemaname | relname | indexrelname | idx_scan | idx_tup_read | idx_tup_fetch
-------+------------+------------+------------------+-----------------------+----------+--------------+---------------
16433 | 16454 | public | pgbench_accounts | index_f | 6 | 6 | 0
16433 | 16450 | public | pgbench_accounts | index_b | 3 | 199999 | 0
16433 | 16447 | public | pgbench_accounts | pgbench_accounts_pkey | 0 | 0 | 0
16433 | 16452 | public | pgbench_accounts | index_d | 0 | 0 | 0
16433 | 16453 | public | pgbench_accounts | index_e | 0 | 0 | 0
16433 | 16451 | public | pgbench_accounts | index_c | 0 | 0 | 0
16433 | 16449 | public | pgbench_accounts | index_a | 0 | 0 | 0
(7 rows)`
```

```
postgres=> select schemaname, relname, indexrelname, idx_scan from pg_stat_user_indexes where relname = 'pgbench_accounts' order by idx_scan desc;
    `schemaname | relname | indexrelname | idx_scan
------------+------------------+-----------------------+----------
public | pgbench_accounts | index_f | 6
public | pgbench_accounts | index_b | 3
public | pgbench_accounts | pgbench_accounts_pkey | 0
public | pgbench_accounts | index_d | 0
public | pgbench_accounts | index_e | 0
public | pgbench_accounts | index_c | 0
public | pgbench_accounts | index_a | 0
(7 rows)`
```

###### Note

These statistics are incremental from the time that the statistics are reset. Suppose
you have an index that is only used at the end of a business quarter or just for a
specific report. It's possible that this index hasn't been used since the statistics
were reset. For more information, see [Statistics Functions](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-FUNCTIONS "https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-STATS-FUNCTIONS"). Indexes that are used to enforce uniqueness won't
have scans performed and shouldn't be identified as unused indexes. To identify the
unused indexes, you should have in-depth knowledge of the application and its
queries.

To check when the stats were last reset for a database, use [`pg_stat_database`](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW " https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-DATABASE-VIEW")

```
postgres=> select datname, stats_reset from pg_stat_database where datname = 'postgres';
    `datname | stats_reset
----------+-------------------------------
postgres | 2022-11-17 08:58:11.427224+00
(1 row)`
```

## Vacuuming a table as quickly as possible

**RDS for PostgreSQL 12 and higher**

If you have too many indexes in a large table, your DB instance could be nearing
transaction ID wraparound (XID), which is when the XID counter wraps around to zero.
Left unchecked, this situation could result in data loss. However, you can quickly
vacuum the table without cleaning up the indexes. In RDS for PostgreSQL 12 and higher, you
can use VACUUM with the [`INDEX_CLEANUP`](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html") clause.

```
postgres=> VACUUM (INDEX_CLEANUP FALSE, VERBOSE TRUE) pgbench_accounts;
        `INFO: vacuuming "public.pgbench_accounts"
INFO: table "pgbench_accounts": found 0 removable, 8 nonremovable row versions in 1 out of 819673 pages
DETAIL: 0 dead row versions cannot be removed yet, oldest xmin: 7517
Skipped 0 pages due to buffer pins, 0 frozen pages.
CPU: user: 0.01 s, system: 0.00 s, elapsed: 0.01 s.`
```

If an autovacuum session is already running, you must terminate it to begin the manual
VACUUM. For information on performing a manual vacuum freeze, see [Performing a
manual vacuum freeze](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md")

###### Note

Skipping index cleanup regularly causes index bloat, which degrades scan
performance. The index retains dead rows, and the table retains dead line pointers.
As a result, `pg_stat_all_tables.n_dead_tup` increases until autovacuum
or a manual VACUUM with index cleanup runs. As a best practice, use this procedure
only to prevent transaction ID wraparound.

**RDS for PostgreSQL 11 and older**

However, in RDS for PostgreSQL 11 and lower versions, the only way to allow vacuum to
complete faster is to reduce the number of indexes on a table. Dropping an index can
affect query plans. We recommend that you drop unused indexes first, then drop the
indexes when XID wraparound is very near. After the vacuum process completes, you can
recreate these indexes.
