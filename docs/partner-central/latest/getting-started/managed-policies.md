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

- [AWS managed policy: AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess")
- [AWS managed policy: PartnerCentralAccountManagementUserRoleAssociation](#user-role-association "#user-role-association")
- [AWS managed policy: AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement")
- [AWS managed policy: AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess "#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess")
- [AWS managed policy: AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy "#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy")
- [AWS managed policy: AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelManagement")
- [AWS managed policy: AWSPartnerCentralChannelHandshakeApprovalManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement")
- [AWS managed policy: AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement "#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement")
- [AWS managed policy: PartnerCentralIncentiveBenefitManagement](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement "#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement")
- [AWS managed policy: AWSPartnerProServeToolsFullAccess](#security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess "#security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess")
- [AWS managed policy: AWSPartnerProServeToolsOrganizationReaderIndividualContributor](#security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor "#security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor")
- [AWS managed policy: AWSPartnerProServeToolsIndividualContributor](#security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor "#security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor")
- [AWS managed policy: AWSPartnerCentralRevenueAttributionManagement](#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement "#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement")
- [AWS managed policy: AWSRevenueAttributionManagement](#security-iam-awsmanpol-AWSRevenueAttributionManagement "#security-iam-awsmanpol-AWSRevenueAttributionManagement")
- [AWS Partner Central updates to AWS managed policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWS managed policy: `AWSPartnerCentralFullAccess`

You can attach the `AWSPartnerCentralFullAccess` policy to your IAM
identities.

This policy grants full access to AWS Partner Central and related AWS
services.

To view the permissions for this policy, see
[AWSPartnerCentralFullAccess](../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `PartnerCentralAccountManagementUserRoleAssociation`

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

## AWS managed policy: `AWSPartnerCentralOpportunityManagement`

You can attach the `AWSPartnerCentralOpportunityManagement` policy to your
IAM identities.

This policy grants full access to manage opportunities in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralOpportunityManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerCentralSandboxFullAccess`

You can attach the `AWSPartnerCentralSandboxFullAccess` policy to your
IAM identities.

This policy grants access for developer testing in the Sandbox catalog.

To view the permissions for this policy, see
[AWSPartnerCentralSandboxFullAccess](../../../aws-managed-policy/latest/reference/AWSPartnerCentralSandboxFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralSandboxFullAccess.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy`

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

## AWS managed policy: `AWSPartnerCentralChannelManagement`

You can attach the `AWSPartnerCentralChannelManagement` policy to your
IAM identities.

This policy grants access to manage channel programs and relationships in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralChannelManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerCentralChannelHandshakeApprovalManagement`

You can attach the `AWSPartnerCentralChannelHandshakeApprovalManagement` policy to your
IAM identities.

This policy grants access to channel handshake approval management activities in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralChannelHandshakeApprovalManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelHandshakeApprovalManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralChannelHandshakeApprovalManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerCentralMarketingManagement`

You can attach the `AWSPartnerCentralMarketingManagement` policy to your
IAM identities.

This policy grants access to manage marketing activities and campaigns in AWS Partner Central.

To view the permissions for this policy, see
[AWSPartnerCentralMarketingManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralMarketingManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralMarketingManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `PartnerCentralIncentiveBenefitManagement`

You can attach the `PartnerCentralIncentiveBenefitManagement` policy to your
IAM identities.

This policy grants access to manage all the incentive benefits in AWS Partner Central.

To view the permissions for this policy, see
[PartnerCentralIncentiveBenefitManagement](../../../aws-managed-policy/latest/reference/PartnerCentralIncentiveBenefitManagement.md "../../../aws-managed-policy/latest/reference/PartnerCentralIncentiveBenefitManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerProServeToolsFullAccess`

You can attach the `AWSPartnerProServeToolsFullAccess` policy to your
IAM identities.

This policy grants full access to AWS ProServe Tools (A2T and MPA) via AWS Partner Central Single Sign-On.
It includes all assessment roles — individual contributor, organization reader, organization contributor, and
organization admin — enabling complete access to create, read, update, and share assessments across the organization,
as well as manage organization-level settings.

**Roles granted:**

- AssessmentIndividualContributor
- AssessmentOrganizationReader
- AssessmentOrganizationContributor
- OrganizationAdmin

To view the permissions for this policy, see
[AWSPartnerProServeToolsFullAccess](../../../aws-managed-policy/latest/reference/AWSPartnerProServeToolsFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerProServeToolsFullAccess.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerProServeToolsOrganizationReaderIndividualContributor`

You can attach the `AWSPartnerProServeToolsOrganizationReaderIndividualContributor` policy to your
IAM identities.

This policy grants read access to all organizational assessments in A2T, combined with the ability to create
and manage the user's own assessments in both A2T and MPA. It is intended for users who need visibility into
team assessments while retaining the ability to manage their own work.

###### Note

MPA does not support read-only mode. Users assigned this policy will retain read/write access to their
own MPA assessments.

**Roles granted:**

- AssessmentIndividualContributor
- AssessmentOrganizationReader

To view the permissions for this policy, see
[AWSPartnerProServeToolsOrganizationReaderIndividualContributor](../../../aws-managed-policy/latest/reference/AWSPartnerProServeToolsOrganizationReaderIndividualContributor.md "../../../aws-managed-policy/latest/reference/AWSPartnerProServeToolsOrganizationReaderIndividualContributor.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerProServeToolsIndividualContributor`

You can attach the `AWSPartnerProServeToolsIndividualContributor` policy to your
IAM identities.

This policy grants the minimum permissions required to access AWS ProServe Tools via AWS Partner Central
Single Sign-On. Users can create, read, update, and share their own assessments in both A2T and MPA. Access is
scoped to assessments created by the user's own IAM identity (role or user ARN).

**Roles granted:**

- AssessmentIndividualContributor

To view the permissions for this policy, see
[AWSPartnerProServeToolsIndividualContributor](../../../aws-managed-policy/latest/reference/AWSPartnerProServeToolsIndividualContributor.md "../../../aws-managed-policy/latest/reference/AWSPartnerProServeToolsIndividualContributor.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSPartnerCentralRevenueAttributionManagement`

You can attach the `AWSPartnerCentralRevenueAttributionManagement` policy
to your IAM identities.

This policy provides necessary access for revenue attribution management activities.
It is intended for AWS accounts registered with AWS Partner Central.

This policy grants access to the following capabilities:

- Create, retrieve, update, and list Revenue Attribution resources and their
  allocations.
- Create, retrieve, and list Marketplace Revenue Share resources and their
  allocations.
- Tag and untag Revenue Attribution and Marketplace Revenue Share
  resources.

To view the permissions for this policy, see
[AWSPartnerCentralRevenueAttributionManagement](../../../aws-managed-policy/latest/reference/AWSPartnerCentralRevenueAttributionManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralRevenueAttributionManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS managed policy: `AWSRevenueAttributionManagement`

You can attach the `AWSRevenueAttributionManagement` policy to your IAM
identities.

This policy provides necessary access for revenue attribution management activities.
It is intended for AWS accounts who are not registered with AWS Partner Central.

This policy grants access to the following capabilities:

- Create, retrieve, update, and list Revenue Attribution resources.
- Tag and untag Revenue Attribution resources.

To view the permissions for this policy, see
[AWSRevenueAttributionManagement](../../../aws-managed-policy/latest/reference/AWSRevenueAttributionManagement.md "../../../aws-managed-policy/latest/reference/AWSRevenueAttributionManagement.md")
in the _AWS Managed Policy
Reference_.

## AWS Partner Central updates to AWS managed policies

View details about updates to AWS managed policies for AWS Partner Central since this
service began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the AWS Partner Central [Document history for the AWS Partner Central Getting Started Guide](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                  | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| [AWSPartnerCentralRevenueAttributionManagement](#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement "#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement") —<br>New policy                                                    | AWS Partner Central added a new policy to provide necessary access for revenue attribution management activities for partners.                                                                                                                               | June 30, 2026     |
| [AWSRevenueAttributionManagement](#security-iam-awsmanpol-AWSRevenueAttributionManagement "#security-iam-awsmanpol-AWSRevenueAttributionManagement") —<br>New policy                                                                                              | AWS Partner Central added a new policy to provide necessary access for revenue attribution management activities for customers.                                                                                                                              | June 30, 2026     |
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement") —<br>Update to an existing policy                                                       | AWS Partner Central updated a policy to add prospecting actions access.                                                                                                                                                                                      | June 16, 2026     |
| [AWSPartnerProServeToolsFullAccess](#security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess "#security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess") —<br>New policy                                                                                        | AWS Partner Central added a new policy to grant full access to AWS ProServe Tools (A2T and MPA) via AWS Partner Central Single Sign-On with all assessment roles.                                                                                            | March 23, 2026    |
| [AWSPartnerProServeToolsOrganizationReaderIndividualContributor](#security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor "#security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor") —<br>New policy | AWS Partner Central added a new policy to grant read access to organizational assessments in A2T and manage own assessments in both A2T and MPA.                                                                                                             | March 23, 2026    |
| [AWSPartnerProServeToolsIndividualContributor](#security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor "#security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor") —<br>New policy                                                       | AWS Partner Central added a new policy to grant minimum permissions to access AWS ProServe Tools and manage own assessments.                                                                                                                                 | March 23, 2026    |
| [PartnerCentralIncentiveBenefitManagement](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement "#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement") —<br>Update to an existing policy                                                 | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol.                                                                                                                         | March 13, 2026    |
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement") —<br>Update to an existing policy                                                       | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol.                                                                                                                         | March 13, 2026    |
| [AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess "#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess") —<br>Update to an existing policy                                                                   | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol.                                                                                                                         | March 13, 2026    |
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess "#security-iam-awsmanpol-AWSPartnerCentralFullAccess") —<br>Update to an existing policy                                                                                        | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol.                                                                                                                         | March 13, 2026    |
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement "#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement") —<br>Update to an existing policy                                                       | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality.                                                                                                                                                | February 23, 2026 |
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement "#security-iam-awsmanpol-AWSPartnerCentralChannelManagement") —<br>Update to an existing policy                                                                   | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality.                                                                                                                                                | February 23, 2026 |
| [AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement "#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement") —<br>Update to an existing policy                                                             | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality.                                                                                                                                                | February 23, 2026 |
| [PartnerCentralIncentiveBenefitManagement](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement "#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement") —<br>New policy                                                                   | AWS Partner Central added a new policy to grant access to all the incentive benefits functionality.                                                                                                                                                          | February 11, 2026 |
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
