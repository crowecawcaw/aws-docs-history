# Amazon MQ for ActiveMQ broker

configurations

A configuration contains all of the settings for your ActiveMQ broker in XML format
(similar to ActiveMQ's `activemq.xml` file). You can create a configuration
before creating any brokers. You can then apply the configuration to one or more
brokers.

###### Important

Making changes to a configuration does _not_ apply the changes to the broker immediately.
To apply your changes, you must wait for the next maintenance window
or [reboot the broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").

You can only **delete**
a configuration using the `DeleteConfiguration` API.
For more information,
see [Configurations](../api-reference/configurations-configuration-id.md "../api-reference/configurations-configuration-id.md")
in the _Amazon MQ API Reference_.

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

## Using Spring

XML configuration files

ActiveMQ brokers are configured using [Spring XML](https://docs.spring.io/spring/docs/current/spring-framework-reference/ "https://docs.spring.io/spring/docs/current/spring-framework-reference/") files. You can configure many aspects of your ActiveMQ
broker, such as predefined destinations, destination policies, authorization
policies, and plugins. Amazon MQ controls some of these configuration elements, such as
network transports and storage. Other configuration options, such as creating
networks of brokers, aren't currently supported.

The full set of supported configuration options is specified in the Amazon MQ XML
schemas. Download zip files of the supported schemas using the following
links.

- [`amazon-mq-active-mq-5.19.1.xsd.zip`](samples/amazon-mq-active-mq-5.19.1.xsd.md "samples/amazon-mq-active-mq-5.19.1.xsd.md")
- [`amazon-mq-active-mq-5.18.4.xsd.zip`](samples/amazon-mq-active-mq-5.18.4.xsd.md "samples/amazon-mq-active-mq-5.18.4.xsd.md")
- [`amazon-mq-active-mq-5.17.6.xsd.zip`](samples/amazon-mq-active-mq-5.17.6.xsd.md "samples/amazon-mq-active-mq-5.17.6.xsd.md")
- [`amazon-mq-active-mq-5.16.7.xsd.zip`](samples/amazon-mq-active-mq-5.16.7.xsd.md "samples/amazon-mq-active-mq-5.16.7.xsd.md")
- [`amazon-mq-active-mq-5.15.16.xsd.zip`](samples/amazon-mq-active-mq-5.15.16.xsd.md "samples/amazon-mq-active-mq-5.15.16.xsd.md")

You can use these schemas to validate and sanitize your configuration files. Amazon MQ
also lets you provide configurations by uploading XML files. When you upload an XML
file, Amazon MQ automatically sanitizes and removes invalid and prohibited configuration
parameters according to the schema.

###### Note

You can use only static values for attributes. Amazon MQ sanitizes elements and
attributes that contain Spring expressions, variables, and element references
from your configuration.
