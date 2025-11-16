# Hardware specifications for DB instance

classes for Aurora

In the table in this section, you can find hardware details about the Amazon RDS DB instance
classes for Aurora.

For information about Aurora DB engine support for each DB instance class, see
[Supported DB engines for DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

###### Topics

- [Hardware terminology for
  DB instance classes for Aurora](#Concepts.DBInstanceClass.hardware-terminology "#Concepts.DBInstanceClass.hardware-terminology")
- [Hardware specifications for the memory-optimized instance classes](#hw-specs-aur.mem-opt "#hw-specs-aur.mem-opt")
- [Hardware specifications for the burstable-performance instance classes](#hardware-specifications.burstable-inst-classes "#hardware-specifications.burstable-inst-classes")

## Hardware terminology for

DB instance classes for Aurora

The following terminology is used to describe hardware specifications for DB instance
classes:

**vCPU**

The number of virtual central processing units (CPUs). A _virtual CPU_ is a unit of capacity that you can
use to compare DB instance classes. Instead of purchasing or leasing a particular
processor to use for several months or years, you are renting capacity by
the hour. Our goal is to make a consistent and specific amount of CPU
capacity available, within the limits of the actual underlying
hardware.

**ECU**

The relative measure of the integer processing power of an Amazon EC2 instance.
To make it easy for developers to compare CPU capacity between different
instance classes, we have defined an Amazon EC2 Compute Unit. The amount of CPU
that is allocated to a particular instance is expressed in terms of these
EC2 Compute Units. One ECU currently provides CPU capacity equivalent to a
1.0–1.2 GHz 2007 Opteron or 2007 Xeon processor.

**Memory (GiB)**

The RAM, in gibibytes, allocated to the DB instance. There is often a consistent
ratio between memory and vCPU. As an example, take the db.r4 instance class,
which has a memory to vCPU ratio similar to the db.r5 instance class.
However, for most use cases the db.r5 instance class provides better, more
consistent performance than the db.r4 instance class.

**Max. EBS bandwidth (Mbps)**

The maximum EBS bandwidth in megabits per second. Divide by 8 to get the
expected throughput in megabytes per second.

###### Note

This figure refers to I/O bandwidth for local storage within the DB
instance. It doesn't apply to communication with the Aurora cluster
volume.

**Network bandwidth**

The network speed relative to other DB instance classes.

For information on using Amazon CloudWatch metrics to monitor your Aurora DB instance throughput, see [Evaluating DB instance usage for Aurora MySQL with Amazon CloudWatch metrics](AuroraMySQL.BestPractices.md "AuroraMySQL.BestPractices.md") and [Evaluating DB instance usage for Aurora PostgreSQL with CloudWatch
metrics](AuroraPostgreSQL_AnayzeResourceUsage.md#AuroraPostgreSQL_AnayzeResourceUsage.EvaluateInstanceUsage "AuroraPostgreSQL_AnayzeResourceUsage.md#AuroraPostgreSQL_AnayzeResourceUsage.EvaluateInstanceUsage").

## Hardware specifications for the memory-optimized instance classes

The following tables show the compute, memory, storage, and bandwidth specifications for the memory-optimized instance classes.

**db.x2g – memory-optimized instance classes with AWS Graviton2 processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x2g.16xlarge | 64   | —   | 1024         | EBS-optimized only     | 19,000                    | 25                       |
| db.x2g.12xlarge | 48   | —   | 768          | EBS-optimized only     | 14,250                    | 20                       |
| db.x2g.8xlarge  | 32   | —   | 512          | EBS-optimized only     | 9,500                     | 12                       |
| db.x2g.4xlarge  | 16   | —   | 256          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.x2g.2xlarge  | 8    | —   | 128          | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.x2g.xlarge   | 4    | —   | 64           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.x2g.large    | 2    | —   | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.r8g – memory-optimized instance classes powered by AWS Graviton4 processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r8g.48xlarge | 192  | —   | 1536         | EBS-optimized only     | 40,000                    | 50                       |
| db.r8g.24xlarge | 96   | —   | 768          | EBS-optimized only     | 30,000                    | 40                       |
| db.r8g.16xlarge | 64   | —   | 512          | EBS-optimized only     | 20,000                    | 30                       |
| db.r8g.12xlarge | 48   | —   | 384          | EBS-optimized only     | 15,000                    | 22.5                     |
| db.r8g.8xlarge  | 32   | —   | 256          | EBS-optimized only     | 10,000                    | 15                       |
| db.r8g.4xlarge  | 16   | —   | 128          | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r8g.2xlarge  | 8    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r8g.xlarge   | 4    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r8g.large    | 2    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r7i – memory-optimized instance classes powered by 4th generation Intel Xeon Scalable processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r7i.48xlarge | 192  | —   | 1536         | EBS-optimized only     | 40,000                    | 50                       |
| db.r7i.24xlarge | 96   | —   | 768          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r7i.16xlarge | 64   | —   | 512          | EBS-optimized only     | 20,000                    | 25                       |
| db.r7i.12xlarge | 48   | —   | 384          | EBS-optimized only     | 15,000                    | 18.75                    |
| db.r7i.8xlarge  | 32   | —   | 256          | EBS-optimized only     | 10,000                    | 12.5                     |
| db.r7i.4xlarge  | 16   | —   | 128          | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.2xlarge  | 8    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.xlarge   | 4    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.large    | 2    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r7g – memory-optimized instance classes with AWS Graviton3 processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r7g.16xlarge | 64   | —   | 512          | EBS-optimized only     | 20,000                    | 30                       |
| db.r7g.12xlarge | 48   | —   | 384          | EBS-optimized only     | 15,000                    | 22.5                     |
| db.r7g.8xlarge  | 32   | —   | 256          | EBS-optimized only     | 10,000                    | 15                       |
| db.r7g.4xlarge  | 16   | —   | 128          | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r7g.2xlarge  | 8    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r7g.xlarge   | 4    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7g.large    | 2    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r6id – memory-optimized instance classes with 3rd generation Intel Xeon Scalable processors and SSD
storage**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6id.32xlarge | 128  | —   | 1,024        | 4x1900 NVMe SSD        | 40,000                    | 50                       |
| db.r6id.24xlarge | 96   | —   | 768          | 4x1425 NVMe SSD        | 30,000                    | 37.5                     |

**db.r6gd – memory-optimized instance classes with AWS Graviton2 processors and SSD storage**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6gd.16xlarge | 64   | —   | 512          | 2 x 1900 NVMe SSD      | 19,000                    | 25                       |
| db.r6gd.12xlarge | 48   | —   | 384          | 2 x 1425 NVMe SSD      | 13,500                    | 20                       |
| db.r6gd.8xlarge  | 32   | —   | 256          | 1 x 1900 NVMe SSD      | 9,000                     | 12                       |
| db.r6gd.4xlarge  | 16   | —   | 128          | 1 x 950 NVMe SSD       | 4,750                     | Up to 10                 |
| db.r6gd.2xlarge  | 8    | —   | 64           | 1 x 474 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.r6gd.xlarge   | 4    | —   | 32           | 1 x 237 NVMe SSD       | Up to 4,750               | Up to 10                 |

**db.r6g – memory-optimized instance classes with AWS Graviton2 processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6g.16xlarge | 64   | —   | 512          | EBS-optimized only     | 19,000                    | 25                       |
| db.r6g.12xlarge | 48   | —   | 384          | EBS-optimized only     | 13,500                    | 20                       |
| db.r6g.8xlarge  | 32   | —   | 256          | EBS-optimized only     | 9,000                     | 12                       |
| db.r6g.4xlarge  | 16   | —   | 128          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.r6g.2xlarge  | 8    | —   | 64           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r6g.xlarge   | 4    | —   | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r6g.large    | 2    | —   | 16           | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.r6i – memory-optimized instance classes with 3rd Generation Intel Xeon Scalable processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6i.32xlarge | 128  | —   | 1,024        | EBS-optimized only     | 40,000                    | 50                       |
| db.r6i.24xlarge | 96   | —   | 768          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r6i.16xlarge | 64   | —   | 512          | EBS-optimized only     | 20,000                    | 25                       |
| db.r6i.12xlarge | 48   | —   | 384          | EBS-optimized only     | 15,000                    | 18.75                    |
| db.r6i.8xlarge  | 32   | —   | 256          | EBS-optimized only     | 10,000                    | 12.5                     |
| db.r6i.4xlarge  | 16   | —   | 128          | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r6i.2xlarge  | 8    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r6i.xlarge   | 4    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r6i.large    | 2    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r5 – memory-optimized instance classes**

| Instance class | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r5.24xlarge | 96   | 347 | 768          | EBS-optimized only     | 19,000                    | 25                       |
| db.r5.16xlarge | 64   | 264 | 512          | EBS-optimized only     | 13,600                    | 20                       |
| db.r5.12xlarge | 48   | 173 | 384          | EBS-optimized only     | 9,500                     | 12                       |
| db.r5.8xlarge  | 32   | 132 | 256          | EBS-optimized only     | 6,800                     | 10                       |
| db.r5.4xlarge  | 16   | 71  | 128          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.r5.2xlarge  | 8    | 38  | 64           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r5.xlarge   | 4    | 19  | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r5.large    | 2    | 10  | 16           | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.r4 – memory-optimized instance classes with Intel Xeon Scalable processors**

| Instance class | vCPU | ECU  | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | ---- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r4.16xlarge | 64   | 195  | 488          | EBS-optimized only     | 14,000                    | 25                       |
| db.r4.8xlarge  | 32   | 99   | 244          | EBS-optimized only     | 7,000                     | 10                       |
| db.r4.4xlarge  | 16   | 53   | 122          | EBS-optimized only     | 3,500                     | Up to 10                 |
| db.r4.2xlarge  | 8    | 27   | 61           | EBS-optimized only     | 1,700                     | Up to 10                 |
| db.r4.xlarge   | 4    | 13.5 | 30.5         | EBS-optimized only     | 850                       | Up to 10                 |
| db.r4.large    | 2    | 7    | 15.25        | EBS-optimized only     | 425                       | Up to 10                 |

## Hardware specifications for the burstable-performance instance classes

The following tables show the compute, memory, storage, and bandwidth specifications for the burstable-performance instance classes.

**db.t4g – burstable-performance instance classes powered by AWS Graviton2 processors**

| Instance class | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.t4g.large   | 2    | —   | 8            | EBS-optimized only     | Up to 2,780               | Up to 5                  |
| db.t4g.medium  | 2    | —   | 4            | EBS-optimized only     | Up to 2,085               | Up to 5                  |

**db.t3 – burstable-performance instance classes**

| Instance class | vCPU | ECU      | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | -------- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.t3.large    | 2    | Variable | 8            | EBS-optimized only     | Up to 2,048               | Up to 5                  |
| db.t3.medium   | 2    | Variable | 4            | EBS-optimized only     | Up to 1,536               | Up to 5                  |
| db.t3.small    | 2    | Variable | 2            | EBS-optimized only     | Up to 1,536               | Up to 5                  |

**db.t2 – burstable-performance instance classes**

| Instance class | vCPU | ECU      | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | -------- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.t2.medium   | 2    | Variable | 4            | EBS only               | —                         | Moderate                 |
| db.t2.small    | 1    | Variable | 2            | EBS only               | —                         | Low                      |
