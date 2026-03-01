# Managing TOAST OID contention in Amazon Aurora PostgreSQL

TOAST (The Oversized-Attribute Storage Technique) is a PostgreSQL feature designed to handle
large data values that exceed the typical 8KB database block size. PostgreSQL doesn't allow
physical rows to span multiple blocks. The block size acts as an upper limit on row size. TOAST
overcomes this restriction by splitting large field values into smaller chunks. It stores them
separately in a dedicated TOAST table linked to the main table. For more information, see the
[PostgreSQL TOAST
storage mechanism and implementation documentation](https://www.postgresql.org/docs/current/storage-toast.html "https://www.postgresql.org/docs/current/storage-toast.html").

###### Topics

- [Understanding TOAST operations](#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.HowWorks "#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.HowWorks")
- [Identifying performance challenges](#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.PerformanceChallenges "#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.PerformanceChallenges")
- [Recommendations](#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.Recommendations "#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.Recommendations")
- [Monitoring](#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.Monitoring "#Appendix.PostgreSQL.CommonDBATasks.TOAST_OID.Monitoring")

## Understanding TOAST operations

TOAST performs compression and stores large field values out of line. TOAST assigns a
unique OID (Object Identifier) to each chunk of oversized data stored in the TOAST table. The
main table stores the TOAST value ID and relation ID on the page to reference the
corresponding row in the TOAST table. This allows PostgreSQL to efficiently locate and manage
these TOAST chunks. However, as the TOAST table grows, the system risks exhausting available
OIDs, leading to both performance degradation and potential downtime due to OID
depletion.

### Object identifiers in TOAST

An Object Identifier (OID) is a system-wide unique identifier used by PostgreSQL to
reference database objects like tables, indexes, and functions. These identifiers play a
vital role in PostgreSQL's internal operations, allowing the database to efficiently locate
and manage objects.

For tables with eligible data sets for toasting, PostgreSQL assigns OIDs to uniquely
identify each chunk of oversized data stored in the associated TOAST table. The system
associates each chunk with a `chunk_id`, which helps PostgreSQL organize and
locate these chunks efficiently within the TOAST table.

## Identifying performance challenges

PostgreSQL's OID management relies on a global 32-bit counter so that it wraps around
after generating 4 billion unique values. While the database cluster shares this counter, OID
allocation involves two steps during TOAST operations:

- Global counter for allocation – The global
  counter assigns a new OID across the cluster.
- Local search for conflicts – The TOAST table
  ensures the new OID does not conflict with existing OIDs already used in that specific
  table.

Performance degradation can occur when:

- The TOAST table has high fragmentation or dense OID usage, leading to delays in
  assigning the OID.
- The system frequently allocates and reuses OIDs in environments with high data churn
  or wide tables that use TOAST extensively.

For more information, see the [PostgreSQL TOAST table
size limits and OID allocation documentation](https://wiki.postgresql.org/wiki/TOAST#Total_table_size_limit "https://wiki.postgresql.org/wiki/TOAST#Total_table_size_limit"):

A global counter generates the OIDs and wraps around every 4 billion values, so that from
time to time, the system generates an already-used value again. PostgreSQL detects that and
tries again with the next OID. A slow INSERT could occur if there is a very long run of used
OID values with no gaps in the TOAST table. These challenges become more pronounced as the OID
space fills, leading to slower inserts and updates.

### Identifying the problem

- Simple `INSERT` statements take significantly longer than usual in an
  inconsistent and random manner.
- Delays occur only for `INSERT` and `UPDATE` statements
  involving TOAST operations.
- The following log entries appear in PostgreSQL logs when the system struggles to
  find available OIDs in TOAST tables:

```
LOG: still searching for an unused OID in relation "pg_toast_20815"
DETAIL: OID candidates have been checked 1000000 times, but no unused OID has been found yet.
```

- Performance Insights indicates a high number of average active sessions (AAS)
  associated with `LWLock:buffer_io` and `LWLock:OidGenLock` wait
  events.

You can run the following SQL query to identify long-running INSERT transactions
with wait events:

```
SELECT
    datname AS database_name,
    usename AS database_user,
    pid,
    now() - pg_stat_activity.xact_start AS transaction_duration,
    concat(wait_event_type, ':', wait_event) AS wait_event,
    substr(query, 1, 30) AS TRANSACTION,
    state
FROM
    pg_stat_activity
WHERE (now() - pg_stat_activity.xact_start) > INTERVAL '60 seconds'
    AND state IN ('active', 'idle in transaction', 'idle in transaction (aborted)', 'fastpath function call', 'disabled')
    AND pid <> pg_backend_pid()
AND lower(query) LIKE '%insert%'
ORDER BY
    transaction_duration DESC;
```

Example query results displaying INSERT operations with extended wait times:

```
 database_name |  database_user  |  pid  | transaction_duration |     wait_event      |          transaction           | state
---------------+-----------------+-------+----------------------+---------------------+--------------------------------+--------
 postgres       | db_admin_user| 70965 | 00:10:19.484061      | LWLock:buffer_io    | INSERT INTO "products" (......... | active
 postgres       | db_admin_user| 69878 | 00:06:14.976037      | LWLock:buffer_io    | INSERT INTO "products" (......... | active
 postgres       | db_admin_user| 68937 | 00:05:13.942847      | :                   | INSERT INTO "products" (......... | active
```

### Isolating the problem

- Test small insert – Insert a record smaller
  than the `toast_tuple_target` threshold. Remember that compression is applied
  before TOAST storage. If this operates without performance issues, the problem is
  related to TOAST operations.
- Test new table – Create a new table with the
  same structure and insert a record larger than `toast_tuple_target`. If this
  works without issues, the problem is localized to the original table's OID
  allocation.

## Recommendations

The following approaches can help resolve TOAST OID contention issues.

- Data cleanup and archive – Review and delete any
  obsolete or unnecessary data to free up OIDs for future use, or archive the data. Consider
  the following limitations:
  - Limited scalability, as future cleanup might not always be possible.
  - Possible long-running VACUUM operation to remove the resulting dead tuples.

- Write to a new table – Create a new table for
  future inserts and use a `UNION ALL` view to combine old and new data for
  queries. This view presents the combined data from both old and new tables, allowing
  queries to access them as a single table. Consider the following limitations:
  - Updates on the old table might still cause OID exhaustion.

- Partition or Shard – Partition the table or
  shard data for better scalability and performance. Consider the following
  limitations:
  - Increased complexity in query logic and maintenance, potential need for
    application changes to handle partitioned data correctly.

## Monitoring

### Using system tables

You can use PostgreSQL's system tables to monitor growth of OID usage.

###### Warning

Depending on the number of OIDs in the TOAST table, it may take time to complete. We
recommend that you schedule monitoring during off-business hours to minimize
impact.

The following anonymous block counts the number of distinct OIDs used in each TOAST
table and displays the parent table information:

```
DO $$
DECLARE
    r record;
    o bigint;
    parent_table text;
    parent_schema text;
BEGIN
    SET LOCAL client_min_messages TO notice;
    FOR r IN
    SELECT
        c.oid,
        c.oid::regclass AS toast_table
    FROM
        pg_class c
    WHERE
        c.relkind = 't'
        AND c.relowner != 10 LOOP
            -- Fetch the number of distinct used OIDs (chunk IDs) from the TOAST table
            EXECUTE 'SELECT COUNT(DISTINCT chunk_id) FROM ' || r.toast_table INTO o;
            -- If there are used OIDs, find the associated parent table and its schema
            IF o <> 0 THEN
                SELECT
                    n.nspname,
                    c.relname INTO parent_schema,
                    parent_table
                FROM
                    pg_class c
                    JOIN pg_namespace n ON c.relnamespace = n.oid
                WHERE
                    c.reltoastrelid = r.oid;
                -- Raise a concise NOTICE message
                RAISE NOTICE 'Parent schema: % | Parent table: % | Toast table: % | Number of used OIDs: %', parent_schema, parent_table, r.toast_table, TO_CHAR(o, 'FM9,999,999,999,999');
            END IF;
        END LOOP;
END
$$;
```

Example output displaying OID usage statistics by TOAST table:

```
NOTICE:  Parent schema: public | Parent table: my_table | Toast table: pg_toast.pg_toast_16559 | Number of used OIDs: 45,623,317
NOTICE:  Parent schema: public | Parent table: my_table1 | Toast table: pg_toast.pg_toast_45639925 | Number of used OIDs: 10,000
NOTICE:  Parent schema: public | Parent table: my_table2 | Toast table: pg_toast.pg_toast_45649931 | Number of used OIDs: 1,000,000
DO
```

The following anonymous block retrieves the maximum assigned OID for each non-empty
TOAST table:

```
DO $$
DECLARE
    r record;
    o bigint;
    parent_table text;
    parent_schema text;
BEGIN
    SET LOCAL client_min_messages TO notice;
    FOR r IN
    SELECT
        c.oid,
        c.oid::regclass AS toast_table
    FROM
        pg_class c
    WHERE
        c.relkind = 't'
        AND c.relowner != 10 LOOP
            -- Fetch the max(chunk_id) from the TOAST table
            EXECUTE 'SELECT max(chunk_id) FROM ' || r.toast_table INTO o;
            -- If there's at least one TOASTed chunk, find the associated parent table and its schema
            IF o IS NOT NULL THEN
                SELECT
                    n.nspname,
                    c.relname INTO parent_schema,
                    parent_table
                FROM
                    pg_class c
                    JOIN pg_namespace n ON c.relnamespace = n.oid
                WHERE
                    c.reltoastrelid = r.oid;
                -- Raise a concise NOTICE message
                RAISE NOTICE 'Parent schema: % | Parent table: % | Toast table: % | Max chunk_id: %', parent_schema, parent_table, r.toast_table, TO_CHAR(o, 'FM9,999,999,999,999');
            END IF;
        END LOOP;
END
$$;
```

Example output displaying maximum chunk IDs for TOAST tables:

```

NOTICE:  Parent schema: public | Parent table: my_table | Toast table: pg_toast.pg_toast_16559 | Max chunk_id: 45,639,907
NOTICE:  Parent schema: public | Parent table: my_table1 | Toast table: pg_toast.pg_toast_45639925 | Max chunk_id: 45,649,929
NOTICE:  Parent schema: public | Parent table: my_table2 | Toast table: pg_toast.pg_toast_45649931 | Max chunk_id: 46,649,935
DO
```

### Using Performance Insights

The wait events `LWLock:buffer_io` and `LWLock:OidGenLock` appear
in Performance Insights during operations that require assigning new Object Identifiers
(OIDs). High Average Active Sessions (AAS) for these events typically point to contention
during OID assignment and resource management. This is particularly common in environments
with high data churn, extensive large data usage, or frequent object creation.

#### LWLock:buffer_io

`LWLock:buffer_io` is a wait event that occurs when a PostgreSQL session is
waiting for I/O operations on a shared buffer to complete. This typically happens when the
database reads data from disk into memory or writes modified pages from memory to disk.
The `BufferIO` wait event ensures consistency by preventing multiple processes
from accessing or modifying the same buffer while I/O operations are in progress. High
occurrences of this wait event may indicate disk bottlenecks or excessive I/O activity in
the database workload.

During TOAST operations:

- PostgreSQL allocates OIDs for large objects and ensures their uniqueness by
  scanning the TOAST table's index.
- Large TOAST indexes may require accessing multiple pages to verify OID uniqueness.
  This results in increased disk I/O, especially when the buffer pool cannot cache all
  required pages.

The size of the index directly affects the number of buffer pages that need to be
accessed during these operations. Even if the index is not bloated, its sheer size can
increase buffer I/O, particularly in high-concurrency or high-churn environments. For more
information, see [LWLock:BufferIO wait event troubleshooting guide](apg-waits.md "apg-waits.md").

#### LWLock:OidGenLock

`OidGenLock` is a wait event that occurs when a PostgreSQL session is
waiting to allocate a new object identifier (OID). This lock ensures that OIDs are
generated sequentially and safely, allowing only one process to generate OIDs at a
time.

During TOAST operations:

- OID allocation for chunks in TOAST table –
  PostgreSQL assigns OIDs to chunks in TOAST tables when managing large data records.
  Each OID must be unique to prevent conflicts in the system catalog.
- High concurrency – Since access to OID
  generator is sequential, when multiple sessions are concurrently creating objects that
  require OIDs, contention for `OidGenLock` can occur. This increases the
  likelihood of sessions waiting for OID allocation to complete.
- Dependency on system catalog access –
  Allocating OIDs requires updates to shared system catalog tables like
  `pg_class` and `pg_type`. If these tables experience heavy
  activity (due to frequent DDL operations), it can increase lock contention for
  `OidGenLock`.
- High OID allocation demand – TOAST heavy
  workloads with large data records require constant OID allocation, increasing
  contention.

Additional factors that increase OID contention:

- Frequent object creation – Workloads that
  frequently create and drop objects, such as temporary tables, amplify contention on
  the global OID counter.
- Global counter locking – The global OID
  counter is accessed serially to ensure uniqueness, creating a single point of
  contention in high-concurrency environments.
