# Hardware specifications for DB instance

classes

In the tables in this section, you can find hardware details about the Amazon RDS DB instance
classes.

For information about Amazon RDS DB engine support for each DB instance class,
see [Supported DB engines for DB instance classes](Concepts.DBInstanceClass.md "Concepts.DBInstanceClass.md").

###### Topics

- [Hardware terminology for
  DB instance classes](#Concepts.DBInstanceClass.hardware-terminology "#Concepts.DBInstanceClass.hardware-terminology")
- [Hardware specifications
  for the general-purpose instance classes](#hardware-specifications.gen-purpose-inst-classes "#hardware-specifications.gen-purpose-inst-classes")
- [Hardware
  specifications for the memory-optimized instance classes](#hardware-specifications.mem-opt-inst-classes "#hardware-specifications.mem-opt-inst-classes")
- [Hardware specifications
  for the compute-optimized instance classes](#hardware-specifications.compute-opt-inst-classes "#hardware-specifications.compute-opt-inst-classes")
- [Hardware specifications for
  the burstable-performance instance classes](#hardware-specifications.burstable-inst-classes "#hardware-specifications.burstable-inst-classes")

## Hardware terminology for

DB instance classes

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

**EBS-optimized**

The DB instance uses an optimized configuration stack and provides additional,
dedicated capacity for I/O. This optimization provides the best performance
by minimizing contention between I/O and other traffic from your instance.
For more information about Amazon EBS–optimized instances, see [Amazon EBS–Optimized
instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the _Amazon EC2 User Guide._

EBS-optimized instances have a baseline and maximum IOPS rate. The maximum IOPS rate is
enforced at the DB instance level. A set of EBS volumes that combine to have an IOPS rate that is
higher than the maximum can't exceed the instance-level threshold. For example, if the maximum
IOPS for a particular DB instance class is 40,000, and you attach four 64,000 IOPS EBS volumes, the
maximum IOPS is 40,000 rather than 256,000. For the IOPS maximum specific to each EC2 instance
type, see [Supported instance
types](../../../AWSEC2/latest/UserGuide/ebs-optimized.md#ebs-optimization-support "../../../AWSEC2/latest/UserGuide/ebs-optimized.md#ebs-optimization-support") in the _Amazon EC2 User Guide for Linux Instances_.

**Max. EBS bandwidth (Mbps)**

The maximum EBS bandwidth in megabits per second. Divide by 8 to get the
expected throughput in megabytes per second.

###### Important

General Purpose SSD (gp2) volumes for Amazon RDS DB instances have a throughput
limit of 250 MiB/s in most cases. However, the throughput limit can vary
depending on volume size. For more information, see [Amazon EBS volume
types](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md") in the _Amazon EC2 User Guide._

**Network bandwidth**

The network speed relative to other DB instance classes.

## Hardware specifications

for the general-purpose instance classes

The following tables show the compute, memory, storage, and bandwidth specifications for
the general-purpose instance classes.

**db.m8g – general-purpose instance classes powered by AWS
Graviton4 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m8g.48xlarge  | 192  | —   | 768          | EBS-optimized only     | 40,000                    | 50                       |
| db.m8g.24xlarge  | 96   | —   | 512          | EBS-optimized only     | 30,000                    | 40                       |
| db.m8g.16xlarge  | 64   | —   | 384          | EBS-optimized only     | 20,000                    | 30                       |
| db.m8g.12xlarge  | 48   | —   | 256          | EBS-optimized only     | 15,000                    | 22.5                     |
| db.m8g.8xlarge   | 32   | —   | 128          | EBS-optimized only     | 10,000                    | 15                       |
| db.m8g.4xlarge\* | 16   | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.m8g.2xlarge\* | 8    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.m8g.xlarge\*  | 4    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m8g.large\*   | 2    | —   | 8            | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.m7i – general-purpose instance classes powered by 4th
generation Intel Xeon Scalable processors**

| Instance class    | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m7i.metal-48xl | 192  | 96              | 2       | —   | 768          | EBS-optimized only     | 40,000                    | 50                       |
| db.m7i.metal-24xl | 96   | 48              | 1       | —   | 384          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.m7i.48xlarge   | 192  | —               | —       | —   | 768          | EBS-optimized only     | 40,000                    | 50                       |
| db.m7i.24xlarge   | 96   | —               | —       | —   | 384          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.m7i.16xlarge   | 64   | —               | —       | —   | 256          | EBS-optimized only     | 20,000                    | 25                       |
| db.m7i.12xlarge   | 48   | —               | —       | —   | 192          | EBS-optimized only     | 15,000                    | 18.75                    |
| db.m7i.8xlarge    | 32   | —               | —       | —   | 128          | EBS-optimized only     | 10,000                    | 12.5                     |
| db.m7i.4xlarge    | 16   | —               | —       | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m7i.2xlarge    | 8    | —               | —       | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m7i.xlarge     | 4    | —               | —       | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m7i.large      | 2    | —               | —       | —   | 8            | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.m7g – general-purpose instance classes powered by AWS
Graviton3 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m7g.16xlarge  | 64   | —   | 256          | EBS-optimized only     | 20,000                    | 30                       |
| db.m7g.12xlarge  | 48   | —   | 192          | EBS-optimized only     | 15,000                    | 22.5                     |
| db.m7g.8xlarge   | 32   | —   | 128          | EBS-optimized only     | 10,000                    | 15                       |
| db.m7g.4xlarge   | 16   | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.m7g.2xlarge\* | 8    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.m7g.xlarge\*  | 4    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m7g.large\*   | 2    | —   | 8            | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.m6g – general-purpose instance classes powered by AWS
Graviton2 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m6g.16xlarge  | 64   | —   | 256          | EBS-optimized only     | 19,000                    | 25                       |
| db.m6g.12xlarge  | 48   | —   | 192          | EBS-optimized only     | 13,500                    | 20                       |
| db.m6g.8xlarge   | 32   | —   | 128          | EBS-optimized only     | 9,000                     | 12                       |
| db.m6g.4xlarge   | 16   | —   | 64           | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.m6g.2xlarge\* | 8    | —   | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.m6g.xlarge\*  | 4    | —   | 16           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.m6g.large\*   | 2    | —   | 8            | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.m6gd – general-purpose instance classes powered by AWS
Graviton2 processors and SSD storage**

| Instance class    | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m6gd.16xlarge  | 64   | —   | 256          | 2 x 1900 NVMe SSD      | 19,000                    | 25                       |
| db.m6gd.12xlarge  | 48   | —   | 192          | 2 x 1425 NVMe SSD      | 13,500                    | 20                       |
| db.m6gd.8xlarge   | 32   | —   | 128          | 1 x 1900 NVMe SSD      | 9,000                     | 12                       |
| db.m6gd.4xlarge\* | 16   | —   | 64           | 1 x 950 NVMe SSD       | 4,750                     | Up to 10                 |
| db.m6gd.2xlarge\* | 8    | —   | 32           | 1 x 474 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.m6gd.xlarge\*  | 4    | —   | 16           | 1 x 237 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.m6gd.large\*   | 2    | —   | 8            | 1 x 118 NVMe SSD       | Up to 4,750               | Up to 10                 |

**db.m6id – general-purpose instance classes powered by 3rd
generation Intel Xeon Scalable processors and SSD storage**

| Instance class    | vCPU | Physical cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | -------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m6id.metal     | 128  | 64             | 2       | —   | 512          | 4 x 1900 NVMe SSD      | 40,000                    | 50                       |
| db.m6id.32xlarge  | 128  | —              | —       | —   | 512          | 4 x 1900 NVMe SSD      | 40,000                    | 50                       |
| db.m6id.24xlarge  | 96   | —              | —       | —   | 384          | 4 x 1425 NVMe SSD      | 30,000                    | 37.5                     |
| db.m6id.16xlarge  | 64   | —              | —       | —   | 256          | 2 x 1900 NVMe SSD      | 20,000                    | 25                       |
| db.m6id.12xlarge  | 48   | —              | —       | —   | 192          | 2 x 1425 NVMe SSD      | 15,000                    | 18.75                    |
| db.m6id.8xlarge   | 32   | —              | —       | —   | 128          | 1 x 1900 NVMe SSD      | 10,000                    | 12.5                     |
| db.m6id.4xlarge\* | 16   | —              | —       | —   | 64           | 1 x 950 NVMe SSD       | Up to 10,000              | Up to 12.5               |
| db.m6id.2xlarge\* | 8    | —              | —       | —   | 32           | 1 x 474 NVMe SSD       | Up to 10,000              | Up to 12.5               |
| db.m6id.xlarge\*  | 4    | —              | —       | —   | 16           | 1 x 237 NVMe SSD       | Up to 10,000              | Up to 12.5               |
| db.m6id.large\*   | 2    | —              | —       | —   | 8            | 1 x 118 NVMe SSD       | Up to 10,000              | Up to 12.5               |

**db.m6idn – general-purpose instance classes with 3rd
Generation Intel Xeon Scalable processors, SSD storage, and network
optimization**

| Instance class     | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------ | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m6idn.32xlarge  | 128  | —   | 512          | 4 x 1900 NVMe SSD      | 80,000                    | 200                      |
| db.m6idn.24xlarge  | 96   | —   | 384          | 4 x 1425 NVMe SSD      | 60,000                    | 150                      |
| db.m6idn.16xlarge  | 64   | —   | 256          | 2 x 1900 NVMe SSD      | 40,000                    | 100                      |
| db.m6idn.12xlarge  | 48   | —   | 192          | 2 x 1425 NVMe SSD      | 30,000                    | 75                       |
| db.m6idn.8xlarge   | 32   | —   | 128          | 1 x 1900 NVMe SSD      | 20,000                    | 50                       |
| db.m6idn.4xlarge\* | 16   | —   | 64           | 1 x 950 NVMe SSD       | Up to 20,000              | Up to 50                 |
| db.m6idn.2xlarge\* | 8    | —   | 32           | 1 x 474 NVMe SSD       | Up to 20,000              | Up to 40                 |
| db.m6idn.xlarge\*  | 4    | —   | 16           | 1 x 237 NVMe SSD       | Up to 20,000              | Up to 30                 |
| db.m6idn.large\*   | 2    | —   | 8            | 1 x 118 NVMe SSD       | Up to 20,000              | Up to 25                 |

**db.m6in – general-purpose instance classes powered by 3rd
generation Intel Xeon Scalable processors and network optimization**

| Instance class    | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m6in.metal     | 128  | 64              | 2       | —   | 512          | EBS-optimized only     | 100,000                   | 200                      |
| db.m6in.32xlarge  | 128  |                 |         | —   | 512          | EBS-optimized only     | 80,000                    | 200                      |
| db.m6in.24xlarge  | 96   |                 |         | —   | 384          | EBS-optimized only     | 60,000                    | 150                      |
| db.m6in.16xlarge  | 64   |                 |         | —   | 256          | EBS-optimized only     | 40,000                    | 100                      |
| db.m6in.12xlarge  | 48   |                 |         | —   | 192          | EBS-optimized only     | 30,000                    | 75                       |
| db.m6in.8xlarge   | 32   |                 |         | —   | 128          | EBS-optimized only     | 20,000                    | 50                       |
| db.m6in.4xlarge\* | 16   |                 |         | —   | 64           | EBS-optimized only     | Up to 20,000              | Up to 50                 |
| db.m6in.2xlarge\* | 8    |                 |         | —   | 32           | EBS-optimized only     | Up to 20,000              | Up to 40                 |
| db.m6in.xlarge\*  | 4    |                 |         | —   | 16           | EBS-optimized only     | Up to 20,000              | Up to 30                 |
| db.m6in.large\*   | 2    |                 |         | —   | 8            | EBS-optimized only     | Up to 20,000              | Up to 25                 |

**db.m6i – general-purpose instance classes powered by 3rd
generation Intel Xeon Scalable processors**

| Instance class   | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m6i.metal     | 128  | 64              | 2       | —   | 512          | EBS-optimized only     | 40,000                    | 50                       |
| db.m6i.32xlarge  | 128  |                 |         | —   | 512          | EBS-optimized only     | 40,000                    | 50                       |
| db.m6i.24xlarge  | 96   |                 |         | —   | 384          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.m6i.16xlarge  | 64   |                 |         | —   | 256          | EBS-optimized only     | 20,000                    | 25                       |
| db.m6i.12xlarge  | 48   |                 |         | —   | 192          | EBS-optimized only     | 15,000                    | 18.75                    |
| db.m6i.8xlarge   | 32   |                 |         | —   | 128          | EBS-optimized only     | 10,000                    | 12.5                     |
| db.m6i.4xlarge\* | 16   |                 |         | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m6i.2xlarge\* | 8    |                 |         | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m6i.xlarge\*  | 4    |                 |         | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.m6i.large\*   | 2    |                 |         | —   | 8            | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.m5d – general-purpose instance classes powered by Intel
Xeon Platinum processors and SSD storage**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m5d.24xlarge  | 96   | 345 | 384          | 4 x 900 NVMe SSD       | 19,000                    | 25                       |
| db.m5d.16xlarge  | 64   | 262 | 256          | 4 x 600 NVMe SSD       | 13,600                    | 20                       |
| db.m5d.12xlarge  | 48   | 173 | 192          | 2 x 900 NVMe SSD       | 9,500                     | 10                       |
| db.m5d.8xlarge   | 32   | 131 | 128          | 2 x 600 NVMe SSD       | 6,800                     | 10                       |
| db.m5d.4xlarge   | 16   | 61  | 64           | 2 x 300 NVMe SSD       | 4,750                     | Up to 10                 |
| db.m5d.2xlarge\* | 8    | 31  | 32           | 1 x 300 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.m5d.xlarge\*  | 4    | 15  | 16           | 1 x 150 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.m5d.large\*   | 2    | 10  | 8            | 1 x 75 NVMe SSD        | Up to 4,750               | Up to 10                 |

**db.m5 – general-purpose instance classes with Intel Xeon
Platinum processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m5.24xlarge  | 96   | 345 | 384          | EBS-optimized only     | 19,000                    | 25                       |
| db.m5.16xlarge  | 64   | 262 | 256          | EBS-optimized only     | 13,600                    | 20                       |
| db.m5.12xlarge  | 48   | 173 | 192          | EBS-optimized only     | 9,500                     | 10                       |
| db.m5.8xlarge   | 32   | 131 | 128          | EBS-optimized only     | 6,800                     | 10                       |
| db.m5.4xlarge   | 16   | 61  | 64           | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.m5.2xlarge\* | 8    | 31  | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.m5.xlarge\*  | 4    | 15  | 16           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.m5.large\*   | 2    | 10  | 8            | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.m4 – general-purpose instance classes with Intel Xeon
Scalable processors**

| Instance class | vCPU | ECU   | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | ----- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m4.16xlarge | 64   | 188   | 256          | EBS-optimized only     | 10,000                    | 25                       |
| db.m4.10xlarge | 40   | 124.5 | 160          | EBS-optimized only     | 4,000                     | 10                       |
| db.m4.4xlarge  | 16   | 53.5  | 64           | EBS-optimized only     | 2,000                     | High                     |
| db.m4.2xlarge  | 8    | 25.5  | 32           | EBS-optimized only     | 1,000                     | High                     |
| db.m4.xlarge   | 4    | 13    | 16           | EBS-optimized only     | 750                       | High                     |
| db.m4.large    | 2    | 6.5   | 8            | EBS-optimized only     | 450                       | Moderate                 |

**db.m3 – general-purpose instance classes**

| Instance class | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m3.2xlarge  | 8    | 26  | 30           | EBS-optimized only     | 1,000                     | High                     |
| db.m3.xlarge   | 4    | 13  | 15           | EBS-optimized only     | 500                       | High                     |
| db.m3.large    | 2    | 6.5 | 7.5          | EBS only               | —                         | Moderate                 |
| db.m3.medium   | 1    | 3   | 3.75         | EBS only               | —                         | Moderate                 |

\* These DB instance classes can support maximum performance for 30 minutes
at least once every 24 hours. For more information on baseline performance of the underlying
EC2 instance types, see [Amazon EBS-optimized
instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the _Amazon EC2 User Guide._

## Hardware

specifications for the memory-optimized instance classes

The following tables show the compute, memory, storage, and bandwidth specifications
for the memory-optimized instance classes.

**db.z1d – memory-optimized instance
classes**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.z1d.12xlarge | 48   | 271 | 384          | 2 x 900 NVMe SSD       | 14,000                    | 25                       |
| db.z1d.6xlarge  | 24   | 134 | 192          | 1 x 900 NVMe SSD       | 7,000                     | 10                       |
| db.z1d.3xlarge  | 12   | 75  | 96           | 1 x 450 NVMe SSD       | 3,500                     | Up to 10                 |
| db.z1d.2xlarge  | 8    | 53  | 64           | 1 x 300 NVMe SSD       | 2,333                     | Up to 10                 |
| db.z1d.xlarge\* | 4    | 28  | 32           | 1 x 150 NVMe SSD       | Up to 2,333               | Up to 10                 |
| db.z1d.large\*  | 2    | 15  | 16           | 1 x 75 NVMe SSD        | Up to 2,333               | Up to 10                 |

**db.x2g – memory-optimized instance classes with AWS
Graviton2 processors**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x2g.16xlarge | 64   | —   | 1024         | EBS-optimized only     | 19,000                    | 25                       |
| db.x2g.12xlarge | 48   | —   | 768          | EBS-optimized only     | 14,250                    | 20                       |
| db.x2g.8xlarge  | 32   | —   | 512          | EBS-optimized only     | 9,500                     | 12                       |
| db.x2g.4xlarge  | 16   | —   | 256          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.x2g.2xlarge  | 8    | —   | 128          | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.x2g.xlarge   | 4    | —   | 64           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.x2g.large    | 2    | —   | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.x2idn – memory-optimized instance classes with 3rd
generation Intel Xeon Scalable processors**

| Instance class    | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x2idn.metal    | 128  | 64              | 2       | —   | 2,048        | 2 x 1900 NVMe SSD      | 80,000                    | 100                      |
| db.x2idn.32xlarge | 128  | —               | —       | —   | 2,048        | 2 x 1900 NVMe SSD      | 80,000                    | 100                      |
| db.x2idn.24xlarge | 96   | —               | —       | —   | 1,536        | 2 x 1425 NVMe SSD      | 60,000                    | 75                       |
| db.x2idn.16xlarge | 64   | —               | —       | —   | 1,024        | 1 x 1900 NVMe SSD      | 40,000                    | 50                       |

**db.x2iedn – memory-optimized instance classes with local
NVMe-based SSDs, with 3rd generation Intel Xeon Scalable
processors**

| Instance class     | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------ | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x2iedn.metal    | 128  | 64              | 2       | —   | 4,096        | 2 x 1900 NVMe SSD      | 80,000                    | 100                      |
| db.x2iedn.32xlarge | 128  | —               | —       | —   | 4,096        | 2 x 1900 NVMe SSD      | 80,000                    | 100                      |
| db.x2iedn.24xlarge | 96   | —               | —       | —   | 3,072        | 2 x 1425 NVMe SSD      | 60,000                    | 75                       |
| db.x2iedn.16xlarge | 64   | —               | —       | —   | 2,048        | 1 x 1900 NVMe SSD      | 40,000                    | 50                       |
| db.x2iedn.8xlarge  | 32   | —               | —       | —   | 1,024        | 1 x 950 NVMe SSD       | 20,000                    | 25                       |
| db.x2iedn.4xlarge  | 16   | —               | —       | —   | 512          | 1 x 475 NVMe SSD       | Up to 20,000              | Up to 25                 |
| db.x2iedn.2xlarge  | 8    | —               | —       | —   | 256          | 1 x 237 NVMe SSD       | Up to 20,000              | Up to 25                 |
| db.x2iedn.xlarge   | 4    | —               | —       | —   | 128          | 1 x 118 NVMe SSD       | Up to 20,000              | Up to 25                 |

**db.x2iezn – memory-optimized instance classes with 2nd
generation Intel Xeon Scalable processors**

| Instance class     | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------ | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x2iezn.metal    | 48   | 24              | 2       | —   | 1,536        | EBS-optimized only     | 19,000                    | 100                      |
| db.x2iezn.12xlarge | >48  | —               | —       | —   | 1,536        | EBS-optimized only     | 19,000                    | 100                      |
| db.x2iezn.8xlarge  | 32   | —               | —       | —   | 1,024        | EBS-optimized only     | 12,000                    | 75                       |
| db.x2iezn.6xlarge  | 24   | —               | —       | —   | 768          | EBS-optimized only     | Up to 9,500               | 50                       |
| db.x2iezn.4xlarge  | 16   | —               | —       | —   | 512          | EBS-optimized only     | Up to 4,750               | Up to 25                 |
| db.x2iezn.2xlarge  | 8    | —               | —       | —   | 256          | EBS-optimized only     | Up to 3,170               | Up to 25                 |

**db.x1e – memory-optimized instance
classes**

| Instance class  | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x1e.32xlarge | 128  | 340 | 3,904        | EBS-optimized only     | 14,000                    | 25                       |
| db.x1e.16xlarge | 64   | 179 | 1,952        | EBS-optimized only     | 7,000                     | 10                       |
| db.x1e.8xlarge  | 32   | 91  | 976          | EBS-optimized only     | 3,500                     | Up to 10                 |
| db.x1e.4xlarge  | 16   | 47  | 488          | EBS-optimized only     | 1,750                     | Up to 10                 |
| db.x1e.2xlarge  | 8    | 23  | 244          | EBS-optimized only     | 1,000                     | Up to 10                 |
| db.x1e.xlarge   | 4    | 12  | 122          | EBS-optimized only     | 500                       | Up to 10                 |

**db.x1 – memory-optimized instance
classes**

| Instance class | vCPU | ECU   | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | ----- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.x1.32xlarge | 128  | 349   | 1,952        | EBS-optimized only     | 14,000                    | 25                       |
| db.x1.16xlarge | 64   | 174.5 | 976          | EBS-optimized only     | 7,000                     | 10                       |

**db.m8gd – memory-optimized instance classes powered by AWS
Graviton4 processors and SSD storage**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.m8gd.48xlarge | 192  | —   | 768          | 6 x 1900 NVMe SSD      | 40,000                    | 50                       |
| db.m8gd.24xlarge | 96   | —   | 512          | 3 x 1900 NVMe SSD      | 30,000                    | 40                       |
| db.m8gd.16xlarge | 64   | —   | 384          | 2 x 1900 NVMe SSD      | 20,000                    | 30                       |
| db.m8gd.12xlarge | 48   | —   | 256          | 3 x 950 NVMe SSD       | 15,000                    | 22.5                     |
| db.m8gd.8xlarge  | 32   | —   | 128          | 1 x 1900 NVMe SSD      | 10,000                    | 15                       |
| db.m8gd.4xlarge  | 16   | —   | 64           | 1 x 950 NVMe SSD       | Up to 10,000              | Up to 15                 |
| db.m8gd.2xlarge  | 8    | —   | 32           | 1 x 474 NVMe SSD       | Up to 10,000              | Up to 15                 |
| db.m8gd.xlarge   | 4    | —   | 16           | 1 x 237 NVMe SSD       | Up to 10,000              | Up to 12.5               |
| db.m8gd.large    | 2    | —   | 8            | 1 x 118 NVMe SSD       | Up to 10,000              | Up to 12.5               |

**db.r8gd – memory-optimized instance classes with AWS
Graviton4 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r8gd.48xlarge | 192  | —   | 1536         | 6 x 1900 NVMe SSD      | 40,000                    | 50                       |
| db.r8gd.24xlarge | 96   | —   | 768          | 3 x 1900 NVMe SSD      | 30,000                    | 40                       |
| db.r8gd.16xlarge | 64   | —   | 512          | 2 x 1900 NVMe SSD      | 20,000                    | 30                       |
| db.r8gd.12xlarge | 48   | —   | 384          | 3 x 950 NVMe SSD       | 15,000                    | 22.5                     |
| db.r8gd.8xlarge  | 32   | —   | 256          | 1 x 1900 NVMe SSD      | 10,000                    | 15                       |
| db.r8gd.4xlarge  | 16   | —   | 128          | 1 x 950 NVMe SSD       | Up to 10,000              | Up to 15                 |
| db.r8gd.2xlarge  | 8    | —   | 64           | 1 x 474 NVMe SSD       | Up to 10,000              | Up to 15                 |
| db.r8gd.xlarge   | 4    | —   | 32           | 1 x 237 NVMe SSD       | Up to 10,000              | Up to 12.5               |
| db.r8gd.large    | 2    | —   | 16           | 1 x 118 NVMe SSD       | Up to 10,000              | Up to 12.5               |

**db.r8g – memory-optimized instance classes with AWS
Graviton4 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r8g.48xlarge  | 192  | —   | 1536         | EBS-optimized only     | 40,000                    | 50                       |
| db.r8g.24xlarge  | 96   | —   | 768          | EBS-optimized only     | 30,000                    | 40                       |
| db.r8g.16xlarge  | 64   | —   | 512          | EBS-optimized only     | 20,000                    | 30                       |
| db.r8g.12xlarge  | 48   | —   | 384          | EBS-optimized only     | 15,000                    | 22.5                     |
| db.r8g.8xlarge   | 32   | —   | 256          | EBS-optimized only     | 10,000                    | 15                       |
| db.r8g.4xlarge\* | 16   | —   | 128          | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r8g.2xlarge\* | 8    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r8g.xlarge\*  | 4    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r8g.large\*   | 2    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r7i – memory-optimized instance classes powered by 4th
generation Intel Xeon Scalable processors**

| Instance class            | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Normalized units | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------------- | ---- | --------------- | ------- | --- | ------------ | ---------------- | ---------------------- | ------------------------- | ------------------------ |
| db.r7i.metal-48xl         | 192  | 96              | 2       | —   | 1536         | 192              | EBS-optimized only     | 40,000                    | 50                       |
| db.r7i.metal-24xl         | 96   | 48              | 1       | —   | 768          | 96               | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r7i.48xlarge           | 192  | —               | —       | —   | 1536         | 192              | EBS-optimized only     | 40,000                    | 50                       |
| db.r7i.24xlarge           | 96   | —               | —       | —   | 768          | 96               | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r7i.16xlarge           | 64   | —               | —       | —   | 512          | 64               | EBS-optimized only     | 20,000                    | 25                       |
| db.r7i.12xlarge           | 48   | —               | —       | —   | 384          | 48               | EBS-optimized only     | 15,000                    | 18.75                    |
| db.r7i.8xlarge.tpc2.mem3x | 32   | —               | —       | —   | 768          | 96               | EBS-optimized only     | 30,000                    | 12.5                     |
| db.r7i.8xlarge.tpc2.mem2x | 32   | —               | —       | —   | 512          | 64               | EBS-optimized only     | 20,000                    | 12.5                     |
| db.r7i.8xlarge            | 32   | —               | —       | —   | 256          | 32               | EBS-optimized only     | 10,000                    | 12.5                     |
| db.r7i.6xlarge.tpc2.mem4x | 24   | —               | —       | —   | 768          | 96               | EBS-optimized only     | 30,000                    | Up to 12.5               |
| db.r7i.6xlarge.tpc2.mem2x | 24   | —               | —       | —   | 384          | 48               | EBS-optimized only     | 15,000                    | Up to 12.5               |
| db.r7i.4xlarge.tpc2.mem4x | 16   | —               | —       | —   | 512          | 64               | EBS-optimized only     | 20,000                    | Up to 12.5               |
| db.r7i.4xlarge.tpc2.mem3x | 16   | —               | —       | —   | 384          | 48               | EBS-optimized only     | 15,000                    | Up to 12.5               |
| db.r7i.4xlarge.tpc2.mem2x | 16   | —               | —       | —   | 256          | 32               | EBS-optimized only     | 10,000                    | Up to 12.5               |
| db.r7i.4xlarge            | 16   | —               | —       | —   | 128          | 16               | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.3xlarge.tpc2.mem4x | 12   | —               | —       | —   | 384          | 48               | EBS-optimized only     | 15,000                    | Up to 12.5               |
| db.r7i.2xlarge.tpc2.mem8x | 8    | —               | —       | —   | 512          | 64               | EBS-optimized only     | 20,000                    | Up to 12.5               |
| db.r7i.2xlarge.tpc2.mem4x | 8    | —               | —       | —   | 256          | 32               | EBS-optimized only     | 10,000                    | Up to 12.5               |
| db.r7i.2xlarge            | 8    | —               | —       | —   | 64           | 8                | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.xlarge.tpc2.mem4x  | 4    | —               | —       | —   | 128          | 16               | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.xlarge.tpc2.mem2x  | 4    | —               | —       | —   | 64           | 8                | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.xlarge             | 4    | —               | —       | —   | 32           | 4                | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7i.large              | 2    | —               | —       | —   | 16           | 2                | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r7g – memory-optimized instance classes with AWS
Graviton3 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r7g.16xlarge  | 64   | —   | 512          | EBS-optimized only     | 20,000                    | 30                       |
| db.r7g.12xlarge  | 48   | —   | 384          | EBS-optimized only     | 15,000                    | 22.5                     |
| db.r7g.8xlarge   | 32   | —   | 256          | EBS-optimized only     | 10,000                    | 15                       |
| db.r7g.4xlarge   | 16   | —   | 128          | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r7g.2xlarge\* | 8    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 15                 |
| db.r7g.xlarge\*  | 4    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r7g.large\*   | 2    | —   | 16           | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r6g – memory-optimized instance classes with AWS
Graviton2 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6g.16xlarge  | 64   | —   | 512          | EBS-optimized only     | 19,000                    | 25                       |
| db.r6g.12xlarge  | 48   | —   | 384          | EBS-optimized only     | 13,500                    | 20                       |
| db.r6g.8xlarge   | 32   | —   | 256          | EBS-optimized only     | 9,000                     | 12                       |
| db.r6g.4xlarge   | 16   | —   | 128          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.r6g.2xlarge\* | 8    | —   | 64           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r6g.xlarge\*  | 4    | —   | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r6g.large\*   | 2    | —   | 16           | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.r6gd – memory-optimized instance classes with AWS
Graviton2 processors and SSD storage**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6gd.16xlarge | 64   | —   | 512          | 2 x 1900 NVMe SSD      | 19,000                    | 25                       |
| db.r6gd.12xlarge | 48   | —   | 384          | 2 x 1425 NVMe SSD      | 13,500                    | 20                       |
| db.r6gd.8xlarge  | 32   | —   | 256          | 1 x 1900 NVMe SSD      | 9,000                     | 12                       |
| db.r6gd.4xlarge  | 16   | —   | 128          | 1 x 950 NVMe SSD       | 4,750                     | Up to 10                 |
| db.r6gd.2xlarge  | 8    | —   | 64           | 1 x 474 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.r6gd.xlarge   | 4    | —   | 32           | 1 x 237 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.r6gd.large    | 2    | —   | 16           | 1 x 118 NVMe SSD       | Up to 4,750               | Up to 10                 |

**db.r6id – memory-optimized instance classes with 3rd
generation Intel Xeon Scalable processors and SSD storage**

| Instance class    | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6id.metal     | 128  | 64              | 2       | —   | 1,024        | 4 x 1900 NVMe SSD      | 40,000                    | 50                       |
| db.r6id.32xlarge  | 128  | —               | —       | —   | 1,024        | 4x1900 NVMe SSD        | 40,000                    | 50                       |
| db.r6id.24xlarge  | 96   | —               | —       | —   | 768          | 4x1425 NVMe SSD        | 30,000                    | 37.5                     |
| db.r6id.16xlarge  | 64   | —               | —       | —   | 512          | 2x1900 NVMe SSD        | 20,000                    | 25                       |
| db.r6id.12xlarge  | 48   | —               | —       | —   | 384          | 2x1425 NVMe SSD        | 15,000                    | 18.75                    |
| db.r6id.8xlarge   | 32   | —               | —       | —   | 256          | 1x1900 NVMe SSD        | 10,000                    | 12.5                     |
| db.r6id.4xlarge\* | 16   | —               | —       | —   | 128          | 1x950 NVMe SSD         | Up to 10,000              | Up to 12.5               |
| db.r6id.2xlarge\* | 8    | —               | —       | —   | 64           | 1x474 NVMe SSD         | Up to 10,000              | Up to 12.5               |
| db.r6id.xlarge\*  | 4    | —               | —       | —   | 32           | 1x237 NVMe SSD         | Up to 10,000              | Up to 12.5               |
| db.r6id.large\*   | 2    | —               | —       | —   | 16           | 1x118 NVMe SSD         | Up to 10,000              | Up to 12.5               |

**db.r6idn – memory-optimized instance classes with 3rd
generation Intel Xeon Scalable processors, SSD storage, and network
optimization**

| Instance class     | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------ | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6idn.32xlarge  | 128  | —   | 1,024        | 4x1900 NVMe SSD        | 80,000                    | 200                      |
| db.r6idn.24xlarge  | 96   | —   | 768          | 4x1425 NVMe SSD        | 60,000                    | 150                      |
| db.r6idn.16xlarge  | 64   | —   | 512          | 2x1900 NVMe SSD        | 40,000                    | 100                      |
| db.r6idn.12xlarge  | 48   | —   | 384          | 2x1425 NVMe SSD        | 30,000                    | 75                       |
| db.r6idn.8xlarge   | 32   | —   | 256          | 1x1900 NVMe SSD        | 20,000                    | 50                       |
| db.r6idn.4xlarge\* | 16   | —   | 128          | 1x950 NVMe SSD         | Up to 20,000              | Up to 50                 |
| db.r6idn.2xlarge\* | 8    | —   | 64           | 1x474 NVMe SSD         | Up to 20,000              | Up to 40                 |
| db.r6idn.xlarge\*  | 4    | —   | 32           | 1x237 NVMe SSD         | Up to 20,000              | Up to 30                 |
| db.r6idn.large\*   | 2    | —   | 16           | 1x118 NVMe SSD         | Up to 20,000              | Up to 25                 |

**db.r6in – memory-optimized instance classes with 3rd
generation Intel Xeon Scalable processors and network
optimization**

| Instance class    | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --------------- | ------- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6in.metal     | 128  | 64              | 2       | —   | 1,024        | EBS-optimized only     | 100,000                   | 200                      |
| db.r6in.32xlarge  | 128  | —               | —       | —   | 1,024        | EBS-optimized only     | 80,000                    | 200                      |
| db.r6in.24xlarge  | 96   | —               | —       | —   | 768          | EBS-optimized only     | 60,000                    | 150                      |
| db.r6in.16xlarge  | 64   | —               | —       | —   | 512          | EBS-optimized only     | 40,000                    | 100                      |
| db.r6in.12xlarge  | 48   | —               | —       | —   | 384          | EBS-optimized only     | 30,000                    | 75                       |
| db.r6in.8xlarge   | 32   | —               | —       | —   | 256          | EBS-optimized only     | 20,000                    | 50                       |
| db.r6in.4xlarge\* | 16   | —               | —       | —   | 128          | EBS-optimized only     | Up to 20,000              | Up to 50                 |
| db.r6in.2xlarge\* | 8    | —               | —       | —   | 64           | EBS-optimized only     | Up to 20,000              | Up to 40                 |
| db.r6in.xlarge\*  | 4    | —               | —       | —   | 32           | EBS-optimized only     | Up to 20,000              | Up to 30                 |
| db.r6in.large\*   | 2    | —               | —       | —   | 16           | EBS-optimized only     | Up to 20,000              | Up to 25                 |

**db.r6i – Oracle memory-optimized instance classes
preconfigured for high memory, storage, and I/O**

| Instance class            | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r6i.8xlarge.tpc2.mem4x | 32   | —   | 1024         | EBS-optimized only     | 40,000                    | 50                       |
| db.r6i.8xlarge.tpc2.mem3x | 32   | —   | 768          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r6i.6xlarge.tpc2.mem4x | 24   | —   | 768          | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r6i.4xlarge.tpc2.mem4x | 16   | —   | 512          | EBS-optimized only     | 20,000                    | 25                       |
| db.r6i.4xlarge.tpc2.mem3x | 16   | —   | 384          | EBS-optimized only     | 15,000                    | 18.75                    |
| db.r6i.4xlarge.tpc2.mem2x | 16   | —   | 256          | EBS-optimized only     | 10,000                    | 12.5                     |
| db.r6i.2xlarge.tpc2.mem8x | 8    | —   | 512          | EBS-optimized only     | 20,000                    | 12.5                     |
| db.r6i.2xlarge.tpc2.mem4x | 8    | —   | 256          | EBS-optimized only     | 10,000                    | 12.5                     |
| db.r6i.2xlarge.tpc1.mem2x | 8    | —   | 128          | EBS-optimized only     | Up to 10,000              | 12.5                     |
| db.r6i.xlarge.tpc2.mem4x  | 4    | —   | 128          | EBS-optimized only     | Up to 10,000              | 12.5                     |
| db.r6i.xlarge.tpc2.mem2x  | 4    | —   | 64           | EBS-optimized only     | Up to 10,000              | 12.5                     |
| db.r6i.large.tpc1.mem2x   | 2    | —   | 32           | EBS-optimized only     | Up to 10,000              | 12.5                     |

**db.r6i – memory-optimized instance classes with 3rd
Generation Intel Xeon Scalable processors**

| Instance class   | vCPU | Processor cores | Sockets | ECU | Memory (GiB) | Normalized units | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --------------- | ------- | --- | ------------ | ---------------- | ---------------------- | ------------------------- | ------------------------ |
| db.r6i.metal     | 128  | 64              | 2       | —   | 1,024        | 256              | EBS-optimized only     | 40,000                    | 50                       |
| db.r6i.32xlarge  | 128  | —               | —       | —   | 1,024        | 256              | EBS-optimized only     | 40,000                    | 50                       |
| db.r6i.24xlarge  | 96   | —               | —       | —   | 768          | 192              | EBS-optimized only     | 30,000                    | 37.5                     |
| db.r6i.16xlarge  | 64   | —               | —       | —   | 512          | 128              | EBS-optimized only     | 20,000                    | 25                       |
| db.r6i.12xlarge  | 48   | —               | —       | —   | 384          | 96               | EBS-optimized only     | 15,000                    | 18.75                    |
| db.r6i.8xlarge   | 32   | —               | —       | —   | 256          | 64               | EBS-optimized only     | 10,000                    | 12.5                     |
| db.r6i.4xlarge\* | 16   | —               | —       | —   | 128          | 32               | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r6i.2xlarge\* | 8    | —               | —       | —   | 64           | 16               | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r6i.xlarge\*  | 4    | —               | —       | —   | 32           | 8                | EBS-optimized only     | Up to 10,000              | Up to 12.5               |
| db.r6i.large\*   | 2    | —               | —       | —   | 16           | 4                | EBS-optimized only     | Up to 10,000              | Up to 12.5               |

**db.r5d – memory-optimized instance classes with Intel
Xeon Platinum processors and SSD storage**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r5d.24xlarge  | 96   | 347 | 768          | 4 x 900 NVMe SSD       | 19,000                    | 25                       |
| db.r5d.16xlarge  | 64   | 264 | 512          | 4 x 600 NVMe SSD       | 13,600                    | 20                       |
| db.r5d.12xlarge  | 48   | 173 | 384          | 2 x 900 NVMe SSD       | 9,500                     | 10                       |
| db.r5d.8xlarge   | 32   | 132 | 256          | 2 x 600 NVMe SSD       | 6,800                     | 10                       |
| db.r5d.4xlarge   | 16   | 71  | 128          | 2 x 300 NVMe SSD       | 4,750                     | Up to 10                 |
| db.r5d.2xlarge\* | 8    | 38  | 64           | 1 x 300 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.r5d.xlarge\*  | 4    | 19  | 32           | 1 x 150 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.r5d.large\*   | 2    | 10  | 16           | 1 x 75 NVMe SSD        | Up to 4,750               | Up to 10                 |

**db.r5b – Oracle memory-optimized instance classes
preconfigured for high memory, storage, and I/O**

| Instance class            | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r5b.8xlarge.tpc2.mem3x | 32   | —   | 768          | EBS-optimized only     | 60,000                    | 25                       |
| db.r5b.6xlarge.tpc2.mem4x | 24   | —   | 768          | EBS-optimized only     | 60,000                    | 25                       |
| db.r5b.4xlarge.tpc2.mem4x | 16   | —   | 512          | EBS-optimized only     | 40,000                    | 20                       |
| db.r5b.4xlarge.tpc2.mem3x | 16   | —   | 384          | EBS-optimized only     | 30,000                    | 10                       |
| db.r5b.4xlarge.tpc2.mem2x | 16   | —   | 256          | EBS-optimized only     | 20,000                    | 10                       |
| db.r5b.2xlarge.tpc2.mem8x | 8    | —   | 512          | EBS-optimized only     | 40,000                    | 20                       |
| db.r5b.2xlarge.tpc2.mem4x | 8    | —   | 256          | EBS-optimized only     | 20,000                    | 10                       |
| db.r5b.2xlarge.tpc1.mem2x | 8    | —   | 128          | EBS-optimized only     | 10,000                    | Up to 10                 |
| db.r5b.xlarge.tpc2.mem4x  | 4    | —   | 128          | EBS-optimized only     | 10,000                    | Up to 10                 |
| db.r5b.xlarge.tpc2.mem2x  | 4    | —   | 64           | EBS-optimized only     | Up to 10,000              | Up to 10                 |
| db.r5b.large.tpc1.mem2x   | 2    | —   | 32           | EBS-optimized only     | Up to 10,000              | Up to 10                 |

**db.r5b – memory-optimized instance classes with Intel
Xeon Platinum processors and EBS optimization**

| Instance class   | vCPU | ECU | Memory (GiB) | Normalized units | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------- | ---------------------- | ------------------------- | ------------------------ |
| db.r5b.24xlarge  | 96   | 347 | 768          | 192              | EBS-optimized only     | 60,000                    | 25                       |
| db.r5b.16xlarge  | 64   | 264 | 512          | 128              | EBS-optimized only     | 40,000                    | 20                       |
| db.r5b.12xlarge  | 48   | 173 | 384          | 96               | EBS-optimized only     | 30,000                    | 10                       |
| db.r5b.8xlarge   | 32   | 132 | 256          | 64               | EBS-optimized only     | 20,000                    | 10                       |
| db.r5b.4xlarge   | 16   | 71  | 128          | 32               | EBS-optimized only     | 10,000                    | Up to 10                 |
| db.r5b.2xlarge\* | 8    | 38  | 64           | 16               | EBS-optimized only     | Up to 10,000              | Up to 10                 |
| db.r5b.xlarge\*  | 4    | 19  | 32           | 8                | EBS-optimized only     | Up to 10,000              | Up to 10                 |
| db.r5b.large\*   | 2    | 10  | 16           | 4                | EBS-optimized only     | Up to 10,000              | Up to 10                 |

**db.r5 – Oracle memory-optimized instance classes
preconfigured for high memory, storage, and I/O**

| Instance class            | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ------------------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r5.12xlarge.tpc2.mem2x | 48   | —   | 768          | EBS-optimized only     | 19,000                    | 25                       |
| db.r5.8xlarge.tpc2.mem3x  | 32   | —   | 768          | EBS-optimized only     | 19,000                    | 25                       |
| db.r5.6xlarge.tpc2.mem4x  | 24   | —   | 768          | EBS-optimized only     | 19,000                    | 25                       |
| db.r5.4xlarge.tpc2.mem4x  | 16   | —   | 512          | EBS-optimized only     | 13,600                    | 20                       |
| db.r5.4xlarge.tpc2.mem3x  | 16   | —   | 384          | EBS-optimized only     | 9,500                     | 10                       |
| db.r5.4xlarge.tpc2.mem2x  | 16   | —   | 256          | EBS-optimized only     | 6,800                     | 10                       |
| db.r5.2xlarge.tpc2.mem8x  | 8    | —   | 512          | EBS-optimized only     | 13,600                    | 20                       |
| db.r5.2xlarge.tpc2.mem4x  | 8    | —   | 256          | EBS-optimized only     | 6,800                     | 10                       |
| db.r5.2xlarge.tpc1.mem2x  | 8    | —   | 128          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.r5.xlarge.tpc2.mem4x   | 4    | —   | 128          | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.r5.xlarge.tpc2.mem2x   | 4    | —   | 64           | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r5.large.tpc1.mem2x    | 2    | —   | 32           | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.r5 – memory-optimized instance
classes**

| Instance class  | vCPU | ECU | Memory (GiB) | Normalized units | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | --- | ------------ | ---------------- | ---------------------- | ------------------------- | ------------------------ |
| db.r5.24xlarge  | 96   | 347 | 768          | 192              | EBS-optimized only     | 19,000                    | 25                       |
| db.r5.16xlarge  | 64   | 264 | 512          | 128              | EBS-optimized only     | 13,600                    | 20                       |
| db.r5.12xlarge  | 48   | 173 | 384          | 96               | EBS-optimized only     | 9,500                     | 12                       |
| db.r5.8xlarge   | 32   | 132 | 256          | 64               | EBS-optimized only     | 6,800                     | 10                       |
| db.r5.4xlarge   | 16   | 71  | 128          | 32               | EBS-optimized only     | 4,750                     | Up to 10                 |
| db.r5.2xlarge\* | 8    | 38  | 64           | 16               | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r5.xlarge\*  | 4    | 19  | 32           | 8                | EBS-optimized only     | Up to 4,750               | Up to 10                 |
| db.r5.large\*   | 2    | 10  | 16           | 4                | EBS-optimized only     | Up to 4,750               | Up to 10                 |

**db.r4 – memory-optimized instance classes with Intel Xeon
Scalable processors**

| Instance class | vCPU | ECU  | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | ---- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r4.16xlarge | 64   | 195  | 488          | EBS-optimized only     | 14,000                    | 25                       |
| db.r4.8xlarge  | 32   | 99   | 244          | EBS-optimized only     | 7,000                     | 10                       |
| db.r4.4xlarge  | 16   | 53   | 122          | EBS-optimized only     | 3,500                     | Up to 10                 |
| db.r4.2xlarge  | 8    | 27   | 61           | EBS-optimized only     | 1,700                     | Up to 10                 |
| db.r4.xlarge   | 4    | 13.5 | 30.5         | EBS-optimized only     | 850                       | Up to 10                 |
| db.r4.large    | 2    | 7    | 15.25        | EBS-optimized only     | 425                       | Up to 10                 |

**db.r3 – memory-optimized instance
classes**

| Instance class    | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ----------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.r3.8xlarge\*\* | 32   | 104 | 244          | EBS only               | —                         | 10                       |
| db.r3.4xlarge     | 16   | 52  | 122          | EBS-optimized only     | 2,000                     | High                     |
| db.r3.2xlarge     | 8    | 26  | 61           | EBS-optimized only     | 1,000                     | High                     |
| db.r3.xlarge      | 4    | 13  | 30.5         | EBS-optimized only     | 500                       | Moderate                 |
| db.r3.large       | 2    | 6.5 | 15.25        | EBS-optimized only     | —                         | Moderate                 |

\* These DB instance classes can support maximum performance for 30
minutes at least once every 24 hours. For more information on baseline performance
of the underlying EC2 instance types, see [Amazon EBS-optimized instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in
the _Amazon EC2 User Guide._

\*\* The r3.8xlarge DB instance class doesn't have dedicated EBS
bandwidth and therefore doesn't offer EBS optimization. For this instance class,
network traffic and Amazon EBS traffic share the same 10-gigabit network
interface.

## Hardware specifications

for the compute-optimized instance classes

The following tables show the compute, memory, storage, and bandwidth specifications for
the compute-optimized instance classes.

**db.c6gd – compute-optimized instance classes (for Multi-AZ DB cluster
deployments only)**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.c6gd.16xlarge | 64   | —   | 128          | 2 x 1900 NVMe SSD      | 19,000                    | 25                       |
| db.c6gd.12xlarge | 48   | —   | 96           | 2 x 1425 NVMe SSD      | 13,500                    | 20                       |
| db.c6gd.8xlarge  | 32   | —   | 64           | 1 x 1900 NVMe SSD      | 9,000                     | 12                       |
| db.c6gd.4xlarge  | 16   | —   | 32           | 1 x 950 NVMe SSD       | 4,750                     | Up to 10                 |
| db.c6gd.2xlarge  | 8    | —   | 16           | 1 x 474 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.c6gd.xlarge   | 4    | —   | 8            | 1 x 237 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.c6gd.large    | 2    | —   | 4            | 1 x 118 NVMe SSD       | Up to 4,750               | Up to 10                 |
| db.c6gd.medium   | 1    | —   | 2            | 1 x 59 NVMe SSD        | Up to 4,750               | Up to 10                 |

## Hardware specifications for

the burstable-performance instance classes

The following tables show the compute, memory, storage, and bandwidth specifications for
the burstable-performance instance classes.

**db.t4g – burstable-performance instance classes powered by
AWS Graviton2 processors**

| Instance class   | vCPU | ECU | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| ---------------- | ---- | --- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.t4g.2xlarge\* | 8    | —   | 32           | EBS-optimized only     | Up to 2,780               | Up to 5                  |
| db.t4g.xlarge\*  | 4    | —   | 16           | EBS-optimized only     | Up to 2,780               | Up to 5                  |
| db.t4g.large\*   | 2    | —   | 8            | EBS-optimized only     | Up to 2,780               | Up to 5                  |
| db.t4g.medium\*  | 2    | —   | 4            | EBS-optimized only     | Up to 2,085               | Up to 5                  |
| db.t4g.small\*   | 2    | —   | 2            | EBS-optimized only     | Up to 2,085               | Up to 5                  |
| db.t4g.micro\*   | 2    | —   | 1            | EBS-optimized only     | Up to 2,085               | Up to 5                  |

**db.t3 – burstable-performance instance
classes**

| Instance class  | vCPU | ECU      | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| --------------- | ---- | -------- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.t3.2xlarge\* | 8    | Variable | 32           | EBS-optimized only     | Up to 2,048               | Up to 5                  |
| db.t3.xlarge\*  | 4    | Variable | 16           | EBS-optimized only     | Up to 2,048               | Up to 5                  |
| db.t3.large\*   | 2    | Variable | 8            | EBS-optimized only     | Up to 2,048               | Up to 5                  |
| db.t3.medium\*  | 2    | Variable | 4            | EBS-optimized only     | Up to 1,536               | Up to 5                  |
| db.t3.small\*   | 2    | Variable | 2            | EBS-optimized only     | Up to 1,536               | Up to 5                  |
| db.t3.micro\*   | 2    | Variable | 1            | EBS-optimized only     | Up to 1,536               | Up to 5                  |

**db.t2 – burstable-performance instance
classes**

| Instance class | vCPU | ECU      | Memory (GiB) | Instance storage (GiB) | Max. EBS bandwidth (Mbps) | Network bandwidth (Gbps) |
| -------------- | ---- | -------- | ------------ | ---------------------- | ------------------------- | ------------------------ |
| db.t2.2xlarge  | 8    | Variable | 32           | EBS only               | —                         | Moderate                 |
| db.t2.xlarge   | 4    | Variable | 16           | EBS only               | —                         | Moderate                 |
| db.t2.large    | 2    | Variable | 8            | EBS only               | —                         | Moderate                 |
| db.t2.medium   | 2    | Variable | 4            | EBS only               | —                         | Moderate                 |
| db.t2.small    | 1    | Variable | 2            | EBS only               | —                         | Low                      |
| db.t2.micro    | 1    | Variable | 1            | EBS only               | —                         | Low                      |

\* These DB instance classes can support maximum performance for 30 minutes
at least once every 24 hours. For more information on baseline performance of the underlying
EC2 instance types, see [Amazon EBS-optimized
instances](../../../AWSEC2/latest/UserGuide/EBSOptimized.md "../../../AWSEC2/latest/UserGuide/EBSOptimized.md") in the _Amazon EC2 User Guide._
