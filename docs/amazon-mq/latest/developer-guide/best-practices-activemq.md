# Amazon MQ for ActiveMQ best practices

Use this as a reference to quickly find recommendations for maximizing performance and minimizing throughput costs when working with
ActiveMQ brokers on Amazon MQ.

## Never Modify or Delete the Amazon MQ Elastic Network Interface

When you first [create an
Amazon MQ broker](getting-started-activemq.md "getting-started-activemq.md"), Amazon MQ provisions an [elastic network
interface](../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md "../../../vpc/latest/userguide/VPC_ElasticNetworkInterfaces.md") in the [Virtual Private Cloud (VPC)](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md") under your account and, thus, requires a
number of [EC2
permissions](security-api-authentication-authorization.md "security-api-authentication-authorization.md"). The network interface allows your client (producer or
consumer) to communicate with the Amazon MQ broker. The network interface is considered
to be within the _service scope_ of Amazon MQ, despite being part of
your account's VPC.

###### Warning

You must not modify or delete this network interface. Modifying or deleting
the network interface can cause a permanent loss of connection between your VPC
and your broker.

![Diagram showing Client, Elastic Network Interface, and Amazon MQ Broker within a Customer VPC and service scope.](images/amazon-mq-network-configuration-architecture-vpc-elastic-network-interface.png)

## Always Use Connection Pooling

In a scenario with a single producer and single consumer (such as the [Getting started: Creating and connecting to an ActiveMQ broker](getting-started-activemq.md "getting-started-activemq.md")
tutorial), you can use a single [`ActiveMQConnectionFactory`](http://activemq.apache.org/maven/apidocs/org/apache/activemq/ActiveMQConnectionFactory.html "http://activemq.apache.org/maven/apidocs/org/apache/activemq/ActiveMQConnectionFactory.html") class for every producer and
consumer. For example:

```
// Create a connection factory.
final ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(wireLevelEndpoint);

// Pass the sign-in credentials.
connectionFactory.setUserName(activeMqUsername);
connectionFactory.setPassword(activeMqPassword);

// Establish a connection for the consumer.
final Connection consumerConnection = connectionFactory.createConnection();
consumerConnection.start();
```

However, in more realistic scenarios with multiple producers and consumers, it can
be costly and inefficient to create a large number of connections for multiple
producers. In these scenarios, you should group multiple producer requests using the
[`PooledConnectionFactory`](http://activemq.apache.org/maven/apidocs/org/apache/activemq/jms/pool/PooledConnectionFactory.html "http://activemq.apache.org/maven/apidocs/org/apache/activemq/jms/pool/PooledConnectionFactory.html") class. For example:

###### Note

Message consumers should _never_ use the
`PooledConnectionFactory` class.

```
// Create a connection factory.
final ActiveMQConnectionFactory connectionFactory = new ActiveMQConnectionFactory(wireLevelEndpoint);

// Pass the sign-in credentials.
connectionFactory.setUserName(activeMqUsername);
connectionFactory.setPassword(activeMqPassword);

// Create a pooled connection factory.
final PooledConnectionFactory pooledConnectionFactory = new PooledConnectionFactory();
pooledConnectionFactory.setConnectionFactory(connectionFactory);
pooledConnectionFactory.setMaxConnections(10);

// Establish a connection for the producer.
final Connection producerConnection = pooledConnectionFactory.createConnection();
producerConnection.start();
```

## Always Use the Failover Transport to Connect to Multiple Broker Endpoints

If you need your application to connect to multiple broker endpoints—for example,
when you use an [active/standby](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment") deployment mode or when you [migrate from an on-premises message broker to
Amazon MQ](../migration-guide.md "../migration-guide.md")—use the [Failover
Transport](http://activemq.apache.org/failover-transport-reference.html "http://activemq.apache.org/failover-transport-reference.html") to allow your consumers to randomly connect to either one. For
example:

```
failover:(ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617,ssl://b-9876l5k4-32ji-109h-8gfe-7d65c4b132a1-2.mq.us-west-2.amazonaws.com:61617)?randomize=true
```

###### Important

Multi-availability zone brokers can experience failovers during maintenance windows and broker restarts. Use the Failover Transport to ensure your broker availability.

## Avoid Using Message Selectors

It is possible to use [JMS
selectors](https://docs.oracle.com/cd/E19798-01/821-1841/bncer/index.html "https://docs.oracle.com/cd/E19798-01/821-1841/bncer/index.html") to attach filters to topic subscriptions (to route messages to
consumers based on their content). However, the use of JMS selectors fills up the
Amazon MQ broker's filter buffer, preventing it from filtering messages.

In general, avoid letting consumers route messages because, for optimal decoupling
of consumers and producers, both the consumer and the producer should be
ephemeral.

## Prefer Virtual Destinations to Durable Subscriptions

A [durable subscription](http://activemq.apache.org/how-do-durable-queues-and-topics-work.html "http://activemq.apache.org/how-do-durable-queues-and-topics-work.html") can help ensure that the consumer receives all
messages published to a topic, for example, after a lost connection is restored.
However, the use of durable subscriptions also precludes the use of competing
consumers and might have performance issues at scale. Consider using [virtual
destinations](http://activemq.apache.org/virtual-destinations.html "http://activemq.apache.org/virtual-destinations.html") instead.

## If using Amazon VPC peering, avoid client IPs in CIDR range `10.0.0.0/16`

If you are setting up Amazon VPC peering between on-premise infrastructure and your Amazon MQ broker, you must not configure client connections with IPs in CIDR range `10.0.0.0/16`.

## Disable Concurrent Store and Dispatch for Queues with Slow Consumers

By default, Amazon MQ optimizes for queues with fast consumers:

- Consumers are considered _fast_ if they are able to
  keep up with the rate of messages generated by producers.
- Consumers are considered _slow_ if a queue builds up a
  backlog of unacknowledged messages, potentially causing a decrease in
  producer throughput.

To instruct Amazon MQ to optimize for queues with slow consumers, set the
`concurrentStoreAndDispatchQueues` attribute to `false`.
For an example configuration, see [concurrentStoreAndDispatchQueues](child-element-details.md#concurrentStoreAndDispatchQueues "child-element-details.md#concurrentStoreAndDispatchQueues").

## Choose the Correct Broker Instance Type for the Best Throughput

The message throughput of a [broker instance
type](broker-instance-types.md "broker-instance-types.md") depends on your application's use case and the following
factors:

- Use of ActiveMQ in persistent mode
- Message size
- The number of producers and consumers
- The number of destinations

### Understanding the relationship between message size, latency, and throughput

Depending on your use case, a larger broker instance type might not
necessarily improve system throughput. When ActiveMQ writes messages to durable
storage, the size of your messages determines your system's limiting
factor:

- If your messages are smaller than 100 KB, persistent storage latency
  is the limiting factor.
- If your messages are larger than 100 KB, persistent storage throughput
  is the limiting factor.

When you use ActiveMQ in persistent mode, writing to storage normally occurs
when there are either few consumers or when the consumers are slow. In
non-persistent mode, writing to storage also occurs with slow consumers if the
heap memory of the broker instance is full.

To determine the best broker instance type for your application, we recommend
testing different broker instance types. For more information, see [Broker instance types](broker-instance-types.md "broker-instance-types.md") and
also [Measuring the Throughput for Amazon MQ using the JMS Benchmark](https://aws.amazon.com/blogs/compute/measuring-the-throughput-for-amazon-mq-using-the-jms-benchmark/ "https://aws.amazon.com/blogs/compute/measuring-the-throughput-for-amazon-mq-using-the-jms-benchmark/").

### Use cases for larger broker instance types

There are three common use cases when larger broker instance types improve
throughput:

- **Non-persistent mode** – When
  your application is less sensitive to losing messages during [broker instance
  failover](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment") (for example, when broadcasting sports scores), you
  can often use ActiveMQ's non-persistent mode. In this mode, ActiveMQ
  writes messages to persistent storage only if the heap memory of the
  broker instance is full. Systems that use non-persistent mode can
  benefit from the higher amount of memory, faster CPU, and faster network
  available on larger broker instance types.
- **Fast consumers** – When active
  consumers are available and the [concurrentStoreAndDispatchQueues](child-element-details.md#concurrentStoreAndDispatchQueues "child-element-details.md#concurrentStoreAndDispatchQueues") flag is
  enabled, ActiveMQ allows messages to flow directly from producer to
  consumer without sending messages to storage (even in persistent mode).
  If your application can consume messages quickly (or if you can design
  your consumers to do this), your application can benefit from a larger
  broker instance type. To let your application consume messages more
  quickly, add consumer threads to your application instances or scale up
  your application instances vertically or horizontally.
- **Batched transactions** – When
  you use persistent mode and send multiple messages per transaction, you
  can achieve an overall higher message throughput by using larger broker
  instance types. For more information, see [Should I Use Transactions?](http://activemq.apache.org/should-i-use-transactions.html "http://activemq.apache.org/should-i-use-transactions.html") in the ActiveMQ
  documentation.

## Choose the correct broker storage type for the best throughput

To take advantage of high durability and replication across multiple Availability Zones, use Amazon EFS.
To take advantage of low latency and high throughput, use Amazon EBS. For more information, see [Storage](broker-storage.md "broker-storage.md").

## Configure Your Network of Brokers Correctly

When you create a [network of brokers](network-of-brokers.md "network-of-brokers.md"),
configure it correctly for your application:

- **Enable persistent mode** – Because
  (relative to its peers) each broker instance acts like a producer or a
  consumer, networks of brokers don't provide distributed replication of
  messages. The first broker that acts as a consumer receives a message and
  persists it to storage. This broker sends an acknowledgement to the producer
  and forwards the message to the next broker. When the second broker
  acknowledges the persistence of the message, the first broker deletes the
  message.

If persistent mode is disabled, the first broker acknowledges the producer
without persisting the message to storage. For more information, see [Replicated Message Store](http://activemq.apache.org/replicated-message-store.html "http://activemq.apache.org/replicated-message-store.html") and [What is the difference between persistent and non-persistent
delivery?](http://activemq.apache.org/what-is-the-difference-between-persistent-and-non-persistent-delivery.html "http://activemq.apache.org/what-is-the-difference-between-persistent-and-non-persistent-delivery.html") in the Apache ActiveMQ documentation.

- **Don't disable advisory messages for broker
  instances** – For more information, see [Advisory
  Message](http://activemq.apache.org/advisory-message.html "http://activemq.apache.org/advisory-message.html") in the Apache ActiveMQ documentation.
- **Don't use multicast broker discovery**
  – Amazon MQ doesn't support broker discovery using multicast. For more
  information, see [What
  is the difference between discovery, multicast, and zeroconf?](http://activemq.apache.org/multicast-transport-reference.html "http://activemq.apache.org/multicast-transport-reference.html") in
  the Apache ActiveMQ documentation.

## Avoid slow restarts by recovering prepared XA transactions

ActiveMQ supports distributed (XA) transactions. Knowing how ActiveMQ processes XA
transactions can help avoid slow recovery times for broker restarts and failovers in
Amazon MQ

Unresolved prepared XA transactions are replayed on every restart. If these remain
unresolved, their number will grow over time, significantly increasing the time needed
to start up the broker. This affects restart and failover time. You must resolve these
transactions with a `commit()` or a `rollback()` so that
performance doesn't degrade over time.

To monitor your unresolved prepared XA transactions, you can use the
`JournalFilesForFastRecovery` metric in Amazon CloudWatch Logs. If this number is
increasing, or is consistently higher than `1`, you should recover your
unresolved transactions with code similar to the following example. For more
information, see [Quotas in Amazon MQ](amazon-mq-limits.md "amazon-mq-limits.md").

The following example code walks through prepared XA transactions and closes them with
a `rollback()`.

```
import org.apache.activemq.ActiveMQXAConnectionFactory;

import javax.jms.XAConnection;
import javax.jms.XASession;
import javax.transaction.xa.XAResource;
import javax.transaction.xa.Xid;

public class RecoverXaTransactions {
    private static final ActiveMQXAConnectionFactory ACTIVE_MQ_CONNECTION_FACTORY;
    final static String WIRE_LEVEL_ENDPOINT =
            "tcp://localhost:61616";;
    static {
        final String activeMqUsername = "`MyUsername123`";
        final String activeMqPassword = "`MyPassword456`";
        ACTIVE_MQ_CONNECTION_FACTORY = new ActiveMQXAConnectionFactory(activeMqUsername, activeMqPassword, WIRE_LEVEL_ENDPOINT);
        ACTIVE_MQ_CONNECTION_FACTORY.setUserName(activeMqUsername);
        ACTIVE_MQ_CONNECTION_FACTORY.setPassword(activeMqPassword);
    }

    public static void main(String[] args) {
        try {
            final XAConnection connection = ACTIVE_MQ_CONNECTION_FACTORY.createXAConnection();
            XASession xaSession = connection.createXASession();
            XAResource xaRes = xaSession.getXAResource();

            for (Xid id : xaRes.recover(XAResource.TMENDRSCAN)) {
                xaRes.rollback(id);
            }
            connection.close();

        } catch (Exception e) {
        }
    }
}
```

In a real-world scenario, you could check your prepared XA transactions against your
XA Transaction Manager. Then you can decide whether to handle each prepared transaction
with a `rollback()` or a `commit()`.
