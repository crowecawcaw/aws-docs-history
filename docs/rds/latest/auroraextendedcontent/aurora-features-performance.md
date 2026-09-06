

# Performance
<a name="aurora-features-performance"></a>

**Topics**
+ [Up to 6x the throughput of PostgreSQL and MySQL](#aurora-features-throughput)
+ [Optimized reads](#aurora-features-optimized-reads)
+ [Diagnose and resolve performance bottlenecks](#aurora-features-diagnose-performance)

## Up to 6x the throughput of PostgreSQL and MySQL
<a name="aurora-features-throughput"></a>

Testing on standard benchmarks such as SysBench has shown an increase in throughput of up to 6x over stock PostgreSQL and stock MySQL on similar hardware. Aurora uses a variety of software and hardware techniques to ensure the database engine is able to fully use available compute, memory, and networking. I/O operations use distributed systems techniques, such as quorums, to improve performance consistency.

## Optimized reads
<a name="aurora-features-optimized-reads"></a>

[Optimized reads](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.optimized.reads.html) for Aurora PostgreSQL delivers up to 30% cost savings compared to instances without it. It is ideal for applications with large datasets that exceed the memory capacity of a database instance.

Optimized reads instances use local NVMe-based SSD block-level storage, available on Graviton-based R6gd and R8gd and Intel-based R6id instances. Performance enhancements include tiered caching and temporary objects to enable you to make the most of your database instances. With up to 8x improved query latency, you can effectively run read-heavy, I/O-intensive workloads such as operational dashboards, anomaly detection, and vector search.

When you use optimized reads instances with pgvector, it increases queries per second for vector search by up to 9x.

## Diagnose and resolve performance bottlenecks
<a name="aurora-features-diagnose-performance"></a>

[Amazon DevOps Guru for RDS](https://aws.amazon.com/devops-guru/features/devops-guru-for-rds/) uses ML-powered insights to help easily detect and diagnose performance-related database issues and resolve them in minutes rather than days. You can use it to automatically identify the root cause of performance issues and get intelligent recommendations to help address the issue, without needing help from database experts.

To get started, enable [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html) in the [Amazon RDS Management Console](https://console.aws.amazon.com/rds/home), and then enable [DevOps Guru for RDS](https://console.aws.amazon.com/codeguru/devops-guru) for your Aurora resources or your entire account.