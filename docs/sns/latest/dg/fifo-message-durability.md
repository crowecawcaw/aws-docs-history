# Amazon SNS message durability for FIFO topics

Amazon SNS FIFO topics and Amazon SQS queues are durable. Both resource types store messages
redundantly across multiple Availability Zones, and provide dead-letter queues to handle
exceptional cases.

In Amazon SNS, message delivery fails when the Amazon SNS topic can't access a subscribed Amazon SQS queue
due to a client-side or server-side error:

- Client-side errors occur when the Amazon SNS FIFO topic has stale subscription metadata. Two
  common causes of client-side errors are when the Amazon SQS queue owner does one of the
  following:

      + Deletes the queue.
      + Changes the queue policy in a way that prevents the Amazon SNS service principal from
       delivering messages to it.

  Amazon SNS doesn't retry delivering messages that failed due to client-side errors.

- Server-side errors can occur in these situations:

      + The Amazon SQS service is unavailable.
      + Amazon SQS fails to process a valid request from the Amazon SNS service.

  When server-side errors occur, Amazon SNS FIFO topics retry the failed deliveries up to
  100,015 times over 23 days. For more information, see [Amazon SNS message delivery retries](sns-message-delivery-retries.md "sns-message-delivery-retries.md").
  For any type of error, Amazon SNS can sideline messages to Amazon SQS dead-letter queues so data isn't
  lost.

In Amazon SQS, message processing fails when the consumer application fails to receive the
message, process it, and delete it from the queue. When the maximum number of receive requests
fail, Amazon SQS can sideline messages to dead-letter queues so data isn't lost.

In the [auto parts price management example use
case](fifo-example-use-case.md "fifo-example-use-case.md"), the company can assign an Amazon SQS dead-letter queue (DLQ) to each Amazon SNS FIFO topic
subscription, as well as to each subscribed Amazon SQS queue. This protects the company from any
price update loss.

![Example of how dead-letter queues (DLQs) are integrated with Amazon SNS FIFO topics and Amazon SQS queues to ensure message reliability in an auto parts price management system. It shows the setup where each Amazon SNS FIFO subscription for wholesale, retail, and analytics purposes is paired with corresponding Amazon SQS FIFO or standard queues, each equipped with its own type-matched DLQ to safeguard against message loss due to processing failures.](images/sns-fifo-dlq.png)
The dead-letter queue associated with an Amazon SNS subscription must be an Amazon SQS queue of the
same type as the subscribing queue. For example, the Amazon SNS FIFO subscription for an Amazon SQS FIFO
queue must have an Amazon SQS FIFO queue as the dead-letter queue. Similarly, the Amazon SNS FIFO
subscription for an Amazon SQS standard queue must have an Amazon SQS standard queue as its dead-letter
queue. For more information, see [Amazon SNS dead-letter queues](sns-dead-letter-queues.md "sns-dead-letter-queues.md") and the [Designing durable serverless apps with DLQs for Amazon SNS, Amazon SQS, AWS Lambda](https://aws.amazon.com/blogs/compute/designing-durable-serverless-apps-with-dlqs-for-amazon-sns-amazon-sqs-aws-lambda/ "https://aws.amazon.com/blogs/compute/designing-durable-serverless-apps-with-dlqs-for-amazon-sns-amazon-sqs-aws-lambda/ ") post on the
_AWS Compute Blog_.

For extended durability to assist in recovery from downstream failures,
topic owners can also use FIFO topics to archive messages up to 365 days. Topic subscribers can
then replay those messages to a subscribed endpoint to recover messages lost due to a failure in
a downstream application, or to replicate a state of an existing application. For more, see
[Amazon SNS message archiving and replay for FIFO
topics](fifo-message-archiving-replay.md "fifo-message-archiving-replay.md").
