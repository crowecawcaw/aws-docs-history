

# Actions, resources, and condition keys for Amazon Braket
<a name="list_braket"></a>

Amazon Braket (service prefix: `braket`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/braket/latest/developerguide/what-is-braket.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/braket/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/braket/braket.json) for this service.

**Topics**
+ [API operations defined by Amazon Braket](#list_braket-operations)
+ [Actions defined by Amazon Braket](#list_braket-actions-as-permissions)
+ [Permission-only actions for Amazon Braket](#list_braket-permission-only-actions)
+ [Resource types defined by Amazon Braket](#list_braket-resources-for-iam-policies)
+ [Condition keys for Amazon Braket](#list_braket-policy-keys)

## API operations defined by Amazon Braket
<a name="list_braket-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_braket-actions-as-permissions).




- **   CancelJob  **
  - **IAM action:**  [braket:CancelJob](#list_braket-action-CancelJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelQuantumTask  **
  - **IAM action:**  [braket:CancelQuantumTask](#list_braket-action-CancelQuantumTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateJob  **
  - **IAM action:**  [braket:CreateJob](#list_braket-action-CreateJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [braket:TagResource](#list_braket-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** braket.amazonaws.com, sagemaker.amazonaws.com / **Access level:** Write

- **   CreateQuantumTask  **
  - **IAM action:**  [braket:CreateQuantumTask](#list_braket-action-CreateQuantumTask)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [braket:TagResource](#list_braket-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSpendingLimit  **
  - **IAM action:**  [braket:CreateSpendingLimit](#list_braket-action-CreateSpendingLimit)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [braket:TagResource](#list_braket-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteSpendingLimit  **
  - **IAM action:**  [braket:DeleteSpendingLimit](#list_braket-action-DeleteSpendingLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDevice  **
  - **IAM action:**  [braket:GetDevice](#list_braket-action-GetDevice) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetJob  **
  - **IAM action:**  [braket:GetJob](#list_braket-action-GetJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQuantumTask  **
  - **IAM action:**  [braket:GetQuantumTask](#list_braket-action-GetQuantumTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [braket:ListTagsForResource](#list_braket-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchDevices  **
  - **IAM action:**  [braket:SearchDevices](#list_braket-action-SearchDevices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchJobs  **
  - **IAM action:**  [braket:SearchJobs](#list_braket-action-SearchJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchQuantumTasks  **
  - **IAM action:**  [braket:SearchQuantumTasks](#list_braket-action-SearchQuantumTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchSpendingLimits  **
  - **IAM action:**  [braket:SearchSpendingLimits](#list_braket-action-SearchSpendingLimits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [braket:TagResource](#list_braket-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [braket:UntagResource](#list_braket-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateSpendingLimit  **
  - **IAM action:**  [braket:UpdateSpendingLimit](#list_braket-action-UpdateSpendingLimit) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Braket
<a name="list_braket-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelJob](https://docs.aws.amazon.com/braket/latest/APIReference/API_CancelJob.html)  **
  - **Description:** Grants permission to cancel a job
  - **Resource types (\*required):** [job\*](#list_braket-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelQuantumTask](https://docs.aws.amazon.com/braket/latest/APIReference/API_CancelQuantumTask.html)  **
  - **Description:** Grants permission to cancel a quantum task
  - **Resource types (\*required):** [quantum-task\*](#list_braket-resource-quantum-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateJob](https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateJob.html)  **
  - **Description:** Grants permission to create a job
  - **Resource types (\*required):** [device\*](#list_braket-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [job\*](#list_braket-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Access level:** Write

- **   [CreateQuantumTask](https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html)  **
  - **Description:** Grants permission to create a quantum task
  - **Resource types (\*required):** [device\*](#list_braket-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [quantum-task\*](#list_braket-resource-quantum-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSpendingLimit](https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateSpendingLimit.html)  **
  - **Description:** Grants permission to create a spending limit
  - **Resource types (\*required):** [device\*](#list_braket-resource-device) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [spending-limit\*](#list_braket-resource-spending-limit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteSpendingLimit](https://docs.aws.amazon.com/braket/latest/APIReference/API_DeleteSpendingLimit.html)  **
  - **Description:** Grants permission to delete a spending limit
  - **Resource types (\*required):** [spending-limit\*](#list_braket-resource-spending-limit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDevice](https://docs.aws.amazon.com/braket/latest/APIReference/API_GetDevice.html)  **
  - **Description:** Grants permission to retrieve information about the devices available in Amazon Braket
  - **Resource types (\*required):** [device\*](#list_braket-resource-device)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetJob](https://docs.aws.amazon.com/braket/latest/APIReference/API_GetJob.html)  **
  - **Description:** Grants permission to retrieve jobs
  - **Resource types (\*required):** [job\*](#list_braket-resource-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQuantumTask](https://docs.aws.amazon.com/braket/latest/APIReference/API_GetQuantumTask.html)  **
  - **Description:** Grants permission to retrieve quantum tasks
  - **Resource types (\*required):** [quantum-task\*](#list_braket-resource-quantum-task)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/braket/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to listing the tags that have been applied to the quantum task resource or the job
  - **Resource types (\*required):** [job](#list_braket-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [quantum-task](#list_braket-resource-quantum-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [spending-limit](#list_braket-resource-spending-limit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchDevices](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchDevices.html)  **
  - **Description:** Grants permission to search for devices available in Amazon Braket
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchJobs](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchJobs.html)  **
  - **Description:** Grants permission to search for jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchQuantumTasks](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchQuantumTasks.html)  **
  - **Description:** Grants permission to search for quantum tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchSpendingLimits](https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchSpendingLimits.html)  **
  - **Description:** Grants permission to search for spending limit
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/braket/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a quantum task or a hybrid job
  - **Resource types (\*required):** [job](#list_braket-resource-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [quantum-task](#list_braket-resource-quantum-task) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [spending-limit](#list_braket-resource-spending-limit) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_braket-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/braket/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a quantum task resource or a job. A tag consists of a key-value pair
  - **Resource types (\*required):** [job](#list_braket-resource-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [quantum-task](#list_braket-resource-quantum-task) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Resource types (\*required):** [spending-limit](#list_braket-resource-spending-limit) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_braket-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateSpendingLimit](https://docs.aws.amazon.com/braket/latest/APIReference/API_UpdateSpendingLimit.html)  **
  - **Description:** Grants permission to update a spending limit
  - **Resource types (\*required):** [spending-limit\*](#list_braket-resource-spending-limit)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for Amazon Braket
<a name="list_braket-permission-only-actions"></a>

The following actions are defined by Amazon Braket but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AcceptUserAgreement](${UserGuideDocPage})  | Grants permission to accept the Amazon Braket user agreement |  |   | Write | 
|   [GetServiceLinkedRoleStatus](${UserGuideDocPage})  | Grants permission to check if the Amazon Braket service linked role has been created |  |   | Read | 
|   [GetUserAgreementStatus](${UserGuideDocPage})  | Grants permission to check if the account has accepted the Amazon Braket user agreement |  |   | Read | 

## Resource types defined by Amazon Braket
<a name="list_braket-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [device](https://docs.aws.amazon.com/braket/latest/developerguide/restrict-access.html)  | arn:${Partition}:braket:\*:\*:device/${DeviceType}/${Provider}/${DeviceId} |   | 
|  [job](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources)  | arn:${Partition}:braket:${Region}:${Account}:job/${RandomId} | [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_) | 
|  [quantum-task](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources)  | arn:${Partition}:braket:${Region}:${Account}:quantum-task/${RandomId} | [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_) | 
|  [spending-limit](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html#resources)  | arn:${Partition}:braket:${Region}:${Account}:spending-limit/${RandomId} | [aws:ResourceTag/${TagKey}](#list_braket-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Braket
<a name="list_braket-policy-keys"></a>

Amazon Braket defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 