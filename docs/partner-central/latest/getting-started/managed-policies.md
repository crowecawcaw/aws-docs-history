

# AWS managed policies for AWS Partner Central users

An AWS managed policy is a standalone policy created and administered by AWS. AWS managed policies provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) specific to your use cases. For more information, refer to [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies).

The AWS managed policies described in this section manage AWS Partner Central users' access to AWS Marketplace. For more information about AWS Marketplace seller policies, refer to [AWS managed policies for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html).

**Topics**
+ [AWS managed policy: `AWSPartnerCentralFullAccess`](#security-iam-awsmanpol-AWSPartnerCentralFullAccess)
+ [AWS managed policy: `PartnerCentralAccountManagementUserRoleAssociation`](#user-role-association)
+ [AWS managed policy: `AWSPartnerCentralOpportunityManagement`](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement)
+ [AWS managed policy: `AWSPartnerCentralSandboxFullAccess`](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess)
+ [AWS managed policy: `AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy`](#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy)
+ [AWS managed policy: `AWSPartnerCentralChannelManagement`](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement)
+ [AWS managed policy: `AWSPartnerCentralChannelHandshakeApprovalManagement`](#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement)
+ [AWS managed policy: `AWSPartnerCentralMarketingManagement`](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement)
+ [AWS managed policy: `PartnerCentralIncentiveBenefitManagement`](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement)
+ [AWS managed policy: `AWSPartnerProServeToolsFullAccess`](#security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess)
+ [AWS managed policy: `AWSPartnerProServeToolsOrganizationReaderIndividualContributor`](#security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor)
+ [AWS managed policy: `AWSPartnerProServeToolsIndividualContributor`](#security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor)
+ [AWS managed policy: `AWSPartnerCentralRevenueAttributionManagement`](#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement)
+ [AWS managed policy: `AWSRevenueAttributionManagement`](#security-iam-awsmanpol-AWSRevenueAttributionManagement)
+ [AWS managed policy: `AWSPartnerCentralBusinessPlanManagement`](#security-iam-awsmanpol-AWSPartnerCentralBusinessPlanManagement)
+ [AWS managed policy: `AWSPartnerCentralAccountManagementServiceRolePolicy`](#security-iam-awsmanpol-AWSPartnerCentralAccountManagementServiceRolePolicy)
+ [AWS Partner Central updates to AWS managed policies](#security-iam-awsmanpol-updates)

## AWS managed policy: `AWSPartnerCentralFullAccess`
<a name="security-iam-awsmanpol-AWSPartnerCentralFullAccess"></a>

You can attach the `AWSPartnerCentralFullAccess` policy to your IAM identities.

With this policy, you can access all AWS Partner Central features and related services. This policy allows the following operations:
+ Create, edit, and submit opportunities
+ Accept and manage leads
+ Create and manage fund requests and claims
+ View historical fund requests and funding wallets
+ Manage Partner Central settings and create Partner and Seller profiles
+ Access and manage Marketing Central campaigns, content, and case studies
+ View and manage channel relationships, channel handshakes, deal registration requests, and distribution engagement requests
+ Create and manage subsidiary account connections
+ Accept and manage multi-partner connections and opportunities
+ Search for and request connections with other AWS Partners
+ Create and manage Partner Business plans
+ Access Partner Scorecard and Partner Analytics
+ Access Badge Manager, Guides, and the AWS assistant (Partner Assistant)
+ Create and manage program applications
+ Create, view, search, reply to, and resolve Support cases, add attachments to them, and view them in the Support Center console. This access applies to every Support case in the account, not only cases about AWS Partner Central or AWS Marketplace.

 To view the permissions for this policy, see [AWSPartnerCentralFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `PartnerCentralAccountManagementUserRoleAssociation`
<a name="user-role-association"></a>

You can attach the `PartnerCentralAccountManagementUserRoleAssociation` policy to your IAM identities. This policy is used by a partner cloud admin to manage IAM roles linked to partner users.

This policy allows the following operations:
+ List all roles.
+ Pass an IAM role with the name prefix `PartnerCentralRoleFor` to the AWS Partner Central account management service.
+ Associate a AWS Partner Central user with an IAM role.
+ Disassociate a AWS Partner Central user from an IAM role.

 To view the permissions for this policy, see [PartnerCentralAccountManagementUserRoleAssociation](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/PartnerCentralAccountManagementUserRoleAssociation.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralOpportunityManagement`
<a name="security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement"></a>

You can attach the `AWSPartnerCentralOpportunityManagement` policy to your IAM identities.

With this policy, you can manage opportunities and leads in AWS Partner Central. This policy allows the following operations:
+ Create, edit, and submit opportunities
+ Accept and manage leads
+ Search leads and list lead groups
+ Map customer accounts to AWS customers, import them in bulk, and read their enrichment data
+ Accept and manage multi-partner opportunities
+ Access Partner Scorecard, Guides, and the AWS assistant (Partner Assistant)
+ Create, view, search, reply to, and resolve Support cases, add attachments to them, and view them in the Support Center console. This access applies to every Support case in the account, not only cases about AWS Partner Central.

 To view the permissions for this policy, see [AWSPartnerCentralOpportunityManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralSandboxFullAccess`
<a name="security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess"></a>

You can attach the `AWSPartnerCentralSandboxFullAccess` policy to your IAM identities.

This policy grants access for developer testing in the Sandbox catalog.

 To view the permissions for this policy, see [AWSPartnerCentralSandboxFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralSandboxFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy`
<a name="security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy"></a>

You can attach the `AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy` policy to your IAM identities.

This policy provides the ResourceSnapshotJob with permission to read a resource and snapshot it in the target environment. For more information on how to use this policy, see [Working with multi-partner opportunities](https://docs.aws.amazon.com/partner-central/latest/APIReference/working-with-multi-partner-opportunities.html#creating-custom-policy-resourcesnapshotjobrole) in the *AWS Partner Central API Reference*.

 To view the permissions for this policy, see [AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralChannelManagement`
<a name="security-iam-awsmanpol-AWSPartnerCentralChannelManagement"></a>

You can attach the `AWSPartnerCentralChannelManagement` policy to your IAM identities.

With this policy, you can manage channel programs and partner relationships in AWS Partner Central. This policy allows the following operations:
+ View and manage channel relationships
+ Manage channel handshakes
+ View and manage channel contracts
+ View and manage distribution engagement requests
+ Access Guides and the AWS assistant (Partner Assistant)
+ Create, view, search, reply to, and resolve Support cases, add attachments to them, and view them in the Support Center console. This access applies to every Support case in the account, not only cases about AWS Partner Central.

 To view the permissions for this policy, see [AWSPartnerCentralChannelManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralChannelManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralChannelHandshakeApprovalManagement`
<a name="security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement"></a>

You can attach the `AWSPartnerCentralChannelHandshakeApprovalManagement` policy to your IAM identities.

This policy grants access to channel handshake approval management activities in AWS Partner Central.

 To view the permissions for this policy, see [AWSPartnerCentralChannelHandshakeApprovalManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralChannelHandshakeApprovalManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralMarketingManagement`
<a name="security-iam-awsmanpol-AWSPartnerCentralMarketingManagement"></a>

You can attach the `AWSPartnerCentralMarketingManagement` policy to your IAM identities.

With this policy, you can manage marketing activities and promotional content in AWS Partner Central. This policy allows the following operations:
+ Access and manage Marketing Central campaigns and content
+ Create and manage case studies
+ Access Badge Manager, Guides, and the AWS assistant (Partner Assistant)
+ Create, view, search, reply to, and resolve Support cases, add attachments to them, and view them in the Support Center console. This access applies to every Support case in the account, not only cases about AWS Partner Central.

 To view the permissions for this policy, see [AWSPartnerCentralMarketingManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralMarketingManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `PartnerCentralIncentiveBenefitManagement`
<a name="security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement"></a>

You can attach the `PartnerCentralIncentiveBenefitManagement` policy to your IAM identities.

With this policy, you can manage incentive benefits, funding, and claims in AWS Partner Central. This policy allows the following operations:
+ Create and manage fund requests and claims
+ View historical fund requests
+ View funding wallets
+ Access Guides and the AWS assistant (Partner Assistant)
+ Create, view, search, reply to, and resolve Support cases, add attachments to them, and view them in the Support Center console. This access applies to every Support case in the account, not only cases about AWS Partner Central.
+ Create and manage program applications

 To view the permissions for this policy, see [PartnerCentralIncentiveBenefitManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/PartnerCentralIncentiveBenefitManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerProServeToolsFullAccess`
<a name="security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess"></a>

You can attach the `AWSPartnerProServeToolsFullAccess` policy to your IAM identities.

This policy grants full access to AWS ProServe Tools (A2T and MPA) via AWS Partner Central Single Sign-On. It includes all assessment roles — individual contributor, organization reader, organization contributor, and organization admin — enabling complete access to create, read, update, and share assessments across the organization, as well as manage organization-level settings.

**Roles granted:**
+ AssessmentIndividualContributor
+ AssessmentOrganizationReader
+ AssessmentOrganizationContributor
+ OrganizationAdmin

 To view the permissions for this policy, see [AWSPartnerProServeToolsFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerProServeToolsFullAccess.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerProServeToolsOrganizationReaderIndividualContributor`
<a name="security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor"></a>

You can attach the `AWSPartnerProServeToolsOrganizationReaderIndividualContributor` policy to your IAM identities.

This policy grants read access to all organizational assessments in A2T, combined with the ability to create and manage the user's own assessments in both A2T and MPA. It is intended for users who need visibility into team assessments while retaining the ability to manage their own work.

**Note**  
MPA does not support read-only mode. Users assigned this policy will retain read/write access to their own MPA assessments.

**Roles granted:**
+ AssessmentIndividualContributor
+ AssessmentOrganizationReader

 To view the permissions for this policy, see [AWSPartnerProServeToolsOrganizationReaderIndividualContributor](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerProServeToolsOrganizationReaderIndividualContributor.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerProServeToolsIndividualContributor`
<a name="security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor"></a>

You can attach the `AWSPartnerProServeToolsIndividualContributor` policy to your IAM identities.

This policy grants the minimum permissions required to access AWS ProServe Tools via AWS Partner Central Single Sign-On. Users can create, read, update, and share their own assessments in both A2T and MPA. Access is scoped to assessments created by the user's own IAM identity (role or user ARN).

**Roles granted:**
+ AssessmentIndividualContributor

 To view the permissions for this policy, see [AWSPartnerProServeToolsIndividualContributor](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerProServeToolsIndividualContributor.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralRevenueAttributionManagement`
<a name="security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement"></a>

You can attach the `AWSPartnerCentralRevenueAttributionManagement` policy to your IAM identities.

This policy provides necessary access for revenue attribution management activities. It is intended for AWS accounts registered with AWS Partner Central.

This policy grants access to the following capabilities:
+ Create, retrieve, update, and list Revenue Attribution resources and their allocations.
+ Create, retrieve, and list Marketplace Revenue Share resources and their allocations.
+ Tag and untag Revenue Attribution and Marketplace Revenue Share resources.
+ Create, view, search, reply to, and resolve Support cases, add attachments to them, and view them in the Support Center console. This access applies to every Support case in the account, not only cases about AWS Partner Central.

 To view the permissions for this policy, see [AWSPartnerCentralRevenueAttributionManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralRevenueAttributionManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSRevenueAttributionManagement`
<a name="security-iam-awsmanpol-AWSRevenueAttributionManagement"></a>

You can attach the `AWSRevenueAttributionManagement` policy to your IAM identities.

This policy provides necessary access for revenue attribution management activities. It is intended for AWS accounts who are not registered with AWS Partner Central.

This policy grants access to the following capabilities:
+ Create, retrieve, update, and list Revenue Attribution resources.
+ Tag and untag Revenue Attribution resources.

 To view the permissions for this policy, see [AWSRevenueAttributionManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSRevenueAttributionManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralBusinessPlanManagement`
<a name="security-iam-awsmanpol-AWSPartnerCentralBusinessPlanManagement"></a>

You can attach the `AWSPartnerCentralBusinessPlanManagement` policy to your IAM identities.

This policy provides full access to business plans in AWS Partner Central, including the reporting data behind business plan metrics. You can attach it on its own or with other AWS Partner Central managed policies.

This policy grants access to the following capabilities:
+ Create, view, update, submit, and cancel business plans in the AWS and Sandbox catalogs
+ Create, view, update, and delete business plan items, and link them to opportunities or campaigns
+ Upload, import, view, and delete business plan attachments
+ Tag and untag business plans
+ Turn AWS collaboration on or off
+ View the AWS Partner Central and AWS Marketplace reporting data that business plan metrics use

This policy doesn't grant permission to create the business plan service-linked role. For more information, see [Managing service-linked roles for business plans](using-roles-for-partner-central-account.md).

 To view the permissions for this policy, see [AWSPartnerCentralBusinessPlanManagement](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralBusinessPlanManagement.html) in the *AWS Managed Policy Reference*.

## AWS managed policy: `AWSPartnerCentralAccountManagementServiceRolePolicy`
<a name="security-iam-awsmanpol-AWSPartnerCentralAccountManagementServiceRolePolicy"></a>

You can't attach `AWSPartnerCentralAccountManagementServiceRolePolicy` to your AWS Identity and Access Management (IAM) entities. The `AWSServiceRoleForPartnerCentralAccount` service-linked role uses this policy. Your AWS partner development team uses this role to update your business plans after you turn on AWS collaboration. For more information, see [Managing service-linked roles for business plans](using-roles-for-partner-central-account.md).

This policy grants access to the following capabilities:
+ Create, update, and cancel business plans
+ Create, update, and delete business plan items
+ Start and cancel business plan submission tasks
+ Import and delete business plan attachments

These actions apply only to business plans in the same AWS account as the role, and only while you have AWS collaboration turned on (`partnercentral:AllowAwsEngagement` is `ENABLED`). The policy grants no read actions.

 To view the permissions for this policy, see [AWSPartnerCentralAccountManagementServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralAccountManagementServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## AWS Partner Central updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Partner Central since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the AWS Partner Central [Document history for the AWS Partner Central Getting Started Guide](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement) — Update to an existing policy | AWS Partner Central added permissions to create, view, list, and cancel channel contracts. A channel contract is an agreement between a partner and AWS under an AWS program. With these permissions, users can request, view, list, and cancel the channel contracts in their account. | November 20, 2026 | 
| [AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement) — Update to an existing policy | AWS Partner Central added permissions to create, view, search, reply to, and resolve Support cases, add attachments to them, and to view them in the Support Center console. These permissions apply to every Support case in the account, not only cases about AWS Partner Central. | November 19, 2026 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central added permissions to create, view, search, reply to, and resolve Support cases, add attachments to them, and to view them in the Support Center console. These permissions apply to every Support case in the account, not only cases about AWS Partner Central. | November 19, 2026 | 
| [PartnerCentralIncentiveBenefitManagement](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement) — Update to an existing policy | AWS Partner Central added permissions to create, view, search, reply to, and resolve Support cases, add attachments to them, and to view them in the Support Center console. These permissions apply to every Support case in the account, not only cases about AWS Partner Central. Updated the partnercentral:ListPartners permission so that users can list the partner account. | November 19, 2026 | 
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement) — Update to an existing policy | AWS Partner Central added permissions to create, view, search, reply to, and resolve Support cases, add attachments to them, and to view them in the Support Center console. These permissions apply to every Support case in the account, not only cases about AWS Partner Central. | November 19, 2026 | 
| [AWSPartnerCentralRevenueAttributionManagement](#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement) — Update to an existing policy | AWS Partner Central added permissions to create, view, search, reply to, and resolve Support cases, add attachments to them, and to view them in the Support Center console. These permissions apply to every Support case in the account, not only cases about AWS Partner Central. | November 19, 2026 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) — Update to an existing policy | AWS Partner Central added permissions to search Support cases, and to view them in the Support Center console. These permissions apply to every Support case in the account, not only cases about AWS Partner Central or AWS Marketplace. | November 19, 2026 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy to add customer account and customer account bulk job access, and tagging access for customer accounts. | November 18, 2026 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy to add search engagements and list engagement groups access. | November 18, 2026 | 
| [AWSPartnerCentralBusinessPlanManagement](#security-iam-awsmanpol-AWSPartnerCentralBusinessPlanManagement)—New policy | AWS Partner Central added a new policy that provides full access to business plans, including the reporting data behind business plan metrics. | November 10, 2026 | 
| [AWSPartnerCentralAccountManagementServiceRolePolicy](#security-iam-awsmanpol-AWSPartnerCentralAccountManagementServiceRolePolicy) — New policy | AWS Partner Central now includes a new policy for the AWSServiceRoleForPartnerCentralAccount service-linked role. After you turn on AWS collaboration, your AWS partner development team can create and update your business plans. | October 30, 2026 | 
| [AWSPartnerCentralRevenueAttributionManagement](#security-iam-awsmanpol-AWSPartnerCentralRevenueAttributionManagement) — New policy | AWS Partner Central added a new policy to provide necessary access for revenue attribution management activities for partners. | June 30, 2026 | 
| [AWSRevenueAttributionManagement](#security-iam-awsmanpol-AWSRevenueAttributionManagement) — New policy | AWS Partner Central added a new policy to provide necessary access for revenue attribution management activities for customers. | June 30, 2026 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy to add prospecting actions access. | June 16, 2026 | 
| [AWSPartnerProServeToolsFullAccess](#security-iam-awsmanpol-AWSPartnerProServeToolsFullAccess) — New policy | AWS Partner Central added a new policy to grant full access to AWS ProServe Tools (A2T and MPA) via AWS Partner Central Single Sign-On with all assessment roles. | March 23, 2026 | 
| [AWSPartnerProServeToolsOrganizationReaderIndividualContributor](#security-iam-awsmanpol-AWSPartnerProServeToolsOrganizationReaderIndividualContributor) — New policy | AWS Partner Central added a new policy to grant read access to organizational assessments in A2T and manage own assessments in both A2T and MPA. | March 23, 2026 | 
| [AWSPartnerProServeToolsIndividualContributor](#security-iam-awsmanpol-AWSPartnerProServeToolsIndividualContributor) — New policy | AWS Partner Central added a new policy to grant minimum permissions to access AWS ProServe Tools and manage own assessments. | March 23, 2026 | 
| [PartnerCentralIncentiveBenefitManagement](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement) — Update to an existing policy | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol. | March 13, 2026 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol. | March 13, 2026 | 
| [AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess) — Update to an existing policy | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol. | March 13, 2026 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) — Update to an existing policy | AWS Partner Central updated a policy to add Partner Central Agents session management capability through the Model Context Protocol. | March 13, 2026 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality. | February 23, 2026 | 
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement) — Update to an existing policy | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality. | February 23, 2026 | 
| [AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement) — Update to an existing policy | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality. | February 23, 2026 | 
| [PartnerCentralIncentiveBenefitManagement](#security-iam-awsmanpol-PartnerCentralIncentiveBenefitManagement) — New policy | AWS Partner Central added a new policy to grant access to all the incentive benefits functionality. | February 11, 2026 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) — Update to an existing policy | AWS Partner Central updated a policy to add Amazon Q permissions for Partner Assistant chatbot functionality and to add AWS Marketplace Agreements read access for MPOPP benefits functionality. | February 4, 2026 | 
| [AWSPartnerCentralMarketingManagement](#security-iam-awsmanpol-AWSPartnerCentralMarketingManagement) — New policy | AWS Partner Central added a new policy to grant access to manage partner central marketing and campaigns. | November 30, 2025 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) — Update to an existing policy | AWS Partner Central updated a policy to add legacy Partner Central access, put files into S3, and get AWS Marketplace entities. | November 30, 2025 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy to add engagement context access, opportunity from engagement task access, and legacy Partner Central access, get dashboard, collaboration channel access, get partner, and tag opportunity and resource snapshot jobs. | November 30, 2025 | 
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement) — Update to an existing policy | AWS Partner Central updated a policy to add legacy Partner Central access, get dashboard, and get partner. | November 30, 2025 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) — Update to an existing policy | AWS Partner Central updated a policy to add Channel billing transfer role access. | November 19, 2025 | 
| [AWSPartnerCentralChannelManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelManagement) — New policy | AWS Partner Central added a new policy to grant access to manage channel management activities. | November 19, 2025 | 
| [AWSPartnerCentralChannelHandshakeApprovalManagement](#security-iam-awsmanpol-AWSPartnerCentralChannelHandshakeApprovalManagement) — New policy | AWS Partner Central added a new policy to grant access to channel handshake approval management activities. | November 19, 2025 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) — Update to an existing policy | AWS Partner Central updated a policy. | December 4, 2024 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — Update to an existing policy | AWS Partner Central updated a policy. | December 4, 2024 | 
| [AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess) — Update to an existing policy | AWS Partner Central updated a policy. | December 4, 2024 | 
| [AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy](#security-iam-awsmanpol-AWSPartnerCentralSellingResourceSnapshotJobExecutionRolePolicy) — New policy | AWS Partner Central added a new policy to grant access to read resources and create snapshots. | December 4, 2024 | 
| [AWSPartnerCentralFullAccess](#security-iam-awsmanpol-AWSPartnerCentralFullAccess) – New policy | AWS Partner Central added a new policy to grant full access to the AWS Partner Central service. | November 18, 2024 | 
| [AWSPartnerCentralOpportunityManagement](#security-iam-awsmanpol-AWSPartnerCentralOpportunityManagement) — New policy | AWS Partner Central added a new policy to grant full access to manage opportunities in AWS Partner Central. | November 14, 2024 | 
| [AWSPartnerCentralSandboxFullAccess](#security-iam-awsmanpol-AWSPartnerCentralSandboxFullAccess) — New policy | AWS Partner Central added a new policy to grant access for developer testing in the Sandbox catalog. | November 14, 2024 | 
| AWS Partner Central started tracking changes | AWS Partner Central started tracking changes for its AWS managed policies. | November 14, 2024 | 