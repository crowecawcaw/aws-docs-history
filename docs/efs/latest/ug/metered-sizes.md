# How Amazon EFS reports file system and object

sizes

The following sections describe how Amazon EFS reports file system sizes, sizes of objects
within a file system, and file system throughput.

## Metering EFS file system

objects

Objects that you can view in an EFS file system include regular files,
directories, symbolic links, and special files (FIFOs and sockets). Each of these objects is
metered for 2 kibibytes (KiB) of metadata (for its inode) and one or more increments of 4
KiB of data. The following list explains the metered data size for different types of file
system objects:

- Regular files – The metered data size of a
  regular file is the logical size of the file rounded to the next 4-KiB increment, except
  that it might be less for sparse files.

A _sparse file_ is a file to which data is not
written to all positions of the file before its logical size is reached. For a sparse
file, in some cases the actual storage used is less than the logical size rounded to the
next 4-KiB increment. In these cases, Amazon EFS reports actual storage used as the metered
data size.

- Directories – The metered data size of a
  directory is the actual storage used for the directory entries and the data structure
  that holds them, rounded to the next 4-KiB increment. The metered data size doesn't
  include the actual storage used by the file data.
- Symbolic links and special files – The metered
  data size for these objects is always 4 KiB.

When Amazon EFS reports the space used for an object, through the NFSv4.1
`space_used` attribute, it includes the object's current metered data size but
not its metadata size. You can use two utilities for measuring the disk usage of a file, the
`du` and `stat` utilities. Following is an example of how to use the
`du` utility on an empty file that includes the `-k` option to return the
output in kilobytes.

```
`$` `du -k file`
`4 file`
```

Following example shows how to use the `stat` utility on an empty file to
return the file's disk usage.

```
`$` `/usr/bin/stat --format="%b*%B" file | bc`
`4096`
```

To measure the size of a directory, use the `stat` utility. Find the
`Blocks` value, and then multiply that value by the block size. Following is an
example of how to use the `stat` utility on an empty directory:

```
`$` `/usr/bin/stat --format="%b*%B" . | bc`
`4096`
```

## Metered size of an EFS file system

The metered size of an EFS file system includes the sum of the sizes of all
current objects in all of the EFS storage classes. The size of each object is
calculated from a representative sampling of the size of the object during the metered hour,
for example from 8 AM to 9 AM.

An empty file contributes 6 KiB (2 KiB metadata + 4 KiB data) to the
metered size of a file system. Upon creation, a file system has a single empty root
directory and therefore has a metered size of 6 KiB.

The metered sizes of a particular file system define the usage for which the owner
account is billed for that file system for that hour.

###### Note

The computed metered size doesn't represent a consistent snapshot of the file
system at any particular time during that hour. Instead, it represents the sizes of the
objects that existed in the file system at varying times within each hour, or possibly the
hour before it. These sizes are summed to determine the file system's metered size for the
hour. The metered size of a file system is thus eventually consistent with the metered
sizes of the objects stored when there are no writes to the file system.

You can see the metered size for an EFS file system in the following
ways:

- Using the [describe-file-systems](../../../cli/latest/reference/efs/describe-file-systems.md "../../../cli/latest/reference/efs/describe-file-systems.md") AWS CLI command and the [DescribeFileSystem](API_DescribeFileSystems.md "API_DescribeFileSystems.md") API operation, the response includes the
  following:

```
`"SizeInBytes":{
 "Timestamp": 1403301078,
 "Value": 29313744866,
 "ValueInIA": 675432,
 "ValueInStandard": 29312741784
 "ValueInArchive": 327650
 }`
```

Where the metered size of `ValueInStandard` is also used
to determine your I/O throughput baseline and burst rates for file systems using the
[Bursting throughput](performance.md#throughput-modes "performance.md#throughput-modes").

- View the `StorageBytes` CloudWatch metric, which displays the total metered
  size of data in each storage classes. For more information about the
  `StorageBytes` metric, see [CloudWatch metrics for Amazon EFS](efs-metrics.md "efs-metrics.md").
- Run the `df` command in Linux at the terminal prompt of an EC2 instance.

Don't use the **du** command on the root of the file system for storage metering purposes because
the response does not reflect the full set data used for metering your file system.

###### Note

The metered size of `ValueInStandard` is also used to determine your I/O
throughput baseline and burst rates. For more information, see [Bursting throughput](performance.md#bursting "performance.md#bursting").

### Metering Infrequent Access and Archive storage classes

The EFS Infrequent Access (IA) and Archive
storage classes are metered in 4 KiB increments and have a minimum billing charge per file
of 128 KiB. IA and Archive file metadata (2 KiB per file) is
always stored and metered in the Standard storage class. Support for files
smaller than 128 KiB is only available for lifecycle policies updated on or after 12:00 PM
PT, November 26, 2023. Data access for IA and Archive storage
is metered in 128 KiB increments.

You can use the `StorageBytes` CloudWatch metric to view the metered size of data
in each of the storage classes. The metric also displays the total number of bytes that
are consumed by small-file rounding within the IA and Archive
storage classes. For more information about viewing CloudWatch metrics, see [Accessing CloudWatch metrics for Amazon EFS](accessingmetrics.md "accessingmetrics.md"). For more
information about the `StorageBytes` metric, see [CloudWatch metrics for Amazon EFS](efs-metrics.md "efs-metrics.md").

## Metering throughput

Amazon EFS meters the throughput for read requests at one-third the rate of the other file system I/O operations. For example,
if you are driving 30 mebibytes per second (MiBps) of both read and write throughput, the read portion counts as 10 MiBps of
effective throughput, the write portion counts as 30 MiBps, and the combined metered throughput is 40 MiBps. This combined
throughput adjusted for consumption rates is reflected in the `MeteredIOBytes` CloudWatch metric.

### Metering Elastic

throughput

When Elastic throughput mode is enabled for a file system, you pay only
for the amount of metadata and data read from or written to the file system.
EFS file systems using Elastic throughput mode meter and bill
metadata reads as read operations and metadata writes as write operations. Metadata
operations are metered in 1 KiB increments after the first 4 KiB. Data operations are
metered in 1 KiB increments after the first 32 KiB.

###### Note

While Elastic throughput is designed to scale elastically with your throughput, we recommend implementing proper governance through
monitoring metrics with CloudWatch (MeteredIOBytes) and usage alerts as part of your operational best practices. This helps you maintain optimal
resource utilization and stay within your planned operational parameters. For more information, see [Monitoring metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

### Metering Provisioned

throughput

For file systems that use Provisioned throughput mode, you pay only for the
amount of time that throughput is enabled. Amazon EFS meters file systems with
Provisioned throughput mode enabled once every hour. For metering when
Provisioned throughput mode is set for less than one hour, Amazon EFS calculates
the time-average using millisecond precision.
