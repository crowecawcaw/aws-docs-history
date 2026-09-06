

# Use Signer actions in IAM
<a name="authen-apipermissions"></a>

Administrators who set up access control and write permissions policies that they attach to an IAM identity (identity-based policies) can use the following table as a reference. The first column in the table lists each AWS Signer API operation. You specify actions in a policy's `Action` element. You can use the IAM policy elements in your ACM policies to express conditions. For a complete list, see [IAM JSON policy element reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) in the *IAM User Guide*. 

**Note**  
To specify an action, use the `signer` prefix followed by the API operation name (for example, `signer:StartSigningJob`). 


**AWS Signer API Operations and Permissions**  

|  API Operation  |  Required Permissions (API Actions)  | 
| --- | --- | 
| [`AddProfilePermission`](https://docs.aws.amazon.com/signer/latest/api/API_AddProfilePermission.html) | `signer:AddProfilePermission` | 
| [`CancelSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html) | `signer:CancelSigningProfile` | 
| [`DescribeSigningJob`](https://docs.aws.amazon.com/signer/latest/api/API_DescribeSigningJob.html) | `signer:DescribeSigningJob` | 
| [`GetRevocationStatus`](https://docs.aws.amazon.com/signer/latest/api/API_GetRevocationStatus.html) | `signer:GetRevocationStatus` | 
| [`GetSigningPlatform`](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningPlatform.html) | `signer:GetSigningPlatform` | 
| [`GetSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html) | `signer:GetSigningProfile` | 
| [`ListProfilePermissions`](https://docs.aws.amazon.com/signer/latest/api/API_ListProfilePermissions.html) | `signer:ListProfilePermissions` | 
| [`ListSigningJobs`](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningJobs.html) | `signer:ListSigningJobs` | 
| [`ListSigningPlatforms`](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningPlatforms.html) | `signer:ListSigningPlatforms` | 
| [`ListSigningProfiles`](https://docs.aws.amazon.com/signer/latest/api/API_ListSigningProfiles.html) | `signer:ListSigningProfiles` | 
| [`ListTagsForResource`](https://docs.aws.amazon.com/signer/latest/api/API_ListTagsForResource.html) | `signer:ListTagsForResource` | 
| [`PutSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_PutSigningProfile.html) | `signer:PutSigningProfile` | 
| [`RemoveProfilePermission`](https://docs.aws.amazon.com/signer/latest/api/API_RemoveProfilePermission.html) | `signer:RemoveProfilePermission` | 
| [`RevokeSignature`](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSignature.html) | `signer:RevokeSignature` | 
| [`RevokeSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html) | `signer:RevokeSigningProfile` | 
| [`SignPayload`](https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html) | `signer:SignPayload` | 
| [`StartSigningJob`](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html) | `signer:StartSigningJob` | 
| [`TagResource`](https://docs.aws.amazon.com/signer/latest/api/API_TagResource.html) | `signer:TagResource` | 
| [`UntagResource`](https://docs.aws.amazon.com/signer/latest/api/API_UntagResource.html) | `signer:UntagResource` | 

For the actions `StartSigningJob`, `GetSigningProfile`, `CancelSigningProfile`,`RevokeSigningProfile`, and `SignPayload`, use the `signer:ProfileVersion` condition key to limit what version of a signing profile a principal has access to.


**AWS Signer API Condition Keys**  

|  Condition Key  |  Description  |  APIs  | 
| --- | --- | --- | 
| `signer:ProfileVersion` | Limit access to a specific version of a Signing Profile  | [`StartSigningJob`](https://docs.aws.amazon.com/signer/latest/api/API_StartSigningJob.html)<br />[`GetSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_GetSigningProfile.html)<br />[`CancelSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_CancelSigningProfile.html)<br />[`RevokeSigningProfile`](https://docs.aws.amazon.com/signer/latest/api/API_RevokeSigningProfile.html)<br />[`SignPayload`](https://docs.aws.amazon.com/signer/latest/api/API_SignPayload.html) | 