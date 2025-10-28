# Consistency

In MemoryDB, primary nodes are strongly consistent. Successful write operations are durably stored in a distributed Multi-AZ transactional logs before
returning to clients. Read operations on primaries always return the most up-to-date data reflecting the effects from all prior successful write operations.
Such strong consistency is preserved across primary failovers.

In MemoryDB, replica nodes are eventually consistent. Read operations from replicas (using `READONLY` command)
might not always reflect the effects of the most recent successful write operations, with lag metrics published to CloudWatch.
However, read operations from a single replica are sequentially consistent. Successful write operations take effect on each replica in
the same order they were executed on the primary.
