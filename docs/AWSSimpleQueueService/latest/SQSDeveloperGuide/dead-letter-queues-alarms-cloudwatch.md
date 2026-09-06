

# Creating alarms for dead-letter queues using Amazon CloudWatch
<a name="dead-letter-queues-alarms-cloudwatch"></a>

Set up a CloudWatch alarm to monitor messages in a dead-letter queue using the [`ApproximateNumberOfMessagesVisible`](sqs-available-cloudwatch-metrics.md) metric. For detailed instructions, see [Creating CloudWatch alarms for Amazon SQS metrics](set-cloudwatch-alarms-for-metrics.md). When the alarm triggers, indicating messages have been moved to the dead-letter queue, you can [poll](sqs-short-and-long-polling.md) the queue to review and retrieve them.