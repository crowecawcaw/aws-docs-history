

# Deployment options for Amazon MQ for ActiveMQ brokers
<a name="amazon-mq-broker-architecture"></a>

Amazon MQ offers single instance and cluster deployment options for brokers.

## Option 1: Amazon MQ single-instance brokers
<a name="single-broker-deployment"></a>

A *single-instance broker* is comprised of one broker in one Availability Zone. The broker communicates with your application and with an Amazon EBS or Amazon EFS storage volume. Amazon EFS storage volumes are designed to provide the highest level of durability and availability by storing data redundantly across multiple Availability Zones (AZs). Amazon EBS provides block level storage optimized for low-latency and high throughput. For more information about storage options, see [Amazon MQ for ActiveMQ storage types](broker-storage.md).

The following diagram illustrates a single-instance broker with Amazon EFS storage replicated across multiple AZs.

![Client connecting to Amazon MQ Broker in us-west-2a availability zone with EFS Volume storage.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-activemq-broker-architecture-single-broker-efs.png)


The following diagram illustrates a single-instance broker with Amazon EBS storage replicated across multiple servers within a single AZ.

![Client connecting to Amazon MQ Broker and EBS Volume within availability zone us-west-2a.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-activemq-broker-architecture-single-broker-ebs.png)


## Option 2: Amazon MQ active/standby brokers for high availability
<a name="active-standby-broker-deployment"></a>

An *active/standby broker* is comprised of two brokers in two different Availability Zones, configured in a *redundant pair*. These brokers communicate synchronously with your application, and with Amazon EFS. Amazon EFS storage volumes are designed to provide the highest level of durability, and availability by storing data redundantly across multiple Availability Zones (AZs). For more information, see [Amazon MQ for ActiveMQ storage types](broker-storage.md).

Usually, only one of the broker instances is active at any time, while the other broker instance is on standby. If one of the broker instances malfunctions or undergoes maintenance, it takes Amazon MQ a short while to take the inactive instance out of service. This allows the healthy standby instance to become active and to begin accepting incoming communications. Maintenance windows and broker reboots you initiate will cause a failover to happen. When you reboot a broker, the failover takes only a few seconds.

For an active/standby broker, Amazon MQ provides two ActiveMQ Web Console URLs, but only one URL is active at a time. Likewise, Amazon MQ provides two endpoints for each wire-level protocol, but only one endpoint is active in each pair at a time. The `-1` and `-2` suffixes denote a redundant pair. For wire-level protocol endpoints, you should allow your application to connect to either endpoint by using the [Failover Transport](https://activemq.apache.org/failover-transport-reference.html).

The following diagram illustrates an active/standby broker with Amazon EFS storage replicated across multiple AZs.

![Active MQ broker in us-west-2a and standby broker in us-west-2b, both connected to client and EFS volume.](http://docs.aws.amazon.com/amazon-mq/latest/developer-guide/images/amazon-mq-activemq-broker-architecture-active-standby.png)
