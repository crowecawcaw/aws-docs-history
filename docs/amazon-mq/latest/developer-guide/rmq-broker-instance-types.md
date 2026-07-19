# Amazon MQ for RabbitMQ broker instance types

The combined description of the broker instance class (m7g) and size (large, medium) is called the broker instance type (for example, mq.m7g.large).

We recommend using mq.m7g instance types for both cluster and single-instance deployments.

Amazon MQ provides at least a 90 day notice before an instance type reaches end of support. We recommend upgrading your broker to a new instance type before the end-of-support date to prevent any disruptions.

###### Important

The `mq.t3.micro` instance type is deprecated and is no longer available
for new broker creation. Existing brokers using `mq.t3.micro` are not affected,
but we recommend upgrading to `mq.m5.large` or `mq.m7g.medium` or higher.

You cannot downgrade a broker from an `mq.m7g` or `mq.m5` instance type to a `mq.t3.micro` instance type.

The `mq.t3.micro` instance type does not support cluster deployment.

## Instance types for m7g cluster deployment

We recommending using `mq.m7g.x` instance types with cluster deployment.
The following table shows the available `mq.m7g.x` instance types for cluster deployment.

| Instance Type   | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use | Storage | Disk volume size per node(GB) | Max configurable storage (GB) |
| --------------- | ---- | ------------ | ----------------------------------------- | --------------- | ------- | ----------------------------- | ----------------------------- |
| mq.m7g.medium   | 1    | 4            | 0.52 / 12.5                               | Evaluation      | EBS     | 5                             | 25                            |
| mq.m7g.large    | 2    | 8            | 0.937 / 12.5                              | Production      | EBS     | 15                            | 75                            |
| mq.m7g.xlarge   | 4    | 16           | 1.876 / 12.5                              | Production      | EBS     | 25                            | 125                           |
| mq.m7g.2xlarge  | 8    | 32           | 3.75 / 15.0                               | Production      | EBS     | 45                            | 180                           |
| mq.m7g.4xlarge  | 16   | 64           | 7.5 / 15.0                                | Production      | EBS     | 90                            | 250                           |
| mq.m7g.8xlarge  | 32   | 128          | 15 Gigabit                                | Production      | EBS     | 175                           | 400                           |
| mq.m7g.12xlarge | 48   | 192          | 22.5 Gigabit                              | Production      | EBS     | 260                           | 500                           |
| mq.m7g.16xlarge | 64   | 256          | 30 Gigabit                                | Production      | EBS     | 345                           | 500                           |

###### Note

Configurable storage size is available for RabbitMQ version 4.x brokers with `CLUSTER_MULTI_AZ` deployment mode only. The storage size must be a multiple of 5 GB. If not specified, the broker uses the default storage size shown in the "Disk volume size per node" column. You can configure storage size when creating or updating a broker. For more information, see the [CreateBroker](../api-reference/rest-api-brokers.md "../api-reference/rest-api-brokers.md") and [UpdateBroker](../api-reference/rest-api-broker.md "../api-reference/rest-api-broker.md") API operations.

## Instance types for m7g single instance deployment

The following table shows the available `mq.m7g.x` instance types
for single instance deployment.

| Instance Type   | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use | Storage | Disk volume size per node(GB) |
| --------------- | ---- | ------------ | ----------------------------------------- | --------------- | ------- | ----------------------------- |
| mq.m7g.medium   | 1    | 4            | 0.52 / 12.5                               | Evaluation      | EBS     | 200                           |
| mq.m7g.large    | 2    | 8            | 0.937 / 12.5                              | Production      | EBS     | 200                           |
| mq.m7g.xlarge   | 4    | 16           | 1.876 / 12.5                              | Production      | EBS     | 200                           |
| mq.m7g.2xlarge  | 8    | 32           | 3.75 / 15.0                               | Production      | EBS     | 200                           |
| mq.m7g.4xlarge  | 16   | 64           | 7.5 / 15.0                                | Production      | EBS     | 200                           |
| mq.m7g.8xlarge  | 32   | 128          | 15 Gigabit                                | Production      | EBS     | 200                           |
| mq.m7g.12xlarge | 48   | 192          | 22.5 Gigabit                              | Production      | EBS     | 200                           |
| mq.m7g.16xlarge | 64   | 256          | 39 Gigabit                                | Production      | EBS     | 200                           |

## Instance types for `mq.m5` single instance deployment

The following tables show the available `mq.m5.x` instance types for single instance deployment

| Instance Type            | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use                                     | Storage | Disk volume size per node(GB) |
| ------------------------ | ---- | ------------ | ----------------------------------------- | --------------------------------------------------- | ------- | ----------------------------- |
| mq.t3.micro (deprecated) | 2    | 1            | 0.064 / 5.0                               | Evaluation<br>• no longer available for new brokers | EBS     | 20                            |
| mq.m5.large              | 2    | 8            | 0.75 / 10.0                               | Production                                          | EBS     | 200                           |
| mq.m5.xlarge             | 4    | 16           | 1.25 / 10.0                               | Production                                          | EBS     | 200                           |
| mq.m5.2xlarge            | 8    | 32           | 2.5 / 10.0                                | Production                                          | EBS     | 200                           |
| mq.m5.4xlarge            | 16   | 64           | 5.0 / 10.0                                | Production                                          | EBS     | 200                           |

