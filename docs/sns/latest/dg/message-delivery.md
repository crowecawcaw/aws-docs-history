

# Amazon SNS message delivery
<a name="message-delivery"></a>

This topic describes how Amazon SNS handles message delivery. You'll learn about raw message delivery, where Amazon SNS delivers messages in their original, unmodified format to the endpoint. You'll also learn how to send messages from an Amazon SNS topic to an Amazon SQS queue in a different AWS account.

This topic covers the delivery of Amazon SNS messages to an Amazon SQS queue or a Lambda function in a different AWS Region. It explains how cross-Region delivery works and what to consider when using it.

You'll also learn how to monitor delivery status, which tells you whether messages were delivered or encountered issues. When delivery fails, Amazon SNS automatically retries to ensure messages reach their destinations. Messages that can't be delivered after multiple attempts go to a dead-letter queue. You can use the dead-letter queue to analyze and troubleshoot delivery failures.