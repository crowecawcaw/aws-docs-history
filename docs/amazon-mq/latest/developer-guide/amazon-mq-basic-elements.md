# Amazon MQ for ActiveMQ brokers

## What is an Amazon MQ for ActiveMQ broker?

A _broker_ is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. The combined description of the
broker instance _class_ (`m5`) and
_size_ (`large`, `medium`) is called the
_broker instance type_ (for example, `mq.m5.large`). For more information, see [Broker instance types](broker-instance-types.md "broker-instance-types.md").

- A _single-instance broker_ is comprised of one broker
  in one Availability Zone. The broker communicates with your application and
  with an Amazon EBS or Amazon EFS storage volume.
- An _active/standby broker_
  is comprised of two brokers in two different Availability Zones,
  configured in a _redundant pair_. These brokers communicate synchronously with your application, and with Amazon EFS.

For more information, see [Deployment options for Amazon MQ for ActiveMQ brokers](amazon-mq-broker-architecture.md "amazon-mq-broker-architecture.md").

You can enable _automatic minor version upgrades_ to new minor
versions of the broker engine, as Apache releases new versions.
Automatic upgrades occur during the _maintenance window_
defined by the day of the week, the time of day (in 24-hour format), and the time zone (UTC by default).

For information about creating and managing brokers, see the following:

- [Getting started: Creating and connecting to an ActiveMQ broker](getting-started-activemq.md "getting-started-activemq.md")
- [Brokers](amazon-mq-limits.md#broker-limits "amazon-mq-limits.md#broker-limits")
- [Broker statuses](broker-statuses.md "broker-statuses.md")

### Supported wire-level protocols

You can access your brokers by using [any programming language that ActiveMQ supports](http://activemq.apache.org/cross-language-clients.html "http://activemq.apache.org/cross-language-clients.html") and by enabling TLS explicitly for the following protocols:

- [AMQP](http://activemq.apache.org/amqp.html "http://activemq.apache.org/amqp.html")
- [MQTT](http://activemq.apache.org/mqtt.html "http://activemq.apache.org/mqtt.html")
- MQTT over [WebSocket](http://activemq.apache.org/websockets.html "http://activemq.apache.org/websockets.html")
- [OpenWire](http://activemq.apache.org/openwire.html "http://activemq.apache.org/openwire.html")
- [STOMP](http://activemq.apache.org/stomp.html "http://activemq.apache.org/stomp.html")
- STOMP over WebSocket

### Attributes

An ActiveMQ broker has several attributes, for example:

- A name (`MyBroker`)
- An ID (`b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`)
- An Amazon Resource Name (ARN) (`arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`)
- An ActiveMQ Web Console URL
  (`https://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:8162`)

For more information, see [Web Console](http://activemq.apache.org/web-console.html "http://activemq.apache.org/web-console.html") in the Apache ActiveMQ documentation.

###### Important

If you specify an authorization map which doesn't include the
`activemq-webconsole` group, you can't use the ActiveMQ Web Console because the group isn't authorized to send
messages to, or receive messages from, the Amazon MQ broker.

- Wire-level protocol endpoints:

      + `amqp+ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:5671`
      + `mqtt+ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:8883`
      + `ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617`


      ###### Note

      This is an OpenWire endpoint.
      + `stomp+ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61614`
      + `wss://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61619`

  For more information, see [Configuring Transports](http://activemq.apache.org/configuring-transports.html "http://activemq.apache.org/configuring-transports.html") in the Apache ActiveMQ documentation.

###### Note

For an active/standby broker, Amazon MQ provides two ActiveMQ Web Console URLs, but only one URL is active at a time.
Likewise, Amazon MQ provides two endpoints for each wire-level protocol, but only one endpoint is active in each pair at a time.
The `-1` and `-2` suffixes denote a redundant pair.

For a full list of broker attributes, see the following in the
_Amazon MQ REST API Reference_:

- [REST Operation ID:
  Broker](../api-reference/rest-api-broker.md "../api-reference/rest-api-broker.md")
- [REST Operation ID:
  Brokers](../api-reference/rest-api-brokers.md "../api-reference/rest-api-brokers.md")
- [REST Operation
  ID: Broker Reboot](../api-reference/rest-api-broker-reboot.md "../api-reference/rest-api-broker-reboot.md")

## Broker users

An ActiveMQ _user_ is a person or an application that can access the queues and topics of an ActiveMQ broker.
You can configure users to have specific permissions. For example, you can allow some users to access the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html "http://activemq.apache.org/web-console.html").

A _group_ is a semantic label. You can assign a group to a user and configure permissions for groups to send to, receive from, and administer specific queues and topics.

###### Important

Making changes to a user does _not_ apply the changes to the user immediately.
To apply your changes, you must wait for the next maintenance window
or [reboot the broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").

For information about users and groups, see the following in the Apache ActiveMQ
documentation:

- [Authorization](http://activemq.apache.org/security.html#Security-Authorization "http://activemq.apache.org/security.html#Security-Authorization")
- [Authorization Example](http://activemq.apache.org/security.html#Security-AuthorizationExample "http://activemq.apache.org/security.html#Security-AuthorizationExample")

For information about creating, editing, and deleting ActiveMQ users, see the
following:

- [Creating an ActiveMQ
  broker user](amazon-mq-listing-managing-users.md "amazon-mq-listing-managing-users.md")
- [Users](amazon-mq-limits.md#activemq-user-limits "amazon-mq-limits.md#activemq-user-limits")

### User attributes

For a full list of user attributes, see the following in the
_Amazon MQ REST API Reference_:

- [REST Operation ID:
  User](../api-reference/rest-api-user.md "../api-reference/rest-api-user.md")
- [REST Operation ID:
  Users](../api-reference/rest-api-users.md "../api-reference/rest-api-users.md")
