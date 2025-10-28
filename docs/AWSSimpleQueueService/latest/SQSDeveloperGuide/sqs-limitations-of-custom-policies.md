# Limitations of Amazon SQS custom

policies

## Cross-account access

Cross-account permissions don't apply to the following actions:

- `AddPermission`
- `CancelMessageMoveTask`
- `CreateQueue`
- `DeleteQueue`
- `ListMessageMoveTask`
- `ListQueues`
- `ListQueueTags`
- `RemovePermission`
- `SetQueueAttributes`
- `StartMessageMoveTask`
- `TagQueue`
- `UntagQueue`

## Condition keys

Currently, Amazon SQS supports only a limited subset of the [condition keys available in IAM](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys"). For more information, see
[Amazon SQS API permissions:
Actions and resource reference](sqs-api-permissions-reference.md "sqs-api-permissions-reference.md").
