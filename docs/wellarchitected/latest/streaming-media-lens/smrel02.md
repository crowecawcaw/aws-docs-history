

# Content processing
<a name="smrel02"></a>

Processing transforms ingested content into distribution formats. Failures in encoding or packaging can stop content from reaching viewers or degrade quality. Reliable processing requires redundancy, idempotent workflows, and automatic error recovery.


| SMREL02: How does your streaming workflow provide reliable content processing across encoding, transcoding, and packaging operations? | 
| --- | 
| [SMREL02-BP01 Design processing workflows with redundancy and automatic error recovery](smrel02-bp01.md) | 

## Capability intent
<a name="smrel02-intent"></a>
+ Processing continues without interruption when individual encoding or packaging components fail.
+ Workflows are idempotent and can be safely retried without producing duplicates or corruption.
+ Quality is validated between processing stages.
+ Failed jobs are captured and retried or escalated rather than silently dropped.

## Common issues to watch for
<a name="smrel02-issues"></a>
+ Single-pipeline encoding with no failover for live processing.
+ Non-idempotent workflows that produce duplicates or corruption on retry.
+ No quality validation between stages, allowing degraded output to propagate.
+ No dead letter queues for failed processing jobs.