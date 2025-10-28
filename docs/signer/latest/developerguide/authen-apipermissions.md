# Use Signer actions in IAM

Administrators who set up access control and write permissions policies that they
attach to an IAM identity (identity-based policies) can use the following table as a
reference. The first column in the table lists each AWS Signer API operation. You
specify actions in a policy's `Action` element. You can use the IAM policy
elements in your ACM policies to express conditions. For a complete list, see [IAM JSON policy element reference](../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements.md#AvailableKeys") in the _IAM User Guide_.

###### Note

To specify an action, use the `signer` prefix followed by the API
operation name (for example, `signer:StartSigningJob`).

| AWS Signer API Operations and Permissions                                                                  | API Operation                                           | Required Permissions (API Actions)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- | ----------- | ---- |
| [`AddProfilePermission`](../api/API_AddProfilePermission.md "../api/API_AddProfilePermission.md")          | `signer:AddProfilePermission`                           |
| [`CancelSigningProfile`](../api/API_CancelSigningProfile.md "../api/API_CancelSigningProfile.md")          | `signer:CancelSigningProfile`                           |
| [`DescribeSigningJob`](../api/API_DescribeSigningJob.md "../api/API_DescribeSigningJob.md")                | `signer:DescribeSigningJob`                             |
| [`GetRevocationStatus`](../api/API_GetRevocationStatus.md "../api/API_GetRevocationStatus.md")             | `signer:GetRevocationStatus`                            |
| [`GetSigningPlatform`](../api/API_GetSigningPlatform.md "../api/API_GetSigningPlatform.md")                | `signer:GetSigningPlatform`                             |
| [`GetSigningProfile`](../api/API_GetSigningProfile.md "../api/API_GetSigningProfile.md")                   | `signer:GetSigningProfile`                              |
| [`ListProfilePermissions`](../api/API_ListProfilePermissions.md "../api/API_ListProfilePermissions.md")    | `signer:ListProfilePermissions`                         |
| [`ListSigningJobs`](../api/API_ListSigningJobs.md "../api/API_ListSigningJobs.md")                         | `signer:ListSigningJobs`                                |
| [`ListSigningPlatforms`](../api/API_ListSigningPlatforms.md "../api/API_ListSigningPlatforms.md")          | `signer:ListSigningPlatforms`                           |
| [`ListSigningProfiles`](../api/API_ListSigningProfiles.md "../api/API_ListSigningProfiles.md")             | `signer:ListSigningProfiles`                            |
| [`ListTagsForResource`](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md")             | `signer:ListTagsForResource`                            |
| [`PutSigningProfile`](../api/API_PutSigningProfile.md "../api/API_PutSigningProfile.md")                   | `signer:PutSigningProfile`                              |
| [`RemoveProfilePermission`](../api/API_RemoveProfilePermission.md "../api/API_RemoveProfilePermission.md") | `signer:RemoveProfilePermission`                        |
| [`RevokeSignature`](../api/API_RevokeSignature.md "../api/API_RevokeSignature.md")                         | `signer:RevokeSignature`                                |
| [`RevokeSigningProfile`](../api/API_RevokeSigningProfile.md "../api/API_RevokeSigningProfile.md")          | `signer:RevokeSigningProfile`                           |
| [`SignPayload`](../api/API_SignPayload.md "../api/API_SignPayload.md")                                     | `signer:SignPayload`                                    |
| [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md")                         | `signer:StartSigningJob`                                |
| [`TagResource`](../api/API_TagResource.md "../api/API_TagResource.md")                                     | `signer:TagResource`                                    |
| [`UntagResource`](../api/API_UntagResource.md "../api/API_UntagResource.md")                               | `signer:UntagResource`                                  | For the actions `StartSigningJob`, `GetSigningProfile`, `CancelSigningProfile`,`RevokeSigningProfile`, and `SignPayload`, use the `signer:ProfileVersion` condition key to limit what version of a signing profile a principal has access to. AWS Signer API Condition Keys                                                                                                                                                                            | Condition Key | Description | APIs |
| ---                                                                                                        | ---                                                     | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `signer:ProfileVersion`                                                                                    | Limit access to a specific version of a Signing Profile | [`StartSigningJob`](../api/API_StartSigningJob.md "../api/API_StartSigningJob.md") [`GetSigningProfile`](../api/API_GetSigningProfile.md "../api/API_GetSigningProfile.md") [`CancelSigningProfile`](../api/API_CancelSigningProfile.md "../api/API_CancelSigningProfile.md") [`RevokeSigningProfile`](../api/API_RevokeSigningProfile.md "../api/API_RevokeSigningProfile.md") [`SignPayload`](../api/API_SignPayload.md "../api/API_SignPayload.md") |
