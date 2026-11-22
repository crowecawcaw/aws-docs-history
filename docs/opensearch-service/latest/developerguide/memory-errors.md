

# Error handling in Amazon OpenSearch Memory

This topic describes the errors that Amazon OpenSearch Memory returns and how to handle them in your application. For a list of common errors that apply to all AWS services, see [Common Errors](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/CommonErrors.html) in the *Amazon OpenSearch Memory API Reference*.

**Topics**
+ [Error components](#memory-errors-components)
+ [Error messages and codes](#memory-errors-codes)
+ [Validation error reasons](#memory-errors-validation-reasons)
+ [Error retries and exponential backoff](#memory-errors-retries)
+ [Idempotent requests](#memory-errors-idempotency)
+ [Batch operations and error handling](#memory-errors-batch)

## Error components
<a name="memory-errors-components"></a>

When your application sends a request, OpenSearch Memory attempts to process it. If the request succeeds, OpenSearch Memory returns an HTTP `200 OK` status code with the results of the operation. If the request fails, OpenSearch Memory returns an error with three components:
+ An HTTP status code, such as `400`.
+ An exception name, such as `ResourceNotFoundException`.
+ An error message, such as `Space sp-02864597b164 not found`.

The AWS SDKs propagate errors to your application as typed exceptions, so you can handle each kind separately. `ValidationException` also carries a `reason` code and, when a specific field is at fault, a `fieldList` naming the fields. For more information, see [Validation error reasons](#memory-errors-validation-reasons).

## Error messages and codes
<a name="memory-errors-codes"></a>

The following list describes the exceptions that OpenSearch Memory returns, grouped by HTTP status code. If *OK to retry?* is *Yes*, you can submit the same request again. If it is *No*, fix the problem on the client side before you submit a new request.

### HTTP status code 400
<a name="memory-errors-400"></a>

An HTTP `400` status code indicates a problem with your request. Fix the issue in your application before submitting the request again.

**ValidationException**

The request isn't valid. The `reason` and `message` describe the problem, and `fieldList` names the fields that failed validation, if any. Common causes: a value outside its allowed range, a query that uses an unsupported query type or field, a `CUSTOM` strategy without an `extractionPrompt`, an [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html) request with an empty `memoryStrategies` list, or an unusable customer managed key.

OK to retry? No

**ResourceNotFoundException**

The space, event, or memory doesn't exist, or the request's `actorId`, `sessionId`, or `strategyName` doesn't match the stored record. Also returned for a memory past its expiry, for a memory written with [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) that hasn't been indexed yet, and by [GetSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetSpace.html) for a short time after [CreateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateSpace.html) returns.

OK to retry? Yes, if the resource was just created. Otherwise no.

**ConflictException**

The request conflicts with the current state of the resource. Causes: a `CreateSpace` request with a name that another space in the account and Region already has; an `UpdateSpace` or [DeleteSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteSpace.html) request on a space that is `CREATING`, `UPDATING`, or `DELETING`; or a `clientToken` reused with different request content. For more information, see [Idempotent requests](#memory-errors-idempotency).

OK to retry? Yes, after the space leaves its transitional status. Otherwise no.

**ServiceQuotaExceededException**

A `CreateSpace` or `UpdateSpace` request would exceed a quota, such as the number of strategies in a space. For more information, see [Endpoints and quotas for Amazon OpenSearch Memory](memory-quotas.md).

OK to retry? No

**ThrottlingException**

The request rate is too high, or AWS KMS throttled OpenSearch Memory's use of the space's customer managed key. The AWS SDKs retry throttled requests automatically.

OK to retry? Yes

**AccessDeniedException**

The caller doesn't have permission for the `osm:` action on the space, or, for a space with a customer managed key, doesn't have permission to use the key. The message names the action and resource. For more information, see [Troubleshooting OpenSearch Memory identity and access](security-iam-memory.md#security_iam_memory-troubleshoot).

OK to retry? No

### HTTP status code 500
<a name="memory-errors-500"></a>

**InternalServerException**

OpenSearch Memory couldn't process the request because of an internal error. The AWS SDKs retry this error automatically.

OK to retry? Yes

## Validation error reasons
<a name="memory-errors-validation-reasons"></a>

A `ValidationException` includes a `reason` that identifies the rule the request broke. OpenSearch Memory might add reasons over time, so treat a value you don't recognize as a general validation failure.


| Reason | Meaning | 
| --- | --- | 
| fieldValidationFailed | A field's value is outside its allowed range or format. fieldList names the field. | 
| unsupportedParameter | The request includes a parameter that this operation doesn't accept. | 
| disallowedQueryType | The query uses a query type that isn't supported, such as knn or wildcard. | 
| unknownField | The query or sort refers to a field that doesn't exist. | 
| unsupportedField | The query or sort refers to a field that exists but can't be used in that position. | 
| nonFilterableField | The query or sort refers to the actor or session field. Use the actorId and sessionIds parameters instead. | 
| fieldIndexMismatch | The field can't be used with that query type, for example a neural query on a text field. | 
| unboundedPattern | A query pattern isn't bounded and would be too costly to run. | 
| queryNestingTooDeep | A bool query nests more than 5 levels, or the query has too many clauses. | 
| queryBodyTooLarge | The query and sort exceed 64 KB together, or exceed a clause, value, or function limit, or the response would exceed 5 MiB. | 
| malformedQueryBody | The query or sort can't be parsed. | 
| invalidNextToken | The pagination token isn't valid, or paging went past the limit on results you can page through. | 
| other | Another validation failure, such as an unusable customer managed key. Read the message. | 

## Error retries and exponential backoff
<a name="memory-errors-retries"></a>

Many errors are transient. The AWS SDKs retry `ThrottlingException` and `InternalServerException` automatically with exponential backoff: each retry waits longer than the one before it, with some random jitter. If you don't use an SDK, implement the same approach. Start with a short delay such as 50 milliseconds, double it on each retry, and stop after a reasonable number of attempts.

Two situations call for retries that the SDKs don't do for you:
+ Right after `CreateSpace`, `GetSpace` can return `ResourceNotFoundException` for a short time. Use the `SpaceActive` waiter, which handles this, rather than calling `GetSpace` once.
+ Right after `CreateMemory`, [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html) returns `ResourceNotFoundException` until the memory is indexed. Poll with backoff if your application needs the memory immediately.

## Idempotent requests
<a name="memory-errors-idempotency"></a>

`CreateSpace`, [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html), and `CreateMemory` accept a `clientToken`, a unique string that identifies the request. If a request with the same token is received again within 2 hours, OpenSearch Memory returns the result of the first request instead of creating a second resource. The AWS SDKs and the AWS CLI generate a token for you and reuse it when they retry a request, so a network timeout can't create a duplicate space, event, or memory.

The retried request must be the same request. If the same token arrives with different content, the request fails with `ConflictException`.

Without a client token, a retry of `CreateEvent` stores the event again, and if you omitted `sessionId`, the copy lands in a new session. Reuse the same `sessionId` on every `CreateEvent` of a conversation so that it stays in one session.

The other operations handle retries as follows:


| Operation | Retry behavior | 
| --- | --- | 
| UpdateSpace | Doesn't take a token. A retry while the space is UPDATING fails with ConflictException; a retry after the update completes changes nothing, because the space already has the values. | 
| [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html) | Doesn't take a token. A retry applies the same change again, with the same result. | 
| DeleteSpace | A retry while the space is DELETING returns DELETING again. Safe to retry. | 
| [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html), [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html) | A retry after the delete succeeded returns ResourceNotFoundException. Treat that error as success. | 
| Read operations | Safe to retry. | 

## Batch operations and error handling
<a name="memory-errors-batch"></a>

[BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html) reads up to 10 events in one call. It doesn't fail the whole call when one event can't be returned. Instead, the response lists the events it could return in `events`, in the order you requested them, and the rest in `errors`, each with an `errorCode`:


| Error code | Meaning | Action | 
| --- | --- | --- | 
| RESOURCE\_NOT\_FOUND | The event doesn't exist, or doesn't belong to the actorId or sessionId in the request. | Don't retry. | 
| THROTTLING | The read was throttled. | Retry the event with backoff. | 
| ACCESS\_DENIED | The caller can't decrypt the event under the space's customer managed key. | Fix the key permissions. | 
| INTERNAL\_SERVER | The event couldn't be read. | Retry the event with backoff. | 

Check `errors` on every response, and retry only the events that failed with a retryable code. If the space's customer managed key is disabled or deleted, the whole call fails with `ValidationException`, as [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html) does.