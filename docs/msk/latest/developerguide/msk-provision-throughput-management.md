# Manage storage throughput for Standard brokers in a Amazon MSK cluster

For information on how to provision throughput using the Amazon MSK console, CLI, and API, see [Provision storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput.md "msk-provision-throughput.md").

###### Topics

- [Amazon MSK broker throughput
  bottlenecks and maximum throughput settings](#throughput-bottlenecks "#throughput-bottlenecks")
- [Measure storage throughput of a Amazon MSK cluster](#throughput-metrics "#throughput-metrics")
- [Configuration update values for provisioned storage in a Amazon MSK cluster](#provisioned-throughput-config "#provisioned-throughput-config")
- [Provision storage throughput for Standard brokers in a Amazon MSK cluster](msk-provision-throughput.md "msk-provision-throughput.md")

## Amazon MSK broker throughput

bottlenecks and maximum throughput settings

There are multiple causes of bottlenecks in broker throughput: volume throughput,
Amazon EC2 to Amazon EBS network throughput, and Amazon EC2 egress throughput. You can enable
provisioned storage throughput to adjust volume throughput. However, broker
throughput limitations can be caused by Amazon EC2 to Amazon EBS network throughput and Amazon EC2
egress throughput.

Amazon EC2 egress throughput is impacted by the number of consumer groups and consumers
per consumer groups. Also, both Amazon EC2 to Amazon EBS network throughput and Amazon EC2
egress throughput are higher for larger broker sizes.

For volume sizes of 10 GiB or larger, you can provision storage throughput of 250
MiB per second or greater. 250 MiB per second is the default. To provision
storage throughput, you must choose broker size kafka.m5.4xlarge or larger (or
kafka.m7g.2xlarge or larger), and you can specify maximum throughput as shown in
the following table.

| broker size        | Maximum storage throughput (MiB/second) |
| ------------------ | --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| kafka.m5.4xlarge   | 593                                     |
| kafka.m5.8xlarge   | 850                                     |
| kafka.m5.12xlarge  | 1000                                    |
| kafka.m5.16xlarge  | 1000                                    |
| kafka.m5.24xlarge  | 1000                                    |
| kafka.m7g.2xlarge  | 312.5                                   |
| kafka.m7g.4xlarge  | 625                                     |
| kafka.m7g.8xlarge  | 1000                                    |
| kafka.m7g.12xlarge | 1000                                    |
| kafka.m7g.16xlarge | 1000                                    | ## Measure storage throughput of a Amazon MSK cluster You can use the `VolumeReadBytes` and `VolumeWriteBytes` metrics to measure the average storage throughput of a cluster. The sum of these two metrics gives the average storage throughput in bytes. To get the average storage throughput for a cluster, set these two metrics to SUM and the period to 1 minute, then use the following formula. `Average storage throughput in MiB/s = (Sum(VolumeReadBytes) + Sum(VolumeWriteBytes)) / (60 * 1024 * 1024)` For information about the `VolumeReadBytes` and `VolumeWriteBytes` metrics, see [PER_BROKER Level monitoring](metrics-details.md#broker-metrics "metrics-details.md#broker-metrics"). ## Configuration update values for provisioned storage in a Amazon MSK cluster You can update your Amazon MSK configuration either before or after you turn on provisioned throughput. However, you won't see the desired throughput until you perform both actions: update the `num.replica.fetchers` configuration parameter and turn on provisioned throughput. In the default Amazon MSK configuration, `num.replica.fetchers` has a value of 2. To update your `num.replica.fetchers`, you can use the suggested values from the following table. These values are for guidance purposes. We recommend that you adjust these values based on your use case. |
| broker size        | num.replica.fetchers                    |
| ---                | ---                                     |
| kafka.m5.4xlarge   | 4                                       |
| kafka.m5.8xlarge   | 8                                       |
| kafka.m5.12xlarge  | 14                                      |
| kafka.m5.16xlarge  | 16                                      |
| kafka.m5.24xlarge  | 16                                      | Your updated configuration may not take effect for up to 24 hours, and may take longer when a source volume is not fully utilized. However, transitional volume performance at least equals the performance of source storage volumes during the migration period. A fully-utilized 1 TiB volume typically takes about six hours to migrate to an updated configuration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
