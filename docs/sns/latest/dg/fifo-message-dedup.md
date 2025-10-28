# Amazon SNS message deduplication for FIFO topics

Amazon SNS FIFO topics and Amazon SQS FIFO queues support message deduplication, which provides
exactly-once message delivery and processing as long as the following conditions are met:

- The subscribed Amazon SQS FIFO queue exists and has permissions that allow the Amazon SNS service
  principal to deliver messages to the queue.
- The Amazon SQS FIFO queue consumer processes the message and deletes it from the queue before
  the visibility timeout expires.
- The Amazon SNS subscription topic has no [message
  filtering](fifo-message-filtering.md "fifo-message-filtering.md"). When you configure message filtering, Amazon SNS FIFO topics support
  at-most-once delivery, as messages can be filtered out based on your subscription filter
  policies.
- There are no network disruptions that prevent acknowledgment of the message
  delivery.

###### Note

Message deduplication applies to an entire Amazon SNS FIFO topic when the topic attribute
`FifoThroughputScope` is set to `Topic`. When the topic attribute
`FifoThroughputScope` is set to `MessageGroup`, message deduplication
applies to each individual [message group](fifo-message-grouping.md "fifo-message-grouping.md").

When you publish a message to an Amazon SNS FIFO topic, the message must include a deduplication
ID. This ID is included in the message that the Amazon SNS FIFO topic delivers to the subscribed
Amazon SQS FIFO queues.

If a message with a particular deduplication ID is successfully published to an Amazon SNS FIFO
topic, any message published with the same deduplication ID, within the five minute
deduplication interval, is accepted but not delivered. The Amazon SNS FIFO topic continues to track
the message deduplication ID, at the deduplication scope configured by the topic attribute
`FifoThroughputScope`, even after the message is delivered to subscribed
endpoints.

If the message body is guaranteed to be unique for each published message, you can enable
content-based deduplication for an Amazon SNS FIFO topic and the subscribed Amazon SQS FIFO queues. Amazon SNS
uses the message body to generate a unique hash value to use as the deduplication ID for each
message, so you don't need to set a deduplication ID when you send each message.

###### Note

Message attributes are not included in the hash calculation.

When content-based deduplication is enabled for an Amazon SNS FIFO topic, and a message is
published with a deduplication ID, the published deduplication ID overrides the generated
content-based deduplication ID.

In the [auto parts price management example use
case](fifo-example-use-case.md "fifo-example-use-case.md"), the company must set a universally unique deduplication ID for each price update.
This is because the message body can be identical even when the message attribute is different
for wholesale and retail. However, if the company added the business type (wholesale or retail)
to the message body alongside the product ID and product price, they could enable content-based
duplication in the Amazon SNS FIFO topic and the subscribed Amazon SQS FIFO queues.

![How message deduplication works in an Amazon SNS FIFO (First In, First Out) topic environment, using an auto parts price management example. It shows how duplicated messages (m1) published to the Amazon SNS FIFO topic are prevented from being delivered multiple times to the subscriber systems (wholesale, retail, and analytics queues). This deduplication ensures that only unique messages are processed, enhancing efficiency and accuracy in message handling across different subscriber functions.](images/sns-fifo-dedup.png)
In addition to message ordering and deduplication, Amazon SNS FIFO topics support message
server-side encryption (SSE) with AWS KMS keys, and message privacy via VPC endpoints with
AWS PrivateLink. For more information, see [Amazon SNS message security for FIFO topics](fifo-message-security.md "fifo-message-security.md").
