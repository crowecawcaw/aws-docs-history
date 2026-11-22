

# Working with memories in Amazon OpenSearch Memory

In Amazon OpenSearch Memory, a *memory* is a piece of text that a memory strategy extracted from events, or that you wrote directly. Each memory belongs to one actor, one session, and one strategy, and carries the IDs of the events it was derived from.

OpenSearch Memory provides the following memory operations. Every one of them takes the ID of the space.
+ [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html) – Write a memory directly, without extraction.
+ [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html) – Read a memory by ID.
+ [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html) – List memories without a query, for example the most recent memories of one actor.
+ [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) – Find memories by relevance to a query.
+ [UpdateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateMemory.html) – Change a memory's text or metadata.
+ [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html) – Delete a memory.

**Topics**
+ [The memory record](#memory-memories-record)
+ [Writing a memory directly](#memory-memories-create)
+ [Reading memories](#memory-memories-read)
+ [Searching memories](#memory-memories-search)
+ [Updating a memory](#memory-memories-update)
+ [Deleting a memory](#memory-memories-delete)

## The memory record
<a name="memory-memories-record"></a>

`GetMemory` returns a memory with the following members. `SearchMemories` and `ListMemories` return subsets of them.


| Member | Description | 
| --- | --- | 
| memoryId | The memory's ID, assigned by OpenSearch Memory. | 
| memoryType | SEMANTIC, SUMMARY, or CUSTOM. The type of the strategy that produced the memory. | 
| strategyName | The name of the strategy the memory belongs to. | 
| content | The memory text. | 
| systemMetadata | The owning actorId and sessionId, and the createdAt and updatedAt timestamps. | 
| metadata | The memory's metadata tags. | 
| sourceEventIds | The IDs of the events the memory was extracted from. Returned by SearchMemories. | 

## Writing a memory directly
<a name="memory-memories-create"></a>

When your application already knows something worth remembering, you can write it as a memory with `CreateMemory` instead of sending it as an event and waiting for extraction. OpenSearch Memory stores the text as you supply it under the strategy you name. It doesn't extract or consolidate it.

The request requires the space ID, the `name` of a strategy that the space already declares, the memory `content` (1 to 16,000 characters), and an `actorId`. You can also supply a `sessionId`, `metadata`, and a `clientToken`.

```bash
aws opensearchmemory create-memory \
    --space-id sp-02864597b164 \
    --name user-facts \
    --actor-id user-123 \
    --content "The user prefers vegetarian recipes."
```

The response returns the new memory's ID.

```json
{
    "memory": {
        "memoryId": "mem-3b9f1c2e-7d4a-4e8b-9c1f-2a6d8e0b4f17",
        "spaceId": "sp-02864597b164",
        "name": "user-facts",
        "actorId": "user-123",
        "sessionId": "a4c1e0f2-9b3d-4c5e-8f6a-7b8c9d0e1f2a"
    }
}
```

The memory takes its type from the strategy. It becomes searchable shortly after the call returns. Until it is indexed, `GetMemory`, `UpdateMemory`, and `DeleteMemory` return `ResourceNotFoundException` for the new ID. If your application needs the memory right away, poll `GetMemory` with backoff.

The AWS CLI and SDKs add a `clientToken` to the request. A retry with the same token within 2 hours returns the same `memoryId` instead of creating a second memory. For more information, see [Idempotent requests](memory-errors.md#memory-errors-idempotency).

## Reading memories
<a name="memory-memories-read"></a>

### Getting a memory by ID
<a name="memory-memories-get"></a>

To read one memory, call `GetMemory` with the space ID and the memory ID that `SearchMemories` or `ListMemories` returned.

```bash
aws opensearchmemory get-memory \
    --space-id sp-02864597b164 \
    --memory-id mem-3b9f1c2e-7d4a-4e8b-9c1f-2a6d8e0b4f17
```

`GetMemory`, `UpdateMemory`, and `DeleteMemory` accept optional `actorId` and `strategyName` parameters. If you supply them, OpenSearch Memory checks that the memory belongs to that actor and strategy and returns `ResourceNotFoundException` if it doesn't, as if the memory didn't exist. Use these parameters when your application acts on behalf of one end user. You can require them in IAM with the `osm:actorId` and `osm:strategyName` condition keys. For more information, see [Policy condition keys for OpenSearch Memory](security-iam-memory.md#security_iam_memory-conditionkeys).

### Listing memories
<a name="memory-memories-list"></a>

To list memories without a query, call `ListMemories`. The results include each memory's ID, type, strategy name, system metadata, and metadata tags, but not its content. Use `GetMemory` to read the content of the memories you need.

You can narrow the list with the following parameters:
+ `memoryStrategies` – One to five selectors, each naming a `memoryType` and optionally `memoryStrategyNames` of that type. Omit it to list every strategy.
+ `actorIds` and `sessionIds` – Up to 10 of each. A memory must match both filters if you supply both.
+ `sortBy` – `CREATED_AT` (the default) or `UPDATED_AT`.
+ `sortOrder` – `ASC` or `DESC` (the default).

The following example lists the most recently updated `user-facts` memories of one actor.

```bash
aws opensearchmemory list-memories \
    --space-id sp-02864597b164 \
    --memory-strategies '[{"memoryType":"SEMANTIC","memoryStrategyNames":["user-facts"]}]' \
    --actor-ids user-123 \
    --sort-by UPDATED_AT \
    --max-results 20
```

`ListMemories` returns up to `maxResults` memories per page (1 to 100, default 20) and a `nextToken` when there are more. If memories are written or deleted while you page through results, a memory can be skipped or returned twice.

## Searching memories
<a name="memory-memories-search"></a>

To find memories by what they say, call `SearchMemories` with the space ID, an `actorId`, and a query. Each search covers one actor. The results are ranked by relevance and include each memory's content, score, and source events.

```bash
aws opensearchmemory search-memories \
    --space-id sp-02864597b164 \
    --actor-id user-123 \
    --query '{"neural": {"memory_vector": {"query_text": "what does the user like to eat", "k": 10}}}'
```

To search only some strategies, add `memoryStrategies` selectors. To filter by metadata, add a `metadata.key` filter to the query. For the query language, see [Searching memories and events in Amazon OpenSearch Memory](memory-search.md).

## Updating a memory
<a name="memory-memories-update"></a>

To change a memory's text or metadata, call `UpdateMemory` with the space ID, the memory ID, and the fields to change. Supply `content`, `metadata`, or both.
+ `content` – Replaces the memory text. The memory becomes searchable by its new text shortly after the call returns, and the old text is no longer searchable.
+ `metadata` and `metadataMode` – With `REPLACE`, the default, the supplied tags replace the memory's tags, and any tag you don't supply is removed. With `MERGE`, tags you don't supply are kept, and a tag whose value is the empty string is removed.

The following example adds one tag and keeps the others.

```bash
aws opensearchmemory update-memory \
    --space-id sp-02864597b164 \
    --memory-id mem-3b9f1c2e-7d4a-4e8b-9c1f-2a6d8e0b4f17 \
    --metadata-mode MERGE \
    --metadata verified=true
```

The response returns the updated memory in the same shape as `GetMemory`.

Note the following about updates:
+ The memory keeps its `memoryId`. You can't change its type. To change the type, delete the memory and create a new one under a different strategy.
+ An update doesn't extend the memory's lifetime. The expiry is counted from when the memory was first written.
+ If two requests update the same memory at the same time, the last one wins. OpenSearch Memory doesn't check versions. If your application needs ordered updates to a memory, serialize them.
+ `UpdateMemory` doesn't take a `clientToken`. A retried request is applied again, with the same result.

## Deleting a memory
<a name="memory-memories-delete"></a>

**Warning**  
You can't undo deleting a memory.

To delete a memory, call `DeleteMemory` with the space ID and memory ID. You can supply `actorId` and `strategyName` to check the memory's owner first.

```bash
aws opensearchmemory delete-memory \
    --space-id sp-02864597b164 \
    --memory-id mem-3b9f1c2e-7d4a-4e8b-9c1f-2a6d8e0b4f17 \
    --actor-id user-123
```

The memory stops appearing in search results shortly after the call returns. Deleting a memory that doesn't exist returns `ResourceNotFoundException`. If your application retries deletes, treat that error as success.