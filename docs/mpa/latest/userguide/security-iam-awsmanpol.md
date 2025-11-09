# AWS managed policies for Multi-party approval

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

## AWS managed policy:

MultiPartyApprovalFullAccess

The `MultiPartyApprovalFullAccess` policy provides full access to Multi-party approval
operations. This policy grants broad permissions to manage all aspects of multi-party
approval workflows and the following related identity services.

- Multi-party approval – Full access to create, read, update, and delete multi-party
  approval operations (`mpa`)
- AWS Organizations – Full access to administer approval teams and policies
  (`organizations`)
- AWS IAM Identity Center – Full access to manage identity sources for approvals
  (`sso`, `sso-directory`)
- AWS Key Management Service (AWS KMS) – Decrypt operation for accessing SSO instances as IAM Identity Center
  supports customer managed keys, which allows customer to use their own AWS KMS keys
  to encrypt identity data (`kms:Decrypt`)

To review the permissions for this policy, see [MultiPartyApprovalFullAccess](../../../aws-managed-policy/latest/reference/MultiPartyApprovalFullAccess.md "../../../aws-managed-policy/latest/reference/MultiPartyApprovalFullAccess.md") in the _AWS Managed Policy Reference
Guide_.

## AWS managed

policy: MultiPartyApprovalReadOnlyAccess

The `MultiPartyApprovalReadOnlyAccess` policy provides read-only access to
Multi-party approval operations and the following related identity services.

- Multi-party approval – Read-only access to multi-party approval operations
  (`mpa`)
- AWS Organizations – Basic read access to organization information
  (`organizations`)
- AWS IAM Identity Center – Read access to SSO instances and the user directory
  (`sso`, `sso-directory`)
- AWS KMS – Decrypt operation for accessing SSO instances as IAM Identity Center
  supports customer managed keys, which allows customer to use their own AWS KMS keys
  to encrypt identity data (`kms:Decrypt`)

To review the permissions for this policy, see [MultiPartyApprovalReadOnlyAccess](../../../aws-managed-policy/latest/reference/MultiPartyApprovalReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/MultiPartyApprovalReadOnlyAccess.md") in the _AWS Managed Policy
Reference Guide_.

## Multi-party approval updates to AWS managed

policies

View details about updates to AWS managed policies for Multi-party approval since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Multi-party approval Document history page.

| Change                                                                                                                                                                                                                                | Description                                                                                                                                                                                                                                     | Date              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| [MultiPartyApprovalFullAccess](#security-iam-awsmanpol-MultiPartyApprovalFullAccess "#security-iam-awsmanpol-MultiPartyApprovalFullAccess") – updated to include<br>`kms:Decrypt` permission which decrypts identity data             | Added the `kms:Decrypt` permission to the<br>`MultiPartyApprovalFullAccess` managed policy for AWS IAM Identity Center to<br>support customer managed keys, which allows you to use your own AWS KMS keys<br>to encrypt your identity data.     | September 8, 2025 |
| [MultiPartyApprovalReadOnlyAccess](#security-iam-awsmanpol-MultiPartyApprovalReadOnlyAccess "#security-iam-awsmanpol-MultiPartyApprovalReadOnlyAccess") – updated to include<br>`kms:Decrypt` permission which decrypts identity data | Added the `kms:Decrypt` permission to the<br>`MultiPartyApprovalReadOnlyAccess` managed policy for<br>AWS IAM Identity Center to support customer managed keys, which allows you to use your own<br>AWS KMS keys to encrypt your identity data. | September 8, 2025 |
| Multi-party approval started tracking changes                                                                                                                                                                                         | Multi-party approval started tracking changes for its AWS managed policies.                                                                                                                                                                     | June 17, 2025     |
