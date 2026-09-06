

# Semantic long-term memory for LangGraph agents
<a name="ddb-langgraph-memory"></a>

LangGraph separates two kinds of agent state. Short-term state is the conversation thread itself, which a checkpointer persists so a thread can resume, replay, and recover (see [Using DynamoDB as a checkpoint store for LangGraph agents](ddb-langgraph-checkpoint.md)). Long-term memory is what the agent knows across threads, and LangGraph models it as a store: a namespaced key-value surface the agent writes to deliberately and reads back later.

The `DynamoDBStore` class, in the [langgraph-checkpoint-aws](https://pypi.org/project/langgraph-checkpoint-aws/) package, is the DynamoDB implementation of that store. It handles the key-value side with hierarchical namespaces, Time to Live for expiring stale memories, and basic filtering. With a vector index configured (see [Using vector indexes in DynamoDB](VectorSearch.md)), its `search()` method performs semantic search: memories are embedded on write, indexed asynchronously, and recalled by meaning, ranked by similarity, from the same table that holds them. There is no separate vector database to provision and no pipeline copying data into it.

## Prerequisites
<a name="langgraph-memory-prerequisites"></a>
+ An AWS account with permission to create DynamoDB tables and invoke Amazon Bedrock models
+ Access to an embeddings model in Amazon Bedrock in your Region. These examples use Amazon Titan Text Embeddings V2
+ Python 3.10 or later, with `langgraph-checkpoint-aws` 1.2.2 or later and `boto3` 1.43.64 or later (earlier `boto3` versions have no `SearchVectors` operation)

Install the libraries using pip:

```
pip install langgraph langgraph-checkpoint-aws langchain-aws
```

## Set up the store
<a name="langgraph-memory-setup"></a>

Configure the store with an `index` block and call `setup()`:

```
from langchain_aws import BedrockEmbeddings
from langgraph_checkpoint_aws import DynamoDBStore

store = DynamoDBStore(
    table_name="support-agent-memory",
    region_name="us-east-1",
    index={
        "embed": BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0"),
        "dims": 1024,
        "fields": ["text"],
        "distance_function": "COSINE",
    },
)

store.setup()
```

Four settings in the `index` block are worth understanding:
+ `embed` takes any LangChain embeddings object, or a plain callable that maps a list of strings to a list of vectors.
+ `dims` must match your model's output size. Titan Text Embeddings V2 returns 1,024 dimensions by default. If these disagree, the store raises a dimension mismatch error naming both numbers on the first write, rather than writing vectors the index can't use.
+ `fields` selects which parts of the value get embedded. Here only the `text` field is embedded. The default, `["$"]`, serializes the whole value to JSON and embeds that, which is convenient but also embeds your bookkeeping attributes.
+ `distance_function` defaults to `COSINE`, and also accepts `EUCLIDEAN` and `DOT_PRODUCT`.

`setup()` creates the table if it's absent, attaches the vector index, and enables Time to Live if you configured it. On an existing table, it adds only what's missing, so existing `DynamoDBStore` deployments can adopt semantic search without recreating the table or migrating items. Keep in mind that `setup()` doesn't return until the index reports `ACTIVE` and is no longer backfilling: an index that reports `ACTIVE` while still backfilling rejects `SearchVectors` calls. On a new empty table the wait is short. Retrofitting onto a table with existing items takes as long as the backfill takes.

## Write memories
<a name="langgraph-memory-write"></a>

Writing is an ordinary `put()`. The embedding happens for you:

```
namespace = ("memories", "acme-corp", "user-8812")

store.put(namespace, "mem-1", {
    "text": "Account runs a proxy that closes idle sockets after 60 seconds",
    "source": "ticket-4471",
})
store.put(namespace, "mem-2", {
    "text": "Customer prefers email, asked not to be called by phone",
    "source": "ticket-4471",
})
store.put(namespace, "mem-3", {
    "text": "Uses a custom build of the SDK pinned to version 2.14",
    "source": "ticket-4502",
})
```

## Recall by meaning
<a name="langgraph-memory-recall"></a>

The customer opens a new conversation and says their connection keeps dropping after about a minute:

```
results = store.search(
    namespace,
    query="connection drops after a minute of inactivity",
    limit=3,
)

for item in results:
    print(round(item.score, 3), item.value["text"])
```

Output:

```
0.324 Account runs a proxy that closes idle sockets after 60 seconds
0.039 Customer prefers email, asked not to be called by phone
0.031 Uses a custom build of the SDK pinned to version 2.14
```

The relevant memory ranks first, and no key in the query matched anything. `SearchItem.score` follows the LangGraph convention where higher is more relevant. DynamoDB returns a distance, where lower is closer, so the store converts: for `COSINE` the score is `1 - distance`, for `EUCLIDEAN` it is `1 / (1 + distance)`, and `DOT_PRODUCT` scores pass through unchanged. If you gate on an absolute score to decide whether a memory is relevant enough to inject into a prompt, calibrate that threshold against your own data and your chosen distance function.

## Scope memory with the search schema
<a name="langgraph-memory-scoping"></a>

When `DynamoDBStore` creates the vector index, it declares the table's partition key as a `HASH` element in the index search schema. Because that element exists, every search must supply a condition for it, and the store supplies the namespace: the namespace tuple is joined to form the partition key value, so every semantic search is pinned to exactly one namespace. Three consequences follow:
+ **Isolation is structural, not a filter you remember to write.** A search cannot reach a memory in a different namespace, so a store serving many tenants has no query shape that returns another tenant's memories. This is query scoping rather than authorization: a principal with `dynamodb:SearchVectors` permission on the table can search any namespace value directly, so deciding which namespaces a caller may read still belongs to IAM and your application's authorization layer.
+ **Recall cost tracks one user's memory, not your whole table.** The search work is bounded by how much that one namespace holds, not by how many memories your whole product holds, which keeps both latency and vector search cost small and stable as you grow.
+ **Semantic search is exact-namespace, not prefix.** A search reaches exactly the namespace you pass and nothing beneath it. Searching `("memories", "acme-corp")` does not reach `("memories", "acme-corp", "user-8812")`, because those are different partition key values. Your namespace is your recall scope, so choose it to match the scope you want a single search to see.

The following table summarizes how to choose a namespace shape.


| Namespace shape | One `search()` reaches | Choose it when | 
| --- | --- | --- | 
| `("memories", user_id)` | That user's memories | Single-tenant product with per-user recall | 
| `("memories", tenant_id, user_id)` | That user, at that tenant | Multi-tenant, the common case | 
| `("memories", tenant_id, user_id, agent_name)` | One agent's notes on that user | Multiple specialized agents that shouldn't read each other's notes | 
| `("account_facts", tenant_id)` | Tenant-wide knowledge | Facts that apply to every user at an account | 

Avoid putting every memory in one namespace and filtering on metadata: filters are applied after DynamoDB has already selected the nearest matches across the entire namespace, and a single search returns at most the top 100 matches, so once one busy tenant fills the top 100 for a common query, a quieter tenant's search returns fewer results than requested even though their memories are present. Prefer namespace scoping over filters for anything that determines correctness. Going finer than your recall boundary is a legitimate design too: an agent that needs both user-specific and account-wide context searches both namespaces and merges the results.

## Considerations
<a name="langgraph-memory-considerations"></a>
+ The index is eventually consistent, the same model as a global secondary index. A `search()` issued immediately after a `put()` may not include the new memory yet. For an agent that writes a memory and then recalls it within the same turn, read it back by key instead.
+ A single search returns at most the top 100 matches. A request whose `limit` plus `offset` exceeds it is rejected with a clear error rather than silently returning nothing beyond the cap.
+ If you use Time to Live to expire stale memories and enable refresh on read, a memory the agent actually recalls has its expiry pushed out, so the memories in active use are not the ones quietly disappearing.
+ Vector search failures raise so your application can react. A throttle, a permissions problem, and a genuinely empty result would look identical if the store returned an empty list on failure.
+ Vector operations bill in their own units, metered separately from base table read and write request units, and both scale with the number of dimensions. A smaller embedding dimension is cheaper on every write and every search, so use the smallest dimension that holds your recall quality.
+ Memories written with no text in the configured `fields` are stored without an embedding and won't appear in semantic results. The store logs a warning when this happens.

## Additional resources
<a name="langgraph-memory-resources"></a>
+ [DynamoDBStore documentation on GitHub](https://github.com/langchain-ai/langchain-aws/blob/main/libs/langgraph-checkpoint-aws/langgraph_checkpoint_aws/store/dynamodb/DynamoDBStore.md)
+ [langgraph-checkpoint-aws on PyPI](https://pypi.org/project/langgraph-checkpoint-aws/)
+ [LangGraph documentation](https://langchain-ai.github.io/langgraph/)