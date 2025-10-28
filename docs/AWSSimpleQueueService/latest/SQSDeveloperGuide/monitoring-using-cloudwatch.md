# Monitoring Amazon SQS queues using CloudWatch

Amazon SQS and Amazon CloudWatch are integrated so you can use CloudWatch to view and analyze metrics for
your Amazon SQS queues. You can view and analyze your queues' metrics from the [Amazon SQS console](sqs-access-metrics.md#access-cloudwatch-metrics-sqs-console "sqs-access-metrics.md#access-cloudwatch-metrics-sqs-console"), the [CloudWatch console](sqs-access-metrics.md#access-metrics-cloudwatch-console "sqs-access-metrics.md#access-metrics-cloudwatch-console"), using the [AWS CLI](sqs-access-metrics.md#access-cloudwatch-metrics-cli "sqs-access-metrics.md#access-cloudwatch-metrics-cli"), or using the [CloudWatch API](sqs-access-metrics.md#access-metrics-cloudwatch-api "sqs-access-metrics.md#access-metrics-cloudwatch-api"). You can also [set CloudWatch alarms](set-cloudwatch-alarms-for-metrics.md "set-cloudwatch-alarms-for-metrics.md") for Amazon SQS metrics.

CloudWatch metrics for your Amazon SQS queues are automatically collected
and pushed to CloudWatch at one-minute intervals.
These metrics are gathered on all queues
that meet the CloudWatch guidelines for being _active_. CloudWatch considers a queue to
be active for up to six hours if it contains any messages, or if any action accesses it.

When an Amazon SQS queue is inactive for more than six hours, the Amazon SQS service is considered
asleep and stops delivering metrics to the CloudWatch service. Missing data, or data representing
zero, can't be visualized in the CloudWatch metrics for Amazon SQS for the time period that your Amazon SQS
queue was inactive.

###### Note

- An Amazon SQS queue can be activated when the user calling an API against the queue is not
  authorized, and the request fails.
- The Amazon SQS console performs a [`GetQueueAttributes`](../APIReference/API_GetQueueAttributes.md "../APIReference/API_GetQueueAttributes.md") API call when the queue’s page is opened. The
  `GetQueueAttributes` API request activates the queue.
- A delay of up to 15 minutes occurs in CloudWatch metrics when a queue is activated from an
  inactive state.
- There is no charge for the Amazon SQS metrics reported in CloudWatch. They're provided as part of
  the Amazon SQS service.
- CloudWatch metrics are supported for both standard and FIFO queues.
