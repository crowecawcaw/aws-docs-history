# AWS managed policies for AWS Partner Central users

An AWS managed policy is a standalone policy created and administered by AWS. AWS
managed policies provide permissions for many common use cases so that you can start
assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for
your specific use cases because they're available for all AWS customers to use. We
recommend that you reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") specific to your use cases. For more information,
refer to [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies").

The AWS managed policies described in this section manage AWS Partner Central users' access
to AWS Marketplace. For more information about AWS Marketplace seller policies, refer to
[AWS managed policies
for AWS Marketplace sellers](../../../marketplace/latest/userguide/security-iam-awsmanpol.md "../../../marketplace/latest/userguide/security-iam-awsmanpol.md").

###### Topics

- [AWS managed
  policy: AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess")
- [AWS managed policy:
  PartnerCentralAccountManagementUserRoleAssociation](#user-role-association "#user-role-association")
- [AWS
  managed policy: AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement")
- [AWS
  managed policy: AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess "#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess")
- [AWS
  managed policy: AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy "#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy")
- [AWS
  managed policy: AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelManagement")
- [AWS
  managed policy: AWSPartnerCentralChannelHandshakeApprovalManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement")
- [AWS
  managed policy: AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement "#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement")
- [AWS Partner Central updates to AWS
  managed policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed

policy: `AWSPartnerCentralFullAccess`

You can attach the `AWSPartnerCentralFullAccess` policy to your IAM
identities.

This policy grants full access to AWS Partner Central and related AWS
services.

To view the permissions for this policy, see
[AWSPartnerCentralFullAccess](../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy:

`PartnerCentralAccountManagementUserRoleAssociation`

You can attach the `PartnerCentralAccountManagementUserRoleAssociation`
policy to your IAM identities. This policy is used by a partner cloud admin to manage
IAM roles linked to partner users.

This policy allows the following operations:

- List all roles.
- Pass an IAM role with the name prefix `PartnerCentralRoleFor` to
  the AWS Partner Central account management service.
- Associate a AWS Partner Central user with an IAM role.
- Disassociate a AWS Partner Central user from an IAM role.

To view the permissions for this policy, see
[PartnerCentralAccountManagementUserRoleAssociation](../../../aws-managed-policy/latest/reference/PartnerCentralAccountManagementUserRoleAssociation.md "../../../aws-managed-policy/latest/reference/PartnerCentralAccountManagementUserRoleAssociation.md")
in the _AWS Managed Policy
Reference_.

## AWS

managed policy: `AWSPartnerCentralOpportunityManagement`

You can attach the `AWSPartnerCentralOpportunityManagement` policy to your
IAM identities.

This policy grants full access to manage opportunities in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralOpportunityManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS

managed policy: `AWSPartnerCentralSandboxFullAccess`

You can attach the `AWSPartnerCentralSandboxFullAccess` policy to your
IAM identities.

This policy grants access for developer testing in the Sandbox catalog.

To view the permissions for this policy, see
[AWSPartnerCentralSandboxFullAccess](../../../aws-managed-policy/latest/reference/AWSPartnerCentralSandboxFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralSandboxFullAccess.md")
in the _AWS Managed Policy
Reference_.

## AWS

managed policy: `AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy`

You can attach the `AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy` policy to your
IAM identities.

This policy provides the ResourceSnapshotJob with permission to read a resource and
snapshot it in the target environment. For more information on how to use this policy,
see [Working with
multi-partner opportunities](../APIReference/working-with-multi-partner-opportunities.md#creating-custom-policy-resourcesnapshotjobrole "../APIReference/working-with-multi-partner-opportunities.md#creating-custom-policy-resourcesnapshotjobrole") in the _AWS Partner Central API Reference_.

To view the permissions for this policy, see
[AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy.md")
in the _AWS Managed Policy
Reference_.

## AWS

managed policy: `AWSPartnerCentralChannelManagement`

You can attach the `AWSPartnerCentralChannelManagement` policy to your
IAM identities.

This policy grants access to manage channel programs and relationships in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralChannelManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS

managed policy: `AWSPartnerCentralChannelHandshakeApprovalManagement`

You can attach the `AWSPartnerCentralChannelHandshakeApprovalManagement` policy to your
IAM identities.

This policy grants access to channel handshake approval management activities in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralChannelHandshakeApprovalManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelHandshakeApprovalManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelHandshakeApprovalManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS

managed policy: `AWSPartnerCentralMarketingManagement`

You can attach the `AWSPartnerCentralMarketingManagement` policy to your
IAM identities.

This policy grants access to manage marketing activities and campaigns in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralMarketingManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralMarketingManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralMarketingManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS Partner Central updates to AWS

managed policies

View details about updates to AWS managed policies for AWS Partner Central since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the AWS Partner Central [Document history for the AWS Partner Central Getting Started
Guide](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                  | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess") —<br>Update to an existing policy                                                                                        | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality and to add AWS Marketplace Agreements read access for MPOPP benefits functionality.                                                             | February 4, 2026  |
| [AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement "#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement")<br>— New policy                                                                               | AWS Partner Central added a new policy to grant access to manage partner central marketing and campaigns.                                                                                                                                                    | November 30, 2025 |
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess") —<br>Update to an existing policy                                                                                        | AWS Partner Central updated a policy to add legacy Partner Central access, put files into S3, and get AWS Marketplace entities.                                                                                                                              | November 30, 2025 |
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement") —<br>Update to an existing policy                                                       | AWS Partner Central updated a policy to add engagement context access, opportunity from engagement task access, and legacy Partner Central access, get dashboard, collaboration channel access, get partner, and tag opportunity and resource snapshot jobs. | November 30, 2025 |
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelManagement") —<br>Update to an existing policy                                                                   | AWS Partner Central updated a policy to add legacy Partner Central access, get dashboard, and get partner.                                                                                                                                                   | November 30, 2025 |
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess") —<br>Update to an existing policy                                                                                        | AWS Partner Central updated a policy to add Channel billing transfer role access.                                                                                                                                                                            | November 19, 2025 |
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelManagement")<br>— New policy                                                                                     | AWS Partner Central added a new policy to grant access to manage<br>channel management activities.                                                                                                                                                           | November 19, 2025 |
| [AWSPartnerCentralChannelHandshakeApprovalManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement")<br>— New policy                                  | AWS Partner Central added a new policy to grant access to channel<br>handshake approval management activities.                                                                                                                                               | November 19, 2025 |
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess") —<br>Update to an existing policy                                                                                        | AWS Partner Central updated a policy.                                                                                                                                                                                                                        | December 4, 2024  |
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement") —<br>Update to an existing policy                                                       | AWS Partner Central updated a policy.                                                                                                                                                                                                                        | December 4, 2024  |
| [AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess "#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess") —<br>Update to an existing policy                                                                   | AWS Partner Central updated a policy.                                                                                                                                                                                                                        | December 4, 2024  |
| [AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy "#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy")<br>— New policy | AWS Partner Central added a new policy to grant access to read resources<br>and create snapshots.                                                                                                                                                            | December 4, 2024  |
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess") –<br>New policy                                                                                                          | AWS Partner Central added a new policy to grant full access to the<br>AWS Partner Central service.                                                                                                                                                           | November 18, 2024 |
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement") — New<br>policy                                                                         | AWS Partner Central added a new policy to grant full access to manage<br>opportunities in AWS Partner Central.                                                                                                                                               | November 14, 2024 |
| [AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess "#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess") — New<br>policy                                                                                     | AWS Partner Central added a new policy to grant access for developer<br>testing in the Sandbox catalog.                                                                                                                                                      | November 14, 2024 |
| AWS Partner Central started tracking changes                                                                                                                                                                                                                      | AWS Partner Central started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                | November 14, 2024 |
