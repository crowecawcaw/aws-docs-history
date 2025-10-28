# Capturing problematic messages in

Amazon SQS

To capture all messages that can't be processed, and to collect accurate CloudWatch metrics,
configure a [dead-letter queue](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md").

- The redrive policy redirects messages to a dead-letter queue after the source
  queue fails to process a message a specified number of times.
- Using a dead-letter queue decreases the number of messages and reduces the
  possibility of exposing you to _poison pill_ messages
  (messages that are received but can't be processed).
- Including a poison pill message in a queue can distort the [ApproximateAgeOfOldestMessage](sqs-available-cloudwatch-metrics.md "sqs-available-cloudwatch-metrics.md") CloudWatch metric by giving
  an incorrect age of the poison pill message. Configuring a dead-letter queue
  helps avoid false alarms when using this metric.
