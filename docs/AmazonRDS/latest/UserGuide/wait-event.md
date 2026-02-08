# LWLock:buffer_content (BufferContent)

The `LWLock:buffer_content` event occurs when a session is waiting to read or write a data
page in memory while another session has that page locked for writing. In RDS for PostgreSQL 13 and higher,
this wait event is called `BufferContent`.

###### Topics

- [Supported engine versions](#wait-event.lwlockbuffercontent.context.supported "#wait-event.lwlockbuffercontent.context.supported")
- [Context](#wait-event.lwlockbuffercontent.context "#wait-event.lwlockbuffercontent.context")
- [Likely causes of increased waits](#wait-event.lwlockbuffercontent.causes "#wait-event.lwlockbuffercontent.causes")
- [Actions](#wait-event.lwlockbuffercontent.actions "#wait-event.lwlockbuffercontent.actions")

## Supported engine versions

This wait event information is supported for all versions of RDS for PostgreSQL.

## Context

To read or manipulate data, PostgreSQL accesses it through shared memory
buffers. To read from the buffer, a process gets a lightweight lock (LWLock) on the
buffer content in shared mode. To write to the buffer, it gets that lock in exclusive
mode. Shared locks allow other processes to concurrently acquire shared locks on that
content. Exclusive locks prevent other processes from getting any type of lock on
it.

The `LWLock:buffer_content` (`BufferContent`) event
indicates that multiple processes are attempting to get a lock on contents of a specific
buffer.

## Likely causes of increased waits

When the `LWLock:buffer_content` (`BufferContent`) event appears more than normal,
possibly indicating a performance problem, typical causes include the following:

**Increased concurrent updates to the same data**

There might be an increase in the number of concurrent sessions with queries that update the same buffer content. This contention can be more pronounced on tables with a lot of indexes.

**Workload data is not in memory**

When data that the active workload is processing is not in memory,
these wait events can increase. This effect is because processes holding
locks can keep them longer while they perform disk I/O operations.

**Excessive use of foreign key constraints**

Foreign key constraints can increase the amount of time a process
holds onto a buffer content lock. This effect is because read operations
require a shared buffer content lock on the referenced key while that key is
being updated.

## Actions

We recommend different actions depending on the causes of your wait event. You might identify
`LWLock:buffer_content` (`BufferContent`) events by using Amazon RDS Performance
Insights or by querying the view `pg_stat_activity`.

###### Topics

- [Improve in-memory efficiency](#wait-event.lwlockbuffercontent.actions.in-memory "#wait-event.lwlockbuffercontent.actions.in-memory")
- [Reduce usage of foreign key constraints](#wait-event.lwlockbuffercontent.actions.foreignkey "#wait-event.lwlockbuffercontent.actions.foreignkey")
- [Remove unused indexes](#wait-event.lwlockbuffercontent.actions.indexes "#wait-event.lwlockbuffercontent.actions.indexes")
- [Increase the cache size when using sequences](#wait-event.lwlockbuffercontent.actions.sequences "#wait-event.lwlockbuffercontent.actions.sequences")

### Improve in-memory efficiency

To increase the chance that active workload data is in memory, partition tables or scale up your instance class. For information about DB instance classes, see [DB instance classes](Concepts.md "Concepts.md").

### Reduce usage of foreign key constraints

Investigate workloads experiencing high numbers of `LWLock:buffer_content` (`BufferContent`)
wait events for usage of foreign key constraints. Remove unnecessary foreign key constraints.

### Remove unused indexes

For workloads experiencing high numbers of `LWLock:buffer_content`
(`BufferContent`) wait events, identify unused indexes and remove them.

### Increase the cache size when using sequences

If your tables uses sequences, increase the cache size to remove contention on sequence pages and index pages. Each sequence is a single page in shared memory.
The pre-defined cache is per connection. This might not be enough to handle
the workload when many concurrent sessions are getting a sequence value.
