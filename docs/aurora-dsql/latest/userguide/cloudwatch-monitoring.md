

# Monitoring Aurora DSQL with Amazon CloudWatch
<a name="cloudwatch-monitoring"></a>

Monitor Aurora DSQL using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch keeps these statistics for 15 months, helping you gain better perspective on your web application or service performance. Set alarms to watch for specific thresholds and send notifications or take actions when met. Review the following Usage and Observability metrics available for Aurora DSQL.

For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). 

## Observability and performance
<a name="observability-performance"></a>

This table outlines observability metrics for Aurora DSQL. It includes metrics for tracking read-only and total transactions to provide overall workload characterization. Actionable metrics like query timeouts and OCC conflict rate are included to help identify performance issues and concurrency conflicts. Session-related metrics, both active and total, offer insights into the current load on the system.


| CloudWatch Metric Name | Metric | Unit | Description | 
| --- |--- |--- |--- |
| ReadOnlyTransactions | Read-only transactions | none | The number of read-only transactions | 
| TotalTransactions | Total transactions | none | The total number of transactions executed on the system, including read-only transactions. | 
| QueryTimeouts | Query timeouts | none | The number of queries which have timed out due to hitting the maximum transaction time | 
| OccConflicts | OCC conflicts | none | The number of transactions aborted due to key level OCC | 
| CommitLatency | Commit Latency | milliseconds | Time spent by commit phase of query execution (P50) | 
| BytesWritten | Bytes Written | bytes | Bytes written to storage | 
| BytesRead | Bytes Read | bytes | Bytes read from storage | 
| ComputeTime | QP compute time | milliseconds | QP wall clock time | 
| ClusterStorageSize | Cluster Storage Size | bytes | Cluster size | 

Aurora DSQL also publishes the following metrics under the AWS/Usage namespace. Use these metrics to monitor connection attempts and active connection count for your clusters.


| CloudWatch Metric Name | Type | Resource | ResourceId | Service | Unit | Description | 
| --- |--- |--- |--- |--- |--- |--- |
| ResourceCount | Resource | ClusterConnectionCount | cluster/<cluster-id> | AuroraDSQL | Count | The number of active connections for a cluster. | 
| CallCount | API | DbConnectAdmin or DbConnect | cluster/<cluster-id> | AuroraDSQL | Count | The number of API calls for database connection operations (DbConnectAdmin or DbConnect). | 

## Usage metrics
<a name="usage-metrics"></a>

 Aurora DSQL measures all request-based activity, such as query processing, reads, and writes, using a single normalized billing unit called Distributed Processing Unit (DPU). 


| CloudWatch Metric Name | Metric | Dimension: ResourceId | Unit | Description | 
| --- |--- |--- |--- |--- |
| WriteDPU | Write Units | <cluster-id> | DPU | Approximates the write active-use component of your Aurora DSQL cluster DPU usage. | 
| MultiRegionWriteDPU | Multi-Region Write Units | <cluster-id> | DPU | Applicable for Multi-Region clusters: Approximates the multi-Region write active-use component of your Aurora DSQL cluster DPU usage. | 
| ReadDPU | Read Units | <cluster-id> | DPU | Approximates the read active-use component of your Aurora DSQL cluster DPU usage. | 
| ComputeDPU | Compute Units | <cluster-id> | DPU | Approximates the compute active-use component of your Aurora DSQL cluster DPU usage. | 
| TotalDPU | Total Units | <cluster-id> | DPU | Approximates the total active-use component of your Aurora DSQL cluster DPU usage. | 

## CDC stream metrics
<a name="cdc-stream-metrics"></a>

Aurora DSQL publishes the following metrics for change data capture (CDC) streams. These metrics use the `ClusterId` and `StreamId` dimensions, so you can monitor each CDC stream independently. For more information about CDC streams, see [Change data capture (CDC) streams](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html).


| CloudWatch Metric Name | Metric | Unit | Description | 
| --- |--- |--- |--- |
| IsImpaired | Is impaired | none | Indicates whether the stream is impaired. The value is 1 when the stream is in the IMPAIRED state, and 0 when the stream is healthy. Use this metric to create a CloudWatch alarm that notifies you when a stream becomes impaired. | 
| PublishedBytes | Published bytes | bytes | The total number of bytes that Aurora DSQL wrote to the target Kinesis data stream. | 
| PublishedRecords | Published records | none | The number of CDC records that Aurora DSQL wrote to the target Kinesis data stream. | 
| BehindSourceLag | Behind source lag | milliseconds | The delay, in milliseconds, between when a transaction commits in Aurora DSQL and when the CDC system processes the resulting record. A rising value indicates that the CDC pipeline is falling behind the write workload. If lag grows beyond the failure threshold, the stream transitions to FAILED. | 
| BytesStreamed | Bytes streamed | bytes | The total bytes streamed through the CDC pipeline for billing purposes. This metric reflects the data volume used to calculate streaming charges. | 
| StreamDPU | Stream DPU | DPU | The Distributed Processing Units (DPU) consumed by the CDC stream. This metric reflects the processing cost of streaming change data. | 