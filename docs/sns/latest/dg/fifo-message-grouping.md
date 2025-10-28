# Amazon SNS message grouping for FIFO topics

Messages that belong to the same group are processed one by one, in a strict order relative
to the group.

When you publish messages to an Amazon SNS FIFO topic, you set the message group ID. The group ID
is a mandatory token that specifies that a message belongs to a specific message group. The SNS
FIFO topic passes the group ID to the subscribed Amazon SQS FIFO queues. There is no limit to the
number of group IDs in SNS FIFO topics or SQS FIFO queues. Message group ID is not passed to
Amazon SQS standard queues.

There's no affinity between a message group and a subscription. Therefore, messages that are
published to any message group are delivered to all subscribed queues, subject to any filter
policies attached to subscriptions. For more information, see [Amazon SNS message delivery for FIFO topics](fifo-message-delivery.md "fifo-message-delivery.md") and [Amazon SNS message filtering for FIFO topics](fifo-message-filtering.md "fifo-message-filtering.md").

In the [auto parts price management example use
case](fifo-example-use-case.md "fifo-example-use-case.md"), there's a dedicated message group for each product sold in the platform. The same
Amazon SNS FIFO topic is used for processing all price updates. The sequence of price updates is
preserved within the context of a single auto parts product, but not across multiple products.
The following diagram shows how this works. Notice that, for the product whose message group ID
is **product-214**, message **m1** is
processed before **m4**. This sequence is preserved throughout the
workflows that use Amazon SNS FIFO to Amazon SQS FIFO. Likewise, for the product whose message group ID is
**product-799**, message **m2** is
processed before **m3**. However, when using Amazon SQS standard queues,
the message order is no longer guaranteed, and message groups do not exist. The **product-214** and **product-799** message
groups are independent of each other, so there is no relationship between how their messages are
sequenced.

![Example of how message ordering and deduplication work in an Amazon SNS FIFO topic scenario involving different AWS services and message group IDs. It shows the flow of messages from Lambda functions through an Amazon SNS FIFO topic to various types of Amazon SQS queues (FIFO and standard), maintaining strict order in FIFO queues while demonstrating the potential disorder in standard queues. This setup is used to emphasize the importance of message sequencing in applications like price updates in an ecommerce platform, highlighting how each message group maintains its order independently across different consumer services.](images/sns-fifo-grouping.png)

## Distributing data by message group

IDs for improved performance

To optimize delivery throughput, Amazon SNS FIFO topics deliver messages from different message
groups in parallel, while message order is strictly maintained within each message group. Each
individual message group can deliver a maximum of 300 messages per second. Therefore, to
achieve high throughput for a single topic, use a large number of distinct message group IDs.
By utilizing a diverse set of message groups, Amazon SNS FIFO topics automatically distributes
messages across a larger number of parallel partitions.

###### Note

Amazon SNS FIFO topics are optimized for uniform distribution of messages across message
group IDs, regardless of the number of groups. AWS recommends that you use a
large number of distinct message group IDs for optimized performance.

When publishing to your Amazon SNS FIFO topic with high throughput and one or more Amazon SQS FIFO
queues are subscribed, it is recommended that you enable high throughput on your queues. For
more see [High
throughput for FIFO queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/high-throughput-fifo.md") in the _Amazon Simple Queue Service Developer Guide_.
