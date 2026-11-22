

# Billing for DynamoDB caching

Amazon DynamoDB caching is available at no additional cost. You pay only for the Amazon ElastiCache Serverless and DynamoDB resources used. For more information, see the [ElastiCache Serverless pricing page](https://aws.amazon.com/elasticache/pricing/).

## Storage
<a name="ddb-caching-billing-storage"></a>

You pay for the memory used to store cached DynamoDB item projections, queries, and scans including overhead for each entry. Each distinct projection of an item is its own cache entry. Caching multiple projections of the same item uses storage equivalent to the sum of all projections plus caching overhead.

## ECPU
<a name="ddb-caching-billing-ecpu"></a>

DynamoDB caching consumes 1 ECPU for each 1 KB of processed data. Writes refresh all cached entries for the updated items, except for UpdateItem requests that do not set the ReturnValues parameter to ALL\_NEW. Because each projection is a separate cache entry (see [Storage](#ddb-caching-billing-storage)), items with multiple cached projections consume more ECPUs for each write.


**ECPUs consumed by DynamoDB caching requests**  

| Request | What it does | ECPUs used | 
| --- | --- | --- | 
| Cache hit | Returns a cached entry | 1× (entry size in KB \+ overhead) | 
| Cache miss | Reads from DynamoDB, then stores the result | 2× (entry size in KB \+ overhead) | 
| Write | Writes to DynamoDB, then updates the cache | 1× (write size in KB \+ overhead) \+ sum(updated entry sizes in KB \+ overhead) | 