

# Actions, resources, and condition keys for Amazon EventBridge Pipes
<a name="list_pipes"></a>

Amazon EventBridge Pipes (service prefix: `pipes`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pipes/pipes.json) for this service.

**Topics**
+ [API operations defined by Amazon EventBridge Pipes](#list_pipes-operations)
+ [Actions defined by Amazon EventBridge Pipes](#list_pipes-actions-as-permissions)
+ [Resource types defined by Amazon EventBridge Pipes](#list_pipes-resources-for-iam-policies)
+ [Condition keys for Amazon EventBridge Pipes](#list_pipes-policy-keys)

## API operations defined by Amazon EventBridge Pipes
<a name="list_pipes-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pipes-actions-as-permissions).




- **   CreatePipe  **
  - **IAM action:**  [pipes:CreatePipe](#list_pipes-action-CreatePipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pipes:TagResource](#list_pipes-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** pipes.amazonaws.com / **Access level:** Write

- **   DeletePipe  **
  - **IAM action:**  [pipes:DeletePipe](#list_pipes-action-DeletePipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribePipe  **
  - **IAM action:**  [pipes:DescribePipe](#list_pipes-action-DescribePipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPipes  **
  - **IAM action:**  [pipes:ListPipes](#list_pipes-action-ListPipes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [pipes:ListTagsForResource](#list_pipes-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartPipe  **
  - **IAM action:**  [pipes:StartPipe](#list_pipes-action-StartPipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPipe  **
  - **IAM action:**  [pipes:StopPipe](#list_pipes-action-StopPipe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [pipes:TagResource](#list_pipes-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [pipes:UntagResource](#list_pipes-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdatePipe  **
  - **IAM action:**  [pipes:UpdatePipe](#list_pipes-action-UpdatePipe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** pipes.amazonaws.com / **Access level:** Write



## Actions defined by Amazon EventBridge Pipes
<a name="list_pipes-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreatePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_CreatePipe.html)  **
  - **Description:** Grants permission to create a pipe
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pipes-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pipes-aws_TagKeys)
  - **Access level:** Write

- **   [DeletePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_DeletePipe.html)  **
  - **Description:** Grants permission to delete a pipe
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_DescribePipe.html)  **
  - **Description:** Grants permission to describe a pipe
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListPipes](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_ListPipes.html)  **
  - **Description:** Grants permission to list all pipes in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a resource
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartPipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_StartPipe.html)  **
  - **Description:** Grants permission to start a pipe
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopPipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_StopPipe.html)  **
  - **Description:** Grants permission to stop a pipe
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pipes-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pipes-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pipes-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePipe](https://docs.aws.amazon.com/eventbridge/latest/pipes-reference/API_UpdatePipe.html)  **
  - **Description:** Grants permission to update a pipe
  - **Resource types (\*required):** [pipe\*](#list_pipes-resource-pipe)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon EventBridge Pipes
<a name="list_pipes-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [pipe](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html)  | arn:${Partition}:pipes:${Region}:${Account}:pipe/${Name} | [aws:ResourceTag/${TagKey}](#list_pipes-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon EventBridge Pipes
<a name="list_pipes-policy-keys"></a>

Amazon EventBridge Pipes defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 