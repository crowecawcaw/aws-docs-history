# Amazon MQ for RabbitMQ broker configurations

A configuration contains all of the settings for your RabbitMQ broker in Cuttlefish format.
You can create a configuration before creating any brokers.
You can then apply the configuration to one or more brokers.

## Attributes

A broker configuration has several attributes, for example:

- A name (`MyConfiguration`)
- An ID (`c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`)
- An Amazon Resource Name (ARN)
  (`arn:aws:mq:us-east-2:123456789012:configuration:c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`)

For a full list of configuration attributes, see the following in the
_Amazon MQ REST API Reference_:

- [REST Operation
  ID: Configuration](../api-reference/rest-api-configuration.md "../api-reference/rest-api-configuration.md")
- [REST Operation
  ID: Configurations](../api-reference/rest-api-configurations.md "../api-reference/rest-api-configurations.md")

For a full list of configuration revision attributes, see the
following:

- [REST
  Operation ID: Configuration Revision](../api-reference/rest-api-configuration-revision.md "../api-reference/rest-api-configuration-revision.md")
- [REST
  Operation ID: Configuration Revisions](../api-reference/rest-api-configuration-revisions.md "../api-reference/rest-api-configuration-revisions.md")

###### Topics

- [Creating and applying RabbitMQ broker configurations](rabbitmq-creating-applying-configurations.md "rabbitmq-creating-applying-configurations.md")
- [Edit a
  Amazon MQ for RabbitMQ Configuration Revision](edit-current-rabbitmq-configuration-console.md "edit-current-rabbitmq-configuration-console.md")
- [Configurable values for RabbitMQ on Amazon MQ](rabbitmq-configuration-policies.md "rabbitmq-configuration-policies.md")
- [OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ](oauth-for-amq-for-rabbitmq.md "oauth-for-amq-for-rabbitmq.md")
