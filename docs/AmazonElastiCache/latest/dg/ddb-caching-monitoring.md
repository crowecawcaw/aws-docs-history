

# Monitoring DynamoDB caching

In addition to the metrics supported by Amazon ElastiCache Serverless, Amazon DynamoDB caching emits additional metrics to enable monitoring and alarm creation for cache integration behavior. For information about accessing ElastiCache metrics through Amazon CloudWatch, see [Monitoring use with CloudWatch Metrics](CacheMetrics.md). For the list of metrics published for a serverless cache, see [ElastiCache Serverless](serverless-metrics-events-redis.md#serverless-metrics).

**Topics**
+ [DynamoDB caching cluster-level metrics](#ddb-caching-cluster-metrics)
+ [DynamoDB caching table-level metrics](#ddb-caching-table-metrics)
+ [Recommended alarms](#ddb-caching-recommended-alarms)
+ [Related DynamoDB metrics](#ddb-caching-related-ddb-metrics)

## DynamoDB caching cluster-level metrics
<a name="ddb-caching-cluster-metrics"></a>

Cluster-level metrics include the following dimension.


**Cluster-level metric dimensions**  

| Dimension | Valid values | Description | 
| --- | --- | --- | 
| `clusterId` | Cache identifier | Identifies the cache emitting the metric. | 

DynamoDB caching publishes the following cluster-level metrics.


**Cluster-level metrics**  

| Metric | Description | Unit | 
| --- | --- | --- | 
| `DynamoDBCachingRequestErrors` | Number of request errors returned. | Count | 
| `DynamoDBCachingBatchReadRequestLatency` | Average read latency for BatchGetItem and BatchWriteItem requests. | Microseconds | 
| `DynamoDBCachingTransactionReadRequestLatency` | Average read latency for TransactGetItems and TransactWriteItems requests. | Microseconds | 

## DynamoDB caching table-level metrics
<a name="ddb-caching-table-metrics"></a>

Table-level metrics include the following dimensions.


**Table-level metric dimensions**  

| Dimension | Valid values | Description | 
| --- | --- | --- | 
| `clusterId` | Cache identifier | Identifies the cache emitting the metric. | 
| `table` | DynamoDB table name | Identifies the DynamoDB table to which this metric applies. | 
| `operation` | GetItem, BatchGetItem, Query, Scan, PutItem, UpdateItem, DeleteItem, BatchWriteItem, TransactGetItems, TransactWriteItems | Identifies the DynamoDB operation to which this metric applies. | 

DynamoDB caching publishes the following table-specific metrics.


**Table-specific metrics**  

| Metric | Description | Unit | 
| --- | --- | --- | 
| `DynamoDBCachingHits` | Number of DynamoDB read requests served from cache. | Count | 
| `DynamoDBCachingMisses` | Number of DynamoDB read requests not found in the cache and served from DynamoDB. | Count | 
| `DynamoDBCachingHitRate` | The ratio of DynamoDB read requests served from the cache, from 0.0 to 1.0. | Count | 
| `DynamoDBCachingItemWrites` | Number of DynamoDB item write requests. | Count | 
| `DynamoDBCachingItemWriteFills` | Number of cached DynamoDB item entries with at least one projection populated by a write request. | Count | 
| `DynamoDBCachingItemWriteFilledProjections` | Number of cached DynamoDB projection entries populated for each item write. | Count | 
| `DynamoDBCachingItemWriteInvalidations` | Number of cached DynamoDB item entries with at least one projection invalidated by a write request. | Count | 
| `DynamoDBCachingNegativeHits` | Number of DynamoDB read requests that received a negative cache response. | Count | 
| `DynamoDBCachingReadRequestLatency` | The total time elapsed between the cache receiving a DynamoDB request and sending a response. | Microseconds | 

**Note**  
Metric counts are incremented once for each entry in batch (BatchGetItem, BatchWriteItem) and transaction (TransactGetItems, TransactWriteItems) operations. If a BatchGetItem request for 20 items is returned entirely from cached entries, the `DynamoDBCachingHits` metric is incremented 20 times.

## Recommended alarms
<a name="ddb-caching-recommended-alarms"></a>

We recommend that you create Amazon CloudWatch alarms on the following metrics.
+ `DynamoDBCachingHitRate` below your expected baseline might indicate TTLs that are too low or a change in workload.
+ `DynamoDBCachingRequestErrors` sustained above zero might indicate that the cache is failing to communicate with DynamoDB, for example because of missing IAM permissions or throttling.

## Related DynamoDB metrics
<a name="ddb-caching-related-ddb-metrics"></a>

Because DynamoDB caching reduces the request volume that reaches DynamoDB, we recommend that you also monitor the corresponding DynamoDB table-level metrics to confirm the expected change in your workload usage after you enable DynamoDB caching. These metrics include the following:
+ `ConsumedReadCapacityUnits`
+ `ThrottledRequests`
+ `SuccessfulRequestLatency`