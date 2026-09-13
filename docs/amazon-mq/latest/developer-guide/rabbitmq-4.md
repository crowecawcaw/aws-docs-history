

# RabbitMQ 4
<a name="rabbitmq-4"></a>

Amazon MQ supports RabbitMQ 4.3 and 4.2 in the RabbitMQ 4 release series only on the mq.m7g instance type across all supported instance sizes.

Amazon MQ supports in-place upgrades from RabbitMQ 3.13 to RabbitMQ 4.2, and from RabbitMQ 4.2 to 4.3. For more information, see [Upgrading from RabbitMQ 3 to 4](upgrading-rabbitmq-v3-to-v4.md).

**Important**  
 The default queue type on Amazon MQ for RabbitMQ 4.2 brokers is `quorum`. If no queue type argument is specified during queue creation, a quorum queue will be created.   
 We highly recommend using quorum queues on RabbitMQ 4 for durability needs, since classic queues are not guaranteed to be durable in all cases. 

## The following features are not supported on RabbitMQ 4 on Amazon MQ
<a name="rabbitmq-4-not-supported"></a>
+ **Local Random exchanges:** Local random exchanges are not supported on Amazon MQ since the Amazon MQ nodes are behind a network load balancer.
+ **Message Interceptor:** [ RabbitMQ message interceptors ](https://www.rabbitmq.com/docs/message-interceptors) are not supported on Amazon MQ.
+  **Per queue metrics:** Amazon MQ will not vend RabbitMQ queue metrics for RabbitMQ 4 brokers through AWS CloudWatch. Amazon MQ will still provide broker level metrics through AWS CloudWatch. You can query queue metrics using the RabbitMQ management API. We recommend querying metrics for specific queues at a frequency of one minute or longer intervals. 