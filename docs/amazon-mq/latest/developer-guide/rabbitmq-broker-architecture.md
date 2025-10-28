# Deployment options for Amazon MQ for RabbitMQ brokers

RabbitMQ brokers can be created as _single-instance brokers_ or in a
_cluster deployment_. For both deployment modes,
Amazon MQ provides high durability by storing its data redundantly.

You can access your RabbitMQ brokers by using [any programming language that RabbitMQ supports](https://www.rabbitmq.com/devtools.html "https://www.rabbitmq.com/devtools.html") and by enabling TLS for the following protocols:

- [AMQP (0-9-1)](https://www.rabbitmq.com/specification.html "https://www.rabbitmq.com/specification.html")

###### Topics

- [Option 1: Amazon MQ for RabbitMQ single-instance broker](#rabbitmq-broker-architecture-single-instance "#rabbitmq-broker-architecture-single-instance")
- [Option 2: Amazon MQ for RabbitMQ cluster deployment](#rabbitmq-broker-architecture-cluster "#rabbitmq-broker-architecture-cluster")

## Option 1: Amazon MQ for RabbitMQ single-instance broker

A _single-instance broker_ is comprised of one broker in one Availability Zone behind a Network Load Balancer (NLB).
The broker communicates with your application and with an Amazon EBS storage volume. Amazon EBS provides block level storage optimized for low-latency and high throughput.

Using an Network Load Balancer ensures that your Amazon MQ for RabbitMQ broker endpoint remains unchanged if the broker instance
is replaced during a maintenance window or because of underlying Amazon EC2 hardware failures. An Network Load Balancer allows your applications and users
to continue to use the same endpoint to connect to the broker.

The following diagram illustrates an Amazon MQ for RabbitMQ single-instance broker.

![Diagram showing client, load balancer, Amazon MQ broker, and EBS volume in AWS Cloud.](images/amazon-mq-rabbitmq-broker-architecture-single-broker.png)

## Option 2: Amazon MQ for RabbitMQ cluster deployment

A _cluster deployment_
is a logical grouping of three RabbitMQ broker nodes behind a Network Load Balancer, each sharing users, queues, and a distributed state across multiple Availability Zones (AZ).

In a cluster deployment, Amazon MQ automatically manages broker policies to enable classic mirroring across all nodes, ensuring high availability (HA).
Each mirrored queue consists of one _main_ node and one or more _mirrors_. Each queue
has its own main node. All operations for a given queue are first applied on the queue's main node and then propagated to mirrors.
Amazon MQ creates a default system policy that sets the `ha-mode` to `all` and `ha-sync-mode` to
`automatic`. This ensures that data is replicated to all nodes in the cluster across different Availability Zones for better durability.

###### Note

In a cluster deployment, if an Availability Zone outage occurs,
Amazon MQ will automatically attempt to relocate the affected RabbitMQ nodes to a different AZ
to maintain the cluster size. Once the outage resolves,
the cluster will be automatically rebalanced across the AZs.

###### Note

During a _maintenance window_, all maintenance to a cluster is performed one node at a time, keeping at least two running nodes at all times.
Each time a node is brought down, client connections to that node are severed and need to be re-established. You must ensure that your client code is designed
to automatically reconnect to your cluster. For more information about connection recovery, see [Step 1: Automatically recover from network failures](best-practices-network-resilience.md#automatically-recover-from-network-failures "best-practices-network-resilience.md#automatically-recover-from-network-failures").

Because Amazon MQ sets `ha-sync-mode: automatic`, during a maintenance window, queues will synchronize when each node re-joins the cluster. Queue
synchronization blocks all other queue operations. You can mitigate the impact of queue synchronization during maintenance windows
by keeping queues short.

The default policy should not be deleted. If you do delete this policy, Amazon MQ will automatically recreate it.
Amazon MQ will also ensure that HA properties are applied to all other
policies that you create on a clustered broker. If you add a policy without the HA properties, Amazon MQ will add
them for you. If you add a policy with different high availability properties, Amazon MQ will replace them.
For more information about classic mirroring, see [Classic mirrored queues](https://www.rabbitmq.com/ha.html "https://www.rabbitmq.com/ha.html").

The following diagram illustrates a RabbitMQ cluster broker deployment with three nodes in three
Availability Zones (AZ), each with its own Amazon EBS volume and a shared state. Amazon EBS provides block level storage optimized for low-latency and high throughput.

![Illustrates the cluster deployment broker architecture for RabbitMQ brokers.](images/amazon-mq-rabbitmq-broker-architecture-cluster-broker.png)
