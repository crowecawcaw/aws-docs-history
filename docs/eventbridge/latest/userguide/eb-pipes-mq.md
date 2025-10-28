# Amazon MQ message broker as a source in EventBridge Pipes

You can use EventBridge Pipes to receive records from an Amazon MQ message broker. You can then
optionally filter or enhance these records before sending them to one of the available
destinations for processing. There are settings specific to Amazon MQ that you can choose when
setting up a pipe. EventBridge Pipes maintains the order of the records from the message broker when
sending that data to the destination.

Amazon MQ is a managed message broker service for [Apache ActiveMQ](https://activemq.apache.org/ "https://activemq.apache.org/") and [RabbitMQ](https://www.rabbitmq.com/ "https://www.rabbitmq.com/"). A
message broker enables software applications and components to communicate using different
programming languages, operating systems, and formal messaging protocols with either topics or
queues as event destinations.

Amazon MQ can also manage Amazon Elastic Compute Cloud (Amazon EC2) instances on your behalf by installing ActiveMQ or
RabbitMQ brokers. After a broker is installed, it provides different network topologies and
other infrastructure needs to your instances.

The Amazon MQ source has the following configuration restrictions:

- Cross account – EventBridge doesn’t support cross-account
  processing. You can’t use EventBridge to process records from an Amazon MQ message broker that is in a
  different AWS account.
- Authentication – For ActiveMQ, only the [ActiveMQ
  SimpleAuthenticationPlugin](https://activemq.apache.org/security#simple-authentication-plugin "https://activemq.apache.org/security#simple-authentication-plugin") is supported. For RabbitMQ, only the [PLAIN](https://www.rabbitmq.com/access-control.html#mechanisms "https://www.rabbitmq.com/access-control.html#mechanisms") authentication
  mechanism is supported. To manage credentials, use AWS Secrets Manager. For more information about
  ActiveMQ authentication, see [Integrating ActiveMQ brokers
  with LDAP](../../../amazon-mq/latest/developer-guide/security-authentication-authorization.md "../../../amazon-mq/latest/developer-guide/security-authentication-authorization.md") in the Amazon MQ Developer Guide.
- Connection quota – Brokers have a maximum number
  of allowed connections for each wire-level protocol. This quota is based on the broker
  instance type. For more information, see the [Brokers](../../../amazon-mq/latest/developer-guide/amazon-mq-limits.md#broker-limits "../../../amazon-mq/latest/developer-guide/amazon-mq-limits.md#broker-limits") section of
  **\*Quotas in Amazon MQ\*** in the Amazon MQ Developer Guide.
- Connectivity – You can create brokers in a public
  or private virtual private cloud (VPC). For private VPCs, your pipe needs access to the VPC
  to receive messages.
- Event destinations – Only queue destinations are
  supported. However, you can use a virtual topic, which behaves as both a topic internally
  and as a queue externally when it interacts with your pipes. For more information, see
  [Virtual
  Destinations](https://activemq.apache.org/virtual-destinations "https://activemq.apache.org/virtual-destinations") on the Apache ActiveMQ website, and [Virtual Hosts](https://www.rabbitmq.com/vhosts.html "https://www.rabbitmq.com/vhosts.html") on the RabbitMQ
  website.
- Network topology – For ActiveMQ, only one
  single-instance or standby broker is supported for pipe. For RabbitMQ, only one
  single-instance broker or cluster deployment is supported for each pipe. Single-instance
  brokers require a failover endpoint. For more information about these broker deployment
  modes, see [Active MQ Broker
  Architecture](../../../amazon-mq/latest/developer-guide/amazon-mq-broker-architecture.md "../../../amazon-mq/latest/developer-guide/amazon-mq-broker-architecture.md") and [Rabbit MQ Broker Architecture](../../../amazon-mq/latest/developer-guide/rabbitmq-broker-architecture.md "../../../amazon-mq/latest/developer-guide/rabbitmq-broker-architecture.md") in the Amazon MQ Developer Guide.
- Protocols – Supported protocols depend on the
  Amazon MQ integration that you use.

      + For ActiveMQ integrations, EventBridge uses the OpenWire/Java Message Service (JMS)
       protocol to consume messages. Message consumption isn’t supported on any other protocol.
       EventBridge only supports the [TextMessage](https://activemq.apache.org/maven/apidocs/org/apache/activemq/command/ActiveMQTextMessage.html "https://activemq.apache.org/maven/apidocs/org/apache/activemq/command/ActiveMQTextMessage.html") and [BytesMessage](https://activemq.apache.org/maven/apidocs/org/apache/activemq/command/ActiveMQBytesMessage.html "https://activemq.apache.org/maven/apidocs/org/apache/activemq/command/ActiveMQBytesMessage.html") operations within the JMS protocol. For more information about
       the OpenWire protocol, see [OpenWire](https://activemq.apache.org/openwire.html "https://activemq.apache.org/openwire.html") on the Apache ActiveMQ website.
      + For RabbitMQ integrations, EventBridge uses the AMQP 0-9-1 protocol to consume messages. No
       other protocols are supported for consuming messages. For more information about
       RabbitMQ's implementation of the AMQP 0-9-1 protocol, see [AMQP 0-9-1 Complete Reference
       Guide](https://www.rabbitmq.com/amqp-0-9-1-reference.html "https://www.rabbitmq.com/amqp-0-9-1-reference.html") on the RabbitMQ website.

  EventBridge automatically supports the latest versions of ActiveMQ and RabbitMQ that Amazon MQ
  supports. For the latest supported versions, see [Amazon MQ release notes](../../../amazon-mq/latest/developer-guide/amazon-mq-release-notes.md "../../../amazon-mq/latest/developer-guide/amazon-mq-release-notes.md") in the
  Amazon MQ Developer Guide.

###### Note

By default, Amazon MQ has a weekly maintenance window for brokers. During that window of time,
brokers are unavailable. For brokers without standby, EventBridge won’t process messages until the
window ends.

**Example events**

The following sample event shows the information that is received by the pipe. You can use
this event to create and filter your event patterns, or to define input transformation. Not all
of the fields can be filtered. For more information about which fields you can filter, see [Event filtering in Amazon EventBridge Pipes](eb-pipes-event-filtering.md "eb-pipes-event-filtering.md").

**ActiveMQ**

```
[
  {
    "eventSource": "aws:amq",
    "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:test:b-9bcfa592-423a-4942-879d-eb284b418fc8",
    "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",
    "messageType": "jms/text-message",
    "data": "QUJDOkFBQUE=",
    "connectionId": "myJMSCoID",
    "redelivered": false,
    "destination": {
      "physicalname": "testQueue"
    },
    "timestamp": 1598827811958,
    "brokerInTime": 1598827811958,
    "brokerOutTime": 1598827811959
  },
  {
    "eventSource": "aws:amq",
    "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:test:b-9bcfa592-423a-4942-879d-eb284b418fc8",
    "messageID": "ID:b-9bcfa592-423a-4942-879d-eb284b418fc8-1.mq.us-west-2.amazonaws.com-37557-1234520418293-4:1:1:1:1",
    "messageType": "jms/bytes-message",
    "data": "3DTOOW7crj51prgVLQaGQ82S48k=",
    "connectionId": "myJMSCoID1",
    "persistent": false,
    "destination": {
      "physicalname": "testQueue"
    },
    "timestamp": 1598827811958,
    "brokerInTime": 1598827811958,
    "brokerOutTime": 1598827811959
  }
]
```

**RabbitMQ**

```
[
  {
    "eventSource": "aws:rmq",
    "eventSourceArn": "arn:aws:mq:us-west-2:111122223333:broker:pizzaBroker:b-9bcfa592-423a-4942-879d-eb284b418fc8",
    "eventSourceKey": "pizzaQueue::/",
    "basicProperties": {
      "contentType": "text/plain",
      "contentEncoding": null,
      "headers": {
        "header1": {
          "bytes": [
            118,
            97,
            108,
            117,
            101,
            49
          ]
        },
        "header2": {
          "bytes": [
            118,
            97,
            108,
            117,
            101,
            50
          ]
        },
        "numberInHeader": 10
      },
      "deliveryMode": 1,
      "priority": 34,
      "correlationId": null,
      "replyTo": null,
      "expiration": "60000",
      "messageId": null,
      "timestamp": "Jan 1, 1970, 12:33:41 AM",
      "type": null,
      "userId": "AIDACKCEVSQ6C2EXAMPLE",
      "appId": null,
      "clusterId": null,
      "bodySize": 80
    },
    "redelivered": false,
    "data": "eyJ0aW1lb3V0IjowLCJkYXRhIjoiQ1pybWYwR3c4T3Y0YnFMUXhENEUifQ=="
  }
]
```

## Consumer group

To interact with Amazon MQ, EventBridge creates a consumer group that can read from your Amazon MQ
brokers. The consumer group is created with the same ID as the pipe UUID.

For Amazon MQ sources, EventBridge batches records together and sends them to your function in a
single payload. To control behavior, you can configure the batching window and batch size.
EventBridge pulls messages until one of the following occurs:

- The processed records reach the payload size maximum of 6 MB.
- The batching window expires.
- The number of records reaches the full batch size.

EventBridge converts your batch into a single payload and then invokes your function. Messages
aren't persisted or deserialized. Instead, the consumer group retrieves them as a BLOB of
bytes. It then base64-encodes them into a JSON payload. If the pipe returns an error for any
of the messages in a batch, EventBridge retries the entire batch of messages until processing
succeeds or the messages expire.

## Network configuration

By default, Amazon MQ brokers are created with the `PubliclyAccessible` flag set to
false. It's only when `PubliclyAccessible` is set to true that the broker receives
a public IP address. For full access with your pipe, your broker must either use a public
endpoint or provide access to the VPC.

If your Amazon MQ broker isn't publicly accessible, EventBridge must have access to the Amazon Virtual Private Cloud
(Amazon VPC) resources associated with your broker.

- To access the VPC of your Amazon MQ brokers, EventBridge can use outbound internet access for the
  subnets of your source. For public subnets this must be a managed [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md"). For private subnets it
  can be a NAT gateway, or your own NAT. Ensure that the NAT has a public IP address and can
  connect to the internet.
- EventBridge Pipes also supports event delivery through [AWS PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/"), allowing
  you to send events from an event source located in an Amazon Virtual Private Cloud (Amazon VPC) to a Pipes target without traversing the public internet. You can use Pipes
  to poll from Amazon Managed Streaming for Apache Kafka (Amazon MSK), self-managed Apache Kafka, and
  Amazon MQ sources residing in a private subnet without the need to deploy an
  internet gateway, configure firewall rules, or set up proxy servers.

To set up a VPC endpoint, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws")
in the _AWS PrivateLink User Guide_.
For service name, select `com.amazonaws.`region`.pipes-data`.

Configure your Amazon VPC security groups with the following rules (at minimum):

- Inbound rules – Allow all traffic on the Amazon MQ broker port for the security groups specified for your source.
- Outbound rules – Allow all traffic on port 443 for all destinations. Allow all traffic on the Amazon MQ
  broker port for the security groups
  specified for your source.

Broker ports include:

    + 9092 for plaintext
    + 9094 for TLS
    + 9096
     for SASL
    + 9098 for IAM

###### Note

Your Amazon VPC configuration is discoverable through the [Amazon MQ API](../../../amazon-mq/latest/api-reference/resources.md "../../../amazon-mq/latest/api-reference/resources.md"). You don't need to configure it during
setup.
