

# Amazon ElastiCache (Valkey) for e-commerce applications
<a name="ecommerce-caching-valkey"></a>

An e-commerce application benefits from an in-memory cache layer between the application servers and the database. Amazon ElastiCache running Valkey provides sub-millisecond read latency for frequently accessed data — product catalog entries, inventory counts, search results, and user sessions — reducing database load and improving response times during traffic spikes.

## Cluster configuration
<a name="ecommerce-cache-cluster-config"></a>

Choose a cluster type based on your data volume, throughput requirements, and operational preferences.


**Cluster type comparison for e-commerce**  

| Cluster type | Best for | Scaling | Considerations | 
| --- | --- | --- | --- | 
| Serverless | Variable traffic patterns, new applications, teams without cache operations expertise | Automatic — scales compute and memory based on demand | No capacity planning needed. Variable cost model—you pay for what you consume. | 
| Node-based (cluster mode enabled) | Predictable high-throughput workloads, need for fine-grained control over sharding and node types | Manual or auto-scaling of shards and replicas | Requires capacity planning. Fixed cost model—you pay for provisioned capacity regardless of utilization. Supports up to 500 nodes per cluster. | 

For most e-commerce applications starting out, Serverless provides the simplest path to production. Migrate to node-based clusters when you have predictable traffic baselines and need more control over cluster topology, node types, and scaling behavior.


**Recommended cluster settings**  

| Setting | Value | Rationale | 
| --- | --- | --- | 
| Engine | Latest stable version | Use the latest stable Valkey release available in ElastiCache. Fully compatible with Redis OSS commands. Provides performance improvements over previous versions. | 
| Multi-AZ | Enabled | Automatic failover to a replica in another Availability Zone if the primary node fails. Required for production e-commerce workloads. | 
| In-transit encryption | Enabled (TLS) | Encrypts data between your application and the cache cluster. Required for workloads handling user sessions or any PII. | 
| At-rest encryption | Enabled | Encrypts data on disk (backups, swap). Required for compliance workloads. | 
| Subnet group | Private isolated subnets (2\+ AZs) | No internet access. Only reachable from your application's security group. | 

## Key design for product data
<a name="ecommerce-cache-key-design"></a>

Design cache keys to be predictable, debuggable, and scoped to avoid collisions across data types.


**Key naming conventions**  

| Data type | Key pattern | Value type | Example | 
| --- | --- | --- | --- | 
| Product details | `product:{id}` | Hash | `product:12345` → {name, price, description, imageUrl} | 
| Inventory count | `inventory:{sku}` | String (integer) | `inventory:SKU-A100` → 42 | 
| User session | `session:{sessionId}` | Hash | `session:abc123` → {userId, cart, lastAccess} | 
| Search results | `search:{queryHash}` | String (JSON) | `search:sha256(q=shoes&page=1)` → [product IDs] | 
| Category listing | `category:{slug}:page:{n}` | List | `category:electronics:page:1` → [product IDs] | 

Key design best practices:
+ Use colons as separators for readability and tooling support.
+ Keep keys short — long keys consume memory and network bandwidth.
+ Include the data type prefix to avoid collisions between products, sessions, and other entities that might share numeric IDs.
+ Use hashes for multi-field objects (products, sessions) to allow partial reads and updates without retrieving the entire value.

## TTL strategy by data type
<a name="ecommerce-cache-ttl"></a>

Set TTL (time-to-live) values based on how frequently data changes and how stale it can be without affecting the customer experience.


**Recommended TTLs for e-commerce data**  

| Data type | TTL | Invalidation trigger | Rationale | 
| --- | --- | --- | --- | 
| Product details | 5 minutes | Seller edits product | Product descriptions and images change infrequently. Short enough to pick up edits reasonably quickly without explicit invalidation for every change. | 
| Inventory count | 30 seconds | Purchase or restock | Stale inventory can cause overselling. Very short TTL ensures counts refresh frequently. Explicit invalidation on purchase for immediate accuracy. | 
| Search results | 60 seconds | None (TTL-based only) | Search indexes update periodically. Caching reduces search engine load. New products appear within 60 seconds without explicit invalidation. | 
| User session | 24 hours | Logout or session expiry | Sessions persist across browsing. Refresh TTL on each access to keep active sessions alive. Delete explicitly on logout. | 
| Category listing | 2 minutes | Product added/removed from category | Category pages are high-traffic. Brief caching reduces database queries substantially during browsing. | 

## Cache-aside pattern
<a name="ecommerce-cache-aside-pattern"></a>

The cache-aside pattern (also called lazy loading) is the most common caching strategy for e-commerce applications. Your application checks the cache first, and only queries the database on a cache miss.

**Read path (pseudocode)**  


```
FUNCTION getProduct(productId):
    cacheKey = "product:" + productId

    // Step 1: Check the cache
    cachedValue = cache.GET(cacheKey)

    IF cachedValue exists:
        RETURN deserialize(cachedValue)    // Cache hit — sub-millisecond

    // Step 2: Cache miss — query database
    product = database.query("SELECT * FROM products WHERE id = ?", productId)

    IF product not found:
        RETURN null

    // Step 3: Write to cache with TTL
    cache.SET(cacheKey, serialize(product), EXPIRE = 300)    // 5 minutes

    RETURN product
```

**Write path (pseudocode)**  


```
FUNCTION updateProduct(productId, updatedFields):
    // Step 1: Update the database (source of truth)
    database.update("UPDATE products SET ... WHERE id = ?", updatedFields, productId)

    // Step 2: Invalidate the cache (don't update it)
    cache.DELETE("product:" + productId)

    // Next read will trigger a cache miss and repopulate from database
```

