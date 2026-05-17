# Monitoring Aurora DSQL with Amazon CloudWatch

Monitor Aurora DSQL using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch keeps these statistics for 15 months, helping you gain better perspective on your web application or service performance. Set alarms to watch for specific thresholds and send notifications or take actions when met. Review the following Usage and Observability metrics available for Aurora DSQL.

For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

## Observability and performance

This table outlines observability metrics for Aurora DSQL. It includes metrics for tracking
read-only and total transactions to provide overall workload characterization.
Actionable metrics like query timeouts and OCC conflict rate are included to help
identify performance issues and concurrency conflicts. Session-related metrics, both
active and total, offer insights into the current load on the system.

| CloudWatch Metric Name | Metric                 | Unit         | Description                                                                                   |
| ---------------------- | ---------------------- | ------------ | --------------------------------------------------------------------------------------------- |
| ReadOnlyTransactions   | Read-only transactions | none         | The number of read-only transactions                                                          |
| TotalTransactions      | Total transactions     | none         | The total number of transactions executed on the system, including read-only<br>transactions. |
| QueryTimeouts          | Query timeouts         | none         | The number of queries which have timed out due to hitting the maximum<br>transaction time     |
| OccConflicts           | OCC conflicts          | none         | The number of transactions aborted due to key level OCC                                       |
| CommitLatency          | Commit Latency         | milliseconds | Time spent by commit phase of query execution (P50)                                           |
| BytesWritten           | Bytes Written          | bytes        | Bytes written to storage                                                                      |
| BytesRead              | Bytes Read             | bytes        | Bytes read from storage                                                                       |
| ComputeTime            | QP compute time        | milliseconds | QP wall clock time                                                                            |
| ClusterStorageSize     | Cluster Storage Size   | bytes        | Cluster size                                                                                  |

## Usage metrics

Aurora DSQL measures all request-based activity, such as query processing, reads, and writes, using a single normalized billing unit called Distributed Processing Unit (DPU).

| CloudWatch Metric Name | Metric                   | Dimension: ResourceId | Unit | Description                                                                                                                              |
| ---------------------- | ------------------------ | --------------------- | ---- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| WriteDPU               | Write Units              | <cluster-id>          | DPU  | Approximates the write active-use component of your Aurora DSQL cluster DPU<br>usage.                                                    |
| MultiRegionWriteDPU    | Multi-Region Write Units | <cluster-id>          | DPU  | Applicable for Multi-Region clusters: Approximates the multi-Region write<br>active-use component of your Aurora DSQL cluster DPU usage. |
| ReadDPU                | Read Units               | <cluster-id>          | DPU  | Approximates the read active-use component of your Aurora DSQL cluster DPU<br>usage.                                                     |
| ComputeDPU             | Compute Units            | <cluster-id>          | DPU  | Approximates the compute active-use component of your Aurora DSQL cluster DPU<br>usage.                                                  |
| TotalDPU               | Total Units              | <cluster-id>          | DPU  | Approximates the total active-use component of your Aurora DSQL cluster DPU<br>usage.                                                    |

## CDC stream metrics

Aurora DSQL publishes the following metrics for change data capture (CDC) streams. These
metrics use the `ClusterId` and `StreamId` dimensions, so you
can monitor each CDC stream independently. For more information about CDC streams, see
[Change data capture (CDC)
streams](cdc-streams.md "cdc-streams.md").

| CloudWatch Metric Name | Metric            | Unit         | Description                                                                                                                                                                                                                                                                                                           |
| ---------------------- | ----------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IsImpaired             | Is impaired       | none         | Indicates whether the stream is impaired. The value is `1`<br>when the stream is in the `IMPAIRED` state, and<br>`0` when the stream is healthy. Use this metric to create a<br>CloudWatch alarm that notifies you when a stream becomes impaired.                                                                    |
| PublishedBytes         | Published bytes   | bytes        | The total number of bytes that Aurora DSQL wrote to the target Kinesis data<br>stream.                                                                                                                                                                                                                                |
| PublishedRecords       | Published records | none         | The number of CDC records that Aurora DSQL wrote to the target Kinesis data<br>stream.                                                                                                                                                                                                                                |
| BehindSourceLag        | Behind source lag | milliseconds | The delay, in milliseconds, between when a transaction commits in Aurora DSQL and when<br>the CDC system processes the resulting record. A rising value indicates<br>that the CDC pipeline is falling behind the write workload. If lag<br>grows beyond the failure threshold, the stream transitions to<br>`FAILED`. |
| BytesStreamed          | Bytes streamed    | bytes        | The total bytes streamed through the CDC pipeline for billing<br>purposes. This metric reflects the data volume used to calculate<br>streaming charges.                                                                                                                                                               |
| StreamDPU              | Stream DPU        | DPU          | The Distributed Processing Units (DPU) consumed by the CDC stream.<br>This metric reflects the processing cost of streaming change<br>data.                                                                                                                                                                           |
