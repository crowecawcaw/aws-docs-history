

# DynamoDB caching

DynamoDB caching is a feature of Amazon ElastiCache Serverless for Valkey that provides write-through caching for Amazon DynamoDB table data. DynamoDB caching delivers sub-millisecond read latencies for cached data and can help reduce the impact of DynamoDB throttling because of high read activity on a subset of items (hot keys). DynamoDB caching can also reduce read costs for frequently read DynamoDB data while requiring minimal application changes.

DynamoDB caching provides in-memory caching for DynamoDB items and query results without requiring custom management code. Your applications continue to use DynamoDB APIs through the AWS SDK, while the ElastiCache integration client you configure at application startup automatically routes cacheable requests to a serverless Valkey cache. DynamoDB caching provides write-through caching, where writes to DynamoDB tables configured for caching are automatically updated in cached data after they are applied to DynamoDB. Reads to cached tables are served from the cache when available and read from DynamoDB when needed. DynamoDB caching is serverless, and scales automatically with your workload with no infrastructure to manage.

**Topics**
+ [How DynamoDB caching works](ddb-caching-how-it-works.md)
+ [Getting started with DynamoDB caching](ddb-caching-getting-started.md)
+ [Security in DynamoDB caching](ddb-caching-security.md)
+ [Configuring DynamoDB caching](ddb-caching-configuration.md)
+ [Monitoring DynamoDB caching](ddb-caching-monitoring.md)
+ [Billing for DynamoDB caching](ddb-caching-billing.md)