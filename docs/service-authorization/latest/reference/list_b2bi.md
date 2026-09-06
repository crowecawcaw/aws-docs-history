

# Actions, resources, and condition keys for AWS B2B Data Interchange
<a name="list_b2bi"></a>

AWS B2B Data Interchange (service prefix: `b2bi`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/b2bi/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/b2bi/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/b2bi/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/b2bi/b2bi.json) for this service.

**Topics**
+ [API operations defined by AWS B2B Data Interchange](#list_b2bi-operations)
+ [Actions defined by AWS B2B Data Interchange](#list_b2bi-actions-as-permissions)
+ [Resource types defined by AWS B2B Data Interchange](#list_b2bi-resources-for-iam-policies)
+ [Condition keys for AWS B2B Data Interchange](#list_b2bi-policy-keys)

## API operations defined by AWS B2B Data Interchange
<a name="list_b2bi-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_b2bi-actions-as-permissions).




- **   CreateCapability  **
  - **IAM action:**  [b2bi:CreateCapability](#list_b2bi-action-CreateCapability)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [b2bi:TagResource](#list_b2bi-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePartnership  **
  - **IAM action:**  [b2bi:CreatePartnership](#list_b2bi-action-CreatePartnership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [b2bi:TagResource](#list_b2bi-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProfile  **
  - **IAM action:**  [b2bi:CreateProfile](#list_b2bi-action-CreateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [b2bi:TagResource](#list_b2bi-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStarterMappingTemplate  **
  - **IAM action:**  [b2bi:CreateStarterMappingTemplate](#list_b2bi-action-CreateStarterMappingTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTransformer  **
  - **IAM action:**  [b2bi:CreateTransformer](#list_b2bi-action-CreateTransformer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [b2bi:TagResource](#list_b2bi-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteCapability  **
  - **IAM action:**  [b2bi:DeleteCapability](#list_b2bi-action-DeleteCapability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePartnership  **
  - **IAM action:**  [b2bi:DeletePartnership](#list_b2bi-action-DeletePartnership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfile  **
  - **IAM action:**  [b2bi:DeleteProfile](#list_b2bi-action-DeleteProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTransformer  **
  - **IAM action:**  [b2bi:DeleteTransformer](#list_b2bi-action-DeleteTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GenerateMapping  **
  - **IAM action:**  [b2bi:GenerateMapping](#list_b2bi-action-GenerateMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCapability  **
  - **IAM action:**  [b2bi:GetCapability](#list_b2bi-action-GetCapability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPartnership  **
  - **IAM action:**  [b2bi:GetPartnership](#list_b2bi-action-GetPartnership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfile  **
  - **IAM action:**  [b2bi:GetProfile](#list_b2bi-action-GetProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTransformer  **
  - **IAM action:**  [b2bi:GetTransformer](#list_b2bi-action-GetTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTransformerJob  **
  - **IAM action:**  [b2bi:GetTransformerJob](#list_b2bi-action-GetTransformerJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCapabilities  **
  - **IAM action:**  [b2bi:ListCapabilities](#list_b2bi-action-ListCapabilities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPartnerships  **
  - **IAM action:**  [b2bi:ListPartnerships](#list_b2bi-action-ListPartnerships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfiles  **
  - **IAM action:**  [b2bi:ListProfiles](#list_b2bi-action-ListProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [b2bi:ListTagsForResource](#list_b2bi-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTransformers  **
  - **IAM action:**  [b2bi:ListTransformers](#list_b2bi-action-ListTransformers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartTransformerJob  **
  - **IAM action:**  [b2bi:StartTransformerJob](#list_b2bi-action-StartTransformerJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [b2bi:TagResource](#list_b2bi-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestConversion  **
  - **IAM action:**  [b2bi:TestConversion](#list_b2bi-action-TestConversion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestMapping  **
  - **IAM action:**  [b2bi:TestMapping](#list_b2bi-action-TestMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TestParsing  **
  - **IAM action:**  [b2bi:TestParsing](#list_b2bi-action-TestParsing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [b2bi:UntagResource](#list_b2bi-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCapability  **
  - **IAM action:**  [b2bi:UpdateCapability](#list_b2bi-action-UpdateCapability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePartnership  **
  - **IAM action:**  [b2bi:UpdatePartnership](#list_b2bi-action-UpdatePartnership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfile  **
  - **IAM action:**  [b2bi:UpdateProfile](#list_b2bi-action-UpdateProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTransformer  **
  - **IAM action:**  [b2bi:UpdateTransformer](#list_b2bi-action-UpdateTransformer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS B2B Data Interchange
<a name="list_b2bi-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateCapability.html)  **
  - **Description:** Grants permission to create a capability
  - **Resource types (\*required):** [transformer](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreatePartnership.html)  **
  - **Description:** Grants permission to create a partnership
  - **Resource types (\*required):** [capability\*](#list_b2bi-resource-capability) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [profile\*](#list_b2bi-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateProfile.html)  **
  - **Description:** Grants permission to create a profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStarterMappingTemplate](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateStarterMappingTemplate.html)  **
  - **Description:** Grants permission to generate a starter JSONATA/XSLT template
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_CreateTransformer.html)  **
  - **Description:** Grants permission to create a transformer
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeleteCapability.html)  **
  - **Description:** Grants permission to delete a capability
  - **Resource types (\*required):** [capability\*](#list_b2bi-resource-capability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeletePartnership.html)  **
  - **Description:** Grants permission to delete an partnership
  - **Resource types (\*required):** [partnership\*](#list_b2bi-resource-partnership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeleteProfile.html)  **
  - **Description:** Grants permission to delete a profile
  - **Resource types (\*required):** [profile\*](#list_b2bi-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeleteTransformer.html)  **
  - **Description:** Grants permission to delete a transformer
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateMapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GenerateMapping.html)  **
  - **Description:** Grants permission to generate a starter JSONATA/XSLT mapping template from Amazon Bedrock
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetCapability.html)  **
  - **Description:** Grants permission to get a capability
  - **Resource types (\*required):** [capability\*](#list_b2bi-resource-capability)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetPartnership.html)  **
  - **Description:** Grants permission to get a partnership
  - **Resource types (\*required):** [partnership\*](#list_b2bi-resource-partnership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetProfile.html)  **
  - **Description:** Grants permission to get a profile
  - **Resource types (\*required):** [profile\*](#list_b2bi-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformer.html)  **
  - **Description:** Grants permission to get a transformer
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTransformerJob](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_GetTransformerJob.html)  **
  - **Description:** Grants permission to get a transformer job
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCapabilities](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListCapabilities.html)  **
  - **Description:** Grants permission to list all capabilities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPartnerships](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListPartnerships.html)  **
  - **Description:** Grants permission to list all partnerships
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfiles](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListProfiles.html)  **
  - **Description:** Grants permission to list all profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a B2Bi resource
  - **Resource types (\*required):** [capability](#list_b2bi-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [partnership](#list_b2bi-resource-partnership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [profile](#list_b2bi-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [transformer](#list_b2bi-resource-transformer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTransformers](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_ListTransformers.html)  **
  - **Description:** Grants permission to list all transformers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartTransformerJob](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_StartTransformerJob.html)  **
  - **Description:** Grants permission to transformer a document
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a B2Bi resource
  - **Resource types (\*required):** [capability](#list_b2bi-resource-capability) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [partnership](#list_b2bi-resource-partnership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_b2bi-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [transformer](#list_b2bi-resource-transformer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_b2bi-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestConversion](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestConversion.html)  **
  - **Description:** Grants permission to convert a JSON/XML to an edi document
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TestMapping](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestMapping.html)  **
  - **Description:** Grants permission to map a sample file
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TestParsing](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_TestParsing.html)  **
  - **Description:** Grants permission to parse an edi document
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a B2Bi resource
  - **Resource types (\*required):** [capability](#list_b2bi-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [partnership](#list_b2bi-resource-partnership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_b2bi-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Resource types (\*required):** [transformer](#list_b2bi-resource-transformer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_b2bi-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCapability](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateCapability.html)  **
  - **Description:** Grants permission to update a capability
  - **Resource types (\*required):** [capability\*](#list_b2bi-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [transformer](#list_b2bi-resource-transformer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePartnership](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdatePartnership.html)  **
  - **Description:** Grants permission to update a partnership
  - **Resource types (\*required):** [capability](#list_b2bi-resource-capability) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [partnership\*](#list_b2bi-resource-partnership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateProfile.html)  **
  - **Description:** Grants permission to update a profile
  - **Resource types (\*required):** [profile\*](#list_b2bi-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTransformer](https://docs.aws.amazon.com/b2bi/latest/APIReference/API_UpdateTransformer.html)  **
  - **Description:** Grants permission to update a transformer
  - **Resource types (\*required):** [transformer\*](#list_b2bi-resource-transformer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS B2B Data Interchange
<a name="list_b2bi-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [capability](https://docs.aws.amazon.com/b2bi/latest/userguide/)  | arn:${Partition}:b2bi:${Region}:${Account}:capability/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_) | 
|  [partnership](https://docs.aws.amazon.com/b2bi/latest/userguide/)  | arn:${Partition}:b2bi:${Region}:${Account}:partnership/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/b2bi/latest/userguide/)  | arn:${Partition}:b2bi:${Region}:${Account}:profile/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_) | 
|  [transformer](https://docs.aws.amazon.com/b2bi/latest/userguide/)  | arn:${Partition}:b2bi:${Region}:${Account}:transformer/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_b2bi-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS B2B Data Interchange
<a name="list_b2bi-policy-keys"></a>

AWS B2B Data Interchange defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 