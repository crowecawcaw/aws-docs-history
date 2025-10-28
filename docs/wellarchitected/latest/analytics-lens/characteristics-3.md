# Characteristics

**Scalable throughput:** For real-time analytics, you should plan
a resilient stream storage infrastructure that can adapt to changes in the rate of data ﬂowing
through the stream. Scaling is typically performed by an administrative application that
monitors shard and partition data-handling metrics.

**Dynamic stream processor consumption and collaboration:**
Stream processors and consumers should automatically discover newly added Kinesis shards or Kafka
partitions, and distribute them equitably across all available resources to process
independently or collaboratively as a consumption group (Kinesis Application Name, Kafka Consumer
Group).

**Durable:** Real-time streaming systems should provide high
availability and data durability. For example, Amazon Kinesis Data Streams and Amazon Managed Streaming for Apache Kafka (Amazon MSK) replicate data
across Availability Zones providing the high durability that streaming applications need.

**Replay-ability:** Stream storage systems should provide the
ordering of records within shards and partitions, as well as the ability to independently read
or replay records in the same order to stream processors and consumers.

**Fault-tolerance, checkpoint, and replay:** Checkpointing refers
to recording the farthest point in the stream that data records have been consumed and
processed. If the consuming application crashes, it can resume reading the stream from that
point instead of having to start at the beginning.

**Loosely coupled integration:** A key benefit of streaming
applications is the construct of loose coupling. The value of loose coupling is the ability of
stream ingestion, stream producers, stream processors, and stream consumers to act and behave
independently of one another. Examples include the ability to scale consumers outside of the
producer configuration and adding additional stream processors and consumers to receive from
the same stream or topic as existing stream processors and consumers, but perform different
actions.

**Allow multiple processing applications in parallel:** The
ability for multiple applications to consume the same stream concurrently is an essential
characteristic of a stream processing system. For example, you might have one application that
updates a real-time dashboard and another that archives data to Amazon Redshift. You want both
applications to consume data from the same stream concurrently and independently.

**Messaging semantics:** In a distributed messaging system,
components might fail independently. Different messaging systems implement different semantic
guarantees between a producer and a consumer in the case of such a failure. The most common
message delivery guarantees implemented are:

- **At most once**: Messages that could not be delivered, or
  are lost, are never redelivered
- **At least once**: Message might be delivered more than once
  to the consumer
- **Exactly once**: Message is delivered exactly once
  Depending on your application needs, you can choose a message delivery system that
  supports one or more of these required semantics.

**Security:** Streaming ingest and processing systems must be
secure by default. You must grant access by using the principal of least privilege to the
streaming APIs and infrastructure, and encrypt data at rest and in transit. Both Kinesis Data
Streams and Amazon MSK can be configured to use IAM policies to grant least privilege access. For
stream storage in particular, allow encryption in transit for producers and consumers, and
encryption at rest.
