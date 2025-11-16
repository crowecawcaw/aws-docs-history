# LWLock:BufferIO (IPC:BufferIO)

The `LWLock:BufferIO` event occurs when Aurora PostgreSQL or RDS for PostgreSQL is waiting for other processes to
finish their input/output (I/O) operations when concurrently trying to access a page. Its
purpose is for the same page to be read into the shared buffer.

###### Topics

- [Relevant engine versions](#apg-waits.lwlockbufferio.context.supported "#apg-waits.lwlockbufferio.context.supported")
- [Context](#apg-waits.lwlockbufferio.context "#apg-waits.lwlockbufferio.context")
- [Causes](#apg-waits.lwlockbufferio.causes "#apg-waits.lwlockbufferio.causes")
- [Actions](#apg-waits.lwlockbufferio.actions "#apg-waits.lwlockbufferio.actions")

## Relevant engine versions

This wait event information is relevant for all Aurora PostgreSQL versions. For Aurora PostgreSQL
12 and earlier versions this wait event is named as lwlock:buffer_io whereas in Aurora PostgreSQL
13 version it is named as lwlock:bufferio. From Aurora PostgreSQL 14 version BufferIO wait event
moved from `LWLock` to `IPC` wait event type (IPC:BufferIO).

## Context

Each shared buffer has an I/O lock that is associated with the `LWLock:BufferIO` wait event, each time a block (or
a page) has to be retrieved outside the shared buffer pool.

This lock is used to handle multiple sessions that all require access to the same
block. This block has to be read from outside the shared buffer pool, defined by the
`shared_buffers` parameter.

As soon as the page is read inside the shared buffer pool, the `LWLock:BufferIO` lock is released.

###### Note

The `LWLock:BufferIO` wait event precedes the [IO:DataFileRead](apg-waits.md "apg-waits.md") wait event. The `IO:DataFileRead` wait event occurs while data is
being read from storage.

For more information on lightweight locks, see [Locking Overview](https://github.com/postgres/postgres/blob/65dc30ced64cd17f3800ff1b73ab1d358e92efd8/src/backend/storage/lmgr/README#L20 "https://github.com/postgres/postgres/blob/65dc30ced64cd17f3800ff1b73ab1d358e92efd8/src/backend/storage/lmgr/README#L20").

## Causes

Common causes for the `LWLock:BufferIO` event to appear in top waits include the following:

- Multiple backends or connections trying to access the same page that's
  also pending an I/O operation
- The ratio between the size of the shared buffer pool (defined by the `shared_buffers` parameter) and the
  number of buffers needed by the current workload
- The size of the shared buffer pool not being well balanced with the number of pages being evicted by other
  operations
- Large or bloated indexes that require the engine to read more pages than necessary into the shared buffer pool
- Lack of indexes that forces the DB engine to read more pages from the tables than necessary
- Sudden spikes for database connections trying to perform operations on the same page

## Actions

We recommend different actions depending on the causes of your wait event:

- Observe Amazon CloudWatch metrics for correlation between sharp decreases in the
  `BufferCacheHitRatio` and `LWLock:BufferIO` wait
  events. This effect can mean that you have a small shared buffers setting. You
  might need to increase it or scale up your DB instance class. You can split your
  workload into more reader nodes.
- Verify whether you have unused indexes, then remove them.
- Use partitioned tables (which also have partitioned indexes). Doing this helps
  to keep index reordering low and reduces its impact.
- Avoid indexing columns unnecessarily.
- Prevent sudden database connection spikes by using a connection pool.
- Restrict the maximum number of connections to the database as a best practice.
