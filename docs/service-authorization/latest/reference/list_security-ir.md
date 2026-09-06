

# Actions, resources, and condition keys for AWS Security Incident Response
<a name="list_security-ir"></a>

AWS Security Incident Response (service prefix: `security-ir`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/security-ir/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/security-ir/latest/userguide/identity-and-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/security-ir/security-ir.json) for this service.

**Topics**
+ [API operations defined by AWS Security Incident Response](#list_security-ir-operations)
+ [Actions defined by AWS Security Incident Response](#list_security-ir-actions-as-permissions)
+ [Resource types defined by AWS Security Incident Response](#list_security-ir-resources-for-iam-policies)
+ [Condition keys for AWS Security Incident Response](#list_security-ir-policy-keys)

## API operations defined by AWS Security Incident Response
<a name="list_security-ir-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_security-ir-actions-as-permissions).




- **   BatchGetMemberAccountDetails  **
  - **IAM action:**  [security-ir:BatchGetMemberAccountDetails](#list_security-ir-action-BatchGetMemberAccountDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CancelMembership  **
  - **IAM action:**  [security-ir:CancelMembership](#list_security-ir-action-CancelMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CloseCase  **
  - **IAM action:**  [security-ir:CloseCase](#list_security-ir-action-CloseCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCase  **
  - **IAM action:**  [security-ir:CreateCase](#list_security-ir-action-CreateCase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [security-ir:TagResource](#list_security-ir-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCaseComment  **
  - **IAM action:**  [security-ir:CreateCaseComment](#list_security-ir-action-CreateCaseComment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMembership  **
  - **IAM action:**  [security-ir:CreateMembership](#list_security-ir-action-CreateMembership)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [security-ir:TagResource](#list_security-ir-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   GetCase  **
  - **IAM action:**  [security-ir:GetCase](#list_security-ir-action-GetCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCaseAttachmentDownloadUrl  **
  - **IAM action:**  [security-ir:GetCaseAttachmentDownloadUrl](#list_security-ir-action-GetCaseAttachmentDownloadUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCaseAttachmentUploadUrl  **
  - **IAM action:**  [security-ir:GetCaseAttachmentUploadUrl](#list_security-ir-action-GetCaseAttachmentUploadUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetMembership  **
  - **IAM action:**  [security-ir:GetMembership](#list_security-ir-action-GetMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCaseEdits  **
  - **IAM action:**  [security-ir:ListCaseEdits](#list_security-ir-action-ListCaseEdits) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCases  **
  - **IAM action:**  [security-ir:ListCases](#list_security-ir-action-ListCases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComments  **
  - **IAM action:**  [security-ir:ListComments](#list_security-ir-action-ListComments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListInvestigations  **
  - **IAM action:**  [security-ir:ListInvestigations](#list_security-ir-action-ListInvestigations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMemberships  **
  - **IAM action:**  [security-ir:ListMemberships](#list_security-ir-action-ListMemberships) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [security-ir:ListTagsForResource](#list_security-ir-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendFeedback  **
  - **IAM action:**  [security-ir:SendFeedback](#list_security-ir-action-SendFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [security-ir:TagResource](#list_security-ir-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [security-ir:UntagResource](#list_security-ir-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCase  **
  - **IAM action:**  [security-ir:UpdateCase](#list_security-ir-action-UpdateCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCaseComment  **
  - **IAM action:**  [security-ir:UpdateCaseComment](#list_security-ir-action-UpdateCaseComment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCaseStatus  **
  - **IAM action:**  [security-ir:UpdateCaseStatus](#list_security-ir-action-UpdateCaseStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMembership  **
  - **IAM action:**  [security-ir:UpdateMembership](#list_security-ir-action-UpdateMembership) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResolverType  **
  - **IAM action:**  [security-ir:UpdateResolverType](#list_security-ir-action-UpdateResolverType) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Security Incident Response
<a name="list_security-ir-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetMemberAccountDetails](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_BatchGetMemberAccountDetails.html)  **
  - **Description:** Grants permission to get member account details in batch
  - **Resource types (\*required):** [membership\*](#list_security-ir-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CancelMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CancelMembership.html)  **
  - **Description:** Grants permission to cancel a membership
  - **Resource types (\*required):** [membership\*](#list_security-ir-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CloseCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CloseCase.html)  **
  - **Description:** Grants permission to close a case
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateCase.html)  **
  - **Description:** Grants permission to create a case
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_security-ir-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCaseComment](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateCaseComment.html)  **
  - **Description:** Grants permission to create a case comment
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_CreateMembership.html)  **
  - **Description:** Grants permission to create a membership
  - **Resource types (\*required):** [membership\*](#list_security-ir-resource-membership)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_security-ir-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Access level:** Write

- **   [GetCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCase.html)  **
  - **Description:** Grants permission to get a case
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCaseAttachmentDownloadUrl](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCaseAttachmentDownloadUrl.html)  **
  - **Description:** Grants permission to get a case attachment download URL
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCaseAttachmentUploadUrl](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetCaseAttachmentUploadUrl.html)  **
  - **Description:** Grants permission to get a case attachment upload URL
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetMembership.html)  **
  - **Description:** Grants permission to get a membership
  - **Resource types (\*required):** [membership\*](#list_security-ir-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCaseEdits](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCaseEdits.html)  **
  - **Description:** Grants permission to list case edits
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCases](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCases.html)  **
  - **Description:** Grants permission to list cases
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComments](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListComments.html)  **
  - **Description:** Grants permission to list case comments
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListInvestigations](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListInvestigations.html)  **
  - **Description:** Grants permission to list investigations for a case
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMemberships](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListMemberships.html)  **
  - **Description:** Grants permission to list memberships
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags attached to the specified resource
  - **Resource types (\*required):** [case](#list_security-ir-resource-case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Resource types (\*required):** [membership](#list_security-ir-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Access level:** Read

- **   [SendFeedback](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_SendFeedback.html)  **
  - **Description:** Grants permission to send feedback for investigation results
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the specified resource
  - **Resource types (\*required):** [case](#list_security-ir-resource-case) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_security-ir-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Resource types (\*required):** [membership](#list_security-ir-resource-membership) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_security-ir-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified resource
  - **Resource types (\*required):** [case](#list_security-ir-resource-case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Resource types (\*required):** [membership](#list_security-ir-resource-membership) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_security-ir-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCase](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCase.html)  **
  - **Description:** Grants permission to update a case
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCaseComment](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCaseComment.html)  **
  - **Description:** Grants permission to update a case comment
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCaseStatus](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateCaseStatus.html)  **
  - **Description:** Grants permission to update a case status
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMembership](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateMembership.html)  **
  - **Description:** Grants permission to update memberships
  - **Resource types (\*required):** [membership\*](#list_security-ir-resource-membership)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateResolverType](https://docs.aws.amazon.com/security-ir/latest/APIReference/API_UpdateResolverType.html)  **
  - **Description:** Grants permission to update case resolver type
  - **Resource types (\*required):** [case\*](#list_security-ir-resource-case)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Security Incident Response
<a name="list_security-ir-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [case](https://docs.aws.amazon.com/security-ir/latest/userguide/cases.html)  | arn:${Partition}:security-ir:${Region}:${Account}:case/${CaseId} | [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_) | 
|  [membership](https://docs.aws.amazon.com/security-ir/latest/userguide/select-a-membership-account.html)  | arn:${Partition}:security-ir:${Region}:${Account}:membership/${MembershipId} | [aws:ResourceTag/${TagKey}](#list_security-ir-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Security Incident Response
<a name="list_security-ir-policy-keys"></a>

AWS Security Incident Response defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 