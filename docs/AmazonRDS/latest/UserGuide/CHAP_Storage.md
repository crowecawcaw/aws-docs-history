# Amazon RDS DB instance storage

DB instances for Amazon RDS for Db2, MariaDB, MySQL, PostgreSQL, Oracle, and Microsoft SQL
Server use Amazon Elastic Block Store (Amazon EBS) volumes for database and log storage.

In some cases, your database workload might not be able to achieve 100 percent of the IOPS
that you have provisioned. For more information, see [Factors that affect database performance](#CHAP_Storage.Other.Factors "#CHAP_Storage.Other.Factors").

For more information about instance storage pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

###### Topics

- [Amazon RDS storage types](#Concepts.Storage "#Concepts.Storage")
- [Provisioned IOPS SSD storage](#USER_PIOPS "#USER_PIOPS")
- [General Purpose SSD storage](#Concepts.Storage.GeneralSSD "#Concepts.Storage.GeneralSSD")
- [Performance characteristics of solid-state drive (SSD) storage types](#storage-comparison "#storage-comparison")
- [Magnetic storage (legacy, not recommended)](#CHAP_Storage.Magnetic "#CHAP_Storage.Magnetic")
- [Additional storage volumes](#Welcome.AdditionalStorageVolumes "#Welcome.AdditionalStorageVolumes")
- [Dedicated log volume (DLV)](#CHAP_Storage.dlv "#CHAP_Storage.dlv")
- [Monitoring database performance](#Concepts.Storage.Metrics "#Concepts.Storage.Metrics")
- [Factors that affect database performance](#CHAP_Storage.Other.Factors "#CHAP_Storage.Other.Factors")

## Amazon RDS storage types

Amazon RDS provides three storage types: Provisioned IOPS SSD (also known as io1 and io2
Block Express), General Purpose SSD (also known as gp2 and gp3), and magnetic (also
known as standard). They differ in performance characteristics and price, which means
that you can tailor your storage performance and cost to the needs of your database
workload. You can create Db2, MySQL, MariaDB, and PostgreSQL
RDS DB instances with up to 64 tebibytes (TiB) of storage. You can create Oracle and SQL
Server instances with up to 256 TiB of storage with additional storage volumes. For
more information, see [Additional storage volumes](#Welcome.AdditionalStorageVolumes "#Welcome.AdditionalStorageVolumes"). RDS for Db2
doesn't support the gp2 and magnetic storage types.

The following list briefly describes the three storage types:

- Provisioned IOPS SSD – Provisioned IOPS
  storage is designed to meet the needs of I/O-intensive workloads, particularly
  database workloads, that require low I/O latency and consistent I/O throughput.
  Provisioned IOPS storage is best suited for production environments.

For more information about Provisioned IOPS storage, including the storage
size ranges, see [Provisioned IOPS SSD storage](#USER_PIOPS "#USER_PIOPS").

- General Purpose SSD – General Purpose
  SSD volumes offer cost-effective storage that is ideal for a broad range of
  workloads running on medium-sized DB instances. General Purpose storage is best
  suited for development and testing environments.

For more information about General Purpose SSD storage, including the storage
size ranges, see [General Purpose SSD storage](#Concepts.Storage.GeneralSSD "#Concepts.Storage.GeneralSSD").

- Magnetic – Amazon RDS also supports magnetic
  storage for backward compatibility. We recommend that you use General Purpose
  SSD or Provisioned IOPS SSD for any new storage needs. The maximum amount of
  storage allowed for DB instances on magnetic storage is 3 TiB. For more
  information, see [Magnetic storage (legacy, not recommended)](#CHAP_Storage.Magnetic "#CHAP_Storage.Magnetic").

## Provisioned IOPS SSD storage

For a production application that requires fast and consistent I/O performance, we
recommend Provisioned IOPS storage. Provisioned IOPS storage is a storage type that
delivers predictable performance, and consistently low latency. Provisioned IOPS storage
is optimized for online transaction processing (OLTP) workloads that require consistent
performance. Provisioned IOPS helps performance tuning of these workloads.

Amazon RDS offers two types of Provisioned IOPS SSD storage: io2 and io1. When you create a
DB instance, you specify the IOPS rate and the size of the volume. Amazon RDS provides that
IOPS rate for the DB instance until you change it.

###### Topics

- [io2 Block Express storage (recommended)](#USER_PIOPS.io2 "#USER_PIOPS.io2")
- [io1 storage (previous generation)](#USER_PIOPS.io1 "#USER_PIOPS.io1")
- [Combining Provisioned IOPS storage with Multi-AZ deployments or read replicas](#Overview.ProvisionedIOPS-support "#Overview.ProvisionedIOPS-support")
- [Provisioned IOPS storage costs](#Overview.ProvisionedIOPS-cost "#Overview.ProvisionedIOPS-cost")
- [Getting the best performance from Amazon RDS Provisioned IOPS storage](#Overview.ProvisionedIOPS.gettingthemostoutofpiops "#Overview.ProvisionedIOPS.gettingthemostoutofpiops")

### io2 Block Express storage (recommended)

For I/O-intensive and latency-sensitive workloads, we recommend that you use
Provisioned IOPS SSD io2 Block Express storage to achieve up to 256,000 I/O
operations per second (IOPS). The throughput of io2 Block Express volumes varies
based on the amount of IOPS provisioned per volume and on the size of the I/O
operations being run.

All RDS io2 volumes based on the AWS Nitro System are io2 Block Express volumes
and provide sub-millisecond average latency. DB instances not based on the AWS
Nitro System are io2 volumes.

The following table shows the range of Provisioned IOPS and maximum throughput per storage volume for
each database engine and storage size range. In Amazon RDS for Oracle and SQL Server, you can
attach up to three additional storage volumes in addition to the primary storage volumes
to provision up to 256 TiB storage size in total. With additional storage volumes, you
can have higher provisioned IOPS and maximum throughput for your DB instance. However, your DB instance
might not be able to fully utilize the provisioned IOPS and maximum throughput if your instance class
has lower limits than the values you've provisioned for your storage volumes. For more information, see
[Factors that affect database performance](#CHAP_Storage.Other.Factors "#CHAP_Storage.Other.Factors").

| Database engine                     | Range of storage size | Range of Provisioned IOPS | Maximum throughput |
| ----------------------------------- | --------------------- | ------------------------- | ------------------ |
| Db2, MariaDB, MySQL, and PostgreSQL | 100–65,536 GiB        | 1,000–256,000 IOPS        | 16,000 MiB/s       |
| Oracle                              | 100–199 GiB           | 1,000–199,000 IOPS        | 4,000 MiB/s        |
| Oracle                              | 200–65,536 GiB        | 1,000–256,000 IOPS        | 16,000 MiB/s       |
| SQL Server                          | 20–65,536 GiB         | 1,000–256,000 IOPS        | 4,000 MiB/s        |

The IOPS and storage size ranges have the following constraints:

- The ratio of IOPS to allocated storage (in GiB) must be from
  0.5–1,000. For DB instances not based on the AWS Nitro System, the
  ratio must be from 0.5–500.
- Maximum IOPS can be provisioned with volumes 256 GiB and larger (1,000
  IOPS × 256 GiB = 256,000 IOPS). For DB instances not based on the AWS
  Nitro System, maximum IOPS are achieved at 512 GiB (500 IOPS x 512 GiB =
  256,000 IOPS).
- Throughput scales proportionally up to 0.256 MiB/s per provisioned IOPS.
  Maximum throughput of 4,000 MiB/s can be achieved at 256,000 IOPS with a
  16-KiB I/O size and 16,000 IOPS or higher with a 256-KiB I/O size. For DB
  instances not based on the AWS Nitro System, maximum throughput of 2,000
  MiB/s can be achieved at 128,000 IOPS with a 16-KiB I/O size.
- If you're using storage autoscaling, the same ratios between IOPS and
  maximum storage threshold (in GiB) also apply. For more information on
  storage autoscaling, see [Managing capacity automatically with Amazon RDS storage autoscaling](USER_PIOPS.md "USER_PIOPS.md").

Amazon RDS io2 Block Express volumes are available in all commercial AWS Regions and
AWS GovCloud (US) Regions. These volumes aren't available in the China Regions.

### io1 storage (previous generation)

For I/O-intensive workloads, you can use Provisioned IOPS SSD io1 storage and
achieve up to 256,000 I/O operations per second (IOPS). The throughput of io1
volumes varies based on the amount of IOPS provisioned per volume and on the size of
the I/O operations being run. We recommend using io2 Block Express storage where
it's available.

The following table shows the range of Provisioned IOPS and maximum throughput for
each database engine and storage size range.

| Database engine                     | Range of storage size | Range of Provisioned IOPS | Maximum throughput |
| ----------------------------------- | --------------------- | ------------------------- | ------------------ |
| Db2, MariaDB, MySQL, and PostgreSQL | 100–399 GiB           | 1,000–19,950 IOPS         | 500 MiB/s          |
| Db2, MariaDB, MySQL, and PostgreSQL | 400–65,536 GiB        | 1,000–256,000 IOPS        | 4,000 MiB/s        |
| Oracle                              | 100–199 GiB           | 1,000–9,950 IOPS          | 500 MiB/s          |
| Oracle                              | 200–65,536 GiB        | 1,000–256,000 IOPS¹       | 4,000 MiB/s        |
| SQL Server                          | 20–16,384 GiB         | 1,000–64,000 IOPS²        | 1,000 MiB/s        |

###### Note

¹ For Oracle, you can provision the maximum 256,000 IOPS only on the r5b
instance type.

² For SQL Server, the maximum 64,000 IOPS is guaranteed only on [Nitro-based instances](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances") that are on the m5\*, m6i, r5\*, r6i, and z1d
instance types. Other instance types guarantee performance up to 32,000
IOPS.

The IOPS and storage size ranges have the following constraints:

- The ratio of IOPS to allocated storage (in GiB) must be from 1–50
  on RDS for SQL Server, and 0.5–50 on other RDS DB engines.
- If you're using storage autoscaling, the same ratios between IOPS and
  maximum storage threshold (in GiB) also apply.

For more information on storage autoscaling, see [Managing capacity automatically with Amazon RDS storage autoscaling](USER_PIOPS.md "USER_PIOPS.md").

### Combining Provisioned IOPS storage with Multi-AZ deployments or read replicas

For production OLTP use cases, we recommend that you use Multi-AZ deployments for
enhanced fault tolerance with Provisioned IOPS storage for fast and predictable
performance.

You can also use Provisioned IOPS storage with read replicas for MySQL, MariaDB or
PostgreSQL. The type of storage for a read replica is independent of that on the
primary DB instance. For example, you might use General Purpose SSD for read
replicas with a primary DB instance that uses Provisioned IOPS SSD storage to reduce
costs. However, your read replica's performance in this case might differ from that
of a configuration where both the primary DB instance and the read replicas use
Provisioned IOPS storage.

### Provisioned IOPS storage costs

With Provisioned IOPS storage, you are charged for the provisioned resources
whether or not you use them in a given month.

For more information about pricing, see [Amazon RDS pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

### Getting the best performance from Amazon RDS Provisioned IOPS storage

If your workload is I/O constrained, using Provisioned IOPS storage can increase
the number of I/O requests that the system can process concurrently. Increased
concurrency allows for decreased latency because I/O requests spend less time in a
queue. Decreased latency allows for faster database commits, which improves response
time and allows for higher database throughput.

Provisioned IOPS storage provides a way to reserve I/O capacity by specifying
IOPS. However, as with any other system capacity attribute, its maximum throughput
under load is constrained by the resource that is consumed first. That resource
might be network bandwidth, CPU, memory, or database internal resources.

## General Purpose SSD storage

General Purpose storage offers cost-effective storage that is acceptable for most
database workloads that aren't latency or performance sensitive.

###### Note

DB instances that use General Purpose storage can experience much longer latency
than instances that use Provisioned IOPS storage. If you need a DB instance with
minimum latency after these operations, we recommend using [Provisioned IOPS SSD storage](#USER_PIOPS "#USER_PIOPS").

Amazon RDS offers two types of General Purpose storage: [gp3 storage (recommended)](#gp3-storage "#gp3-storage") and [gp2 storage (previous generation)](#gp2-storage "#gp2-storage").

### gp3 storage (recommended)

By using General Purpose gp3 storage volumes, you can customize storage
performance independently of storage capacity. _Storage
performance_ is the combination of I/O operations per second (IOPS)
and how fast the storage volume can perform reads and writes (storage throughput).
On gp3 storage volumes, Amazon RDS provides a baseline storage performance of 3000 IOPS
and 125 MiB/s.

For every RDS DB engine except RDS for SQL Server, when the storage size for gp3 volumes
reaches a certain threshold, the baseline storage performance increases. This is
because of _volume striping_, where the storage uses four volumes
instead of one. RDS for SQL Server doesn't support volume striping, and therefore doesn't have
a threshold value. For striped volumes, Amazon RDS provides a baseline storage
performance of 12,000 IOPS and 500 MiB/s.

Storage performance for gp3 volumes on Amazon RDS DB engines, including the threshold
per storage volume, is shown in the following table. In RDS for Oracle and SQL Server,
you can attach up to three additional storage volumes in addition to the primary
storage volume. You can provision up to 256 TiB storage size in total with three gp3
additional storage volumes in RDS for Oracle. You can provision up to 64 TiB storage
size in total with three gp3 additional storage volumes in RDS for SQL Server because
each gp3 storage volume can be sized up to 16 TiB. With additional storage volumes, you
can have higher provisioned IOPS and maximum throughput for your DB instance. However, your DB instance
might not be able to fully utilize the provisioned IOPS and maximum throughput if your
instance class has lower limits than the values you've provisioned for your storage volumes.
For more information, see [Factors that affect database performance](#CHAP_Storage.Other.Factors "#CHAP_Storage.Other.Factors").

| DB engine                           | Storage size   | Baseline storage performance | Range of Provisioned IOPS | Range of provisioned storage throughput |
| ----------------------------------- | -------------- | ---------------------------- | ------------------------- | --------------------------------------- |
| Db2, MariaDB, MySQL, and PostgreSQL | 20–399 GiB     | 3,000 IOPS/125 MiB/s         | N/A                       | N/A                                     |
| Db2, MariaDB, MySQL, and PostgreSQL | 400–65,536 GiB | 12,000 IOPS/500 MiB/s        | 12,000–64,000 IOPS        | 500–4,000 MiB/s                         |
| Oracle                              | 20–199 GiB     | 3,000 IOPS/125 MiB/s         | N/A                       | N/A                                     |
| Oracle                              | 200–65,536 GiB | 12,000 IOPS/500 MiB/s        | 12,000–64,000 IOPS        | 500–4,000 MiB/s                         |
| SQL Server                          | 20–16,384 GiB  | 3,000 IOPS/125 MiB/s         | 3,000–16,000 IOPS         | 125–1,000 MiB/s                         |

For every DB engine except RDS for SQL Server, you can provision additional IOPS and storage
throughput when storage size is at or above the threshold value. For RDS for SQL Server, you
can provision additional IOPS and storage throughput for any available storage size.
For all DB engines, you pay for only the additional provisioned storage performance.
For more information, see [Amazon RDS
pricing](https://aws.amazon.com/rds/pricing/ "https://aws.amazon.com/rds/pricing/").

Although the added Provisioned IOPS and storage throughput aren't dependent on the
storage size, they are related to each other. When you raise the IOPS above 32,000
for MariaDB and MySQL, the storage throughput value automatically increases from 500
MiBps. For example, when you set the IOPS to 40,000 on RDS for MySQL, the storage
throughput must be at least 625 MiBps. The automatic increase doesn't happen for
Db2, Oracle, PostgreSQL, and SQL Server DB instances.

For Multi-AZ DB clusters, Amazon RDS automatically sets the throughput value based on the IOPS that
you provision. You can't modify the throughput value.

Storage performance values for gp3 volumes on RDS have the following
constraints:

- The maximum ratio of storage throughput to IOPS is 0.25 for all supported
  DB engines.
- The minimum ratio of IOPS to allocated storage (in GiB) is 0.5 on RDS for SQL Server.
  There is no minimum ratio for the other supported DB engines.
- The maximum ratio of IOPS to allocated storage is 500 for all supported DB
  engines.
- If you're using storage autoscaling, the same ratios between IOPS and
  maximum storage threshold (in GiB) also apply.

For more information on storage autoscaling, see [Managing capacity automatically with Amazon RDS storage autoscaling](USER_PIOPS.md "USER_PIOPS.md").

### gp2 storage (previous generation)

When your applications don't need high storage performance, you can use General
Purpose SSD gp2 storage. Baseline I/O performance for gp2 storage is 3 IOPS for each
GiB, with a minimum of 100 IOPS. This relationship means that larger volumes have
better performance. For example, baseline performance for one 100 GiB volume is 300
IOPS. Baseline performance for one 1,000 GiB volume is 3,000 IOPS.

Individual gp2 volumes below 1,000 GiB in size also have the ability to burst to
3,000 IOPS for extended periods of time. Volume I/O credit balance determines burst
performance. For a more detailed description of how baseline performance and I/O
credit balance affect performance, see the post [Understanding burst vs. baseline performance with Amazon RDS and gp2](https://aws.amazon.com/blogs/database/understanding-burst-vs-baseline-performance-with-amazon-rds-and-gp2/ "https://aws.amazon.com/blogs/database/understanding-burst-vs-baseline-performance-with-amazon-rds-and-gp2/") on the
AWS Database Blog.

Many workloads never deplete the burst balance. However, some workloads can
exhaust the 3,000 IOPS burst storage credit balance, so plan your storage capacity
to meet the needs of your workloads.

For gp2 volumes larger than 4,000 GiB, the baseline performance is greater than
the burst performance. For such volumes, burst is irrelevant because the baseline
performance is better than the 3,000 IOPS burst performance. However, for DB
instances of certain engines and sizes, storage is _striped_
across four volumes providing four times the baseline throughput, and four times the
burst IOPS of a single volume.

Storage performance for gp2 volumes of various storage sizes on Amazon RDS DB engines
is shown in the following table.

| DB engine                      | RDS storage size | Range of baseline IOPS | Range of baseline throughput | Burst IOPS |
| ------------------------------ | ---------------- | ---------------------- | ---------------------------- | ---------- |
| MariaDB, MySQL, and PostgreSQL | 5–399 GiB        | 100-1197 IOPS          | 128-250 MiB/s                | 3,000      |
| MariaDB, MySQL, and PostgreSQL | 400–1,335 GiB    | 1,200-4,005 IOPS       | 512-1,000 MiB/s              | 12,000     |
| MariaDB, MySQL, and PostgreSQL | 1,336–3,999 GiB  | 4008-11,997 IOPS       | 1,000 MiB/s                  | 12,000     |
| MariaDB, MySQL, and PostgreSQL | 4,000–65,536 GiB | 12,000-64,000 IOPS     | 1,000 MiB/s                  | N/A¹       |
| Oracle                         | 20–199 GiB       | 100-597 IOPS           | 128-250 MiB/s                | 3,000      |
| Oracle                         | 200–1,335 GiB    | 600-4,005 IOPS         | 512-1,000 MiB/s              | 12,000     |
| Oracle                         | 1,336–3,999 GiB  | 4008-11,997 IOPS       | 1,000 MiB/s                  | 12,000     |
| Oracle                         | 4,000–65,536 GiB | 12,000-64,000 IOPS     | 1,000 MiB/s                  | N/A¹       |
| SQL Server                     | 20–333 GiB       | 100-999 IOPS           | 128-250 MiB/s                | 3,000      |
| SQL Server                     | 334–999 GiB      | 1,002-2,997 IOPS       | 250 MiB/s                    | 3,000      |
| SQL Server                     | 1,000–16,384 GiB | 3,000-16,000 IOPS      | 250 MiB/s                    | N/A¹       |

¹ The baseline performance of the volume exceeds the maximum burst
performance.

## Performance characteristics of solid-state drive (SSD) storage types

The following table describes use cases and per-volume performance characteristics for
the SSD storage volumes used by Amazon RDS.

| Characteristic           | Provisioned IOPS (io2 Block Express)                                                                                                                                                                                                                                                                                                                                                                                                   | Provisioned IOPS (io1)                                                                                                | General Purpose (gp3)                                                                                                                                     | General Purpose (gp2)                                                                                                                          |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Description              | Highest performance within the RDS storage portfolio (IOPS,<br>throughput, latency)<br>Designed for latency-sensitive, transactional workloads                                                                                                                                                                                                                                                                                         | Consistent storage performance (IOPS, throughput, latency)<br>Designed for latency-sensitive, transactional workloads | Flexibility in provisioning storage, IOPS, and throughput<br>independently<br>Balances price performance for a wide variety of transactional<br>workloads | Provides burstable IOPS<br>Balances price performance for a wide variety of transactional<br>workloads                                         |
| Use cases                | Business-critical transactional workloads that require<br>sub-millisecond latency and sustained IOPS performance up to 256,000<br>IOPS                                                                                                                                                                                                                                                                                                 | Transactional workloads that require sustained IOPS performance up<br>to 256,000 IOPS                                 | Broad range of workloads running on medium-sized relational<br>databases in development/test environments                                                 | Broad range of workloads running on medium-sized relational<br>databases in development/test environments                                      |
| Latency                  | Sub-millisecond, provided consistently 99.9% of the time                                                                                                                                                                                                                                                                                                                                                                               | Single-digit millisecond, provided consistently 99.9% of the<br>time                                                  | Single-digit millisecond, provided consistently 99% of the<br>time                                                                                        | Single-digit millisecond, provided consistently 99% of the<br>time                                                                             |
| Volume size              | 100–65,536 GiB                                                                                                                                                                                                                                                                                                                                                                                                                         | 100–65,536 GiB (20–16,384 GiB on RDS for SQL Server)                                                                  | 20–65,536 GiB (16,384 GiB on RDS for SQL Server)                                                                                                          | 20–65,536 GiB (16,384 GiB on RDS for SQL Server)                                                                                               |
| Maximum IOPS             | 256,000                                                                                                                                                                                                                                                                                                                                                                                                                                | 256,000 (64,000 on RDS for SQL Server)                                                                                | 64,000 (16,000 on RDS for SQL Server)                                                                                                                     | 64,000 (16,000 on RDS for SQL Server)<br>NoteYou can't provision IOPS directly on gp2 storage. IOPS varies<br>with the allocated storage size. |
| Maximum throughput       | Scales based on Provisioned IOPS up to 4,000 MB/s<br>Throughput scales proportionally up to 0.256 MiB/s per provisioned<br>IOPS. Maximum throughput of 4,000 MiB/s can be achieved at 256,000<br>IOPS with a 16-KiB I/O size and 16,000 IOPS or higher with a 256-KiB<br>I/O size.<br>For instances not based on the AWS Nitro System, maximum<br>throughput of 2,000 MiB/s can be achieved at 128,000 IOPS with a<br>16-KiB I/O size. | Scales based on Provisioned IOPS up to 4,000 MB/s                                                                     | Provision additional throughput up to 4,000 MB/s (1000 MB/s on RDS<br>for SQL Server)                                                                     | 1000 MB/s (250 MB/s on RDS for SQL Server)                                                                                                     |
| AWS CLI and RDS API name | io2                                                                                                                                                                                                                                                                                                                                                                                                                                    | io1                                                                                                                   | gp3                                                                                                                                                       | gp2                                                                                                                                            |

### Automatic striping across SSD volumes

When you select General Purpose SSD or Provisioned IOPS SSD, depending on the
engine selected and the amount of storage requested, Amazon RDS automatically stripes
across multiple volumes to enhance performance, as shown in the following
table.

| Database engine                | Amazon RDS storage size | Number of volumes provisioned |
| ------------------------------ | ----------------------- | ----------------------------- |
| Db2                            | Less than 400 GiB       | 1                             |
| Db2                            | 400–65,536 GiB          | 4                             |
| MariaDB, MySQL, and PostgreSQL | Less than 400 GiB       | 1                             |
| MariaDB, MySQL, and PostgreSQL | 400–65,536 GiB          | 4                             |
| Oracle                         | Less than 200 GiB       | 1                             |
| Oracle                         | 200–65,536 GiB          | 4                             |
| SQL Server                     | Any                     | 1                             |

### Performance impact when you modify an SSD volume

When you modify a General Purpose SSD or Provisioned IOPS SSD volume, it goes
through a sequence of states. While the volume is in the `optimizing`
state, your volume performance is between the source and target configuration
specifications. Transitional volume performance will be no less than the lower of
the two specifications.

When you modify an instance’s storage so that it goes from one volume to four
volumes, or when you modify an instance using magnetic storage, Amazon RDS doesn't use
the Elastic Volumes feature. Instead, Amazon RDS provisions new volumes and transparently
moves the data from the old volume to the new volumes. This operation consumes a
significant amount of IOPS and throughput of both the old and new volumes. Depending
on the size of the volume and the amount of database workload present during the
modification, this operation can consume a high amount of IOPS, significantly
increase I/O latency, and take several hours to complete, while the RDS instance
remains in the `Modifying` state.

### Baseline and maximum IOPS rates for EBS-optimized instances

EBS-optimized instances have a baseline and maximum IOPS rate. The maximum IOPS rate is
enforced at the DB instance level. A set of EBS volumes that combine to have an IOPS rate that is
higher than the maximum can't exceed the instance-level threshold. For example, if the maximum
IOPS for a particular DB instance class is 40,000, and you attach four 64,000 IOPS EBS volumes, the
maximum IOPS is 40,000 rather than 256,000. For the IOPS maximum specific to each EC2 instance
type, see [Supported instance
types](../../../AWSEC2/latest/UserGuide/ebs-optimized.md#ebs-optimization-support "../../../AWSEC2/latest/UserGuide/ebs-optimized.md#ebs-optimization-support") in the _Amazon EC2 User Guide for Linux Instances_.

## Magnetic storage (legacy, not recommended)

Amazon RDS also supports magnetic storage for backward compatibility. We recommend that you
use General Purpose SSD or Provisioned IOPS SSD for any new storage needs. The following
are some limitations for magnetic storage:

- Doesn't allow you to scale storage when using the SQL Server database
  engine.
- Doesn't allow you to convert to a different storage type when using the SQL
  Server database engine.
- Doesn't support storage autoscaling.
- Doesn't support zero-ETL integrations with Amazon Redshift.
- Doesn't support elastic volumes.
- Limited to a maximum size of 3 TiB.
- Limited to a maximum of 1,000 IOPS.

## Additional storage volumes

With RDS for Oracle and RDS for SQL Server, you can attach up to three additional storage volumes to your
DB instance. Depending on your workload requirements, choose between gp3 and io2 storage for each volume.

Additional storage volumes provide the following benefits:

- Flexible storage configuration and performance optimization
  – Mix different storage types (gp3 and io2) to optimize for both cost and
  performance based on your data access patterns. Separate frequently accessed data on
  high-performance io2 storage from archival data on cost-effective gp3 storage.
- Enhanced capacity – Scale your total storage up to 256 TiB per DB instance by combining primary and
  additional storage volumes.
- Expand and reduce storage capacity as needed
  – Create a volume when you need additional storage, as during data migration,
  and then later delete the volume. In this way, you can expand and reduce the total
  DB instance storage.
- Online data movement – Use the built-in capabilities of Oracle Database to move data between volumes
  without downtime.

###### Note

You can remove additional storage volumes but you can't remove the primary volume.

The additional volumes must use the volume names shown in the following table.

| RDS for Oracle volume name | RDS for SQL Server volume name |
| -------------------------- | ------------------------------ |
| `rdsdbdata2`               | `H:`                           |
| `rdsdbdata3`               | `I:`                           |
| `rdsdbdata4`               | `J:`                           |

For more information about working with additional storage volumes, see the following
sections:

- [Working with storage for Amazon RDS DB instances](USER_PIOPS.md "USER_PIOPS.md")
- [Working with storage in RDS for Oracle](User_Oracle_AdditionalStorage.md "User_Oracle_AdditionalStorage.md")
- [Working with storage in RDS for SQL Server](Appendix.SQLServer.CommonDBATasks.md "Appendix.SQLServer.CommonDBATasks.md")

## Dedicated log volume (DLV)

You can use a dedicated log volume (DLV) for a DB instance that uses Provisioned IOPS
(PIOPS) storage by using the Amazon RDS console, AWS CLI, or Amazon RDS API. A DLV moves PostgreSQL
database transaction logs and MySQL/MariaDB redo logs and binary logs to a storage
volume that's separate from the volume containing the database tables. A DLV makes
transaction write logging more efficient and consistent. DLVs are ideal for databases
with large allocated storage, high I/O per second (IOPS) requirements, or
latency-sensitive workloads.

DLVs are supported for PIOPS storage (io1 and io2 Block Express), and are created with
a fixed size of 1,024 GiB and 3,000 Provisioned IOPS.

###### Note

DLVs aren't supported for General Purpose storage (gp2 and gp3).

Amazon RDS supports DLVs in all AWS Regions for the following versions:

- MariaDB 10.6.7 and higher 10 versions
- MySQL 8.0.28 and higher 8.0 versions, MySQL 8.4.3 and higher 8.4
  versions
- PostgreSQL 13.10 and higher 13 versions, 14.7 and higher 14 versions, 15.2 and
  higher 15 versions, and 16.1 and higher 16 versions

RDS supports DLVs with Multi-AZ deployments. When you modify or create a Multi-AZ
instance, A DLV is created for both the primary and the secondary.

RDS supports DLVs with read replicas. If the primary DB instance has a DLV enabled,
all read replicas created after enabling DLV will also have a DLV. Any read replicas
created before the switch to DLV will not have it enabled unless explicitly modified to
do so. We recommend all read replicas attached to a primary instance before DLV was
enabled also be manually modified to have A DLV.

After you modify the DLV setting for a DB instance, the DB instance must be
rebooted.

For information on enabling a DLV, see [Using a dedicated log volume (DLV)](USER_PIOPS.md "USER_PIOPS.md").

## Monitoring database performance

Amazon RDS provides several metrics that you can use to determine how your DB instance is
performing. You can view the metrics on the summary page for your instance in Amazon RDS
Management Console. You can also use Amazon CloudWatch to monitor these metrics. For more
information, see [Viewing metrics in the Amazon RDS console](USER_Monitoring.md "USER_Monitoring.md").
Enhanced Monitoring provides more detailed I/O metrics; for more information, see [Monitoring OS metrics with Enhanced Monitoring](USER_Monitoring.md "USER_Monitoring.md").

The following metrics are useful for monitoring performance for your DB
instance:

- `DiskQueueDepth` – The number of I/O requests in
  the queue waiting to be serviced. These are I/O requests that have been
  submitted by the application but have not been sent to the device because the
  device is busy servicing other I/O requests. Time spent waiting in the queue is
  a component of latency and service time (not available as a metric). This metric
  is reported as the average queue depth for a given time interval. Amazon RDS reports
  queue depth at 1-minute intervals. Typical values for queue depth range from
  zero to several hundred.
- `EBSByteBalance%` – The percentage of throughput credits
  remaining in the burst bucket of your RDS database. This metric is available for
  basic monitoring only. The metric value is based on the throughput of all
  volumes, including the root volume, rather than on only those volumes containing
  database files.

When this metric approaches zero, it means that your DB instance is running out of
computing capacity. If this happens regularly, consider upgrading to a larger
instance class size, for example from db.r6g.large to db.r6g.xlarge. For more
information, see [DB instance class](#other-factors-instance "#other-factors-instance").

- `ReadIOPS` and `WriteIOPS` – The
  number of I/O operations completed each second. This metric is reported as the
  average IOPS for a given time interval. Amazon RDS reports read and write IOPS
  separately at 1-minute intervals. `TotalIOPS` is the sum of the read
  and write IOPS. Typical values for IOPS range from zero to tens of thousands per
  second.

If your `TotalIOPS` values regularly approach the Provisioned IOPS
value that you have set for your DB instance, then consider increasing the
Provisioned IOPS (io1, io2 Block Express, and gp3 storage types).

Measured IOPS values are independent of the size of the individual I/O
operation. This means that when you measure I/O performance, make sure to look
at the throughput of the instance, not simply the number of I/O
operations.

- `ReadLatency` and `WriteLatency`
  – The elapsed time between the submission of an I/O request and its
  completion. This metric is reported as the average latency for a given time
  interval. Amazon RDS reports read and write latency separately at 1-minute intervals.
  Typical values for latency are in milliseconds (ms).
- `ReadThroughput` and `WriteThroughput` – The number of bytes each second that are
  transferred to or from disk. This metric is reported as the average throughput
  for a given time interval. Amazon RDS reports read and write throughput separately at
  1-minute intervals using units of bytes per second (B/s). Typical values for
  throughput range from zero to the I/O channel's maximum bandwidth.

If your throughput values regularly approach the maximum throughput for your
DB instance, then consider provisioning more storage throughput if you're using
the gp3 storage type.

## Factors that affect database performance

System activities, database workload, and DB instance class can affect database
performance.

###### Topics

- [System activities](#other-factors-system "#other-factors-system")
- [Database workload](#other-factors-workload "#other-factors-workload")
- [DB instance class](#other-factors-instance "#other-factors-instance")

### System activities

The following system-related activities consume I/O capacity and might reduce DB
instance performance while in progress:

- Multi-AZ standby creation
- Read replica creation
- Changing storage types

### Database workload

In some cases, your database or application design results in concurrency issues,
locking, or other forms of database contention. In these cases, you might not be
able to use all the provisioned bandwidth directly. In addition, you might encounter
the following workload-related situations:

- The throughput limit of the underlying instance type is reached.
- Queue depth is consistently less than 1 because your application isn't
  driving enough I/O operations.
- You experience query contention in the database even though some I/O
  capacity is unused.

In some cases, there isn't a system resource that is at or near a limit, and
adding threads doesn't increase the database transaction rate. In such cases, the
bottleneck is most likely contention in the database. The most common forms are row
lock and index page lock contention, but there are many other possibilities. If this
is your situation, seek the advice of a database performance tuning expert.

### DB instance class

To get the most performance out of your Amazon RDS DB instance, choose a current
generation instance type with enough bandwidth and IOPS to support your storage type.
For example, you can choose Amazon EBS–optimized instances and instances with
10-gigabit network connectivity.

###### Important

Depending on the instance class you're using, you might see lower bandwidth,
throughput and IOPS performance than the maximum that you can provision with RDS.
For specific information on bandwidth, throughput and IOPS performance for DB instance
classes, see [Amazon
EBS–optimized instances](../../../AWSEC2/latest/UserGuide/ebs-optimized.md "../../../AWSEC2/latest/UserGuide/ebs-optimized.md") in the _Amazon EC2 User
Guide_. We recommend that you determine the maximum bandwidth,
throughput and IOPS for the instance class before setting a Provisioned IOPS and
throughput value for your storage volumes in your DB instance.

We encourage you to use the latest generation of instances to get the best
performance. Previous generation DB instances can also have lower maximum
storage.

Some older 32-bit file systems might have lower storage capacities. To determine
the storage capacity of your DB instance, you can use the [describe-valid-db-instance-modifications](../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md "../../../cli/latest/reference/rds/describe-valid-db-instance-modifications.md") AWS CLI command.

The following list shows the maximum storage that most DB instance classes can
scale to for each database engine:

- Db2 – 64 TiB
- MariaDB – 64 TiB
- Microsoft SQL Server – 64 TiB
- MySQL – 64 TiB
- Oracle – 64 TiB
- PostgreSQL – 64 TiB

The following table shows some exceptions for maximum storage (in TiB). All
RDS for Microsoft SQL Server DB instances apart from io2 Block Express storage have a maximum storage
of 16 TiB, so there are no entries for SQL Server.

| Instance class                                         | Db2 | MariaDB | MySQL | Oracle | PostgreSQL |
| ------------------------------------------------------ | --- | ------- | ----- | ------ | ---------- |
| **db.m3 –<br>standard instance classes**               |
| **db.t4g –<br>burstable-performance instance classes** |
| db.t4g.medium                                          | N/A | 16      | 16    | N/A    | 32         |
| db.t4g.small                                           | N/A | 16      | 16    | N/A    | 16         |
| db.t4g.micro                                           | N/A | 6       | 6     | N/A    | 6          |
| **db.t3 –<br>burstable-performance instance classes**  |
| db.t3.medium                                           | 32  | 16      | 16    | 32     | 32         |
| db.t3.small                                            | 32  | 16      | 16    | 32     | 16         |
| db.t3.micro                                            | N/A | 6       | 6     | 32     | 6          |
| **db.t2 –<br>burstable-performance instance classes**  |

For more details about all instance classes supported, see [Previous generation DB instances](https://aws.amazon.com/rds/previous-generation/ "https://aws.amazon.com/rds/previous-generation/").
