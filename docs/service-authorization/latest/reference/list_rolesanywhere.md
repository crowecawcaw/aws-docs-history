

# Actions, resources, and condition keys for AWS Identity and Access Management Roles Anywhere
<a name="list_rolesanywhere"></a>

AWS Identity and Access Management Roles Anywhere (service prefix: `rolesanywhere`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rolesanywhere/rolesanywhere.json) for this service.

**Topics**
+ [API operations defined by AWS Identity and Access Management Roles Anywhere](#list_rolesanywhere-operations)
+ [Actions defined by AWS Identity and Access Management Roles Anywhere](#list_rolesanywhere-actions-as-permissions)
+ [Resource types defined by AWS Identity and Access Management Roles Anywhere](#list_rolesanywhere-resources-for-iam-policies)
+ [Condition keys for AWS Identity and Access Management Roles Anywhere](#list_rolesanywhere-policy-keys)

## API operations defined by AWS Identity and Access Management Roles Anywhere
<a name="list_rolesanywhere-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rolesanywhere-actions-as-permissions).




- **   CreateProfile  **
  - **IAM action:**  [rolesanywhere:CreateProfile](#list_rolesanywhere-action-CreateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rolesanywhere:TagResource](#list_rolesanywhere-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rolesanywhere.amazonaws.com / **Access level:** Write

- **   CreateTrustAnchor  **
  - **IAM action:**  [rolesanywhere:CreateTrustAnchor](#list_rolesanywhere-action-CreateTrustAnchor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rolesanywhere:TagResource](#list_rolesanywhere-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAttributeMapping  **
  - **IAM action:**  [rolesanywhere:DeleteAttributeMapping](#list_rolesanywhere-action-DeleteAttributeMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCrl  **
  - **IAM action:**  [rolesanywhere:DeleteCrl](#list_rolesanywhere-action-DeleteCrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProfile  **
  - **IAM action:**  [rolesanywhere:DeleteProfile](#list_rolesanywhere-action-DeleteProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrustAnchor  **
  - **IAM action:**  [rolesanywhere:DeleteTrustAnchor](#list_rolesanywhere-action-DeleteTrustAnchor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableCrl  **
  - **IAM action:**  [rolesanywhere:DisableCrl](#list_rolesanywhere-action-DisableCrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableProfile  **
  - **IAM action:**  [rolesanywhere:DisableProfile](#list_rolesanywhere-action-DisableProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableTrustAnchor  **
  - **IAM action:**  [rolesanywhere:DisableTrustAnchor](#list_rolesanywhere-action-DisableTrustAnchor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableCrl  **
  - **IAM action:**  [rolesanywhere:EnableCrl](#list_rolesanywhere-action-EnableCrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableProfile  **
  - **IAM action:**  [rolesanywhere:EnableProfile](#list_rolesanywhere-action-EnableProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rolesanywhere.amazonaws.com / **Access level:** Write

- **   EnableTrustAnchor  **
  - **IAM action:**  [rolesanywhere:EnableTrustAnchor](#list_rolesanywhere-action-EnableTrustAnchor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCrl  **
  - **IAM action:**  [rolesanywhere:GetCrl](#list_rolesanywhere-action-GetCrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProfile  **
  - **IAM action:**  [rolesanywhere:GetProfile](#list_rolesanywhere-action-GetProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubject  **
  - **IAM action:**  [rolesanywhere:GetSubject](#list_rolesanywhere-action-GetSubject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrustAnchor  **
  - **IAM action:**  [rolesanywhere:GetTrustAnchor](#list_rolesanywhere-action-GetTrustAnchor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportCrl  **
  - **IAM action:**  [rolesanywhere:ImportCrl](#list_rolesanywhere-action-ImportCrl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rolesanywhere:TagResource](#list_rolesanywhere-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListCrls  **
  - **IAM action:**  [rolesanywhere:ListCrls](#list_rolesanywhere-action-ListCrls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProfiles  **
  - **IAM action:**  [rolesanywhere:ListProfiles](#list_rolesanywhere-action-ListProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubjects  **
  - **IAM action:**  [rolesanywhere:ListSubjects](#list_rolesanywhere-action-ListSubjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [rolesanywhere:ListTagsForResource](#list_rolesanywhere-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrustAnchors  **
  - **IAM action:**  [rolesanywhere:ListTrustAnchors](#list_rolesanywhere-action-ListTrustAnchors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAttributeMapping  **
  - **IAM action:**  [rolesanywhere:PutAttributeMapping](#list_rolesanywhere-action-PutAttributeMapping) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutNotificationSettings  **
  - **IAM action:**  [rolesanywhere:PutNotificationSettings](#list_rolesanywhere-action-PutNotificationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ResetNotificationSettings  **
  - **IAM action:**  [rolesanywhere:ResetNotificationSettings](#list_rolesanywhere-action-ResetNotificationSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [rolesanywhere:TagResource](#list_rolesanywhere-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [rolesanywhere:UntagResource](#list_rolesanywhere-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCrl  **
  - **IAM action:**  [rolesanywhere:UpdateCrl](#list_rolesanywhere-action-UpdateCrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProfile  **
  - **IAM action:**  [rolesanywhere:UpdateProfile](#list_rolesanywhere-action-UpdateProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rolesanywhere.amazonaws.com / **Access level:** Write

- **   UpdateTrustAnchor  **
  - **IAM action:**  [rolesanywhere:UpdateTrustAnchor](#list_rolesanywhere-action-UpdateTrustAnchor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Identity and Access Management Roles Anywhere
<a name="list_rolesanywhere-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateProfile.html)  **
  - **Description:** Grants permission to create a profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_CreateTrustAnchor.html)  **
  - **Description:** Grants permission to create a trust anchor
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteAttributeMapping.html)  **
  - **Description:** Grants permission to delete a mapping rule from a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteCrl.html)  **
  - **Description:** Grants permission to delete a certificate revocation list (crl)
  - **Resource types (\*required):** [crl\*](#list_rolesanywhere-resource-crl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteProfile.html)  **
  - **Description:** Grants permission to delete a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DeleteTrustAnchor.html)  **
  - **Description:** Grants permission to delete a trust anchor
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableCrl.html)  **
  - **Description:** Grants permission to disable a certificate revocation list (crl)
  - **Resource types (\*required):** [crl\*](#list_rolesanywhere-resource-crl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableProfile.html)  **
  - **Description:** Grants permission to disable a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_DisableTrustAnchor.html)  **
  - **Description:** Grants permission to disable a trust anchor
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableCrl.html)  **
  - **Description:** Grants permission to enable a certificate revocation list (crl)
  - **Resource types (\*required):** [crl\*](#list_rolesanywhere-resource-crl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableProfile.html)  **
  - **Description:** Grants permission to enable a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_EnableTrustAnchor.html)  **
  - **Description:** Grants permission to enable a trust anchor
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetCrl.html)  **
  - **Description:** Grants permission to get a certificate revocation list (crl)
  - **Resource types (\*required):** [crl\*](#list_rolesanywhere-resource-crl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetProfile.html)  **
  - **Description:** Grants permission to get a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSubject](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetSubject.html)  **
  - **Description:** Grants permission to get a subject
  - **Resource types (\*required):** [subject\*](#list_rolesanywhere-resource-subject)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_GetTrustAnchor.html)  **
  - **Description:** Grants permission to get a trust anchor
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ImportCrl.html)  **
  - **Description:** Grants permission to import a certificate revocation list (crl)
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Access level:** Write

- **   [ListCrls](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListCrls.html)  **
  - **Description:** Grants permission to list certificate revocation lists (crls)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProfiles](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListProfiles.html)  **
  - **Description:** Grants permission to list profiles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubjects](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListSubjects.html)  **
  - **Description:** Grants permission to list subjects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTrustAnchors](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ListTrustAnchors.html)  **
  - **Description:** Grants permission to list trust anchors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAttributeMapping](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_PutAttributeMapping.html)  **
  - **Description:** Grants permission to put a mapping rule into a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutNotificationSettings](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_PutNotificationSettings.html)  **
  - **Description:** Grants permission to attach notification settings to a trust anchor
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ResetNotificationSettings](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_ResetNotificationSettings.html)  **
  - **Description:** Grants permission to reset custom notification settings to IAM Roles Anywhere defined default state
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [crl](#list_rolesanywhere-resource-crl) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_rolesanywhere-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Resource types (\*required):** [subject](#list_rolesanywhere-resource-subject) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Resource types (\*required):** [trust-anchor](#list_rolesanywhere-resource-trust-anchor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rolesanywhere-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [crl](#list_rolesanywhere-resource-crl) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_rolesanywhere-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Resource types (\*required):** [subject](#list_rolesanywhere-resource-subject) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Resource types (\*required):** [trust-anchor](#list_rolesanywhere-resource-trust-anchor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rolesanywhere-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCrl](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateCrl.html)  **
  - **Description:** Grants permission to update a certificate revocation list (crl)
  - **Resource types (\*required):** [crl\*](#list_rolesanywhere-resource-crl)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProfile](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateProfile.html)  **
  - **Description:** Grants permission to update a profile
  - **Resource types (\*required):** [profile\*](#list_rolesanywhere-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrustAnchor](https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_UpdateTrustAnchor.html)  **
  - **Description:** Grants permission to update a trust anchor
  - **Resource types (\*required):** [trust-anchor\*](#list_rolesanywhere-resource-trust-anchor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Identity and Access Management Roles Anywhere
<a name="list_rolesanywhere-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [crl](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user)  | arn:${Partition}:rolesanywhere:${Region}:${Account}:crl/${CrlId} | [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user)  | arn:${Partition}:rolesanywhere:${Region}:${Account}:profile/${ProfileId} | [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_) | 
|  [subject](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user)  | arn:${Partition}:rolesanywhere:${Region}:${Account}:subject/${SubjectId} | [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_) | 
|  [trust-anchor](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html#first-time-user)  | arn:${Partition}:rolesanywhere:${Region}:${Account}:trust-anchor/${TrustAnchorId} | [aws:ResourceTag/${TagKey}](#list_rolesanywhere-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Identity and Access Management Roles Anywhere
<a name="list_rolesanywhere-policy-keys"></a>

AWS Identity and Access Management Roles Anywhere defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 