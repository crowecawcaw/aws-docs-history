

# Best practices
<a name="semantic-caching-best-practices"></a>

## Choosing data that can be cached
<a name="semantic-caching-bp-choosing-data"></a>

Semantic caching is well suited for repeated queries whose responses are relatively stable, whereas real-time or highly dynamic responses are often poor candidates for caching.

Use tag and numeric filters derived from existing application context (such as product ID, category, region, or user segment) to decide which queries and responses are eligible for caching and to improve the relevance of cache hits.

## Similarity threshold tuning
<a name="semantic-caching-bp-threshold"></a>

The similarity threshold controls the trade-off between cache hit rate and answer quality. Choose a threshold that balances cost savings with accuracy for your use case:


| Threshold | Hit rate | Quality risk | Best for | 
| --- | --- | --- | --- | 
| 0.95 (strict) | Low (\~25%) | Very low | Medical, legal, financial applications | 
| 0.90 (moderate) | Medium (\~55%) | Low | General chatbots | 
| 0.80 (balanced) | High (\~75%) | Low–Medium | FAQ bots, IT support | 
| 0.75 (relaxed) | Very high (\~90%) | Medium | High-volume repetitive queries | 

**Important**  
Start with a higher threshold (0.90–0.95) and gradually lower it while monitoring accuracy. Use A/B testing to find the optimal balance for your workload.

## Standalone queries versus conversations
<a name="semantic-caching-bp-standalone-vs-conversations"></a>
+ **For standalone queries** – Apply semantic caching directly on the user query text.
+ **For multi-turn conversations** – First use your conversation memory to retrieve the key facts and recent messages needed to answer the current turn. Then apply semantic caching to the combination of the current user message and the retrieved context, instead of embedding the entire raw dialogue.

## Setting cache invalidation periods
<a name="semantic-caching-bp-ttl"></a>

Use TTL to control how long cached responses are served before they are regenerated on a cache miss.


| Data type | Recommended TTL | Rationale | 
| --- | --- | --- | 
| Static facts (documentation, policies) | 24 hours | Facts change infrequently | 
| Product information | 12–24 hours | Updated daily in most catalogs | 
| General assistant responses | 1–4 hours | Balance freshness with hit rate | 
| Real-time data (prices, inventory) | 5–15 minutes | Data changes frequently | 
| Conversation context | 30 minutes | Session-scoped, short-lived | 

```
# Set TTL with random jitter to spread out cache invalidations
import random

base_ttl = 82800  # ~23 hours
jitter = random.randint(0, 3600)  # Up to 1 hour of jitter
valkey_client.expire(cache_key, base_ttl + jitter)
```

**Tip**  
Set TTLs that match your application use case and how often your data or model outputs change. Longer TTLs increase cache hit rates but raise the risk of outdated answers. Shorter TTLs keep responses fresher but lower cache hit rates and require more LLM inference.

## Monitoring and cost tracking
<a name="semantic-caching-bp-monitoring"></a>

Track cache performance metrics to optimize your semantic cache over time:

```
def record_cache_event(valkey_client, event_type: str):
    """Track cache hits and misses using atomic counters."""
    valkey_client.incr(f"cache:metrics:{event_type}")

    # Also track hourly for time-series analysis
    from datetime import datetime
    hour_key = datetime.now().strftime("%Y%m%d%H")
    counter_key = f"cache:metrics:{event_type}:{hour_key}"
    valkey_client.incr(counter_key)
    valkey_client.expire(counter_key, 86400 * 7)  # Keep 7 days

def get_cache_stats(valkey_client) -> dict:
    """Get current cache performance metrics."""
    hits = int(valkey_client.get("cache:metrics:hit") or 0)
    misses = int(valkey_client.get("cache:metrics:miss") or 0)
    total = hits + misses
    hit_rate = hits / total if total > 0 else 0

    avg_cost_per_call = 0.015  # Example: ~$0.015 per LLM call
    savings = hits * avg_cost_per_call

    return {
        "total_requests": total,
        "hits": hits,
        "misses": misses,
        "hit_rate": round(hit_rate, 3),
        "estimated_savings_usd": round(savings, 2),
    }
```

## Memory management
<a name="semantic-caching-bp-memory"></a>
+ **Set maxmemory policy** – Configure `maxmemory-policy allkeys-lru` on your ElastiCache cluster to automatically evict least-recently-used cache entries when the cluster reaches its memory limit.
+ **Plan for capacity** – Each cache entry typically requires approximately 4–6 KB (embedding dimensions × 4 bytes \+ query text \+ response text). A 1 GB ElastiCache instance can store approximately 170,000 cached entries.
+ **Use cache invalidation for stale data** – When underlying data changes, use text search to find and invalidate related cache entries:

  ```
  def invalidate_by_topic(valkey_client, topic_keyword: str):
      """Remove cached entries matching a topic after a data update."""
      results = valkey_client.execute_command(
          "FT.SEARCH", "semantic_cache",
          f"@query:{topic_keyword}",
          "NOCONTENT",  # Only return keys, not fields
      )
  
      if results[0] > 0:
          keys = results[1:]
          for key in keys:
              valkey_client.delete(key)
          print(f"Invalidated {len(keys)} cached entries for '{topic_keyword}'")
  ```