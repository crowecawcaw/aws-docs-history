# Amazon SNS features and capabilities

Amazon SNS offers a comprehensive set of features designed to enhance messaging between
applications and users. These features enable seamless communication, secure message
delivery, and robust message management, ensuring high availability, durability, and
flexibility for a wide range of messaging use cases.

\***\*Application-to-application messaging\*\***

[Application-to-application
messaging](sns-system-to-system-messaging.md "sns-system-to-system-messaging.md") supports subscribers such as delivery
streams, Lambda functions, Amazon SQS queues, HTTP/S endpoints, and
AWS Event Fork Pipelines. This allows for efficient message delivery in event-driven
architectures.

\***\*Application-to-person notifications\*\***

[Application-to-person
notifications](sns-user-notifications.md "sns-user-notifications.md") provide user notifications to subscribers such as
mobile applications, mobile phone numbers, and email addresses.

\***\*Standard and FIFO topics\*\***

[FIFO topics](sns-fifo-topics.md "sns-fifo-topics.md") ensure strict message
ordering, message grouping, and deduplication, allowing FIFO and standard
queues to subscribe for message processing. [Standard topics](sns-create-topic.md "sns-create-topic.md") are used when message ordering and possible
duplication are not critical, supporting all delivery protocols for broader
use cases.

\***\*Message durability\*\***

Amazon SNS uses a number of strategies that work together to provide message
durability:

- Published messages are stored across multiple, geographically
  separated servers and data centers.
- If a subscribed endpoint isn't available, Amazon SNS runs a [delivery retry
  policy](sns-message-delivery-retries.md "sns-message-delivery-retries.md").
- To preserve any messages that aren't delivered before the delivery
  retry policy ends, you can create a [dead-letter
  queue](sns-dead-letter-queues.md "sns-dead-letter-queues.md").

\***\*Message archiving, replay, and
analytics\*\***

You can archive messages with Amazon SNS in multiple ways including subscribing
[Firehose delivery streams to SNS
topics](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md"), which allows you to send notifications to analytics
endpoints such as Amazon Simple Storage Service (Amazon S3) buckets, Amazon Redshift tables, and more.
Additionally, Amazon SNS FIFO topics support message archiving and replay as a
no-code, in-place message archive that lets topic owners store (or _archive_) messages within their topic. Topic
subscribers can then retrieve (or _replay_)
the archived messages back to a subscribed endpoint. For more, see [Amazon SNS message archiving and replay for FIFO
topics](fifo-message-archiving-replay.md "fifo-message-archiving-replay.md").

\***\*Message attributes\*\***

[Amazon SNS message attributes](sns-message-attributes.md "sns-message-attributes.md") let you provide any arbitrary
metadata about the message.

\***\*Message filtering\*\***

By default, each subscriber receives every message published to the topic.
To receive a subset of the messages, a subscriber must assign a filter
policy to the topic subscription. A subscriber can also define the filter
policy scope to enable payload-based or attribute-based filtering. The
default value for the filter policy scope is `MessageAttributes`.
When the incoming message attributes match the filter policy attributes, the
message is delivered to the subscribed endpoint. Otherwise, the message is
filtered out. When the filter policy scope is `MessageBody`,
filter policy attributes are matched against the payload. For more
information, see [Amazon SNS message filtering](sns-message-filtering.md "sns-message-filtering.md").

\***\*Message security\*\***

Server-side encryption protects the contents of messages that are stored
in Amazon SNS topics, using encryption keys provided by AWS KMS. For more
information, see [Securing Amazon SNS data with server-side
encryption](sns-server-side-encryption.md "sns-server-side-encryption.md") You can also
establish a private connection between Amazon SNS and your virtual private cloud
(VPC). for more information, see [Securing Amazon SNS traffic with VPC
endpoints](sns-internetwork-traffic-privacy.md "sns-internetwork-traffic-privacy.md").
