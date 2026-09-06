

# Implementing a semantic cache with ElastiCache for Valkey
<a name="semantic-caching-implementation"></a>

The following walkthrough shows how to implement a read-through semantic cache using ElastiCache for Valkey with Amazon Bedrock.

## Step 1: Create an ElastiCache for Valkey cluster
<a name="semantic-caching-step1"></a>

Create an ElastiCache for Valkey cluster with version 8.2 or later using the AWS CLI:

```
aws elasticache create-replication-group \
  --replication-group-id "valkey-semantic-cache" \
  --cache-node-type cache.r7g.large \
  --engine valkey \
  --engine-version 8.2 \
  --num-node-groups 1 \
  --replicas-per-node-group 1
```

## Step 2: Connect to the cluster and configure embeddings
<a name="semantic-caching-step2"></a>

From your application code running on your Amazon EC2 instance, connect to the ElastiCache cluster and set up the embedding model:

```
from valkey.cluster import ValkeyCluster
from langchain_aws import BedrockEmbeddings

# Connect to ElastiCache for Valkey
valkey_client = ValkeyCluster(
    host="mycluster.xxxxxx.clustercfg.use1.cache.amazonaws.com",  # Your cluster endpoint
    port=6379,
    decode_responses=False
)

# Set up Amazon Bedrock Titan embeddings
embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0",
    region_name="us-east-1"
)
```

Replace the host value with your ElastiCache cluster's configuration endpoint. For instructions on finding your cluster endpoint, see [Accessing your ElastiCache cluster](accessing-elasticache.md).

## Step 3: Create the vector index for the semantic cache
<a name="semantic-caching-step3"></a>

Configure a ValkeyStore that automatically embeds queries using an HNSW index with COSINE distance for vector search:

```
from langgraph_checkpoint_aws import ValkeyStore
from hashlib import md5

store = ValkeyStore(
    client=valkey_client,
    index={
        "collection_name": "semantic_cache",
        "embed": embeddings,
        "fields": ["query"],           # Fields to vectorize
        "index_type": "HNSW",          # Vector search algorithm
        "distance_metric": "COSINE",   # Similarity metric
        "dims": 1024                   # Titan V2 produces 1024-d vectors
    }
)
store.setup()

def cache_key_for_query(query: str):
    """Generate a deterministic cache key for a query."""
    return md5(query.encode("utf-8")).hexdigest()
```

**Note**  
ElastiCache for Valkey uses an index to provide fast and accurate vector search. The `FT.CREATE` command creates the underlying index. For more information, see [Vector search for ElastiCache](search.md).

## Step 4: Implement cache search and update functions
<a name="semantic-caching-step4"></a>

Create functions to search the cache for semantically similar queries and to store new query-response pairs:

```
def search_cache(user_message: str, k: int = 3, min_similarity: float = 0.8):
    """Look up a semantically similar cached response from ElastiCache."""
    hits = store.search(
        namespace="semantic-cache",
        query=user_message,
        limit=k
    )
    if not hits:
        return None

    # Sort by similarity score (highest first)
    hits = sorted(hits, key=lambda h: h["score"], reverse=True)
    top_hit = hits[0]
    score = top_hit["score"]

    if score < min_similarity:
        return None  # Below similarity threshold

    return top_hit["value"]["answer"]  # Return cached answer


def store_cache(user_message: str, result_message: str):
    """Store a new query-response pair in the semantic cache."""
    key = cache_key_for_query(user_message)
    store.put(
        namespace="semantic-cache",
        key=key,
        value={
            "query": user_message,
            "answer": result_message
        }
    )
```

## Step 5: Implement the read-through cache pattern
<a name="semantic-caching-step5"></a>

Integrate the cache into your application's request handling:

```
import time

def handle_query(user_message: str) -> dict:
    """Handle a user query with read-through semantic cache."""
    start = time.time()

    # Step 1: Search the semantic cache
    cached_response = search_cache(user_message, min_similarity=0.8)

    if cached_response:
        # Cache hit - return cached response
        elapsed = (time.time() - start) * 1000
        return {
            "response": cached_response,
            "source": "cache",
            "latency_ms": round(elapsed, 1),
        }

    # Step 2: Cache miss - invoke LLM
    llm_response = invoke_llm(user_message)  # Your LLM invocation function

    # Step 3: Store the response in cache for future reuse
    store_cache(user_message, llm_response)

    elapsed = (time.time() - start) * 1000
    return {
        "response": llm_response,
        "source": "llm",
        "latency_ms": round(elapsed, 1),
    }
```

## Underlying Valkey commands
<a name="semantic-caching-valkey-commands"></a>

The following table shows the Valkey commands used to implement the semantic cache:


| Operation | Valkey command | Typical latency | 
| --- | --- | --- | 
| Create index | FT.CREATE semantic\_cache SCHEMA query TEXT answer TEXT embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 1024 DISTANCE\_METRIC COSINE | One-time setup | 
| Cache lookup | FT.SEARCH semantic\_cache "\*=>[KNN 3 @embedding $query\_vec]" PARAMS 2 query\_vec [bytes] DIALECT 2 | Microseconds | 
| Store response | HSET cache:{hash} query "..." answer "..." embedding [bytes] | Microseconds | 
| Set TTL | EXPIRE cache:{hash} 82800 | Microseconds | 
| LLM inference (miss) | External API call to Amazon Bedrock | 500–6000 ms | 