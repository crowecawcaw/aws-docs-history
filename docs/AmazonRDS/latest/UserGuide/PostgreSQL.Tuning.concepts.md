# RDS for PostgreSQL memory

RDS for PostgreSQL memory is divided into shared and local.

###### Topics

- [Shared memory in RDS for PostgreSQL](#PostgreSQL.Tuning.concepts.shared "#PostgreSQL.Tuning.concepts.shared")
- [Local memory in RDS for PostgreSQL](#PostgreSQL.Tuning.concepts.local "#PostgreSQL.Tuning.concepts.local")

## Shared memory in RDS for PostgreSQL

RDS for PostgreSQL allocates shared memory when the instance starts. Shared memory
is divided into multiple subareas. The following sections provide descriptions
of the most important ones.

###### Topics

- [Shared buffers](#PostgreSQL.Tuning.concepts.buffer-pool "#PostgreSQL.Tuning.concepts.buffer-pool")
- [Write ahead log (WAL) buffers](#PostgreSQL.Tuning.concepts.WAL "#PostgreSQL.Tuning.concepts.WAL")

### Shared buffers

The _shared buffer pool_ is an RDS for PostgreSQL memory
area that holds all pages that are or were being used by application
connections. A _page_ is the memory version of a disk
block. The shared buffer pool caches the data blocks read from disk. The
pool reduces the need to reread data from disk, making the database operate
more efficiently.

Every table and index is stored as an array of pages of a fixed size. Each
block contains multiple tuples, which correspond to rows. A tuple can be
stored in any page.

The shared buffer pool has finite memory. If a new request requires a page
that isn't in memory, and no more memory exists, RDS for PostgreSQL evicts a less
frequently used page to accommodate the request. The eviction policy is
implemented by a clock sweep algorithm.

The `shared_buffers` parameter determines how much memory the
server dedicates to caching data. The default value is set to
`{DBInstanceClassMemory/32768}` bytes, based on the available
memory for the DB instance.

### Write ahead log (WAL) buffers

A _write-ahead log (WAL) buffer_ holds transaction data
that RDS for PostgreSQL later writes to persistent storage. Using the WAL
mechanism, RDS for PostgreSQL can do the following:

- Recover data after a failure
- Reduce disk I/O by avoiding frequent writes to disk

When a client changes data, RDS for PostgreSQL writes the changes to the WAL
buffer. When the client issues a `COMMIT`, the WAL writer process
writes transaction data to the WAL file.

The `wal_level` parameter determines how much information is
written to the WAL, with possible values such as `minimal`,
`replica`, and `logical`.

## Local memory in RDS for PostgreSQL

Every backend process allocates local memory for query processing.

###### Topics

- [Work memory area](#PostgreSQL.Tuning.concepts.local.work_mem "#PostgreSQL.Tuning.concepts.local.work_mem")
- [Maintenance work memory area](#PostgreSQL.Tuning.concepts.local.maintenance_work_mem "#PostgreSQL.Tuning.concepts.local.maintenance_work_mem")
- [Temporary buffer area](#PostgreSQL.Tuning.concepts.temp "#PostgreSQL.Tuning.concepts.temp")

### Work memory area

The _work memory area_ holds temporary data for queries
that performs sorts and hashes. For example, a query with an `ORDER
 BY` clause performs a sort. Queries use hash tables in hash joins
and aggregations.

The `work_mem` parameter the amount of memory to be used by
internal sort operations and hash tables before writing to temporary disk
files, measured in megabytes. The default value is 4 MB. Multiple sessions
can run simultaneously, and each session can run maintenance operations in
parallel. For this reason, the total work memory used can be multiples of
the `work_mem` setting.

### Maintenance work memory area

The _maintenance work memory area_ caches data for
maintenance operations. These operations include vacuuming, creating an
index, and adding foreign keys.

The `maintenance_work_mem` parameter specifies the maximum
amount of memory to be used by maintenance operations, measured in
megabytes. The default value is 64 MB. A database session can only run one
maintenance operation at a time.

### Temporary buffer area

The _temporary buffer area_ caches temporary tables for
each database session.

Each session allocates temporary buffers as needed up to the limit you
specify. When the session ends, the server clears the buffers.

The `temp_buffers` parameter sets the maximum number of
temporary buffers used by each session, measured in megabytes. The default
value is 8 MB. Before the first use of temporary tables within a session,
you can change the `temp_buffers` value.
