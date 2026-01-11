# AMQP client SSL configuration

Federation and shovel use AMQP for communication between upstream and downstream brokers.
By default, _TLS peer verification_ is enabled for AMQP clients in Amazon MQ for RabbitMQ 4.
With this setting, federation and shovel AMQP clients running on Amazon MQ brokers will perform peer verification
when establishing connections with upstream broker.

AMQP clients running on Amazon MQ brokers support the same certificate authorities as Mozilla.
If you don't use [ACM](https://www.amazontrust.com/repository "https://www.amazontrust.com/repository"), use a certificate issued by a CA on the [Mozilla Included CA Certificate List](https://wiki.mozilla.org/CA/Included_Certificates "https://wiki.mozilla.org/CA/Included_Certificates").
If your on-premises broker uses certificates from other certificate authorities, SSL verification will fail.
You can disable _TLS peer verification_ for these use cases.

###### Important

Amazon MQ does not currently support configuring client certificates for AMQP client connections. As a result, federation and shovel cannot connect to mTLS-enabled brokers that require client certificate authentication.

###### Important

On Amazon MQ for RabbitMQ 3 SSL properties of AMQP clients is configured with RabbitMQ defaults*(verify_none)*.
Amazon MQ for RabbitMQ 3 does not support overriding these defaults.

###### Note

With the default `verify_peer` setting, you can establish federation and shovel connections between any 2 Amazon MQ brokers but this does not support establishing the connection between Amazon MQ broker and private brokers or on-premises brokers that are running with non-Amazon MQ CA certificates. To connect with private or on-premises brokers, you need to disable peer verification on the downstream Amazon MQ broker.

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
