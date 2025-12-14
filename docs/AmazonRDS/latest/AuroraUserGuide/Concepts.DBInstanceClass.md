# DB instance class types

Amazon Aurora
supports DB instance classes for the following use cases:

- [Aurora Serverless v2](#Concepts.DBInstanceClass.Types.serverless-v2 "#Concepts.DBInstanceClass.Types.serverless-v2")
- [Memory-optimized](#Concepts.DBInstanceClass.Types.memory "#Concepts.DBInstanceClass.Types.memory")
- [Burstable-performance](#Concepts.DBInstanceClass.Types.burstable "#Concepts.DBInstanceClass.Types.burstable")
- [Optimized Reads](#Concepts.DBInstanceClass.Types.optimized-reads "#Concepts.DBInstanceClass.Types.optimized-reads")
  For more information about Amazon EC2 instance types, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the Amazon EC2
  documentation.

## Aurora Serverless v2 instance class type

The following Aurora Serverless v2 type is available:

- db.serverless – A special DB instance class type
  used by Aurora Serverless v2. Aurora adjusts the compute, memory, and network resources
  dynamically as the workload changes. For usage details, see [Using Aurora Serverless v2](aurora-serverless-v2.md "aurora-serverless-v2.md").

## Memory-optimized instance class types

The memory-optimized X family supports the following instance classes:

- db.x2g – Instance classes optimized for
  memory-intensive applications and powered by AWS Graviton2 processors. These
  instance classes offer low cost per GiB of memory.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton2
processors. To do so, complete the same steps as with any other DB instance
modification.

The memory-optimized R family supports the following instance class types:

- db.r8g – Instance classes powered by AWS
  Graviton4 processors. These instance classes are ideal for running memory-intensive
  workloads. These instances offer larger instance sizes with up to
  3x more vCPUs and memory than the seventh-generation AWS Graviton3-based db.r7g
  instances. They are powered by the AWS Nitro System, a combination of dedicated
  hardware and lightweight hypervisor.
- You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton4
  processors. To do so, complete the same steps as with any other DB instance
  modification.
- db.r7g – Instance classes powered by AWS Graviton3 processors. These instance
  classes are ideal for running memory-intensive workloads.

You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton3
processors. To do so, complete the same steps as with any other DB instance modification.
They are powered by the AWS Nitro System, a combination of dedicated hardware and
lightweight hypervisor.

- db.r7i – Instance classes powered by 4th
  Generation Intel Xeon Scalable processors. These instance classes are SAP-Certified
  and are ideal for running memory-intensive workloads. You can modify a
  DB instance to use one of the DB instance classes powered by 4th Generation Intel Xeon Scalable
  processors. To do so, complete the same steps as with any other DB instance modification.
  They are powered by the AWS Nitro System, a combination of dedicated hardware and
  lightweight hypervisor.
- db.r6g – Instance classes powered by AWS
  Graviton2 processors. These instance classes are ideal for running memory-intensive
  workloads. They are powered by the AWS Nitro System, a combination of
  dedicated hardware and lightweight hypervisor.
- You can modify a DB instance to use one of the DB instance classes powered by AWS Graviton2
  processors. To do so, complete the same steps as with any other DB instance
  modification.
- db.r6i – Instance classes powered by 3rd
  Generation Intel Xeon Scalable processors. These instance classes are SAP-Certified
  and are an ideal fit for memory-intensive workloads.
- db.r5 – Instance classes optimized for
  memory-intensive applications. These instance classes offer improved networking
  and Amazon Elastic Block Store (Amazon EBS) performance. They are
  powered by the AWS Nitro System, a combination of dedicated hardware and
  lightweight hypervisor.
- db.r4 – These instance classes are supported only for Aurora MySQL 2.x and Aurora PostgreSQL 11 and 12
  versions. For all Aurora DB clusters that use db.r4 DB instance classes, we recommend that you upgrade to a higher generation instance class as soon as
  possible.

The db.r4 instance classes aren't available for the Aurora I/O-Optimized cluster storage configuration.

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
  We recommend using these instance classes only for
  development and test servers, or other non-production servers.
- db.t2 – Instance classes that provide a
  baseline performance level, with the ability to burst to full CPU usage. The db.t2
  instances are configured for Unlimited mode. We recommend using these instance classes
  only for development and test servers, or other non-production servers.

The db.t2 instance classes aren't available for the Aurora I/O-Optimized cluster storage configuration.

###### Note

We recommend using the T DB instance classes only for development, test,
or other nonproduction servers. For more detailed recommendations for the T instance
classes, see [Using T instance classes for development and testing](AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium "AuroraMySQL.BestPractices.md#AuroraMySQL.BestPractices.T2Medium").

For DB instance class hardware specifications, see [Hardware specifications for DB instance
classes for Aurora](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

## Optimized Reads instance class types

The following Optimized Reads instance class types are available:

- db.r8gd – Instance classes powered by Graviton4 processors. These instance classes are ideal
  for running memory-intensive workloads and offer local NVMe-based SSD block-level storage for applications that need high-speed,
  low latency local storage. They offer a maximum memory of 1.5 TiB and up to 11.4 TB of direct-attached NVMe-based SSD storage.
- db.r6gd – Instance classes powered by AWS Graviton2 processors. These instance
  classes are ideal for running memory-intensive workloads and offer local NVMe-based SSD block-level storage for applications that need high-speed, low latency local storage.
- db.r6id – Instance classes powered by 3rd Generation Intel Xeon Scalable processors. These instance classes are SAP-Certified and
  are an ideal fit for memory-intensive workloads. They offer a maximum memory of 1 TiB and up to 7.6 TB of direct-attached NVMe-based SSD storage.
