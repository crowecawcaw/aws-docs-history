# Amazon EFS performance specifications

The following sections provide an overview of Amazon EFS performance, and describe how your file
system configuration impacts key performance dimensions. We also provide some important tips and
recommendations for optimizing the performance of your file system.

###### Topics

- [Performance summary](#performance-overview "#performance-overview")
- [Storage classes](#storage-perf "#storage-perf")
- [Performance modes](#performancemodes "#performancemodes")
- [Throughput modes](#throughput-modes "#throughput-modes")
- [Amazon EFS performance tips](performance-tips.md "performance-tips.md")
- [Troubleshooting Amazon EFS performance
  issues](troubleshooting-efs-general.md "troubleshooting-efs-general.md")
- [Troubleshooting AMI and kernel issues](troubleshooting-efs-ami-kernel.md "troubleshooting-efs-ami-kernel.md")

## Performance summary

File system performance is typically measured by using the dimensions of latency,
throughput, and Input/Output operations per second (IOPS). Amazon EFS performance across these
dimensions depends on your file system's configuration. The following configurations impact
the performance of an Amazon EFS file system:

- **File system type** – Regional or One Zone
- **Performance mode** – General Purpose or Max I/O

###### Important

Max I/O performance mode has higher per-operation latencies than General Purpose performance
mode. For faster performance, we recommend always using General Purpose performance
mode. For more information, see [Performance modes](#performancemodes "#performancemodes").

- **Throughput mode** – Elastic, Provisioned, or
  Bursting

The following table outlines performance specifications for file systems using
General Purpose performance mode and the possible different combinations of file system type
and throughput mode.

Performance specifications for file systems using General Purpose
performance mode| Storage and throughput<br>configuration | Latency1 | Maximum<br>IOPS | Maximum throughput |
| --- | --- | --- | --- |
| **File system type** | **Throughput mode** | **Read operations** | **Write operations** | **Read operations** | **Write operations** | **Per-file-system<br>read**2 | **Per-file-system<br>write**2 | **Per-client read/write** |
| **Regional** | Elastic | As low as 250 microseconds (µs) | As low as 2.7 milliseconds (ms) | 900,000–2,500,0003 | 500,000**3** | 20–60 gibibytes per second (GiBps) | 1–5 GiBps | 1,500 mebibytes per second (MiBps)4 |
| **Regional** | Provisioned | As low as 250 µs | As low as 2.7 ms | 55,000 | 25,000 | 3–10 GiBps | 1–3.33 GiBps | 500 MiBps |
| **Regional** | Bursting | As low as 250 µs | As low as 2.7 ms | 35,000 | 7,000 | 3–5 GiBps | 1–3 GiBps | 500 MiBps |
| **One Zone** | Elastic, Provisioned, Bursting | As low as 250 µs | As low as 1.6 ms | 35,000 | 7,000 | 3 GiBps5 | 1 GiBps5 | 500 MiBps |

1. Latency values shown represent best-case performance under optimal conditions. Actual
   results may vary based on network, workload, and system factors.
2. Maximum read and write throughput depend on the AWS Region. Throughput in excess of
   an AWS Region's maximum throughput requires a throughput quota increase. Any request for
   additional throughput is considered on a case-by-case basis by the Amazon EFS service team.
   Approval might depend on your type of workload. To learn more about requesting quota
   increases, see [Amazon EFS quotas](limits.md "limits.md").
3. By default, file systems that use Elastic throughput drive a maximum of
   90,000 read IOPS for infrequently accessed data, 250,000 read IOPS for frequently accessed
   data, and 50,000 write IOPS. If your workload requires more IOPS, then you can request an
   increase of up to 10 times these numbers. For more information, see [Amazon EFS quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits"). Additional recommendations apply to
   achieve maximum IOPS. For more information, see [Optimizing workloads that demand high throughput and
   IOPS](performance-tips.md#recs-intensive-workloads "performance-tips.md#recs-intensive-workloads").
4. The maximum combined read and write throughput is 1,500 MiBps for file systems using
   Elastic throughput and mounted using version 2.0 or later of the Amazon EFS client
   (amazon-efs-utils version) or the Amazon EFS CSI Driver (aws-efs-csi-driver). For all other
   file systems, the throughput limit is 500 MiBps. For more information about the Amazon EFS
   client, see [Installing the Amazon EFS client](using-amazon-efs-utils.md "using-amazon-efs-utils.md").
5. One Zone file systems that use Bursting throughput can drive
   the same per-file-system read and write throughput amounts as Regional file
   systems using Bursting throughput (maximum read of 5 GiBps for read and 3
   GiBps for write).

## Storage classes

Amazon EFS storage classes are designed for the most effective storage depending on use
cases.

- EFS Standard storage class uses solid state drive (SSD) storage to deliver the
  lowest levels of latency for frequently accessed files. This storage class provides
  first-byte latencies as low as 250 microseconds for reads and 2.7 milliseconds for
  writes.
- EFS Infrequent Access (IA) and EFS Archive storage classes store less frequently accessed data
  that doesn't require the latency performance that frequently accessed data requires. These
  storage classes provide first-byte latencies of tens of milliseconds.

For more information about EFS storage classes, see [EFS storage classes](features.md#storage-classes "features.md#storage-classes").

## Performance modes

Amazon EFS offers two performance modes, General Purpose and Max I/O.

- **General Purpose mode**
  has the lowest per-operation latency and is the default performance mode for file systems. One Zone file systems
  always use the General Purpose performance mode. For faster performance,
  we recommend always using General Purpose performance mode.
- **Max I/O mode** is a previous generation performance type that is designed for highly parallelized workloads that can tolerate higher latencies
  than the General Purpose mode. Max I/O mode is not supported for One Zone file systems or
  file systems that use Elastic throughput.

###### Important

Due to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems.

To help ensure that your workload stays within the IOPS limit available to file systems
using General Purpose performance mode, you can monitor the `PercentIOLimit` CloudWatch metric. For
more information, see [CloudWatch metrics for Amazon EFS](efs-metrics.md "efs-metrics.md").

Applications can scale their IOPS elastically up to the limit associated with the
performance mode. You are not billed separately for IOPS; they are included in a file system's
throughput accounting. Every Network File System (NFS) request is accounted for as 4 kilobyte
(KB) of throughput, or its actual request and response size, whichever is larger.

## Throughput modes

A file system's throughput mode determines the throughput available to your file system.
Amazon EFS offers three throughput modes: Elastic, Provisioned, and Bursting. Read throughput is
discounted to allow you to drive higher read throughput than write throughput. The maximum
throughput available with each throughput mode depends on the AWS Region. For more
information about the maximum file system throughput in the different regions, see
[Amazon EFS quotas](limits.md "limits.md").

Your file system can achieve a combined 100% of its read and write throughput. For
example, if your file system is using 33% of its read throughput limit, the file system can
simultaneously achieve up to 67% of its write throughput limit. You can monitor your file
system’s throughput usage in the **Throughput utilization (%)**
graph on the on the **File System Detail** page of the console. For more
information, see [Monitoring throughput
performance](how_to_use_metrics.md#monitor-throughput-performance "how_to_use_metrics.md#monitor-throughput-performance").

### Choosing the correct throughput mode for a file system

Choosing the correct throughput mode for your file system depends on your workload's
performance requirements.

- **Elastic throughput** (Recommended) – Use
  the default Elastic throughput when you have spiky or unpredictable
  workloads and performance requirements that are difficult to forecast, or when your
  application drives throughput at an average-to-peak ratio of 5% or less. For more
  information, see [Elastic throughput](#elastic "#elastic").
- **Provisioned throughput** – Use
  Provisioned throughput if you know your workload's performance
  requirements, or when your application drives throughput at an average-to-peak ratio of
  5% or more. For more information, see [Provisioned throughput](#provisioned-throughput "#provisioned-throughput").
- **Bursting throughput** – Use
  Bursting throughput when you want throughput that scales with the
  amount of storage in your file system.

If, after using Bursting throughput, you find that your application is
throughput-constrained (for example, it uses more than 80% of the permitted throughput
or you have used all of your burst credits), then you should use either Elastic or
Provisioned throughput. For more information, see [Bursting throughput](#bursting "#bursting").

For
more information about Amazon EFS metrics, see [CloudWatch metrics for Amazon EFS](efs-metrics.md "efs-metrics.md").

### Elastic throughput

For file systems that are using Elastic throughput, Amazon EFS automatically
scales throughput performance up or down to meet the needs of your workload activity.
Elastic throughput is the best throughput mode for spiky or unpredictable
workloads with performance requirements that are difficult to forecast, or for applications
that drive throughput at 5% or less of the peak throughput on average (the average-to-peak
ratio).

Because throughput performance for file systems with Elastic throughput
scales automatically, you don't need to specify or provision the throughput capacity to meet
your application needs. You pay only for the amount of metadata and data read or written,
and you don't accrue or consume burst credits while using Elastic
throughput.

###### Note

While Elastic throughput is designed to scale elastically with your throughput, we recommend implementing proper governance through
monitoring metrics with CloudWatch (MeteredIOBytes) and usage alerts as part of your operational best practices. This helps you maintain optimal
resource utilization and stay within your planned operational parameters. For more information, see [Monitoring metrics with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

For information about per-Region Elastic throughput
limits, see [Amazon EFS quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits").

### Provisioned throughput

With Provisioned throughput, you specify a level of throughput that the
file system can drive independent of the file system's size or burst credit balance. Use
Provisioned throughput if you know your workload's performance requirements,
or if your application drives throughput at 5% or more of the average-to-peak ratio.

For file systems using Provisioned throughput, you are charged for the
amount of throughput enabled for the file system. The throughput amount billed in a month is
based on the throughput provisioned in excess of your file system’s included baseline
throughput from Standard storage, up to the prevailing Bursting
baseline throughput limits in the AWS Region.

If the file system’s baseline throughput exceeds the Provisioned
throughput amount, then it automatically uses the Bursting throughput
allowed for the file system (up to the prevailing Bursting baseline throughput
limits in that AWS Region).

For information about per-Region Provisioned throughput
limits, see [Amazon EFS quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits").

#### Bursting throughput

Bursting throughput is recommended for workloads that require throughput
that scales with the amount of storage in your file system. With Bursting
throughput, the base throughput is proportionate to the file system's size in the
Standard storage class, at a rate of 50 KiBps per each GiB of storage. Burst
credits accrue when the file system consumes below its base throughput rate, and are
deducted when throughput exceeds the base rate.

When burst credits are available, a file system can drive throughput up to 100 MiBps
per TiB in Standard storage (50 KiBps per GiB), up to the AWS Region
limit, with a minimum of 100 MiBps. If no burst credits are available, a file system can
drive up to 50 MiBps per TiB of storage, with a minimum of 1 MiBps.

For information about per-Region Bursting throughput,
see [General resource quotas that cannot be changed](limits.md#ResourceHardLimits "limits.md#ResourceHardLimits").

##### Understanding Amazon EFS burst credits

With Bursting throughput, each file system earns burst credits over
time at a baseline rate that is determined by the size of the file system that is stored
in the EFS Standard storage class. The baseline rate is 50 MiBps per tebibyte
[TiB] of storage (equivalent to 50 KiBps per GiB of storage). Amazon EFS meters read
operations up to one-third the rate of write operations, permitting the file system to
drive a baseline rate up to 150 KiBps per GiB of read throughput, or 50 KiBps per GiB of
write throughput.

A file system can drive throughput at its baseline metered rate continuously. A file
system accumulates burst credits whenever it is inactive or driving throughput below its
baseline metered rate. Accumulated burst credits give the file system the ability to
drive throughput above its baseline rate.

For example, a file system with 100 GiB of metered data in the
Standard storage class has a baseline throughput of 5 MiBps. Over a
24-hour period of inactivity, the file system earns 432,000 MiB worth of credit (5 MiB
**×** 86,400 seconds **=**
432,000 MiB), which can be used to burst at 100 MiBps for 72 minutes (432,000 MiB
**÷** 100 MiBps **=** 72
minutes).

File systems larger than 1 TiB can always burst for up to 50 percent of the time if
they are inactive for the remaining 50 percent of the time.

The following table provides examples of bursting behavior.

| File system size                            | Burst throughput                                                                                                                                            | Baseline throughput                                                                                                        |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 100 GiB of metered data in Standard storage | • Burst to 300 (MiBps) read-only for up to 72 minutes per day, or<br>• Burst to 100 MiBps write-only for up to 72 minutes per day                           | • Drive up to 15 MiBps read-only continuously<br>• Drive up to 5 MiBps write-only continuously                             |
| 1 TiB of metered data in Standard storage   | • Burst to 300 MiBps read-only for 12 hours per day, or<br>• Burst to 100 MiBps write-only for 12 hours per day                                             | • Drive 150 MiBps read-only continuously<br>• Drive 50 MiBps write-only continuously                                       |
| 10 TiB of metered data in Standard storage  | • Burst to 3 GiBps read-only for 12 hours per day, or<br>• Burst to 1 GiBps write-only for 12 hours per day                                                 | • Drive 1.5 GiBps read-only continuously<br>• Drive 500 MiBps write-only continuously                                      |
| Generally, larger file systems              | • Burst to 300 MiBps read-only per TiB of storage for 12 hours per day,<br>or<br>• Burst to 100 MiBps write-only per TiB of storage for 12 hours per<br>day | • Drive 150 MiBps read-only per TiB of storage continuously<br>• Drive 50 MiBps write-only per TiB of storage continuously |

###### Note

Amazon EFS provides a metered throughput
of 1 MiBps to all file systems, even if the baseline rate is lower.

The file system size used to determine the baseline and burst rates is the
`ValueInStandard` metered size available through the [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md") API
operation.

File systems can earn credits up to a maximum credit balance of 2.1 TiB for file
systems smaller than 1 TiB, or 2.1 TiB per TiB stored for file systems larger than 1
TiB. This behavior means that file systems can accumulate enough credits to burst for
up to 12 hours continuously.

### Restrictions on switching throughput and changing

provisioned amount

You can switch an existing file system's throughput mode and change the throughput
amount. However, after switching the throughput mode to Provisioned
throughput or changing the Provisioned throughput amount, the following
actions are restricted for a 24-hour period:

- Switching from Provisioned throughput mode to Elastic or
  Bursting throughput mode.
- Decreasing the Provisioned throughput amount.
