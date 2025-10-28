# Performance for Amazon FSx for OpenZFS

Amazon FSx for OpenZFS provides simple, high-performance file storage. In this section, we provide
an overview of FSx for OpenZFS performance for all deployment types, and describe how your file system configuration impacts key performance dimensions. We
also include some important tips and recommendations for maximizing the performance of your file
system.

###### Topics

- [File system performance](#zfs-fs-performance "#zfs-fs-performance")
- [Choosing a deployment type based on performance](#choosing-between "#choosing-between")
- [Choosing a storage class based on performance](#choosing-between-storage-classes "#choosing-between-storage-classes")
- [Migrating between deployment types and storage classes](#migrating-between-deployments "#migrating-between-deployments")
- [Performance on S3 access points](#access-points-performance "#access-points-performance")
- [General tips for maximizing performance](#performance-tips-zfs "#performance-tips-zfs")
- [Monitoring performance](#measure-performance-cw "#measure-performance-cw")
- [How FSx for OpenZFS file systems work with SSD storage](performance-ssd.md "performance-ssd.md")
- [How FSx for OpenZFS file systems work with Intelligent-Tiering](performance-intelligent-tiering.md "performance-intelligent-tiering.md")

## File system performance

File system performance is typically measured in latency, throughput, and I/O operations per second (IOPS).
Amazon FSx for OpenZFS offers three deployment options, Multi-AZ (HA), Single-AZ (HA), and Single-AZ (non-HA).
Both Single-AZ (non-HA and HA) deployment types, also support Single-AZ 1 and Single-AZ 2. Single-AZ 2 offers higher levels of performance than the maximum offered by Single-AZ 1. Each
deployment option offers a different performance profile. In this section, we document the
performance you can expect for frequently accessed data from the in-memory or NVMe caches and
data accessed from disk for both deployment types. We also document the baseline performance
you can always deliver, as well as the burst performance you can drive for short periods of
time.

The specific level of performance a file system can provide is defined by
its _provisioned throughput capacity_, which determines
the size of the file server hosting the file system. Provisioned throughput capacity is equivalent to the
baseline disk throughput supported by your file server. For data access from
disks, your file system’s performance is also dependent on the number of
_provisioned SSD disk IOPS_ configured for the file
system’s underlying disks. Note that the actual level of performance you can drive for your workload depends on a variety of factors.
For more information, see [Tips for maximizing performance](#performance-tips-zfs "#performance-tips-zfs").

## Choosing a deployment type based on performance

Both Single-AZ (non-HA) and Single-AZ (HA) offer two tiers of performance with Single-AZ 1 and Single-AZ 2.
Single-AZ 2 (HA) is recommended for most use cases, given the higher level of both performance and availablity that it provides. Single-AZ 2 file systems offer double the performance scalability as compared to Single-AZ 1, delivering up to 400,000 IOPS and 10 GBps throughput for both reads and writes to persistent SSD storage.

In addition, Single-AZ 2 file systems include an up to 2.5 TB high-speed NVMe
read cache that automatically caches your most recently-accessed data, making that data
accessible at millions of IOPS and with latencies of a few hundred microseconds. Single-AZ 2
file systems are suitable for high-performance workloads such as media processing and
rendering, financial analytics, and machine learning. Single-AZ 2 file systems are also appropriate for
read-heavy workloads with frequently accessed datasets.

In addition to Single-AZ file systems, Amazon FSx for OpenZFS also offers Multi-AZ file systems that offer higher levels of availability and durability in addition to the same
levels of performance as Single-AZ 2. For more information on Multi-AZ (HA) file systems and choosing between deployment types, see [Availability and durability for Amazon FSx for OpenZFS](availability-durability.md "availability-durability.md").

For information on which deployment types are supported in each AWS Region, see [Availability by AWS Region](available-aws-regions.md "available-aws-regions.md")

## Choosing a storage class based on performance

Your file system's performance also depends on its storage class. FSx for OpenZFS offers two storage classes, Intelligent-Tiering (elastic) and SSD (provisioned).

With Intelligent-Tiering, your file system has fully elastic, low-cost storage and access to a built-in SSD-backed write log for low-latency writes and an optional provisioned SSD read cache for low-latency reads.
Intelligent-Tiering is recommended for most Network Attached Storage (NAS) datasets to simplify storage management and reduce costs while offering performance levels comparable to file systems using the SSD (provisioned) storage class for most workloads.
Intelligent-Tiering is suitable for home directories, analytics, and other project-based workloads. For more information on performance for file systems that use Intelligent-Tiering, see [How FSx for OpenZFS file systems work with Intelligent-Tiering](performance-intelligent-tiering.md "performance-intelligent-tiering.md").

With SSD (provisioned) storage, your file system provides low-latency access to your full dataset. SSD (provisioned) is recommend for datasets that require the performance of all-flash storage across all data.
SSD (provisioned) is suitable for databases and non-cache-friendly electronic design automation workloads. For more information on performance for file systems that use SSD (provisioned) storage, see [How FSx for OpenZFS file systems work with SSD storage](performance-ssd.md "performance-ssd.md").

For information on which storage classes are supported in each AWS Region, see [Availability by AWS Region](available-aws-regions.md "available-aws-regions.md")

## Migrating between deployment types and storage classes

Once you create your file system, you cannot change its deployment type or storage class.
However, there are several options that you can use to migrate data from your pre-existing file system to a new file system with your desired deployment type or storage class.

- **Restoring from backup** ‐
  You can create a new Single-AZ 2 file system by restoring from a backup of your Single-AZ 1 file system and choosing the desired deployment type.
  You can also create a Single-AZ (HA) file system from a Single-AZ (non-HA) file system. You cannot create a Multi-AZ file system from a Single-AZ backup or migrate between storage classes by restoring from a backup. For more information, see [Restoring backups](restoring-backups.md "restoring-backups.md").
- **Using on-demand replication** ‐ You can use on-demand replication to synchronize data between file systems with different deployment types or storage classes. For more information, see [Protecting your data with on-demand replication](on-demand-replication.md "on-demand-replication.md").

For more information on how to migrate your data, see [Migrating your existing file storage to Amazon FSx for OpenZFS](migrating-fsx-openzfs.md "migrating-fsx-openzfs.md").

## Performance on S3 access points

Amazon S3 access points for FSx for OpenZFS file systems deliver latency in the tens of milliseconds range, consistent
with S3 bucket access. Requests per second and throughput performance scale with your Amazon FSx ﬁle system's
provisioned throughput and SSD. For example, your applications can achieve up to 3,500 PUT or 5,500 GET
requests per second (consistent with what you can achieve per Amazon S3 partitioned prefix) and 3.5 GBps of
write (PUT) throughput and 10 GBps of read (GET) throughput on a file system provisioned with the maximum
throughput capacity level.

## General tips for maximizing performance

FSx for OpenZFS file systems are designed to deliver the maximum performance of your file system
across your clients in aggregate, whether you are supporting data access from a single client,
or thousands of clients. The following sections provide some practical tips on how to maximize client performance.

### Client considerations

#### Amazon EC2 instances

When launching the Amazon EC2 instances that will work with your FSx for OpenZFS file system,
ensure that they can support the level of performance your file system needs to deliver.
Ensure they have the compute, memory, and network capacity sufficient to drive the throughput,
IOPS, and latencies provided by your FSx for OpenZFS file system.

To determine your EC2 instance’s compute and memory capacity,
see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md")
in the _Amazon EC2 User Guide for Linux Instances_. To determine
its network capacity, see
[Amazon EC2 instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md")
in the same guide. The performance characteristics of FSx for OpenZFS file systems don't depend
on the use of Amazon EC2–optimized instances.

#### NFS nconnect

With FSx for OpenZFS, NFS clients can use the `nconnect` mount option to have multiple
TCP connections (up to 16) associated with a single NFS mount. Such an NFS client multiplexes
file operations onto multiple TCP connections (multi-flow) in a round-robin fashion to obtain
improved performance beyond single TCP connection (single-flow) limits. For more information
on single-flow limits, see
[Amazon EC2 instance network bandwidth](../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md "../../../AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.md")
in the _Amazon EC2 User Guide for Linux Instances_.

The following command demonstrates how to use the `nconnect` mount option
to mount an FSx for OpenZFS volume with a maximum of 16 simultaneous connections:

```
`sudo mount -t nfs -o nconnect=16 `filesystem_dns_name`:/`vol_path` /`localpath``
```

The `nconnect` mount option is supported for all NFS versions (v3, v4.0, v4.1, v4.2). NFS `nconnect` is supported by default in Linux kernel
versions 5.3 and above, including the latest Ubuntu 18.04 LTS. In addition, RHEL8.3 supports `nconnect` by way of a backport into the
`4.18.0-240.e18` kernel and newer.

#### NFS v3

FSx for OpenZFS file systems flexibly support multiple versions of the NFS protocol (v3, v4.0, v4.1, v4.2).
While more recent versions of NFS can better support simultaneous access from many clients (due to
a more robust file-locking mechanism) and client-side caching, NFS v3 may still provide improved latency,
throughput, and IOPS performance for performance-sensitive workloads. You can mount using NFS v3 from
Linux, Windows, or macOS EC2 instances. For more information, see
[Step 2: Mount your file system from an Amazon EC2 instance](getting-started.md#getting-started-step2 "getting-started.md#getting-started-step2").

The following example illustrates how to specify NFS v3 when mounting an FSx for OpenZFS volume:

```
`sudo mount -t nfs -o nfsvers=3 `fs-dns-name`:/`vol_path` /`local_path``
```

#### NFS delegations

To improve the ability of NFS clients to cache data locally, NFS v4 introduced NFS delegations,
or the ability of the server to delegate certain responsibilities to the client. If the client is
granted a read delegation, it is assured that no other client has the ability to write to the file
for the duration of the delegation, meaning that the client can read from its local copy instead
of having to go back to the file server.

FSx for OpenZFS file systems support NFS v4 file read delegations. To take advantage of this capability,
ensure your clients are mounting with NFS v4.0 or higher.

#### Request model

When you mount your file system, asynchronous writes are enabled by default (that is,
`-o async`). With asynchronous writes, pending write operations are buffered
on the client before they are written to your Amazon FSx file system, enabling lower
latencies for these operations. A client that has enabled synchronous writes (that is,
`-o sync`), or one that opens files using an option that bypasses the cache
(for example, `O_DIRECT`), issues synchronous requests, which means that every
operation incurs a round-trip between your client and the file server. We recommend using
the default asynchronous write option to maximize client performance.

#### Other recommended mount options

To improve the performance of your file system, you can also configure the following
options when mounting your file system:

- `rsize=1048576` – Sets the maximum number of bytes
  of data that the NFS client can receive for each network READ request to 1048576 bytes (1 MB).
  Due to lower memory capacity on file systems with 64 MBps and 128 MBps of provisioned throughput,
  these file systems will only accept a maximum `rsize` of 262144 and 524288 bytes, respectively.
- `wsize=1048576` – Sets the maximum number of bytes
  of data that the NFS client can send for each network WRITE request to 1048576 bytes (1 MB).
  Due to lower memory capacity on file systems with 64 MBps and 128 MBps of provisioned throughput,
  these file systems will only accept a maximum `wsize` of 262144 and 524288 bytes, respectively.
- `timeo=600` – Sets the timeout value that the NFS client
  uses to wait for a response before it retries an NFS request to 600 deciseconds (60 seconds).
- `_netdev` – When present in **/etc/fstab**,
  prevents the client from attempting to mount the FSx for OpenZFS volume until the network has been enabled.

The following example uses sample values.

```
`sudo mount -t nfs -o rsize=1048576,wsize=1048576,timeo=600 fs-01234567890abcdef1.fsx.us-east-1.amazonaws.com:/fsx/vol1 /fsx`
```

### File system and volume configurations

#### Storage capacity utilization

As the amount of used storage space gets closer to the total available storage capacity, Amazon FSx (like other file systems) spends more time finding suitable places
to store new files and their metadata. This leads to higher latency for operations that modify files,
which can negatively impact overall performance. To avoid this performance impact, we recommended keeping storage utilization of SSD (provisioned) file systems below 80% of the total capacity.
If needed, you can increase your maximum storage capacity at anytime, without disruption to your end users or applications. For more information, see [Modifying provisioned SSD storage capacity
and IOPS](managing-storage-capacity.md "managing-storage-capacity.md").

You do not need to modify storage capacity if your file system uses the Intelligent-Tiering storage class. For more information, see
[How FSx for OpenZFS file systems work with Intelligent-Tiering](performance-intelligent-tiering.md "performance-intelligent-tiering.md").

#### Provisioned throughput capacity and in-memory cache

In addition to defining the throughput and IOPS that a file system can deliver, a file system's provisioned throughput
capacity also determines the amount of in-memory cache on your file server. Increasing your file system's throughput
capacity improves workload performance in two ways.

First, it increases the throughput and IOPS you can drive from disk (disk I/O) and from in-memory cache.
Second, by increasing the amount of in-memory cache, you can store more data in your file server's in-memory cache,
which drives higher cached performance for larger workloads.

Some request- or metadata-intensive workloads will also benefit from a larger file server in-memory cache.
These types of workloads can generate and store a large volume of metadata in the in-memory cache. To ensure
the size of your file server's in-memory cache is not a bottleneck for your file system performance, we
recommend provisioning at least 128 MBps of throughput capacity for these types of workloads.

#### NFS export options (sync and async)

On the file server side, the `sync` or `async`
NFS export option can impact performance. (This is distinct from the
similarly-named option you use when mounting your FSx for OpenZFS volume on your client.)
This option determines whether your file server will acknowledge client I/O requests
as complete when they are written to the file server’s in-memory cache (`async`),
or only after they are committed to the file server’s persistent disks (`sync`).
`sync` is the default option and is generally recommended for most workloads.

If you have performance-intensive workloads that can use an FSx for OpenZFS volume as
temporary storage for shorter-term data processing or workloads that are resilient to
data loss, you can use the `async` option to achieve substantially higher performance.
Because an FSx for OpenZFS volume exported with the `async` option will acknowledge
client writes before they are committed to durable disk storage, clients can write data to
the file server at a significantly faster rate. However, this performance comes at the
cost of losing data from acknowledged writes that have not yet been committed to the server's disks, in the event of a file server crash.

#### Data compression

For read-heavy workloads, compression can significantly improve the overall
throughput performance of your file system because it reduces the amount of data
that needs to be sent between the underlying storage and the file server.
FSx for OpenZFS volumes support the following data compression algorithms.

- _Zstandard compression_ delivers very high levels of
  on-disk data compression, with higher read throughput and reduced write throughput performance than
  LZ4 compression.
- _LZ4 compression_ delivers higher write throughput performance, but achieves
  lower levels of data compression than Zstandard compression.

With data compression, you can improve your read throughput on data accessed from disk up
to the same levels you deliver for frequently accessed cached data. The specific improvement
depends upon the amount by which compression can reduce the size of your dataset. Your effective
throughput will be roughly equivalent to the product of your provisioned disk throughput and
your compression ratio (defined as the ratio of the size of the compressed data to the size
of the uncompressed data). For the highest provisioned throughput level (4096 MBps), common
Z-Standard compression ratios of 2-3x can increase your effective read throughput by up
to 8-12 GBps.

You can change a volume's data compression to improve performance. Changing this property affects only
newly-written data on the volume.

#### ZFS record size

The ZFS record size specifies a suggested block size for files in the volume. This
property is designed solely for use with databases and other workloads that access files
in fixed-size records. ZFS automatically tunes block sizes according to internal
algorithms optimized for typical access patterns. When you create a volume, the default
record size for file systems using the Intelligent-Tiering storage class is 1024 KiB. The default for all other file systems is 128 KiB. General purpose workflows perform well using the default record
size, and we don't recommend changing it, as it may adversely affect performance.

For database workflows that create very large files but access them in small random chunks, specifying a
record size greater than or equal to the record size of the database can result in significant
performance gains. For databases that use a fixed disk block or record size for I/O, set the
ZFS record size to match it. See
[Dataset record size](https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Workload%20Tuning.html#dataset-recordsize "https://openzfs.github.io/openzfs-docs/Performance%20and%20Tuning/Workload%20Tuning.html#dataset-recordsize") in the OpenZFS documentation for more information.

Streaming workflows such as multimedia and video can benefit from setting a larger record size than the default value.
For more information about setting the record size on a volume, see [Managing Amazon FSx for OpenZFS volumes](managing-volumes.md "managing-volumes.md").

You can change a volume's record size to make performance improvements. Changing the volume record
size affects only files created afterward; existing files are unaffected.

## Monitoring performance

Every minute, FSx for OpenZFS emits usage metrics to Amazon CloudWatch and you can use these metrics to help
identify opportunities to improve the performance your clients can drive from your file system.

You can investigate aggregate file system performance with the `Sum` statistic of
each metric. For example, the `Sum` of the `DataReadBytes` statistic reports
the total read throughput by file system or volume, and the `Sum` of the
`DataWriteBytes` statistic reports the total write throughput by file system or volume.

For more information on monitoring your file system’s performance,
see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
