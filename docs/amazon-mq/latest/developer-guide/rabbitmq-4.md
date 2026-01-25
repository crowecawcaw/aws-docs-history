# RabbitMQ 4

Amazon MQ supports RabbitMQ 4.2 in the RabbitMQ 4 release series only on the mq.m7g instance type across all supported instance sizes.

###### Important

You can only create new brokers on RabbitMQ 4.2. In place upgrades from RabbitMQ 3.13 are not currently supported.

###### Important

The default queue type on Amazon MQ for RabbitMQ 4.2 brokers will be “quorum”.
If no queue type argument is specified during queue creation, a quorum queue will be created.

We highly recommend using quorum queues on RabbitMQ 4 for durability needs,
since classic queues are not guaranteed to be durable in all cases.

## The following changes have been introduced in RabbitMQ 4 on Amazon MQ

- **AMQP 1.0 as a core protocol:** For more information, see [Protocols](rabbitmq-supported-protocols.md "rabbitmq-supported-protocols.md").
- **Local shovels:** Shovels now support a new protocol called "local" in addition to AMQP 0-9-1 and AMQP 1.0. Local shovels are internally based on AMQP 1.0 but instead of using separate TCP connections, they use intra-cluster connections between cluster nodes and internal APIs for publishing and consuming messages. This can only be used for consuming and publishing within the same cluster and can offer higher throughput while using fewer resources than AMQP 0-9-1 and AMQP 1.0.
- **Quorum queues support message priorities:** Quorum queue message priorities are always active and do not require a policy to work. As soon as a quorum queue receives a message with a priority set it will enable prioritization. Quorum queues internally only support two priorities - high and normal. Messages without a priority set will be mapped to normal as will priorities 0 - 4. Messages with a priority higher than 4 will be mapped to high. High priority messages will be favoured over normal priority messages at a ratio of 2:1, i.e. for every 2 high priority message the queue will deliver 1 normal priority message (if available). Hence, quorum queues implement a kind of non-strict, "fair share" priority processing. This ensures progress is always made on normal priority messages, but high priorities are favoured at a ratio of 2:1.
- **Khepri:** Khepri is used as the default metadata store for RabbitMQ 4 brokers
- **Mutual TLS (mTLS):** Amazon MQ supports mutual TLS (mTLS) for RabbitMQ brokers, allowing clients to authenticate using certificates. For more information, see [mTLS configuration](configure-mtls.md "configure-mtls.md").
- **SSL certificate authentication plugin:** The SSL authentication plugin uses client certificates from mTLS connections to authenticate users, allowing authentication using X.509 client certificates instead of username and password credentials. For more information, see [SSL certificate authentication](ssl-for-amq-for-rabbitmq.md "ssl-for-amq-for-rabbitmq.md").
- **HTTP authentication plugin:** The HTTP authentication backend plugin allows delegating authentication and authorization to an external HTTP service. For more information, see [HTTP authentication and authorization](http-for-amq-for-rabbitmq.md "http-for-amq-for-rabbitmq.md").
- **JMS support:** The broker now supports JMS workloads with the JMS topic exchange plugin enabled, allowing JMS applications to connect using the [RabbitMQ JMS client](https://github.com/rabbitmq/rabbitmq-jms-client "https://github.com/rabbitmq/rabbitmq-jms-client").

## The following features have been deprecated from RabbitMQ 4 on Amazon MQ

- **Mirroring of classic queues:** Classic queues continue to be supported without any breaking changes for client libraries and applications, but they are now a non-replicated queue type. Clients will be able to connect to any node to publish to and consume from any non-replicated classic queues. Quorum queues are recommended for replication and data safety.
- **Removal of Global QoS:** Customers are recommended to set per-consumer QoS (non-global) instead of Global QoS, where a single shared prefetch is used for an entire channel.
- **Support for transient, non-exclusive queues:** Transient queues are queues whose lifetime is linked to the uptime of the node they are declared on. In a single instance broker, they are removed when the node is restarted. In a cluster deployment, they are removed when the node they are hosted on is restarted. We recommend using queue TTL for auto-deleting unused, idle queues after some time of inactivity. Exclusive queues continue to be supported and are deleted once all connections to the queue have been removed.

## The following breaking changes may impact your applications when upgrading to RabbitMQ 4.2 on Amazon MQ

- **Default queue type:** The default queue type on a RabbitMQ 4 broker is set to quorum.
  If no queue type argument is specified during queue creation, a quorum queue will be created.
- **Default redelivery limit on quorum queues is set to 20:** Messages that are redelivered 20 times or more will be dead-lettered or dropped (removed). If 20 deliveries per message is a common scenario for a queue, a dead-lettering target or a higher limit must be configured for such queues to avoid data loss. The recommended way of doing that is via a policy.
- **amqplib:** Node JS client **amqplib versions older than 0.10.7** or any AMQP client library using **frame_max < 8192** will not be able to connect to RabbitMQ
- [Default resource limits:](rabbitmq-resource-limits-configuration.md "rabbitmq-resource-limits-configuration.md") Amazon MQ for RabbitMQ has introduced default resource usage limits for connections, channels, consumers per channel, queues, vhosts, shovels, exchanges, and maximum message size. These serve as guardrails to protect broker availability and can be customized using configurations to match your specific requirements.

## The following features are not supported on RabbitMQ 4 on Amazon MQ

- **Local Random exchanges:** Local random exchanges are not supported on Amazon MQ since the Amazon MQ nodes are behind a network load balancer.
- **Message Interceptor:** [RabbitMQ message interceptors](https://www.rabbitmq.com/docs/message-interceptors "https://www.rabbitmq.com/docs/message-interceptors") are not supported on Amazon MQ.
- **Per queue metrics:**
  Amazon MQ will not vend RabbitMQ queue metrics for RabbitMQ 4 brokers through AWS CloudWatch.
  Amazon MQ will still provide broker level metrics through AWS CloudWatch. You can query queue metrics
  using the RabbitMQ management API. We recommend querying metrics for specific queues at a frequency of one minute or longer intervals.
