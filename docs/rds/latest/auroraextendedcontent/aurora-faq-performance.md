# Performance

###### Topics

- [How does Amazon Aurora improve MySQL performance?](#aurora-faq-how-does-amazon-aurora-improve-mysql-performance "#aurora-faq-how-does-amazon-aurora-improve-mysql-performance")
- [How does Amazon Aurora improve PostgreSQL performance?](#aurora-faq-how-does-amazon-aurora-improve-postgresql-performance "#aurora-faq-how-does-amazon-aurora-improve-postgresql-performance")
- [How can I maximize throughput on Amazon Aurora MySQL?](#aurora-faq-how-can-i-maximize-throughput-on-amazon-aurora-mysql "#aurora-faq-how-can-i-maximize-throughput-on-amazon-aurora-mysql")
- [How can I maximize throughput on Amazon Aurora PostgreSQL?](#aurora-faq-how-can-i-maximize-throughput-on-amazon-aurora-postgresql "#aurora-faq-how-can-i-maximize-throughput-on-amazon-aurora-postgresql")
- [What is Amazon Aurora Parallel Query?](#aurora-faq-what-is-amazon-aurora-parallel-query "#aurora-faq-what-is-amazon-aurora-parallel-query")
- [What is optimized reads for Aurora PostgreSQL?](#aurora-faq-what-is-optimized-reads-for-aurora-postgresql "#aurora-faq-what-is-optimized-reads-for-aurora-postgresql")

## How does Amazon Aurora improve MySQL performance?

Amazon Aurora delivers up to 6x the throughput of stock MySQL by tightly integrating the database engine with an SSD-based virtualized storage layer purpose-built for database workloads. This reduces writes to the storage system, minimizes lock contention, and eliminates delays created by database process threads.

## How does Amazon Aurora improve PostgreSQL performance?

Amazon Aurora delivers up to 6x the throughput of stock PostgreSQL by tightly integrating the database engine with an SSD-based virtualized storage layer purpose-built for database workloads. Aurora decouples compute from storage, reducing writes to the storage system, minimizing lock contention, and eliminating delays created by database process threads.

## How can I maximize throughput on Amazon Aurora MySQL?

Aurora is fully compatible with MySQL, so existing applications and tools run without modification. The area where Aurora excels beyond stock MySQL is [highly concurrent workloads](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Managing.Performance.md"). To maximize throughput, design your applications to drive a large number of concurrent queries and transactions — Aurora's [storage architecture](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.md") is optimized to handle high parallelism with minimal lock contention.

## How can I maximize throughput on Amazon Aurora PostgreSQL?

Aurora is fully compatible with PostgreSQL, so existing applications and tools run without modification. Aurora delivers the highest performance gains over stock PostgreSQL under high concurrency. To maximize throughput, build your applications to drive a large number of concurrent queries and transactions. Aurora's [decoupled compute and storage architecture](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.md") reduces write amplification and I/O bottlenecks, enabling consistently higher throughput as connections scale.

## What is Amazon Aurora Parallel Query?

[Parallel Query](../../../AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-mysql-parallel-query.md") for Aurora MySQL pushes down and distributes the computational load of a single query across thousands of CPUs in Aurora's storage layer, speeding up analytical queries by up to two orders of magnitude. It can push down processing of more than 200 SQL functions, equijoins, and projections — no changes to query syntax are required, as the query optimizer automatically decides whether to use Parallel Query.

Parallel Query is ideal for operational analytics — when you need fast analytical queries on fresh data in large tables. It is not a data warehouse replacement; for exabyte-scale analytics, consider [Amazon Redshift](https://aws.amazon.com/pm/redshift/ "https://aws.amazon.com/pm/redshift/"). Parallel Query is compatible with Aurora serverless and Backtrack, runs on R\* instance family types, and is included at no additional charge beyond standard instance, I/O, and storage pricing.

## What is optimized reads for Aurora PostgreSQL?

Optimized reads for Aurora PostgreSQL delivers up to 8x improved query latency and up to 30% cost savings compared to instances without it. It is ideal for applications with large datasets that exceed the memory capacity of a database instance. Optimized Reads is available on Intel-based R6id and Graviton-based R6gd and R8gd instances (not available on Aurora serverless).

Optimized reads uses local NVMe-based SSD storage and includes two key features. Tiered caching automatically caches data evicted from the in-memory buffer cache onto local storage, speeding up subsequent accesses (available with Aurora I/O-Optimized). Temporary objects places temporary tables on local storage, improving performance of queries involving sorts, hash aggregations, and high-load joins. Approximately 90% of local storage is available for these features. If local storage fails, Aurora automatically performs a host replacement and triggers an in-region failover.

Can I use optimized reads for Aurora PostgreSQL with Aurora Standard and Aurora I/O-Optimized configurations?

Yes, Amazon Aurora optimized reads is available with both configurations. On both configurations, optimized reads-enabled instances automatically map temporary tables to the NVMe-based local storage to improve the performance of analytical queries and index rebuilds.

For I/O intensive workloads which are read heavy, optimized reads-enabled instances on Aurora PostgreSQL configured to use Aurora I/O-Optimized automatically cache data evicted from memory on NVMe-based local storage to deliver up to 8x improved query latency and up to 30% cost savings compared to instances without it, for applications with large datasets that exceed the memory capacity of a database instance.

How do I get started with optimized reads for Aurora PostgreSQL?

Customers can get started with Amazon Aurora Optimized Reads through the AWS Management Console, CLI, and SDK. Optimized reads is available on all R6id and R6gd instances by default. To use this capability, customers can simply modify their existing Aurora database clusters to include R6id and R6gd instances or create new database clusters using these instances. See the [Amazon Aurora optimized reads documentation](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.md") to get started.
