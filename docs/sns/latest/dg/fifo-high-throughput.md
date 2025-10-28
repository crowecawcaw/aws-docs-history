# High throughput FIFO topics in Amazon SNS

High throughput FIFO topics in Amazon SNS efficiently manage high message throughput while
maintaining strict message order, ensuring reliability and scalability for applications
processing numerous messages. This solution is ideal for scenarios demanding both high
throughput and ordered message delivery. To improve message throughput using high throughput
FIFO topics, increasing the number of message groups is recommended. For more information on
high throughput message quotas, see [Amazon SNS service quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") in the _Amazon Web Services General Reference_.

## Use cases for high throughput for Amazon SNS FIFO

topics

The following use cases highlight the diverse applications of high throughput FIFO topics,
showcasing their effectiveness across industries and scenarios:

- **Real-time data processing:** Applications dealing with
  real-time data streams, such as event processing or telemetry data ingestion, can benefit
  from high throughput FIFO topics to handle the continuous influx of messages while
  preserving their order for accurate analysis.
- **E-commerce order processing:** In e-commerce platforms
  where maintaining the order of customer transactions is critical, high throughput FIFO
  topics ensure that orders are delivered sequentially and without delays, even during peak
  shopping seasons.
- **Financial services:** Financial institutions handling
  high-frequency trading or transactional data rely on high throughput FIFO topics to
  process market data and transactions with minimal latency while adhering to strict
  regulatory requirements for message ordering.
- **Media streaming:** Streaming platforms and media
  distribution services utilize high throughput FIFO topics to manage the delivery of media
  files and streaming content, ensuring smooth playback experiences for users while
  maintaining the correct order of content delivery

## Partitions and data distribution

for high throughput for Amazon SNS FIFO topics

With high throughput topics, Amazon SNS distributes FIFO topic data across partitions. A
partition is an allocation of capacity for a topic that is automatically replicated across
multiple Availability Zones within an AWS Region. You don't manage partitions. Instead,
Amazon SNS automatically manages partitions on your behalf, based on the ingress rate.

For FIFO topics, Amazon SNS modifies the number of partitions in a topic in the following
situations:

- If the current publish rate approaches or exceeds what the existing partitions can
  support, additional partitions are allocated until the topic reaches the regional quota.
  For information on quotas, see [Amazon SNS service quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") in the _Amazon Web Services General Reference_.
- If the current partitions have low utilization, the number of partitions may be
  reduced.

Partition management occurs automatically in the background and is transparent to your
applications. Your topic and messages are available at all times.

###### Note

Temporary [Publish](../api/API_Publish.md "../api/API_Publish.md") API throttling may occur if you suddenly and significantly increase
traffic to your topic while sending multiple times the usual volume. This throttling can
last up to the duration of the deduplication window while the topic scales up to accommodate
the increased traffic.

## Distributing data by message group IDs

When publishing a message to a FIFO topic, Amazon SNS uses the value of each message’s message
group ID as input to an internal hash function. The output value from the hash function
determines which partition processes the message, one or more message group IDs may be handled
by a given partition.

###### Note

Amazon SNS is optimized for uniform distribution of items across a FIFO topic's partitions,
regardless of the number of partitions. AWS recommends that you use message group IDs that
can have a large number of distinct values.

## Enable high throughput on your Amazon SNS

FIFO topic

By default Amazon SNS FIFO topics are configured for topic-level deduplication, this is
controlled by the topic attribute [`FifoThroughputScope`](../api/API_CreateTopic.md "../api/API_CreateTopic.md") set to
`Topic` and have more restricted throughput quotas, see [Amazon SNS service quotas](../../../general/latest/gr/sns.md "../../../general/latest/gr/sns.md") in the
_Amazon Web Services General Reference_.

To enable high throughput for your Amazon SNS FIFO topic, update the
`FifoThroughputScope` attribute to `MessageGroup`. This change can be
done through the console or using the AWS CLI and SDK, and can also be set during topic
creation, which Amazon SNS recommends for the best customer experience and to reduce the chances of
your topic being throttled.

###### Important

Once you've enabled a topic's `FifoThroughputScope` to
`MessageGroup`, it cannot be reverted back to the `Topic`
throughput.

## Enable high throughput mode for

any subscribed Amazon SQS FIFO queue

When publishing to your Amazon SNS FIFO topic with high throughput enabled, and one or more
Amazon SQS FIFO queues are subscribed, it is recommended that you enable high throughput on your
Amazon SQS FIFO queues to enable your Amazon SNS FIFO high throughput topic to deliver smoothly. For
more see [High
throughput for FIFO queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.md") in the _Amazon Simple Queue Service Developer
Guide_.
