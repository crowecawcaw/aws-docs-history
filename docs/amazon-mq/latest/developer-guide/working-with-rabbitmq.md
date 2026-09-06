

# Using Amazon MQ for RabbitMQ
<a name="working-with-rabbitmq"></a>

Amazon MQ makes it easy to create a message broker with the computing and storage resources that fit your needs. You can create, manage, and delete brokers using the AWS Management Console, Amazon MQ REST API, or the AWS Command Line Interface.

This section describes the basic elements of a message broker for ActiveMQ and RabbitMQ engine types, lists available Amazon MQ broker instance types and their statuses, and provides an overview of broker architecture and configuration options.

To learn about Amazon MQ REST APIs, see the *[Amazon MQ REST API Reference](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/)*.

## What is an Amazon MQ for RabbitMQ broker?
<a name="rabbitmq-basic-elements-broker"></a>

 A *broker* is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. The combined description of the broker instance *class* (`m7g`) and *size* (`large`, `medium`) is called the *broker instance type* (for example, `mq.m7g.large`). 
+ A *single-instance broker* consists of one broker in one Availability Zone behind a Network Load Balancer (NLB). The broker communicates with your application and with an Amazon EBS storage volume.
+ A *cluster deployment* is a logical grouping of three RabbitMQ broker nodes behind a Network Load Balancer, each sharing users, queues, and a distributed state across multiple Availability Zones (AZ).

For more information, see [Deploying a RabbitMQ broker. ](rabbitmq-broker-architecture.md)

### Listener ports
<a name="rabbitmq-broker-listeners"></a>

 Amazon MQ managed RabbitMQ brokers support the following listener ports for application-level connectivity via `amqps`. You can also use these ports for client connections using the RabbitMQ web console and the management API. All connections use TLS encryption for security. 
+ Listener port `5671` - Used for secure AMQP connections made via the secure AMQP URL. This port supports both AMQP 0-9-1 and AMQP 1.0 protocols in RabbitMQ 4. For example, given a broker with broker ID `b-c8352341-ec91-4a78-ad9c-a43f23d325bb`, deployed in the `us-west-2` region, the following is the broker's full `amqps` URL: `b-c8352341-ec91-4a78-ad9c-a43f23d325bb.mq.us-west-2.amazonaws.com:5671`.
+ Listener ports `443` and `15671` - You can use both listener ports interchangeably to access a broker via the RabbitMQ web console or the management API. Port 443 provides standard HTTPS access, while port 15671 is the traditional RabbitMQ management port with TLS encryption.

### Attributes
<a name="broker-attributes"></a>

A RabbitMQ broker has several attributes:
+ A name. For example, `MyBroker`.
+ An ID. For example, `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`.
+ An Amazon Resource Name (ARN). For example, `arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`.
+ A RabbitMQ web console URL. For example, `https://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com`.

  For more information, see [RabbitMQ web console](https://www.rabbitmq.com/management.html) in the RabbitMQ documentation.
+ A secure AMQP endpoint. For example, `amqps://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com`.

For a full list of broker attributes, see the following in the *Amazon MQ REST API Reference*:
+ [REST Operation ID: Broker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker.html)
+ [REST Operation ID: Brokers](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-brokers.html)
+ [REST Operation ID: Broker Reboot](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/rest-api-broker-reboot.html)