

# Troubleshooting Amazon OpenSearch Memory

This topic describes problems that you might encounter when you use Amazon OpenSearch Memory, their likely causes, and how to resolve them. For the meaning of each exception and whether to retry it, see [Error handling in Amazon OpenSearch Memory](memory-errors.md).

**Topics**
+ [I can't send events to a space I just created](#memory-troubleshooting-new-space)
+ [Search doesn't return the event or memory I just wrote](#memory-troubleshooting-not-yet-searchable)
+ [No memories are extracted from my events](#memory-troubleshooting-no-memories)
+ [Memories duplicate or contradict each other](#memory-troubleshooting-duplicates)
+ [Memories disappeared](#memory-troubleshooting-disappeared)
+ [A CreateSpace or UpdateSpace request fails with ValidationException](#memory-troubleshooting-space-validation)
+ [A search fails with ValidationException](#memory-troubleshooting-search-validation)
+ [Requests fail with ConflictException](#memory-troubleshooting-conflict)
+ [Requests fail for a space with a customer managed key](#memory-troubleshooting-cmk)

## I can't send events to a space I just created
<a name="memory-troubleshooting-new-space"></a>

**Problem**: [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html) or [GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html) returns `ResourceNotFoundException`, or `CreateEvent` returns `ConflictException`, right after [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html).

**Cause**: `CreateSpace` returns before the space is ready. The space's status is `CREATING` until setup finishes, and for a short time after `CreateSpace` returns, `GetSpace` may not find the space at all.

**Resolution**: Wait until the space is `ACTIVE` before you use it. Use the `SpaceActive` waiter in the AWS CLI (`aws opensearchmemory wait space-active`) or the SDKs, which handles both the not-found window and the `CREATING` status. If the status becomes `FAILED`, read `statusReason`. For more information, see [Space status](memory-spaces.md#memory-spaces-status).

## Search doesn't return the event or memory I just wrote
<a name="memory-troubleshooting-not-yet-searchable"></a>

**Problem**: [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html) returns an event, but [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html) doesn't find it, or [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) doesn't return memories from it. Or [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) succeeded, but [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html) returns `ResourceNotFoundException`.

**Cause**: Writing and indexing are separate. An event is searchable shortly after `CreateEvent` returns. Memories are extracted only when a strategy's trigger fires: by default, after 12 messages accumulate in the session, or after the session has been idle for 60 seconds. A memory written with `CreateMemory` is readable and searchable shortly after the call returns, once it is indexed.

**Resolution**: Wait at least the strategy's `idleTimeoutSeconds` after the last event in the session, then search again. If your application needs memories sooner, lower `extractEveryNMessages` or `idleTimeoutSeconds`. For `CreateMemory`, poll `GetMemory` with backoff. For more information, see [What you see, and when](memory-how-it-works.md#memory-how-it-works-consistency).

## No memories are extracted from my events
<a name="memory-troubleshooting-no-memories"></a>

**Problem**: Events are stored and searchable, but `SearchMemories` and [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) never return memories.

**Cause and resolution**: Check the following, in order:

1. **The space has no strategies.** A space with no `memoryStrategies` stores events but extracts nothing. Call `GetSpace` and add strategies with [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html) if the list is empty.

1. **The events were sent with `infer: false`.** Such events are stored and searchable but aren't extracted.

1. **The session hasn't gone idle yet.** Extraction waits for a trigger. See the previous section.

1. **The conversation contained nothing to extract.** A `SEMANTIC` strategy extracts facts worth remembering; greetings and small talk produce none. Test with a conversation that states a clear preference or fact.

1. **The space's customer managed key is unavailable.** Extraction stops while the key is disabled or pending deletion. Check the key's state in AWS KMS.

To confirm that extraction is running, look for `ExtractMemories` service events in CloudTrail. For more information, see [Service events](memory-cloudtrail.md#memory-cloudtrail-service).

## Memories duplicate or contradict each other
<a name="memory-troubleshooting-duplicates"></a>

**Problem**: A strategy stores memories that repeat facts it already stored, or stores both an old and a new version of a fact.

**Cause**: Consolidation is off for the strategy. Without consolidation, every extracted memory is stored as a new memory.

**Resolution**: Set `consolidationEnabled` to `true` in the strategy's configuration. To further reduce duplicates, set `extractionSeedTopK` or `extractionSeedRecentN` so that extraction can see what is already stored. For more information, see [Consolidation](memory-strategies.md#memory-strategies-consolidation) and [Memory seeding](memory-strategies.md#memory-strategies-seeding).

## Memories disappeared
<a name="memory-troubleshooting-disappeared"></a>

**Problem**: Memories that searches used to return no longer appear.

**Cause**: One of the following:
+ **The memories expired.** The space sets `memoryExpiryDays`, and the memories reached the end of their lifetime. Look for `ExpireMemories` service events in CloudTrail.
+ **Consolidation replaced them.** When a newer fact supersedes an older memory, `SearchMemories` returns the replacement, which has a new ID, instead of the older memory. `GetMemory` still returns the older memory by its ID. Search again to get current IDs.
+ **The strategy was removed.** Memories of a removed strategy stay in the space but are no longer associated with a declared strategy.

**Resolution**: To keep memories longer, raise `memoryExpiryDays` or set it to 0. The change applies to memories written after it. Don't store memory IDs long term; fetch them from `SearchMemories` or `ListMemories` when you need them.

## A CreateSpace or UpdateSpace request fails with ValidationException
<a name="memory-troubleshooting-space-validation"></a>

**Problem**: The request is rejected and the message refers to strategies, retention, the model, or the key.

**Cause and resolution**:


| Message refers to | Cause | Resolution | 
| --- | --- | --- | 
| extractionPrompt | A CUSTOM strategy has no prompt. | Add an extractionPrompt to every CUSTOM strategy. | 
| memoryStrategies | An UpdateSpace request sent an empty list, or the list has more than 10 strategies or duplicate names. | Send at least one strategy, or omit the list to leave strategies unchanged. | 
| extractionModelId | The model ID isn't supported, or includes a Region or inference-profile prefix such as us.. | Use anthropic.claude-haiku-5-5 or anthropic.claude-opus-5-5, exactly. | 
| kmsKeyArn | The key isn't a symmetric encryption key, isn't enabled, or isn't in the space's Region. | Use an enabled symmetric key in the same Region. | 
| name | The name has invalid characters or length. | Use 1–128 characters, starting with a letter. | 

## A search fails with ValidationException
<a name="memory-troubleshooting-search-validation"></a>

**Problem**: `SearchMemories` or `SearchEvents` rejects the query.

**Cause**: The `reason` in the exception identifies the rule. The most common:


| Reason | Fix | 
| --- | --- | 
| disallowedQueryType | Use only the supported query types. Replace knn with neural, and wildcard or fuzzy with match. | 
| nonFilterableField | Don't refer to the actor or session in the query. Use the actorId parameter, and sessionIds in SearchEvents. | 
| unknownField | Check the field name. Memory text is memory\_text; event text is text. Field names are snake\_case. | 
| queryBodyTooLarge | Reduce the query size, the number of clauses or terms values, or maxResults. | 
| invalidNextToken | Don't modify tokens, and don't page past the limit. Narrow the query instead. | 

For the complete list, see [Validation error reasons](memory-errors.md#memory-errors-validation-reasons). For the query rules, see [Searching memories and events in Amazon OpenSearch Memory](memory-search.md).

## Requests fail with ConflictException
<a name="memory-troubleshooting-conflict"></a>

**Problem**: A request is rejected because it conflicts with the resource's current state.


| Cause | Resolution | 
| --- | --- | 
| Another space in the account and Region has the name in the CreateSpace request. | Choose a different name or use the existing space. | 
| The space is CREATING, UPDATING, or DELETING and the request tried to update or delete it. | Wait for the space to become ACTIVE, then retry. | 
| A clientToken was reused with different request content. | Use a new token for each new request. When you retry, send the same content. | 

For more information, see [Idempotent requests](memory-errors.md#memory-errors-idempotency).

## Requests fail for a space with a customer managed key
<a name="memory-troubleshooting-cmk"></a>

**Problem**: Requests on one space fail with `AccessDeniedException`, `ValidationException`, or `ThrottlingException`, while requests on other spaces succeed.


| Error | Cause | Resolution | 
| --- | --- | --- | 
| AccessDeniedException on CreateSpace | The caller can't create grants on the key. | Grant kms:CreateGrant on the key in the key policy or IAM policy. | 
| AccessDeniedException on event or memory operations | The caller can't use the key. | Grant the AWS KMS actions the operation needs. See [Permissions required for a customer managed key](memory-data-protection.md#memory-encryption-permissions). | 
| ValidationException mentioning the key | The key is disabled, pending deletion, or deleted. | Enable the key or cancel its deletion. | 
| ThrottlingException | AWS KMS throttled the request. | Retry with backoff, or request a higher AWS KMS request quota. | 