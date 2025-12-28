# Amazon MQ for RabbitMQ broker defaults

When you create an Amazon MQ for RabbitMQ broker, Amazon MQ applies a default set of
broker policies and vhost limits to optimize your broker's performance. Amazon MQ applies vhost
limits only to the default (`/`) vhost. Amazon MQ will not apply default policies to newly created vhosts.
We recommend keeping these defaults for all new and existing brokers. However,
you can modify, override, or delete these defaults at any time.

Amazon MQ creates different broker policies and vhost limits for Amazon MQ for RabbitMQ 3 and RabbitMQ 4. The differences will be discussed in detail in the following subsections.

Amazon MQ creates policies and limits based on the instance type and broker deployment mode
that you choose when you create your broker. The default policies are named according to the
deployment mode, as follows:

**Amazon MQ for RabbitMQ 3:**

- Single-instance – `AWS-DEFAULT-POLICY-SINGLE-INSTANCE`
- Cluster deployment – `AWS-DEFAULT-POLICY-CLUSTER-MULTI-AZ` && `AWS-DEFAULT-QUORUM-QUEUES-POLICY-CLUSTER-MULTI-AZ`
  **Amazon MQ for RabbitMQ 4:**

- Single-instance – `AWS-DEFAULT-POLICY-SINGLE-INSTANCE`
- Cluster deployment – `AWS-DEFAULT-POLICY-CLUSTER` && `AWS-DEFAULT-QUORUM-QUEUES-POLICY-CLUSTER-MULTI-AZ`
  For [single-instance
  brokers](rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-single-instance "rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-single-instance"), Amazon MQ sets the policy priority value to `0`. To override the
  default priority value, you can create your own custom policies with higher priority values.
  For [cluster deployments](rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-cluster "rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-cluster"), Amazon MQ
  sets the priority value to `1` for broker defaults. To create your own custom
  policy for clusters, assign a priority value greater than `1`.

###### Note

In cluster deployments, `ha-mode` and `ha-sync-mode` broker
policies are required for classic mirroring and high availability (HA). These settings are only applicable for Amazon MQ for RabbitMQ 3 and are not configured for RabbitMQ 4.

If you delete the default `AWS-DEFAULT-POLICY-CLUSTER-MULTI-AZ` policy,
Amazon MQ uses the `ha-all-AWS-OWNED-DO-NOT-DELETE` policy with a priority value
of `0`. This ensures that the required `ha-mode` and
`ha-sync-mode` policies are still in effect. If you create your own
custom policy, Amazon MQ automatically appends `ha-mode` and
`ha-sync-mode` to your policy definitions.

###### Topics

