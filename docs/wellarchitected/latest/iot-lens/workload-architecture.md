# Workload architecture

A reliable workload starts with upfront design decisions for both
software and infrastructure. Your architecture choices will impact
your workload behavior across all six Well-Architected pillars.
For reliability, there are specific patterns you must follow:

The following sections explain best practices to use with these
patterns for reliability.

| IOTREL05: How do you manage data ingestion<br>and processing throughput for IoT workloads to other<br>applications? |
| ------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                     |

Although IoT applications have communication that is only routed
between other devices, there will be messages that are processed
and stored in your application. In these cases, the rest of your
IoT application must be prepared to respond to incoming data. All
internal services that are dependent upon that data need a way to
seamlessly scale the ingestion and processing of the data.

## IOTREL05-BP01 Decouple IoT applications from the Connectivity Layer through an Ingestion Layer

In a well-architected IoT application, internal systems are
decoupled from the connectivity layer of the IoT system through
the ingestion layer. The ingestion layer is composed of queues
and streams that enable durable short-term storage while
allowing compute resources to process data independent of the
rate of ingestion.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL05-BP01-01** _Decouple application
consumers using streaming data services._

To optimize throughput, use AWS IoT rules to route inbound
device data to services such as Amazon Kinesis Data Streams,
Amazon Data Firehose, Amazon Simple Queue Service, or
Amazon Managed Streaming for Apache Kafka before performing any
compute operations. Make sure that all the intermediate
streaming points are provisioned to handle peak capacity. This
approach creates the queueing layer necessary for upstream
applications to process data resiliently.

**Prescriptive guidance
IOTREL05-BP01-02** _Make use of MQTT features
to support reliable delivery of messages._

AWS IoT Core supports MQTT persistent sessions, which store a
client's subscriptions and messages that haven't been
acknowledged by the client. Messages are stored according to
account limits, and the Persistent session expiry period what
can be adjusted between 1 hour and 7 days. This allows for
clients to publish messages that will be persisted by the AWS IoT Core Broker for up to the account limits and expiry period,
for later processing. Read more about persistent sessions in the
[AWS IoT Core developer guide](../../../iot/latest/developerguide/mqtt.md#mqtt-persistent-sessions "../../../iot/latest/developerguide/mqtt.md#mqtt-persistent-sessions").

| IOTREL06: How do you facilitate reliable<br>processing and delivery of IoT messages across your<br>workload? |
| ------------------------------------------------------------------------------------------------------------ |
|                                                                                                              |

Data sent from devices should be processed and stored without
excessive loss. Services that queue and deliver IoT data to
compute and database services should be used to support the
processing of data. IoT devices send lots of data in small sizes
without order, and the cloud application should be able to
handle this.

## IOTREL06-BP01 Dynamically scale cloud resources based on the utilization

The elastic nature of the cloud can be used to increase and
decrease resources on demand. Use the ability to increase and
decrease cloud resources based on data, number of messages, and
size of messages and number of devices.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL06-BP01-01** _Know the mechanisms that
can be used to monitor cloud resource usage and methods to scale
the resources._

- Use Amazon CloudWatch Logs to trigger based on rate of data
  flow to auto-scale cloud resources as needed.
- [Use
  AWS IoT Rules engine error actions](../../../iot/latest/developerguide/rule-error-handling.md "../../../iot/latest/developerguide/rule-error-handling.md") to provision
  additional cloud resources and message retries as needed.
- Examine IoT logs for errors in communicating to resources
  and provision resources based on that data.
- Use AWS Lambda to automatically scale your application by
  running code in response to each event.
- Use automatic scaling where possible. Kinesis Data Streams
  and Amazon DynamoDB are two services that provide automatic
  scaling.

**Prescriptive guidance
IOTREL06-BP01-02** _Use MQTT 5 Shared
Subscriptions to effectively load balance MQTT messages across
several subscribers._

Using _Shared Subscriptions_ in
MQTT is an effective way to _load
balance_ messages across multiple subscribers in a way
that optimizes resource usage, improves scalability, and
supports more efficient message delivery.

| IOTREL07: How do you provision storage<br>strategies for IoT data in the cloud? |
| ------------------------------------------------------------------------------- |
|                                                                                 |

IoT devices send a lot of small messages with no guarantee of
delivery order. This data might not be immediately useful, but
the data volume is typically low enough to economically store
against a future need. It will be beneficial to store the data
so that the data can processed in order. Stored data can be
reprocessed as new requirements are developed.

## IOTREL07-BP01 Store data before processing

Make sure that the data from the devices is stored before
processing. As new requirements and capabilities are added,
stored data can be analyzed to meet the new requirements.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL07-BP01-01** _Use IoT Core Rules Engine
to send data to Firehose to batch and store data on
Amazon S3._

- IoT Rules Engine can send data to Firehose to
  batch and store data on Amazon S3. Intelligent tiering can be enabled in Amazon S3 to
  reduce storage costs.
- Understand the latency to access data and choose the Region
  to store the data in based on device location.
- If data will be processed in Amazon EC2 instances, consider
  using the highly available and low-latency Amazon Elastic Block Store (Amazon EBS).
- NoSQL data can be stored in Amazon DynamoDB, which is a
  key-value and document database that delivers single-digit
  millisecond performance at scale. IoT Core Rules engine can
  write all or part of an MQTT message to a DynamoDB table.

## IOTREL07-BP02Implement storage redundancy and failover mechanisms for IoT data persistence

There should be recovery plans for failures in storing and
accessing device data in the cloud. Understand the Recovery
Point Objective (RPO) and Recovery Time Objective (RTO) needed
by your application to access data to be used for analysis.

**Level of risk exposed if this best
practice is not established:** Medium

Prescriptive guidance IOTREL07-BP02-01 _Know how to
monitor and take action on cloud storage failures for IoT
data._

- AWS Health Dashboard provides notification and
  remediation guidance when AWS is experiencing events that
  might impact you. Storage and access of data can be modified
  based on the notification.
- Use Amazon CloudWatch Logs to trigger on events on writing
  and reading data and take appropriate error handling action.
  - Use AWS IoT rules engine error actions to provision data
    storage to other locations if primary storage is
    unavailable.
