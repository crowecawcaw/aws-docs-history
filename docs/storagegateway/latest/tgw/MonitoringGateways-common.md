# Understanding gateway metrics

For the discussion in this topic, we define _gateway_ metrics as
metrics that are scoped to the gateway—that is, they measure something about the
gateway. Because a gateway contains one or more volumes, a gateway-specific metric is
representative of all volumes on the gateway. For example, the
`CloudBytesUploaded` metric is the total number of bytes that the gateway
sent to the cloud during the reporting period. This metric includes the activity of all
the volumes on the gateway.

When working with gateway metric data, you specify the unique identification of the
gateway that you are interested in viewing metrics for. To do this, you specify both the
`GatewayId` and the `GatewayName`
values. When you want to work with metric for a gateway, you specify the gateway
_dimension_ in the metrics namespace, which distinguishes a
gateway-specific metric from a volume-specific metric. For more information, see [Using Amazon CloudWatch
Metrics](UsingCloudWatchConsole-vtl-common.md "UsingCloudWatchConsole-vtl-common.md").

###### Note

Some metrics return data points only when new data has been generated during the
most recent monitoring period.

| Metric                      | Description                                                                                                                                                                                                                                                                                                     |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AvailabilityNotifications` | Number of availability-related health notifications generated<br>by the gateway.<br>Use this metric with the `Sum` statistic to observe<br>whether the gateway is experiencing any availability-related events.<br>For details about the events, check your configured CloudWatch log<br>group.<br>Unit: Number |
| `CacheHitPercent`           | Percent of application reads served from the cache. The sample is<br>taken at the end of the reporting period.<br>Unit: Percent                                                                                                                                                                                 |
| `CachePercentDirty`         | The overall percentage of the gateway cache that has not been<br>persisted to AWS. The sample is taken at the end of the reporting<br>period.<br>Use this metric with the `Sum` statistic.<br>Ideally, this metric should remain low.<br>Unit: Percent                                                          |
| `CacheUsed`                 | The total number of bytes being used in the gateway's cache<br>storage. The sample is taken at the end of the reporting<br>period.<br>Unit: Bytes                                                                                                                                                               |
| `IoWaitPercent`             | Percent of time that the gateway is waiting on a response from the<br>local disk.<br>Unit: Percent                                                                                                                                                                                                              |
| `MemTotalBytes`             | Amount of RAM provisioned to the gateway VM, in bytes.<br>Unit: Bytes                                                                                                                                                                                                                                           |
| `MemUsedBytes`              | Amount of RAM currently in use by the gateway VM, in bytes.<br>Unit: Bytes                                                                                                                                                                                                                                      |
| `QueuedWrites`              | Normally, this value represents the number of locally-stored bytes<br>waiting to be written to AWS, but it also reflects the<br>synchronization process that occurs between local data and cloud<br>data during "bootstrapping", which occurs each time a gateway<br>restarts.<br>Unit: Bytes                   |
| `TotalCacheSize`            | The total size of the cache in bytes. The sample is taken at the<br>end of the reporting period.<br>Unit: Bytes                                                                                                                                                                                                 |
| `UploadBufferPercentUsed`   | Percent use of the gateway's upload buffer. The sample is<br>taken at the end of the reporting period.<br>Unit: Percent                                                                                                                                                                                         |
| `UploadBufferUsed`          | The total number of bytes being used in the gateway's upload<br>buffer. The sample is taken at the end of the reporting<br>period.<br>Unit: Bytes                                                                                                                                                               |
| `UserCpuPercent`            | Percent of CPU time spent on gateway processing, averaged across<br>all cores.<br>Unit: Percent                                                                                                                                                                                                                 |

## Dimensions for Storage Gateway

metrics

The CloudWatch namespace for the Storage Gateway service is
`AWS/StorageGateway`. Data is available automatically in 5-minute periods
at no charge.

| Dimension                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GatewayId`, `GatewayName` | These dimensions filter the data that you request to<br>gateway-specific metrics. You can identify a gateway to work by<br>the value for `GatewayId` or<br>`GatewayName`. If the name of your gateway was<br>different for the time range that you are interested in viewing<br>metrics, use the `GatewayId`.<br>Throughput and latency data of a gateway is based on all the<br>volumes for the gateway. For information about working with<br>gateway metrics, see [Measuring Performance Between Your Gateway and<br>AWS](../vgw/monitoring-volume-gateway.md#PerfGatewayAWS-common "../vgw/monitoring-volume-gateway.md#PerfGatewayAWS-common"). |
