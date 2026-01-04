# Amazon EventBridge Pipes error handling and troubleshooting

Understanding the types of errors EventBridge Pipes may encounter, and how EventBridge handles those errors, can help you troubleshoot issues with your pipes.

## Retry behavior and error handling

EventBridge Pipes automatically retries enrichment and target invocation on any retryable AWS
failures with the source service, the enrichment or target services, or EventBridge. However, if
there are failures returned by enrichment or target customer implementations, the pipe polling
throughput will gradually back off. For nearly continuous 4xx errors (such as authorization
problems with IAM or missing resources), the pipe can be automatically disabled with an
explanatory message in the `StateReason`.

## Pipe invocation errors and retry behavior

When you invoke a pipe, two main types of errors can occur: _pipe internal
errors_ and _customer invocation errors_.

### Pipe internal errors

Pipe internal errors are errors resulting by aspects of the invocation
managed by the EventBridge Pipes service.

These types of errors can include issues such as:

- A HTTP connection failure when attempting to invoke the customer targer service
- A transient drop in availability on the pipe service itself.

In general, EventBridge Pipes retries internal errors an indefinite number of times, and
stops only when the record expires in the source.

For pipes with a stream source, EventBridge Pipes does not count retries for internal errors
against the maximum number of retries specified on the retry policy for the stream source.
For pipes with an Amazon SQS source, EventBridge Pipes does not count retries for internal errors
against the maximum receive count for the Amazon SQS source.

### Customer invocation errors

Customer invocation errors are errors resulting from configuration or
code managed by the user.

These types of errors can include issues such as:

- Insufficient permissions on the pipe to invoke the target.
- A logic error in a synchronously-invoked customer Lambda, Step Functions, API destination, or API Gateway endpoint.

For customer invocation errors, EventBridge Pipes does the following:

- For pipes with a stream source, EventBridge Pipes retries up to the maximum retry times configured on
  the pipe retry policy or until the maximum record age expires, whichever comes
  first.
- For pipes with an Amazon SQS source, EventBridge Pipes retries a customer error up to the maximum receive
  count on the source queue.
- For pipes with a Apache Kafka or Amazon MQ source, EventBridge retries customer errors the same as it retries internal errors.

For pipes with compute targets, you must invoke the pipe synchronously in order for
EventBridge Pipes to be aware of any runtime errors that are thrown from the customer compute
logic and retry on such errors. Pipes cannot retry on errors thrown from the logic of a
Step Functions standard workflow, as this target must be invoked asynchronously.

For Amazon SQS and stream sources, such as Kinesis and DynamoDB, EventBridge Pipes supports partial batch failure handling of target failures. For more information, see [Partial batch failure](eb-pipes-batching-concurrency.md#pipes-partial-batch-failure "eb-pipes-batching-concurrency.md#pipes-partial-batch-failure").

## Amazon SQS source retry timing with maxBatchWindowInSeconds

When using an Amazon SQS queue as a pipe source, the retry timing behavior differs depending on whether you configure the `maxBatchWindowInSeconds` parameter:

- **Without maxBatchWindowInSeconds** – The SQS poller uses the queue's visibility timeout setting for retries. When processing fails, messages remain hidden for the visibility timeout duration before becoming available for retry. To reduce retry delays, configure the queue's visibility timeout to an appropriate value for your use case.
- **With maxBatchWindowInSeconds** – The SQS poller dynamically sets the visibility timeout for polled messages using the formula: `functionTimeout + maxBatchWindowInSeconds + 30 seconds`. For EventBridge Pipes, the function timeout is 7 minutes, resulting in a visibility timeout of approximately 7.5 minutes plus your configured `maxBatchWindowInSeconds` value. When processing fails, messages remain hidden for this extended duration before becoming available for retry.

This behavior is particularly relevant when using [partial batch responses](eb-pipes-batching-concurrency.md#pipes-partial-batch-failure "eb-pipes-batching-concurrency.md#pipes-partial-batch-failure"). If you require faster retry timing, avoid setting `maxBatchWindowInSeconds` and instead rely on the queue's configured visibility timeout.

## Pipe DLQ behavior

A pipe inherits dead-letter queue (DLQ) behavior from the source:

- If the source Amazon SQS queue has a configured DLQ, messages are automatically delivered there
  after the specified number of attempts.
- For stream sources, such as DynamoDB and Kinesis streams, you can configure a
  DLQ for the pipe and route events. DynamoDB and Kinesis stream sources support Amazon SQS queues and
  Amazon SNS topics as DLQ targets.

If you specify a `DeadLetterConfig` for a pipe with a Kinesis or DynamoDB source, make sure that the `MaximumRecordAgeInSeconds` property on the pipe
is less than the `MaximumRecordAge` of the source event. `MaximumRecordAgeInSeconds` controls when the pipe poller will give up on the event and deliver it to
the DLQ and the `MaximumRecordAge` controls how long the message will be visible in the source stream before it gets deleted. Therefore, set `MaximumRecordAgeInSeconds`
to a value that is less than the source `MaximumRecordAge` so that there's adequate time between when the event gets sent to the DLQ, and when it gets automatically deleted
by the source for you to determine why the event went to the DLQ.

For Amazon MQ sources, the DLQ can be configured directly on the message broker.

EventBridge Pipes does not support first-in first-out (FIFO) DLQs for stream sources.

EventBridge Pipes does not support DLQ for Amazon MSK stream and Self managed Apache Kafka stream sources.

## Pipe failure states

Creating, deleting, and updating pipes are asynchronous operations that might result in a
failure state. Likewise, a pipe might be automatically disabled due to failures. In all cases,
the pipe `StateReason` provides information to help troubleshoot the
failure.

The following is a sample of the possible `StateReason` values:

- Stream not found. To resume processing please delete the pipe and create a new one.
- Pipes does not have required permissions to perform Queue operations (sqs:ReceiveMessage, sqs:DeleteMessage and sqs:GetQueueAttributes)
- Connection error. Your VPC must be able to connect to pipes. You can provide access by configuring a NAT Gateway or a VPC Endpoint to pipes-data. For how to setup NAT gateway or VPC Endpoint to pipes-data, please check AWS documentation.
- MSK cluster does not have security groups associated with it

A pipe may be automatically stopped with an updated `StateReason`. Possible reasons include:

- A Step Functions standard workflow configured as an [enrichment](eb-pipes.md#pipes-enrichment "eb-pipes.md#pipes-enrichment").
- A Step Functions standard workflow configured as as a target to be [invoked synchronously](eb-pipes.md#pipes-invocation "eb-pipes.md#pipes-invocation").

## Custom encryption failures

If you configure a source to use an AWS KMS custom encryption key (CMK), rather than an
AWS-managed AWS KMS key, you must explicitly give your pipe's Execution Role decryption permission. To do so, include the following additional permission in the custom CMK policy:

```
  {
      "Sid": "Allow Pipes access",
      "Effect": "Allow",
      "Principal": {
          `"AWS": "arn:aws:iam::01234567890:role/service-role/Amazon_EventBridge_Pipe_DDBStreamSourcePipe_12345678"`
      },
      "Action": "kms:Decrypt",
      "Resource": "*"
  }
```

Replace the above role with your pipe's Execution Role.

Next, ensure that the same permissions for KMS are added to your Pipe execution role.

This is true for all pipe sources with AWS KMS CMK, including:

- Amazon DynamoDB Streams
- Amazon Kinesis Data Streams
- Amazon MQ
- Amazon MSK
- Amazon SQS
