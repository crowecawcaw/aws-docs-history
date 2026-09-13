

# RabbitMQ 4.2
<a name="rabbitmq-42"></a>

 Amazon MQ supports RabbitMQ 4.2 as the first release in the RabbitMQ 4 series. RabbitMQ 4.2 introduces AMQP 1.0 as a core protocol, Khepri as the default metadata store, quorum queue message priorities, and new authentication plugins including mTLS and HTTP authentication. For more information about this release, see the [RabbitMQ 4.0.0 release notes](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.0.0) on the GitHub website. 

## New features and enhancements in RabbitMQ 4.2 on Amazon MQ
<a name="rabbitmq-42-new-features"></a>
+ **AMQP 1.0 as a core protocol:** For more information, see [Protocols](rabbitmq-supported-protocols.md).
+ **Local shovels:** Shovels now support a new protocol called "local" in addition to AMQP 0-9-1 and AMQP 1.0. Local shovels are internally based on AMQP 1.0 but instead of using separate TCP connections, they use intra-cluster connections between cluster nodes and internal APIs for publishing and consuming messages. This can only be used for consuming and publishing within the same cluster and can offer higher throughput while using fewer resources than AMQP 0-9-1 and AMQP 1.0.
+ **Quorum queues support message priorities:** Quorum queue message priorities are always active and do not require a policy. When a quorum queue receives a message with a priority set, it enables prioritization. Quorum queues support only two internal priority levels—high and normal.

   RabbitMQ maps messages without a priority, and messages with priorities 0–4, to normal. Messages with a priority higher than 4 are mapped to high. High-priority messages are favored over normal-priority messages at a 2:1 ratio. For every 2 high-priority messages, the queue delivers 1 normal-priority message, if one is available. As a result, quorum queues implement a non-strict, fair-share priority processing model that ensures progress on normal-priority messages. 
+ **Khepri:** Khepri is used as the default metadata store for RabbitMQ 4 brokers
+ **Mutual TLS (mTLS):** Amazon MQ supports mutual TLS (mTLS) for RabbitMQ brokers, allowing clients to authenticate using certificates. For more information, see [mTLS configuration](configure-mtls.md).
+ **SSL certificate authentication plugin:** The SSL authentication plugin uses client certificates from mTLS connections to authenticate users, allowing authentication using X.509 client certificates instead of username and password credentials. For more information, see [SSL certificate authentication](ssl-for-amq-for-rabbitmq.md).
+ **HTTP authentication plugin:** The HTTP authentication backend plugin allows delegating authentication and authorization to an external HTTP service. For more information, see [HTTP authentication and authorization](http-for-amq-for-rabbitmq.md).
+ **JMS support:** The broker now supports JMS workloads with the JMS topic exchange plugin enabled, allowing JMS applications to connect using the [RabbitMQ JMS client](https://github.com/rabbitmq/rabbitmq-jms-client).
+ **Configurable storage size:** RabbitMQ 4.x brokers deployed in CLUSTER\_MULTI\_AZ mode support configurable EBS storage sizes. For more information, see [mq.m7g instance types](rmq-broker-instance-types.md#instance-types-m7g-cluster).

## Deprecated features in RabbitMQ 4.2 on Amazon MQ
<a name="rabbitmq-42-deprecations"></a>
+ **Mirroring of classic queues:** Classic queues continue to be supported without any breaking changes for client libraries and applications, but they are now a non-replicated queue type. Clients will be able to connect to any node to publish to and consume from any non-replicated classic queues. Quorum queues are recommended for replication and data safety.
+ **Removal of Global QoS:** Customers are recommended to set per-consumer QoS (non-global) instead of Global QoS, where a single shared prefetch is used for an entire channel.
+ **Support for transient, non-exclusive queues: ** Transient queues are queues whose lifetime is linked to the uptime of the node they are declared on. In a single instance broker, they are removed when the node is restarted. In a cluster deployment, they are removed when the node they are hosted on is restarted. We recommend using queue TTL for auto-deleting unused, idle queues after some time of inactivity. Exclusive queues continue to be supported and are deleted once all connections to the queue have been removed.

## Breaking changes in RabbitMQ 4.2 on Amazon MQ
<a name="rabbitmq-42-breaking-changes"></a>

The following open-source changes might impact your applications when upgrading to RabbitMQ 4.2. Review these changes before upgrading your broker.
+  **Default queue type:** The default queue type on a RabbitMQ 4 broker is set to quorum. If no queue type argument is specified during queue creation, a quorum queue will be created. 
+ **Default redelivery limit on quorum queues is set to 20: ** Messages that are redelivered 20 times or more will be dead-lettered or dropped (removed). If 20 deliveries per message is a common scenario for a queue, a dead-lettering target or a higher limit must be configured for such queues to avoid data loss. The recommended way of doing that is via a policy.
+ **amqplib: **Node JS client ** amqplib versions older than 0.10.7 **or any AMQP client library using **frame\_max < 8192 ** will not be able to connect to RabbitMQ
+ [Default resource limits:](rabbitmq-resource-limits-configuration.md) Amazon MQ for RabbitMQ has introduced default resource usage limits for connections, channels, consumers per channel, queues, vhosts, shovels, exchanges, and maximum message size. These serve as guardrails to protect broker availability and can be customized using configurations to match your specific requirements.