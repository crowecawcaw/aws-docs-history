

# Amazon MQ for RabbitMQ: Instance type has reached end of support
<a name="troubleshooting-action-required-codes-rabbitmq-instance-type-end-of-support"></a>

Amazon MQ for RabbitMQ raises a `RABBITMQ_INSTANCE_TYPE_END_OF_SUPPORT` action required code when your broker is running on an instance type that has reached end of support. Support for `mq.t3.micro` ended on October 1, 2026.

While a broker is in this state, you may be unable to connect to it from your client applications. The broker continues to run and none of your broker configuration or message data is deleted. You are not billed for the broker while it is unreachable.

## Resolving RABBITMQ\_INSTANCE\_TYPE\_END\_OF\_SUPPORT
<a name="w2aac40c43b7"></a>

1. Change your broker to a supported instance type using the [UpdateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#UpdateBroker) API operation, the AWS CLI, or the Amazon MQ console. For the instance types Amazon MQ supports, see [RabbitMQ broker instance types](rmq-broker-instance-types.md).

1. If your broker is already unreachable and you need more time before changing your instance type, create a case with Support. We can restore connectivity to your broker temporarily so that you can complete the change.

After your broker moves to a supported instance type, Amazon MQ clears the `CRITICAL_ACTION_REQUIRED` state and your clients can connect again.