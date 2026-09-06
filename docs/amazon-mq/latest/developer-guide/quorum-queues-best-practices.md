

# Best practices for quorum queues for Amazon MQ for RabbitMQ
<a name="quorum-queues-best-practices"></a>

We recommend using the following best practices to improve performance when working with quorum queues.

## Handling poison messages by setting a delivery limit
<a name="using-quorum-queues-delivery-limit"></a>

 Poison messages occur when a message fails and is redelivered multiple times. You can set a message delivery limit using the `delivery-limit` policy argument to drop messages that are redelivered multiple times. If a message is redelivered more times than the delivery limit allows, the message is then dropped and deleted by RabbitMQ. When you set a delivery limit, the message is requeued near the head of the queue. 

## Message priority for quorum queues
<a name="quorum-queues-message-priority"></a>

 Quorum queues do not have message priority. If you need message priority, you must create multiple quorum queues. For more information on prioritizing messages with multiple quorum queues, see [Message priority](https://www.rabbitmq.com/docs/quorum-queues#priorities) in the RabbitMQ documentation. 

## Using the default replication factor
<a name="using-quorum-queues-replication-factor"></a>

 Amazon MQ for RabbitMQ defaults to a replication factor of three (3) nodes for cluster brokers using quorum queues. If you make changes to `x-quorum-initial-group-size`, Amazon MQ will default again to the replication factor of 3. 