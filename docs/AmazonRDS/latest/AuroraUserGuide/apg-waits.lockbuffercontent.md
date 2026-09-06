

# LWLock:buffer\_content (BufferContent)
<a name="apg-waits.lockbuffercontent"></a>

The `LWLock:buffer_content` event occurs when a session is waiting to read or write a data page in memory while another session has that page locked for writing. In Aurora PostgreSQL 13 and higher, this wait event is called `BufferContent`.

**Topics**
+ [Supported engine versions](#apg-waits.lockbuffercontent.context.supported)
+ [Context](#apg-waits.lockbuffercontent.context)
+ [Likely causes of increased waits](#apg-waits.lockbuffercontent.causes)
+ [Actions](#apg-waits.lockbuffercontent.actions)

## Supported engine versions
<a name="apg-waits.lockbuffercontent.context.supported"></a>

This wait event information is supported for all versions of Aurora PostgreSQL.

## Context
<a name="apg-waits.lockbuffercontent.context"></a>

To read or manipulate data, PostgreSQL accesses it through shared memory buffers. To read from the buffer, a process gets a lightweight lock (LWLock) on the buffer content in shared mode. To write to the buffer, it gets that lock in exclusive mode. Shared locks allow other processes to concurrently acquire shared locks on that content. Exclusive locks prevent other processes from getting any type of lock on it.

The `LWLock:buffer_content` (`BufferContent`) event indicates that multiple processes are attempting to get lightweight locks (LWLocks) on contents of a specific buffer.

## Likely causes of increased waits
<a name="apg-waits.lockbuffercontent.causes"></a>

When the `LWLock:buffer_content` (`BufferContent`) event appears more than normal, possibly indicating a performance problem, typical causes include the following:

**Increased concurrent updates to the same data**  
There might be an increase in the number of concurrent sessions with queries that update the same buffer content. This contention can be more pronounced on tables with a lot of indexes.

**Workload data is not in memory**  
When data that the active workload is processing is not in memory, these wait events can increase. This effect is because processes holding locks can keep them longer while they perform disk I/O operations.

**Excessive use of foreign key constraints**  
Foreign key constraints can increase the amount of time a process holds onto a buffer content lock. This effect is because read operations require a shared buffer content lock on the referenced key while that key is being updated.

## Actions
<a name="apg-waits.lockbuffercontent.actions"></a>

We recommend different actions depending on the causes of your wait event. You might identify `LWLock:buffer_content` (`BufferContent`) events by using Amazon RDS Performance Insights or by querying the view `pg_stat_activity`.

**Topics**
+ [Improve in-memory efficiency](#apg-waits.lockbuffercontent.actions.in-memory)
+ [Reduce usage of foreign key constraints](#apg-waits.lockbuffercontent.actions.foreignkey)
+ [Remove unused indexes](#apg-waits.lockbuffercontent.actions.indexes)
+ [Remove duplicate indexes](#apg-waits.lockbuffercontent.actions.duplicate-indexes)
+ [Drop or REINDEX invalid indexes](#apg-waits.lockbuffercontent.actions.invalid-indexes)
+ [Use partial indexes](#apg-waits.lockbuffercontent.actions.partial-indexes)
+ [Remove table and index bloat](#apg-waits.lockbuffercontent.actions.bloat)

### Improve in-memory efficiency
<a name="apg-waits.lockbuffercontent.actions.in-memory"></a>

To increase the chance that active workload data is in memory, partition tables or scale up your instance class. For information about DB instance classes, see [Amazon AuroraDB instance classes](Concepts.DBInstanceClass.md).

Monitor the `BufferCacheHitRatio` metric, which measures the percentage of requests served by the buffer cache of a DB instance in your DB cluster. This metric provides insight into the amount of data being served from memory. A high hit ratio indicates that your DB instance has sufficient memory available for your working data set, while a low ratio suggests that your queries are frequently accessing data from storage.

The cache read hit per table and cache read hit per index under Memory setting section of the [PG Collector](https://github.com/awslabs/pg-collector) report can provide insights into the tables and indexes cache hit ratio.

### Reduce usage of foreign key constraints
<a name="apg-waits.lockbuffercontent.actions.foreignkey"></a>

Investigate workloads experiencing high numbers of `LWLock:buffer_content` (`BufferContent`) wait events for usage of foreign key constraints. Remove unnecessary foreign key constraints.

### Remove unused indexes
<a name="apg-waits.lockbuffercontent.actions.indexes"></a>

For workloads experiencing high numbers of `LWLock:buffer_content` (`BufferContent`) wait events, identify unused indexes and remove them.

The unused indexes section of the [PG Collector](https://github.com/awslabs/pg-collector) report can provide insights into the unused indexes in the database.

### Remove duplicate indexes
<a name="apg-waits.lockbuffercontent.actions.duplicate-indexes"></a>

Identify duplicate indexes and remove them.

The duplicate indexes section of the [PG Collector](https://github.com/awslabs/pg-collector) report can provide insights into the duplicate indexes in the database.

### Drop or REINDEX invalid indexes
<a name="apg-waits.lockbuffercontent.actions.invalid-indexes"></a>

Invalid indexes typically occur when using `CREATE INDEX CONCURRENTLY` or `REINDEX CONCURRENTLY` and the command fails or is aborted.

Invalid indexes can't be used for queries, though they will still be updated and take up disk space.

The Invalid indexes section of the [PG Collector](https://github.com/awslabs/pg-collector) report can provide insights into the invalid indexes in the database.

### Use partial indexes
<a name="apg-waits.lockbuffercontent.actions.partial-indexes"></a>

Partial indexes can be leveraged to enhance query performance and reduce index size. A partial index is an index built over a subset of a table, with the subset defined by a conditional expression. As detailed in the [partial index](https://www.postgresql.org/docs/current/indexes-partial.html) documentation, partial indexes can reduce the overhead of maintaining indexes, as PostgreSQL does not need to update the index in all cases.

### Remove table and index bloat
<a name="apg-waits.lockbuffercontent.actions.bloat"></a>

Excessive table and index bloat can negatively impact database performance. Bloated tables and indexes increase the active working set size, degrading in-memory efficiency. Additionally, bloat increases storage costs and slows query execution. To diagnose bloat, refer to the [Diagnosing table and index bloat](AuroraPostgreSQL.diag-table-ind-bloat.md). Further, the Fragmentation (Bloat) section of the [PG Collector](https://github.com/awslabs/pg-collector) report can provide insights into tables and indexes bloat.

To address table and index bloat, there are a few options:

**VACUUM FULL**  
`VACUUM FULL` creates a new copy of the table, copying over only the live tuples, and then replaces the old table with the new one while holding an `ACCESS EXCLUSIVE` lock. This prevents any reading or writing to the table, which can cause an outage. Additionally, `VACUUM FULL` will take longer if the table is large.

**pg\_repack**  
The `pg_repack` is helpful in situations where `VACUUM FULL` might not be suitable. It creates a new table that contains the data of the bloated table, tracks the changes from the original table, and then replaces the original table with the new one. It doesn't lock the original table for read or write operations while it's building the new table. For more information, for how to use `pg_repack`, see [Removing bloat with pg\_repack](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/pg-repack.html) and [pg\_repack](https://reorg.github.io/pg_repack/).

**REINDEX**  
The `REINDEX` command can be leveraged to address index bloat. `REINDEX` writes a new version of the index without the dead pages or the empty or nearly-empty pages, thereby reducing the space consumption of the index. For detailed information about the [`REINDEX`](https://www.postgresql.org/docs/current/sql-reindex.html) command, please refer to the REINDEX documentation.

After removing bloat from tables and indexes, it may be necessary to increase the autovacuum frequency on those tables. Implementing aggressive autovacuum settings at the table level can help prevent future bloat from occurring. For more information, please refer to the documentation on [`Vacuuming and analyzing tables automatically`](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/autovacuum.html).