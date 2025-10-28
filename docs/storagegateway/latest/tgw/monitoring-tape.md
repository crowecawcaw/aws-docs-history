# Understanding virtual tape metrics

You can find information following about the Storage Gateway metrics that cover virtual
tapes. Each tape has a set of metrics associated with it.

Some tape-specific metrics might have the same name as certain gateway-specific
metrics. These metrics represent the same kinds of measurements but are scoped to a tape
instead of a gateway. Before starting work, specify whether you want to work with a
gateway metric or a tape metric. When working with tape metrics, specify the tape ID for
the tape that you want to view metrics for. For more information, see [Using Amazon CloudWatch
Metrics](UsingCloudWatchConsole-vtl-common.md "UsingCloudWatchConsole-vtl-common.md").

###### Note

Some metrics return data points only when new data has been generated during the
most recent monitoring period.

The following table describes the Storage Gateway metrics that you can use to get
information about your tapes.

| Metric               | Description                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CachePercentDirty`  | The tape's contribution to the overall percentage of the gateway's cache that isn't persisted to AWS. The sample is taken at the end of the reporting period. Use the `CachePercentDirty` metric of the gateway to view the overall percentage of the gateway's cache that isn't persisted to AWS. For more information, see [Understanding gateway metrics](MonitoringGateways-common.md "MonitoringGateways-common.md"). Units: Percent |
| `CloudTraffic`       | The amount of bytes uploaded and downloaded from the cloud to the tape. Units: bytes                                                                                                                                                                                                                                                                                                                                                      |
| `IoWaitPercent`      | The percentage of allocated IoWait units that are currently used by the tape. Units: Percent                                                                                                                                                                                                                                                                                                                                              |
| `HealthNotification` | The number of health notifications sent by the tape. Units: count                                                                                                                                                                                                                                                                                                                                                                         |
| `MemUsedBytes`       | The percentage of allocated memory that is currently used by the tape. Units: Bytes                                                                                                                                                                                                                                                                                                                                                       |
| `MemTotalBytes`      | The percentage of total memory that is currently used by the tape. Units: Bytes                                                                                                                                                                                                                                                                                                                                                           |
| `ReadBytes`          | The total number of bytes read from your on-premises applications in the reporting period for a file share. Use this metric with the `Sum` statistic to measure throughput and with the `Samples` statistic to measure IOPS. Units: Bytes                                                                                                                                                                                                 |
| `UserCpuPercent`     | The percentage of allocated CPU compute units for the user that are currently used by the tape. Units: Percent                                                                                                                                                                                                                                                                                                                            |
| `WriteBytes`         | The total number of bytes written to your on-premises applications in the reporting period. Use this metric with the `Sum` statistic to measure throughput and with the `Samples` statistic to measure IOPS. Units: Bytes                                                                                                                                                                                                                 |
