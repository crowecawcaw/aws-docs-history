# Plugins

Amazon MQ for RabbitMQ also supports the following plugins.

- [RabbitMQ management plugin](#rabbitmq-management-plugin "#rabbitmq-management-plugin")
- [Shovel plugin](#rabbitmq-shovel-plugin "#rabbitmq-shovel-plugin")
- [Federation plugin](#rabbitmq-federation-plugin "#rabbitmq-federation-plugin")
- [Consistent Hash exchange plugin](#rabbitmq-consistent-hash-exchange "#rabbitmq-consistent-hash-exchange")
- [OAuth 2 plugin](#rabbitmq-oauth-plugin "#rabbitmq-oauth-plugin")
- [LDAP plugin](#rabbitmq-ldap-plugin "#rabbitmq-ldap-plugin")
- [HTTP plugin](#rabbitmq-http-plugin "#rabbitmq-http-plugin")
- [SSL certificate plugin](#rabbitmq-ssl-plugin "#rabbitmq-ssl-plugin")
- [aws plugin](#rabbitmq-aws-plugin "#rabbitmq-aws-plugin")
- [JMS Topic Exchange plugin](#rabbitmq-jms-topic-exchange-plugin "#rabbitmq-jms-topic-exchange-plugin")

## RabbitMQ management plugin

Amazon MQ for RabbitMQ supports the [RabbitMQ management plugin](https://www.rabbitmq.com/management.html "https://www.rabbitmq.com/management.html"), which provides an HTTP-based
management API along with a browser based UI for the RabbitMQ web console. You can use the web console
and the management API to create and manage broker users and policies.

## Shovel plugin

Amazon MQ for RabbitMQ supports the [RabbitMQ shovel plugin](https://www.rabbitmq.com/shovel.html "https://www.rabbitmq.com/shovel.html"), which allows you to move messages from
queues and exchanges on one broker to another. You can use shovel to connect loosely coupled brokers and
distribute messages away from nodes with heavier message loads.

###### Important

You cannot configure shovel between queues or exchanges if the shovel destination is a private broker.

Amazon MQ does not support using static shovels.

Only [dynamic shovels](https://www.rabbitmq.com/shovel-dynamic.html "https://www.rabbitmq.com/shovel-dynamic.html") are supported. Dynamic shovels are configured using runtime parameters and can be
started and stopped at any time programmatically by a client connection. For example, using the RabbitMQ
management API, you can create a PUT request to the following API endpoint to configure a dynamic shovel. In
the example, {vhost} can be replaced by the name of the broker's vhost, and {name} replaced by the name of
the new dynamic shovel.

```
/api/parameters/shovel/{vhost}/{name}
```

In the request body, you must specify either a queue or an exchange but not both. This example below
configures a dynamic shovel between a local queue specified in src-queue and a remote queue defined in dest-queue. Similarly, you can use src-exchange and dest-exchange parameters to configure a shovel between two
exchanges.

```
{
"value": {
"src-protocol": "amqp091",
"src-uri": "amqp://localhost",
"src-queue": "source-queue-name",
"dest-protocol": "amqp091",
"dest-uri": "amqps://b-c8352341-ec91-4a78-ad9c-a43f23d325bb.mq.us-west2.amazonaws.com:5671",
"dest-queue": "destination-queue-name"
}
}
```

## Federation plugin

Amazon MQ supports federated exchanges and queues using the [RabbitMQ federation plugin](https://www.rabbitmq.com/federation.html "https://www.rabbitmq.com/federation.html"). With
federation, you can replicate the flow of messages between queues, exchanges and consumers on separate
brokers. Federated queues and exchanges use point-to-point links to connect to peers in other brokers. While
federated exchanges, by default, route messages once, federated queues can move messages any number of
times as needed by consumers.

You can use federation to allow a downstream broker to consume a message from an exchange or a queue on
an upstream. You can enable federation on downstream brokers by using the RabbitMQ web console or the
management API.

###### Important

You cannot configure federation if the upstream queue or exchange is in a private broker. You can only
configure federation between queues or exchanges in public brokers, or between an upstream queue or
exchange in a public broker, and a downstream queue or exchange in a private broker.

For example, using the management API, you can configure federation by doing the following.

- Configure one or more upstreams that define federation connections to other nodes. You can define
  federation connections by using the RabbitMQ web console or the management API. Using the
  management API, you can create a POST request to /api/parameters/federation-upstream/%2f/myupstream with the following request body.

```
{"value":{"uri":"amqp://server-name","expires":3600000}}
```

- Configure a policy to enable your queues or exchanges to become federated. You can configure policies
  by using the RabbitMQ web console, or the management API. Using the management API, you can
  create a POST request to /api/policies/%2f/federate-me with the following request body.

```
{"pattern":"^amq\.", "definition":{"federation-upstream-set":"all"}, "apply-to":"exchanges"}
```

###### Note

The request body assumes exchanges on the server are named beginning with amq. Using regular
expression ^amq\. will ensure that federation is enabled for all exchanges whose names begin with "amq." The
exchanges on your RabbitMQ server can be named differently.

## Consistent Hash exchange plugin

Amazon MQ for RabbitMQ supports the [RabbitMQ Consistent Hash Exchange Type plugin](https://github.com/rabbitmq/rabbitmq-consistent-hash-exchange "https://github.com/rabbitmq/rabbitmq-consistent-hash-exchange"). Consistent Hash
exchanges route messages to queues based on a hash value calculated from the routing key of a message.
Given a reasonably even routing key, Consistent Hash exchanges can distribute messages between queues
reasonably evenly.

For queues bound to a Consistent Hash exchange, the binding key is a number-as-a-string that determines
the binding weight of each queue. Queues with a higher binding weight will receive a proportionally higher
distribution of messages from the Consistent Hash exchange to which they are bound. In a Consistent Hash
exchange topology, publishers can simply publish messages to the exchange, but consumers must be explicitly
configured to consume messages from specific queues.

## OAuth 2.0 plugin

Amazon MQ for RabbitMQ supports the [OAuth 2 authentication backend plugin](https://github.com/rabbitmq/rabbitmq-auth-backend-oauth2 "https://github.com/rabbitmq/rabbitmq-auth-backend-oauth2"). This plugin is conditionally
enabled based on your broker configuration. When enabled, this plugin provides OAuth 2.0 authentication and
authorization with integration to external OAuth 2.0 identity providers for centralized user management and
access control. For more information about OAuth 2.0 authentication, see [OAuth 2.0 authentication and authorization](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md").

## LDAP plugin

Amazon MQ for RabbitMQ supports the [LDAP authentication backend plugin](https://github.com/rabbitmq/rabbitmq-auth-backend-ldap "https://github.com/rabbitmq/rabbitmq-auth-backend-ldap"). This plugin is conditionally
enabled based on your broker configuration. When enabled, this plugin provides LDAP authentication and
authorization with integration to external LDAP directory services for centralized user authentication and
authorization. For more information about LDAP authentication, see [LDAP authentication and authorization](ldap-for-amq-for-rabbitmq.md "ldap-for-amq-for-rabbitmq.md").

## HTTP plugin

Amazon MQ for RabbitMQ supports the [HTTP authentication backend plugin](https://github.com/rabbitmq/rabbitmq-auth-backend-http "https://github.com/rabbitmq/rabbitmq-auth-backend-http"). This plugin is conditionally
enabled based on your broker configuration. When enabled, this plugin provides HTTP authentication and
authorization with integration to external HTTP servers for centralized user authentication and
authorization. For more information about HTTP authentication, see [HTTP authentication and authorization](http-for-amq-for-rabbitmq.md "http-for-amq-for-rabbitmq.md").

###### Note

The HTTP authentication plugin is only available for Amazon MQ for RabbitMQ version 4 and above.

## SSL certificate plugin

Amazon MQ supports mutual TLS (mTLS) for RabbitMQ brokers. The [SSL authentication plugin](https://github.com/rabbitmq/rabbitmq-auth-mechanism-ssl "https://github.com/rabbitmq/rabbitmq-auth-mechanism-ssl") uses client certificates from mTLS connections to authenticate users. This plugin is conditionally
enabled based on your broker configuration. When enabled, it provides certificate-based authentication
using X.509 client certificates for strong authentication without transmitting credentials over the network.
For more information about SSL certificate authentication, see [SSL certificate authentication](ssl-for-amq-for-rabbitmq.md "ssl-for-amq-for-rabbitmq.md").

###### Note

The SSL certificate authentication plugin is only available for Amazon MQ for RabbitMQ version 4 and above.

## aws plugin

The [aws plugin](https://github.com/rabbitmq/rabbitmq-aws "https://github.com/rabbitmq/rabbitmq-aws") is conditionally enabled by Amazon MQ for RabbitMQ based on your broker configuration. This
community plugin, developed and maintained by Amazon MQ, provides secure retrieval of credentials and
certificates from AWS services using AWS ARNs in RabbitMQ configuration settings. For more information
about ARN support, see [ARN support in RabbitMQ configuration](arn-support-rabbitmq-configuration.md "arn-support-rabbitmq-configuration.md").

## JMS Topic Exchange plugin

The [JMS Topic Exchange Plugin](https://github.com/rabbitmq/rabbitmq-server/tree/main/deps/rabbitmq_jms_topic_exchange "https://github.com/rabbitmq/rabbitmq-server/tree/main/deps/rabbitmq_jms_topic_exchange") is
always enabled by Amazon MQ for RabbitMQ. It works with [RabbitMQ JMS client](https://github.com/rabbitmq/rabbitmq-jms-client "https://github.com/rabbitmq/rabbitmq-jms-client") to allow new and existing
JMS applications to connect to Amazon MQ for RabbitMQ.

###### Note

The JMS Topic Exchange plugin is only available for Amazon MQ for RabbitMQ version 4 and above. It is enabled by default but only activates when the RabbitMQ JMS client is used to run JMS workloads.
