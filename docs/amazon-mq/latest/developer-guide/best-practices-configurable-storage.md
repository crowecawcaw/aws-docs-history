

# Configurable storage best practices for Amazon MQ for RabbitMQ
<a name="best-practices-configurable-storage"></a>

 Amazon MQ for RabbitMQ brokers use Amazon Elastic Block Store (Amazon EBS) for persistent storage. Configure the storage size within a range that depends on your instance type. Monitoring your broker's disk usage over time helps you choose the right storage size and avoid disk alarm events that block publishers. 

**Prerequisites**  
Configurable storage is available only for Amazon MQ for RabbitMQ brokers that meet the following requirements:  
Engine version 4.2 or later.
Cluster deployment mode.
`m7g` instance types only.

## Step 1: Configurable storage ranges by instance type
<a name="configurable-storage-ranges"></a>

 Each instance type supports a specific range of configurable storage sizes. The following table lists the minimum (default) and maximum storage sizes available for each instance type. 


| Instance type | Minimum/Default storage size (GB) | Maximum storage size (GB) | 
| --- | --- | --- | 
| mq.m7g.medium | 5 | 25 | 
| mq.m7g.large | 15 | 75 | 
| mq.m7g.xlarge | 25 | 125 | 
| mq.m7g.2xlarge | 45 | 180 | 
| mq.m7g.4xlarge | 90 | 250 | 
| mq.m7g.8xlarge | 175 | 400 | 
| mq.m7g.12xlarge | 260 | 500 | 
| mq.m7g.16xlarge | 345 | 500 | 

## Step 2: Monitor your disk usage
<a name="monitor-disk-usage"></a>

 To make informed decisions about your storage size, monitor your broker's disk usage using Amazon CloudWatch metrics. The following key metrics help you understand your disk usage patterns: 

**`RabbitMQDiskFree`**  
The total volume of free disk space available on each node's EBS volume (in bytes).

**`RabbitMQDiskFreeLimit`**  
The disk limit for each node's EBS volume. When free disk space on any node falls below this value, a disk alarm triggers and all nodes in the cluster block incoming messages.

 To monitor your disk usage: 

1. Open the **Amazon MQ console** and choose your broker name.

1. Under **Actions**, choose **View metrics**.

1. Under **Broker metrics**, select `RabbitMQDiskFree` and `RabbitMQDiskFreeLimit`.

1. Set the time range to approximately 2 weeks to observe your disk usage pattern.

## Step 3: Decide when to upgrade storage
<a name="decide-when-to-upgrade-storage"></a>

 After monitoring `RabbitMQDiskFree` and `RabbitMQDiskFreeLimit` for approximately 2 weeks, use the following guidance to determine whether to increase your storage size: 
+ **No action needed** — `RabbitMQDiskFree` remains well above `RabbitMQDiskFreeLimit` with more than 10 GB of headroom, and usage is stable. Continue monitoring.
+ **Consider upgrading** — `RabbitMQDiskFree` is trending downward and only approximately 5 GB remains above `RabbitMQDiskFreeLimit`. You have two options:
  + **Increase your configurable storage size.** Increase the EBS volume size within the maximum for your instance type (see table above) to provide more disk headroom.
  + **Upgrade your instance size.** Move to a larger instance type, which supports a higher maximum storage ceiling and other resource benefits.

**Important**  
When `RabbitMQDiskFree` drops below `RabbitMQDiskFreeLimit` on any node, RabbitMQ raises a disk alarm (`RABBITMQ_DISK_ALARM`). This alarm is cluster-wide. If any node goes under the limit, all nodes block incoming messages. Consumers can still drain messages, but no new data is accepted until free space recovers above the limit.  
For steps on diagnosing and resolving the disk limit alarm, see [RabbitMQ on Amazon MQ: Disk limit alarm](troubleshooting-action-required-codes-disk-limit-alarm.md).