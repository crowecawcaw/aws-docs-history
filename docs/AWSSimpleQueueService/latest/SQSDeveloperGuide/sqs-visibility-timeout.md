

# Amazon SQS visibility timeout
<a name="sqs-visibility-timeout"></a>

When you receive a message from an Amazon SQS queue, it remains in the queue but becomes temporarily invisible to other consumers. This invisibility is controlled by the visibility timeout, which ensures that other consumers cannot process the same message while you are working on it. Amazon SQS offers two options for deleting messages after processing:
+ **Manual deletion** – You explicitly delete messages using the [`DeleteMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html) action.
+ **Automatic deletion** – Supported in certain AWS SDKs, messages are automatically deleted upon successful processing, simplifying workflows.

![Time line graph displaying how requests are processed during visibility timeout](http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/images/sqs-visibility-timeout-diagram.png)


## Visibility timeout use cases
<a name="visibility-timeout-use-case"></a>

**Manage long-running tasks** – Use the visibility timeout to handle tasks that require extended processing times. Set an appropriate visibility timeout for messages that require extended processing time. This ensures that other consumers don't pick up the same message while it's being processed, preventing duplicate work and maintaining system efficiency.

**Implement retry mechanisms** – Extend the visibility timeout programmatically for tasks that fail to complete within the initial timeout. If a task fails to complete within the initial visibility timeout, you can extend the timeout programmatically. This allows your system to retry processing the message without it becoming visible to other consumers, improving fault tolerance and reliability. Combine with **Dead-Letter Queues (DLQs)** to manage persistent failures.

**Coordinate distributed systems** – Use SQS visibility timeout to coordinate tasks across distributed systems. Set visibility timeouts that align with your expected processing times for different components. This helps maintain consistency and prevents race conditions in complex, distributed architectures.

**Optimize resource utilization** – Adjust SQS visibility timeouts to optimize resource utilization in your application. By setting appropriate timeouts, you can ensure that messages are processed efficiently without tying up resources unnecessarily. This leads to better overall system performance and cost-effectiveness.

## Setting and adjusting the visibility timeout
<a name="configuring-visibility-timeout"></a>

The visibility timeout starts as soon as a message is delivered to you. During this period, you're expected to process and delete the message. If you don't delete it before the timeout expires, the message becomes visible again in the queue and can be retrieved by another consumer. The default visibility timeout for a queue is 30 seconds, but you can adjust this to match the time your application needs to process and delete a message. You can also set a specific visibility timeout for individual messages without changing the queue's overall setting. Use the [`ChangeMessageVisibility`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html) action to programmatically extend or shorten the timeout as needed.

## In flight messages and quotas
<a name="inflight-messages"></a>

In Amazon SQS, in-flight messages are messages that have been received by a consumer but not yet deleted. For standard queues, there's a limit of approximately 120,000 in-flight messages, depending on queue traffic and message backlog. If you reach this limit, Amazon SQS returns an `OverLimit` error, indicating that no additional messages can be received until some in-flight messages are deleted. For FIFO queues, limits depend on active message groups.
+ **When using short polling** – If this limit is reached while using short polling, Amazon SQS will return an `OverLimit` error, indicating that no additional messages can be received until some in-flight messages are deleted.
+ **When using long polling** – If you are using long polling, Amazon SQS does not return an error when the in-flight message limit is reached. Instead, it will not return any new messages until the number of in-flight messages drops below the limit.

To manage in-flight messages effectively:

1. **Prompt deletion** – Delete messages (manually or automatically) after processing to reduce the in-flight count.

1. **Monitor with CloudWatch** – Set alarms for high in-flight counts to prevent reaching the limit.

1. **Distribute load** – If you're processing a high volume of messages, use additional queues or consumers to balance load and avoid bottlenecks.

1. **Request a quota increase** – Submit a request to [AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/create-service-quota-increase.html) if higher limits are required.

## Understanding visibility timeout in standard and FIFO queues
<a name="visibility-timeout-standard-fifo-queues"></a>

In both standard and FIFO (First-In-First-Out) queues, the visibility timeout helps prevent multiple consumers from processing the same message simultaneously. However, due to the at-least-once delivery model of Amazon SQS, there's no absolute guarantee that a message won't be delivered more than once during the visibility timeout period.
+ **Standard queues** – The visibility timeout in standard queues prevents multiple consumers from processing the same message at the same time. However, because of the at-least-once delivery model, Amazon SQS doesn't guarantee that a message won’t be delivered more than once within the visibility timeout period.
+ **FIFO queues** – For FIFO queues, messages with the same message group ID are processed in a strict sequence. When a message with a message group ID is in-flight, subsequent messages in that group are not made available until the in-flight message is either deleted or the visibility timeout expires. However, this doesn’t "lock" the group indefinitely– each message is processed in sequence, and only when each message is deleted or becomes visible again will the next message in that group be available to consumers. This approach ensures ordered processing within the group without unnecessarily locking the group from delivering messages.

## Handling failures
<a name="consumer-fails-to-process-message"></a>

If you don't process and delete a message before the visibility timeout expires—due to application errors, crashes, or connectivity problems—the message becomes visible again in the queue. It can then be retrieved by the same or a different consumer for another processing attempt. This ensures that messages aren't lost even if the initial processing fails. However, setting the visibility timeout too high can delay the reappearance of unprocessed messages, potentially slowing down retries. It's crucial to set an appropriate visibility timeout based on the expected processing time for timely message handling.

## Changing and terminating visibility timeout
<a name="changing-terminating-visibility-timeout"></a>

You can change or terminate the visibility timeout using the `ChangeMessageVisibility` action:
+ **Changing the timeout** – Adjust the visibility timeout dynamically using [`ChangeMessageVisibility`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html). This allows you to extend or reduce timeout durations to match processing needs.
+ **Terminating the timeout** – If you decide not to process a received message, terminate its visibility timeout by setting the `VisibilityTimeout` to 0 seconds through the `ChangeMessageVisibility` action. This immediately makes the message available for other consumers to process.

## Best practices
<a name="visibility-timeout-best-practices"></a>

Use the following best practices for managing visibility timeouts in Amazon SQS, including setting, adjusting, and extending timeouts, as well as handling unprocessed messages using Dead-Letter Queues (DLQs).
+ **Setting and adjusting the timeout.** Start by setting the visibility timeout to match the maximum time your application typically needs to process and delete a message. If you're unsure about the exact processing time, begin with a shorter timeout (for example, 2 minutes) and extend it as necessary. Implement a heartbeat mechanism to periodically extend the visibility timeout, ensuring the message remains invisible until processing is complete. This minimizes delays in reprocessing unhandled messages and prevents premature visibility.
+ **Extending the timeout and handling the 12-Hour limit.** If your processing time varies or may exceed the initially set timeout, use the `ChangeMessageVisibility` action to extend the visibility timeout while processing the message. Keep in mind that the visibility timeout has a maximum limit of 12 hours from when the message is first received. Extending the timeout doesn't reset this 12-hour limit. If your processing requires more time than this limit, consider using AWS Step Functions or breaking the task into smaller steps.
+ **Handling unprocessed messages.** To manage messages that fail multiple processing attempts, configure a Dead-Letter Queue (DLQ). This ensures that messages that can't be processed after several retries are captured separately for further analysis or handling, preventing them from repeatedly circulating in the main queue. 