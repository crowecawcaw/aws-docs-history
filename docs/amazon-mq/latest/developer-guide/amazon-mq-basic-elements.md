

# Amazon MQ for ActiveMQ brokers
<a name="amazon-mq-basic-elements"></a>

## What is an Amazon MQ for ActiveMQ broker?
<a name="broker"></a>

A *broker* is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. The combined description of the broker instance *class* (`m5`) and *size* (`large`, `medium`) is called the *broker instance type* (for example, `mq.m5.large`). For more information, see [Amazon MQ for ActiveMQ broker instance types](broker-instance-types.md).
+ A *single-instance broker* is comprised of one broker in one Availability Zone. The broker communicates with your application and with an Amazon EBS or Amazon EFS storage volume.
+ An *active/standby broker* is comprised of two brokers in two different Availability Zones, configured in a *redundant pair*. These brokers communicate synchronously with your application, and with Amazon EFS.

For more information, see [Deployment options for Amazon MQ for ActiveMQ brokers](amazon-mq-broker-architecture.md).

You can enable *automatic minor version upgrades* to new minor versions of the broker engine, as Apache releases new versions. Automatic upgrades occur during the *maintenance window* defined by the day of the week, the time of day (in 24-hour format), and the time zone (UTC by default).

For information about creating and managing brokers, see the following:
+ [Getting started: Creating and connecting to an ActiveMQ broker](getting-started-activemq.md)
+ [Brokers](amazon-mq-limits.md#broker-limits)
+ [Amazon MQ broker statuses](broker-statuses.md)

### Supported wire-level protocols
<a name="broker-protocols"></a>

You can access your brokers by using [any programming language that ActiveMQ supports](https://activemq.apache.org/cross-language-clients.html) and by enabling TLS explicitly for the following protocols:
+ [AMQP](https://activemq.apache.org/amqp.html)
+ [MQTT](https://activemq.apache.org/mqtt.html)
+ MQTT over [WebSocket](https://activemq.apache.org/websockets.html)
+ [OpenWire](https://activemq.apache.org/openwire.html)
+ [STOMP](https://activemq.apache.org/stomp.html)
+ STOMP over WebSocket

### Attributes
<a name="broker-attributes"></a>

An ActiveMQ broker has several attributes, for example:
+ A name (`MyBroker`)
+ An ID (`b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`)
+ An Amazon Resource Name (ARN) (`arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`)
+ An ActiveMQ Web Console URL (`https://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:8162`)

  For more information, see [Web Console](https://activemq.apache.org/web-console.html) in the Apache ActiveMQ documentation.
**Important**  
If you specify an authorization map which doesn't include the `activemq-webconsole` group, you can't use the ActiveMQ Web Console because the group isn't authorized to send messages to, or receive messages from, the Amazon MQ broker.
+ Wire-level protocol endpoints:
  + `amqp+ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:5671`
  + `mqtt+ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:8883`
  + `ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617`
**Note**  
This is an OpenWire endpoint.
  + `stomp+ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61614`
  + `wss://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61619`

  For more information, see [Configuring Transports](https://activemq.apache.org/configuring-transports.html) in the Apache ActiveMQ documentation.

**Note**  
For an active/standby broker, Amazon MQ provides two ActiveMQ Web Console URLs, but only one URL is active at a time. Likewise, Amazon MQ provides two endpoints for each wire-level protocol, but only one endpoint is active in each pair at a time. The `-1` and `-2` suffixes denote a redundant pair.

For a full list of broker attributes, see the following in the *Amazon MQ REST API Reference*:
+ [REST Operation ID: Broker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker.html)
+ [REST Operation ID: Brokers](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-brokers.html)
+ [REST Operation ID: Broker Reboot](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker-reboot.html)

## Broker users
<a name="user"></a>

An ActiveMQ *user* is a person or an application that can access the queues and topics of an ActiveMQ broker. You can configure users to have specific permissions. For example, you can allow some users to access the [ActiveMQ Web Console](https://activemq.apache.org/web-console.html).

A *group* is a semantic label. You can assign a group to a user and configure permissions for groups to send to, receive from, and administer specific queues and topics.

**Important**  
Making changes to a user does *not* apply the changes to the user immediately. To apply your changes, you must wait for the next maintenance window or [reboot the broker](amazon-mq-rebooting-broker.md).

For information about users and groups, see the following in the Apache ActiveMQ documentation:
+ [Authorization](https://activemq.apache.org/security.html#Security-Authorization)
+ [Authorization Example](https://activemq.apache.org/security.html#Security-AuthorizationExample)

For information about creating, editing, and deleting ActiveMQ users, see the following:
+ [Creating an ActiveMQ broker user](amazon-mq-listing-managing-users.md)
+ [Users](amazon-mq-limits.md#activemq-user-limits)

### User attributes
<a name="user-attributes"></a>

For a full list of user attributes, see the following in the *Amazon MQ REST API Reference*:
+ [REST Operation ID: User](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-user.html)
+ [REST Operation ID: Users](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-users.html)