## Instance types for `mq.m5` cluster deployment

The following tables show the available `mq.m5.x` instance types for cluster deployment

| Instance Type | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use | Storage | Disk volume size per node(GB) |
| ------------- | ---- | ------------ | ----------------------------------------- | --------------- | ------- | ----------------------------- |
| mq.m5.large   | 2    | 8            | 0.75 / 10.0                               | Production      | EBS     | 200                           |
| mq.m5.xlarge  | 4    | 16           | 1.25 / 10.0                               | Production      | EBS     | 200                           |
| mq.m5.2xlarge | 8    | 32           | 2.5 / 10.0                                | Production      | EBS     | 200                           |
| mq.m5.4xlarge | 16   | 64           | 5.0 / 10.0                                | Production      | EBS     | 200                           |

## Memory and disk alarms

Amazon MQ configures memory and disk thresholds on each RabbitMQ broker to protect
against resource exhaustion. When a threshold is exceeded, RabbitMQ triggers an
[alarm](https://www.rabbitmq.com/docs/alarms "https://www.rabbitmq.com/docs/alarms")
and blocks publishers from sending messages. Consumers on separate connections
continue to operate normally. However, if a publisher and consumer share the same
connection, the consumer is also blocked.

###### Important

Amazon MQ manages these thresholds and you cannot modify them. When the alarm
condition clears, publishers are unblocked automatically. For troubleshooting
information, see
[Amazon MQ for RabbitMQ: High memory alarm](troubleshooting-action-required-codes-rabbitmq-memory-alarm.md "troubleshooting-action-required-codes-rabbitmq-memory-alarm.md") and
[RabbitMQ on Amazon MQ: Disk limit alarm](troubleshooting-action-required-codes-disk-limit-alarm.md "troubleshooting-action-required-codes-disk-limit-alarm.md").

### Memory alarm

The `vm_memory_high_watermark` parameter defines the maximum amount
of memory that a RabbitMQ broker can use before it blocks publishers from sending
messages. When memory usage exceeds this threshold, RabbitMQ triggers a memory
alarm. For more information, see
[Memory Alarms](https://www.rabbitmq.com/docs/memory "https://www.rabbitmq.com/docs/memory") on the
RabbitMQ website.

For `mq.m7g` instance types, Amazon MQ sets the following absolute memory
high watermark values:

| Instance Type   | Memory High Watermark (GiB) |
| --------------- | --------------------------- |
| mq.m7g.medium   | 1.8                         |
| mq.m7g.large    | 4.3                         |
| mq.m7g.xlarge   | 9.3                         |
| mq.m7g.2xlarge  | 19.3                        |
| mq.m7g.4xlarge  | 39.4                        |
| mq.m7g.8xlarge  | 79.7                        |
| mq.m7g.12xlarge | 119.8                       |
| mq.m7g.16xlarge | 160.1                       |

For `mq.m5` instance types, Amazon MQ sets a relative memory high
watermark of 0.4 (40% of the available memory).

The higher memory thresholds on `mq.m7g` instances allow RabbitMQ to use
more available memory before triggering an alarm. For more information about
performance improvements with `mq.m7g` instances, see
[Improve
RabbitMQ performance on Amazon MQ with AWS Graviton3-based M7g instances](https://aws.amazon.com/blogs/big-data/improve-rabbitmq-performance-on-amazon-mq-with-aws-graviton3-based-m7g-instances/ "https://aws.amazon.com/blogs/big-data/improve-rabbitmq-performance-on-amazon-mq-with-aws-graviton3-based-m7g-instances/")
on the AWS Blog.

### Disk alarm

The `disk_free_limit` parameter defines the minimum amount of free
disk space that a RabbitMQ node requires. When free disk space on any node drops
below this limit, RabbitMQ triggers a disk alarm and blocks publishers from
sending messages. For more information, see
[Disk
Alarms](https://www.rabbitmq.com/docs/disk-alarms "https://www.rabbitmq.com/docs/disk-alarms") on the RabbitMQ website.

For `mq.m7g` instance types, Amazon MQ sets the following disk free
limits. Single-instance brokers have a higher disk free limit to provide
additional protection because they do not have other nodes to serve traffic
if disk space is exhausted.

| Deployment Mode | Disk Free Limit (GiB) |
| --------------- | --------------------- |
| Single-instance | 10                    |
| Cluster         | 2                     |

For `mq.m5` instance types, Amazon MQ sets the following disk free
limits. These values apply to both single-instance and cluster deployments.

| Instance Type | Disk Free Limit (GiB) |
| ------------- | --------------------- |
| mq.m5.large   | 12                    |
| mq.m5.xlarge  | 20                    |
| mq.m5.2xlarge | 36                    |
| mq.m5.4xlarge | 69                    |

Because `mq.m7g` instances have a lower disk free limit,
more of the provisioned disk volume is available for message storage compared
to equivalent `mq.m5` instances.
