

# Amazon MQ for RabbitMQ: Broker not upgradeable to version 4
<a name="troubleshooting-action-required-codes-rabbitmq-not-upgradeable-to-v4"></a>

Amazon MQ for RabbitMQ will raise a `RABBITMQ_BROKER_NOT_UPGRADEABLE_TO_V4` action required code when you attempt to upgrade a RabbitMQ 3 broker to RabbitMQ 4 and the broker has classic queues or the Khepri metadata store feature flag is enabled. Amazon MQ will not apply the major version upgrade and will make the broker available for publishing and consuming. 

This action required code applies only to RabbitMQ 3 brokers. To resolve this state and continue with the upgrade, complete the following steps.

## Diagnosing and resolving RABBITMQ\_BROKER\_NOT\_UPGRADEABLE\_TO\_V4
<a name="w2aac40c41b7"></a>

1. Migrate all classic queues to quorum queues using the [Amazon MQ queue migration tool](https://github.com/amazon-mq/rabbitmq-queue-migration). The tool is accessible through the RabbitMQ web console (**Admin** > **Queue Migration**) or through the HTTP API.

1. If Khepri is enabled on the broker, there is no in-place upgrade path to RabbitMQ 4. Consider a [RabbitMQ blue-green deployment](https://www.rabbitmq.com/docs/blue-green-upgrade) instead.

After you resolve the underlying issue, Amazon MQ automatically clears the `CRITICAL_ACTION_REQUIRED` state.

**Note**  
You can clear the `CRITICAL_ACTION_REQUIRED` state by updating the broker engine version back to 3.13 using the [UpdateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#UpdateBroker) API operation.