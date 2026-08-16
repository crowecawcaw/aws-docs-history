# Neptune CloudWatch Metrics

###### Note

Amazon Neptune sends metrics to CloudWatch only when they have a non-zero value.

For all Neptune metrics, the aggregation granularity is 5 minutes.

###### Topics

- [Neptune CloudWatch metrics](#cw-metrics-available "#cw-metrics-available")
- [CloudWatch Metrics That Are Now Deprecated in Neptune](#cw-metrics-deprecated "#cw-metrics-deprecated")

## Neptune CloudWatch metrics

The following table lists the CloudWatch metrics that Neptune supports.

###### Note

All cumulative metrics are reset to zero whenever the server restarts,
whether for maintenance, a reboot, or recovering from a crash.

Neptune CloudWatch metrics| Metric | Description | Time Interval | Instance Statistic |
| --- | --- | --- | --- |
| `BackupRetentionPeriodStorageUsed` | The total amount of backup storage, in bytes, used to support<br>from the Neptune DB cluster's backup retention window. Included in the<br>total reported by the `TotalBackupStorageBilled` metric. | | |
| `BufferCacheHitRatio` | The percentage of requests that are served by the buffer cache.<br>This metric can be useful in diagnosing query latency, because cache<br>misses induce significant latency. If the cache hit ratio is below<br>99.9, consider upgrading the instance type to cache more data in memory. | 1 minute | average |
| `ClusterReplicaLag` | For a read replica, the amount of lag when replicating updates<br>from the primary instance, in milliseconds. | 1 minute | average |
| `ClusterReplicaLagMaximum` | The maximum amount of lag between the primary instance and each<br>Neptune DB instance in the DB cluster, in milliseconds. | 1 minute | max/min |
| `ClusterReplicaLagMinimum` | The minimum amount of lag between the primary instance and each<br>Neptune DB instance in the DB cluster, in milliseconds. | 1 minute | max/min |
| `CPUCreditBalance` | The number of CPU credits that an instance has accumulated, reported at 5-minute intervals.<br>You can use this metric to determine how long a DB instance can burst beyond its baseline performance level<br>at a given rate. | 5 min | average |
| `CPUCreditUsage` | The number of CPU credits consumed during the specified period, reported at 5-minute intervals.<br>This metric measures the amount of time during which physical CPUs have been used for processing instructions<br>by virtual CPUs allocated to the DB instance. | 5 min | average |
| `CPUSurplusCreditBalance` | The number of surplus credits that have been spent by an unlimited instance when its<br>`CPUCreditBalance` value is zero. The `CPUSurplusCreditBalance` value is paid<br>down by earned CPU credits. If the number of surplus credits exceeds the maximum number of credits that<br>the instance can earn in a 24-hour period, the spent surplus credits above the maximum incur an additional<br>charge. CPU credit metrics are available at a 5-minute frequency only. | 5 min | average |
| `CPUSurplusCreditsCharged` | The number of spent surplus credits that are not paid down by earned CPU credits, and incur an<br>additional charge. | 5 min | average |
| `CPUUtilization` | The percentage of CPU utilization. | 1 minute | average/P99 |
| `EngineUptime` | The amount of time that the instance has been running, in seconds. | 1 min | average |
| `FreeableMemory` | The amount of available random access memory, in bytes. | 1 min | average |
| `GlobalDbDataTransferBytes` | The number of bytes of redo log data transferred from the<br>primary AWS Region to a secondary AWS Region in a Neptune global<br>database. | 1 min | average |
| `GlobalDbReplicatedWriteIO` | The number of write I/O operations replicated from the primary<br>AWS Region in the global database to the cluster volume in a<br>secondary AWS Region.<br>The billing calculations for each DB cluster in a Neptune global database<br>use the `VolumeWriteIOPS` metric to account for writes performed<br>within that cluster. For the primary DB cluster, the billing calculations use<br>`GlobalDbReplicatedWriteIO` to account for the cross-region<br>replication to secondary DB clusters. | 5 min | sum |
| `GlobalDbProgressLag` | The number of milliseconds that a secondary cluster is behind<br>the primary cluster for both user transactions and system transactions. | 1 min | average |
| `GremlinClientErrorsPerSec` | Number of client-side errors per second in Gremlin traversals. | 1 min | average |
| `GremlinServerErrorsPerSec` | Number of server-side errors per second in Gremlin traversals. | 1 min | average |
| `GremlinRequestsPerSec` | Number of requests per second to the Gremlin engine. | 1 min | average |
| `GremlinWebSocketOpenConnections` | The number of open WebSocket connections to Neptune. | 1 min | sum |
| `LoaderClientErrorsPerSec` | Number of client-side errors per second from loader requests. | 1 min | average |
| `LoaderRequestsPerSec` | Number of loader requests per second. | 1 min | average |
| `LoaderServerErrorsPerSec` | Number of loader server-side errors per second. | 1 min | average |
| `MainRequestQueuePendingRequests` | The number of requests waiting in the input queue pending execution. Neptune starts<br>throttling requests when they exceed the maximum queue capacity. | 1 min | sum |
| `NCUUtilization` | Only applicable to a [Neptune Serverless](neptune-serverless.md "neptune-serverless.md")<br>DB instance or DB cluster. At an instance level, reports a percentage calculated<br>as the number of Neptune capacity units (NCUs) currently being used by the<br>instance in question, divided by the maximum NCU capacity setting for the cluster.<br>An NCU, or Neptune capacity unit, consists of 2 GiB (gibibyte) of memory (RAM),<br>along with associated virtual processor capacity (vCPU) and networking.<br>At a cluster level, `NCUUtilization` reports the percentage<br>of maximum capacity being used by the cluster as a whole. | | |
| `NetworkReceiveThroughput` | The amount of incoming network throughput received from clients<br>by each instance in the Neptune DB cluster, in bytes per second. This<br>throughput does *_not_<br>• include network traffic<br>between instances in the DB cluster and the cluster volume. | 1 min | average |
| `NetworkThroughput` | The amount of network throughput both received from and<br>transmitted to clients by each instance in the Neptune DB cluster,<br>in bytes per second. This throughput does **not**<br>include network traffic between instances in the DB cluster and the<br>cluster volume. | 1 min | average |
| `NetworkTransmitThroughput` | The amount of outgoing network throughput transmitted to<br>clients by each instance in the Neptune DB cluster, in bytes per<br>second. This throughput does **not**<br>include network traffic between instances in the DB cluster and the<br>cluster volume. | 1 min | average |
| `NumIndexDeletesPerSec` | Number of deletes from individual indexes. Deletes from each index are counted individually.<br>This includes the deletes that may get rolled back if a query encounters an error. | 1 min | average |
| `NumIndexInsertsPerSec` | Number of inserts to individual indexes. Inserts to each index are counted separately. This includes<br>the inserts that may get rolled back if a query encounters an error. | 1 min | average |
| `NumIndexReadsPerSec` | Number of statements scanned from any index. Any access pattern starts with a search on an index<br>and reads of all matching statements. An increase in this metric can cause an increase in query<br>latencies or CPU utilization. | 1 min | average |
| `NumQueuedRequestsPerSec` | The number of requests queued per second. | | |
| `NumResultCacheHit` | Number of Gremlin result cache hits. | 1 min | sum |
| `NumResultCacheMiss` | Number of Gremlin result cache misses. | 1 min | sum |
| `NumTxCommitted` | The number of transactions successfully committed per second. | 1 min | sum |
| `NumTxOpened` | The number of transactions opened on the server per second. | 1 min | sum |
| `NumTxRolledBack` | For write queries, the number of transactions per second rolled back<br>on the server because of errors. For read-only queries, this metric is equal to<br>the number of completed read-only transactions per second. | 1 min | sum |
| `NumUndoPagesPurged` | This metric indicates the number of batches purged. This metric is indicator of progress in<br>purging. The value is `0` for reader instances, and the metric only applies to<br>the writer instance. | 1 min | sum |
| `OpenCypherRequestsPerSec` | Number of requests per second (both HTTPS and Bolt) to the openCypher engine. | 1 min | average |
| `OpenCypherBoltOpenConnections` | The number of open Bolt connections to Neptune. | 1 min | sum |
| `ResultCacheSizeInBytes` | Total estimated size (in bytes) of all cached items in the Gremlin result cache. | 1 min | sum |
| `ResultCacheItemCount` | Number of items in the Gremlin result cache. | 1 min | sum |
| `ResultCacheOldestItemTimestamp` | The timestamp of the oldest item cached in the Gremlin result cache. | 1 min | sum |
| `ResultCacheNewestItemTimestamp` | The timestamp of the newest item cached in the Gremlin result cache. | | |
| `ServerlessDatabaseCapacity` | As an instance-level metric, `ServerlessDatabaseCapacity`<br>reports the current instance capacity of a given [Neptune<br>serverless](neptune-serverless.md "neptune-serverless.md") instance, in NCUs. An NCU, or Neptune capacity unit,<br>consists of 2 GiB (gibibyte) of memory (RAM), along with associated virtual<br>processor capacity (vCPU) and networking.<br>At a cluster-level, `ServerlessDatabaseCapacity`<br>reports the average of all the `ServerlessDatabaseCapacity` values<br>of the DB instances in the cluster. | | |
| `SnapshotStorageUsed` | The total amount of backup storage consumed by all snapshots<br>for a Neptune DB cluster outside its backup retention window, in bytes.<br>Included in the total reported by the `TotalBackupStorageBilled` metric. | 1 min | sum |
| `SparqlClientErrorsPerSec` | The number of client-side errors per second in SPARQL queries. | 1 min | average |
| `SparqlRequestsPerSec` | The number of requests per second to the SPARQL engine. | 1 min | average |
| `SparqlServerErrorsPerSec` | The number of SPARQL server errors per second. | 1 min | average |
| `StatsNumStatementsScanned` | The total number of statements scanned for [DFE statistics](neptune-dfe-statistics.md "neptune-dfe-statistics.md") since the server started.<br>Every time statistics computation is triggered, this number increases, but<br>when no computation is happening, it remains static. As a result, if you graph it<br>over time, you can tell when computation happened and when it didn't:<br>Graph of StatsNumStatementsScanned values over time<br>By looking at the slope of the graph in periods where the metric is increasing,<br>you can also tell how quickly the computation was going.<br>If there is no such metric, it means that the statistics feature is disabled<br>on your DB cluster, or that the engine version you're running doesn't have the<br>statistics feature. If the metric value is zero, it means that no statistics<br>computation has occurred. | 1 min | sum |
| `StorageNetworkReceiveThroughput` | The amount of network throughput received from the storage subsystem by each instance in<br>the Neptune DB cluster. | 1 min | average |
| `StorageNetworkThroughput` | The amount of network throughput received from and sent to the storage subsystem by each instance<br>in the Neptune DB cluster. | 1 min | average |
| `StorageNetworkTransmitThroughput` | The amount of network throughput sent to the storage subsystem by each instance in the Neptune<br>DB cluster. | 1 min | average |
| `SwapUsage` | The amount of swap space used. | 1 min | sum |
| `TempStorageIOPS` | The number of IOPS for both read and writes on local storage attached to the Neptune DB instance. This<br>metric represents a count and is measured once per second. | | |
| `TempStorageThroughput` | The amount of data transferred to and from local storage associated with the Neptune DB instance. This metric<br>represents bytes and is measured once per second. | | |
| `TotalBackupStorageBilled` | The total amount of backup storage for which you are billed for a<br>given Neptune DB cluster, in bytes. Includes the backup storage measured by<br>the `BackupRetentionPeriodStorageUsed` and `SnapshotStorageUsed`<br>metrics. | 1 day | sum |
| `TotalRequestsPerSec` | The total number of requests per second to the server from all sources. | 1 min | average |
| `TotalClientErrorsPerSec` | The total number per second of requests that errored out because of client-side issues. | 1 min | average |
| `TotalServerErrorsPerSec` | The total number per second of requests that errored out on the server because of internal<br>failures. | 1 min | average |
| `UndoLogListSize` | The count of undo logs in the undo log list.<br>Undo logs contain records of committed transactions that expire when<br>all active transactions are more recent than the commit time. The expired<br>records are periodically purged. Records for delete operations can take<br>longer to purge than records for other types of transaction.<br>Purging is done exclusively by the DB cluster's writer instance, so the<br>rate of purging is dependent on the writer instance type. If the<br>`UndoLogListSize` is high and growing in your DB cluster,<br>upgrade the writer instance to increase the purge rate.<br>Also, if you are upgrading to engine version `1.2.0.0` or<br>higher from a version earlier than `1.2.0.0`, first make sure<br>that the `UndoLogListSize` value is under a certain threshold.<br>Otherwise, the patch will roll back and fail. The thresholds are based on<br>instance type: the default limit is 40k for 4xlarge or larger instances, and<br>10k for instances smaller than 4xlarge. If you attempt to upgrade a cluster<br>with the `UndoLogListSize` metric above the limit, the patch process<br>will roll back, the upgrade will be canceled, and an event with the reason will<br>be visible on the cluster event page. These limits can change for operational<br>reasons without prior warning. Because engine versions `1.2.0.0` and<br>higher use a different format for undo logs, the upgrade can only begin after<br>your previous undo logs have been fully purged below the applicable threshold.<br>See [Upgrading to 1.2.0.0 or above](engine-updates-1200-changes.md "engine-updates-1200-changes.md") for more information. | 1 min | sum |
| `VolumeBytesLeftTotal` | The remaining available space for the cluster volume, in bytes.<br>As the cluster volume grows, this value decreases. If it reaches zero,<br>the cluster reports an out-of-space error.<br>If you want to detect whether your Neptune DB cluster is approaching<br>it's size limit, this value is simpler and more reliable<br>to monitor than `VolumeBytesUsed`. `VolumeBytesLeftTotal`<br>takes into account storage used for internal housekeeping and other allocations<br>that don't affect your storage billing.<br>This metric is reported only by the writer instance. To avoid disruption during<br>failovers, use the cluster-level dimension (`DBClusterIdentifier`). | 1 min | average |
| `VolumeBytesUsed` | The total amount of storage allocated to your Neptune DB cluster, in bytes.<br>This is the amount of storage for which you are billed. It is the maximum amount of<br>storage allocated to your DB cluster at any point in its existence, not the amount<br>you are currently using (see [Neptune storage billing](storage.md#storage-billing "storage.md#storage-billing")). | 5 min | sum |
| `VolumeReadIOPs` | The total number of billed read I/O operations from a cluster volume, reported a 5-minute intervals.<br>Billed read operations are calculated at the cluster volume level, aggregated from all instances in the<br>Neptune DB cluster, and then reported at 5-minute intervals. | 5 min | sum |
| `VolumeWriteIOPs` | The total number of write disk I/O operations to the cluster volume, reported at 5-minute intervals. | 5 min | sum |

## CloudWatch Metrics That Are Now Deprecated in Neptune

Use of these Neptune metrics has now been deprecated. They are still supported, but
may be eliminated in the future as new and better metrics become available.

| Metric                                 | Description                                                                                                                                  |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `GremlinHttp1xx`                       | Number of HTTP 1xx responses for the Gremlin endpoint per second.<br>We recommend that you use the new `Http1xx`<br>combined metric instead. |
| `GremlinHttp2xx`                       | Number of HTTP 2xx responses for the Gremlin endpoint per second.                                                                            |
| `GremlinHttp4xx`                       | Number of HTTP 4xx errors for the Gremlin endpoint per second.<br>We recommend that you use the new `Http4xx`<br>combined metric instead.    |
| `GremlinHttp5xx`                       | Number of HTTP 5xx errors for the Gremlin endpoint per second.<br>We recommend that you use the new `Http5xx`<br>combined metric instead.    |
| `GremlinErrors`                        | Number of errors in Gremlin traversals.                                                                                                      |
| `GremlinRequests`                      | Number of requests to Gremlin engine.                                                                                                        |
| `GremlinWebSocketSuccess`              | Number of successful WebSocket connections to the Gremlin endpoint<br>per second.                                                            |
| `GremlinWebSocketClientErrors`         | Number of WebSocket client errors on the Gremlin endpoint per<br>second.                                                                     |
| `GremlinWebSocketServerErrors`         | Number of WebSocket server errors on the Gremlin endpoint per<br>second.                                                                     |
| `GremlinWebSocketAvailableConnections` | Number of potential WebSocket connections currently available.                                                                               |
| `Http100`                              | Number of HTTP 100 responses for the endpoint per second.<br>We recommend that you use the new `Http1xx` combined metric<br>instead.         |
| `Http101`                              | Number of HTTP 101 responses for the endpoint per second.<br>We recommend that you use the new `Http1xx` combined metric<br>instead.         |
| `Http1xx`                              | Number of HTTP 1xx responses for the endpoint per second.                                                                                    |
| `Http200`                              | Number of HTTP 200 responses for the endpoint per second.                                                                                    |
| `Http2xx`                              | Number of HTTP 2xx responses for the endpoint per second.                                                                                    |
| `Http400`                              | Number of HTTP 400 errors for the endpoint per second.<br>We recommend that you use the new `Http4xx` combined metric<br>instead.            |
| `Http403`                              | Number of HTTP 403 errors for the endpoint per second.<br>We recommend that you use the new `Http4xx` combined metric<br>instead.            |
| `Http405`                              | Number of HTTP 405 errors for the endpoint per second.<br>We recommend that you use the new `Http4xx` combined metric<br>instead.            |
| `Http413`                              | Number of HTTP 413 errors for the endpoint per second.<br>We recommend that you use the new `Http4xx` combined metric<br>instead.            |
| `Http429`                              | Number of HTTP 429 errors for the endpoint per second.<br>We recommend that you use the new `Http4xx` combined metric<br>instead.            |
| `Http4xx`                              | Number of HTTP 4xx errors for the endpoint per second.                                                                                       |
| `Http500`                              | Number of HTTP 500 errors for the endpoint per second.<br>We recommend that you use the new `Http5xx` combined metric<br>instead.            |
| `Http501`                              | Number of HTTP 501 errors for the endpoint per second.<br>We recommend that you use the new `Http5xx` combined metric<br>instead.            |
| `Http5xx`                              | Number of HTTP 5xx errors for the endpoint per second.                                                                                       |
| `LoaderErrors`                         | Number of errors from Loader requests.                                                                                                       |
| `LoaderRequests`                       | Number of Loader Requests.                                                                                                                   |
| `SparqlHttp1xx`                        | Number of HTTP 1xx responses for the SPARQL endpoint per second.<br>We recommend that you use the new `Http1xx` combined metric<br>instead.  |
| `SparqlHttp2xx`                        | Number of HTTP 2xx responses for the SPARQL endpoint per second.                                                                             |
| `SparqlHttp4xx`                        | Number of HTTP 4xx errors for the SPARQL endpoint per second.<br>We recommend that you use the new `Http4xx` combined metric<br>instead.     |
| `SparqlHttp5xx`                        | Number of HTTP 5xx errors for the SPARQL endpoint per second.<br>We recommend that you use the new `Http5xx` combined metric<br>instead.     |
| `SparqlErrors`                         | Number of errors in the SPARQL queries.                                                                                                      |
| `SparqlRequests`                       | Number of requests to the SPARQL engine.                                                                                                     |
| `StatusErrors`                         | Number of errors from the status endpoint.                                                                                                   |
| `StatusRequests`                       | Number of requests to the status endpoint.                                                                                                   |
