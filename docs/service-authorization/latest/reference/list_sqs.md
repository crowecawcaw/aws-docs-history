

# Actions, resources, and condition keys for Amazon SQS
<a name="list_sqs"></a>

Amazon SQS (service prefix: `sqs`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-authentication-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sqs/sqs.json) for this service.

**Topics**
+ [API operations defined by Amazon SQS](#list_sqs-operations)
+ [Actions defined by Amazon SQS](#list_sqs-actions-as-permissions)
+ [Resource types defined by Amazon SQS](#list_sqs-resources-for-iam-policies)
+ [Condition keys for Amazon SQS](#list_sqs-policy-keys)

## API operations defined by Amazon SQS
<a name="list_sqs-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sqs-actions-as-permissions).




- **   AddPermission  **
  - **IAM action:**  [sqs:AddPermission](#list_sqs-action-AddPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CancelMessageMoveTask  **
  - **IAM action:**  [sqs:CancelMessageMoveTask](#list_sqs-action-CancelMessageMoveTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sqs:DeleteMessage](#list_sqs-action-DeleteMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sqs:GetQueueAttributes](#list_sqs-action-GetQueueAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sqs:ReceiveMessage](#list_sqs-action-ReceiveMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ChangeMessageVisibility  **
  - **IAM action:**  [sqs:ChangeMessageVisibility](#list_sqs-action-ChangeMessageVisibility) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ChangeMessageVisibilityBatch  **
  - **IAM action:**  [sqs:ChangeMessageVisibility](#list_sqs-action-ChangeMessageVisibility) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQueue  **
  - **IAM action:**  [sqs:CreateQueue](#list_sqs-action-CreateQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sqs:TagQueue](#list_sqs-action-TagQueue)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteMessage  **
  - **IAM action:**  [sqs:DeleteMessage](#list_sqs-action-DeleteMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMessageBatch  **
  - **IAM action:**  [sqs:DeleteMessage](#list_sqs-action-DeleteMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQueue  **
  - **IAM action:**  [sqs:DeleteQueue](#list_sqs-action-DeleteQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetQueueAttributes  **
  - **IAM action:**  [sqs:GetQueueAttributes](#list_sqs-action-GetQueueAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQueueUrl  **
  - **IAM action:**  [sqs:GetQueueUrl](#list_sqs-action-GetQueueUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDeadLetterSourceQueues  **
  - **IAM action:**  [sqs:ListDeadLetterSourceQueues](#list_sqs-action-ListDeadLetterSourceQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMessageMoveTasks  **
  - **IAM action:**  [sqs:GetQueueAttributes](#list_sqs-action-GetQueueAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sqs:ListMessageMoveTasks](#list_sqs-action-ListMessageMoveTasks)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   ListQueueTags  **
  - **IAM action:**  [sqs:ListQueueTags](#list_sqs-action-ListQueueTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListQueues  **
  - **IAM action:**  [sqs:ListQueues](#list_sqs-action-ListQueues) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PurgeQueue  **
  - **IAM action:**  [sqs:PurgeQueue](#list_sqs-action-PurgeQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ReceiveMessage  **
  - **IAM action:**  [sqs:ReceiveMessage](#list_sqs-action-ReceiveMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RemovePermission  **
  - **IAM action:**  [sqs:RemovePermission](#list_sqs-action-RemovePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SendMessage  **
  - **IAM action:**  [sqs:SendMessage](#list_sqs-action-SendMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendMessageBatch  **
  - **IAM action:**  [sqs:SendMessage](#list_sqs-action-SendMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetQueueAttributes  **
  - **IAM action:**  [sqs:SetQueueAttributes](#list_sqs-action-SetQueueAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   StartMessageMoveTask  **
  - **IAM action:**  [sqs:DeleteMessage](#list_sqs-action-DeleteMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sqs:GetQueueAttributes](#list_sqs-action-GetQueueAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sqs:ReceiveMessage](#list_sqs-action-ReceiveMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [sqs:SendMessage](#list_sqs-action-SendMessage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sqs:StartMessageMoveTask](#list_sqs-action-StartMessageMoveTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   TagQueue  **
  - **IAM action:**  [sqs:TagQueue](#list_sqs-action-TagQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagQueue  **
  - **IAM action:**  [sqs:UntagQueue](#list_sqs-action-UntagQueue) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by Amazon SQS
<a name="list_sqs-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddPermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_AddPermission.html)  **
  - **Description:** Grants permission to a queue for a specific principal
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CancelMessageMoveTask](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CancelMessageMoveTask.html)  **
  - **Description:** Grants permission to cancel an in progress message move task
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ChangeMessageVisibility](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ChangeMessageVisibility.html)  **
  - **Description:** Grants permission to change the visibility timeout of a specified message in a queue to a new value
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_CreateQueue.html)  **
  - **Description:** Grants permission to create a new queue, or returns the URL of an existing one
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqs-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteMessage.html)  **
  - **Description:** Grants permission to delete the specified message from the specified queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_DeleteQueue.html)  **
  - **Description:** Grants permission to delete the queue specified by the queue URL, regardless of whether the queue is empty
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueAttributes.html)  **
  - **Description:** Grants permission to get attributes for the specified queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQueueUrl](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_GetQueueUrl.html)  **
  - **Description:** Grants permission to return the URL of an existing queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDeadLetterSourceQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListDeadLetterSourceQueues.html)  **
  - **Description:** Grants permission to return a list of your queues that have the RedrivePolicy queue attribute configured with a dead letter queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMessageMoveTasks](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListMessageMoveTasks.html)  **
  - **Description:** Grants permission to list message move tasks
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListQueueTags](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueueTags.html)  **
  - **Description:** Grants permission to list tags added to an SQS queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListQueues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ListQueues.html)  **
  - **Description:** Grants permission to return a list of your queues
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PurgeQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_PurgeQueue.html)  **
  - **Description:** Grants permission to delete the messages in a queue specified by the queue URL
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html)  **
  - **Description:** Grants permission to retrieve one or more messages, with a maximum limit of 10 messages, from the specified queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RemovePermission](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_RemovePermission.html)  **
  - **Description:** Grants permission to revoke any permissions in the queue policy that matches the specified Label parameter
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SendMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SendMessage.html)  **
  - **Description:** Grants permission to deliver a message to the specified queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetQueueAttributes](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_SetQueueAttributes.html)  **
  - **Description:** Grants permission to set the value of one or more queue attributes
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [StartMessageMoveTask](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_StartMessageMoveTask.html)  **
  - **Description:** Grants permission to start a message move task
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_TagQueue.html)  **
  - **Description:** Grants permission to add tags to the specified SQS queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sqs-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqs-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagQueue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_UntagQueue.html)  **
  - **Description:** Grants permission to remove tags from the specified SQS queue
  - **Resource types (\*required):** [queue\*](#list_sqs-resource-queue)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sqs-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by Amazon SQS
<a name="list_sqs-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [queue](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-queue-types.html)  | arn:${Partition}:sqs:${Region}:${Account}:${QueueName} | [aws:ResourceTag/${TagKey}](#list_sqs-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon SQS
<a name="list_sqs-policy-keys"></a>

Amazon SQS defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 