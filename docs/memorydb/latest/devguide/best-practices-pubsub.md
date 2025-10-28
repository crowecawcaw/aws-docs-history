# Best practices: Pub/Sub and Enhanced I/O Multiplexing

When using Valkey or Redis OSS version 7 or later, we recommend using [sharded Pub/Sub](https://valkey.io/topics/pubsub/ "https://valkey.io/topics/pubsub/").
You also improve throughput and latency using [enhanced I/O multiplexing](https://aws.amazon.com/memorydb/features/#Ultra-fast_performance "https://aws.amazon.com/memorydb/features/#Ultra-fast_performance"), which is automatically available when using Valkey or Redis OSS version 7 or later and requires no client changes. It is ideal for pub/sub workloads, which often are throughput-bound with multiple client connections.
