# Setting-up dead-letter queue

retention in Amazon SQS

For standard queues, the expiration of a message is always based on its original enqueue timestamp.
When a message is moved to a dead-letter queue, the enqueue timestamp is unchanged. The
`ApproximateAgeOfOldestMessage` metric indicates when the message moved to
the dead-letter queue, _not_ when the message was originally sent.
For example, assume that a message spends 1 day in the original queue before it's moved to a dead-letter queue.
If the dead-letter queue's retention period is 4 days, the message is deleted from the dead-letter queue after 3 days
and the `ApproximateAgeOfOldestMessage` is 3 days. Thus, it is a best practice
to always set the retention period of a dead-letter queue to be longer than the
retention period of the original queue.

For FIFO queues, the enqueue timestamp resets when the message is moved to a dead-letter queue.
The `ApproximateAgeOfOldestMessage` metric indicates when the message moved to the dead-letter queue.
In the same example above, the message is deleted from the dead-letter queue after 4 days and the `ApproximateAgeOfOldestMessage` is 4 days.
