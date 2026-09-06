

# Durability in ElastiCache
<a name="durability"></a>

Amazon ElastiCache for Valkey now supports durability. This capability enables you to use ElastiCache for both caching and data store workloads with microsecond read latency. Durability provides data protection through a Multi-AZ transactional log, enabling fast recovery and restart during failures. ElastiCache offers two durability options: synchronous writes designed for zero data loss at single-digit millisecond write latency, and asynchronous writes for microsecond write latency. Durability is currently supported with node-based ElastiCache.

When configuring an ElastiCache cluster, you can choose between two durability options. With synchronous writes, data is persisted across at least two Availability Zones (AZs) in a Multi-AZ transactional log before responding to the client. While this provides data durability during failures, it increases write latency from microseconds to single-digit milliseconds. With asynchronous writes, data is persisted in a Multi-AZ transactional log after responding to the client, maintaining ElastiCache's microsecond write latency with the risk of losing up to 10 seconds of uncommitted data during a failure. Both options maintain microsecond read latencies. With asynchronous writes, if the primary node cannot persist changes to the Multi-AZ transactional log for more than 10 seconds, it will reject incoming write commands until the ability to persist writes is restored. If your application cannot tolerate any data loss, we recommend synchronous writes. Otherwise, we recommend asynchronous writes. The durability options give you flexibility to balance between write performance and data durability based on your specific workload requirements.

**Topics**
+ [Durability options](Durability.Options.md)
+ [Configuring durability](Durability.Configuring.md)
+ [Consistency](Durability.Consistency.md)
+ [Failure scenarios](Durability.FailureScenarios.md)
+ [Limitations](Durability.Limitations.md)
+ [Monitoring](Durability.Monitoring.md)
+ [Getting started with durability](Durability.GettingStarted.md)