# Deployment options for Amazon MQ for ActiveMQ brokers

Amazon MQ offers single instance and cluster deployment options for brokers.

## Option 1: Amazon MQ single-instance brokers

A _single-instance broker_ is comprised of one broker in one
Availability Zone. The broker communicates with your application and with an Amazon EBS
or Amazon EFS storage volume. Amazon EFS storage volumes are designed to provide the highest
level of durability and availability by storing data redundantly across multiple
Availability Zones (AZs). Amazon EBS provides block level storage optimized for
low-latency and high throughput. For more information about storage options, see
[Storage](broker-storage.md "broker-storage.md").

The following diagram illustrates a single-instance broker with Amazon EFS storage
replicated across multiple AZs.

![Diagram showing client, Amazon MQ broker, and EFS volume in AWS Cloud availability zone.](images/amazon-mq-activemq-broker-architecture-single-broker-efs.png)

The following diagram illustrates a single-instance broker with Amazon EBS storage
replicated across multiple servers within a single AZ.

![Diagram showing client, Amazon MQ broker, and EBS volume within AWS Cloud availability zone.](images/amazon-mq-activemq-broker-architecture-single-broker-ebs.png)

## Option 2: Amazon MQ active/standby brokers for high availability

An _active/standby broker_
is comprised of two brokers in two different Availability Zones,
configured in a _redundant pair_. These brokers communicate synchronously with your application, and with Amazon EFS. Amazon EFS storage volumes are designed
to provide the highest level of durability, and availability by storing data
redundantly across multiple Availability Zones (AZs). For more information, see
[Storage](broker-storage.md "broker-storage.md").

Usually, only one of the broker instances is active at any time, while the other
broker instance is on standby. If one of the broker instances malfunctions or
undergoes maintenance, it takes Amazon MQ a short while to take the inactive instance out of service. This allows the healthy standby
instance to become active and to begin accepting incoming communications. Maintencance windows and broker
reboots you initate will cause a failover to happen. When you reboot a broker, the failover
takes only a few seconds.

For an active/standby broker, Amazon MQ provides two ActiveMQ Web Console URLs, but only one URL is active at a time.
Likewise, Amazon MQ provides two endpoints for each wire-level protocol, but only one endpoint is active in each pair at a time.
The `-1` and `-2` suffixes denote a redundant pair.
For wire-level protocol endpoints, you should allow your application to connect to either endpoint by using the
[Failover Transport](http://activemq.apache.org/failover-transport-reference.html "http://activemq.apache.org/failover-transport-reference.html").

The following diagram illustrates an active/standby broker with Amazon EFS storage
replicated across multiple AZs.

![Active/standby Amazon MQ broker setup with EFS volume across multiple availability zones.](images/amazon-mq-activemq-broker-architecture-active-standby.png)
