

# Amazon SQS message deduplication and grouping
<a name="best-practices-message-deduplication"></a>

This topic provides best practices for ensuring consistent message processing in Amazon SQS. It explains how to use:
+ [`MessageDeduplicationId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html#API_SendMessage_RequestSyntax) to prevent duplicate messages in FIFO queues.
+ [`MessageGroupId`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) to manage message ordering within distinct message groups.

****Topics****
+ [Avoiding inconsistent message processing in Amazon SQS](avoiding-inconsistent-message-processing.md)
+ [Using the message deduplication ID](using-messagededuplicationid-property.md)
+ [Using the message group ID](using-messagegroupid-property.md)
+ [Using the receive request attempt ID](using-receiverequestattemptid-request-parameter.md)