# Amazon SNS message delivery

This topic describes how Amazon SNS handles message delivery across various scenarios. You'll
learn about raw message delivery, where Amazon SNS delivers messages in their original,
unmodified format to the endpoint. You'll also discover how to send messages from an Amazon SNS
topic to an Amazon SQS queue in a different AWS account, providing insights into cross-account
messaging.

This topic provides information on the delivery of Amazon SNS messages to an Amazon SQS queue or a
Lambda function in different AWS Regions, how cross-region delivery works, and the
considerations involved.

Additionally, you'll learn how to monitor and interpret message delivery status, which
provides critical information on whether messages were successfully delivered or encountered
issues. In cases where message delivery fails, you'll understand the message delivery retry
process, including how Amazon SNS automatically attempts to redeliver messages to ensure they
reach their intended destinations. This topic also discusses the use of dead-letter queues
to capture messages that could not be delivered after multiple attempts, enabling you to
analyze and troubleshoot these failures effectively.
