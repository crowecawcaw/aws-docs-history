# Amazon SQS API permissions:

Actions and resource reference

When you set up [Access control](security_iam_service-with-iam.md#access-control "security_iam_service-with-iam.md#access-control") and write permissions policies that you
can attach to an IAM identity, you can use the following table as a
reference. The table lists
each Amazon Simple Queue Service action,
the corresponding actions for which you can grant permissions to perform the
action, and the AWS resource for which you can grant the
permissions.

Specify the actions in the policy's `Action` field, and the
resource value in the policy's `Resource` field. To specify an
action, use the `sqs:` prefix followed by the action name (for
example, `sqs:CreateQueue`).

Currently, Amazon SQS supports the [global
condition context keys available in IAM](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").

Use the scroll bars to see the rest of the table.

| Amazon Simple Queue Service API and required permissions for actions | Amazon SQS actions                                      | Required permissions                                    | Resource |
| -------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | -------- |
| `AddPermission`                                                      | `sqs:AddPermission`                                     | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `CancelMessageMoveTask`                                              | `sqs:CancelMessageMoveTask`                             | `arn:aws:sqs:`region`:`account_id`:`dlq_queue_name``    |
| `sqs:ReceiveMessage`                                                 |
| `sqs:DeleteMessage`                                                  |
| `sqs:GetQueueAttributes`                                             |
| `ChangeMessageVisibility`                                            | `sqs:ChangeMessageVisibility`                           | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `ChangeMessageVisibilityBatch`                                       |
| `CreateQueue`                                                        | `sqs:CreateQueue`                                       | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `DeleteMessage`                                                      | `sqs:DeleteMessage`                                     | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `DeleteMessageBatch`                                                 |
| `DeleteQueue`                                                        | `sqs:DeleteQueue`                                       | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `GetQueueAttributes`                                                 | `sqs:GetQueueAttributes`                                | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `GetQueueUrl`                                                        | `sqs:GetQueueUrl`                                       | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `ListDeadLetterSourceQueues`                                         | `sqs:ListDeadLetterSourceQueues`                        | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `ListMessageMoveTasks`                                               | `sqs:ListMessageMoveTasks`                              | `arn:aws:sqs:`region`:`account_id`:`dlq_queue_name``    |
| `sqs:GetQueueAttributes`                                             |
| `ListQueues`                                                         | `sqs:ListQueues`                                        | `arn:aws:sqs:`region`:`account_id`:*`                   |
| `ListQueueTags`                                                      | `sqs:ListQueueTags`                                     | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `PurgeQueue`                                                         | `sqs:PurgeQueue`                                        | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `ReceiveMessage`                                                     | `sqs:ReceiveMessage`                                    | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `RemovePermission`                                                   | `sqs:RemovePermission`                                  | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `SendMessage`                                                        | `sqs:SendMessage`                                       | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `SendMessageBatch`                                                   |
| `SetQueueAttributes`                                                 | `sqs:SetQueueAttributes`                                | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `StartMessageMoveTask`                                               | `sqs:StartMessageMoveTask`                              | `arn:aws:sqs:`region`:`account_id`:`source_queue_name`` |
| `sqs:ReceiveMessage`                                                 |
| `sqs:DeleteMessage`                                                  |
| `sqs:GetQueueAttributes`                                             |
| `sqs:SendMessage`                                                    | `arn:aws:sqs:`region`:`account_id`:`source_queue_name`` |
| `TagQueue`                                                           | `sqs:TagQueue`                                          | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
| `UntagQueue`                                                         | `sqs:UntagQueue`                                        | `arn:aws:sqs:`region`:`account_id`:`queue_name``        |
