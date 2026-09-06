

# Using custom policies with the Amazon SQS Access Policy Language
<a name="sqs-creating-custom-policies"></a>

To grant basic permissions (such as [`SendMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html) or [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html)) based only on an AWS account ID, you don’t need to write a custom policy. Instead, use the Amazon SQS [`AddPermission`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html) action.

To allow or deny access based on specific conditions, such as request time or the requester's IP address, you must create a custom Amazon SQS policy and upload it using the [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html) action.

**Topics**
+ [Access control architecture](sqs-creating-custom-policies-architecture.md)
+ [Access control process workflow](sqs-creating-custom-policies-process-workflow.md)
+ [Access Policy Language key concepts](sqs-creating-custom-policies-key-concepts.md)
+ [Access Policy Language evaluation logic](sqs-creating-custom-policies-evaluation-logic.md)
+ [Relationships between explicit and default denials](sqs-creating-custom-policies-relationships-between-explicit-default-denials.md)
+ [Custom policy limitations](sqs-limitations-of-custom-policies.md)
+ [Custom Access Policy Language examples](sqs-creating-custom-policies-access-policy-examples.md)