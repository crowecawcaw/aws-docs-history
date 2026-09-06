

# Consistency
<a name="Durability.Consistency"></a>

**Synchronous writes**

Primary nodes are strongly consistent. Successful write operations are durably stored in the Multi-AZ transactional log before returning to clients. During normal operations, read operations on primaries always return the most up-to-date data reflecting the effects from all prior successful write operations. Such strong consistency is preserved across primary failovers. Replica nodes are eventually consistent. Read operations from replicas (using `READONLY` command) might not always reflect the effects of the most recent successful write operations, with lag metrics published to CloudWatch. The read operations from a single replica are sequentially consistent. Successful write operations take effect on each replica in the same order they were executed on the primary.

**Asynchronous writes**

During normal operation, asynchronous writes provide the same consistency behavior as synchronous writes. However, as the write operations are returned to clients before being durably stored in the Multi-AZ transactional log, strong consistency is not preserved across primary failovers. In the event of a failure, up to 10 seconds of acknowledged write operations may be lost, meaning that after a failover, read operations on the new primary may not reflect all previously acknowledged writes. Asynchronous writes is not recommended for workloads that require strong consistency guarantees.