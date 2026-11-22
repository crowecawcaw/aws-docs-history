

# Searching memories and events in Amazon OpenSearch Memory

Amazon OpenSearch Memory searches memories and events with a query that you write in a subset of the OpenSearch Query DSL. You pass the query clause in the `query` parameter of [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) or [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html), and an optional `sort` clause. OpenSearch Memory validates the query, runs it against one actor's data, and returns results ranked by relevance.

This topic describes the search request, the supported query types, and the fields you can query.

**Topics**
+ [The search request](#memory-search-request)
+ [Fields you can query](#memory-search-fields)
+ [Keyword, semantic, and hybrid queries](#memory-search-query-types)
+ [Filtering and sorting](#memory-search-filtering)
+ [Supported query types and limits](#memory-search-limits)
+ [Paginating results](#memory-search-pagination)

## The search request
<a name="memory-search-request"></a>

Both search operations take the following parameters:
+ `spaceId` – The space to search.
+ `actorId` – The actor whose data to search. Required. Every search covers exactly one actor.
+ `query` – A query clause, such as `{"match": {"memory_text": "vegetarian"}}`.
+ `sort` – Optional. A sort clause on `_score` or a time field. Omit it to rank by relevance.
+ `maxResults` and `nextToken` – Pagination. For more information, see [Paginating results](#memory-search-pagination).

`SearchMemories` also accepts `memoryStrategies`, one to five selectors that limit the search to particular strategies. `SearchEvents` also accepts `sessionIds`, up to 10 session IDs that limit the search to particular conversations.

The following AWS CLI example searches one actor's memories in two strategies.

```bash
aws opensearchmemory search-memories \
    --space-id sp-02864597b164 \
    --actor-id user-123 \
    --memory-strategies '[{"memoryType":"SEMANTIC"},{"memoryType":"CUSTOM","memoryStrategyNames":["support-cases"]}]' \
    --query '{"match": {"memory_text": "refund"}}'
```

## Fields you can query
<a name="memory-search-fields"></a>


| Field | In `SearchMemories` | In `SearchEvents` | Use | 
| --- | --- | --- | --- | 
| Text | memory\_text | text | Keyword queries such as match and match\_phrase | 
| Embedding | memory\_vector | vector | neural queries | 
| Created time | system\_metadata.created\_at | system\_metadata.created\_at | range filters, decay functions, and sort | 
| Updated time | system\_metadata.updated\_at | system\_metadata.updated\_at | range filters, decay functions, and sort | 
| Metadata tag | metadata.key | metadata.key | term, terms, and exists filters | 
| Event IDs | — | event\_ids | term, terms (up to 10 IDs), and exists filters | 

Field names in a query use snake\_case. The same values appear in responses as camelCase members, for example `system_metadata.created_at` in a query and `systemMetadata.createdAt` in the response.

You can't refer to the actor or session fields in a query or sort. Scope a search with the `actorId` parameter and, for events, `sessionIds`. A query that references `system_metadata.actor_id` or `system_metadata.session_id` fails with `ValidationException`.

## Keyword, semantic, and hybrid queries
<a name="memory-search-query-types"></a>

### Keyword search
<a name="memory-search-keyword"></a>

A `match` query finds text that contains the query's words. Use it when the user's words are likely to appear in the memory.

```json
{ "match": { "memory_text": "window seat" } }
```

### Semantic search
<a name="memory-search-semantic"></a>

A `neural` query finds text with a similar meaning, whether or not it shares words with the query. Give it the natural-language `query_text` and the number of nearest results, `k`, up to 100. OpenSearch Memory converts the query text to an embedding for you.

```json
{ "neural": { "memory_vector": { "query_text": "where does the user like to sit on a plane", "k": 10 } } }
```

### Hybrid search
<a name="memory-search-hybrid"></a>

A `hybrid` query combines a keyword query and a semantic query into one ranked list. It usually gives the best results for agent recall, because it finds both exact matches and paraphrases.

```json
{
    "hybrid": {
        "queries": [
            { "match":  { "memory_text": "seat" } },
            { "neural": { "memory_vector": { "query_text": "seating preference", "k": 10 } } }
        ]
    }
}
```

A query can contain only one distinct `neural` query text, and the text can be up to 2,048 characters.

## Filtering and sorting
<a name="memory-search-filtering"></a>

Use a `bool` query to combine a relevance query with filters. Filters narrow the results without affecting the score. The following example finds memories about recipes that were created in the last 30 days and carry the tag `channel=web`.

```json
{
    "bool": {
        "must": [
            { "neural": { "memory_vector": { "query_text": "food the user likes", "k": 20 } } }
        ],
        "filter": [
            { "term":  { "metadata.channel": "web" } },
            { "range": { "system_metadata.created_at": { "gte": "now-30d" } } }
        ]
    }
}
```

To prefer recent memories without excluding older ones, use a `function_score` query with a decay function on a time field. To order results by time instead of relevance, use `sort`.

```json
"sort": [ { "system_metadata.updated_at": { "order": "desc" } } ]
```

Relevance scores are not normalized to a fixed range and can be greater than 1. Use them only to order results within one response.

## Supported query types and limits
<a name="memory-search-limits"></a>

OpenSearch Memory supports the following query types: `match`, `match_phrase`, `match_all`, `term`, `terms`, `ids`, `exists`, `range`, `neural`, `hybrid`, `bool`, `constant_score`, `boosting`, and `function_score`. A `range` query can be used only on the time fields. A `function_score` query can use only decay functions, and only on the time fields.

Aggregations, highlighting, rescoring, and the `from` and `size` parameters aren't supported. Use `maxResults` and `nextToken` to control the number of results.

A query that uses an unsupported query type, such as `knn`, `fuzzy`, or `wildcard`, fails with `ValidationException`. So does a query that exceeds any of the following limits. For the complete list, see [Endpoints and quotas for Amazon OpenSearch Memory](memory-quotas.md).


| Limit | Value | 
| --- | --- | 
| Size of query and sort together | 64 KB | 
| Clauses in a query, counting function\_score functions | 32 | 
| Nesting depth of bool queries | 5 | 
| Values in a terms or ids query | 100 | 
| Decay functions in a function\_score query | 3 | 
| Distinct neural query texts | 1 | 
| Length of a neural query text | 2,048 characters | 
| k in a neural query | 100 | 
| Event IDs in a terms query on event\_ids | 10 | 
| Size of one response | 5 MiB | 

When a request fails validation, the `ValidationException` includes a `reason` that identifies the rule, such as `disallowedQueryType` or `nonFilterableField`. For more information, see [Error handling in Amazon OpenSearch Memory](memory-errors.md).

## Paginating results
<a name="memory-search-pagination"></a>

A search returns up to `maxResults` results per page, from 1 to 100. The default is 20. If more results are available, the response includes a `nextToken`. Pass it in the next request to get the next page. OpenSearch Memory limits how far you can page through one search's results. A request past that limit fails with `ValidationException` and the reason `invalidNextToken`, and the message states the limit. To find specific results, narrow the query instead of paging deeper.

If a response would be larger than 5 MiB, the request fails. Lower `maxResults` and try again.