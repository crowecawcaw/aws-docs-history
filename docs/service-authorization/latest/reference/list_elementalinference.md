

# Actions, resources, and condition keys for AWS Elemental Inference
<a name="list_elementalinference"></a>

AWS Elemental Inference (service prefix: `elemental-inference`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/elemental-inference/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/elemental-inference/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/elemental-inference/elemental-inference.json) for this service.

**Topics**
+ [API operations defined by AWS Elemental Inference](#list_elementalinference-operations)
+ [Actions defined by AWS Elemental Inference](#list_elementalinference-actions-as-permissions)
+ [Resource types defined by AWS Elemental Inference](#list_elementalinference-resources-for-iam-policies)
+ [Condition keys for AWS Elemental Inference](#list_elementalinference-policy-keys)

## API operations defined by AWS Elemental Inference
<a name="list_elementalinference-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_elementalinference-actions-as-permissions).




- **   AssociateFeed  **
  - **IAM action:**  [elemental-inference:AssociateFeed](#list_elementalinference-action-AssociateFeed) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDictionary  **
  - **IAM action:**  [elemental-inference:CreateDictionary](#list_elementalinference-action-CreateDictionary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elemental-inference:TagResource](#list_elementalinference-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFeed  **
  - **IAM action:**  [elemental-inference:CreateFeed](#list_elementalinference-action-CreateFeed)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [elemental-inference:TagResource](#list_elementalinference-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** elemental-inference.amazonaws.com / **Access level:** Write

- **   DeleteDictionary  **
  - **IAM action:**  [elemental-inference:DeleteDictionary](#list_elementalinference-action-DeleteDictionary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFeed  **
  - **IAM action:**  [elemental-inference:DeleteFeed](#list_elementalinference-action-DeleteFeed) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFeed  **
  - **IAM action:**  [elemental-inference:DisassociateFeed](#list_elementalinference-action-DisassociateFeed) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExportDictionaryEntries  **
  - **IAM action:**  [elemental-inference:ExportDictionaryEntries](#list_elementalinference-action-ExportDictionaryEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDictionary  **
  - **IAM action:**  [elemental-inference:GetDictionary](#list_elementalinference-action-GetDictionary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFeed  **
  - **IAM action:**  [elemental-inference:GetFeed](#list_elementalinference-action-GetFeed) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDictionaries  **
  - **IAM action:**  [elemental-inference:ListDictionaries](#list_elementalinference-action-ListDictionaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFeeds  **
  - **IAM action:**  [elemental-inference:ListFeeds](#list_elementalinference-action-ListFeeds) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [elemental-inference:ListTagsForResource](#list_elementalinference-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [elemental-inference:TagResource](#list_elementalinference-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [elemental-inference:UntagResource](#list_elementalinference-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDictionary  **
  - **IAM action:**  [elemental-inference:UpdateDictionary](#list_elementalinference-action-UpdateDictionary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFeed  **
  - **IAM action:**  [elemental-inference:UpdateFeed](#list_elementalinference-action-UpdateFeed)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** elemental-inference.amazonaws.com / **Access level:** Write



## Actions defined by AWS Elemental Inference
<a name="list_elementalinference-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_AssociateFeed.html)  **
  - **Description:** Grants permission to associate a feed with an AWS resource
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDictionary](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateDictionary.html)  **
  - **Description:** Grants permission to create a new dictionary
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elementalinference-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_elementalinference-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_CreateFeed.html)  **
  - **Description:** Grants permission to create a new feed
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_elementalinference-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_elementalinference-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDictionary](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DeleteDictionary.html)  **
  - **Description:** Grants permission to delete a dictionary
  - **Resource types (\*required):** [dictionary\*](#list_elementalinference-resource-dictionary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DeleteFeed.html)  **
  - **Description:** Grants permission to delete a feed
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_DisassociateFeed.html)  **
  - **Description:** Grants permission to disassociate a feed from an AWS resource
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ExportDictionaryEntries](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ExportDictionaryEntries.html)  **
  - **Description:** Grants permission to export dictionary entries
  - **Resource types (\*required):** [dictionary\*](#list_elementalinference-resource-dictionary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDictionary](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetDictionary.html)  **
  - **Description:** Grants permission to get dictionary details
  - **Resource types (\*required):** [dictionary\*](#list_elementalinference-resource-dictionary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetFeed.html)  **
  - **Description:** Grants permission to get feed details
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMetadata](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_GetMetadata.html)  **
  - **Description:** Grants permission to retrieve metadata for a specific feed output
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDictionaries](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListDictionaries.html)  **
  - **Description:** Grants permission to list dictionaries in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFeeds](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListFeeds.html)  **
  - **Description:** Grants permission to list feeds in the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags on a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutMedia](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_PutMedia.html)  **
  - **Description:** Grants permission to upload media data for a specified feed
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a resource
  - **Resource types (\*required):** [dictionary](#list_elementalinference-resource-dictionary) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elementalinference-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elementalinference-aws_TagKeys)
  - **Resource types (\*required):** [feed](#list_elementalinference-resource-feed) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_elementalinference-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elementalinference-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a resource
  - **Resource types (\*required):** [dictionary](#list_elementalinference-resource-dictionary) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elementalinference-aws_TagKeys)
  - **Resource types (\*required):** [feed](#list_elementalinference-resource-feed) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_elementalinference-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDictionary](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateDictionary.html)  **
  - **Description:** Grants permission to update dictionary configuration
  - **Resource types (\*required):** [dictionary\*](#list_elementalinference-resource-dictionary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFeed](https://docs.aws.amazon.com/elemental-inference/latest/APIReference/API_UpdateFeed.html)  **
  - **Description:** Grants permission to update feed configuration
  - **Resource types (\*required):** [feed\*](#list_elementalinference-resource-feed)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Elemental Inference
<a name="list_elementalinference-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [dictionary](https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-configuration.html)  | arn:${Partition}:elemental-inference:${Region}:${Account}:dictionary/${Id} | [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_) | 
|  [feed](https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-configuration.html)  | arn:${Partition}:elemental-inference:${Region}:${Account}:feed/${Id} | [aws:ResourceTag/${TagKey}](#list_elementalinference-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Elemental Inference
<a name="list_elementalinference-policy-keys"></a>

AWS Elemental Inference defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 