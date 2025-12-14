# Amazon FSx for OpenZFS metrics and dimensions

Amazon FSx publishes the metrics described in the following tables in the
`AWS/FSx` namespace in Amazon CloudWatch for all FSx for OpenZFS file systems:

###### Topics

- [FSx for OpenZFS network I/O metrics](#fsx-networkio-metrics "#fsx-networkio-metrics")
- [FSx for OpenZFS file server metrics](#fsx-file-server-metrics "#fsx-file-server-metrics")
- [FSx for OpenZFS disk metrics](#fsx-diskio-metrics "#fsx-diskio-metrics")
- [FSx for OpenZFS storage capacity metrics](#fsx-storage-capacity-metrics "#fsx-storage-capacity-metrics")
- [FSx for OpenZFS dimensions](#fsx-dimensions "#fsx-dimensions")

## FSx for OpenZFS network I/O metrics

The `AWS/FSx` namespace includes the following network I/O metrics.

| Metric                | Description                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `DataReadBytes`       | The number of bytes for read operations for clients that access the file<br>system.<br>Unit: Bytes<br>Valid statistic: `Sum`      |
| `DataWriteBytes`      | The number of bytes for write operations for clients that access the file<br>system.<br>Unit: Bytes<br>Valid statistic: `Sum`     |
| `DataReadOperations`  | The number of read operations for clients that access the file<br>system.<br>Unit: Count<br>Valid statistic: `Sum`                |
| `DataWriteOperations` | The number of write operations for clients that access the file<br>system.<br>Unit: Count<br>Valid statistic: `Sum`               |
| `ClientConnections`   | The number of active connections between clients and the file server.<br>Unit: Count<br>Valid statistics: `Average`, `Maximum`    |
| `MetadataOperations`  | The number of metadata operations for clients that access the file<br>system.<br>Unit: Count<br>Valid statistic: `Sum`            |
| `NfsBadCalls`         | The number of calls rejected by the NFS server remote procedure call<br>(RPC) mechanism.<br>Unit: Count<br>Valid statistic: `Sum` |

## FSx for OpenZFS file server metrics

The `AWS/FSx` namespace includes the following file server metrics.

| Metric                                | Description                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `NetworkThroughputUtilization`        | The network throughput for clients that access the file system, as a percentage of the<br>provisioned limit. For Multi-AZ file systems, this metric includes replication<br>traffic. Note that this metric reflects the direction<br>• i.e. inbound or outbound<br>• that has the higher traffic flow.<br>Unit: Percent<br>Valid statistics: `Average`, `Maximum` |
| `CPUUtilization`                      | The percentage utilization of your file server’s CPU resources.<br>Unit: Percent<br>Valid statistics: `Average`, `Maximum`                                                                                                                                                                                                                                        |
| `FileServerDiskThroughputUtilization` | The disk throughput between your file server and its storage volumes.<br>Listed<br>as a percentage of the provisioned limit, which is determined by throughput<br>capacity.<br>Unit: Percent<br>Valid statistics: `Average`, `Maximum`                                                                                                                            |
| `FileServerDiskThroughputBalance`     | The percentage of available burst credits for disk throughput between your file server and its storage volumes.<br>Unit: Percent<br>Valid statistics: `Average`, `Minimum`                                                                                                                                                                                        |
| `FileServerDiskIopsUtilization`       | The disk IOPS between your file server and storage volumes, as a percentage of the<br>provisioned<br>limit, which is determined by throughput capacity.<br>Unit: Percent<br>Valid statistics: `Average`, `Maximum`                                                                                                                                                |
| `FileServerDiskIopsBalance`           | The percentage of available burst credits for disk IOPS between your file server and its storage volumes.<br>Unit: Percent<br>Valid statistics: `Average`, `Minimum`                                                                                                                                                                                              |
| `MemoryUtilization`                   | The percentage of your file server’s memory resources that are utilized.<br>Unit: Percent<br>Valid statistics: `Average`, `Maximum`                                                                                                                                                                                                                               |
| `FileServerCacheHitRatio`             | The percentage of cache hits. For Single-AZ 2 (non-HA and HA) file systems, this metric reports the cache hit ratio for both the in-memory (ARC) and NVMe (L2ARC) caches.<br>For Single-AZ 1 (non-HA and HA) file systems, this metric reports only the cache hit ratio for the ARC cache.<br>Unit: Percent<br>Valid statistics: `Average`, `Minimum`             |

## FSx for OpenZFS disk metrics

The `AWS/FSx` namespace includes the following disk metrics.

| Metric                  | Description                                                                                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DiskReadBytes`         | The number of bytes for read operations that access storage volumes.<br>Unit: Bytes<br>Valid statistic: `Sum`                                                                                                           |
| `DiskWriteBytes`        | The number of bytes for write operations that access storage volumes.<br>Unit: Bytes<br>Valid statistic: `Sum`                                                                                                          |
| `DiskReadOperations`    | The number of read operations for the file server that accesses storage<br>volumes.<br>Unit: Count<br>Valid statistic: `Sum`                                                                                            |
| `DiskWriteOperations`   | The number of write operations for the file server that accesses storage<br>volumes.<br>Unit: Count<br>Valid statistic: `Sum`                                                                                           |
| `DiskThroughputBalance` | The percentage of available burst credits for disk throughput for the storage volumes.<br>Unit: Percent<br>Valid statistics: `Average`, `Minimum`                                                                       |
| `DiskIopsUtilization`   | The disk IOPS between your ﬁle server and storage volumes, as a percentage of the provisioned<br>IOPS limit that has been determined by the storage volumes.<br>Unit: Percent<br>Valid statistics: `Average`, `Maximum` |

## FSx for OpenZFS storage capacity metrics

The `AWS/FSx` namespace includes the following storage capacity
metrics.

| Metric                | Description                                                                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `StorageCapacity`     | The total storage capacity, equal to the sum of used and available storage<br>capacity.<br>Unit: Bytes<br>Valid statistics: `Average`, `Minimum` |
| `UsedStorageCapacity` | The amount of storage that's used.<br>Unit: Bytes<br>Valid statistics: `Average`, `Minimum`                                                      |
| `CompressionRatio`    | The ratio of compressed storage usage to uncompressed storage usage.<br>Valid statistics: `Average`, `Minimum`                                   |

## FSx for OpenZFS dimensions

FSx for OpenZFS provides additional dimensions to further refine the metrics listed in
the previous table. FSx for OpenZFS metrics use the `FSx` namespace and provide
metrics at the file system or volume granularity by using the `FileSystemId` or
`VolumeId`.

| Dimension      | Description                                                                                                                                                                                                                                                                                                                                             |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FileSystemId` | This dimension filters the metrics that you request to an individual file system.                                                                                                                                                                                                                                                                       |
| `VolumeId`     | This dimension filters the metrics that you request to an individual volume within a file<br>system. This dimension must be used in combination with<br>`FileSystemId`.                                                                                                                                                                                 |
| `CacheType`    | This dimension filters the metrics that you request by the type of cache used, either ARC for in-memory caching or L2ARC for SSD and NVMe caching.<br>This dimension must be used in combination with `FileSystemId`.                                                                                                                                   |
| `DataType`     | This dimension filters the metrics that you requested to a specific type of stored data. Metrics with `DataType` set to `Snapshot`<br>report information about the snapshots within the volume. Metrics without a `DataType` dimension report aggregated information from the volume, which includes any child volumes and snapshots within the volume. |

FSx for OpenZFS metrics use the `FSx` namespace and provide metrics for the
dimensions that are listed in the table above.
