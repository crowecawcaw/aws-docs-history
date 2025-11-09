# Volume metrics

Your Amazon FSx for NetApp ONTAP file system can have one or more volumes that store your data. Each
of these volumes has a set of CloudWatch metrics, classified as either **Volume
metrics** or **Detailed volume metrics**.

- **Volume metrics** are per-volume performance and storage metrics that take
  two dimensions, `FileSystemId` and `VolumeId`.
  `FileSystemId` maps to the file system that the volume belongs to.
- **Detailed volume metrics** are per-storage-tier metrics that measure storage
  consumption per tier with the `StorageTier` dimension (with possible values
  of `SSD` and `StandardCapacityPool`) and per data type with the
  `DataType` dimension (with possible values of `User`,
  `Snapshot`, and `Other`). These metrics have the
  `FileSystemId`, `VolumeId`, `StorageTier`, and
  `DataType` dimensions.

###### Topics

- [Network I/O metrics](#fsxn-vol-network-IO-metrics "#fsxn-vol-network-IO-metrics")
- [Storage capacity metrics](#fsxn-vol-storage-volume-metrics "#fsxn-vol-storage-volume-metrics")
- [Detailed volume metrics](#detailed-vol-metrics "#detailed-vol-metrics")

## Network I/O metrics

All of these metrics take two dimensions, `FileSystemId` and `VolumeId`.

| Metric                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DataReadBytes`               | The number of bytes (network I/O) read from the volume by clients.<br>The `Sum` statistic is the total number of bytes associated with<br>read operations during the specified period. To calculate the average throughput<br>(bytes per second) for a period, divide the `Sum` statistic by the<br>number of seconds in the specified period.<br>Units: Bytes<br>Valid statistics: `Sum`                                                                                                                                                                                |
| `DataWriteBytes`              | The number of bytes (network I/O) written to the volume by clients.<br>The `Sum` statistic is the total number of bytes associated with<br>write operations during the specified period. To calculate the average<br>throughput (bytes per second) for a period, divide the `Sum`<br>statistic by the number of seconds in the specified period.<br>Units: Bytes<br>Valid statistics: `Sum`                                                                                                                                                                              |
| `DataReadOperations`          | The number of read operations (network I/O) on the volume by clients.<br>The `Sum` statistic is the total number of read operations during<br>the specified period. To calculate the average read operations per second for a<br>period, divide the `Sum` statistic by the number of seconds in the<br>specified period.<br>Units: Count<br>Valid statistics: `Sum`                                                                                                                                                                                                      |
| `DataWriteOperations`         | The number of write operations (network I/O) on the volume by<br>clients.<br>The `Sum` statistic is the total number of write operations<br>during the specified period. To calculate the average write operations per<br>second for a period, divide the `Sum` statistic by the number of<br>seconds in the specified period.<br>Units: Count<br>Valid statistics: `Sum`                                                                                                                                                                                                |
| `MetadataOperations`          | The number of I/O operations (network I/O) from metadata activities by<br>clients to the volume.<br>The `Sum` statistic is the total number of metadata operations<br>during the specified period. To calculate the average metadata operations per<br>second for a period, divide the `Sum` statistic by the number of<br>seconds in the specified period.<br>Units: Count<br>Valid statistics: `Sum`                                                                                                                                                                   |
| `DataReadOperationTime`       | The sum of total time spent within the volume for read operations (network<br>I/O) from clients accessing data in the volume.<br>The `Sum` statistic is the total number of seconds spent by read<br>operations during the specified period. To calculate the average read latency<br>for a period, divide the `Sum` statistic by the `Sum` of<br>the `DataReadOperations` metric over the same period.<br>Units: Seconds<br>Valid statistics: `Sum`                                                                                                                     |
| `DataWriteOperationTime`      | The sum of total time spent within the volume for fulfilling write<br>operations (network I/O) from clients accessing data in the volume.<br>The `Sum` statistic is the total number of seconds spent by write<br>operations during the specified period. To calculate the average write latency<br>for a period, divide the `Sum` statistic by the `Sum` of<br>the `DataWriteOperations` metric over the same period.<br>Units: Seconds<br>Valid statistics: `Sum`                                                                                                      |
| `MetadataOperationTime`       | The sum of total time spent within the volume for fulfilling metadata<br>operations (network I/O) from clients that are accessing data in the<br>volume.<br>The `Sum` statistic is the total number of seconds spent by read<br>operations during the specified period. To calculate the average latency for a<br>period, divide the `Sum` statistic by the `Sum` of the<br>`MetadataOperations` over the same period.<br>Units: Seconds<br>Valid statistics: `Sum`                                                                                                      |
| `CapacityPoolReadBytes`       | The number of bytes read (network I/O) from the volume's capacity pool<br>tier.<br>To ensure data integrity, ONTAP performs a read operation on the capacity pool<br>immediately after performing a write operation.<br>The `Sum` statistic is the total number of bytes read from<br>the<br>volume's capacity pool tier over a specified period. To calculate capacity pool bytes per second,<br>divide the `Sum` statistic by the seconds in a specified period. Units:<br>BytesValid statistics: `Sum`                                                                |
| `CapacityPoolReadOperations`  | The number of read operations (network I/O) from the volume's capacity pool<br>tier. This translates to a capacity pool read request.<br>To ensure data integrity, ONTAP performs a read operation on the capacity pool<br>immediately after performing a write operation.<br>The `Sum` statistic is the total number of read operations from<br>the volume's capacity pool tier over a specified period. To calculate capacity pool<br>requests per second, divide the `Sum` statistic by the seconds in a specified period.<br>Units: Count<br>Valid statistics: `Sum` |
| `CapacityPoolWriteBytes`      | The number of bytes written (network I/O) to the volume's capacity pool<br>tier.<br>To ensure data integrity, ONTAP performs a read operation on the capacity pool<br>immediately after performing a write operation.<br>The `Sum` statistic is the total number of bytes written<br>to the volume's capacity pool tier over a specified period. To calculate capacity pool bytes per second,<br>divide the `Sum` statistic by the seconds in a specified period.<br>Units: Bytes<br>Valid statistics: `Sum`                                                             |
| `CapacityPoolWriteOperations` | The number of write operations (network I/O) to the volume from the capacity<br>pool tier. This translates to a write request.<br>To ensure data integrity, ONTAP performs a read operation on the capacity pool<br>immediately after performing a write operation.<br>The `Sum` statistic is the total number of write operations to<br>the volume's capacity pool tier over a specified period. To calculate capacity pool requests per second,<br>divide the `Sum` statistic by the seconds in a specified period.<br>Units: Count<br>Valid statistics: `Sum`         |

## Storage capacity metrics

All of these metrics take two dimensions, `FileSystemId` and `VolumeId`.

| Metric                       | Description                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `StorageCapacity`            | The size of the volume in bytes.<br>Units: Bytes<br>Valid statistics: `Maximum`                              |
| `StorageUsed`                | The used logical storage capacity of the volume.<br>Units: Bytes<br>Valid statistics: `Average`              |
| `StorageCapacityUtilization` | The storage capacity utilization of the volume.<br>Units: Percent<br>Valid statistics: `Average`             |
| `FilesUsed`                  | The used files (number of files or inodes) on the volume.<br>Units: Count<br>Valid statistics: `Average`     |
| `FilesCapacity`              | The total number of inodes that can be created on the volume.<br>Units: Count<br>Valid statistics: `Maximum` |

## Detailed volume metrics

Detailed volume metrics take more dimensions than volume metrics, enabling more
granular measurements of your data. All detailed volume metrics have the dimensions
`FileSystemId`, `VolumeId`, `StorageTier`, and
`DataType`.

- The `StorageTier` dimension indicates the storage tier that the metric measures,
  with possible values of `All`, `SSD`, and
  `StandardCapacityPool`.
- The `DataType` dimension indicates the type of data that the metric measures, with
  possible values of `All`, `User`, `Snapshot`, and
  `Other`.

The following table defines what the `StorageUsed` metric measures for the listed dimensions.

| Metric                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `StorageUsed`                | The amount of logical space used, in bytes.<br>This metric measures different types of space consumption<br>depending on the dimensions used with this metric.<br>When setting `StorageTier` to `SSD` or `StandardCapacityPool`,<br>and setting `DataType` to `All`, this metric measures the<br>logical space usage for this volume for your SSD and capacity pool tiers, respectively.<br>When setting the `DataType` dimension to `User`, `Snapshot`, or `Other`, and<br>setting `StorageTier` to `All`, this metric measures the logical space usage for each respective type of data.<br>The `Snapshot` data consumption includes the snapshot reserve, which is 5% of the volume's size by default.<br>Units: Bytes<br>Valid statistics: `Average`, `Minimum`, and<br>`Maximum` |
| `StorageCapacityUtilization` | The percentage of the volume's used physical disk space.<br>Units: Percent<br>Valid statistics: `Maximum`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
