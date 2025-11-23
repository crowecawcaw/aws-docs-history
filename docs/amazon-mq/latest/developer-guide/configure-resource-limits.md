# Resource Limit Configuration

Amazon MQ for RabbitMQ supports configuring broker resource limits from RabbitMQ 4 onwards.
When you create a broker, Amazon MQ automatically applies default values to these resource limits.
These defaults act as guardrails to protect your broker availability while accommodating common
customer usage patterns. You can customize your broker behavior by changing the limit configuration
values to better match your specific workload requirements.
For more details about default and maximum allowed values,
see [Amazon MQ for RabbitMQ sizing guidelines](rabbitmq-sizing-guidelines.md "rabbitmq-sizing-guidelines.md").

## Resource names and configuration keys

| Resource Name        | Configuration Key                  |
| -------------------- | ---------------------------------- |
| Connection           | `connection_max`                   |
| Channel              | `channel_max_per_node`             |
| Queue                | `cluster_queue_limit`              |
| Vhost                | `vhost_max`                        |
| Shovel               | `runtime_parameters.limits.shovel` |
| Exchange             | `cluster_exchange_limit`           |
| Consumer per channel | `consumer_max_per_channel`         |
| Maximum message size | `max_message_size`                 |

## How to override resource limits

You can override resource limits using the Amazon MQ API and Amazon MQ console.

The following example shows how to override the queue count default limit using the AWS CLI:

```

aws mq update-configuration --configuration-id <config-id> --data "$(echo "cluster_queue_limit=500" | base64 --wrap=0)"

```

A successful invocation creates a configuration revision.
You must associate the configuration to your RabbitMQ broker and reboot the broker to apply the override.
For more details see [RabbitMQ Broker Configurations](rabbitmq-broker-configuration-parameters.md "rabbitmq-broker-configuration-parameters.md")

## Resource limit override errors

Associating or creating a broker with configuration values outside the supported range results in an error response similar to the following:

```

Configuration Revision N for configuration:cluster_queue_limit has limit: of value: 100000000 larger than maximum allowed limit:5000

```
