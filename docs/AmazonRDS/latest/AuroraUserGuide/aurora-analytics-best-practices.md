

# Best practices
<a name="aurora-analytics-best-practices"></a>

Performance of queries against your Iceberg and Parquet data depends on choosing an instance class that provides enough memory and CPU for your workload, balancing memory against concurrency, and laying out your data for efficient scanning. The following practices cover instance selection, memory configuration, data layout, concurrency, and operations.

**Topics**
+ [Choosing the right DB instance class](aurora-analytics-instance-class.md)
+ [Using a dedicated reader instance for analytics](aurora-analytics-dedicated-reader.md)
+ [Tuning query\_mem for your workload](aurora-analytics-tuning-query-mem.md)
+ [Concurrency sizing](aurora-analytics-concurrency-sizing.md)
+ [Optimizing data layout in Amazon S3](aurora-analytics-data-layout.md)
+ [IAM and networking recommendations](aurora-analytics-iam-networking.md)
+ [Operational best practices](aurora-analytics-operational.md)