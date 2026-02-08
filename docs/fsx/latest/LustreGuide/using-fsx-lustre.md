# Deployment and storage class options for FSx for Lustre file systems

Amazon FSx for Lustre provides two file system deployment options: **persistent**
and **scratch**. It provides three storage classes: **SSD** (solid state drive),
**AWS Interconnect**, and **HDD** (hard disk drive).

You choose the file system deployment type and storage class when you create a new file
system, using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or the Amazon FSx for Lustre API. For more information, see [Step 1: Create your FSx for Lustre file system](getting-started.md#getting-started-step1 "getting-started.md#getting-started-step1") and [CreateFileSystem](../APIReference/API_CreateFileSystem.md "../APIReference/API_CreateFileSystem.md") in the _Amazon FSx API Reference_.

## Persistent file systems

_Persistent file systems_ are designed for
longer-term storage and workloads. For SSD and HDD-based
file systems, data is automatically replicated within the same Availability Zone in which the file
system is located. For Intelligent-Tiering file systems, data is replicated across multiple
Availability Zones. The data volumes attached to the file servers are replicated independently
from the file servers to which they are attached.

Amazon FSx continuously monitors persistent file systems for hardware failures, and
automatically replaces infrastructure components in the event of a failure. On a persistent file
system, if a file server becomes unavailable, it's replaced automatically within minutes of
failure. During that time, client requests for data on that server transparently retry and
eventually succeed after the file server is replaced. Data on persistent file systems is
replicated on disks, and any failed disks are automatically replaced transparently.

Use persistent file systems for longer-term storage and for throughput-focused workloads
that run for extended periods or indefinitely, and that might be sensitive to disruptions in
availability.

Persistent deployment types automatically encrypt data in transit when they are accessed
from Amazon EC2 instances that support encryption in transit.

Amazon FSx for Lustre supports two persistent deployment types: Persistent 1
and Persistent 2.

### Persistent 2 deployment type

Persistent 2 is the latest generation of Persistent deployment type, and is best-suited
for use cases that require longer-term storage, and that require the highest levels of IOPS
and throughput. Persistent 2 file systems support SSD and Intelligent-Tiering storage
classes.

You can create Persistent 2 file systems with a metadata configuration and EFA enabled
using the Amazon FSx console, AWS Command Line Interface, and Amazon FSx API.

### Persistent 1 deployment type

The Persistent 1 deployment type is well-suited for use cases that require longer-term
storage.
Persistent 1 deployment types support SSD (solid state drive) and HDD (hard disk drive)
storage classes.

You can create Persistent 1 deployment types only by using the AWS CLI and the Amazon FSx API.

### Scratch file systems

_Scratch file systems_ are designed for temporary storage
and shorter-term processing of data. Data isn't replicated and doesn't persist if a file
server fails. Scratch file systems provide high burst throughput of up to six times the baseline
throughput of 200 MBps per TiB of storage capacity. For more information, see [Performance characteristics of SSD and HDD storage classes](ssd-storage.md "ssd-storage.md").

Use scratch file systems when you need cost-optimized storage for short-term,
processing-heavy workloads.

On a scratch file system, file servers aren't replaced if they fail and data isn't
replicated. If a file server or a storage disk becomes unavailable on a scratch file system,
files stored on other servers are still accessible. If clients try to access data that is on the
unavailable server or disk, clients experience an immediate I/O error.

The following table illustrates the availability or durability that scratch file systems of
example sizes are designed for, over the course of a day and a week. Because larger file systems
have more file servers and more disks, the probabilities of failure are increased.

| File system size (TiB) | Number of file servers | Availability/durability over one day | Availability/durability over one week |
| ---------------------- | ---------------------- | ------------------------------------ | ------------------------------------- |
| 1.2                    | 2                      | 99.9%                                | 99.4%                                 |
| 2.4                    | 2                      | 99.9%                                | 99.4%                                 |
| 4.8                    | 3                      | 99.8%                                | 99.2%                                 |
| 9.6                    | 5                      | 99.8%                                | 98.6%                                 |
| 50.4                   | 22                     | 99.1%                                | 93.9%                                 |

## IP addresses for file systems

Each FSx for Lustre file system requires one IP address for each metadata server (MDS) and
one IP address for each storage server (OSS).

| File systems using SSD or HDD storage class | File System Type    | Throughput, MBps/TiB | Storage per OSS |
| ------------------------------------------- | ------------------- | -------------------- | --------------- |
| Persistent 2 EFA\*                          | 125                 | 38.4 TiB per OSS     |
| 250                                         | 19.2 TiB per OSS    |
| 500                                         | 9.6 TiB per OSS     |
| 1000                                        | 4.8 TiB per OSS     |
| Persistent 2 non-EFA\*                      | 125, 250, 500, 1000 | 2.4 TiB per OSS      |
| Persistent 1 SSD                            | 50, 100, 200        | 2.4 TiB per OSS      |
| Persistent HDD                              | 12                  | 6 TiB per OSS        |
| 40                                          | 1.8 TiB per OSS     |
| Scratch 2                                   | 200                 | 2.4 TiB per OSS      |
| Scratch 1                                   | 200                 | 3.6 TiB per OSS      |

| File systems using Intelligent-Tiering storage class | File System Type  | Throughput per OSS |
| ---------------------------------------------------- | ----------------- | ------------------ |
| Intelligent-Tiering\*                                | 4000 MBps per OSS |

###### Note

\* Amazon FSx provisions a metadata server for every 12,000 Metadata IOPS
on Persistent 2 SSD and Intelligent-Tiering file systems configured with metadata
configuration.

Amazon FSx for Lustre Intelligent-Tiering file systems support a maximum of 512 TiB of storage per OSS.

## FSx for Lustre storage classes

Amazon FSx for Lustre offers solid state drive (SSD), AWS Interconnect, and hard disk drive (HDD) storage classes
that are optimized for different data processing requirements:

- The SSD storage class provides low-latency (sub-millisecond) access to your full dataset. The SSD storage class
  is provisioned, which means that you specify a file system size and pay storage costs for the amount of
  storage provisioned. Use the SSD storage class for latency-sensitive workloads that require the performance
  of all-flash storage across all data.

Persistent 2 file systems with SSD storage support higher levels of throughput per unit of storage
(that is, 250, 500, or 1000 MBps per TiB) compared to Persistent 1 file systems. For a Persistent 1 file system
with SSD storage, the throughput per unit of storage is either 50, 100, or 200 MBps per TiB. For a Scratch
file system with SSD storage, the throughput per unit of storage is 200 MBps per TiB.

- The Intelligent-Tiering storage class provides fully elastic, intelligently tiered
  storage. Elasticity means that you pay for the amount of data you store and do not have to specify a
  file system size. Intelligent tiering means that you automatically pay less to store data that you haven’t
  accessed recently. This storage class automatically optimizes costs by tiering cold data to lower-cost storage
  tiers. You can provision an optional SSD read cache for low-latency (sub-millisecond) access to your frequently-accessed
  data. The Intelligent-Tiering storage class provides the best balance of price and performance for most workloads.
  Use the Intelligent-Tiering storage class for workloads that are cache-friendly and do not require the performance of
  all-flash storage across all data. Intelligent-Tiering file systems support throughput capacities in increments
  of 4000 MBps.
- The HDD storage class can be used with workloads that need consistent single-digit ms latency
  across all data. You can provision an optional SSD read cache that is sized to 20% of your HDD storage capacity
  to provide low-latency access to frequently-accessed data. With HDD storage, you specify a file system size and
  pay for the amount of storage that you provision. For a Persistent 1 file system with HDD storage, the throughput
  per unit of storage is either 12 or 40 MBps per TiB.

For more information about performance of these storage classes, see
[Performance characteristics of SSD and HDD storage classes](ssd-storage.md "ssd-storage.md") and
[Performance characteristics of Intelligent-Tiering storage class](intelligent-tiering-file-systems.md "intelligent-tiering-file-systems.md").

## How the Intelligent-Tiering storage class tiers data

The Amazon FSx Intelligent-Tiering storage class automatically stores data in three access tiers. It is
designed to optimize storage costs by automatically moving data to the most cost-effective access tier,
without performance impact or operational overhead. The Intelligent-Tiering storage class automatically
tiers data based on last access time, thus automatically optimizing costs for less active data:

- Data accessed in the last 30 days is stored in the Frequent Access tier.
- Data that hasn’t been accessed in 30 consecutive days automatically moves to the
  Infrequent Access tier, and costs less than data in the Frequent Access tier.
- Data that hasn’t been accessed in 90 consecutive days automatically moves to the
  Archive Instant Access tier, and costs less than data in the Infrequent Access tier.

When you access data in the Infrequent Access or Archive Instant Access tiers, the data
automatically moves back to the Frequent Access tier. Additionally, operations like modifying
throughput capacity (which rebalances data across OSTs), re-striping files or directories, or
using `lfs migrate` could move some data back to the Frequent Access tier.

All access to non-cached data has the same performance characteristics, independent of the
data's tier, and there are no additional IOPS, retrieval, or transition costs beyond your normal
read/write operation costs.

## Deployment type availability

Scratch 2, Persistent 1, and Persistent 2 deployment types are available in the following AWS Regions:

| AWS Region                       | Persistent 2 | Persistent 1 | Scratch 2 |
| -------------------------------- | ------------ | ------------ | --------- |
| US East (Ohio)                   | ✓            | ✓            | ✓         |
| US East (N. Virginia)            | ✓            | ✓            | ✓         |
| US East (Atlanta) Local Zone     | ✓ \*         |              |           |
| US East (Dallas) Local Zone      | ✓ \*         |              |           |
| US West (N. California)          | ✓            | ✓            | ✓         |
| US West (Los Angeles) Local Zone |              | ✓            | ✓         |
| US West (Oregon)                 | ✓            | ✓            | ✓         |
| US West (Phoenix) Local Zone     | ✓ \*         |              |           |
| Africa (Cape Town)               |              | ✓            | ✓         |
| Asia Pacific (Hong Kong)         | ✓            | ✓            | ✓         |
| Asia Pacific (Hyderabad)         |              | ✓            | ✓         |
| Asia Pacific (Jakarta)           |              | ✓            | ✓         |
| Asia Pacific (Malaysia)          | ✓ \*         |              |           |
| Asia Pacific (Melbourne)         |              | ✓            | ✓         |
| Asia Pacific (Mumbai)            | ✓            | ✓            | ✓         |
| Asia Pacific (Osaka)             |              | ✓            | ✓         |
| Asia Pacific (Seoul)             | ✓            | ✓            | ✓         |
| Asia Pacific (Singapore)         | ✓            | ✓            | ✓         |
| Asia Pacific (Sydney)            | ✓            | ✓            | ✓         |
| Asia Pacific (Taipei)            | ✓ \*         |              |           |
| Asia Pacific (Thailand)          | ✓ \*         |              |           |
| Asia Pacific (Tokyo)             | ✓            | ✓            | ✓         |
| Canada (Central)                 | ✓            | ✓            | ✓         |
| Canada West (Calgary)            | ✓ \*         |              |           |
| Europe (Frankfurt)               | ✓            | ✓            | ✓         |
| Europe (Ireland)                 | ✓            | ✓            | ✓         |
| Europe (London)                  | ✓            | ✓            | ✓         |
| Europe (Milan)                   |              | ✓            | ✓         |
| Europe (Paris)                   |              | ✓            | ✓         |
| Europe (Spain)                   |              | ✓            | ✓         |
| Europe (Stockholm)               | ✓            | ✓            | ✓         |
| Europe (Zurich)                  |              | ✓            | ✓         |
| Israel (Tel Aviv)                | ✓ \*         |              | ✓         |
| Mexico (Central)                 | ✓ \*         |              |           |
| Middle East (Bahrain)            |              | ✓            | ✓         |
| Middle East (UAE)                |              | ✓            | ✓         |
| South America (São Paulo)        |              | ✓            | ✓         |
| AWS GovCloud (US-East)           |              | ✓            | ✓         |
| AWS GovCloud (US-West)           |              | ✓            | ✓         |

###### Note

\* These AWS Regions support Persistent-125 and Persistent-250
file systems with SSD storage class without EFA.
