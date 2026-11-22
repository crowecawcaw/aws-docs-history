

# Best practices for Amazon OpenSearch Memory

This topic provides recommendations for getting good memories out of Amazon OpenSearch Memory and for keeping your users' data separate and secure. The recommendations are general guidelines and don't represent a complete solution.

**Topics**
+ [Designing spaces and strategies](#memory-best-practices-design)
+ [Sending events](#memory-best-practices-events)
+ [Searching](#memory-best-practices-search)
+ [Security](#memory-best-practices-security)

## Designing spaces and strategies
<a name="memory-best-practices-design"></a>

**Use one space per application, not per user.** A space is the unit of configuration and access control. Separate users within a space by actor ID, and keep separate applications, or separate environments such as development and production, in separate spaces.

**Start with `SEMANTIC` and `SUMMARY`.** These two strategies cover most agent use cases: facts that persist across sessions and a running summary of each session. Add a `CUSTOM` strategy when you need structured records that the built-in types don't capture, and describe the record you want precisely in its prompt.

**Set the idle timeout to match your conversations.** The default idle timeout of 60 seconds suits chat. If your users take minutes between turns, raise `idleTimeoutSeconds` so that one exchange isn't split across several extractions. If your agent needs memories within seconds of a turn, lower `extractEveryNMessages` instead and accept more frequent, smaller extractions.

**Leave consolidation on for facts.** Consolidation keeps a `SEMANTIC` strategy's memories current, so a search returns "lives in Austin" rather than both "lives in Seattle" and "lives in Austin." Turn it off only when you want a full history of every extracted memory and your application handles duplicates.

**Choose retention deliberately.** Keep events only as long as you need them for auditing or re-extraction, and set a memory retention period if your use case or regulations require memories to age out. By default, memories don't expire. For more information, see [Configuring retention](memory-spaces.md#memory-spaces-retention).

## Sending events
<a name="memory-best-practices-events"></a>

**Always send a session ID.** Send every turn of one conversation with the same `sessionId`. Extraction groups a session's turns together, and `SUMMARY` strategies summarize a session. Letting OpenSearch Memory generate a session ID is fine for the first event of a new conversation, as long as you reuse the returned ID afterward.

**Let the SDK supply the client token.** The AWS SDKs add a `clientToken` to [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html) and reuse it when they retry, so a retry returns the original event instead of creating a duplicate. Without a client token, a retry stores the event again, and if you omitted `sessionId`, the copy lands in a new session. Reuse the same `sessionId` on every `CreateEvent` of a conversation so that it stays in one session.

**Send turns as they happen.** Sending each exchange as its own event, rather than batching a whole conversation into one event at the end, lets the idle timeout and message-count triggers work as intended and lets your agent recall earlier parts of a long conversation.

**Use `infer: false` for content you want to search but not learn from.** For example, store a transcript you need for auditing without extracting memories from it.

**Use metadata for your own attributes, not for content.** Tag events with attributes you will filter by, such as a channel or a tenant. Don't put the content itself, or personal data, in metadata.

## Searching
<a name="memory-best-practices-search"></a>

**Prefer `hybrid` queries for recall.** A `hybrid` query combines keyword and semantic matching, so it finds both exact phrases and paraphrases. Use a plain `match` query when you know the exact words, and a `neural` query for natural-language questions.

**Scope searches to the strategies you need.** Searching only the `SEMANTIC` strategy for facts, or only a `CUSTOM` strategy for records, returns more relevant results than searching every strategy at once.

**Don't store memory IDs long term.** Consolidation replaces a memory with a new one when a fact changes, and the replacement has a new ID. Fetch current IDs from [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) or [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) when you need them.

**Treat scores as ordering only.** Relevance scores aren't normalized and vary with the query type. Don't compare scores across queries or apply fixed thresholds without testing.

## Security
<a name="memory-best-practices-security"></a>

**Grant least privilege.** Scope policies to specific space ARNs and to the actions each principal needs. Separate the principals that administer spaces from the principals that read and write data.

**Limit each end user to their own data.** Use a separate actor ID for each end user. When end users call OpenSearch Memory with their own credentials, use the `osm:actorId` condition key with a `Null` check to limit each principal to one actor. For more information, see [Limiting a principal to one actor's memories](security-iam-memory.md#security_iam_id-based-policy-examples-memory-actor).

**Pass the owner on reads and deletes.** When your application acts for one end user, supply `actorId` (and `sessionId` or `strategyName`) on [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html), [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html), [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html), and [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html), so that a mistaken or forged ID can't reach another user's data.

**Use a customer managed key for sensitive data.** With a customer managed key you control and audit access to a space's data and can revoke it. For more information, see [Key management](memory-data-protection.md#memory-key-management).

**Monitor API activity with CloudTrail.** Turn on data events for your spaces to record every event and memory operation. For more information, see [Monitoring Amazon OpenSearch Memory with AWS CloudTrail](memory-cloudtrail.md).