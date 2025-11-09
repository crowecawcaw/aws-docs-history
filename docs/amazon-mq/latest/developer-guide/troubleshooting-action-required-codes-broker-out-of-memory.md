# ActiveMQ on Amazon MQ: Broker Out Of Memory alarm

ActiveMQ on Amazon MQ will raise a BROKER_OOM alarm when the broker undergoes a restart loop due to
the insufficient memory capacity. When a broker is in a restart loop, also called a bounce loop,
the broker initiates repeated recovery attempts within a short time window.
Brokers that cannot complete start-up due to insufficient memory capacity can enter a restart loop,
during which interactions with the broker are limited.

Amazon MQ enables metrics for your broker by default. You can view your broker metrics by accessing the Amazon CloudWatch console,
or by using the CloudWatch API. The following metrics are useful when diagnosing the ActiveMQ BROKER_OOM alarm:

| Amazon MQ CloudWatch metric | Reason for high memory use                                                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `TotalMessageCount`         | Messages are stored in memory until they are consumed or discarded. A high message count might<br>indicate overutilization of resources and can lead to a high memory alarm.                                                                                 |
| `HeapUsage`                 | The percentage of the ActiveMQ JVM memory limit that the broker currently uses.<br>A higher percentage indicates the broker is using significant resources and may lead to an OOM alarm.                                                                     |
| `ConnectionCount`           | Client connections utilize memory, and too many simultaneous connections can lead to a high memory alarm.                                                                                                                                                    |
| `CpuUtilization`            | The percentage of allocated EC2 compute units that the broker currently uses.                                                                                                                                                                                |
| `TotalConsumerCount`        | For every consumer connected to the broker, a set number of messages are loaded from storage into memory before they are delivered to the consumer.<br>A large number of consumer connections might cause high memory usage and lead to a high memory alarm. |

To prevent restart loops and avoid the BROKER_OOM alarm, ensure that messages are consumed quickly.
You can do this by choosing the most effective broker instance type, and also cleaning your [Dead Letter Queue](https://activemq.apache.org/message-redelivery-and-dlq-handling.html "https://activemq.apache.org/message-redelivery-and-dlq-handling.html")
to discard undeliverable or expired messages. You can learn more about ensuring effective performance at
[ActiveMQ on Amazon MQ best practices](best-practices-activemq.md "best-practices-activemq.md").
