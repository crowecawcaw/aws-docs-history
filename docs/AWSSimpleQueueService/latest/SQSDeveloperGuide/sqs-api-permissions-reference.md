

# Amazon SQS API permissions: Actions and resource reference
<a name="sqs-api-permissions-reference"></a>

When you set up [Access control](security_iam_service-with-iam.md#access-control) and write permissions policies that you can attach to an IAM identity, you can use the following table as a reference. The table lists each Amazon Simple Queue Service action, the corresponding actions for which you can grant permissions to perform the action, and the AWS resource for which you can grant the permissions.

Specify the actions in the policy's `Action` field, and the resource value in the policy's `Resource` field. To specify an action, use the `sqs:` prefix followed by the action name (for example, `sqs:CreateQueue`).

Currently, Amazon SQS supports the [global condition context keys available in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html).

Use the scroll bars to see the rest of the table.


**Amazon Simple Queue Service API and required permissions for actions**  
<a name="sqs-api-and-required-permissions-for-actions-table"></a>

- ** `[AddPermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html)` **
  - **Required permissions:** sqs:AddPermission
  - **Resource:** `arn:aws:sqs:{{region}}:{{account_id}}:{{queue_name}}`

- **`[CancelMessageMoveTask](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CancelMessageMoveTask.html)`**
  - **Required permissions:**
    - sqs:CancelMessageMoveTask
    - sqs:ReceiveMessage
    - sqs:DeleteMessage
    - sqs:GetQueueAttributes
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{dlq\_queue\_name}}

- ** `[ChangeMessageVisibility](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html)` **
  - **Required permissions:** sqs:ChangeMessageVisibility
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[ChangeMessageVisibilityBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibilityBatch.html)` **

- ** `[CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html)` **
  - **Required permissions:** sqs:CreateQueue
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html)` **
  - **Required permissions:** sqs:DeleteMessage
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[DeleteMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessageBatch.html)` **

- ** `[DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html)` **
  - **Required permissions:** sqs:DeleteQueue
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html)` **
  - **Required permissions:** sqs:GetQueueAttributes
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html)` **
  - **Required permissions:** sqs:GetQueueUrl
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[ListDeadLetterSourceQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html)` **
  - **Required permissions:** sqs:ListDeadLetterSourceQueues
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- **`[ListMessageMoveTasks](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html)`**
  - **Required permissions:**
    - sqs:ListMessageMoveTasks
    - sqs:GetQueueAttributes
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{dlq\_queue\_name}}

- ** `[ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html)` **
  - **Required permissions:** sqs:ListQueues
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:\*

- ** `[ListQueueTags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html)` **
  - **Required permissions:** sqs:ListQueueTags
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[PurgeQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html)` **
  - **Required permissions:** sqs:PurgeQueue
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html)` **
  - **Required permissions:** sqs:ReceiveMessage
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[RemovePermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_RemovePermission.html)` **
  - **Required permissions:** sqs:RemovePermission
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)` **
  - **Required permissions:** sqs:SendMessage
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[SendMessageBatch](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessageBatch.html)` **

- ** `[SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html)` **
  - **Required permissions:** sqs:SetQueueAttributes
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- **`[StartMessageMoveTask](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_StartMessageMoveTask.html)`**
  - **Required permissions:** sqs:StartMessageMoveTask / **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{source\_queue\_name}}
  - **Required permissions:** sqs:ReceiveMessage
  - **Required permissions:** sqs:DeleteMessage
  - **Required permissions:** sqs:GetQueueAttributes
  - **Required permissions:** sqs:SendMessage / **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{source\_queue\_name}}

- ** `[TagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_TagQueue.html)` **
  - **Required permissions:** sqs:TagQueue
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

- ** `[UntagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_UntagQueue.html)` **
  - **Required permissions:** sqs:UntagQueue
  - **Resource:** arn:aws:sqs:{{region}}:{{account\_id}}:{{queue\_name}}

