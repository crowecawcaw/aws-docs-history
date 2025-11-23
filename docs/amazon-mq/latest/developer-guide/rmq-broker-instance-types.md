# Amazon MQ for RabbitMQ broker instance types

The combined description of the broker instance class (m7g) and size (large, medium) is called the broker instance type (for example, mq.m7g.large).

We recommend using mq.m7g instance types for both cluster and single-instance deployments.

Amazon MQ provides at least a 90 day notice before an instance type reaches end of support. We recommend upgrading your broker to a new instance type before the end-of-support date to prevent any disruptions.

###### Important

You cannot downgrade a broker from an `mq.m7g` or `mq.m5` instance type to a `mq.t3.micro` instance type.

The `mq.t3.micro` instance type does not support cluster deployment.

## Instance types for m7g cluster deployment

We recommending using `mq.m7g.x` instance types with cluster deployment.
The following table shows the available `mq.m7g.x` instance types for cluster deployment.

| Instance Type   | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use | Storage | Disk volume size per node(GB) |
| --------------- | ---- | ------------ | ----------------------------------------- | --------------- | ------- | ----------------------------- |
| mq.m7g.medium   | 1    | 4            | 0.52 / 12.5                               | Evaluation      | EBS     | 5                             |
| mq.m7g.large    | 2    | 8            | 0.937 / 12.5                              | Production      | EBS     | 15                            |
| mq.m7g.xlarge   | 4    | 16           | 1.876 / 12.5                              | Production      | EBS     | 25                            |
| mq.m7g.2xlarge  | 8    | 32           | 3.75 / 15.0                               | Production      | EBS     | 45                            |
| mq.m7g.4xlarge  | 16   | 64           | 7.5 / 15.0                                | Production      | EBS     | 90                            |
| mq.m7g.8xlarge  | 32   | 128          | 15 Gigabit                                | Production      | EBS     | 175                           |
| mq.m7g.12xlarge | 48   | 192          | 22.5 Gigabit                              | Production      | EBS     | 260                           |
| mq.m7g.16xlarge | 64   | 256          | 30 Gigabit                                | Production      | EBS     | 345                           |

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

| Instance Type | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use | Storage | Disk volume size per node(GB) |
| ------------- | ---- | ------------ | ----------------------------------------- | --------------- | ------- | ----------------------------- |
| mq.t3.micro   | 2    | 1            | 0.064 / 5.0                               | Evaluation      | EBS     | 20                            |
| mq.m5.large   | 2    | 8            | 0.75 / 10.0                               | Production      | EBS     | 200                           |
| mq.m5.xlarge  | 4    | 16           | 1.25 / 10.0                               | Production      | EBS     | 200                           |
| mq.m5.2xlarge | 8    | 32           | 2.5 / 10.0                                | Production      | EBS     | 200                           |
| mq.m5.4xlarge | 16   | 64           | 5.0 / 10.0                                | Production      | EBS     | 200                           |

## Instance types for `mq.m5` cluster deployment

The following tables show the available `mq.m5.x` instance types for cluster deployment

| Instance Type | vCPU | Memory (GiB) | Network Baseline / Burst bandwidth (Gbps) | Recommended use | Storage | Disk volume size per node(GB) |
| ------------- | ---- | ------------ | ----------------------------------------- | --------------- | ------- | ----------------------------- |
| mq.m5.large   | 2    | 8            | 0.75 / 10.0                               | Production      | EBS     | 200                           |
| mq.m5.xlarge  | 4    | 16           | 1.25 / 10.0                               | Production      | EBS     | 200                           |
| mq.m5.2xlarge | 8    | 32           | 2.5 / 10.0                                | Production      | EBS     | 200                           |
| mq.m5.4xlarge | 16   | 64           | 5.0 / 10.0                                | Production      | EBS     | 200                           |
