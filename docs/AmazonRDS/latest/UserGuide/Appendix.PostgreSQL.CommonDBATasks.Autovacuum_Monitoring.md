# Resolving vacuum performance issues in RDS for PostgreSQL

This section discusses factors that often contribute to slower vacuum performance and how
to address these issues.

###### Topics

- [Vacuum large indexes](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Large_indexes "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Large_indexes")
- [Too many tables or databases to vacuum](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Multiple_tables "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Multiple_tables")
- [Aggressive vacuum (to prevent wraparound) is running](#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Aggressive_vacuum "#Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.Aggressive_vacuum")

## Vacuum large indexes

VACUUM operates through sequential phases: initialization, heap scanning, index and heap
vacuuming, index cleanup, heap truncation, and final cleanup. During the heap scan, the
process prunes pages, defragments and freezes them. After completing the heap scan, VACUUM
cleans indexes, returns empty pages to the operating system, and performs final cleanup
tasks like vacuuming the free space map and updating statistics.

Index vacuuming may require multiple passes when `maintenance_work_mem` (or
`autovacuum_work_mem`) is insufficient to process the index. In PostgreSQL 16
and earlier, a 1 GB memory limit for storing dead tuple IDs often forced multiple passes on
large indexes. PostgreSQL 17 introduces `TidStore`, which dynamically allocates
memory instead of using a single-allocation array. This removes the 1 GB constraint, uses
memory more efficiently, and reduces the need for multiple index scans per each
index.

Large indexes may still require multiple passes in PostgreSQL 17 if available memory
can't accommodate the entire index processing at once. Typically, larger indexes contain
more dead tuples that require multiple passes.

**Detecting slow vacuum operations**

The `postgres_get_av_diag()` function can detect when vacuum operations are
running slowly due to insufficient memory. For more information on this function, see [Installing autovacuum monitoring and diagnostic tools in RDS for PostgreSQL](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md").

The `postgres_get_av_diag()` function issues the following notices when the
available memory is not enough to complete the index vacuuming in a single pass.

**`rds_tools` 1.8**

```
NOTICE: Your database is currently running aggressive vacuum to prevent wraparound and it might be slow.
```

```
NOTICE: The current setting of autovacuum_work_mem is "XXX" and might not be sufficient. Consider increasing the setting, and if necessary, scaling up the Amazon RDS instance class for more memory.
        Additionally, review the possibility of manual vacuum with exclusion of indexes using (VACUUM (INDEX_CLEANUP FALSE, VERBOSE TRUE) table_name;).
```

**`rds_tools` 1.9**

```
NOTICE: Your database is currently running aggressive vacuum to prevent wraparound and it might be slow.
```

```
NOTICE: The current setting of autovacuum_work_mem is XX might not be sufficient. Consider increasing the setting to XXX, and if necessary, scaling up the RDS instance class for more
        memory. The suggested value is an estimate based on the current number of dead tuples for the table being vacuumed, which might not fully reflect the latest state. Additionally, review the possibility of manual
        vacuum with exclusion of indexes using (VACUUM (INDEX_CLEANUP FALSE, VERBOSE TRUE) table_name;). For more information, see
        Working with PostgreSQL autovacuum in the Amazon Amazon RDS User Guide
        .
```

###### Note

The `postgres_get_av_diag()` function relies on
`pg_stat_all_tables.n_dead_tup` for estimating the amount of memory required
for index vacuuming.

When the `postgres_get_av_diag()` function identifies a slow vacuum operation
that requires multiple index scans due to insufficient `autovacuum_work_mem`, it
will generate the following message:

```
NOTICE: Your vacuum is performing multiple index scans due to insufficient autovacuum_work_mem:XXX for index vacuuming.
        For more information, see Working with PostgreSQL autovacuum in the Amazon Amazon RDS User Guide.
```

**Guidance**

You can apply the following workarounds using manual `VACUUM FREEZE` to speed
up freezing the table.

**Increase the memory for vacuuming**

As suggested by the `postgres_get_av_diag()` function, it's advisable to
increase the `autovacuum_work_mem` parameter to address potential memory
constraints at the instance level. While `autovacuum_work_mem` is a dynamic
parameter, it's important to note that for the new memory setting to take effect, the
autovacuum daemon needs to restart its workers. To accomplish this:

1. Confirm that the new setting is in place.
2. Terminate the processes currently running autovacuum.

This approach ensures that the adjusted memory allocation is applied to new autovacuum
operations.

For more immediate results, consider manually performing a `VACUUM FREEZE`
operation with an increased `maintenance_work_mem` setting within your
session:

```
SET maintenance_work_mem TO '1GB';
VACUUM FREEZE VERBOSE `table_name`;
```

If you're using Amazon RDS and find that you need additional memory to support higher values
for `maintenance_work_mem` or `autovacuum_work_mem`, consider
upgrading to an instance class with more memory. This can provide the necessary resources to
enhance both manual and automatic vacuum operations, leading to improved overall vacuum and
database performance.

**Disable INDEX_CLEANUP**

Manual `VACUUM` in PostgreSQL version 12 and later allows skipping the index
cleanup phase, while emergency autovacuum in PostgreSQL version 14 and later does this
automatically based on the [`vacuum_failsafe_age`](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-VACUUM-FAILSAFE-AGE "https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-VACUUM-FAILSAFE-AGE") parameter.

###### Warning

Skipping index cleanup can lead to index bloat and negatively impact query
performance. To mitigate this, consider reindexing or vacuuming affected indexes during a
maintenance window.

For additional guidance on handling large indexes, refer to the documentation on [Managing
autovacuum with large indexes](Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum.md") .

**Parallel index vacuuming**

Starting with PostgreSQL 13, indexes can be vacuumed and cleaned in parallel by default
using manual `VACUUM`, with one vacuum worker process assigned to each index.
However, for PostgreSQL to determine if a vacuum operation qualifies for parallel execution,
specific criteria must be met:

- There must be at least two indexes.
- The `max_parallel_maintenance_workers` parameter should be set to at
  least 2.
- The index size must exceed the `min_parallel_index_scan_size` limit,
  which defaults to 512KB.

You can adjust the `max_parallel_maintenance_workers` setting based on the
number of vCPUs available on your Amazon RDS instance and the number of indexes on the table to
optimize vacuuming turnaround time.

For more information, see [Parallel vacuuming in Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL](https://aws.amazon.com/blogs/database/parallel-vacuuming-in-amazon-rds-for-postgresql-and-amazon-aurora-postgresql/ "https://aws.amazon.com/blogs/database/parallel-vacuuming-in-amazon-rds-for-postgresql-and-amazon-aurora-postgresql/").

## Too many tables or databases to vacuum

As mentioned in PostgreSQL's [The
Autovacuum Daemon](https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM' "https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM'") documentation, the autovacuum daemon operates through multiple
processes. This includes a persistent autovacuum launcher responsible for starting
autovacuum worker processes for each database within the system. The launcher schedules
these workers to initiate approximately every `autovacuum_naptime` seconds per
database.

With 'N' databases, a new worker begins roughly every [`autovacuum_naptime`/N
seconds]. However, the total number of concurrent workers is limited by the
`autovacuum_max_workers` setting. If the number of databases or tables
requiring vacuuming exceeds this limit, the next database or table will be processed as soon
as a worker becomes available.

When many large tables or databases require vacuuming concurrently, all available
autovacuum workers can become occupied for an extended duration, delaying maintenance on
other tables and databases. In environments with high transaction rates, this bottleneck can
quickly escalate and potentially lead to wraparound vacuum issues within your Amazon RDS
instance.

When `postgres_get_av_diag()` detects a high number of tables or databases,
it provides the following recommendation:

```
NOTICE: Your database is currently running aggressive vacuum to prevent wraparound and it might be slow.
```

```
NOTICE: The current setting of autovacuum_max_workers:3 might not be sufficient. Consider increasing the setting and, if necessary, consider scaling up the Amazon RDS instance class for more workers.
```

**Guidance**

**Increase autovacuum_max_workers**

To expedite the vacuuming, we recommend adjusting the
`autovacuum_max_workers` parameter to allow more concurrent autovacuum workers.
If performance bottlenecks persist, consider scaling up your Amazon RDS instance to a class with
more vCPUs, which can further improve the parallel processing capabilities.

## Aggressive vacuum (to prevent wraparound) is running

The age of the database (MaximumUsedTransactionIDs) in PostgreSQL only decreases when an
aggressive vacuum (to prevent wraparound) is successfully completed. Until this vacuum
finishes, the age will continue to increase depending on the transaction rate.

The `postgres_get_av_diag()` function generates the following
`NOTICE` when it detects an aggressive vacuum. However, it only triggers this
output after the vacuum has been active for at least two minutes.

```
NOTICE: Your database is currently running aggressive vacuum to prevent wraparound, monitor autovacuum performance.
```

For more information about aggressive vacuum, see [When an
aggressive vacuum is already running](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md "Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md").

You can verify if an aggressive vacuum is in progress with the following query:

```
SELECT
    a.xact_start AS start_time,
    v.datname "database",
    a.query,
    a.wait_event,
    v.pid,
    v.phase,
    v.relid::regclass,
    pg_size_pretty(pg_relation_size(v.relid)) AS heap_size,
    (
        SELECT
            string_agg(pg_size_pretty(pg_relation_size(i.indexrelid)) || ':' || i.indexrelid::regclass || chr(10), ', ')
        FROM
            pg_index i
        WHERE
            i.indrelid = v.relid
    ) AS index_sizes,
    trunc(v.heap_blks_scanned * 100 / NULLIF(v.heap_blks_total, 0)) AS step1_scan_pct,
    v.index_vacuum_count || '/' || (
        SELECT
            count(*)
        FROM
            pg_index i
        WHERE
            i.indrelid = v.relid
    ) AS step2_vacuum_indexes,
    trunc(v.heap_blks_vacuumed * 100 / NULLIF(v.heap_blks_total, 0)) AS step3_vacuum_pct,
    age(CURRENT_TIMESTAMP, a.xact_start) AS total_time_spent_sofar
FROM
    pg_stat_activity a
    INNER JOIN pg_stat_progress_vacuum v ON v.pid = a.pid;
```

You can determine if it's an aggressive vacuum (to prevent wraparound) by checking the
query column in the output. The phrase "to prevent wraparound" indicates that it is an
aggressive vacuum.

```
query                  | autovacuum: VACUUM public.t3 (to prevent wraparound)
```

For example, suppose you have a blocker at transaction age 1 billion and a table
requiring an aggressive vacuum to prevent wraparound at the same transaction age.
Additionally, there's another blocker at transaction age 750 million. After clearing the
blocker at transaction age 1 billion, the transaction age won't immediately drop to 750
million. It will remain high until the table needing the aggressive vacuum or any
transaction with an age over 750 million is completed. During this period, the transaction
age of your PostgreSQL cluster will continue to rise. Once the vacuum process is completed,
the transaction age will drop to 750 million but will start increasing again until further
vacuuming is finished. This cycle will continue as long as these conditions persist, until
the transaction age eventually drops to the level configured for your Amazon RDS instance,
specified by `autovacuum_freeze_max_age`.
