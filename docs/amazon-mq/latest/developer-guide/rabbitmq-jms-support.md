# Amazon MQ for RabbitMQ JMS support

You can now run JMS 1.1, 2.0, and 3.1 workloads on Amazon MQ for RabbitMQ 4 with RabbitMQ JMS client.

## RabbitMQ JMS client

The RabbitMQ JMS client is an open-source JMS client library that you need to connect your JMS application to Amazon MQ RabbitMQ brokers. For more information, please visit the [official GitHub repository](https://github.com/rabbitmq/rabbitmq-jms-client "https://github.com/rabbitmq/rabbitmq-jms-client").

## Supported JMS 1.1, 2.0 and 3.1 APIs

From Amazon MQ for RabbitMQ 4 onward, the plugin `jms-topic-exchange` is always enabled. Hence, you can use Amazon MQ for RabbitMQ 4 and RabbitMQ JMS client for your JMS workload.
All JMS APIs defined in the [JMS 1.1](https://javaee.github.io/jms-spec/pages/JMS20FinalRelease#reference-implementation "https://javaee.github.io/jms-spec/pages/JMS20FinalRelease#reference-implementation") are supported except:

- Server sessions APIs are not supported.
- XA transaction APIs are not supported.
- JMS selector for JMS Queue destination is not supported.
- JMS `NoLocal` subscription attribute is not supported.

All newly added APIs in [JMS 2.0 and JMS 3.1](https://javaee.github.io/jms-spec/pages/JMS20FinalRelease#reference-implementation "https://javaee.github.io/jms-spec/pages/JMS20FinalRelease#reference-implementation") are supported except:

- `JMSProducer.setDeliveryDelay` API is not supported.

To learn more about connecting your JMS application to Amazon MQ for RabbitMQ broker, please see the tutorial on [Connecting your JMS application to Amazon MQ for RabbitMQ broker](rabbitmq-tutorial-jms.md "rabbitmq-tutorial-jms.md")

## Authentication and Authorization

All authentication and authorization mechanisms listed in [this section](rabbitmq-authentication.md "rabbitmq-authentication.md") are supported. The credentials used for connecting to the broker using the JMS client are the same as if you were connecting to the RabbitMQ broker using an AMQP Java client.

## Interoperability with AMQP queues on RabbitMQ

You can use the RabbitMQ JMS client to send JMS messages to an AMQP exchange and consume messages from an AMQP queue (this feature does not support JMS topics). This enables you to interoperate or migrate certain JMS workloads to AMQP workloads.
For more information, please visit the [official client documentation](https://rabbitmq.github.io/rabbitmq-jms-client/2.x/stable/htmlsingle/index.html#destination-interoperability "https://rabbitmq.github.io/rabbitmq-jms-client/2.x/stable/htmlsingle/index.html#destination-interoperability").
