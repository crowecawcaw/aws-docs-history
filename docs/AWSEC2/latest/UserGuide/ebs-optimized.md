# Amazon EBS-optimized instance types

Amazon EBS–optimized instances use an optimized configuration stack and provide additional,
dedicated bandwidth for Amazon EBS I/O. This optimization provides the best performance for your
EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance.

When attached to an EBS–optimized instance, General Purpose SSD (`gp2` and `gp3`) volumes are designed to
deliver at least 90 percent of their provisioned IOPS performance 99 percent of the time in
a given year, and Provisioned IOPS SSD (`io1` and `io2`) volumes are designed to deliver at least 90 percent of
their provisioned IOPS performance 99.9 percent of the time in a given year. Throughput Optimized HDD
(`st1`) and Cold HDD (`sc1`) deliver at least 90 percent of their expected throughput
performance 99 percent of the time in a given year. Non-compliant periods are approximately
uniformly distributed, targeting 99 percent of expected total throughput each hour. For more
information, see [Amazon EBS volume types](../../../ebs/latest/userguide/ebs-volume-types.md "../../../ebs/latest/userguide/ebs-volume-types.md")
in the _Amazon EBS User Guide_.

Some instance types are **EBS-optimized by default**, and
there is no need to enable it and no effect if you attempt to disable it. Other instance types
optionally **support EBS optimization** and you can enable it
during or after launch for an [additional hourly fee](https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances "https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances"). Some instance types do not support EBS optimization.

For detailed instance type specifications and features, see the [Amazon EC2 Instance Types Guide](../../../ec2/latest/instancetypes/instance-types.md "../../../ec2/latest/instancetypes/instance-types.md").

###### Considerations

- An instance's EBS performance is bounded by the instance type's performance limits,
  or the aggregated performance of its attached volumes, whichever is smaller. To achieve
  maximum EBS performance, an instance must have attached volumes that provide a combined
  performance equal to or greater than the maximum instance performance. For example, to
  achieve `80,000` IOPS for `r6i.16xlarge`, the instance must have
  at least `5` `gp2` volumes provisioned with `16,000`
  IOPS each (`5` volumes x `16,000` IOPS = `80,000` IOPS),
  or it can have `1` `gp3` volume provisioned with `80,000`
  IOPS. We recommend that you choose an instance type that provides more dedicated Amazon EBS
  throughput than your application needs; otherwise, the connection between Amazon EBS and Amazon EC2
  can become a performance bottleneck.
- The maximum number of Amazon EBS volumes that you can attach to an instance depends on the
  instance type and instance size. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md "volume_limits.md").
- The maximum IOPS and throughput limits are interdependent. Depending on your I/O size,
  you might reach one limit before the other, which can affect overall performance. For
  optimal results, consider both limits when planning your workload.

## EBS-optimized by default

The following instance types are EBS–optimized by default. There is no need
to enable EBS optimization and no effect if you disable EBS optimization.

###### Instances

