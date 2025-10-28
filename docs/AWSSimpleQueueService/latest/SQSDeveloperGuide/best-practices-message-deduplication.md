# Amazon SQS message deduplication and

grouping

This topic provides best practices for ensuring consistent message processing in Amazon SQS. It
explains how to use:

- [`MessageDeduplicationId`](../APIReference/API_SendMessage.md#API_SendMessage_RequestSyntax "../APIReference/API_SendMessage.md#API_SendMessage_RequestSyntax") to prevent duplicate messages
  in FIFO queues.
- [`MessageGroupId`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") to manage message ordering within
  distinct message groups.

###### Topics

- [Avoiding inconsistent message
  processing in Amazon SQS](avoiding-inconsistent-message-processing.md "avoiding-inconsistent-message-processing.md")
- [Using the message deduplication ID](using-messagededuplicationid-property.md "using-messagededuplicationid-property.md")
- [Using the message group ID](using-messagegroupid-property.md "using-messagegroupid-property.md")
- [Using the receive request attempt ID](using-receiverequestattemptid-request-parameter.md "using-receiverequestattemptid-request-parameter.md")
