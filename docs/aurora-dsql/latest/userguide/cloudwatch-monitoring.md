# Monitoring Aurora DSQL with Amazon CloudWatch

Monitor Aurora DSQL using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. CloudWatch keeps these statistics for 15 months, helping you gain better perspective on your web application or service performance. Set alarms to watch for specific thresholds and send notifications or take actions when met. Review the following Usage and Observability metrics available for Aurora DSQL.

For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

## Observability and performance

This table outlines observability metrics for Aurora DSQL. It includes metrics for tracking
read-only and total transactions to provide overall workload characterization.
Actionable metrics like query timeouts and OCC conflict rate are included to help
identify performance issues and concurrency conflicts. Session-related metrics, both
active and total, offer insights into the current load on the system.

| CloudWatch Metric Name | Metric                   | Unit                  | Description                                                                                |
| ---------------------- | ------------------------ | --------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ReadOnlyTransactions   | Read-only transactions   | none                  | The number of read-only transactions                                                       |
| TotalTransactions      | Total transactions       | none                  | The total number of transactions executed on the system, including read-only transactions. |
| QueryTimeouts          | Query timeouts           | none                  | The number of queries which have timed out due to hitting the maximum transaction time     |
| OccConflicts           | OCC conflicts            | none                  | The number of transactions aborted due to key level OCC                                    |
| CommitLatency          | Commit Latency           | milliseconds          | Time spent by commit phase of query execution (P50)                                        |
| BytesWritten           | Bytes Written            | bytes                 | Bytes written to storage                                                                   |
| BytesRead              | Bytes Read               | bytes                 | Bytes read from storage                                                                    |
| ComputeTime            | QP compute time          | milliseconds          | QP wall clock time                                                                         |
| ClusterStorageSize     | Cluster Storage Size     | bytes                 | Cluster size                                                                               | ## Usage metrics Aurora DSQL measures all request-based activity, such as query processing, reads, and writes, using a single normalized billing unit called Distributed Processing Unit (DPU). |
| CloudWatch Metric Name | Metric                   | Dimension: ResourceId | Unit                                                                                       | Description                                                                                                                                                                                     |
| ---                    | ---                      | ---                   | ---                                                                                        | ---                                                                                                                                                                                             |
| WriteDPU               | Write Units              | <cluster-id>          | DPU                                                                                        | Approximates the write active-use component of your Aurora DSQL cluster DPU usage.                                                                                                              |
| MultiRegionWriteDPU    | Multi-Region Write Units | <cluster-id>          | DPU                                                                                        | Applicable for Multi-Region clusters: Approximates the multi-Region write active-use component of your Aurora DSQL cluster DPU usage.                                                           |
| ReadDPU                | Read Units               | <cluster-id>          | DPU                                                                                        | Approximates the read active-use component of your Aurora DSQL cluster DPU usage.                                                                                                               |
| ComputeDPU             | Compute Units            | <cluster-id>          | DPU                                                                                        | Approximates the compute active-use component of your Aurora DSQL cluster DPU usage.                                                                                                            |
| TotalDPU               | Total Units              | <cluster-id>          | DPU                                                                                        | Approximates the total active-use component of your Aurora DSQL cluster DPU usage.                                                                                                              |
