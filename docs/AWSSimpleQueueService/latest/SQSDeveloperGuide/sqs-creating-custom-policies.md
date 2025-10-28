# Using custom policies with the Amazon SQS

Access Policy Language

To grant basic permissions (such as [`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") or [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md"))
based only on an AWS account ID, you don’t need to write a custom policy. Instead,
use the Amazon SQS [`AddPermission`](../APIReference/API_AddPermission.md "../APIReference/API_AddPermission.md") action.

To allow or deny access based on specific conditions, such as request time or the
requester's IP address, you must create a custom Amazon SQS policy and upload it using
the [SetQueueAttributes](../APIReference/API_SetQueueAttributes.md "../APIReference/API_SetQueueAttributes.md") action.

###### Topics

- [Access control architecture](sqs-creating-custom-policies-architecture.md "sqs-creating-custom-policies-architecture.md")
- [Access control process workflow](sqs-creating-custom-policies-process-workflow.md "sqs-creating-custom-policies-process-workflow.md")
- [Access Policy Language key concepts](sqs-creating-custom-policies-key-concepts.md "sqs-creating-custom-policies-key-concepts.md")
- [Access Policy Language evaluation logic](sqs-creating-custom-policies-evaluation-logic.md "sqs-creating-custom-policies-evaluation-logic.md")
- [Relationships between explicit and default denials](sqs-creating-custom-policies-relationships-between-explicit-default-denials.md "sqs-creating-custom-policies-relationships-between-explicit-default-denials.md")
- [Custom policy limitations](sqs-limitations-of-custom-policies.md "sqs-limitations-of-custom-policies.md")
- [Custom Access Policy Language examples](sqs-creating-custom-policies-access-policy-examples.md "sqs-creating-custom-policies-access-policy-examples.md")
