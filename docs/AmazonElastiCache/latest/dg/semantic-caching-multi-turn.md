

# Multi-turn conversation caching
<a name="semantic-caching-multi-turn"></a>

For applications with multi-turn conversations, the same user message can mean different things depending on context. For example, "Tell me more" in a conversation about Valkey means something different from "Tell me more" in a conversation about Python.

## The challenge
<a name="semantic-caching-multi-turn-challenge"></a>

Single-prompt caching works well for stateless queries. In multi-turn conversations, you must cache the full conversation context, not just the last message:

```
# "Tell me more" means nothing without context
# Conversation A: "What is Valkey?" -> "Tell me more"  (about Valkey)
# Conversation B: "What is Python?" -> "Tell me more"  (about Python)
```

## Strategy: context-aware cache keys
<a name="semantic-caching-context-aware-keys"></a>

Instead of embedding only the last user message, embed a summary of the full conversation context. This way, similar follow-up questions in similar conversation flows can reuse cached answers.

```
def build_context_string(messages: list) -> str:
    """Build a cacheable context string from conversation messages."""
    # Use last 3 turns (6 messages: user + assistant pairs)
    recent = messages[-6:]
    parts = []
    for msg in recent:
        role = msg["role"]
        content = msg["content"][:200]  # Truncate long messages
        parts.append(f"{role}: {content}")
    return " | ".join(parts)
```

## Per-user cache isolation with TAG filters
<a name="semantic-caching-tag-filters"></a>

Use TAG fields to isolate cached conversations by user, session, or other dimensions. This prevents one user's cached conversations from being returned for another user:

```
# Create index with TAG field for per-user isolation
valkey_client.execute_command(
    "FT.CREATE", "conv_cache_idx",
    "SCHEMA",
    "context_summary", "TEXT",
    "response", "TEXT",
    "user_id", "TAG",
    "turn_count", "NUMERIC",
    "embedding", "VECTOR", "HNSW", "6",
    "TYPE", "FLOAT32",
    "DIM", "1024",
    "DISTANCE_METRIC", "COSINE",
)
```

Search with hybrid filtering (TAG \+ KNN):

```
def lookup_conversation_cache(messages: list, user_id: str, threshold: float = 0.12):
    """Search cache for similar conversation contexts, scoped to a user.

    Note: FT.SEARCH with COSINE distance returns a distance score where
    0 = identical and 2 = opposite. A lower score means higher similarity.
    The threshold here is a maximum distance: only return results closer
    than this value.
    """
    context = build_context_string(messages)
    query_vec = get_embedding(context)

    # Hybrid search: filter by user_id TAG + KNN on context embedding
    results = valkey_client.execute_command(
        "FT.SEARCH", "conv_cache_idx",
        f"@user_id:{{{user_id}}}=>[KNN 1 @embedding $query_vec]",
        "PARAMS", "2", "query_vec", query_vec,
        "DIALECT", "2",
    )

    if results[0] > 0:
        fields = results[2]
        field_dict = {fields[j]: fields[j+1] for j in range(0, len(fields), 2)}
        distance = float(field_dict.get("__embedding_score", "999"))
        if distance < threshold:  # Lower distance = more similar
            return {"hit": True, "response": field_dict.get("response", ""), "distance": distance}

    return {"hit": False}
```

**Note**  
The `@user_id:{user_123}` TAG filter ensures that User A's cached conversations don't leak to User B. The hybrid query (TAG \+ KNN) runs as a single atomic operation — pre-filtering by user, then finding the nearest conversation context.

## Cache isolation strategies
<a name="semantic-caching-isolation-strategies"></a>


| Strategy | TAG filter | Best for | 
| --- | --- | --- | 
| Per-user | @user\_id:{user\_123} | Personalized assistants | 
| Per-session | @session\_id:{sess\_abc} | Short-lived chats | 
| Global (shared) | No filter (\*) | FAQ bots, common queries | 
| Per-model | @model:{gpt-4} | Multi-model deployments | 
| Per-product | @product\_id:{prod\_456} | E-commerce assistants | 