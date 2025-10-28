# CloudWatch metrics for Amazon EFS

Amazon EFS metrics use the `EFS` namespace. The
`AWS/EFS` namespace includes the following metrics. All metrics
except for `TimeSinceLastSync` are for a single dimension,
`FileSystemId`. A file system's ID can be found in the Amazon EFS console, and
it takes the form of `fs-abcdef0123456789a`.

**`TimeSinceLastSync`**

Shows the amount of time that has passed since the last successful sync to the
destination file system in a replication configuration. Any changes to data on the
source file system that occurred before the `TimeSinceLastSync` value have
been successfully replicated. Any changes on the source that occurred after
`TimeSinceLastSync` might not be fully replicated.

This metric uses two dimensions:

- `FileSystemId` dimension – ID of the source file system in the
  replication configuration.
- `DestinationFileSystemId` dimension – ID of the destination file
  system in the replication configuration.

Units: Seconds

Valid statistics: `Minimum`, `Maximum`,
`Average`

**`PercentIOLimit`**

Shows how close a file system is to reaching the I/O limit of the General Purpose
performance mode.

Units: Percent

Valid statistics: `Minimum`, `Maximum`,
`Average`

**`BurstCreditBalance`**

The number of burst credits that a file system has. Burst credits allow a file
system to burst to throughput levels above a file system’s baseline level for periods
of time.

The `Minimum` statistic is the smallest burst credit balance for any
minute during the period. The `Maximum` statistic is the largest burst
credit balance for any minute during the period. The `Average` statistic
is the average burst credit balance during the period.

Units: Bytes

Valid statistics: `Minimum`, `Maximum`,
`Average`

**`PermittedThroughput`**

The maximum amount of throughput that a file system can drive.

- For file systems using Elastic throughput, this value reflects
  the maximum write throughput of the file system.
- For file systems using Provisioned throughput, if the amount of
  data stored in the EFS Standard storage class allows your
  file system to drive a higher throughput than you provisioned, this metric
  reflects the higher throughput instead of the provisioned amount.
- For file systems in Bursting throughput, this value is a
  function of the file system size and `BurstCreditBalance`.

The `Minimum` statistic is the smallest throughput permitted for any
minute during the period. The `Maximum` statistic is the highest
throughput permitted for any minute during the period. The `Average`
statistic is the average throughput permitted during the period.

###### Note

Read operations are metered at one-third the rate of other operations.

Units: Bytes per second

Valid statistics: `Minimum`, `Maximum`,
`Average`

**`MeteredIOBytes`**

The number of metered bytes for each file system operation, including data read,
data write, and metadata operations, with read operations discounted according to the
throughput limit.

