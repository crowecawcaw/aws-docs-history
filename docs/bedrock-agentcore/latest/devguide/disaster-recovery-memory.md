

# Replicating AgentCore Memory across Regions
<a name="disaster-recovery-memory"></a>

Amazon Bedrock AgentCore Memory (AgentCore Memory) keeps its data in one AWS Region, so the standby Region of the [warm standby architecture](disaster-recovery-resiliency.md#architecture-warm-standby) has none of your agent’s memory unless you replicate it. Choose what to replicate, then check it against the requirements for safe failover and failback.

## Understanding AgentCore Memory
<a name="understanding-agentcore-memory"></a>

AgentCore Memory stores two kinds of data, and you copy each one to another Region in a different way.
+  **Short-term memory (STM)** is the raw conversation: messages and tool call data. Your agent saves each turn as an event with the `CreateEvent` API. STM belongs to one session, and you choose how long it’s kept.
+  **Long-term memory (LTM)** holds what’s worth remembering across sessions, such as user preferences, facts, and conversation summaries. Memory strategies extract it from events and store it as records. Each time a record is created, updated, or deleted, AgentCore emits a lifecycle event: `MemoryRecordCreated`, `MemoryRecordUpdated`, or `MemoryRecordDeleted`.

 [Memory record streaming](memory-record-streaming.md) can send these LTM events to a stream. It doesn’t send STM events, so STM replication starts in your application.

## Memory replication choices
<a name="memory-replication-patterns"></a>

You decide separately whether to replicate LTM and STM. Base each decision on two targets. Your recovery point objective (RPO) is how much recent data you can afford to lose. Your recovery time objective (RTO) is how quickly you need to recover.


| Replicate | What the standby agent has after failover | Trade-off | 
| --- | --- | --- | 
| Neither | No preferences, facts, summaries, or conversation history. | Recovery depends only on Runtime failover, because there’s nothing to load. Everything in the primary Memory is unavailable until the primary recovers. | 
| LTM only | Extracted records, including session summaries if you configure a summary strategy. A conversation resumes from what extraction captured, not from its last turn. | Your RPO includes the time to extract records and stream them. | 
| STM only | The raw turns of each replicated session. | Each session reloads its turns before it resumes in the standby, which adds recovery time. | 
| Both | Extracted records and raw turns. | The least data loss, but still not zero. | 

None of these choices copies application task state, such as in-progress workflows or tool calls waiting for results. If that state must survive failover, checkpoint it separately.

### Replicating LTM
<a name="_replicating_ltm"></a>

Turn on Memory record streaming for the primary Memory with `FULL_CONTENT` delivery, so that create and update events include the record’s content. The stream goes to Amazon Kinesis Data Streams, the only destination that streaming supports. Then run a consumer, the Kinesis term for a program that reads a stream, such as a Lambda function. For more information, see [Read data from Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html) in the *Amazon Kinesis Data Streams Developer Guide*. Your consumer repeats each change on a Memory in the standby Region with `BatchCreateMemoryRecords`, `BatchUpdateMemoryRecords`, or `BatchDeleteMemoryRecords`.

To include records that already exist, copy them once:

1. Turn on streaming.

1. Copy the existing records with `BatchCreateMemoryRecords`. To list them all, set `namespacePath` to `/` in `ListMemoryRecords`. For each copy, save its source and standby record IDs where your consumer can find them.

1. Start your consumer from the oldest record in the stream, with logic that skips creates for records that you already copied.

After failover, your standby agent reads LTM with the same APIs it uses in the primary, such as [`RetrieveMemoryRecords`](long-term-retrieve-records.md).

If you can accept a larger LTM loss, you can copy LTM on a schedule instead of streaming it. Export the records with `ListMemoryRecords`, for example to a versioned Amazon S3 bucket with Cross-Region Replication, and restore the latest export into the standby Memory with the same Batch APIs. Your RPO is then at least the time between exports.

### Replicating STM
<a name="_replicating_stm"></a>

To replicate STM, your application writes each turn twice: once to the primary Memory with [CreateEvent](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CreateEvent.html), and once to a Memory in the standby Region. Use the same `actorId`, `sessionId`, `clientToken`, and `eventTimestamp` in both calls. If you also replicate LTM, add `extractionMode=SKIP` to the standby write, so that the standby doesn’t extract the same LTM records again. If each turn waits for the standby write, you lose less data, but each turn takes longer.

After failover, a user’s session continues as a new Runtime session in the standby, and anything the primary session held in process memory or on its file system is unavailable. The conversation survives because Memory, not the Runtime session, stores it under the `actorId` and `sessionId` that your application passed to `CreateEvent`. Build your agent so that, before it answers its first turn in the standby, it calls [ListEvents](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListEvents.html) with the original `actorId` and `sessionId` and rebuilds the model’s conversation history from the returned events.

## Requirements for any implementation
<a name="memory-replication-requirements"></a>

Check your replication code against these requirements.

1.  **Retries don’t duplicate.** Lambda delivers a stream batch again if your consumer fails partway through it, and your application retries a `CreateEvent` call that timed out, even though the first call might have worked. Make every write safe to repeat:
   + For STM, send the same `clientToken` each time you retry a turn.
   + For LTM creates, `BatchCreateMemoryRecords` takes one `clientToken` for the whole call, and AgentCore uses it to avoid creating the same batch twice. If your consumer resends a call, send the same token. So compute it from the stream records that the call carries, such as their source record IDs and event times, not at random.
   + For LTM updates and deletes, the calls take no token. Keep track of the last change that you applied to each record, and skip anything that isn’t newer.

1.  **If updates and deletes must reach the standby, your consumer must be able to locate the standby record.** The standby gives each copied record a new ID, and a delete event carries only the memory and record identifiers. So give your consumer a way to find the standby record for each primary record, such as a table that maps primary record IDs to standby record IDs. Keep the mapping in both directions if you plan to fail back.

1.  **Replicate in one direction at a time.** Each write that your consumer makes creates a new change event in the Memory that it writes to. If both Memories streamed to each other, every change would loop between them.
   + Normally, copy from the primary to the standby.
   + At failover, stop that copy. Your consumer runs in the primary Region, which might be unavailable, so you need a way to stop it from the standby, such as a flag that your consumer checks before each write.
   + At failback, restart it only after the standby’s changes have reached the primary and you’ve stopped copying in the other direction.

1.  **Measure RPO from the oldest change not yet replicated.** Your current RPO is the age of the oldest change that hasn’t reached the standby yet. Compare it with your target RPO. Neither LTM nor STM replication guarantees zero data loss.
   + For LTM, the part you can measure is consumer lag: how far your consumer is behind the stream. Extraction adds delay before a change reaches the stream, so the real gap is larger.
   + By default, a Kinesis data stream keeps records for 24 hours. Set the stream’s [retention period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html) longer than you might need to detect and fix a consumer failure.
   + Some losses don’t show up as lag. Alarm on the Memory’s `StreamPublishingFailure` and `StreamUserError` metrics, which count changes that weren’t published to the stream. Check `failedRecords` in every Batch response, because it lists records that weren’t written even though the call succeeded. Retry them, or save them for review, before your consumer reports the batch as processed.
   + For STM, count the turns that you abandon after retrying. Each one never reaches the standby, and the age of the oldest pending turn doesn’t show it.

1.  **Capture standby writes for failback.** After failover, the standby collects changes that the primary doesn’t have. Before an incident, set up a way to send them back:
   + For LTM, one way is a second stream, on the standby Memory, with a consumer that writes to the primary. Turn it on only at failover. If you turned it on earlier, it would copy the primary’s changes back to the primary. Set that stream’s retention longer than the longest time you might run on the standby, because its changes can’t be applied until the primary recovers.
   + For STM, one way is to write each standby turn to the primary too, and save the writes that fail while the primary is unavailable so that you can resend them. After failover, write to the standby with normal extraction. If you also replicate LTM, add `extractionMode=SKIP` to the writes to the primary, because the standby’s failback stream already carries the extracted records to the primary.

### Use the standby’s strategy IDs
<a name="_use_the_standbys_strategy_ids"></a>

Each Memory generates its own strategy IDs (`memoryStrategyId`), so the same strategy has a different ID in each Region. To account for this:
+ Create the same strategies in both Regions, including any [custom namespace variables](specify-long-term-memory-organization.md) (placeholders in the path-like name under which a strategy stores records).
+ Whenever you write records to the standby, including the one-time copy and any scheduled restore, use the standby’s strategy IDs, not the primary’s.
+ If a namespace template includes `{memoryStrategyId}`, remove that variable, or rewrite that part of each record’s namespace in your consumer.

### Reference implementations
<a name="memory-reference-implementations"></a>

The AWS Labs [agentcore-samples](https://github.com/awslabs/agentcore-samples) repository on the GitHub website has three Memory replication samples:
+  [Multi-Region replication production pattern](https://github.com/awslabs/agentcore-samples/tree/main/01-features/04-manage-context-of-your-agent/memory/06-production-patterns/00-multi-region-replication): LTM streaming and an STM dual write.
+  [Cross-Region replication workshop](https://github.com/awslabs/agentcore-samples/tree/main/06-workshops/04-AgentCore-memory/03-advanced-patterns/06-streaming-for-cross-region-replication): LTM streaming in a CloudFormation notebook.
+  [Record streaming cross-Region example](https://github.com/awslabs/agentcore-samples/tree/main/01-features/04-manage-context-of-your-agent/memory/02-long-term-memory/09-record-streaming/examples/cross-region-replication): LTM streaming.

The samples show how to set up LTM streaming and, in the production pattern, an STM dual write. Check your implementation against the requirements before production. For Runtime failover, including failure detection and routing to the active Region, see [Operating disaster recovery: detection, response, and recovery](disaster-recovery-operate.md).