# Amazon SNS message delivery for FIFO topics

Amazon SNS FIFO (first in, first out) topics support delivery to both Amazon SQS standard and FIFO
queues to provide customers with flexibility and control when integrating distributed
applications that require data consistency in near real-time.

For workloads that need to preserve strict message ordering or de-duplication, the
combination of Amazon SNS FIFO topics with [Amazon SQS FIFO
queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.md") subscribed as the delivery endpoint provides enhance messaging between
applications when the order of operations and events is critical, or where duplicates can’t be
tolerated.

For workloads that tolerate best-effort ordering and at-least-once delivery, subscribing
[Amazon SQS standard
queues](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues.md") to Amazon SNS FIFO topics provides the ability to lower costs, in addition to
sharing queues across workloads that don't utilize FIFO.

###### Note

To fan out messages from Amazon SNS FIFO topics to AWS Lambda functions, extra steps are
required. First, subscribe Amazon SQS FIFO or standard queues to the topic. Then configure the
queues to trigger the functions. For more information, see the [SQS FIFO as an event source](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-sqs-fifo-as-an-event-source/ "https://aws.amazon.com/blogs/compute/new-for-aws-lambda-sqs-fifo-as-an-event-source/") post on the _AWS Compute
Blog_.

SNS FIFO topics can't deliver messages to customer managed endpoints, such as email
addresses, mobile apps, phone numbers for text messaging (SMS), or HTTP(S) endpoints. These
endpoint types aren't guaranteed to preserve strict message ordering. Attempts to subscribe
customer managed endpoints to SNS FIFO topics result in errors.

SNS FIFO topics support the same message filtering capabilities as standard topics. For more
information, see [Amazon SNS message filtering for FIFO topics](fifo-message-filtering.md "fifo-message-filtering.md")
and the [Simplify Your Pub/Sub Messaging with Amazon SNS Message Filtering](https://aws.amazon.com/blogs/compute/simplify-pubsub-messaging-with-amazon-sns-message-filtering/ "https://aws.amazon.com/blogs/compute/simplify-pubsub-messaging-with-amazon-sns-message-filtering/") post on the
_AWS Compute Blog_.
