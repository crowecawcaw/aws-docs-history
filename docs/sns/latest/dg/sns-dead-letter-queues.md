# Amazon SNS dead-letter queues

A dead-letter queue is an Amazon SQS queue that an Amazon SNS subscription can target
for messages that can't be delivered to subscribers successfully. Messages that can't be delivered
due to client errors or server errors are held in the dead-letter queue for further analysis or reprocessing. For more information, see [Configuring an Amazon SNS dead-letter queue for
a subscription](sns-configure-dead-letter-queue.md "sns-configure-dead-letter-queue.md") and [Amazon SNS message delivery retries](sns-message-delivery-retries.md "sns-message-delivery-retries.md").

###### Note

- The Amazon SNS subscription and Amazon SQS queue must be under the same AWS account and Region.
- For a [FIFO topic](sns-fifo-topics.md "sns-fifo-topics.md"), you can use an Amazon SQS
  queue as a dead-letter queue for the Amazon SNS subscription. FIFO topic
  subscriptions use FIFO queues, and standard topic subscriptions use standard
  queues.
- To use an encrypted Amazon SQS queue as a dead-letter queue, you must use a custom KMS with a key policy
  that grants the Amazon SNS service principal access to AWS KMS API actions. For more information, see [Securing Amazon SNS data with server-side
  encryption](sns-server-side-encryption.md "sns-server-side-encryption.md") in this guide and [Protecting Amazon SQS Data
  Using Server-Side Encryption (SSE) and AWS KMS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.md") in the _Amazon Simple Queue Service Developer Guide_.

## Why do message deliveries fail?

In general, message delivery fails when Amazon SNS can't access a subscribed endpoint due
to a _client-side_ or _server-side error_. When
Amazon SNS receives a client-side error, or continues to receive a server-side error for a
message beyond the number of retries specified by the corresponding retry policy, Amazon SNS
discards the message—unless a dead-letter queue is attached to the subscription.
Failed deliveries don't change the status of your subscriptions. For more information,
see [Amazon SNS message delivery retries](sns-message-delivery-retries.md "sns-message-delivery-retries.md").

### Client-side errors

Client-side errors can happen when Amazon SNS has stale subscription metadata. These
errors commonly occur when an owner deletes the endpoint (for example, a Lambda
function subscribed to an Amazon SNS topic) or when an owner changes the policy attached
to the subscribed endpoint in a way that prevents Amazon SNS from delivering messages to
the endpoint. Amazon SNS doesn't retry the message delivery that fails as a result of a
client-side error.

### Server-side errors

Server-side errors can happen when the system responsible for the subscribed
endpoint becomes unavailable or returns an exception that indicates that it can't
process a valid request from Amazon SNS. When server-side errors occur, Amazon SNS retries the
failed deliveries using either a linear or exponential backoff function. For
server-side errors caused by AWS managed endpoints backed by Amazon SQS or AWS Lambda,
Amazon SNS retries delivery up to 100,015 times, over 23 days.

Customer managed endpoints (such as HTTP, SMTP, SMS, or mobile push) can also
cause server-side errors. Amazon SNS retries delivery to these types of endpoints as
well. While HTTP endpoints support customer-defined retry policies, Amazon SNS sets an
internal delivery retry policy to 50 times over 6 hours, for SMTP, SMS, and mobile
push endpoints.

## How do dead-letter queues work?

A dead-letter queue is attached to an Amazon SNS subscription (rather than a topic) because
message deliveries happen at the subscription level. This lets you identify the original
target endpoint for each message more easily.

A dead-letter queue associated with an Amazon SNS subscription is an ordinary Amazon SQS queue.
For more information about the message retention period, see [Quotas Related to
Messages](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.md#quotas-messages "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-quotas.md#quotas-messages") in the _Amazon Simple Queue Service Developer Guide_. You can change the
message retention period using the Amazon SQS `SetQueueAttributes`
API action. To make your applications more resilient, we recommend setting the maximum
retention period for dead-letter queues to 14 days.

## How are messages moved into

a dead-letter queue?

Your messages are moved into a dead-letter queue using a _redrive
policy_. A redrive policy is a JSON object that refers to the ARN of the
dead-letter queue. The `deadLetterTargetArn` attribute specifies the ARN. The
ARN must point to an Amazon SQS queue in the same AWS account and Region as your Amazon SNS
subscription. For more information, see [Configuring an Amazon SNS dead-letter queue for
a subscription](sns-configure-dead-letter-queue.md "sns-configure-dead-letter-queue.md").

The following JSON object is a sample redrive policy, attached to an SNS
subscription.

```
{
  "deadLetterTargetArn": "arn:aws:sqs:us-east-2:123456789012:MyDeadLetterQueue"
}
```

## How can I move messages

out of a dead-letter queue?

You can move messages out of a dead-letter queue in two ways:

- **Avoid writing Amazon SQS consumer logic** –
  Set your dead-letter queue as an event source to the Lambda function to drain
  your dead-letter queue.
- **Write Amazon SQS consumer logic** – Use the
  Amazon SQS API, AWS SDK, or AWS CLI to write custom consumer logic for polling,
  processing, and deleting the messages in the dead-letter queue.

## How can I monitor and log

dead-letter queues?

You can use Amazon CloudWatch metrics to monitor dead-letter queues associated with your Amazon SNS
subscriptions. All Amazon SQS queues emit CloudWatch metrics at one-minute intervals. For more
information, see [Available CloudWatch metrics for Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.md") in the
_Amazon Simple Queue Service Developer Guide_. All Amazon SNS subscriptions with dead-letter
queues also emit CloudWatch metrics. For more information, see [Monitoring Amazon SNS topics using
CloudWatch](sns-monitoring-using-cloudwatch.md "sns-monitoring-using-cloudwatch.md").

To be notified of activity in your dead-letter queues, you can use CloudWatch metrics and
alarms. Setting up an alarm for the `NumberOfMessagesSent` metric is not
suitable because this metric does not capture messages sent to a DLQ as a result of
failed processing attempts. Instead, use the
`ApproximateNumberOfMessagesVisible` metric, which captures all messages
currently available in the DLQ, including those moved due to processing failures.

###### Example CloudWatch alarm setup

1. Create a [CloudWatch
   alarm](../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md "../../../AmazonCloudWatch/latest/monitoring/ConsoleAlarms.md") for the `**ApproximateNumberOfMessagesVisible**` metric.
2. Set the alarm threshold to **1** (or another
   appropriate value based on your expectations and DLQ traffic).
3. Specify an Amazon SNS **topic** to be notified when
   the alarm goes off. This Amazon SNS topic can deliver your alarm notification to any
   endpoint type (such as an email address, phone number, or mobile pager
   app).

You can use CloudWatch Logs to investigate the exceptions that cause any Amazon SNS deliveries to
fail and for messages to be sent to dead-letter queues. Amazon SNS can log both successful
and failed deliveries in CloudWatch. For more information, see [Amazon SNS mobile app attributes](sns-msg-status.md "sns-msg-status.md").
