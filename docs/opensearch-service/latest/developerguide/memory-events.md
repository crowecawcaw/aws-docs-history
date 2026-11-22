

# Working with events in Amazon OpenSearch Memory

In Amazon OpenSearch Memory, an *event* is content that your agent sends to a space: a set of conversation turns or a JSON object. OpenSearch Memory stores the event as you sent it and extracts memories from it according to the space's strategies.

OpenSearch Memory provides the following event operations. Every one of them takes the ID of the space.
+ [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html) – Send an event.
+ [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html) – Read an event, including its payload.
+ [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html) – Read up to 10 events in one call.
+ [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html) – List the events in a session in time order.
+ [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html) – Find events by the relevance of their content to a query.
+ [DeleteEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteEvent.html) – Delete an event.

**Topics**
+ [Sending an event](#memory-events-create)
+ [Event payloads](#memory-events-payloads)
+ [Reading events](#memory-events-read)
+ [Searching events](#memory-events-search)
+ [Deleting an event](#memory-events-delete)
+ [Metadata tags](#memory-events-metadata)

## Sending an event
<a name="memory-events-create"></a>

To send an event, call `CreateEvent` with the space ID, an `actorId`, and a `payload`. The following parameters are optional:
+ `sessionId` – The conversation the event belongs to. Send every event of one conversation with the same session ID. If you omit it, OpenSearch Memory generates a session ID and returns it. A generated ID is useful for the first event of a new conversation, but every later event of that conversation should carry it.
+ `eventTimestamp` – When the event occurred. The default is the time OpenSearch Memory received the request.
+ `metadata` – Up to 15 key-value tags to store with the event. Memories extracted from the event carry the same tags. For more information, see [Metadata tags](#memory-events-metadata).
+ `infer` – Whether to extract memories from the event. The default is `true`. Set it to `false` to store an event that you want to keep and search but don't want memories extracted from.
+ `clientToken` – A unique token that makes retrying the request safe. The AWS CLI and SDKs supply one for you. For more information, see [Idempotent requests](memory-errors.md#memory-errors-idempotency).

The following example sends a two-turn conversation. The request is in a file named `event.json`.

```bash
aws opensearchmemory create-event --cli-input-json file://event.json
```

```json
{
    "spaceId": "sp-02864597b164",
    "actorId": "user-123",
    "sessionId": "session-001",
    "metadata": { "channel": "web" },
    "payload": {
        "conversational": {
            "unified": {
                "source": {
                    "object": {
                        "messages": [
                            { "role": "USER", "content": { "text": "What's my order status?" } },
                            { "role": "ASSISTANT", "content": { "text": "Order 4471 shipped yesterday and arrives Friday." } }
                        ]
                    }
                }
            }
        }
    }
}
```

The response returns the event's ID, actor, session, and timestamp.

```json
{
    "event": {
        "eventId": "ev-8f3a2c1d9b7e",
        "spaceId": "sp-02864597b164",
        "actorId": "user-123",
        "sessionId": "session-001",
        "eventTimestamp": "2026-11-14T00:35:41Z"
    }
}
```

`CreateEvent` returns as soon as the event is stored. Memories are extracted afterward. For more information about when the event and its memories become visible to each operation, see [What you see, and when](memory-how-it-works.md#memory-how-it-works-consistency).

## Event payloads
<a name="memory-events-payloads"></a>

The `payload` of an event contains exactly one of the following members.

### Conversational
<a name="memory-events-payloads-conversational"></a>

Conversation turns, in order. Set `payload.conversational.unified.source.object.messages` to a list of 1 to 100 turns. Each turn has a `role` of `USER`, `ASSISTANT`, or `SYSTEM` and its text in `content.text`. The order of the turns matters for extraction. The text of all turns in one event can total up to 5 MiB.

### Structured data
<a name="memory-events-payloads-structured"></a>

A JSON object, for content that isn't a conversation, such as a tool result or a record your agent produced. Set `payload.structuredData.source.json` to the object. The object can be up to 1 MiB and nested up to 10 levels deep. Structured data is always JSON, so it has no content type.

```json
{
    "spaceId": "sp-02864597b164",
    "actorId": "user-123",
    "sessionId": "release-2026-11-02",
    "payload": {
        "structuredData": {
            "source": {
                "json": {
                    "service": "checkout",
                    "version": "4.2.0",
                    "result": "rolled back",
                    "reason": "Error rate exceeded the alarm threshold."
                }
            }
        }
    }
}
```

## Reading events
<a name="memory-events-read"></a>

### Getting an event by ID
<a name="memory-events-get"></a>

To read one event, including its payload, call `GetEvent` with the space ID and event ID.

```bash
aws opensearchmemory get-event \
    --space-id sp-02864597b164 \
    --event-id ev-8f3a2c1d9b7e
```

To read up to 10 events in one call, call `BatchGetEvent` with a list of event IDs. The response returns the events in the order you requested them. An event that couldn't be returned is listed in `errors` with a code that explains why, such as `RESOURCE_NOT_FOUND`, instead of failing the whole call.

```bash
aws opensearchmemory batch-get-event \
    --space-id sp-02864597b164 \
    --event-ids ev-8f3a2c1d9b7e ev-1c2d3e4f5a6b
```

### Checking an event's owner
<a name="memory-events-owner"></a>

`GetEvent`, `BatchGetEvent`, and `DeleteEvent` accept optional `actorId` and `sessionId` parameters. If you supply them, OpenSearch Memory checks that the event belongs to that actor and session and returns `ResourceNotFoundException` if it doesn't, as if the event didn't exist. Use these parameters when your application acts on behalf of one end user, so that a mistaken or forged event ID can't reach another user's data. You can require them in IAM with the `osm:actorId` and `osm:sessionId` condition keys. For more information, see [Policy condition keys for OpenSearch Memory](security-iam-memory.md#security_iam_memory-conditionkeys).

### Listing a session's events
<a name="memory-events-list"></a>

To list the events of one session in time order, call `ListEvents` with the space ID, `actorId`, and `sessionId`. The response returns each event's ID, timestamp, and metadata, but not its payload. Use `GetEvent` or `BatchGetEvent` to read the payloads you need.

```bash
aws opensearchmemory list-events \
    --space-id sp-02864597b164 \
    --actor-id user-123 \
    --session-id session-001 \
    --sort-order ASC \
    --max-results 50
```

You can narrow the list with the following parameters:
+ `eventTimestampAfter` and `eventTimestampBefore` – Return only events in a time range. Both bounds are inclusive.
+ `sortOrder` – `ASC` for oldest first or `DESC` for most recent first. The default is `DESC`.
+ `metadataFilters` – Return only events whose metadata contains every one of the given key-value pairs.

`ListEvents` returns up to `maxResults` events per page (1 to 100, default 20) and a `nextToken` when there are more. When you use `metadataFilters`, a page can contain fewer events than `maxResults`, or none, and still return a `nextToken`. Keep paging until the response has no `nextToken`.

## Searching events
<a name="memory-events-search"></a>

To find events by what they say rather than by when they happened, call `SearchEvents` with the space ID, an `actorId`, and a query. The query uses the same subset of the OpenSearch Query DSL as [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html), with the fields `text` and `vector`. Each search covers one actor. To narrow it to specific conversations, add up to 10 `sessionIds`.

```bash
aws opensearchmemory search-events \
    --space-id sp-02864597b164 \
    --actor-id user-123 \
    --session-ids session-001 \
    --query '{"match": {"text": "order status"}}'
```

Each result is the passage of an event that matched, in `matchedContent`, with the event's ID, a relevance score, and the event's metadata. A long event can match more than once. To read the whole event, pass its ID to `GetEvent`.

To search only particular events, such as the source events of a memory, filter on `event_ids` with a `term` or `terms` query. For more information, see [Searching memories and events in Amazon OpenSearch Memory](memory-search.md).

## Deleting an event
<a name="memory-events-delete"></a>

**Warning**  
You can't undo deleting an event.

To delete an event, call `DeleteEvent` with the space ID and event ID. You can supply `actorId` and `sessionId` to check the event's owner first.

```bash
aws opensearchmemory delete-event \
    --space-id sp-02864597b164 \
    --event-id ev-8f3a2c1d9b7e \
    --actor-id user-123
```

The event stops appearing in `SearchEvents` results shortly after the call returns. Deleting an event that doesn't exist returns `ResourceNotFoundException`.

Deleting an event doesn't delete the memories extracted from it, because a memory can combine information from several events. To delete those memories, use [DeleteMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_DeleteMemory.html). For more information, see [Deleting a memory](memory-memories.md#memory-memories-delete).

## Metadata tags
<a name="memory-events-metadata"></a>

Metadata tags are key-value pairs that you attach to an event when you create it. Memories extracted from the event carry the same tags. Use metadata to record attributes of your own, such as the channel a conversation came from or the tenant it belongs to, and then filter by them in `ListEvents`, `SearchEvents`, and `SearchMemories`. Metadata tags are separate from the AWS tags that you attach to a space.

The following rules apply to metadata:
+ An event or memory can have up to 15 tags, and a space can use up to 50 distinct keys.
+ A key has 1 to 128 characters and can contain letters, digits, hyphens, and underscores. Keys that begin with `x-amz-` are reserved for AWS use. A request that uses a reserved key fails with `ValidationException`.
+ A value has up to 256 characters and can contain letters, digits, spaces, and the characters `. _ : / = + @ -`.

In a query, refer to a tag as `metadata.key`. For example, the following `SearchMemories` query finds memories about recipes that have the tag `channel` set to `web`.

```json
{
    "bool": {
        "must":   [ { "match": { "memory_text": "recipes" } } ],
        "filter": [ { "term":  { "metadata.channel": "web" } } ]
    }
}
```

Don't put sensitive information, such as names or email addresses, in metadata keys or values.