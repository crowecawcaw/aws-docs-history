#

Amazon MQ for RabbitMQ: High memory alarm

Amazon MQ for RabbitMQ will raise a high memory alarm when the broker's memory usage, identified by CloudWatch metric
`RabbitMQMemUsed`, exceeds the memory limit, identified by `RabbitMQMemLimit`.

A RabbitMQ broker that has raised a high memory alarm will block all clients that are
publishing messages. Your broker may enter a [restart loop](troubleshooting-rabbitmq.md#single-instance-broker-restart-loop "troubleshooting-rabbitmq.md#single-instance-broker-restart-loop"),
experience [paused queue synchronization](troubleshooting-rabbitmq.md#addressing-paused-queue-sync "troubleshooting-rabbitmq.md#addressing-paused-queue-sync"),
or develop other issues that complicate diagnosis and resolution of the alarm.

To diagnose and resolve high memory alarm, first follow all [best practices](best-practices-rabbitmq.md "best-practices-rabbitmq.md") for RabbitMQ, then complete the following steps.

###### Important

- `RabbitMQMemLimit` is set by Amazon MQ and is specifically tuned considering the memory available for
  each host instance type.
- Amazon MQ will not restart a broker experiencing a high memory alarm and will return an exception for
  [`RebootBroker`](../api-reference/brokers-broker-id-reboot.md "../api-reference/brokers-broker-id-reboot.md") API
  operations as long as the broker continues to raise the alarm.

##

Step 1: Diagnose high memory alarm

There are two ways to diagnose high memory alarms on your Amazon MQ for RabbitMQ broker.
We recommend that you check both the RabbitMQ web console and Amazon MQ metrics in CloudWatch.

###

Diagnose high memory alarm using the RabbitMQ web console

The RabbitMQ web console can generate and display detailed memory usage information for each
node. You can find this information by doing the following:

1. Sign in to AWS Management Console and open your broker's RabbitMQ web console.
2. On the RabbitMQ console, on the **Overview** page, choose the name of a node from the **Nodes** list.
3. On the node detail page, choose **Memory details** to expand the section to view the node's memory usage information.

The memory usage information that RabbitMQ provides in the web console can help you determine which resources might be consuming too
much memory and contributing to the high memory alarm. For more information on the memory usage details available via the RabbitMQ web console,
see [Reasoning About Memory Use](https://www.rabbitmq.com/memory-use.html "https://www.rabbitmq.com/memory-use.html") on the RabbitMQ Server Documentation website.

### Diagnose high memory alarm using Amazon MQ metrics

Amazon MQ enables metrics for your broker by default. You can [view your broker metrics](amazon-mq-accessing-metrics.md "amazon-mq-accessing-metrics.md")
by accessing the CloudWatch console, or by using the CloudWatch API. The following metrics are useful when diagnosing the RabbitMQ
high memory alarm.

| Amazon MQ CloudWatch metric | Reason for high memory use                                                                                                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MessageCount`              | Messages are stored in memory until they are consumed or discarded. A high message count might<br>indicate overutilization of resources and can lead to a high memory alarm.                                                                                  |
| `QueueCount`                | Queues are stored in memory, and a high number of queues can lead to a high memory alarm.                                                                                                                                                                     |
| `ConnectionCount`           | Client connections utilize memory, and too many simultaneous connections can lead to a high memory alarm.                                                                                                                                                     |
| `ChannelCount`              | Similar to connections, channels established using each connection are also stored in node memory, and a high number of channels<br>can lead to a high memory alarm.                                                                                          |
| `ConsumerCount`             | For every consumer connected to the broker, a set number of messages are loaded from storage into memory before they are delivered to the consumer.<br>A large number of consumer connections might cause high memory usage and lead to a high memory alarm.  |
| `PublishRate`               | Publishing messages utilizes the broker' memory. If the rate at which messages are published to the broker is too high and<br>significantly outpaces the rate at which the broker delivers messages to consumers, the broker might raise a high memory alarm. |

##

Step 2: Address and prevent high memory alarm

###### Note

It may take up to several hours for the RABBITMQ_MEMORY_ALARM status to clear after you take the required actions.

Follow all [best practices](best-practices-rabbitmq.md "best-practices-rabbitmq.md") for RabbitMQ as a general method of prevention.
For each specific contributor that you identify, we recommend the following set of actions to
address and prevent RabbitMQ high memory alarms.

| Source of high memory use      | Amazon MQ recommendation for addressing                                                                                                  | Amazon MQ recommendation for preventing                                                                                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Number of messages             | Consume messages published to the queues,<br>purge messages from queues,<br>or delete the queues from your broker.                       | Enable lazy queues,<br>and set or reduce the [queue depth limit](rabbitmq-defaults-applying-policies.md "rabbitmq-defaults-applying-policies.md").                                         |
| Number of queues               | Reduce the number of queues.                                                                                                             | Set or reduce the [queue count limit](rabbitmq-resource-limits-configuration.md "rabbitmq-resource-limits-configuration.md").                                                              |
| Number of connections          | [Reduce the number of connections](reducing-connections-and-channels.md "reducing-connections-and-channels.md").                         | Set or reduce the [connection count limit](rabbitmq-resource-limits-configuration.md "rabbitmq-resource-limits-configuration.md").                                                         |
| Number of channels             | [Reduce the number of channels](reducing-connections-and-channels.md "reducing-connections-and-channels.md").                            | Set a maximum number of channels per connection on client applications.                                                                                                                    |
| Number of consumers            | Reduce the number of consumers connected to the broker.                                                                                  | Set a small consumer [pre-fetch limit](rabbitmq-resource-limits-configuration.md "rabbitmq-resource-limits-configuration.md").                                                             |
| Message publishing rate        | Reduce the rate at which publishers send messages to the broker.                                                                         | Turn on [publisher confirms](best-practices-message-reliability.md#configure-confirmation-acknowledgement "best-practices-message-reliability.md#configure-confirmation-acknowledgement"). |
| Client connection attempt rate | Reduce the frequency at which clients attempt to connect to the broker in order to publish or consume messages, or configure the broker. | Use longer-lived connections to reduce the number and frequency of connection attempts.                                                                                                    |

After your broker's memory alarm is resolved, you can upgrade your host instance
type to an instance with additional resources. For information on how to update your broker's instance type, see
[`UpdateBrokerInput`](../api-reference/brokers-broker-id.md#brokers-broker-id-model-updatebrokerinput "../api-reference/brokers-broker-id.md#brokers-broker-id-model-updatebrokerinput")
in the _Amazon MQ REST API Reference_.

###### Note

You can't downgrade a broker from an `mq.m5.x` instance type to an `mq.t3.micro` instance type.
To downgrade, you must delete your broker and create a new one.
