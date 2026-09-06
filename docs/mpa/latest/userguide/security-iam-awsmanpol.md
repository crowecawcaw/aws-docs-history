

# AWS managed policies for Multi-party approval
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: MultiPartyApprovalFullAccess
<a name="security-iam-awsmanpol-MultiPartyApprovalFullAccess"></a>

The `MultiPartyApprovalFullAccess` policy provides full access to Multi-party approval operations. This policy grants broad permissions to manage all aspects of multi-party approval workflows and the following related identity services.
+ Multi-party approval – Full access to create, read, update, and delete multi-party approval operations (`mpa`)
+ AWS Organizations – Full access to administer approval teams and policies (`organizations`)
+ AWS IAM Identity Center – Full access to manage identity sources for approvals (`sso`, `sso-directory`)
+ AWS Key Management Service (AWS KMS) – Decrypt operation for accessing SSO instances as IAM Identity Center supports customer managed keys, which allows customer to use their own AWS KMS keys to encrypt identity data (`kms:Decrypt`)

To review the permissions for this policy, see [MultiPartyApprovalFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/MultiPartyApprovalFullAccess.html) in the *AWS Managed Policy Reference Guide*.

## AWS managed policy: MultiPartyApprovalReadOnlyAccess
<a name="security-iam-awsmanpol-MultiPartyApprovalReadOnlyAccess"></a>

The `MultiPartyApprovalReadOnlyAccess` policy provides read-only access to Multi-party approval operations and the following related identity services.
+ Multi-party approval – Read-only access to multi-party approval operations (`mpa`)
+ AWS Organizations – Basic read access to organization information (`organizations`)
+ AWS IAM Identity Center – Read access to SSO instances and the user directory (`sso`, `sso-directory`)
+ AWS KMS – Decrypt operation for accessing SSO instances as IAM Identity Center supports customer managed keys, which allows customer to use their own AWS KMS keys to encrypt identity data (`kms:Decrypt`)

To review the permissions for this policy, see [MultiPartyApprovalReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/MultiPartyApprovalReadOnlyAccess.html) in the *AWS Managed Policy Reference Guide*.

## Multi-party approval updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Multi-party approval since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Multi-party approval Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [MultiPartyApprovalFullAccess](#security-iam-awsmanpol-MultiPartyApprovalFullAccess) – updated to include `kms:Decrypt` permission which decrypts identity data | Added the `kms:Decrypt` permission to the `MultiPartyApprovalFullAccess` managed policy for AWS IAM Identity Center to support customer managed keys, which allows you to use your own AWS KMS keys to encrypt your identity data. | September 8, 2025 | 
| [MultiPartyApprovalReadOnlyAccess](#security-iam-awsmanpol-MultiPartyApprovalReadOnlyAccess) – updated to include `kms:Decrypt` permission which decrypts identity data | Added the `kms:Decrypt` permission to the `MultiPartyApprovalReadOnlyAccess` managed policy for AWS IAM Identity Center to support customer managed keys, which allows you to use your own AWS KMS keys to encrypt your identity data. | September 8, 2025 | 
| Multi-party approval started tracking changes | Multi-party approval started tracking changes for its AWS managed policies. | June 17, 2025 | 