

# Best practices for quorum queues for Amazon MQ for RabbitMQ
<a name="quorum-queues-best-practices"></a>

We recommend using the following best practices to improve performance when working with quorum queues.

## Handling poison messages by setting a delivery limit
<a name="using-quorum-queues-delivery-limit"></a>

 Poison messages occur when a message fails and is redelivered multiple times. You can set a message delivery limit using the `delivery-limit` policy argument to drop messages that are redelivered multiple times. If a message is redelivered more times than the delivery limit allows, the message is then dropped and deleted by RabbitMQ. When you set a delivery limit, the message is requeued near the head of the queue. 

**Note**  
 On RabbitMQ 4.2, quorum queues have a default delivery limit of 20. For more information, see [Breaking changes in RabbitMQ 4.2 on Amazon MQ](rabbitmq-42.md#rabbitmq-42-breaking-changes).   
 On RabbitMQ 4.3, you can update the quorum queue delivery limit using a policy without requiring queue redeclaration. For more information, see [New features and enhancements in RabbitMQ 4.3 on Amazon MQ](rabbitmq-43.md#rabbitmq-43-new-features). 

## Message priority for quorum queues
<a name="quorum-queues-message-priority"></a>

 Quorum queues on RabbitMQ 3.13 do not have message priority. If you need message priority, use multiple quorum queues. For more information, see [Message priority](https://www.rabbitmq.com/docs/quorum-queues#priorities) in the RabbitMQ documentation. 

**Note**  
 On RabbitMQ 4.2, quorum queues use a 2:1 delivery ratio between high-priority (5 and higher) and normal-priority (0 through 4) messages. For more information, see [New features and enhancements in RabbitMQ 4.2 on Amazon MQ](rabbitmq-42.md#rabbitmq-42-new-features).   
 On RabbitMQ 4.3, quorum queues support strict priority ordering with up to 32 levels, enabled by the `x-max-priority` queue argument. For more information, see [New features and enhancements in RabbitMQ 4.3 on Amazon MQ](rabbitmq-43.md#rabbitmq-43-new-features). 

## Using the default replication factor
<a name="using-quorum-queues-replication-factor"></a>

 Amazon MQ for RabbitMQ defaults to a replication factor of three (3) nodes for cluster brokers using quorum queues. If you make changes to `x-quorum-initial-group-size`, Amazon MQ will default again to the replication factor of 3. 