You can create a [CloudWatch metric
math expression](monitoring-metric-math.md#metric-math-throughput-utilization "monitoring-metric-math.md#metric-math-throughput-utilization") that compares `MeteredIOBytes` to
`PermittedThroughput`. If these values are equal, then you are consuming
the entire amount of throughput allocated to your file system. In this situation, you
might consider changing the file system's throughput mode to get higher
throughput.

The `Sum` statistic is the total number of metered bytes associated with all
file system operations. The `Minimum` statistic is the size of the
smallest operation during the period. The `Maximum` statistic is the size
of the largest operation during the period. The `Average` statistic is
the average size of an operation during the period. The `SampleCount`
statistic provides a count of all operations.

Units:

- Bytes for `Minimum`, `Maximum`, `Average`,
  and `Sum` statistics.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**TotalIOBytes**
The actual number of bytes for each file system operation processed by Amazon EFS,
without any read discounts. This number may differ from the actual amount requested by
your applications because it includes minimums. This number may also be higher than
the numbers shown in `PermittedThroughput`.

Data operations are metered at 32 KiB and other operations are metered at 4 KiB.
After the minimum, all operations are metered per KiB.

The `Sum` statistic is the total number of bytes associated with all
file system operations. The `Minimum` statistic is the size of the smallest
operation during the period. The `Maximum` statistic is the size of the
largest operation during the period. The `Average` statistic is the average
size of an operation during the period. The `SampleCount` statistic
provides a count of all operations.

###### Note

To calculate the average operations per second for a period, divide the
`SampleCount` statistic by the number of seconds in the period. To
calculate the average throughput (bytes per second) for a period, divide the
`Sum` statistic by the number of seconds in the period.

Units:

- Bytes for `Minimum`, `Maximum`, `Average`,
  and `Sum` statistics.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**`DataReadIOBytes`**

The actual number of bytes for each file system read operation.

The `Sum` statistic is the total number of bytes associated with read
operations. The `Minimum` statistic is the size of the smallest read
operation during the period. The `Maximum` statistic is the size of the
largest read operation during the period. The `Average` statistic is the
average size of read operations during the period. The `SampleCount`
statistic provides a count of read operations.

Units:

- Bytes for `Minimum`, `Maximum`, `Average`,
  and `Sum`.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**`DataWriteIOBytes`**

The actual number of bytes for each file system write operation.

The `Sum` statistic is the total number of bytes associated with
write operations. The `Minimum` statistic is the size of the smallest
write operation during the period. The `Maximum` statistic is the size of
the largest write operation during the period. The `Average` statistic is
the average size of write operations during the period. The `SampleCount`
statistic provides a count of write operations.

Units:

- Bytes are the units for the `Minimum`, `Maximum`,
  `Average`, and `Sum` statistics.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**`MetadataIOBytes`**

The actual number of bytes for each metadata operation.

The `Sum` statistic is the total number of bytes associated with
metadata operations. The `Minimum` statistic is the size of the smallest
metadata operation during the period. The `Maximum` statistic is the size
of the largest metadata operation during the period. The `Average`
statistic is the size of the average metadata operation during the period. The
`SampleCount` statistic provides a count of metadata operations.

Units:

- Bytes are the units for the `Minimum`, `Maximum`,
  `Average`, and `Sum` statistics.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**`MetadataReadIOBytes`**

The actual number of bytes for each metadata read operation.

The `Sum` statistic is the total number of bytes associated with
metadata read operations. The `Minimum` statistic is the size of the
smallest metadata read operation during the period. The `Maximum` statistic
is the size of the largest metadata read operation during the period. The
`Average` statistic is the average size of metadata read operations
during the period. The `SampleCount` statistic provides a count of metadata
read operations.

Units:

- Bytes are the units for the `Minimum`, `Maximum`,
  `Average`, and `Sum` statistics.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**`MetadataWriteIOBytes`**

The actual number of bytes for each metadata write operation.

The `Sum` statistic is the total number of bytes associated with
metadata write operations. The `Minimum` statistic is the size of the
smallest metadata write operation during the period. The `Maximum`
statistic is the size of the largest metadata write operation during the period. The
`Average` statistic is the average size of metadata write operations
during the period. The `SampleCount` statistic provides a count of
metadata write operations.

Units:

- Bytes are the units for the `Minimum`, `Maximum`,
  `Average`, and `Sum` statistics.
- Count for `SampleCount`.

Valid statistics: `Minimum`, `Maximum`,
`Average`, `Sum`, `SampleCount`

**`ClientConnections`**

The number of client connections to a file system. When using a standard client,
there is one connection per mounted Amazon EC2 instance.

###### Note

To calculate the average `ClientConnections` for periods greater
than one minute, divide the `Sum` statistic by the number of minutes in
the period.

Units: Count of client connections

Valid statistics: `Sum`

**`StorageBytes`**

The size of the file system in bytes, including the amount of data stored in the
EFS storage classes. This metric is emitted to CloudWatch every 15 minutes.

The `StorageBytes` metric has the following dimensions:

- `Total` is the metered size (in bytes) of data stored in the file
  system, in all storage classes. For EFS Infrequent Access (IA) and
  EFS Archive storage classes, files smaller than 128KiB are rounded to
  128KiB.
- `Standard` is the metered size (in bytes) of data
  stored in the EFS Standard storage class.
- `IA` is the actual size (in bytes) of data stored in
  the EFS Infrequent Access storage class.
- `IASizeOverhead` is the difference (in bytes) between the
  actual size of data in the EFS Infrequent Access storage class (indicated in the
  `IA` dimension) and the metered size of the storage
  class, after rounding small files to 128KiB.
- `Archive` is the actual size (in bytes) of data
  stored in the EFS Archive storage class.
- `ArchiveSizeOverhead` is the difference (in bytes) between the
  actual size of data in the EFS Archive storage class (indicated in the
  `Archive` dimension) and the metered size of the
  storage class, after rounding small files to 128KiB.

Units: Bytes

Valid statistics: `Minimum`, `Maximum`,
`Average`

###### Note

`StorageBytes` is displayed on the Amazon EFS console **File system
metrics** page using base 1024 units (kibibytes, mebibytes, gibibytes,
and tebibytes).
