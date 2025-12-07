# DB instance class types

Amazon RDS
supports DB instance classes for the following use cases:

- [General-purpose](#Concepts.DBInstanceClass.Types.general-purpose "#Concepts.DBInstanceClass.Types.general-purpose")
- [Memory-optimized](#Concepts.DBInstanceClass.Types.memory "#Concepts.DBInstanceClass.Types.memory")
- [Compute-optimized](#Concepts.DBInstanceClass.Types.compute "#Concepts.DBInstanceClass.Types.compute")
- [Burstable-performance](#Concepts.DBInstanceClass.Types.burstable "#Concepts.DBInstanceClass.Types.burstable")
- [Optimized Reads](#Concepts.DBInstanceClass.Types.optimized-reads "#Concepts.DBInstanceClass.Types.optimized-reads")
  For more information about Amazon EC2 instance types, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the Amazon EC2
  documentation.

## General-purpose instance class types

The following general-purpose DB instance classes are available:

- db.m8g – General-purpose DB instance classes
  powered by AWS Graviton4 processors. These instance classes deliver balanced
  compute, memory, and networking for a broad range of general-purpose workloads.
  Compared to seventh-generation AWS Graviton3-based M7g instances, these new
  classes offer larger instance sizes with up to 3x more vCPUs and memory. They are
  powered by the AWS Nitro System, a combination of dedicated hardware and
  lightweight hypervisor.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton4
processors. To do so, complete the same steps as with any other DB instance
modification.

- db.m7i – General-purpose DB instance classes
  powered by 4th Generation Intel Xeon Scalable processors. The db.m7i instances are
  SAP certified and ideal for supporting enterprise applications that need larger
  instance sizes or high continuous CPU usage. These instance classes deliver balanced
  compute, memory, and networking for a broad range of general-purpose workloads. This
  instance class type delivers up to 40,000 Mbps EBS bandwidth and up to 50 Gbps
  network bandwidth. The db.m7i instances deliver up to 15% better price performance
  compared to db.m6i instances. They are powered by the AWS Nitro System, a
  combination of dedicated hardware and lightweight hypervisor.
- db.m7g – General-purpose DB instance classes
  powered by AWS Graviton3 processors. These instance classes deliver balanced
  compute, memory, and networking for a broad range of general-purpose workloads. They
  are powered by the AWS Nitro System, a combination of dedicated hardware and
  lightweight hypervisor.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton3
processors. To do so, complete the same steps as with any other DB instance
modification.

- db.m6g – General-purpose DB instance classes
  powered by AWS Graviton2 processors. These instances deliver balanced compute,
  memory, and networking for a broad range of general-purpose workloads. The db.m6gd
  instance classes have local NVMe-based SSD block-level storage for applications
  that need high-speed, low latency local storage.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton2
processors. To do so, complete the same steps as with any other DB instance
modification.

- db.m6i – General-purpose DB instance classes
  powered by 3rd Generation Intel Xeon Scalable processors. These instances are SAP
  Certified and ideal for workloads such as backend servers supporting enterprise
  applications, gaming servers, caching fleets, and application development
  environments. The db.m6id and db.m6idn instance classes offer up to 7.6 TB of local
  NVMe-based SSD storage, whereas db.m6in offers EBS-only storage. The db.m6in and
  db.m6idn classes offer up to 200 Gbps of network bandwidth. They are powered by the
  AWS Nitro System, a combination of dedicated hardware and lightweight
  hypervisor.
- db.m5 –General-purpose DB instance classes that
  provide a balance of compute, memory, and network resources, and are a good choice
  for many applications. The db.m5d instance class offers NVMe-based SSD storage that is
  physically connected to the host server. The db.m5 instance classes provide more
  computing capacity than the previous db.m4 instance classes. They are powered by the
  AWS Nitro System, a combination of dedicated hardware and lightweight
  hypervisor.
- db.m4 – General-purpose DB instance classes that
  provide more computing capacity than the previous db.m3 instance classes.

For the RDS for Oracle DB engines, Amazon RDS no longer supports db.m4
DB instance classes. If you had previously created RDS for Oracle db.m4 DB instances, Amazon RDS
automatically upgrades those DB instances to equivalent db.m5 DB instance classes.

For the RDS for MariaDB, RDS for MySQL, RDS for SQL Server, and RDS for PostgreSQL DB engines, Amazon RDS has
started the end-of-support process for this DB instance class using the following schedule. For
all RDS DB instances that use this instance class, we recommend that you upgrade to a newer
generation DB instance class as soon as possible.

| Action or recommendation                                                                                                                                                                                                  | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Starting on this date, Amazon RDS began automatically upgrading<br>instances using db.m4 to the newer generation db.m5 instance<br>class. Creating DB instances using the db.m4 instance class is no<br>longer supported. | June 1, 2024      |
| Amazon RDS ends support for db.m4.                                                                                                                                                                                        | December 31, 2024 |

- db.m3 – General-purpose DB instance classes that
  provide more computing capacity than the previous db.m1 instance classes.

For the RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL DB engines, Amazon RDS has started
the end-of-life process for db.m3 DB instance classes using the following schedule, which
includes upgrade recommendations. For all RDS DB instances that use db.m3 DB instance
classes, we recommend that you upgrade to a higher generation DB instance class as soon as
possible.

| Action or recommendation                                                                                                                 | Dates            |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You can no longer create RDS DB instances that use db.m3 DB instance classes.                                                            | Now              |
| Amazon RDS started automatic upgrades of RDS DB instances that use db.m3<br>DB instance classes to equivalent db.m5 DB instance classes. | February 1, 2023 |

## Memory-optimized instance class types

The memory-optimized Z family supports the following instance
classes:

- db.z1d – Instance classes optimized for
  memory-intensive applications. These instance classes offer both high compute
  capacity and a high memory footprint. High frequency z1d instances deliver a
  sustained all-core frequency of up to 4.0 GHz.

The memory-optimized X family supports the following instance classes:

- db.x2g – Instance classes optimized for
  memory-intensive applications and powered by AWS Graviton2 processors. These
  instance classes offer low cost per GiB of memory.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton2
processors. To do so, complete the same steps as with any other DB instance
modification.

- db.x2i – Instance classes optimized for
  memory-intensive applications. The **db.x2iedn** and
  **db.x2idn** instance class types are powered by
  third-generation Intel Xeon Scalable processors (Ice Lake). They include up to 3.8
  TB of local NVMe SSD storage, up to 100 Gbps of networking bandwidth, and up to 4
  TiB (db.x2iden) or 2 TiB (db.x2idn) of memory. The **db.x2iezn**
  type is powered by second-generation Intel Xeon Scalable processors (Cascade Lake)
  with an all-core turbo frequency of up to 4.5 GHz and up to 1.5 TiB of memory and by
  the AWS Nitro System, a combination of dedicated hardware and lightweight
  hypervisor.
- db.x1 – Instance classes optimized for
  memory-intensive applications. These instance classes offer one of the lowest price
  per GiB of RAM among the DB instance classes and up to 1,952 GiB of DRAM-based instance
  memory. The **db.x1e** instance class type offers up to 3,904 GiB
  of DRAM-based instance memory.

The memory-optimized R family supports the following instance class types:

- db.r8g – Instance classes powered by AWS
  Graviton4 processors. These instance classes are ideal for running memory-intensive
  workloads in open-source databases such as MySQL
  and PostgreSQL. These instances offer larger instance sizes with up to
  3x more vCPUs and memory than the seventh-generation AWS Graviton3-based db.r7g
  instances. They are powered by the AWS Nitro System, a combination of dedicated
  hardware and lightweight hypervisor.
- You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton4
  processors. To do so, complete the same steps as with any other DB instance
  modification.
- db.r7g – Instance classes powered by AWS Graviton3 processors. These instance
  classes are ideal for running memory-intensive workloads in open-source databases such as
  MySQL and PostgreSQL.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton3
processors. To do so, complete the same steps as with any other DB instance modification.
They are powered by the AWS Nitro System, a combination of dedicated hardware and
lightweight hypervisor.

- db.r7i – Instance classes powered by 4th
  Generation Intel Xeon Scalable processors. These instance classes are SAP-Certified
  and are ideal for running memory-intensive workloads
  in open-source databases such as MySQL and PostgreSQL. You can modify a
  DB instance to use one of the DB instance classes powered by 4th Generation Intel Xeon Scalable
  processors. To do so, complete the same steps as with any other DB instance modification.
  They are powered by the AWS Nitro System, a combination of dedicated hardware and
  lightweight hypervisor.
- db.r6g – Instance classes powered by AWS
  Graviton2 processors. These instance classes are ideal for running memory-intensive
  workloads in open-source databases such as MySQL
  and PostgreSQL. The **db.r6gd** type offers local NVMe-based
  SSD block-level storage for applications that need high-speed, low latency local
  storage. They are powered by the AWS Nitro System, a combination of
  dedicated hardware and lightweight hypervisor.
- You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton2
  processors. To do so, complete the same steps as with any other DB instance
  modification.
- db.r6i – Instance classes powered by 3rd
  Generation Intel Xeon Scalable processors. These instance classes are SAP-Certified
  and are an ideal fit for memory-intensive workloads in
  open-source databases such as MySQL and PostgreSQL. The **db.r6id**,
  **db.r6in**, and **db.r6idn** instance
  classes have a memory-to-vCPU ratio of 8:1 and a maximum memory of 1 TiB. The
  db.r6id and db.r6idn classes offer up to 7.6 TB of direct-attached NVMe-based
  SSD storage, whereas db.r6in offers EBS-only storage. The db.r6idn and db.r6in
  classes offer up to 200 Gbps of network bandwidth. They are powered by the AWS
  Nitro System, a combination of dedicated hardware and lightweight
  hypervisor.
- db.r5b – Instance classes that are
  memory-optimized for throughput-intensive applications. Powered by the AWS Nitro
  System, db.r5b instances deliver up to 60 Gbps bandwidth and 260,000 IOPS of EBS
  performance. This is the fastest block storage performance on EC2.
- db.r5d – Instance classes that are optimized
  for low latency, very high random I/O performance, and high sequential read
  throughput.
- db.r5 – Instance classes optimized for
  memory-intensive applications. These instance classes offer improved networking
  performance. They are
  powered by the AWS Nitro System, a combination of dedicated hardware and
  lightweight hypervisor.
- db.r4 – Instance classes that provide
  improved networking over previous db.r3 instance classes.

For the RDS for Oracle DB engines, Amazon RDS has started the
end-of-life process for db.r4 DB instance classes using the following schedule,
which includes upgrade recommendations. For RDS for Oracle DB instances that use db.r4
instance classes, we recommend that you upgrade to a higher generation instance class as soon as
possible.

| Action or recommendation                                                                                                                            | Dates          |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| You can no longer create RDS for Oracle DB instances that use db.r4<br>DB instance classes.                                                         | Now            |
| Amazon RDS started automatic upgrades of RDS for Oracle DB instances that use<br>db.r4 DB instance classes to equivalent db.r5 DB instance classes. | April 17, 2023 |

For the RDS for MariaDB, RDS for MySQL, RDS for SQL Server, and RDS for PostgreSQL DB engines, Amazon RDS has
started the end-of-support process for this DB instance class using the following schedule. For
all RDS DB instances that use this instance class, we recommend that you upgrade to a newer
generation DB instance class as soon as possible.

| Action or recommendation                                                                                                                                                                                                  | Dates             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Starting on this date, Amazon RDS began automatically upgrading<br>instances using db.r4 to the newer generation db.r5 instance<br>class. Creating DB instances using the db.m4 instance class is no<br>longer supported. | June 1, 2024      |
| Amazon RDS ends support for db.r4.                                                                                                                                                                                        | December 31, 2024 |

- db.r3 – Instance classes that provide memory
  optimization.

For the RDS for MariaDB, RDS for MySQL, and RDS for PostgreSQL DB engines,
Amazon RDS has started the end-of-life process for db.r3 DB instance classes using the
following schedule, which includes upgrade recommendations. For all RDS DB instances that
use db.r3 DB instance classes, we recommend that you upgrade to a higher generation DB instance class as
soon as possible.

| Action or recommendation                                                                                                                 | Dates            |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| You can no longer create RDS DB instances that use db.r3 DB instance<br>classes.                                                         | Now              |
| Amazon RDS started automatic upgrades of RDS DB instances that use db.r3<br>DB instance classes to equivalent db.r5 DB instance classes. | February 1, 2023 |

## Compute-optimized instance class

type

The following compute-optimized instance class types are available:

- db.c6gd – Instance classes that are ideal
  for running advanced compute-intensive workloads. Powered by AWS Graviton2
  processors, these instance classes offer local NVMe-based SSD block-level storage
  for applications that need high-speed, low latency local storage.

###### Note

The c6gd instance classes are supported only for Multi-AZ DB cluster deployments. They're
the only instance class supported for Multi-AZ DB clusters that offer the `medium`
instance size. For more information, see [Multi-AZ DB cluster deployments for Amazon RDS](multi-az-db-clusters-concepts.md "multi-az-db-clusters-concepts.md").

## Burstable-performance instance

class types

The following burstable-performance DB instance class types are available:

- db.t4g – General-purpose instance classes
  powered by Arm-based AWS Graviton2 processors. These instance classes deliver
  better price performance than previous burstable-performance DB instance classes for a
  broad set of burstable general-purpose workloads. Amazon RDS db.t4g instances are
  configured for Unlimited mode. This means that they can burst beyond the baseline
  over a 24-hour window for an additional charge.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton2
processors. To do so, complete the same steps as with any other DB instance
modification.

- db.t3 – Instance classes that provide a
  baseline performance level, with the ability to burst to full CPU usage. The db.t3
  instances are configured for Unlimited mode. These instance classes provide more
  computing capacity than the previous db.t2 instance classes. They are powered by the
  AWS Nitro System, a combination of dedicated hardware and lightweight hypervisor.
- db.t2 – Instance classes that provide a
  baseline performance level, with the ability to burst to full CPU usage. The db.t2
  instances are configured for Unlimited mode. We recommend using these instance classes
  only for development and test servers, or other non-production servers.

For the RDS for MariaDB, RDS for MySQL, RDS for SQL Server, and RDS for PostgreSQL DB engines, Amazon RDS has
started the end-of-support process for this DB instance class using the following schedule. For
all RDS DB instances that use this instance class, we recommend that you upgrade to a newer
generation DB instance class as soon as possible.

| Action or recommendation                                                                                                                                                                                                  | Dates             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Starting on this date, Amazon RDS began automatically upgrading<br>instances using db.t2 to the newer generation db.t3 instance<br>class. Creating DB instances using the db.t2 instance class is no<br>longer supported. | June 1, 2024      |
| Amazon RDS ends support for db.t2.                                                                                                                                                                                        | December 31, 2024 |

###### Note

The DB instance classes that use the AWS Nitro System (db.m5, db.r5, db.t3) are throttled on combined read
plus write workload.

For DB instance class hardware specifications, see [Hardware specifications for DB instance
classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

## Optimized Reads instance class types

The following Optimized Reads instance class types are available:

- db.m8gd – Instance classes powered by AWS Graviton4 processor.
  These instance classes are ideal for general purpose workloads that need high-speed, low latency storage.
  They offer a maximum memory of 786 GiB and up to 11.4 TB of direct-attached NVMe-based SSD storage.
- db.r8gd – Instance classes powered by Graviton4 processors. These instance classes are ideal
  for running memory-intensive workloads and offer local NVMe-based SSD block-level storage for applications that need high-speed,
  low latency local storage. They offer a maximum memory of 1.5 TiB and up to 11.4 TB of direct-attached NVMe-based SSD storage.
- db.r6gd – Instance classes powered by AWS Graviton2 processors. These instance
  classes are ideal for running memory-intensive workloads and offer local NVMe-based SSD block-level storage for applications that need high-speed, low latency local storage.
- db.r6id – Instance classes powered by 3rd Generation Intel Xeon Scalable processors. These instance classes are SAP-Certified and
  are an ideal fit for memory-intensive workloads. They offer a maximum memory of 1 TiB and up to 7.6 TB of direct-attached NVMe-based SSD storage.