- [General purpose](#current-general-purpose "#current-general-purpose")
- [Compute optimized](#current-compute-optimized "#current-compute-optimized")
- [Memory optimized](#current-memory-optimized "#current-memory-optimized")
- [Storage optimized](#current-storage-optimized "#current-storage-optimized")
- [Accelerated computing](#current-accelerated-computing "#current-accelerated-computing")
- [High-performance computing](#current-high-performance-computing "#current-high-performance-computing")

### General purpose

###### Note

M8a, M8g, M8gd, M8i, M8i-flex instance types support configurable bandwidth weightings. With
these instance types, you can optimize an instance's bandwidth for either networking performance
or Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these
instance types. For more information, see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md "configure-bandwidth-weighting.md").

| Instance size        | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| -------------------- | ------------------------- | ------------------------ | --------------------------------------- | -------------------------------------- | -------------------------- | ------------------------- |
| a1.medium 1          | 300                       | 3500                     | 37.50                                   | 437.50                                 | 2500                       | 20000                     |
| a1.large 1           | 525                       | 3500                     | 65.62                                   | 437.50                                 | 4000                       | 20000                     |
| a1.xlarge 1          | 800                       | 3500                     | 100.00                                  | 437.50                                 | 6000                       | 20000                     |
| a1.2xlarge 1         | 1750                      | 3500                     | 218.75                                  | 437.50                                 | 10000                      | 20000                     |
| a1.4xlarge 2         | 3500                      | 437.5                    | 20000                                   |
| a1.metal 2           | 3500                      | 437.5                    | 20000                                   |
| m4.large 2           | 450                       | 56.25                    | 3600                                    |
| m4.xlarge 2          | 750                       | 93.75                    | 6000                                    |
| m4.2xlarge 2         | 1000                      | 125.0                    | 8000                                    |
| m4.4xlarge 2         | 2000                      | 250.0                    | 16000                                   |
| m4.10xlarge 2        | 4000                      | 500.0                    | 32000                                   |
| m4.16xlarge 2        | 10000                     | 1250.0                   | 65000                                   |
| m5.large 1           | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| m5.xlarge 1          | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| m5.2xlarge 1         | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| m5.4xlarge 2         | 4750                      | 593.75                   | 18750                                   |
| m5.8xlarge 2         | 6800                      | 850.0                    | 30000                                   |
| m5.12xlarge 2        | 9500                      | 1187.5                   | 40000                                   |
| m5.16xlarge 2        | 13600                     | 1700.0                   | 60000                                   |
| m5.24xlarge 2        | 19000                     | 2375.0                   | 80000                                   |
| m5.metal 2           | 19000                     | 2375.0                   | 80000                                   |
| m5a.large 1          | 650                       | 2880                     | 81.25                                   | 360.00                                 | 3600                       | 16000                     |
| m5a.xlarge 1         | 1085                      | 2880                     | 135.62                                  | 360.00                                 | 6000                       | 16000                     |
| m5a.2xlarge 1        | 1580                      | 2880                     | 197.50                                  | 360.00                                 | 8333                       | 16000                     |
| m5a.4xlarge 2        | 2880                      | 360.0                    | 16000                                   |
| m5a.8xlarge 2        | 4750                      | 593.75                   | 20000                                   |
| m5a.12xlarge 2       | 6780                      | 847.5                    | 30000                                   |
| m5a.16xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| m5a.24xlarge 2       | 13750                     | 1718.75                  | 60000                                   |
| m5ad.large 1         | 650                       | 2880                     | 81.25                                   | 360.00                                 | 3600                       | 16000                     |
| m5ad.xlarge 1        | 1085                      | 2880                     | 135.62                                  | 360.00                                 | 6000                       | 16000                     |
| m5ad.2xlarge 1       | 1580                      | 2880                     | 197.50                                  | 360.00                                 | 8333                       | 16000                     |
| m5ad.4xlarge 2       | 2880                      | 360.0                    | 16000                                   |
| m5ad.8xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| m5ad.12xlarge 2      | 6780                      | 847.5                    | 30000                                   |
| m5ad.16xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| m5ad.24xlarge 2      | 13750                     | 1718.75                  | 60000                                   |
| m5d.large 1          | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| m5d.xlarge 1         | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| m5d.2xlarge 1        | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| m5d.4xlarge 2        | 4750                      | 593.75                   | 18750                                   |
| m5d.8xlarge 2        | 6800                      | 850.0                    | 30000                                   |
| m5d.12xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| m5d.16xlarge 2       | 13600                     | 1700.0                   | 60000                                   |
| m5d.24xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| m5d.metal 2          | 19000                     | 2375.0                   | 80000                                   |
| m5dn.large 1         | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| m5dn.xlarge 1        | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| m5dn.2xlarge 1       | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| m5dn.4xlarge 2       | 4750                      | 593.75                   | 18750                                   |
| m5dn.8xlarge 2       | 6800                      | 850.0                    | 30000                                   |
| m5dn.12xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| m5dn.16xlarge 2      | 13600                     | 1700.0                   | 60000                                   |
| m5dn.24xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| m5dn.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| m5n.large 1          | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| m5n.xlarge 1         | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| m5n.2xlarge 1        | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| m5n.4xlarge 2        | 4750                      | 593.75                   | 18750                                   |
| m5n.8xlarge 2        | 6800                      | 850.0                    | 30000                                   |
| m5n.12xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| m5n.16xlarge 2       | 13600                     | 1700.0                   | 60000                                   |
| m5n.24xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| m5n.metal 2          | 19000                     | 2375.0                   | 80000                                   |
| m5zn.large 1         | 800                       | 3170                     | 100.00                                  | 396.25                                 | 3333                       | 13333                     |
| m5zn.xlarge 1        | 1564                      | 3170                     | 195.50                                  | 396.25                                 | 6667                       | 13333                     |
| m5zn.2xlarge 2       | 3170                      | 396.25                   | 13333                                   |
| m5zn.3xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| m5zn.6xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| m5zn.12xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| m5zn.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| m6a.large 1          | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m6a.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m6a.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m6a.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m6a.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m6a.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m6a.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m6a.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m6a.32xlarge 2       | 40000                     | 5000.0                   | 160000                                  |
| m6a.48xlarge 2       | 40000                     | 5000.0                   | 240000                                  |
| m6a.metal 2          | 40000                     | 5000.0                   | 240000                                  |
| m6g.medium 1         | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| m6g.large 1          | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| m6g.xlarge 1         | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| m6g.2xlarge 1        | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| m6g.4xlarge 2        | 4750                      | 593.75                   | 20000                                   |
| m6g.8xlarge 2        | 9500                      | 1187.5                   | 40000                                   |
| m6g.12xlarge 2       | 14250                     | 1781.25                  | 50000                                   |
| m6g.16xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| m6g.metal 2          | 19000                     | 2375.0                   | 80000                                   |
| m6gd.medium 1        | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| m6gd.large 1         | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| m6gd.xlarge 1        | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| m6gd.2xlarge 1       | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| m6gd.4xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| m6gd.8xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| m6gd.12xlarge 2      | 14250                     | 1781.25                  | 50000                                   |
| m6gd.16xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| m6gd.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| m6i.large 1          | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m6i.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m6i.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m6i.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m6i.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m6i.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m6i.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m6i.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m6i.32xlarge 2       | 40000                     | 5000.0                   | 160000                                  |
| m6i.metal 2          | 40000                     | 5000.0                   | 160000                                  |
| m6id.large 1         | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m6id.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m6id.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m6id.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m6id.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| m6id.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| m6id.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| m6id.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| m6id.32xlarge 2      | 40000                     | 5000.0                   | 160000                                  |
| m6id.metal 2         | 40000                     | 5000.0                   | 160000                                  |
| m6idn.large 1        | 1562                      | 25000                    | 195.31                                  | 3125.00                                | 6250                       | 100000                    |
| m6idn.xlarge 1       | 3125                      | 25000                    | 390.62                                  | 3125.00                                | 12500                      | 100000                    |
| m6idn.2xlarge 1      | 6250                      | 25000                    | 781.25                                  | 3125.00                                | 25000                      | 100000                    |
| m6idn.4xlarge 1      | 12500                     | 25000                    | 1562.50                                 | 3125.00                                | 50000                      | 100000                    |
| m6idn.8xlarge 2      | 25000                     | 3125.0                   | 100000                                  |
| m6idn.12xlarge 2     | 37500                     | 4687.5                   | 150000                                  |
| m6idn.16xlarge 2     | 50000                     | 6250.0                   | 200000                                  |
| m6idn.24xlarge 2     | 75000                     | 9375.0                   | 300000                                  |
| m6idn.32xlarge 2     | 100000                    | 12500.0                  | 400000                                  |
| m6idn.metal 2        | 100000                    | 12500.0                  | 400000                                  |
| m6in.large 1         | 1562                      | 25000                    | 195.31                                  | 3125.00                                | 6250                       | 100000                    |
| m6in.xlarge 1        | 3125                      | 25000                    | 390.62                                  | 3125.00                                | 12500                      | 100000                    |
| m6in.2xlarge 1       | 6250                      | 25000                    | 781.25                                  | 3125.00                                | 25000                      | 100000                    |
| m6in.4xlarge 1       | 12500                     | 25000                    | 1562.50                                 | 3125.00                                | 50000                      | 100000                    |
| m6in.8xlarge 2       | 25000                     | 3125.0                   | 100000                                  |
| m6in.12xlarge 2      | 37500                     | 4687.5                   | 150000                                  |
| m6in.16xlarge 2      | 50000                     | 6250.0                   | 200000                                  |
| m6in.24xlarge 2      | 75000                     | 9375.0                   | 300000                                  |
| m6in.32xlarge 2      | 100000                    | 12500.0                  | 400000                                  |
| m6in.metal 2         | 100000                    | 12500.0                  | 400000                                  |
| m7a.medium 1         | 325                       | 10000                    | 40.62                                   | 1250.00                                | 2500                       | 40000                     |
| m7a.large 1          | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m7a.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m7a.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m7a.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m7a.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m7a.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m7a.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m7a.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m7a.32xlarge 2       | 40000                     | 5000.0                   | 160000                                  |
| m7a.48xlarge 2       | 40000                     | 5000.0                   | 240000                                  |
| m7a.metal-48xl 2     | 40000                     | 5000.0                   | 240000                                  |
| m7g.medium 1         | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| m7g.large 1          | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| m7g.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m7g.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m7g.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m7g.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m7g.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m7g.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m7g.metal 2          | 20000                     | 2500.0                   | 80000                                   |
| m7gd.medium 1        | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| m7gd.large 1         | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| m7gd.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m7gd.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m7gd.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m7gd.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| m7gd.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| m7gd.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| m7gd.metal 2         | 20000                     | 2500.0                   | 80000                                   |
| m7i.large 1          | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m7i.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m7i.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m7i.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m7i.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m7i.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m7i.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m7i.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m7i.48xlarge 2       | 40000                     | 5000.0                   | 240000                                  |
| m7i.metal-24xl 2     | 30000                     | 3750.0                   | 120000                                  |
| m7i.metal-48xl 2     | 40000                     | 5000.0                   | 240000                                  |
| m7i-flex.large 1     | 312                       | 10000                    | 39.06                                   | 1250.00                                | 2500                       | 40000                     |
| m7i-flex.xlarge 1    | 625                       | 10000                    | 78.12                                   | 1250.00                                | 3600                       | 40000                     |
| m7i-flex.2xlarge 1   | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m7i-flex.4xlarge 1   | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m7i-flex.8xlarge 1   | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m7i-flex.12xlarge 1  | 7500                      | 15000                    | 937.50                                  | 1875.00                                | 30000                      | 60000                     |
| m7i-flex.16xlarge 1  | 10000                     | 20000                    | 1250.00                                 | 2500.00                                | 40000                      | 80000                     |
| m8a.medium 1         | 325                       | 10000                    | 40.62                                   | 1250.00                                | 2500                       | 40000                     |
| m8a.large 1          | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m8a.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m8a.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m8a.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m8a.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m8a.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m8a.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m8a.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m8a.48xlarge 2       | 60000                     | 7500.0                   | 240000                                  |
| m8a.metal-24xl 2     | 30000                     | 3750.0                   | 120000                                  |
| m8a.metal-48xl 2     | 60000                     | 7500.0                   | 240000                                  |
| m8g.medium 1         | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| m8g.large 1          | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| m8g.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m8g.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m8g.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m8g.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m8g.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m8g.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m8g.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m8g.48xlarge 2       | 40000                     | 5000.0                   | 240000                                  |
| m8g.metal-24xl 2     | 30000                     | 3750.0                   | 120000                                  |
| m8g.metal-48xl 2     | 40000                     | 5000.0                   | 240000                                  |
| m8gd.medium 1        | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| m8gd.large 1         | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| m8gd.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m8gd.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m8gd.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m8gd.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| m8gd.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| m8gd.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| m8gd.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| m8gd.48xlarge 2      | 40000                     | 5000.0                   | 240000                                  |
| m8gd.metal-24xl 2    | 30000                     | 3750.0                   | 120000                                  |
| m8gd.metal-48xl 2    | 40000                     | 5000.0                   | 240000                                  |
| m8i.large 1          | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| m8i.xlarge 1         | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m8i.2xlarge 1        | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m8i.4xlarge 1        | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m8i.8xlarge 2        | 10000                     | 1250.0                   | 40000                                   |
| m8i.12xlarge 2       | 15000                     | 1875.0                   | 60000                                   |
| m8i.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| m8i.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| m8i.32xlarge 2       | 40000                     | 5000.0                   | 160000                                  |
| m8i.48xlarge 2       | 60000                     | 7500.0                   | 240000                                  |
| m8i.96xlarge 2       | 80000                     | 10000.0                  | 480000                                  |
| m8i.metal-48xl 2     | 60000                     | 7500.0                   | 240000                                  |
| m8i.metal-96xl 2     | 80000                     | 10000.0                  | 480000                                  |
| m8i-flex.large 1     | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| m8i-flex.xlarge 1    | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| m8i-flex.2xlarge 1   | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| m8i-flex.4xlarge 1   | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| m8i-flex.8xlarge 1   | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| m8i-flex.12xlarge 1  | 7500                      | 15000                    | 937.50                                  | 1875.00                                | 30000                      | 60000                     |
| m8i-flex.16xlarge 1  | 10000                     | 20000                    | 1250.00                                 | 2500.00                                | 40000                      | 80000                     |
| mac1.metal 2         | 14000                     | 1750.0                   | 80000                                   |
| mac2.metal 2         | 10000                     | 1250.0                   | 55000                                   |
| mac2-m1ultra.metal 2 | 10000                     | 1250.0                   | 55000                                   |
| mac2-m2.metal 2      | 8000                      | 1000.0                   | 55000                                   |
| mac2-m2pro.metal 2   | 8000                      | 1000.0                   | 55000                                   |
| mac-m4.metal 2       | 8000                      | 1000.0                   | 55000                                   |
| mac-m4pro.metal 2    | 8000                      | 1000.0                   | 55000                                   |
| t3.nano 1            | 43                        | 2085                     | 5.38                                    | 260.62                                 | 250                        | 11800                     |
| t3.micro 1           | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11800                     |
| t3.small 1           | 174                       | 2085                     | 21.75                                   | 260.62                                 | 1000                       | 11800                     |
| t3.medium 1          | 347                       | 2085                     | 43.38                                   | 260.62                                 | 2000                       | 11800                     |
| t3.large 1           | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t3.xlarge 1          | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t3.2xlarge 1         | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t3a.nano 1           | 45                        | 2085                     | 5.62                                    | 260.62                                 | 250                        | 11800                     |
| t3a.micro 1          | 90                        | 2085                     | 11.25                                   | 260.62                                 | 500                        | 11800                     |
| t3a.small 1          | 175                       | 2085                     | 21.88                                   | 260.62                                 | 1000                       | 11800                     |
| t3a.medium 1         | 350                       | 2085                     | 43.75                                   | 260.62                                 | 2000                       | 11800                     |
| t3a.large 1          | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t3a.xlarge 1         | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t3a.2xlarge 1        | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t4g.nano 1           | 43                        | 2085                     | 5.38                                    | 260.62                                 | 250                        | 11800                     |
| t4g.micro 1          | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11800                     |
| t4g.small 1          | 174                       | 2085                     | 21.75                                   | 260.62                                 | 1000                       | 11800                     |
| t4g.medium 1         | 347                       | 2085                     | 43.38                                   | 260.62                                 | 2000                       | 11800                     |
| t4g.large 1          | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t4g.xlarge 1         | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |
| t4g.2xlarge 1        | 695                       | 2780                     | 86.88                                   | 347.50                                 | 4000                       | 15700                     |

1 These instances can sustain the maximum performance for 30 minutes
at least once every 24 hours, after which they revert to their baseline performance.

2 These instances can sustain their stated performance indefinitely.
If your workload requires sustained maximum performance for longer than 30 minutes, use one of
these instances.

### Compute optimized

###### Note

C8g, C8gd, C8i, C8i-flex instance types support configurable bandwidth weightings. With these instance types, you can optimize
an instance's bandwidth for either networking performance or Amazon EBS performance. The following table shows the
default Amazon EBS bandwidth performance for these instance types. For more information,
see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md "configure-bandwidth-weighting.md").

| Instance size       | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| ------------------- | ------------------------- | ------------------------ | --------------------------------------- | -------------------------------------- | -------------------------- | ------------------------- |
| c4.large 2          | 500                       | 62.5                     | 4000                                    |
| c4.xlarge 2         | 750                       | 93.75                    | 6000                                    |
| c4.2xlarge 2        | 1000                      | 125.0                    | 8000                                    |
| c4.4xlarge 2        | 2000                      | 250.0                    | 16000                                   |
| c4.8xlarge 2        | 4000                      | 500.0                    | 32000                                   |
| c5.large 1          | 650                       | 4750                     | 81.25                                   | 593.75                                 | 4000                       | 20000                     |
| c5.xlarge 1         | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 20000                     |
| c5.2xlarge 1        | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 10000                      | 20000                     |
| c5.4xlarge 2        | 4750                      | 593.75                   | 20000                                   |
| c5.9xlarge 2        | 9500                      | 1187.5                   | 40000                                   |
| c5.12xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| c5.18xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| c5.24xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| c5.metal 2          | 19000                     | 2375.0                   | 80000                                   |
| c5a.large 1         | 200                       | 3170                     | 25.00                                   | 396.25                                 | 800                        | 13300                     |
| c5a.xlarge 1        | 400                       | 3170                     | 50.00                                   | 396.25                                 | 1600                       | 13300                     |
| c5a.2xlarge 1       | 800                       | 3170                     | 100.00                                  | 396.25                                 | 3200                       | 13300                     |
| c5a.4xlarge 1       | 1580                      | 3170                     | 197.50                                  | 396.25                                 | 6600                       | 13300                     |
| c5a.8xlarge 2       | 3170                      | 396.25                   | 13300                                   |
| c5a.12xlarge 2      | 4750                      | 593.75                   | 20000                                   |
| c5a.16xlarge 2      | 6300                      | 787.5                    | 26700                                   |
| c5a.24xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| c5ad.large 1        | 200                       | 3170                     | 25.00                                   | 396.25                                 | 800                        | 13300                     |
| c5ad.xlarge 1       | 400                       | 3170                     | 50.00                                   | 396.25                                 | 1600                       | 13300                     |
| c5ad.2xlarge 1      | 800                       | 3170                     | 100.00                                  | 396.25                                 | 3200                       | 13300                     |
| c5ad.4xlarge 1      | 1580                      | 3170                     | 197.50                                  | 396.25                                 | 6600                       | 13300                     |
| c5ad.8xlarge 2      | 3170                      | 396.25                   | 13300                                   |
| c5ad.12xlarge 2     | 4750                      | 593.75                   | 20000                                   |
| c5ad.16xlarge 2     | 6300                      | 787.5                    | 26700                                   |
| c5ad.24xlarge 2     | 9500                      | 1187.5                   | 40000                                   |
| c5d.large 1         | 650                       | 4750                     | 81.25                                   | 593.75                                 | 4000                       | 20000                     |
| c5d.xlarge 1        | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 20000                     |
| c5d.2xlarge 1       | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 10000                      | 20000                     |
| c5d.4xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| c5d.9xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| c5d.12xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| c5d.18xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| c5d.24xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| c5d.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| c5n.large 1         | 650                       | 4750                     | 81.25                                   | 593.75                                 | 4000                       | 20000                     |
| c5n.xlarge 1        | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 20000                     |
| c5n.2xlarge 1       | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 10000                      | 20000                     |
| c5n.4xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| c5n.9xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| c5n.18xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| c5n.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| c6a.large 1         | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| c6a.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c6a.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c6a.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c6a.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c6a.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c6a.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c6a.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| c6a.32xlarge 2      | 40000                     | 5000.0                   | 160000                                  |
| c6a.48xlarge 2      | 40000                     | 5000.0                   | 240000                                  |
| c6a.metal 2         | 40000                     | 5000.0                   | 240000                                  |
| c6g.medium 1        | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| c6g.large 1         | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| c6g.xlarge 1        | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| c6g.2xlarge 1       | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| c6g.4xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| c6g.8xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| c6g.12xlarge 2      | 14250                     | 1781.25                  | 50000                                   |
| c6g.16xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| c6g.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| c6gd.medium 1       | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| c6gd.large 1        | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| c6gd.xlarge 1       | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| c6gd.2xlarge 1      | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| c6gd.4xlarge 2      | 4750                      | 593.75                   | 20000                                   |
| c6gd.8xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| c6gd.12xlarge 2     | 14250                     | 1781.25                  | 50000                                   |
| c6gd.16xlarge 2     | 19000                     | 2375.0                   | 80000                                   |
| c6gd.metal 2        | 19000                     | 2375.0                   | 80000                                   |
| c6gn.medium 1       | 760                       | 9500                     | 95.00                                   | 1187.50                                | 2500                       | 40000                     |
| c6gn.large 1        | 1235                      | 9500                     | 154.38                                  | 1187.50                                | 5000                       | 40000                     |
| c6gn.xlarge 1       | 2375                      | 9500                     | 296.88                                  | 1187.50                                | 10000                      | 40000                     |
| c6gn.2xlarge 1      | 4750                      | 9500                     | 593.75                                  | 1187.50                                | 20000                      | 40000                     |
| c6gn.4xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| c6gn.8xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| c6gn.12xlarge 2     | 28500                     | 3562.5                   | 120000                                  |
| c6gn.16xlarge 2     | 38000                     | 4750.0                   | 160000                                  |
| c6i.large 1         | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| c6i.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c6i.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c6i.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c6i.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c6i.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c6i.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c6i.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| c6i.32xlarge 2      | 40000                     | 5000.0                   | 160000                                  |
| c6i.metal 2         | 40000                     | 5000.0                   | 160000                                  |
| c6id.large 1        | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| c6id.xlarge 1       | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c6id.2xlarge 1      | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c6id.4xlarge 1      | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c6id.8xlarge 2      | 10000                     | 1250.0                   | 40000                                   |
| c6id.12xlarge 2     | 15000                     | 1875.0                   | 60000                                   |
| c6id.16xlarge 2     | 20000                     | 2500.0                   | 80000                                   |
| c6id.24xlarge 2     | 30000                     | 3750.0                   | 120000                                  |
| c6id.32xlarge 2     | 40000                     | 5000.0                   | 160000                                  |
| c6id.metal 2        | 40000                     | 5000.0                   | 160000                                  |
| c6in.large 1        | 1562                      | 25000                    | 195.31                                  | 3125.00                                | 6250                       | 100000                    |
| c6in.xlarge 1       | 3125                      | 25000                    | 390.62                                  | 3125.00                                | 12500                      | 100000                    |
| c6in.2xlarge 1      | 6250                      | 25000                    | 781.25                                  | 3125.00                                | 25000                      | 100000                    |
| c6in.4xlarge 1      | 12500                     | 25000                    | 1562.50                                 | 3125.00                                | 50000                      | 100000                    |
| c6in.8xlarge 2      | 25000                     | 3125.0                   | 100000                                  |
| c6in.12xlarge 2     | 37500                     | 4687.5                   | 150000                                  |
| c6in.16xlarge 2     | 50000                     | 6250.0                   | 200000                                  |
| c6in.24xlarge 2     | 75000                     | 9375.0                   | 300000                                  |
| c6in.32xlarge 2     | 100000                    | 12500.0                  | 400000                                  |
| c6in.metal 2        | 100000                    | 12500.0                  | 400000                                  |
| c7a.medium 1        | 325                       | 10000                    | 40.62                                   | 1250.00                                | 2500                       | 40000                     |
| c7a.large 1         | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| c7a.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c7a.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c7a.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c7a.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c7a.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c7a.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c7a.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| c7a.32xlarge 2      | 40000                     | 5000.0                   | 160000                                  |
| c7a.48xlarge 2      | 40000                     | 5000.0                   | 240000                                  |
| c7a.metal-48xl 2    | 40000                     | 5000.0                   | 240000                                  |
| c7g.medium 1        | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| c7g.large 1         | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| c7g.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c7g.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c7g.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c7g.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c7g.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c7g.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c7g.metal 2         | 20000                     | 2500.0                   | 80000                                   |
| c7gd.medium 1       | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| c7gd.large 1        | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| c7gd.xlarge 1       | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c7gd.2xlarge 1      | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c7gd.4xlarge 1      | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c7gd.8xlarge 2      | 10000                     | 1250.0                   | 40000                                   |
| c7gd.12xlarge 2     | 15000                     | 1875.0                   | 60000                                   |
| c7gd.16xlarge 2     | 20000                     | 2500.0                   | 80000                                   |
| c7gd.metal 2        | 20000                     | 2500.0                   | 80000                                   |
| c7gn.medium 1       | 521                       | 10000                    | 65.12                                   | 1250.00                                | 2083                       | 40000                     |
| c7gn.large 1        | 1042                      | 10000                    | 130.25                                  | 1250.00                                | 4167                       | 40000                     |
| c7gn.xlarge 1       | 2083                      | 10000                    | 260.38                                  | 1250.00                                | 8333                       | 40000                     |
| c7gn.2xlarge 1      | 4167                      | 10000                    | 520.88                                  | 1250.00                                | 16667                      | 40000                     |
| c7gn.4xlarge 1      | 8333                      | 10000                    | 1041.62                                 | 1250.00                                | 33333                      | 40000                     |
| c7gn.8xlarge 1      | 16667                     | 20000                    | 2083.38                                 | 2500.00                                | 66667                      | 80000                     |
| c7gn.12xlarge 1     | 25000                     | 30000                    | 3125.00                                 | 3750.00                                | 100000                     | 120000                    |
| c7gn.16xlarge 1     | 33333                     | 40000                    | 4166.62                                 | 5000.00                                | 133333                     | 160000                    |
| c7gn.metal 1        | 33333                     | 40000                    | 4166.62                                 | 5000.00                                | 133333                     | 160000                    |
| c7i.large 1         | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| c7i.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c7i.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c7i.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c7i.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c7i.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c7i.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c7i.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| c7i.48xlarge 2      | 40000                     | 5000.0                   | 240000                                  |
| c7i.metal-24xl 2    | 30000                     | 3750.0                   | 120000                                  |
| c7i.metal-48xl 2    | 40000                     | 5000.0                   | 240000                                  |
| c7i-flex.large 1    | 312                       | 10000                    | 39.06                                   | 1250.00                                | 2500                       | 40000                     |
| c7i-flex.xlarge 1   | 625                       | 10000                    | 78.12                                   | 1250.00                                | 3600                       | 40000                     |
| c7i-flex.2xlarge 1  | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c7i-flex.4xlarge 1  | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c7i-flex.8xlarge 1  | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c7i-flex.12xlarge 1 | 7500                      | 15000                    | 937.50                                  | 1875.00                                | 30000                      | 60000                     |
| c7i-flex.16xlarge 1 | 10000                     | 20000                    | 1250.00                                 | 2500.00                                | 40000                      | 80000                     |
| c8g.medium 1        | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| c8g.large 1         | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| c8g.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c8g.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c8g.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c8g.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c8g.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c8g.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c8g.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| c8g.48xlarge 2      | 40000                     | 5000.0                   | 240000                                  |
| c8g.metal-24xl 2    | 30000                     | 3750.0                   | 120000                                  |
| c8g.metal-48xl 2    | 40000                     | 5000.0                   | 240000                                  |
| c8gd.medium 1       | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| c8gd.large 1        | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| c8gd.xlarge 1       | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c8gd.2xlarge 1      | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c8gd.4xlarge 1      | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c8gd.8xlarge 2      | 10000                     | 1250.0                   | 40000                                   |
| c8gd.12xlarge 2     | 15000                     | 1875.0                   | 60000                                   |
| c8gd.16xlarge 2     | 20000                     | 2500.0                   | 80000                                   |
| c8gd.24xlarge 2     | 30000                     | 3750.0                   | 120000                                  |
| c8gd.48xlarge 2     | 40000                     | 5000.0                   | 240000                                  |
| c8gd.metal-24xl 2   | 30000                     | 3750.0                   | 120000                                  |
| c8gd.metal-48xl 2   | 40000                     | 5000.0                   | 240000                                  |
| c8gn.medium 1       | 760                       | 10000                    | 95.00                                   | 1250.00                                | 2500                       | 40000                     |
| c8gn.large 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| c8gn.xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| c8gn.2xlarge 1      | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c8gn.4xlarge 2      | 10000                     | 1250.0                   | 40000                                   |
| c8gn.8xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c8gn.12xlarge 2     | 30000                     | 3750.0                   | 120000                                  |
| c8gn.16xlarge 2     | 40000                     | 5000.0                   | 160000                                  |
| c8gn.24xlarge 2     | 60000                     | 7500.0                   | 240000                                  |
| c8gn.48xlarge 2     | 60000                     | 7500.0                   | 240000                                  |
| c8gn.metal-24xl 2   | 60000                     | 7500.0                   | 240000                                  |
| c8gn.metal-48xl 2   | 60000                     | 7500.0                   | 240000                                  |
| c8i.large 1         | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| c8i.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c8i.2xlarge 1       | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c8i.4xlarge 1       | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c8i.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| c8i.12xlarge 2      | 15000                     | 1875.0                   | 60000                                   |
| c8i.16xlarge 2      | 20000                     | 2500.0                   | 80000                                   |
| c8i.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| c8i.32xlarge 2      | 40000                     | 5000.0                   | 160000                                  |
| c8i.48xlarge 2      | 60000                     | 7500.0                   | 240000                                  |
| c8i.96xlarge 2      | 80000                     | 10000.0                  | 480000                                  |
| c8i.metal-48xl 2    | 60000                     | 7500.0                   | 240000                                  |
| c8i.metal-96xl 2    | 80000                     | 10000.0                  | 480000                                  |
| c8i-flex.large 1    | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| c8i-flex.xlarge 1   | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| c8i-flex.2xlarge 1  | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| c8i-flex.4xlarge 1  | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| c8i-flex.8xlarge 1  | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| c8i-flex.12xlarge 1 | 7500                      | 15000                    | 937.50                                  | 1875.00                                | 30000                      | 60000                     |
| c8i-flex.16xlarge 1 | 10000                     | 20000                    | 1250.00                                 | 2500.00                                | 40000                      | 80000                     |

1 These instances can sustain the maximum performance for 30 minutes
at least once every 24 hours, after which they revert to their baseline performance.

2 These instances can sustain their stated performance indefinitely.
If your workload requires sustained maximum performance for longer than 30 minutes, use one of
these instances.

### Memory optimized

###### Note

- R8a, R8g, R8gd, R8i, R8i-flex, X8g instance types support configurable bandwidth weightings. With
  these instance types, you can optimize an instance's bandwidth for either networking performance or
  Amazon EBS performance. The following table shows the default Amazon EBS bandwidth performance for these
  instance types. For more information, see [EC2 instance bandwidth weighting configuration](configure-bandwidth-weighting.md "configure-bandwidth-weighting.md").
- For maximum IOPS performance with U7i instances, we recommend that you use io2 BlockExpress
  volumes.

| Instance size          | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| ---------------------- | ------------------------- | ------------------------ | --------------------------------------- | -------------------------------------- | -------------------------- | ------------------------- |
| r4.large 2             | 425                       | 53.125                   | 3000                                    |
| r4.xlarge 2            | 850                       | 106.25                   | 6000                                    |
| r4.2xlarge 2           | 1700                      | 212.5                    | 12000                                   |
| r4.4xlarge 2           | 3500                      | 437.5                    | 18750                                   |
| r4.8xlarge 2           | 7000                      | 875.0                    | 37500                                   |
| r4.16xlarge 2          | 14000                     | 1750.0                   | 75000                                   |
| r5.large 1             | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| r5.xlarge 1            | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| r5.2xlarge 1           | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| r5.4xlarge 2           | 4750                      | 593.75                   | 18750                                   |
| r5.8xlarge 2           | 6800                      | 850.0                    | 30000                                   |
| r5.12xlarge 2          | 9500                      | 1187.5                   | 40000                                   |
| r5.16xlarge 2          | 13600                     | 1700.0                   | 60000                                   |
| r5.24xlarge 2          | 19000                     | 2375.0                   | 80000                                   |
| r5.metal 2             | 19000                     | 2375.0                   | 80000                                   |
| r5a.large 1            | 650                       | 2880                     | 81.25                                   | 360.00                                 | 3600                       | 16000                     |
| r5a.xlarge 1           | 1085                      | 2880                     | 135.62                                  | 360.00                                 | 6000                       | 16000                     |
| r5a.2xlarge 1          | 1580                      | 2880                     | 197.50                                  | 360.00                                 | 8333                       | 16000                     |
| r5a.4xlarge 2          | 2880                      | 360.0                    | 16000                                   |
| r5a.8xlarge 2          | 4750                      | 593.75                   | 20000                                   |
| r5a.12xlarge 2         | 6780                      | 847.5                    | 30000                                   |
| r5a.16xlarge 2         | 9500                      | 1187.5                   | 40000                                   |
| r5a.24xlarge 2         | 13570                     | 1696.25                  | 60000                                   |
| r5ad.large 1           | 650                       | 2880                     | 81.25                                   | 360.00                                 | 3600                       | 16000                     |
| r5ad.xlarge 1          | 1085                      | 2880                     | 135.62                                  | 360.00                                 | 6000                       | 16000                     |
| r5ad.2xlarge 1         | 1580                      | 2880                     | 197.50                                  | 360.00                                 | 8333                       | 16000                     |
| r5ad.4xlarge 2         | 2880                      | 360.0                    | 16000                                   |
| r5ad.8xlarge 2         | 4750                      | 593.75                   | 20000                                   |
| r5ad.12xlarge 2        | 6780                      | 847.5                    | 30000                                   |
| r5ad.16xlarge 2        | 9500                      | 1187.5                   | 40000                                   |
| r5ad.24xlarge 2        | 13570                     | 1696.25                  | 60000                                   |
| r5b.large 1            | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5417                       | 43333                     |
| r5b.xlarge 1           | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10833                      | 43333                     |
| r5b.2xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 21667                      | 43333                     |
| r5b.4xlarge 2          | 10000                     | 1250.0                   | 43333                                   |
| r5b.8xlarge 2          | 20000                     | 2500.0                   | 86667                                   |
| r5b.12xlarge 2         | 30000                     | 3750.0                   | 130000                                  |
| r5b.16xlarge 2         | 40000                     | 5000.0                   | 173333                                  |
| r5b.24xlarge 2         | 60000                     | 7500.0                   | 260000                                  |
| r5b.metal 2            | 60000                     | 7500.0                   | 260000                                  |
| r5d.large 1            | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| r5d.xlarge 1           | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| r5d.2xlarge 1          | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| r5d.4xlarge 2          | 4750                      | 593.75                   | 18750                                   |
| r5d.8xlarge 2          | 6800                      | 850.0                    | 30000                                   |
| r5d.12xlarge 2         | 9500                      | 1187.5                   | 40000                                   |
| r5d.16xlarge 2         | 13600                     | 1700.0                   | 60000                                   |
| r5d.24xlarge 2         | 19000                     | 2375.0                   | 80000                                   |
| r5d.metal 2            | 19000                     | 2375.0                   | 80000                                   |
| r5dn.large 1           | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| r5dn.xlarge 1          | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| r5dn.2xlarge 1         | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| r5dn.4xlarge 2         | 4750                      | 593.75                   | 18750                                   |
| r5dn.8xlarge 2         | 6800                      | 850.0                    | 30000                                   |
| r5dn.12xlarge 2        | 9500                      | 1187.5                   | 40000                                   |
| r5dn.16xlarge 2        | 13600                     | 1700.0                   | 60000                                   |
| r5dn.24xlarge 2        | 19000                     | 2375.0                   | 80000                                   |
| r5dn.metal 2           | 19000                     | 2375.0                   | 80000                                   |
| r5n.large 1            | 650                       | 4750                     | 81.25                                   | 593.75                                 | 3600                       | 18750                     |
| r5n.xlarge 1           | 1150                      | 4750                     | 143.75                                  | 593.75                                 | 6000                       | 18750                     |
| r5n.2xlarge 1          | 2300                      | 4750                     | 287.50                                  | 593.75                                 | 12000                      | 18750                     |
| r5n.4xlarge 2          | 4750                      | 593.75                   | 18750                                   |
| r5n.8xlarge 2          | 6800                      | 850.0                    | 30000                                   |
| r5n.12xlarge 2         | 9500                      | 1187.5                   | 40000                                   |
| r5n.16xlarge 2         | 13600                     | 1700.0                   | 60000                                   |
| r5n.24xlarge 2         | 19000                     | 2375.0                   | 80000                                   |
| r5n.metal 2            | 19000                     | 2375.0                   | 80000                                   |
| r6a.large 1            | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r6a.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r6a.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r6a.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r6a.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r6a.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r6a.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r6a.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r6a.32xlarge 2         | 40000                     | 5000.0                   | 160000                                  |
| r6a.48xlarge 2         | 40000                     | 5000.0                   | 240000                                  |
| r6a.metal 2            | 40000                     | 5000.0                   | 240000                                  |
| r6g.medium 1           | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| r6g.large 1            | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| r6g.xlarge 1           | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| r6g.2xlarge 1          | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| r6g.4xlarge 2          | 4750                      | 593.75                   | 20000                                   |
| r6g.8xlarge 2          | 9500                      | 1187.5                   | 40000                                   |
| r6g.12xlarge 2         | 14250                     | 1781.25                  | 50000                                   |
| r6g.16xlarge 2         | 19000                     | 2375.0                   | 80000                                   |
| r6g.metal 2            | 19000                     | 2375.0                   | 80000                                   |
| r6gd.medium 1          | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| r6gd.large 1           | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| r6gd.xlarge 1          | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| r6gd.2xlarge 1         | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| r6gd.4xlarge 2         | 4750                      | 593.75                   | 20000                                   |
| r6gd.8xlarge 2         | 9500                      | 1187.5                   | 40000                                   |
| r6gd.12xlarge 2        | 14250                     | 1781.25                  | 50000                                   |
| r6gd.16xlarge 2        | 19000                     | 2375.0                   | 80000                                   |
| r6gd.metal 2           | 19000                     | 2375.0                   | 80000                                   |
| r6i.large 1            | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r6i.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r6i.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r6i.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r6i.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r6i.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r6i.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r6i.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r6i.32xlarge 2         | 40000                     | 5000.0                   | 160000                                  |
| r6i.metal 2            | 40000                     | 5000.0                   | 160000                                  |
| r6id.large 1           | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r6id.xlarge 1          | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r6id.2xlarge 1         | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r6id.4xlarge 1         | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r6id.8xlarge 2         | 10000                     | 1250.0                   | 40000                                   |
| r6id.12xlarge 2        | 15000                     | 1875.0                   | 60000                                   |
| r6id.16xlarge 2        | 20000                     | 2500.0                   | 80000                                   |
| r6id.24xlarge 2        | 30000                     | 3750.0                   | 120000                                  |
| r6id.32xlarge 2        | 40000                     | 5000.0                   | 160000                                  |
| r6id.metal 2           | 40000                     | 5000.0                   | 160000                                  |
| r6idn.large 1          | 1562                      | 25000                    | 195.31                                  | 3125.00                                | 6250                       | 100000                    |
| r6idn.xlarge 1         | 3125                      | 25000                    | 390.62                                  | 3125.00                                | 12500                      | 100000                    |
| r6idn.2xlarge 1        | 6250                      | 25000                    | 781.25                                  | 3125.00                                | 25000                      | 100000                    |
| r6idn.4xlarge 1        | 12500                     | 25000                    | 1562.50                                 | 3125.00                                | 50000                      | 100000                    |
| r6idn.8xlarge 2        | 25000                     | 3125.0                   | 100000                                  |
| r6idn.12xlarge 2       | 37500                     | 4687.5                   | 150000                                  |
| r6idn.16xlarge 2       | 50000                     | 6250.0                   | 200000                                  |
| r6idn.24xlarge 2       | 75000                     | 9375.0                   | 300000                                  |
| r6idn.32xlarge 2       | 100000                    | 12500.0                  | 400000                                  |
| r6idn.metal 2          | 100000                    | 12500.0                  | 400000                                  |
| r6in.large 1           | 1562                      | 25000                    | 195.31                                  | 3125.00                                | 6250                       | 100000                    |
| r6in.xlarge 1          | 3125                      | 25000                    | 390.62                                  | 3125.00                                | 12500                      | 100000                    |
| r6in.2xlarge 1         | 6250                      | 25000                    | 781.25                                  | 3125.00                                | 25000                      | 100000                    |
| r6in.4xlarge 1         | 12500                     | 25000                    | 1562.50                                 | 3125.00                                | 50000                      | 100000                    |
| r6in.8xlarge 2         | 25000                     | 3125.0                   | 100000                                  |
| r6in.12xlarge 2        | 37500                     | 4687.5                   | 150000                                  |
| r6in.16xlarge 2        | 50000                     | 6250.0                   | 200000                                  |
| r6in.24xlarge 2        | 75000                     | 9375.0                   | 300000                                  |
| r6in.32xlarge 2        | 100000                    | 12500.0                  | 400000                                  |
| r6in.metal 2           | 100000                    | 12500.0                  | 400000                                  |
| r7a.medium 1           | 325                       | 10000                    | 40.62                                   | 1250.00                                | 2500                       | 40000                     |
| r7a.large 1            | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r7a.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r7a.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r7a.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r7a.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r7a.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r7a.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r7a.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r7a.32xlarge 2         | 40000                     | 5000.0                   | 160000                                  |
| r7a.48xlarge 2         | 40000                     | 5000.0                   | 240000                                  |
| r7a.metal-48xl 2       | 40000                     | 5000.0                   | 240000                                  |
| r7g.medium 1           | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| r7g.large 1            | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| r7g.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r7g.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r7g.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r7g.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r7g.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r7g.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r7g.metal 2            | 20000                     | 2500.0                   | 80000                                   |
| r7gd.medium 1          | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| r7gd.large 1           | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| r7gd.xlarge 1          | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r7gd.2xlarge 1         | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r7gd.4xlarge 1         | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r7gd.8xlarge 2         | 10000                     | 1250.0                   | 40000                                   |
| r7gd.12xlarge 2        | 15000                     | 1875.0                   | 60000                                   |
| r7gd.16xlarge 2        | 20000                     | 2500.0                   | 80000                                   |
| r7gd.metal 2           | 20000                     | 2500.0                   | 80000                                   |
| r7i.large 1            | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r7i.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r7i.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r7i.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r7i.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r7i.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r7i.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r7i.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r7i.48xlarge 2         | 40000                     | 5000.0                   | 240000                                  |
| r7i.metal-24xl 2       | 30000                     | 3750.0                   | 120000                                  |
| r7i.metal-48xl 2       | 40000                     | 5000.0                   | 240000                                  |
| r7iz.large 1           | 792                       | 10000                    | 99.00                                   | 1250.00                                | 3600                       | 40000                     |
| r7iz.xlarge 1          | 1584                      | 10000                    | 198.00                                  | 1250.00                                | 6667                       | 40000                     |
| r7iz.2xlarge 1         | 3168                      | 10000                    | 396.00                                  | 1250.00                                | 13333                      | 40000                     |
| r7iz.4xlarge 1         | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r7iz.8xlarge 2         | 10000                     | 1250.0                   | 40000                                   |
| r7iz.12xlarge 2        | 19000                     | 2375.0                   | 76000                                   |
| r7iz.16xlarge 2        | 20000                     | 2500.0                   | 80000                                   |
| r7iz.32xlarge 2        | 40000                     | 5000.0                   | 160000                                  |
| r7iz.metal-16xl 2      | 20000                     | 2500.0                   | 80000                                   |
| r7iz.metal-32xl 2      | 40000                     | 5000.0                   | 160000                                  |
| r8a.medium 1           | 325                       | 10000                    | 40.62                                   | 1250.00                                | 2500                       | 40000                     |
| r8a.large 1            | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r8a.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r8a.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r8a.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r8a.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r8a.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r8a.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r8a.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r8a.48xlarge 2         | 60000                     | 7500.0                   | 240000                                  |
| r8a.metal-24xl 2       | 30000                     | 3750.0                   | 120000                                  |
| r8a.metal-48xl 2       | 60000                     | 7500.0                   | 240000                                  |
| r8g.medium 1           | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| r8g.large 1            | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| r8g.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r8g.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r8g.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r8g.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r8g.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r8g.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r8g.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r8g.48xlarge 2         | 40000                     | 5000.0                   | 240000                                  |
| r8g.metal-24xl 2       | 30000                     | 3750.0                   | 120000                                  |
| r8g.metal-48xl 2       | 40000                     | 5000.0                   | 240000                                  |
| r8gb.medium 1          | 1562                      | 25000                    | 195.31                                  | 3125.00                                | 7500                       | 120000                    |
| r8gb.large 1           | 3125                      | 25000                    | 390.62                                  | 3125.00                                | 15000                      | 120000                    |
| r8gb.xlarge 1          | 6250                      | 25000                    | 781.25                                  | 3125.00                                | 30000                      | 120000                    |
| r8gb.2xlarge 1         | 12500                     | 25000                    | 1562.50                                 | 3125.00                                | 60000                      | 120000                    |
| r8gb.4xlarge 2         | 25000                     | 3125.0                   | 120000                                  |
| r8gb.8xlarge 2         | 50000                     | 6250.0                   | 240000                                  |
| r8gb.12xlarge 2        | 75000                     | 9375.0                   | 360000                                  |
| r8gb.16xlarge 2        | 100000                    | 12500.0                  | 480000                                  |
| r8gb.24xlarge 2        | 150000                    | 18750.0                  | 720000                                  |
| r8gb.metal-24xl 2      | 150000                    | 18750.0                  | 720000                                  |
| r8gd.medium 1          | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| r8gd.large 1           | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| r8gd.xlarge 1          | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r8gd.2xlarge 1         | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r8gd.4xlarge 1         | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r8gd.8xlarge 2         | 10000                     | 1250.0                   | 40000                                   |
| r8gd.12xlarge 2        | 15000                     | 1875.0                   | 60000                                   |
| r8gd.16xlarge 2        | 20000                     | 2500.0                   | 80000                                   |
| r8gd.24xlarge 2        | 30000                     | 3750.0                   | 120000                                  |
| r8gd.48xlarge 2        | 40000                     | 5000.0                   | 240000                                  |
| r8gd.metal-24xl 2      | 30000                     | 3750.0                   | 120000                                  |
| r8gd.metal-48xl 2      | 40000                     | 5000.0                   | 240000                                  |
| r8gn.medium 1          | 760                       | 10000                    | 95.00                                   | 1250.00                                | 2500                       | 40000                     |
| r8gn.large 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| r8gn.xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| r8gn.2xlarge 1         | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r8gn.4xlarge 2         | 10000                     | 1250.0                   | 40000                                   |
| r8gn.8xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r8gn.12xlarge 2        | 30000                     | 3750.0                   | 120000                                  |
| r8gn.16xlarge 2        | 40000                     | 5000.0                   | 160000                                  |
| r8gn.24xlarge 2        | 60000                     | 7500.0                   | 240000                                  |
| r8gn.48xlarge 2        | 60000                     | 7500.0                   | 240000                                  |
| r8gn.metal-24xl 2      | 60000                     | 7500.0                   | 240000                                  |
| r8gn.metal-48xl 2      | 60000                     | 7500.0                   | 240000                                  |
| r8i.large 1            | 650                       | 10000                    | 81.25                                   | 1250.00                                | 3600                       | 40000                     |
| r8i.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r8i.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r8i.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r8i.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| r8i.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| r8i.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| r8i.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| r8i.32xlarge 2         | 40000                     | 5000.0                   | 160000                                  |
| r8i.48xlarge 2         | 60000                     | 7500.0                   | 240000                                  |
| r8i.96xlarge 2         | 80000                     | 10000.0                  | 480000                                  |
| r8i.metal-48xl 2       | 60000                     | 7500.0                   | 240000                                  |
| r8i.metal-96xl 2       | 80000                     | 10000.0                  | 480000                                  |
| r8i-flex.large 1       | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| r8i-flex.xlarge 1      | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| r8i-flex.2xlarge 1     | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| r8i-flex.4xlarge 1     | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| r8i-flex.8xlarge 1     | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| r8i-flex.12xlarge 1    | 7500                      | 15000                    | 937.50                                  | 1875.00                                | 30000                      | 60000                     |
| r8i-flex.16xlarge 1    | 10000                     | 20000                    | 1250.00                                 | 2500.00                                | 40000                      | 80000                     |
| u-3tb1.56xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| u-6tb1.56xlarge 2      | 38000                     | 4750.0                   | 160000                                  |
| u-6tb1.112xlarge 2     | 38000                     | 4750.0                   | 160000                                  |
| u-6tb1.metal 2         | 38000                     | 4750.0                   | 160000                                  |
| u-9tb1.112xlarge 2     | 38000                     | 4750.0                   | 160000                                  |
| u-9tb1.metal 2         | 38000                     | 4750.0                   | 160000                                  |
| u-12tb1.112xlarge 2    | 38000                     | 4750.0                   | 160000                                  |
| u-12tb1.metal 2        | 38000                     | 4750.0                   | 160000                                  |
| u-18tb1.112xlarge 2    | 38000                     | 4750.0                   | 160000                                  |
| u-18tb1.metal 2        | 38000                     | 4750.0                   | 160000                                  |
| u-24tb1.112xlarge 2    | 38000                     | 4750.0                   | 160000                                  |
| u-24tb1.metal 2        | 38000                     | 4750.0                   | 160000                                  |
| u7i-6tb.112xlarge 2    | 100000                    | 12500.0                  | 560000                                  |
| u7i-8tb.112xlarge 2    | 100000                    | 12500.0                  | 560000                                  |
| u7i-12tb.224xlarge 2   | 100000                    | 12500.0                  | 560000                                  |
| u7in-16tb.224xlarge 2  | 100000                    | 12500.0                  | 560000                                  |
| u7in-24tb.224xlarge 2  | 100000                    | 12500.0                  | 560000                                  |
| u7in-32tb.224xlarge 2  | 100000                    | 12500.0                  | 560000                                  |
| u7inh-32tb.480xlarge 2 | 160000                    | 20000.0                  | 840000                                  |
| x1.16xlarge 2          | 7000                      | 875.0                    | 40000                                   |
| x1.32xlarge 2          | 14000                     | 1750.0                   | 80000                                   |
| x1e.xlarge 2           | 500                       | 62.5                     | 3700                                    |
| x1e.2xlarge 2          | 1000                      | 125.0                    | 7400                                    |
| x1e.4xlarge 2          | 1750                      | 218.75                   | 10000                                   |
| x1e.8xlarge 2          | 3500                      | 437.5                    | 20000                                   |
| x1e.16xlarge 2         | 7000                      | 875.0                    | 40000                                   |
| x1e.32xlarge 2         | 14000                     | 1750.0                   | 80000                                   |
| x2gd.medium 1          | 315                       | 4750                     | 39.38                                   | 593.75                                 | 2500                       | 20000                     |
| x2gd.large 1           | 630                       | 4750                     | 78.75                                   | 593.75                                 | 3600                       | 20000                     |
| x2gd.xlarge 1          | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| x2gd.2xlarge 1         | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| x2gd.4xlarge 2         | 4750                      | 593.75                   | 20000                                   |
| x2gd.8xlarge 2         | 9500                      | 1187.5                   | 40000                                   |
| x2gd.12xlarge 2        | 14250                     | 1781.25                  | 60000                                   |
| x2gd.16xlarge 2        | 19000                     | 2375.0                   | 80000                                   |
| x2gd.metal 2           | 19000                     | 2375.0                   | 80000                                   |
| x2idn.16xlarge 2       | 40000                     | 5000.0                   | 173333                                  |
| x2idn.24xlarge 2       | 60000                     | 7500.0                   | 260000                                  |
| x2idn.32xlarge 2       | 80000                     | 10000.0                  | 260000                                  |
| x2idn.metal 2          | 80000                     | 10000.0                  | 260000                                  |
| x2iedn.xlarge 1        | 2500                      | 20000                    | 312.50                                  | 2500.00                                | 8125                       | 65000                     |
| x2iedn.2xlarge 1       | 5000                      | 20000                    | 625.00                                  | 2500.00                                | 16250                      | 65000                     |
| x2iedn.4xlarge 1       | 10000                     | 20000                    | 1250.00                                 | 2500.00                                | 32500                      | 65000                     |
| x2iedn.8xlarge 2       | 20000                     | 2500.0                   | 65000                                   |
| x2iedn.16xlarge 2      | 40000                     | 5000.0                   | 130000                                  |
| x2iedn.24xlarge 2      | 60000                     | 7500.0                   | 195000                                  |
| x2iedn.32xlarge 2      | 80000                     | 10000.0                  | 260000                                  |
| x2iedn.metal 2         | 80000                     | 10000.0                  | 260000                                  |
| x2iezn.2xlarge 2       | 3170                      | 396.25                   | 13333                                   |
| x2iezn.4xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| x2iezn.6xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| x2iezn.8xlarge 2       | 12000                     | 1500.0                   | 55000                                   |
| x2iezn.12xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| x2iezn.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| x8g.medium 1           | 315                       | 10000                    | 39.38                                   | 1250.00                                | 2500                       | 40000                     |
| x8g.large 1            | 630                       | 10000                    | 78.75                                   | 1250.00                                | 3600                       | 40000                     |
| x8g.xlarge 1           | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| x8g.2xlarge 1          | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 12000                      | 40000                     |
| x8g.4xlarge 1          | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| x8g.8xlarge 2          | 10000                     | 1250.0                   | 40000                                   |
| x8g.12xlarge 2         | 15000                     | 1875.0                   | 60000                                   |
| x8g.16xlarge 2         | 20000                     | 2500.0                   | 80000                                   |
| x8g.24xlarge 2         | 30000                     | 3750.0                   | 120000                                  |
| x8g.48xlarge 2         | 40000                     | 5000.0                   | 240000                                  |
| x8g.metal-24xl 2       | 30000                     | 3750.0                   | 120000                                  |
| x8g.metal-48xl 2       | 40000                     | 5000.0                   | 240000                                  |
| z1d.large 1            | 800                       | 3170                     | 100.00                                  | 396.25                                 | 3333                       | 13333                     |
| z1d.xlarge 1           | 1580                      | 3170                     | 197.50                                  | 396.25                                 | 6667                       | 13333                     |
| z1d.2xlarge 2          | 3170                      | 396.25                   | 13333                                   |
| z1d.3xlarge 2          | 4750                      | 593.75                   | 20000                                   |
| z1d.6xlarge 2          | 9500                      | 1187.5                   | 40000                                   |
| z1d.12xlarge 2         | 19000                     | 2375.0                   | 80000                                   |
| z1d.metal 2            | 19000                     | 2375.0                   | 80000                                   |

1 These instances can sustain the maximum performance for 30 minutes
at least once every 24 hours, after which they revert to their baseline performance.

2 These instances can sustain their stated performance indefinitely.
If your workload requires sustained maximum performance for longer than 30 minutes, use one of
these instances.

### Storage optimized

| Instance size     | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| ----------------- | ------------------------- | ------------------------ | --------------------------------------- | -------------------------------------- | -------------------------- | ------------------------- |
| d2.xlarge 2       | 750                       | 93.75                    | 6000                                    |
| d2.2xlarge 2      | 1000                      | 125.0                    | 8000                                    |
| d2.4xlarge 2      | 2000                      | 250.0                    | 16000                                   |
| d2.8xlarge 2      | 4000                      | 500.0                    | 32000                                   |
| d3.xlarge 1       | 850                       | 2800                     | 106.25                                  | 350.00                                 | 5000                       | 15000                     |
| d3.2xlarge 1      | 1700                      | 2800                     | 212.50                                  | 350.00                                 | 10000                      | 15000                     |
| d3.4xlarge 2      | 2800                      | 350.0                    | 15000                                   |
| d3.8xlarge 2      | 5000                      | 625.0                    | 30000                                   |
| d3en.xlarge 1     | 850                       | 2800                     | 106.25                                  | 350.00                                 | 5000                       | 15000                     |
| d3en.2xlarge 1    | 1700                      | 2800                     | 212.50                                  | 350.00                                 | 10000                      | 15000                     |
| d3en.4xlarge 2    | 2800                      | 350.0                    | 15000                                   |
| d3en.6xlarge 2    | 4000                      | 500.0                    | 25000                                   |
| d3en.8xlarge 2    | 5000                      | 625.0                    | 30000                                   |
| d3en.12xlarge 2   | 7000                      | 875.0                    | 40000                                   |
| h1.2xlarge 2      | 1750                      | 218.75                   | 12000                                   |
| h1.4xlarge 2      | 3500                      | 437.5                    | 20000                                   |
| h1.8xlarge 2      | 7000                      | 875.0                    | 40000                                   |
| h1.16xlarge 2     | 14000                     | 1750.0                   | 80000                                   |
| i3.large 2        | 425                       | 53.125                   | 3000                                    |
| i3.xlarge 2       | 850                       | 106.25                   | 6000                                    |
| i3.2xlarge 2      | 1700                      | 212.5                    | 12000                                   |
| i3.4xlarge 2      | 3500                      | 437.5                    | 16000                                   |
| i3.8xlarge 2      | 7000                      | 875.0                    | 32500                                   |
| i3.16xlarge 2     | 14000                     | 1750.0                   | 65000                                   |
| i3.metal 2        | 19000                     | 2375.0                   | 80000                                   |
| i3en.large 1      | 576                       | 4750                     | 72.10                                   | 593.75                                 | 3000                       | 20000                     |
| i3en.xlarge 1     | 1153                      | 4750                     | 144.20                                  | 593.75                                 | 6000                       | 20000                     |
| i3en.2xlarge 1    | 2307                      | 4750                     | 288.39                                  | 593.75                                 | 12000                      | 20000                     |
| i3en.3xlarge 1    | 3800                      | 4750                     | 475.00                                  | 593.75                                 | 15000                      | 20000                     |
| i3en.6xlarge 2    | 4750                      | 593.75                   | 20000                                   |
| i3en.12xlarge 2   | 9500                      | 1187.5                   | 40000                                   |
| i3en.24xlarge 2   | 19000                     | 2375.0                   | 80000                                   |
| i3en.metal 2      | 19000                     | 2375.0                   | 80000                                   |
| i4g.large 1       | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| i4g.xlarge 1      | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| i4g.2xlarge 1     | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| i4g.4xlarge 1     | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| i4g.8xlarge 2     | 10000                     | 1250.0                   | 40000                                   |
| i4g.16xlarge 2    | 20000                     | 2500.0                   | 80000                                   |
| i4i.large 1       | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| i4i.xlarge 1      | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| i4i.2xlarge 1     | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| i4i.4xlarge 1     | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| i4i.8xlarge 2     | 10000                     | 1250.0                   | 40000                                   |
| i4i.12xlarge 2    | 15000                     | 1875.0                   | 60000                                   |
| i4i.16xlarge 2    | 20000                     | 2500.0                   | 80000                                   |
| i4i.24xlarge 2    | 30000                     | 3750.0                   | 120000                                  |
| i4i.32xlarge 2    | 40000                     | 5000.0                   | 160000                                  |
| i4i.metal 2       | 40000                     | 5000.0                   | 160000                                  |
| i7i.large 1       | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| i7i.xlarge 1      | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| i7i.2xlarge 1     | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| i7i.4xlarge 1     | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| i7i.8xlarge 2     | 10000                     | 1250.0                   | 40000                                   |
| i7i.12xlarge 2    | 15000                     | 1875.0                   | 60000                                   |
| i7i.16xlarge 2    | 20000                     | 2500.0                   | 80000                                   |
| i7i.24xlarge 2    | 30000                     | 3750.0                   | 120000                                  |
| i7i.48xlarge 2    | 60000                     | 7500.0                   | 240000                                  |
| i7i.metal-24xl 2  | 30000                     | 3750.0                   | 120000                                  |
| i7i.metal-48xl 2  | 60000                     | 7500.0                   | 240000                                  |
| i7ie.large 1      | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| i7ie.xlarge 1     | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| i7ie.2xlarge 1    | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| i7ie.3xlarge 1    | 3750                      | 10000                    | 468.75                                  | 1250.00                                | 15000                      | 40000                     |
| i7ie.6xlarge 1    | 7500                      | 10000                    | 937.50                                  | 1250.00                                | 30000                      | 40000                     |
| i7ie.12xlarge 2   | 15000                     | 1875.0                   | 60000                                   |
| i7ie.18xlarge 2   | 22500                     | 2812.5                   | 90000                                   |
| i7ie.24xlarge 2   | 30000                     | 3750.0                   | 120000                                  |
| i7ie.48xlarge 2   | 60000                     | 7500.0                   | 240000                                  |
| i7ie.metal-24xl 2 | 30000                     | 3750.0                   | 120000                                  |
| i7ie.metal-48xl 2 | 60000                     | 7500.0                   | 240000                                  |
| i8g.large 1       | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| i8g.xlarge 1      | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| i8g.2xlarge 1     | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| i8g.4xlarge 1     | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| i8g.8xlarge 2     | 10000                     | 1250.0                   | 40000                                   |
| i8g.12xlarge 2    | 15000                     | 1875.0                   | 60000                                   |
| i8g.16xlarge 2    | 20000                     | 2500.0                   | 80000                                   |
| i8g.24xlarge 2    | 30000                     | 3750.0                   | 120000                                  |
| i8g.48xlarge 2    | 60000                     | 7500.0                   | 240000                                  |
| i8g.metal-24xl 2  | 30000                     | 3750.0                   | 120000                                  |
| i8ge.large 1      | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| i8ge.xlarge 1     | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| i8ge.2xlarge 1    | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| i8ge.3xlarge 1    | 3750                      | 10000                    | 468.75                                  | 1250.00                                | 15000                      | 40000                     |
| i8ge.6xlarge 1    | 7500                      | 10000                    | 937.50                                  | 1250.00                                | 30000                      | 40000                     |
| i8ge.12xlarge 2   | 15000                     | 1875.0                   | 60000                                   |
| i8ge.18xlarge 2   | 22500                     | 2812.5                   | 90000                                   |
| i8ge.24xlarge 2   | 30000                     | 3750.0                   | 120000                                  |
| i8ge.48xlarge 2   | 60000                     | 7500.0                   | 240000                                  |
| i8ge.metal-24xl 2 | 30000                     | 3750.0                   | 120000                                  |
| i8ge.metal-48xl 2 | 60000                     | 7500.0                   | 240000                                  |
| im4gn.large 1     | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| im4gn.xlarge 1    | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| im4gn.2xlarge 1   | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| im4gn.4xlarge 2   | 10000                     | 1250.0                   | 40000                                   |
| im4gn.8xlarge 2   | 20000                     | 2500.0                   | 80000                                   |
| im4gn.16xlarge 2  | 40000                     | 5000.0                   | 160000                                  |
| is4gen.medium 1   | 625                       | 10000                    | 78.12                                   | 1250.00                                | 2500                       | 40000                     |
| is4gen.large 1    | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 5000                       | 40000                     |
| is4gen.xlarge 1   | 2500                      | 10000                    | 312.50                                  | 1250.00                                | 10000                      | 40000                     |
| is4gen.2xlarge 1  | 5000                      | 10000                    | 625.00                                  | 1250.00                                | 20000                      | 40000                     |
| is4gen.4xlarge 2  | 10000                     | 1250.0                   | 40000                                   |
| is4gen.8xlarge 2  | 20000                     | 2500.0                   | 80000                                   |

1 These instances can sustain the maximum performance for 30 minutes
at least once every 24 hours, after which they revert to their baseline performance.

2 These instances can sustain their stated performance indefinitely.
If your workload requires sustained maximum performance for longer than 30 minutes, use one of
these instances.

### Accelerated computing

| Instance size        | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| -------------------- | ------------------------- | ------------------------ | --------------------------------------- | -------------------------------------- | -------------------------- | ------------------------- |
| dl1.24xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| dl2q.24xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| f1.2xlarge 2         | 1700                      | 212.5                    | 12000                                   |
| f1.4xlarge 2         | 3500                      | 437.5                    | 44000                                   |
| f1.16xlarge 2        | 14000                     | 1750.0                   | 75000                                   |
| f2.6xlarge 2         | 7500                      | 937.5                    | 30000                                   |
| f2.12xlarge 2        | 15000                     | 1875.0                   | 60000                                   |
| f2.48xlarge 2        | 60000                     | 7500.0                   | 240000                                  |
| g3.4xlarge 2         | 3500                      | 437.5                    | 20000                                   |
| g3.8xlarge 2         | 7000                      | 875.0                    | 40000                                   |
| g3.16xlarge 2        | 14000                     | 1750.0                   | 80000                                   |
| g4ad.xlarge 1        | 400                       | 3170                     | 50.00                                   | 396.25                                 | 1700                       | 13333                     |
| g4ad.2xlarge 1       | 800                       | 3170                     | 100.00                                  | 396.25                                 | 3400                       | 13333                     |
| g4ad.4xlarge 1       | 1580                      | 3170                     | 197.50                                  | 396.25                                 | 6700                       | 13333                     |
| g4ad.8xlarge 2       | 3170                      | 396.25                   | 13333                                   |
| g4ad.16xlarge 2      | 6300                      | 787.5                    | 26667                                   |
| g4dn.xlarge 1        | 950                       | 3500                     | 118.75                                  | 437.50                                 | 3000                       | 20000                     |
| g4dn.2xlarge 1       | 1150                      | 3500                     | 143.75                                  | 437.50                                 | 6000                       | 20000                     |
| g4dn.4xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| g4dn.8xlarge 2       | 9500                      | 1187.5                   | 40000                                   |
| g4dn.12xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| g4dn.16xlarge 2      | 9500                      | 1187.5                   | 40000                                   |
| g4dn.metal 2         | 19000                     | 2375.0                   | 80000                                   |
| g5.xlarge 1          | 700                       | 3500                     | 87.50                                   | 437.50                                 | 3000                       | 15000                     |
| g5.2xlarge 1         | 850                       | 3500                     | 106.25                                  | 437.50                                 | 3500                       | 15000                     |
| g5.4xlarge 2         | 4750                      | 593.75                   | 20000                                   |
| g5.8xlarge 2         | 16000                     | 2000.0                   | 65000                                   |
| g5.12xlarge 2        | 16000                     | 2000.0                   | 65000                                   |
| g5.16xlarge 2        | 16000                     | 2000.0                   | 65000                                   |
| g5.24xlarge 2        | 19000                     | 2375.0                   | 80000                                   |
| g5.48xlarge 2        | 19000                     | 2375.0                   | 80000                                   |
| g5g.xlarge 1         | 1188                      | 4750                     | 148.50                                  | 593.75                                 | 6000                       | 20000                     |
| g5g.2xlarge 1        | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 12000                      | 20000                     |
| g5g.4xlarge 2        | 4750                      | 593.75                   | 20000                                   |
| g5g.8xlarge 2        | 9500                      | 1187.5                   | 40000                                   |
| g5g.16xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| g5g.metal 2          | 19000                     | 2375.0                   | 80000                                   |
| g6.xlarge 1          | 1000                      | 5000                     | 125.00                                  | 625.00                                 | 4000                       | 20000                     |
| g6.2xlarge 1         | 2000                      | 5000                     | 250.00                                  | 625.00                                 | 8000                       | 20000                     |
| g6.4xlarge 2         | 8000                      | 1000.0                   | 32000                                   |
| g6.8xlarge 2         | 16000                     | 2000.0                   | 64000                                   |
| g6.12xlarge 2        | 20000                     | 2500.0                   | 80000                                   |
| g6.16xlarge 2        | 20000                     | 2500.0                   | 80000                                   |
| g6.24xlarge 2        | 30000                     | 3750.0                   | 120000                                  |
| g6.48xlarge 2        | 60000                     | 7500.0                   | 240000                                  |
| g6e.xlarge 1         | 1000                      | 5000                     | 125.00                                  | 625.00                                 | 4000                       | 20000                     |
| g6e.2xlarge 1        | 2000                      | 5000                     | 250.00                                  | 625.00                                 | 8000                       | 20000                     |
| g6e.4xlarge 2        | 8000                      | 1000.0                   | 32000                                   |
| g6e.8xlarge 2        | 16000                     | 2000.0                   | 64000                                   |
| g6e.12xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| g6e.16xlarge 2       | 20000                     | 2500.0                   | 80000                                   |
| g6e.24xlarge 2       | 30000                     | 3750.0                   | 120000                                  |
| g6e.48xlarge 2       | 60000                     | 7500.0                   | 240000                                  |
| g6f.large 1          | 936                       | 5000                     | 117.00                                  | 625.00                                 | 3750                       | 20000                     |
| g6f.xlarge 1         | 1000                      | 5000                     | 125.00                                  | 625.00                                 | 4000                       | 20000                     |
| g6f.2xlarge 1        | 2000                      | 5000                     | 250.00                                  | 625.00                                 | 8000                       | 20000                     |
| g6f.4xlarge 2        | 6000                      | 750.0                    | 24000                                   |
| gr6.4xlarge 2        | 8000                      | 1000.0                   | 32000                                   |
| gr6.8xlarge 2        | 16000                     | 2000.0                   | 64000                                   |
| gr6f.4xlarge 2       | 8000                      | 1000.0                   | 32000                                   |
| inf1.xlarge 1        | 1190                      | 4750                     | 148.75                                  | 593.75                                 | 4000                       | 20000                     |
| inf1.2xlarge 1       | 1190                      | 4750                     | 148.75                                  | 593.75                                 | 6000                       | 20000                     |
| inf1.6xlarge 2       | 4750                      | 593.75                   | 20000                                   |
| inf1.24xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| inf2.xlarge 1        | 1250                      | 10000                    | 156.25                                  | 1250.00                                | 6000                       | 40000                     |
| inf2.8xlarge 2       | 10000                     | 1250.0                   | 40000                                   |
| inf2.24xlarge 2      | 30000                     | 3750.0                   | 120000                                  |
| inf2.48xlarge 2      | 60000                     | 7500.0                   | 240000                                  |
| p3.2xlarge 2         | 1750                      | 218.75                   | 10000                                   |
| p3.8xlarge 2         | 7000                      | 875.0                    | 40000                                   |
| p3.16xlarge 2        | 14000                     | 1750.0                   | 80000                                   |
| p3dn.24xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| p4d.24xlarge 2       | 19000                     | 2375.0                   | 80000                                   |
| p4de.24xlarge 2      | 19000                     | 2375.0                   | 80000                                   |
| p5.4xlarge 2         | 10000                     | 1250.0                   | 32500                                   |
| p5.48xlarge 2        | 80000                     | 10000.0                  | 260000                                  |
| p5e.48xlarge 2       | 80000                     | 10000.0                  | 260000                                  |
| p5en.48xlarge 2      | 100000                    | 12500.0                  | 400000                                  |
| p6-b200.48xlarge 2   | 100000                    | 12500.0                  | 400000                                  |
| p6-b300.48xlarge 2   | 100000                    | 12500.0                  | 400000                                  |
| p6e-gb200.36xlarge 2 | 60000                     | 7500.0                   | 240000                                  |
| trn1.2xlarge 1       | 5000                      | 20000                    | 625.00                                  | 2500.00                                | 16250                      | 65000                     |
| trn1.32xlarge 2      | 80000                     | 10000.0                  | 260000                                  |
| trn1n.32xlarge 2     | 80000                     | 10000.0                  | 260000                                  |
| trn2.48xlarge 2      | 80000                     | 10000.0                  | 260000                                  |
| trn2u.48xlarge 2     | 80000                     | 10000.0                  | 260000                                  |
| vt1.3xlarge 1        | 2375                      | 4750                     | 296.88                                  | 593.75                                 | 10000                      | 20000                     |
| vt1.6xlarge 2        | 4750                      | 593.75                   | 20000                                   |
| vt1.24xlarge 2       | 19000                     | 2375.0                   | 80000                                   |

1 These instances can sustain the maximum performance for 30 minutes
at least once every 24 hours, after which they revert to their baseline performance.

2 These instances can sustain their stated performance indefinitely.
If your workload requires sustained maximum performance for longer than 30 minutes, use one of
these instances.

### High-performance computing

| Instance size     | Baseline bandwidth (Mbps) | Maximum bandwidth (Mbps) | Baseline throughput (MB/s, 128 KiB I/O) | Maximum throughput (MB/s, 128 KiB I/O) | Baseline IOPS (16 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| ----------------- | ------------------------- | ------------------------ | --------------------------------------- | -------------------------------------- | -------------------------- | ------------------------- |
| hpc6a.48xlarge 1  | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc6id.32xlarge 1 | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7a.12xlarge 1  | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7a.24xlarge 1  | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7a.48xlarge 1  | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7a.96xlarge 1  | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7g.4xlarge 1   | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7g.8xlarge 1   | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |
| hpc7g.16xlarge 1  | 87                        | 2085                     | 10.88                                   | 260.62                                 | 500                        | 11000                     |

1 These instances can sustain the maximum performance for 30 minutes
at least once every 24 hours, after which they revert to their baseline performance.

2 These instances can sustain their stated performance indefinitely.
If your workload requires sustained maximum performance for longer than 30 minutes, use one of
these instances.

## EBS optimization supported

The following instance types support EBS optimization but EBS optimization is not
enabled by default. You must enable EBS optimization, at an [additional hourly fee](https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances "https://aws.amazon.com/ec2/previous-generation/#EBS-optimized_instances"),
during or after launch to achieve the level of EBS performance described.

| Instance size | Maximum bandwidth (Mbps) | Maximum throughput (MB/s, 128 KiB I/O) | Maximum IOPS (16 KiB I/O) |
| ------------- | ------------------------ | -------------------------------------- | ------------------------- |
| c1.xlarge     | 1000                     | 125.0                                  | 8000                      |
| c3.xlarge     | 500                      | 62.5                                   | 4000                      |
| c3.2xlarge    | 1000                     | 125.0                                  | 8000                      |
| c3.4xlarge    | 2000                     | 250.0                                  | 16000                     |
| i2.xlarge     | 500                      | 62.5                                   | 4000                      |
| i2.2xlarge    | 1000                     | 125.0                                  | 8000                      |
| i2.4xlarge    | 2000                     | 250.0                                  | 16000                     |
| m1.large      | 500                      | 62.5                                   | 4000                      |
| m1.xlarge     | 1000                     | 125.0                                  | 8000                      |
| m2.2xlarge    | 500                      | 62.5                                   | 4000                      |
| m2.4xlarge    | 1000                     | 125.0                                  | 8000                      |
| m3.xlarge     | 500                      | 62.5                                   | 4000                      |
| m3.2xlarge    | 1000                     | 125.0                                  | 8000                      |
| r3.xlarge     | 500                      | 62.5                                   | 4000                      |
| r3.2xlarge    | 1000                     | 125.0                                  | 8000                      |
| r3.4xlarge    | 2000                     | 250.0                                  | 16000                     |

###### Note

The `i2.8xlarge`, `c3.8xlarge`, and `r3.8xlarge`
instances do not have dedicated EBS bandwidth and therefore do not offer EBS optimization.
On these instances, network traffic and Amazon EBS traffic share the same 10-gigabit network
interface.
