

# How DynamoDB caching works

DynamoDB caching uses the [ElastiCache integration client library](https://github.com/awslabs/elasticache-integration-client) on the GitHub website to intercept your application's requests to Amazon DynamoDB, redirecting those requests to an Amazon ElastiCache Serverless for Valkey cache.

DynamoDB caching uses three primary components:
+ **The ElastiCache integration client** – A language-specific library you import and configure to enable DynamoDB caching with the AWS SDK for your application.
+ **ElastiCache Serverless** – The serverless cache that maintains cached data, routes requests to DynamoDB when required, and returns cached data to the client.
+ **DynamoDB tables** – The DynamoDB tables containing your data.

## Read processing
<a name="ddb-caching-how-it-works.read"></a>

Read requests take the following path:

1. Your application invokes a DynamoDB API through the AWS SDK.

1. If the request is for a table **not** configured for caching in the application or uses an API that is **not** supported for DynamoDB caching, the request is sent directly to DynamoDB.

1. If the request is for a table configured for caching and uses a supported API, the ElastiCache integration client sends the request to ElastiCache.

1. On a **cache hit**, the cached response is returned directly to your application.

1. On a **cache miss**, the request is forwarded to DynamoDB. The response is returned to your application and added to the cache with the configured TTL.

## Write processing
<a name="ddb-caching-how-it-works.write"></a>

Write requests take the following path with the default configuration:

1. Your application invokes a DynamoDB API through the AWS SDK.

1. If the request is for a table **not** configured for caching in the application or uses an API that is **not** supported for DynamoDB caching, the request is sent directly to DynamoDB.

1. If the request is for a table configured for caching and uses a supported API, the ElastiCache integration client sends the request to ElastiCache.

1. ElastiCache forwards the write to DynamoDB and returns the response to the client.

1. Any cached projections for the item are updated in the cache.

## Fallback behavior
<a name="ddb-caching-how-it-works.fallback"></a>

If the serverless cache is temporarily unavailable or the client connection times out, the ElastiCache integration client falls back to sending requests to DynamoDB directly. When the serverless cache becomes available again, the client begins directing requests to the cache automatically. You can configure the fallback timeout period or disable fallback entirely.

## Supported DynamoDB APIs
<a name="ddb-caching-how-it-works.apis"></a>

DynamoDB caching supports the following DynamoDB APIs:
+ BatchGetItem
+ BatchWriteItem
+ GetItem
+ DeleteItem
+ UpdateItem
+ PutItem
+ Query
+ Scan
+ TransactGetItems
+ TransactWriteItems

## How data is cached
<a name="ddb-caching-how-it-works.caching"></a>

There are three types of cache entries: item, query, and scan.

### Item cache
<a name="ddb-caching-how-it-works.caching.item"></a>

Item cache entries are created, updated, and deleted when item-level DynamoDB API (BatchGetItem, BatchWriteItem, GetItem, DeleteItem, UpdateItem, and PutItem) results are stored. An item cache entry is created for each primary key as a Valkey hash, where the hash key is formatted as `aws:ddb:item:<table>:<primarykey>` where table is the name or ARN of the DynamoDB table as provided in the request. All projections associated with the primary key are stored as hash fields, where the field name is formatted as `proj:<projection>`. Read requests with no ProjectionExpression parameter specified are cached with the field name `proj:*` (all attributes). Multiple read requests for the same primary key (the same item) with different projections result in multiple field entries under the item cache entry. This gives your application granular control over how data is cached through projection expressions.

GetItem requests perform a lookup for an exact projection field match under the item cache entry for the associated primary key. If an exact projection match is found, it is returned from the cache. If no exact projection is found, the request is forwarded to DynamoDB. If DynamoDB returns item data for the GetItem request, the data is returned to the requester and the projection is added to the cache. If no item projection data is returned by DynamoDB, by default a negative cache entry is created for the projection.

As an example, consider a DynamoDB table with a composite primary key, where the partition key is "Users" and the sort key is "Region". Two read requests are issued for partition key "Users:55555" and sort key "Region:NA":

1. A GetItem request with the ProjectionExpression parameter set to "email, first\_name". DynamoDB returns data for this request which is added to the cache.

1. A GetItem request with the ProjectionExpression parameter set to "email, last\_name". DynamoDB returns data for this request which is added to the cache.

```
aws:ddb:item:Users:55555=Region:NA
  ├─ proj:email,last_name → attribute data
  ├─ proj:email,first_name → attribute data
```

PutItem requests are forwarded to DynamoDB, and on success any cached projections associated with that item's primary key are updated with the new item attributes. If there are no associated projections for the PutItem primary key, no entries are added to the cache. You can change the default behavior to instead populate complete items in the cache for PutItem requests (see [Configuring DynamoDB caching](ddb-caching-configuration.md)).

DeleteItem requests are forwarded to DynamoDB, and on success the cache entry (and therefore any cached projections associated with that item's primary key) are invalidated (deleted).

UpdateItem requests are forwarded to DynamoDB, and on success if the ReturnValues parameter is set to ALL\_NEW, any cached projections associated with that item's primary key are updated. If the ReturnValues parameter is set to any value other than ALL\_NEW, the cache entry (and therefore any cached projections associated with that item's primary key) are invalidated (deleted).

### Query cache
<a name="ddb-caching-how-it-works.caching.query"></a>

Query cache entries are created when DynamoDB Query API results are stored. A single cache entry is created for each unique query request. Query cache keys are created using the key format `aws:ddb:query:<table>:<params>` where table is the name or ARN of the DynamoDB table as provided in the request and params is a normalized string containing the query parameters.

### Scan cache
<a name="ddb-caching-how-it-works.caching.scan"></a>

Scan cache entries are created when DynamoDB Scan API results are stored. A single cache entry is created for each unique scan request. Scan cache keys are created using the key format `aws:ddb:scan:<table>:<params>` where table is the name or ARN of the DynamoDB table as provided in the request and params is a normalized string containing the scan parameters.

Updates to item data are not automatically reflected in query or scan cache entries. If you want to ensure a cached query or scan has the latest table data, perform the query or scan operation with the ConsistentRead parameter set to true (a strongly consistent read) which forces the cache to run the query against the table and cache the returned result.

**Note**  
DynamoDB allows requests to specify a table using either the table name or a table ARN. If your application issues two otherwise identical requests where one request specifies a table name and the other request the table ARN, the results are stored as two different cache entries.

**Note**  
Cache entry values are encoded using an internal format and are subject to change. We strongly recommend against modifying cache entry values.

## Consistency model
<a name="ddb-caching-how-it-works.consistency"></a>

DynamoDB caching returns cached results when available for eventually consistent reads. Requests to DynamoDB that set the ConsistentRead parameter to true (strongly consistent reads) are routed through ElastiCache to DynamoDB, the result is returned to your application, and on success the projection is populated in the cache. You can use consistent reads to force a refresh of cached data.

Transaction API (TransactGetItems, TransactWriteItems) results are stored as individual item cache entries. DynamoDB caching does not provide transactional consistency guarantees for item cache entries added as the result of a transaction API.

## Time-to-live (TTL) expiration
<a name="ddb-caching-how-it-works.ttl"></a>

Cache entries have a time-to-live (TTL), after which the cached data is removed from the cache. The regular cache entry TTL (ttl) has a default of 5 minutes and can be set to any value from 1 to 86400 seconds. The negative cache entry TTL (negative\_ttl) has a default of 60 seconds and can be set to any value from 0 to 86400 seconds. Setting negative\_ttl to zero disables negative caching. For more information about configuring TTL settings, see [Configuring DynamoDB caching](ddb-caching-configuration.md).

## Negative caching
<a name="ddb-caching-how-it-works.negative"></a>

A request for DynamoDB data that is not available in the cache or in the source DynamoDB table results in the population of a negative cache entry in the cache. This negative cache entry returns an empty result for subsequent identical requests from the cache until the item is updated or the item's TTL expires, after which the negative cache entry is removed. Negative caching can reduce response times and DynamoDB table read traffic when applications frequently attempt to access data that doesn't exist in the source table. Negative caching is enabled by default, and can be disabled for individual tables in the client configuration. You can configure a TTL for negative cache results separately from other item cache entries. Setting negative\_ttl to zero disables negative caching. For more information, see [Configuring DynamoDB caching](ddb-caching-configuration.md).

## Limitations
<a name="ddb-caching-how-it-works.limitations"></a>
+ DynamoDB caching requires ElastiCache Serverless for Valkey version 9 or later.
+ DynamoDB caching is not supported on node-based ElastiCache clusters.
+ DynamoDB caching must be enabled during serverless cache creation. Enabling DynamoDB caching for an existing serverless cache is not supported.