- [Policy and limit descriptions](#rabbitmq-defaults-descriptions "#rabbitmq-defaults-descriptions")
- [Recommended default values](#rabbitmq-defaults-values "#rabbitmq-defaults-values")

## Policy and limit descriptions

The following list describes the default policies and limits that Amazon MQ applies to a
newly created broker. The values for `max-length`, `max-queues`,
and `max-connections` vary based on your broker's instance type and
deployment mode. These values are listed in the [Recommended default values](#rabbitmq-defaults-values "#rabbitmq-defaults-values") section.

**Settings on both RabbitMQ 3 and RabbitMQ 4 brokers**

- `queue-mode: lazy` (policy) –
  Enables lazy queues. By default, queues keep an in-memory cache of messages,
  enabling the broker to deliver messages to consumers as fast as possible. This
  can lead to the broker running out of memory and raising a high-memory alarm.
  Lazy queues attempt to move messages to disk as early as is practical. This
  means that fewer messages are kept in memory under normal operating conditions.
  Using lazy queues, Amazon MQ for RabbitMQ can support much larger messaging loads
  and longer queues. Note that for certain use cases, brokers with lazy queues
  might perform marginally slower. This is because messages are moved from disk to
  broker, as opposed to delivering messages from an in-memory cache.

###### Deployment modes

Single-instance, cluster

- `max-length:
`number-of-messages``
  (policy) – Sets a limit for the number of messages in a queue. In cluster deployments, the limit
  prevents paused queue synchronization in cases such as broker reboots, or
  following a maintenance window.

###### Deployment modes

Cluster

- `overflow: reject-publish` (policy)
  – Enforces queues with a `max-length` policy to reject new
  messages after the number of messages in the queue reaches the
  `max-length` value. To ensure that messages aren't lost if a
  queue is in an overflow state, client applications that publish messages to the
  broker must implement [publisher
  confirms](best-practices-message-reliability.md#configure-confirmation-acknowledgement "best-practices-message-reliability.md#configure-confirmation-acknowledgement"). For information about implementing publisher confirms, see
  [Publisher Confirms](https://www.rabbitmq.com/confirms.html#publisher-confirms "https://www.rabbitmq.com/confirms.html#publisher-confirms") on the RabbitMQ website.

###### Deployment modes

Cluster

**Settings specific to RabbitMQ 3**

- `max-queues:
`number-of-queues-per-vhost``(vhost limit) – Sets the limit for the number of queues in a
broker. Similar to the`max-length` policy definition, limiting the number of queues
  in cluster deployments prevents paused queue synchronization following broker reboots or maintenance windows.
  Limiting queues also prevents excessive amounts of CPU usage for maintaining queues.

###### Deployment modes

Single-instance, cluster

- `max-connections:
`number-of-connections-per-vhost``
  (vhost limit) – Sets the limit for the number of client connections to
  the broker. Limiting the number of connections according to the recommended values
  prevents excessive broker memory usage, which could result in the broker raising a high memory
  alarm and pausing operations.

###### Deployment modes

Single-instance, cluster

## Recommended default values

###### Important

`max-queues` and `max-connections` are only applied to Amazon MQ for RabbitMQ 3.

###### Note

The `max-length` and `max-queue` default limits are tested and evaluated based on an average message size of 5 kB.
If your messages are significantly larger than 5 kB, you will need to adjust and reduce the `max-length` and `max-queue` limits.

The following table lists the default limit values for a newly created broker. Amazon MQ
applies these values according to the broker's instance type and deployment mode.

| Instance type   | Deployment mode | `max-length` | `max-queues` | `max-connections` |
| --------------- | --------------- | ------------ | ------------ | ----------------- |
| mq.m7g.medium   | Single-instance | N/A          | 2,500        | 100               |
| Cluster         | 500,000         | 100          | 100          |
| mq.m7g.large    | Single-instance | N/A          | 20,000       | 5,000             |
| Cluster         | 8,000,000       | 10,000       | 5,000        |
| mq.m7g.xlarge   | Single-instance | N/A          | 30,000       | 10,000            |
| Cluster         | 9,000,000       | 15,000       | 10,000       |
| mq.m7g.2xlarge  | Single-instance | N/A          | 40,000       | 20,000            |
| Cluster         | 10,000,000      | 40,000       | 20,000       |
| mq.m7g.4xlarge  | Single-instance | N/A          | 60,000       | 40,000            |
| Cluster         | 12,000,000      | 30,000       | 40,000       |
| mq.m7g.8xlarge  | Single-instance | N/A          | 80,000       | 80,000            |
| Cluster         | 20,000,000      | 40,000       | 80,000       |
| mq.m7g.12xlarge | Single-instance | N/A          | 100,000      | 120,000           |
| Cluster         | 30,000,000      | 20,000       | 120,000      |
| mq.m7g.16xlarge | Single-instance | N/A          | 120,000      | 160,000           |
| Cluster         | 40,000,000      | 50,000       | 160,000      |

| Instance type | Deployment mode | `max-length` | `max-queues` | `max-connections` |
| ------------- | --------------- | ------------ | ------------ | ----------------- |
| t3.micro      | Single-instance | N/A          | 500          | 500               |
| m5.large      | Single-instance | N/A          | 20,000       | 4,000             |
| m5.large      | Cluster         | 8,000,000    | 10,000       | 15,000            |
| m5.xlarge     | Single-instance | N/A          | 30,000       | 8,000             |
| m5.xlarge     | Cluster         | 9,000,000    | 10,000       | 20,000            |
| m5.2xlarge    | Single-instance | N/A          | 60,000       | 15,000            |
| m5.2xlarge    | Cluster         | 10,000,000   | 10,000       | 40,000            |
| m5.4xlarge    | Single-instance | N/A          | 150,000      | 30,000            |
| m5.4xlarge    | Cluster         | 12,000,000   | 10,000       | 100,000           |
