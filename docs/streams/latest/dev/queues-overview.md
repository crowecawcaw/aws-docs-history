

# Consume records with a queue

A queue delivers records from an On-demand stream to a *queue consumer*, the application that consumes the stream through the queue. A *consumer instance* is one running instance of that application. Queue consumer instances do not lease shards. Each instance receives the next visible record, so you can add instances to process more records in parallel. A queue delivers each record at least once, and does not necessarily deliver records in the order that producers wrote them to the stream.

The records a queue delivers stay in the stream. Each queue keeps its own delivery state for those records, separate from every other queue on the same stream. Adding a queue therefore does not change anything for your producers or your stream consumers: they keep writing and reading as before, and a queue consumer and a stream consumer can process the same records independently.

## When to use a queue
<a name="queues-overview-when-to-use"></a>

Because a queue tracks the delivery state of each record independently and hands each consumer instance the next visible record, it fits work in which each record can be processed on its own, without reference to other records, which this guide calls [Stateless processing](key-concepts.md#stateless-processing-concept). Examples include microservice integration, order processing, and per-record inference.

For work in which processing one record depends on the records before it, which this guide calls [Stateful processing](key-concepts.md#stateful-processing-concept), read the stream directly, because reading records in order within a shard is what lets a stream consumer keep an accurate state. Examples include live analytics, personalization, and anomaly and pattern detection. For more information, see [Read data from Kinesis data streams](building-consumers.md).

## No coordination to run
<a name="queues-overview-no-coordination"></a>

A queue consumer does not need to coordinate work across its instances. It does not need an Amazon DynamoDB table, shard leases, or the Kinesis Client Library. Each consumer instance receives the next visible record and acknowledges it when processing is complete. For more information about Kinesis Client Library, which a stream consumer uses to coordinate shard assignments, see [Use Kinesis Client Library](kcl.md).

## Streams and registered consumers
<a name="queues-overview-streams-and-consumers"></a>

A queue delivers records from exactly one stream. A queue counts as one registered consumer on its stream, and it shares the stream's registered consumer limit with enhanced fan-out consumers: 20 registered consumers on On-demand Standard and 50 on On-demand Advantage. For more information about enhanced fan-out consumers, see [Develop enhanced fan-out consumers with dedicated throughput](enhanced-consumers.md). For queue quotas and limits, see [Quotas and limits for queues](queues-quotas.md).

For the terms used to describe queues, see [Amazon Kinesis Data Streams terminology and concepts](key-concepts.md).