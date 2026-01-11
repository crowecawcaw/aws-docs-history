# RabbitMQ tutorials

The following tutorials show how you can configure and use RabbitMQ on Amazon MQ. To learn more about working with supported client libraries in
a variety of programming languages such as Node.js, Python, .NET, and more, see [RabbitMQ Tutorials](https://www.rabbitmq.com/getstarted.html "https://www.rabbitmq.com/getstarted.html")
in the _RabbitMQ Getting Started Guide_.

###### Topics

- [Editing broker preferences](amazon-mq-rabbitmq-editing-broker-preferences.md "amazon-mq-rabbitmq-editing-broker-preferences.md")
- [Using Python Pika with Amazon MQ for RabbitMQ](amazon-mq-rabbitmq-pika.md "amazon-mq-rabbitmq-pika.md")
- [Resolving RabbitMQ paused queue synchronization](rabbitmq-queue-sync.md "rabbitmq-queue-sync.md")
- [Reducing the number of connections and channels](reducing-connections-and-channels.md "reducing-connections-and-channels.md")
- [Step 2: Connect a JVM-based application to your broker](#rabbitmq-connect-jvm-application "#rabbitmq-connect-jvm-application")
- [Step 3: (Optional) Connect to an AWS Lambda function](#rabbitmq-connect-to-lambda "#rabbitmq-connect-to-lambda")
- [Using OAuth 2.0 authentication and authorization for Amazon MQ for RabbitMQ](oauth-tutorial.md "oauth-tutorial.md")
- [Using LDAP authentication and authorization for Amazon MQ for RabbitMQ](rabbitmq-ldap-tutorial.md "rabbitmq-ldap-tutorial.md")
- [Using HTTP authentication and authorization for Amazon MQ for RabbitMQ](rabbitmq-http-tutorial.md "rabbitmq-http-tutorial.md")
- [Using SSL certificate authentication for Amazon MQ for RabbitMQ](rabbitmq-ssl-tutorial.md "rabbitmq-ssl-tutorial.md")
- [Using mTLS for AMQP and management endpoints](rabbitmq-mtls-tutorial.md "rabbitmq-mtls-tutorial.md")

## Step 2: Connect a JVM-based application to your broker

After you create a RabbitMQ broker, you can connect your application to it.
The following examples show how you can use the [RabbitMQ Java client library](https://www.rabbitmq.com/java-client.html "https://www.rabbitmq.com/java-client.html")
to create a connection to your broker, create a queue, and send a message.
You can connect to RabbitMQ brokers using supported RabbitMQ client libraries for a variety of languages. For more information on
supported RabbitMQ client libraries, see [RabbitMQ client libraries and developer tools](https://www.rabbitmq.com/devtools.html "https://www.rabbitmq.com/devtools.html").

### Prerequisites

###### Note

The following prerequisite steps are only applicable to RabbitMQ brokers created without public accessibility.
If you are creating a broker with public accessibility you can skip them.

#### Enable VPC attributes

To ensure that your broker is accessible within your VPC, you must enable the `enableDnsHostnames` and `enableDnsSupport`
VPC attributes. For more information, see [DNS Support in your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the _Amazon VPC User Guide_.

#### Enable inbound connections

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. From the broker list, choose the name of your broker (for example, **MyBroker**).
3. On the **`MyBroker`** page,
   in the **Connections** section, note the addresses and
   ports of the broker's web console URL and wire-level
   protocols.
4. In the **Details** section, under **Security and network**,
   choose the name of your security group or
   ![Pencil icon indicating an edit or modification action.](images/amazon-mq-tutorials-broker-details-link.png)
   .

The **Security Groups** page of the EC2 Dashboard
is displayed. 5. From the security group list, choose your security group. 6. At the bottom of the page, choose **Inbound**, and then choose **Edit**. 7. In the **Edit inbound rules** dialog box,
add a rule for every URL or endpoint that you want to be publicly accessible
(the following example shows how to do this for a broker web console).

    1. Choose **Add Rule**.
    2. For **Type**, select **Custom TCP**.
    3. For **Source**, leave **Custom** selected and then
     type the IP address of the system that you want to be able to
     access the web console (for example,
     `192.0.2.1`).
    4. Choose **Save**.


    Your broker can now accept inbound connections.

#### Add Java

dependencies

If you are using Apache Maven for automating builds, add the following dependency to your `pom.xml` file.
For more information on Project Object Model files in Apache Maven,
see [Introduction to the POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html "https://maven.apache.org/guides/introduction/introduction-to-the-pom.html").

```
<dependency>
    <groupId>com.rabbitmq</groupId>
    <artifactId>amqp-client</artifactId>
    <version>5.9.0</version>
</dependency>
```

If you are using [Gradle](https://docs.gradle.org/current/userguide/userguide.html "https://docs.gradle.org/current/userguide/userguide.html") for automating builds, declare the following dependency.

```
dependencies {
    compile 'com.rabbitmq:amqp-client:5.9.0'
}
```

#### Import `Connection` and `Channel` classes

RabbitMQ Java client uses `com.rabbitmq.client` as its top-level package, with `Connection` and `Channel` API classes representing
an AMQP 0-9-1 connection and channel, respectively. Import the `Connection` and `Channel` classes before using them, as shown in the following example.

```
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.Channel;
```

#### Create a `ConnectionFactory` and connect to your broker

Use the following example to create an instance of the `ConnectionFactory` class with the given parameters. Use the `setHost`
method to configure the broker endpoint you noted earlier. For `AMQPS` wire-level connections, use port `5671`.

```
ConnectionFactory factory = new ConnectionFactory();

factory.setUsername(username);
factory.setPassword(password);

//Replace the URL with your information
factory.setHost("`b-c8352341-ec91-4a78-ad9c-a43f23d325bb.mq.us-west-2.amazonaws.com`");
factory.setPort(5671);

// Allows client to establish a connection over TLS
factory.useSslProtocol();

// Create a connection
Connection conn = factory.newConnection();

// Create a channel
Channel channel = conn.createChannel();
```

#### Publish a message to an exchange

You can use `Channel.basicPublish` to publish messages to an exchange. The following example uses the AMQP `Builder`
class to build a message properties object with content-type `plain/text`.

```
byte[] messageBodyBytes = "Hello, world!".getBytes();
channel.basicPublish(exchangeName, routingKey,
             new AMQP.BasicProperties.Builder()
               .contentType("text/plain")
               .userId("userId")
               .build(),
               messageBodyBytes);
```

###### Note

Note that `BasicProperties` is an inner class of the autogenerated holder class, `AMQP`.

#### Subscribe to a queue and receive a message

You can receive a message by subscribing to a queue using the `Consumer` interface.
Once subscribed, messages will then be delivered automatically as they arrive.

The easiest way to implement a `Consumer` is to use the subclass `DefaultConsumer`.
A `DefaultConsumer` object can be passed as part of a `basicConsume` call to set up the subscription as shown in the following example.

```
boolean autoAck = false;
channel.basicConsume(queueName, autoAck, "myConsumerTag",
     new DefaultConsumer(channel) {
         @Override
         public void handleDelivery(String consumerTag,
                                    Envelope envelope,
                                    AMQP.BasicProperties properties,
                                    byte[] body)
             throws IOException
         {
             String routingKey = envelope.getRoutingKey();
             String contentType = properties.getContentType();
             long deliveryTag = envelope.getDeliveryTag();
             // (process the message components here ...)
             channel.basicAck(deliveryTag, false);
         }
     });
```

###### Note

Because we specified `autoAck = false`, it is necessary to acknowledge messages delivered to the `Consumer`,
most conveniently done in the `handleDelivery` method, as shown in the example.

#### Close your connection and disconnect from the broker

In order to disconnect from your RabbitMQ broker, close both the channel and connection as shown in the following.

```
channel.close();
conn.close();
```

###### Note

For more information on working with the RabbitMQ Java client library, see the [RabbitMQ Java Client API Guide](https://www.rabbitmq.com/api-guide.html "https://www.rabbitmq.com/api-guide.html").

## Step 3: (Optional) Connect to an AWS Lambda function

AWS Lambda can connect to and consume messages from your Amazon MQ broker.
When you connect a broker to Lambda, you create an [event source mapping](../../../lambda/latest/dg/invocation-eventsourcemapping.md "../../../lambda/latest/dg/invocation-eventsourcemapping.md")
that reads messages from a queue and invokes the function [synchronously](../../../lambda/latest/dg/invocation-sync.md "../../../lambda/latest/dg/invocation-sync.md"). The event
source mapping you create reads messages from your broker in batches and converts them into a Lambda payload in the form of a JSON object.

###### To connect your broker to a Lambda function

1. Add the following IAM role permissions to your Lambda function [execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md").
   - [mq:DescribeBroker](../api-reference/brokers-broker-id.md#brokers-broker-id-http-methods "../api-reference/brokers-broker-id.md#brokers-broker-id-http-methods")
   - [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
   - [ec2:DeleteNetworkInterface](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
   - [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
   - [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")
   - [ec2:DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
   - [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
   - [logs:CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
   - [logs:CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
   - [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")
   - [secretsmanager:GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")

###### Note

Without the necessary IAM permissions, your function will not be able to successfully read records from Amazon MQ resources. 2. (Optional) If you have created a broker without public accessibility, you must do one of the following to allow Lambda to connect to your broker:

    * Configure one NAT gateway per public subnet. For more information, see
     [Internet and service access for VPC-connected functions](../../../lambda/latest/dg/configuration-vpc.md#vpc-internet "../../../lambda/latest/dg/configuration-vpc.md#vpc-internet") in the *AWS Lambda Developer Guide*.
    * Create a connection between your Amazon Virtual Private Cloud (Amazon VPC) and Lambda using a VPC endpoint. Your Amazon VPC must also connect to AWS Security Token Service (AWS STS) and Secrets Manager endpoints.
     For more information, see [Configuring interface VPC endpoints for Lambda](../../../lambda/latest/dg/configuration-vpc-endpoints.md "../../../lambda/latest/dg/configuration-vpc-endpoints.md")
     in the *AWS Lambda Developer Guide*.

3. [Configure your broker as an event source](../../../lambda/latest/dg/with-mq.md#services-mq-eventsourcemapping "../../../lambda/latest/dg/with-mq.md#services-mq-eventsourcemapping") for a Lambda function using the AWS Management Console. You can also use the
   [`create-event-source-mapping`](../../../cli/latest/reference/lambda/create-event-source-mapping.md "../../../cli/latest/reference/lambda/create-event-source-mapping.md") AWS Command Line Interface command.
4. Write some code for your Lambda function to process the messages from your consumed from your broker. The Lambda payload that
   retrieved by your event source mapping depends on the engine type of the broker. The following is an example of a Lambda payload for an Amazon MQ for RabbitMQ queue.

###### Note

In the example, `test` is the name of the queue, and `/` is the name of the default virtual host.
When receiving messages, the event source lists messages under `test::/`.

```
{
  "eventSource": "aws:rmq",
  "eventSourceArn": "arn:aws:mq:us-west-2:112556298976:broker:test:b-9bcfa592-423a-4942-879d-eb284b418fc8",
  "rmqMessagesByQueue": {
    "test::/": [
      {
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
          }
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
  }
}
```

For more information on connecting Amazon MQ to Lambda, the options Lambda supports for an Amazon MQ event source, and event source mapping errors, see
[Using Lambda with Amazon MQ](../../../lambda/latest/dg/with-mq.md "../../../lambda/latest/dg/with-mq.md") in the _AWS Lambda Developer Guide_.
