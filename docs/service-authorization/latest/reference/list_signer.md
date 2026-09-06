

# Actions, resources, and condition keys for AWS Signer
<a name="list_signer"></a>

AWS Signer (service prefix: `signer`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/signer/latest/api/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/signer/latest/developerguide/accessctrl-toplevel.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/signer/signer.json) for this service.

**Topics**
+ [API operations defined by AWS Signer](#list_signer-operations)
+ [Actions defined by AWS Signer](#list_signer-actions-as-permissions)
+ [Resource types defined by AWS Signer](#list_signer-resources-for-iam-policies)
+ [Condition keys for AWS Signer](#list_signer-policy-keys)

## API operations defined by AWS Signer
<a name="list_signer-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_signer-actions-as-permissions).




- **   AddProfilePermission  **
  - **SDK client:** signer
  - **IAM action:**  [signer:AddProfilePermission](#list_signer-action-AddProfilePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CancelSigningProfile  **
  - **SDK client:** signer
  - **IAM action:**  [signer:CancelSigningProfile](#list_signer-action-CancelSigningProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeSigningJob  **
  - **SDK client:** signer
  - **IAM action:**  [signer:DescribeSigningJob](#list_signer-action-DescribeSigningJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevocationStatus  **
  - **SDK client:** signer
  - **IAM action:**  [signer:GetRevocationStatus](#list_signer-action-GetRevocationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSigningPlatform  **
  - **SDK client:** signer
  - **IAM action:**  [signer:GetSigningPlatform](#list_signer-action-GetSigningPlatform) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSigningProfile  **
  - **SDK client:** signer
  - **IAM action:**  [signer:GetSigningProfile](#list_signer-action-GetSigningProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProfilePermissions  **
  - **SDK client:** signer
  - **IAM action:**  [signer:ListProfilePermissions](#list_signer-action-ListProfilePermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSigningJobs  **
  - **SDK client:** signer
  - **IAM action:**  [signer:ListSigningJobs](#list_signer-action-ListSigningJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSigningPlatforms  **
  - **SDK client:** signer
  - **IAM action:**  [signer:ListSigningPlatforms](#list_signer-action-ListSigningPlatforms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSigningProfiles  **
  - **SDK client:** signer
  - **IAM action:**  [signer:ListSigningProfiles](#list_signer-action-ListSigningProfiles) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **SDK client:** signer
  - **IAM action:**  [signer:ListTagsForResource](#list_signer-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutSigningProfile  **
  - **SDK client:** signer
  - **IAM action:**  [signer:PutSigningProfile](#list_signer-action-PutSigningProfile)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [signer:TagResource](#list_signer-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   RemoveProfilePermission  **
  - **SDK client:** signer
  - **IAM action:**  [signer:RemoveProfilePermission](#list_signer-action-RemoveProfilePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   RevokeSignature  **
  - **SDK client:** signer
  - **IAM action:**  [signer:RevokeSignature](#list_signer-action-RevokeSignature) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RevokeSigningProfile  **
  - **SDK client:** signer
  - **IAM action:**  [signer:RevokeSigningProfile](#list_signer-action-RevokeSigningProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SignPayload  **
  - **SDK client:** signer
  - **IAM action:**  [signer:SignPayload](#list_signer-action-SignPayload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSigningJob  **
  - **SDK client:** signer
  - **IAM action:**  [signer:StartSigningJob](#list_signer-action-StartSigningJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **SDK client:** signer
  - **IAM action:**  [signer:TagResource](#list_signer-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **SDK client:** signer
  - **IAM action:**  [signer:UntagResource](#list_signer-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   GetRevocationStatus  **
  - **SDK client:** signer-data
  - **IAM action:**  [signer:GetRevocationStatus](#list_signer-action-GetRevocationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Signer
<a name="list_signer-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddProfilePermission](https://docs.aws.amazon.com/signer/latest/api/API_AddProfilePermission.html)  **
  - **Description:** Grants permission to add cross-account permissions to a Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CancelSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html)  **
  - **Description:** Grants permission to change the state of a Signing Profile to CANCELED
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[signer:ProfileVersion](#list_signer-signer_ProfileVersion)
  - **Access level:** Write

- **   [DescribeSigningJob](https://docs.aws.amazon.com/signer/latest/api/API_DescribeSigningJob.html)  **
  - **Description:** Grants permission to return information about a specific Signing Job
  - **Resource types (\*required):** [signing-job\*](#list_signer-resource-signing-job)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRevocationStatus](https://docs.aws.amazon.com/signer/latest/api/API_GetRevocationStatus.html)  **
  - **Description:** Grants permission to query revocation info of signing resources
  - **Resource types (\*required):** [signing-job\*](#list_signer-resource-signing-job) / **Condition keys:**  
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSigningPlatform](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningPlatform.html)  **
  - **Description:** Grants permission to return information about a specific Signing Platform
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html)  **
  - **Description:** Grants permission to return information about a specific Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[signer:ProfileVersion](#list_signer-signer_ProfileVersion)
  - **Access level:** Read

- **   [ListProfilePermissions](https://docs.aws.amazon.com/signer/latest/api/API_ListProfilePermissions.html)  **
  - **Description:** Grants permission to list the cross-account permissions associated with a Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSigningJobs](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningJobs.html)  **
  - **Description:** Grants permission to list all Signing Jobs in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSigningPlatforms](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningPlatforms.html)  **
  - **Description:** Grants permission to list all available Signing Platforms
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSigningProfiles](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningProfiles.html)  **
  - **Description:** Grants permission to list all Signing Profiles in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/signer/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags associated with a Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_PutSigningProfile.html)  **
  - **Description:** Grants permission to create a new Signing Profile
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_signer-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_signer-aws_TagKeys)
  - **Access level:** Write

- **   [RemoveProfilePermission](https://docs.aws.amazon.com/signer/latest/api/API_RemoveProfilePermission.html)  **
  - **Description:** Grants permission to remove cross-account permissions from a Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [RevokeSignature](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSignature.html)  **
  - **Description:** Grants permission to change the state of a Signing Job to REVOKED
  - **Resource types (\*required):** [signing-job\*](#list_signer-resource-signing-job)
  - **Condition keys:** [signer:ProfileVersion](#list_signer-signer_ProfileVersion)
  - **Access level:** Write

- **   [RevokeSigningProfile](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html)  **
  - **Description:** Grants permission to change the state of a Signing Profile to REVOKED
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[signer:ProfileVersion](#list_signer-signer_ProfileVersion)
  - **Access level:** Write

- **   [SignPayload](https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html)  **
  - **Description:** Grants permission to initiate a Signing Job on the provided payload
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[signer:ProfileVersion](#list_signer-signer_ProfileVersion)
  - **Access level:** Write

- **   [StartSigningJob](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html)  **
  - **Description:** Grants permission to initiate a Signing Job on the provided code
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[signer:ProfileVersion](#list_signer-signer_ProfileVersion)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/signer/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_signer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_signer-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/signer/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a Signing Profile
  - **Resource types (\*required):** [signing-profile\*](#list_signer-resource-signing-profile)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_signer-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_signer-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Signer
<a name="list_signer-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [signing-job](https://docs.aws.amazon.com/signer/latest/developerguide/gs-job.html)  | arn:${Partition}:signer:${Region}:${Account}:/signing-jobs/${JobId} |   | 
|  [signing-profile](https://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html)  | arn:${Partition}:signer:${Region}:${Account}:/signing-profiles/${ProfileName} | [aws:ResourceTag/${TagKey}](#list_signer-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Signer
<a name="list_signer-policy-keys"></a>

AWS Signer defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by presence of mandatory tags in the request | ArrayOfString | 
|   [signer:ProfileVersion](https://docs.aws.amazon.com/signer/latest/developerguide/authen-apipermissions.html)  | Filters access by version of the Signing Profile | String | 