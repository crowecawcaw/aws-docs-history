

# Actions, resources, and condition keys for AWS Recycle Bin
<a name="list_rbin"></a>

AWS Recycle Bin (service prefix: `rbin`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/recyclebin/latest/APIReference/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-perms.html#rule-perms) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rbin/rbin.json) for this service.

**Topics**
+ [API operations defined by AWS Recycle Bin](#list_rbin-operations)
+ [Actions defined by AWS Recycle Bin](#list_rbin-actions-as-permissions)
+ [Resource types defined by AWS Recycle Bin](#list_rbin-resources-for-iam-policies)
+ [Condition keys for AWS Recycle Bin](#list_rbin-policy-keys)

## API operations defined by AWS Recycle Bin
<a name="list_rbin-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rbin-actions-as-permissions).




- **   CreateRule  **
  - **IAM action:**  [rbin:CreateRule](#list_rbin-action-CreateRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rbin:LockRule](#list_rbin-action-LockRule)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rbin:TagResource](#list_rbin-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteRule  **
  - **IAM action:**  [rbin:DeleteRule](#list_rbin-action-DeleteRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetRule  **
  - **IAM action:**  [rbin:GetRule](#list_rbin-action-GetRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRules  **
  - **IAM action:**  [rbin:ListRules](#list_rbin-action-ListRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [rbin:ListTagsForResource](#list_rbin-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   LockRule  **
  - **IAM action:**  [rbin:LockRule](#list_rbin-action-LockRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [rbin:TagResource](#list_rbin-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UnlockRule  **
  - **IAM action:**  [rbin:UnlockRule](#list_rbin-action-UnlockRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [rbin:UntagResource](#list_rbin-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateRule  **
  - **IAM action:**  [rbin:UpdateRule](#list_rbin-action-UpdateRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Recycle Bin
<a name="list_rbin-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_CreateRule.html)  **
  - **Description:** Grants permission to create a Recycle Bin retention rule
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rbin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rbin-aws_TagKeys)<br />[rbin:Request/ResourceType](#list_rbin-rbin_Request_ResourceType)
  - **Access level:** Write

- **   [DeleteRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_DeleteRule.html)  **
  - **Description:** Grants permission to delete a Recycle Bin retention rule
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Write

- **   [GetRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_GetRule.html)  **
  - **Description:** Grants permission to get detailed information about a Recycle Bin retention rule
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Read

- **   [ListRules](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListRules.html)  **
  - **Description:** Grants permission to list the Recycle Bin retention rules in the Region
  - **Resource types (\*required):** 
  - **Condition keys:** [rbin:Request/ResourceType](#list_rbin-rbin_Request_ResourceType)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags associated with a resource
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Read

- **   [LockRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_LockRule.html)  **
  - **Description:** Grants permission to lock an existing Recycle Bin retention rule
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update tags of a resource
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rbin-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rbin-aws_TagKeys)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Tagging, Write

- **   [UnlockRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UnlockRule.html)  **
  - **Description:** Grants permission to unlock an existing Recycle Bin retention rule
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags associated with a resource
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rbin-aws_TagKeys)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Tagging, Write

- **   [UpdateRule](https://docs.aws.amazon.com/recyclebin/latest/APIReference/API_UpdateRule.html)  **
  - **Description:** Grants permission to update an existing Recycle Bin retention rule
  - **Resource types (\*required):** [rule\*](#list_rbin-resource-rule)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_)<br />[rbin:Attribute/ResourceType](#list_rbin-rbin_Attribute_ResourceType)
  - **Access level:** Write



## Resource types defined by AWS Recycle Bin
<a name="list_rbin-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [rule](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-recycle-bin.html#recycle-bin-concepts)  | arn:${Partition}:rbin:${Region}:${Account}:rule/${ResourceName} | [aws:ResourceTag/${TagKey}](#list_rbin-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Recycle Bin
<a name="list_rbin-policy-keys"></a>

AWS Recycle Bin defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 
|   [rbin:Attribute/ResourceType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-perms.html#rbin-condition-keys)  | Filters access by the resource type of the existing rule | String | 
|   [rbin:Request/ResourceType](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/recycle-bin-perms.html#rbin-condition-keys)  | Filters access by the resource type in a request | String | 