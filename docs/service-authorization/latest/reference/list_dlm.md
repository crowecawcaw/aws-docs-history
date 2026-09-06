

# Actions, resources, and condition keys for Amazon Data Lifecycle Manager
<a name="list_dlm"></a>

Amazon Data Lifecycle Manager (service prefix: `dlm`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/dlm/latest/APIReference/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/dlm/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazondatalifecyclemanager.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/dlm/dlm.json) for this service.

**Topics**
+ [API operations defined by Amazon Data Lifecycle Manager](#list_dlm-operations)
+ [Actions defined by Amazon Data Lifecycle Manager](#list_dlm-actions-as-permissions)
+ [Resource types defined by Amazon Data Lifecycle Manager](#list_dlm-resources-for-iam-policies)
+ [Condition keys for Amazon Data Lifecycle Manager](#list_dlm-policy-keys)

## API operations defined by Amazon Data Lifecycle Manager
<a name="list_dlm-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_dlm-actions-as-permissions).




- **   CreateLifecyclePolicy  **
  - **IAM action:**  [dlm:CreateLifecyclePolicy](#list_dlm-action-CreateLifecyclePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [dlm:TagResource](#list_dlm-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dlm.amazonaws.com / **Access level:** Write

- **   DeleteLifecyclePolicy  **
  - **IAM action:**  [dlm:DeleteLifecyclePolicy](#list_dlm-action-DeleteLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLifecyclePolicies  **
  - **IAM action:**  [dlm:GetLifecyclePolicies](#list_dlm-action-GetLifecyclePolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetLifecyclePolicy  **
  - **IAM action:**  [dlm:GetLifecyclePolicy](#list_dlm-action-GetLifecyclePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [dlm:ListTagsForResource](#list_dlm-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [dlm:TagResource](#list_dlm-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [dlm:UntagResource](#list_dlm-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateLifecyclePolicy  **
  - **IAM action:**  [dlm:UpdateLifecyclePolicy](#list_dlm-action-UpdateLifecyclePolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** dlm.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Data Lifecycle Manager
<a name="list_dlm-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_CreateLifecyclePolicy.html)  **
  - **Description:** Grants permission to create a data lifecycle policy to manage the scheduled creation and retention of Amazon EBS snapshots. You may have up to 100 policies
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dlm-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_dlm-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_DeleteLifecyclePolicy.html)  **
  - **Description:** Grants permission to delete an existing data lifecycle policy. In addition, this action halts the creation and deletion of snapshots that the policy specified. Existing snapshots are not affected
  - **Resource types (\*required):** [policy\*](#list_dlm-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetLifecyclePolicies](https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicies.html)  **
  - **Description:** Grants permission to returns a list of summary descriptions of data lifecycle policies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_GetLifecyclePolicy.html)  **
  - **Description:** Grants permission to return a complete description of a single data lifecycle policy
  - **Resource types (\*required):** [policy\*](#list_dlm-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags associated with a resource
  - **Resource types (\*required):** [policy\*](#list_dlm-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update tags of a resource
  - **Resource types (\*required):** [policy\*](#list_dlm-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_dlm-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dlm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/dlm/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags associated with a resource
  - **Resource types (\*required):** [policy\*](#list_dlm-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_dlm-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateLifecyclePolicy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_UpdateLifecyclePolicy.html)  **
  - **Description:** Grants permission to update an existing data lifecycle policy
  - **Resource types (\*required):** [policy\*](#list_dlm-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Data Lifecycle Manager
<a name="list_dlm-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [policy](https://docs.aws.amazon.com/dlm/latest/APIReference/API_LifecyclePolicy.html)  | arn:${Partition}:dlm:${Region}:${Account}:policy/${ResourceName} | [aws:ResourceTag/${TagKey}](#list_dlm-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Data Lifecycle Manager
<a name="list_dlm-policy-keys"></a>

Amazon Data Lifecycle Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 