**Important**  
Always invalidate (delete) rather than update the cache on writes. This reduces the window for race conditions where a stale read overwrites a newer value. The next read repopulates the cache from the database, which is the source of truth. Note that a narrow race condition still exists—if a concurrent read fetches data from the database before the write occurs, it can repopulate the cache with stale data after the cache key has already been deleted. For most e-commerce workloads, the short TTL makes this acceptable. If you need strict consistency, use a distributed lock or versioned writes.

**Handling cache failures**  


```
FUNCTION getProductWithFallback(productId):
    TRY:
        RETURN getProduct(productId)    // Normal cache-aside path
    CATCH cacheConnectionError:
        // Cache is unavailable — fall back to database directly
        RETURN database.query("SELECT * FROM products WHERE id = ?", productId)
        // Log the error, trigger an alarm, but don't fail the request
```

Design your application so cache failure degrades performance (slower responses) but doesn't break functionality. The database serves as the fallback.

## Cache invalidation strategies
<a name="ecommerce-cache-invalidation"></a>

Invalidation ensures users see current data after updates. Choose a strategy based on how quickly changes must be visible.


**Invalidation approaches**  

| Approach | How it works | When to use | 
| --- | --- | --- | 
| Delete on write | Application deletes the cache key immediately after updating the database. | Most writes (product edits, inventory changes). Simple, reliable, avoids stale data. | 
| TTL expiration only | Don't invalidate — let the TTL expire naturally. | Data where brief staleness is acceptable (search results, category listings, analytics). | 
| Event-driven invalidation | A background process listens to database change events and invalidates affected keys. | Systems where the write path and cache are in different services, or when a single database change affects many cache keys. | 

For marketplace applications that also use Amazon CloudFront as a CDN layer, coordinate invalidation across both tiers: delete the ElastiCache key *and* send a CloudFront cache invalidation (or cache-tag invalidation) so users see updated content at both the application and edge layers.

## Connection management
<a name="ecommerce-cache-connections"></a>
+ **Use connection pooling** — Creating a new TLS connection for each cache operation adds latency. Maintain a pool of persistent connections and reuse them across requests.
+ **Set connection timeouts** — Use a short connection timeout (1–2 seconds) and a shorter command timeout (100–500 ms). If the cache doesn't respond quickly, fall back to the database rather than blocking the request.
+ **Handle failover gracefully** — When Multi-AZ failover occurs, connections to the old primary break. Your connection pool should detect broken connections and reconnect automatically. Most client libraries handle this, but verify the behavior under test.
+ **Use the cluster's configuration endpoint** — For cluster mode enabled, connect to the configuration endpoint rather than individual node endpoints. The configuration endpoint routes requests to the correct shard automatically.

## Key metrics to monitor
<a name="ecommerce-cache-monitoring"></a>


**Recommended Amazon CloudWatch alarms for e-commerce cache**  

| Metric | Threshold | Period | Action | 
| --- | --- | --- | --- | 
| CacheHitRate | < 80% | 5 min | Investigate — low hit rate means your TTLs may be too short, keys are poorly designed, or working set exceeds memory. | 
| EngineCPUUtilization | > 70% | 5 min | Scale up (larger nodes) or scale out (more shards). High CPU indicates the cache is processing more commands than it can handle efficiently. | 
| DatabaseMemoryUsagePercentage | > 80% | 5 min | Risk of evictions. Increase memory (scale up) or reduce stored data (shorter TTLs, fewer cached data types). | 
| Evictions | > 0 sustained | 1 min | Cache is full and removing data to make room. Increases cache misses. Scale up memory or reduce TTLs on less-critical data. | 
| CurrConnections | > 80% of your client pool size | 5 min | Connection pool nearing exhaustion. Increase pool size, reduce connection hold time, or investigate connection leaks in application code. Base the threshold on your application's configured pool size, not the server maximum (65,000). | 

## Frequently asked questions
<a name="ecommerce-cache-faq"></a>

### When should I use Serverless vs. node-based?
<a name="ecommerce-cache-faq-serverless-vs-node"></a>

Use Serverless when your traffic is unpredictable (new marketplace, seasonal spikes), when you want to avoid capacity planning, or when your team doesn't have caching operations expertise. Switch to node-based when your traffic patterns are stable, you need fine-grained control over sharding, or your sustained throughput makes node-based more cost-effective.

### Should I use Valkey or Redis OSS?
<a name="ecommerce-cache-faq-valkey-vs-redis"></a>

Use Valkey for new deployments. Valkey is the default engine for new ElastiCache clusters, is fully compatible with Redis OSS commands and data structures, and receives continued development. Existing Redis OSS clusters continue to work — migrate to Valkey when convenient using the in-place engine upgrade.

### What happens when the cache is unavailable?
<a name="ecommerce-cache-faq-failure"></a>

Your application should treat the cache as an optimization, not a dependency. If the cache is unavailable, fall back to querying the database directly. Response times will be higher, but the application remains functional. With Multi-AZ enabled, complete cache unavailability is rare — failover to a replica typically completes in under 30 seconds.

### How do I estimate the memory I need?
<a name="ecommerce-cache-faq-sizing"></a>

Calculate: (number of unique items to cache) × (average size per item) × (overhead factor of 1.2 for Valkey data structures). The overhead varies by object size and data type—smaller objects have proportionally higher overhead. For example, 100,000 products at 2 KB each with 1.2x overhead = approximately 240 MB. Add session data, search results, and inventory counts. Start with headroom (use 60% of available memory as your target) and monitor the DatabaseMemoryUsagePercentage metric to adjust.