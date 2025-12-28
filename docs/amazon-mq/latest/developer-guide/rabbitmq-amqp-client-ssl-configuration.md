# AMQP client SSL configuration

Federation and shovel use AMQP for communication between upstream and downstream brokers.

By default, _TLS peer verification_ is enabled for Amazon MQ for RabbitMQ 4.
Amazon MQ for RabbitMQ brokers use the _certfile_ (public key) and _keyfile_
(private key) configured by Amazon MQ during TLS verification. If your upstream broker is running on-premise,
it will not be able to validate the certificates and keyfile provided by the Amazon MQ
for RabbitMQ downstream broker, causing TLS verification to fail.

Amazon MQ currently does not support configuring _certfile_ and _keyfile_ with user-provided certificates.
However, for use cases that require shoveling or federating messages between Amazon MQ and on-premise brokers,
you can disable _TLS peer verification_.

###### Important

On Amazon MQ for RabbitMQ 3 SSL properties of AMQP clients is configured with RabbitMQ defaults*(verify_none)*.
Amazon MQ for RabbitMQ 3 does not support overriding these defaults.

## AMQP client SSL configuration key

| Configuration                     | Configuration Key                | Supported Values             |
| --------------------------------- | -------------------------------- | ---------------------------- |
| AMQP client SSL peer verification | `amqp_client.ssl_options.verify` | `verify_none`, `verify_peer` |

## How to override AMQP client SSL peer verification

You can override AMQP client SSL peer verification using the Amazon MQ API and Amazon MQ console on RabbitMQ 4 brokers.

The following example shows how to override the AMQP client SSL peer verification using the AWS CLI:

```

aws mq update-configuration --configuration-id <config-id> --data "$(echo "amqp_client.ssl_options.verify=verify_none" | base64 --wrap=0)"

```

A successful invocation creates a configuration revision.
You must associate the configuration to your RabbitMQ broker and reboot the broker to apply the override.
For more details see [Creating and applying broker configurations](rabbitmq-creating-applying-configurations.md "rabbitmq-creating-applying-configurations.md")

###### Important

When using `verify_none`, SSL encryption is still active, but the identity of the peer is not verified. Use this setting only when necessary and ensure that you trust the network path to the destination broker.
