# Related services

[MemoryDB](../../../memorydb/latest/devguide/what-is-memorydb-for-redis.md "../../../memorydb/latest/devguide/what-is-memorydb-for-redis.md")

When deciding whether to use ElastiCache or MemoryDB consider the following comparisons:

- ElastiCache is a service that is commonly used to cache data from other databases and data stores using Valkey, Memcached, or Redis OSS. You should consider ElastiCache for caching workloads where you want to accelerate data access with your existing primary database or data store (microsecond read and write performance). You should also consider ElastiCache for use cases where you want to use Valkey or Redis OSS data structures and APIs to access data stored in a primary database or data store.
- ElastiCache can also help you save database costs by storing frequently accessed data in a cache. If your application has high read throughput requirements, you can achieve high scale, fast performance, and lowered data storage costs by using ElastiCache, instead of scaling your underlying database.
- MemoryDB is a durable, in-memory database for workloads that require an ultra-fast,
  primary database. It is compatible with Valkey and Redis OSS. You should consider using MemoryDB if your workload requires a durable database that provides ultra-fast performance
  (microsecond read and single-digit millisecond write latency). MemoryDB may also be a good fit for your use case if you want to build an application using Valkey or Redis OSS data structures and APIs with a primary, durable database. Finally, you should consider using MemoryDB to simplify your application architecture and lower costs by replacing usage of a database with a cache for durability and performance.
  [Amazon Relational Database Service](https://aws.amazon.com/rds/ "https://aws.amazon.com/rds/")

ElastiCache can help you save database costs by storing frequently accessed data in a cache. If your application has high read throughput requirements, you can achieve high scale, fast performance, and lowered data storage costs by using ElastiCache, instead of scaling your underlying database.

For further background information on the related Amazon Relational Database Service service, see [Amazon RDS](../../../rds.md "../../../rds.md")

ElastiCache can help you save database costs by storing frequently accessed data in a cache.
If your application has high read throughput requirements, you can achieve high scale, fast performance,
and lowered data storage costs by using ElastiCache, instead of scaling your underlying database.
