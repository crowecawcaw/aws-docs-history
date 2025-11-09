# Migrating to Amazon MQ without service interruption

Use the following topics to learn more about potential service interruptions
before migrating your on-premises message broker to Amazon MQ.

## Migrating to Amazon MQ without

service interruption

You can migrate from an on-premises message broker to an Amazon MQ broker in the AWS Cloud without service interruption.

###### Important

This scenario might cause messages to be delivered out of order.

The following diagrams illustrate the scenario of migrating from an on-premises message
broker to an Amazon MQ broker in the AWS Cloud without service interruption.

| On-Premises Message Broker                                                             | Migration to Amazon MQ with Standard (Unordered) Queues                                       |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Diagram showing producers connecting to on-premises message broker, then to consumers. | Diagram showing message flow between producers, on-premises broker, AWS cloud, and consumers. |

### To migrate to Amazon MQ without service interruption

![Red circle with the number 1 inside, typically used as a numerical indicator.](images/number-1-red.png)
[Create and configure an Amazon MQ
broker](../developer-guide/getting-started-activemq.md "../developer-guide/getting-started-activemq.md") and note your broker's endpoint, for example:

```
ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617
```

![Red circle with the number 2 inside, indicating a numerical step or count.](images/number-2-red.png)
For either of the following cases, use the [Failover Transport](http://activemq.apache.org/failover-transport-reference.html "http://activemq.apache.org/failover-transport-reference.html") to allow your consumers
to randomly connect to your on-premises broker's endpoint or your Amazon MQ broker's endpoint. For example:

```
failover:(ssl://on-premises-broker.example.com:61617,ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617)?randomize=true
```

Do one of the following:

- One by one, point each existing consumer to your Amazon MQ broker's endpoint.
- Create new consumers and point them to your Amazon MQ broker's endpoint.

###### Note

If you scale up your consumer fleet during the migration process, it is a best
practice to scale it down afterward.

![Red circle with white number 3 inside, indicating a numerical label or step.](images/number-3-red.png)
One by one, stop each existing producer, point the producer to your
Amazon MQ broker's endpoint, and then restart the producer.

![Red circle with the number 4 inside, likely representing a numerical icon or badge.](images/number-4-red.png)
Wait for your consumers to drain the destinations on your on-premises broker.

![Red circle with the number 5 inside.](images/number-5-red.png)
Change your consumers' Failover transport to include only your Amazon MQ
broker's endpoint. For example:

```
failover:(ssl://b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9-1.mq.us-east-2.amazonaws.com:61617)
```

![Red circle with the number 6 inside.](images/number-6-red.png)
Stop your on-premises broker.
