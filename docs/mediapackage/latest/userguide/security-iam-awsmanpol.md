

# AWS managed policies for AWS Elemental MediaPackage
<a name="security-iam-awsmanpol"></a>





An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.









## AWS managed policy: AWSElementalMediaPackageV2FullAccess
<a name="security-iam-awsmanpol-AWSElementalMediaPackageV2FullAccess"></a>



This policy grants contributor permissions that allow all actions on all live resources in MediaPackage.

You can attach the `AWSElementalMediaPackageV2FullAccess` policy to your IAM identities.











To view the permissions for this policy, see [AWSElementalMediaPackageV2FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElementalMediaPackageV2FullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: AWSElementalMediaPackageV2ReadOnly
<a name="security-iam-awsmanpol-AWSElementalMediaPackageV2ReadOnly"></a>



This policy grants contributor permissions that allow read-only actions on all live resources in MediaPackage.



You can attach the `AWSElementalMediaPackageV2ReadOnly` policy to your IAM identities.











To view the permissions for this policy, see [AWSElementalMediaPackageV2ReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElementalMediaPackageV2ReadOnly.html) in the *AWS Managed Policy Reference*.





## MediaPackage updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for MediaPackage since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the MediaPackage [Document history](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| `AWSElementalMediaPackageV2FullAccess` – New policy | MediaPackage added a new full-access policy for live resources.<br />This policy allows all actions on all live resources in MediaPackage. | July 25, 2023 | 
| `AWSElementalMediaPackageV2ReadOnly` – New policy | MediaPackage added a new read-only pollicy for live resources.<br />This policy allows read-only actions on all live resources in MediaPackage. | July 25, 2023 | 
| MediaPackage started tracking changes | MediaPackage started tracking changes for its AWS managed policies. | July 25, 2023 | 