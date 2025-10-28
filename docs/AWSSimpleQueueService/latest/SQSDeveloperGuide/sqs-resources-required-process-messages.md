# Resources required to process

Amazon SQS messages

Amazon SQS provides estimates of the approximate number of delayed, visible, and not visible
messages in a queue to help you assess the resources needed for processing. For more
information about visibility, see [Amazon SQS visibility timeout](sqs-visibility-timeout.md "sqs-visibility-timeout.md").

###### Note

For some metrics, the result is approximate because of the distributed architecture of Amazon SQS. In most cases, the count should be close to the actual number of messages in the queue.

The following table lists the attribute name to use with the `GetQueueAttributes`
action:

| Task                                                                                                                                                                                                                                  | Attribute name                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Get the approximate number of messages available for retrieval from the queue.                                                                                                                                                        | `ApproximateNumberOfMessagesVisible`    |
| Get the approximate number of messages in the queue that are delayed and not available for reading immediately. This can happen when the queue is configured as a delay queue or when a message has been sent with a delay parameter. | `ApproximateNumberOfMessagesDelayed`    |
| Get the approximate number of messages that are in flight. Messages are considered to be _in flight_ if they have been sent to a client but have not yet been deleted or have not yet reached the end of their visibility window.     | `ApproximateNumberOfMessagesNotVisible` |
