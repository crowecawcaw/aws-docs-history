# Getting started: Creating and connecting to a RabbitMQ broker

A _broker_ is a message broker environment running on Amazon MQ. It is the basic building block of Amazon MQ. The combined description of the
broker instance _class_ (`m5`) and
_size_ (`large`, `medium`) is called the
_broker instance type_ (for example, `mq.m5.large`). For more information, see [What is an Amazon MQ for RabbitMQ broker?](working-with-rabbitmq.md#rabbitmq-basic-elements-broker "working-with-rabbitmq.md#rabbitmq-basic-elements-broker")

## Create a RabbitMQ broker

The first and most common Amazon MQ task is creating a broker. The following example shows how you can use the AWS Management Console to create a basic broker.

When creating an Amazon MQ for RabbitMQ broker, follow the [broker setup best practices for RabbitMQ](best-practices-broker-setup.md "best-practices-broker-setup.md")
to maximize broker performance and optimize message throughput efficiency.

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. On the **Select broker engine** page, choose **RabbitMQ**, and then choose **Next**.
3. On the **Select deployment mode** page, choose the **Deployment mode**, for example, **Cluster deployment**,
   and then choose **Next**.
   - A **single-instance broker**
     is comprised of one broker in one Availability Zone behind a Network Load Balancer (NLB).
     The broker communicates with your application and with an Amazon EBS storage volume. For more information, see
     [Option 1: Amazon MQ for RabbitMQ single-instance broker](rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-single-instance "rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-single-instance").
   - A **RabbitMQ cluster deployment for high availability**
     is a logical grouping of three RabbitMQ broker nodes behind a Network Load Balancer, each sharing users, queues, and a distributed state across multiple Availability Zones (AZ). For more information, see
     [Option 2: Amazon MQ for RabbitMQ cluster deployment](rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-cluster "rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-cluster").

4. On the **Configure settings** page, in the **Details** section, the following:
   1. Enter the Broker name.

   ###### Important

   Do not add personally identifiable information (PII) or other confidential or sensitive information in broker names.
   Broker names are accessible to other AWS services, including CloudWatch Logs. Broker names are not intended to be used for
   private or sensitive data. 2. Choose the **Broker instance type** (for example, **mq.m7g.large**). For more information, see
   [Broker instance types](broker-instance-types.md "broker-instance-types.md").

5. On the **Configure settings** page, in the **RabbitMQ access** section,
   provide a **Username** and **Password**. The following restrictions apply to broker sign-in credentials:
   - Your username can contain only alphanumeric characters, dashes, periods, and underscores (- . \_).
     This value must not contain any tilde (~) characters. Amazon MQ prohibits using `guest` as a username.
   - Your password must be at least 12 characters long, contain at least 4 unique characters and must not contain commas, colons, or equal signs (,:=).

###### Important

Do not add personally identifiable information (PII) or other confidential or sensitive information in broker usernames.
Broker usernames are accessible to other AWS services, including CloudWatch Logs. Broker usernames are not intended to be used for
private or sensitive data.

###### Note

In the **Additional settings** section, you can also configure the following:

    * [Configurations](rabbitmq-broker-configuration-parameters.md "rabbitmq-broker-configuration-parameters.md")
    * [CloudWatch logs](security-logging-monitoring.md "security-logging-monitoring.md")
    * Private access
    * [Broker maintenance window](maintaining-brokers.md "maintaining-brokers.md")

6. Choose **Next**.
7. On the **Review and create** page, you can review your selections and edit them as needed.
8. Choose **Create broker**.

While Amazon MQ creates your broker, it displays the **Creation in progress** status.

Creating the broker takes about 15 minutes.

When your broker is created successfully, Amazon MQ displays the **Running** status. 9. Choose **`MyBroker`**.

On the **`MyBroker`** page,
in the **Connect** section, note your
broker's **[RabbitMQ web console](https://www.rabbitmq.com/management.html "https://www.rabbitmq.com/management.html")** URL, for example:

```
https://b-c8349341-ec91-4a78-ad9c-a57f23f235bb.mq.us-west-2.on.aws
```

Also, note your broker's [secure-AMQP
**Endpoint**](https://www.rabbitmq.com/connections.html "https://www.rabbitmq.com/connections.html"). The following is an example
of an `amqps` endpoint exposing listener port `5671`.

```
amqps://b-c8349341-ec91-4a78-ad9c-a57f23f235bb.mq.us-west-2.on.aws:5671
```
