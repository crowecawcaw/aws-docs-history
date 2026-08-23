# Streaming execution models

AWS Glue Streaming provides two execution models for processing streaming data.
Choose the model that best fits your latency requirements and workload characteristics.

## Micro-batch mode (default)

Micro-batch mode is the default execution model for all AWS Glue streaming jobs.
This mode uses `forEachBatch` or `Trigger.ProcessingTime`
to poll the source at configured intervals.

During each interval, AWS Glue performs the following steps:

1. Plan the execution DAG.
2. Launch tasks.
3. Read accumulated data from the source.
4. Process the data.
5. Commit the results.
6. Terminate tasks and repeat.

Minimum latency in micro-batch mode is typically 1–2 seconds due to per-batch
scheduling overhead. This mode supports all sources (Kafka, Kinesis), all languages
(Python, Scala), stateful and stateless operations, and auto-scaling.

Micro-batch mode is best for most streaming workloads where second-level latency
is acceptable.

## Real-time mode (AWS Glue 6.0+)

Real-time mode is a new execution model for Spark Structured Streaming available starting
in AWS Glue 6.0 that reduces end-to-end latency to sub-second. Real-time mode can also
help achieve millisecond-level latencies for eligible workloads. Tasks run continuously,
processing records as they arrive rather than waiting for data to accumulate. Real-time
mode applies only to Spark Structured Streaming and does not apply to legacy Spark
Streaming (DStreams).

Real-time mode requires explicit opt-in through the
`--enable-real-time-mode` job argument. This mode does not use
`forEachBatch`. Instead, you use `writeStream` with
`Trigger.RealTime` directly.

Real-time mode has the following requirements and limitations:

- Source: Kafka only
- Operations: Stateless only
- Languages: Scala only
- Auto-scaling: Not supported. Do not enable auto-scaling for real-time mode jobs. Use a fixed worker count.

Real-time mode is best for low-latency stateless transformations, such as
Kafka-to-Kafka pipelines, where sub-second latency is required.

For full details on enabling and using real-time mode, see
[Enabling real-time mode for streaming jobs](streaming-chapter.md#glue-streaming-real-time-mode "streaming-chapter.md#glue-streaming-real-time-mode").

## Comparison of execution models

The following table compares the two execution models.

Execution model comparison| Feature | Micro-batch mode | Real-time mode |
| --- | --- | --- |
| Latency | Seconds to minutes | Sub-second |
| Sources | Kafka, Kinesis | Kafka only |
| Languages | Python, Scala | Scala only |
| Operations | Stateful and stateless | Stateless only |
| Output modes | Append, Update, Complete | Update only |
| Auto-scaling | Yes | No |
| Trigger | Trigger.ProcessingTime / forEachBatch | Trigger.RealTime |
| AWS Glue version | All versions | 6.0+ |
