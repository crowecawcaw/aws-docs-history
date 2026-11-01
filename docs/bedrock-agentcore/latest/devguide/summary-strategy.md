

# Summary strategy
<a name="summary-strategy"></a>

The `SummaryStrategy` is responsible for generating condensed, real-time summaries of conversations within a single session. It captures key topics, main tasks, and decisions, providing a high-level overview of the dialogue.

 **Steps in the strategy** 

The summary strategy includes the following steps:
+  **Consolidation** – Determines whether to write useful information to a new record or an existing record.

 **Strategy output** 

The summary strategy returns XML-formatted output, where each `<topic>` tag represents a distinct area of the user’s memory. XML lets multiple topics to be captured and organized in a single summary while preserving clarity.

The summary strategy produces two types of output for each session: summary chunks and a full session summary. For more information, see [Summary chunks](#summary-strategy-summary-chunks) and [Full session summary](#summary-strategy-full-session-summary).

 **Examples of insights captured by this strategy include:** 
+ A summary of a support interaction, such as "The user reported an issue with order \#XYZ-123 , and the agent initiated a replacement."
+ The outcome of a planning session, like "The team agreed to move the project deadline to Friday."

By referencing this summary, an agent can quickly recall the context of a long or complex conversation without needing to re-process the entire history. This is essential for maintaining conversational flow and for efficiently managing the context window of the foundation model.

 **Default namespace** 

 `/strategy/{memoryStrategyId}/actor/{actorId}/session/{sessionId}/` 

**Note**  
 `sessionId` is a required parameter for summary namespace since summaries are generated and maintained at session level.

## Summary chunks
<a name="summary-strategy-summary-chunks"></a>

A single session can have multiple summary chunks, each representing a portion of the conversation. AgentCore Memory creates a new chunk each time it processes a new set of events from the session. Each chunk is a compacted version of only the events in that set. AgentCore Memory gives the model the earlier summaries of the session as context, so a new chunk doesn’t repeat details that an earlier chunk already captured. AgentCore Memory doesn’t rewrite earlier chunks or merge topics across chunks. If the conversation returns to a topic in a later set of events, the later chunk contains a new `<topic>` entry for that topic with only the new details. The chunks read in order as a running record of the conversation, not as one summary that groups everything about a topic together. To get a single recap of the whole session, use the full session summary. For more information, see [Full session summary](#summary-strategy-full-session-summary).

To retrieve the summary chunks for a session, use the [ListMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryRecords.html) operation with the session’s namespace. To retrieve only the summary chunks that are relevant to a query, use the [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html) operation to run a semantic search over them.

## Full session summary
<a name="summary-strategy-full-session-summary"></a>

In addition to summary chunks, the summary strategy maintains a full session summary for each session. The full session summary recaps the entire session in a single, running record. As new events arrive, AgentCore Memory folds each new summary chunk into the existing recap. The record always reflects the conversation so far.

The following table describes the different purposes of summary chunks and the full session summary.


| Output | What it covers | Use it to | 
| --- | --- | --- | 
| Summary chunks | A portion of the conversation. AgentCore Memory produces a new chunk as the conversation progresses. A topic that the conversation returns to can appear in more than one chunk. | Retrieve only the parts of a session that are relevant to a query. | 
| Full session summary | The whole session, in a single record that AgentCore Memory updates as the session continues. | Give your agent the complete context of a session in one record, without assembling the chunks yourself. | 

AgentCore Memory stores the full session summary as a long-term memory record with a `memoryRecordType` of `FULL_SESSION`, in the same namespace as the session’s summary chunks. Every memory that has a summary strategy produces full session summaries, with no separate setting. AgentCore Memory also creates full session summaries for sessions that it summarized before this capability was available.

A model generates the full session summary and updates it as the session continues, so its content changes over the life of the session. To get the latest recap, read the record again after you add new events.

### Retrieve the full session summary
<a name="summary-strategy-full-session-summary-retrieve"></a>

To retrieve full session summaries, use the same operations that you use for other memory records: [GetMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetMemoryRecord.html), [ListMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryRecords.html), and [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html). No additional operations are required.

To return only full session summaries, filter on the system-generated `x-amz-agentcore-memory-recordType` metadata key. You don’t need to declare this key as an indexed key. For more information, see [Structured metadata for long-term memories](long-term-memory-metadata.md).

The following AWS CLI command lists only the full session summary for a session:

```
aws bedrock-agentcore list-memory-records \
  --memory-id "<memory-id>" \
  --namespace "/strategy/<memory-strategy-id>/actor/<actor-id>/session/<session-id>/" \
  --metadata-filters '[
    {
      "left":     {"metadataKey": "x-amz-agentcore-memory-recordType"},
      "operator": "EQUALS_TO",
      "right":    {"metadataValue": {"stringValue": "FULL_SESSION"}}
    }
  ]'
```

In this command, replace the following placeholder values with your own values:
+  `<memory-id>` – The ID of your memory.
+  `<memory-strategy-id>` – The ID of the summary strategy.
+  `<actor-id>` – The ID of the actor that the session belongs to.
+  `<session-id>` – The ID of the session whose full session summary you want to retrieve.

AgentCore Memory embeds full session summaries like other memory records, so you can also receive them in semantic search results from `RetrieveMemoryRecords`. To limit a semantic search to full session summaries, add the same `x-amz-agentcore-memory-recordType` filter to `metadataFilters` inside `searchCriteria`.

### Permissions and encryption
<a name="summary-strategy-full-session-summary-security"></a>

Full session summaries use the same IAM actions and the same memory resource ARN as other memory records. For example, to read them, you need `bedrock-agentcore:GetMemoryRecord`, `bedrock-agentcore:ListMemoryRecords`, or `bedrock-agentcore:RetrieveMemoryRecords`. You can’t grant or deny access to full session summaries separately from other records in the same memory. To restrict an agent to specific record types, filter on `x-amz-agentcore-memory-recordType` in your application.

AgentCore Memory encrypts full session summaries at rest in the same way as other memory records. If you configured your memory with a customer managed AWS KMS key (`encryptionKeyArn`), that key also encrypts your full session summaries.

### For more information
<a name="summary-strategy-full-session-summary-more-info"></a>
+  [Structured metadata for long-term memories](long-term-memory-metadata.md) 
+  [GetMemoryRecord](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetMemoryRecord.html) in the *Amazon Bedrock AgentCore API Reference* 
+  [ListMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListMemoryRecords.html) in the *Amazon Bedrock AgentCore API Reference* 
+  [RetrieveMemoryRecords](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_RetrieveMemoryRecords.html) in the *Amazon Bedrock AgentCore API Reference* 

**Topics**