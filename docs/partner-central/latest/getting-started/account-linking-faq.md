# Account linking FAQ

The following topics answer frequently asked questions about linking AWS Partner Central
accounts with other AWS accounts.

Alliance Leads and Cloud Admins can link accounts, but only after an IAM administrator completes the
[prerequisites](linking-prerequisites.md "linking-prerequisites.md").

Alliance Leads can delegate linking by assigning Cloud Admin roles to existing users. For more information, refer to
[Managing user roles and assignments](managing-user-roles-and-assignments.md "managing-user-roles-and-assignments.md") later in this guide.

Identify an IAM administrator with console access to your target AWS account.
The IAM administrator must complete the
[prerequisites](linking-prerequisites.md "linking-prerequisites.md") before you initiate linking.

IAM administrators typically work in IT security, information security, or dedicated IAM teams. They implement policies,
configure SSO, handle compliance reviews, and maintain access controls.

Starting November 15, 2025, you must have a Paid account plan to renew your APN membership. On that date, AWS begins processing APN fee billings only for
Partner Central accounts with linked AWS accounts at renewal.
For more information, refer to
[APN Fee Requirement Change for 2025](https://partnercentral.awspartner.com/partnercentral2/s/newsletter?url=APN-Fee-Requirement-Changes-for-2025 "https://partnercentral.awspartner.com/partnercentral2/s/newsletter?url=APN-Fee-Requirement-Changes-for-2025").
Marketplace sellers also need paid accounts for service usage.

You can unlink an AWS account, but doing so creates data persistence issues and requires manual reconciliation efforts.
For more information about unlinking AWS accounts, refer to [Unlinking AWS Partner Central and AWS
accounts](unlinking-apc-aws-marketplace.md "unlinking-apc-aws-marketplace.md") earlier in this guide.

Coordinate with your IAM administrator to identify the team responsible for account approval and provisioning.
For instructions on setting up an AWS account, refer to [Create an AWS account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md") in the
_AWS Account Management Reference Guide_. Be sure to select the
[Paid account plan](../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md "../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md").

Your IAM administrator should know the team responsible for account approval
and provisioning. For information about setting up a new AWS account, refer to
[Create an AWS
account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md") in the _AWS Account Management Reference
Guide_. During that process, be sure to select the **Paid
account plan**. For more information about account plans, refer to
[Choosing an AWS
Free Tier plan](../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md "../../../awsaccountbilling/latest/aboutv2/free-tier-plans.md") in the _AWS Billing User Guide_.

You use AWS managed policies for the account linking
prerequisites. By default, account linking uses AWS managed policies to assign IAM roles during account linking. However, IT admins can use custom
AWS Marketplace policies to assign IAM roles to AWS Partner Central users such as an ACE team. The roles enable users to link ACE opportunities with AWS Marketplace private offers.
For more information, refer to [Using custom policies to map users](user-role-mapping.md "user-role-mapping.md") later in this guide.

The links in the following list take you to the _AWS Managed Policy
Reference_.

###### AWS managed policies

- [AWSPartnerCentralFullAccess:](../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess.md") –
  Provides full access to AWS Partner Central; features and related AWS
  services.
- [AWSPartnerCentralOpportunityManagement:](../../../aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.md "../../../aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement.md")
  – Provides necessary access for opportunity management activities.
- [AWSMarketplaceSellerOfferManagement:](../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement.md "../../../aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement.md")
  – Enables seller access to offer and agreement management activities.
  For more information about the AWS Partner Central managed policies, refer to [AWS managed policies for AWS Partner Central users](managed-policies.md "managed-policies.md") later in this
  guide.

For more information about the AWS Marketplace managed policy, refer to [AWS managed policies for AWS Marketplace sellers](../../../marketplace/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-awsmarketplaceselleroffermanagement "../../../marketplace/latest/userguide/security-iam-awsmanpol.md#security-iam-awsmanpol-awsmarketplaceselleroffermanagement") in the _AWS Marketplace Seller
Guide_.

###### Custom AWS Marketplace policies

- `aws-marketplace:ListEntities` and
  `aws-marketplace:SearchAgreements` – Enables users to
  link ACE opportunities and AWS Marketplace private offers.
- `aws-marketplace:GetSellerDashboard:` – Grants access to
  the AWS Partner Central & Marketplace dashboard.
  For more information about the custom AWS Marketplace policies, refer to [Policies and permissions for AWS Marketplace sellers](../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions "../../../marketplace/latest/userguide/detailed-management-portal-permissions.md#seller-ammp-permissions") in the _AWS Marketplace
  Seller Guide_.

You must have the alliance lead or cloud admin _role_, not the
privileges.

Follow the steps in [Unlinking AWS Partner Central and AWS
accounts](unlinking-apc-aws-marketplace.md "unlinking-apc-aws-marketplace.md") earlier in this guide.

If you unlink and re-link to a different AWS Marketplace seller or AWS account, linked
objects disappear. If a partner re-links to the same AWS Marketplace seller or AWS account,
linked objects remain.

Alliance leads use AWS Partner Central User Management to assign IAM roles to
AWS Partner Central users and grant them access to a linked account. They can also
remove the mapped roles to remove access a linked account.

In addition, each standard IAM role created during account linking comes with
limited permissions. For more information about them, refer to [Understanding the role permissions](linking-prerequisites.md#standard-role-permissions "linking-prerequisites.md#standard-role-permissions")
earlier in this guide.

You use that option to bulk assign IAM roles to the Alliance, Cloud Admin, and
ACE teams. The linking process creates the roles. Partners can use the IAM console
to delete unwanted roles.

For more information, refer to [Updated Account Linking User Guide](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources "https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources") in AWS Partner Central.

Ensure you submitted an accurate account name. The AWS ID you select may already
be in use, and it cannot be shared by multiple parties, especially if your company
is merging. For guidance on what to during a merger, refer to:

- [AWS Partners M&A Policy and FAQs](https://partnercentral.awspartner.com/partnercentral2/s/resources?sfdc.tabName=01r8a000001A846&Id=kA08W000000BiR2SAK "https://partnercentral.awspartner.com/partnercentral2/s/resources?sfdc.tabName=01r8a000001A846&Id=kA08W000000BiR2SAK")
- [How do I merge AWS Partner Central accounts?](https://partnercentral.awspartner.com/partnercentral2/s/resources?sfdc.tabName=01r8a000001A846&Id=kA08W000000BiR2SAK "https://partnercentral.awspartner.com/partnercentral2/s/resources?sfdc.tabName=01r8a000001A846&Id=kA08W000000BiR2SAK")
  The messages appear for the following reasons:

- An AWS Partner Central user wasn't mapped to an IAM role. Ask the alliance
  lead or cloud admin to map the appropriate role to the user. For more
  information, refer to the [AWS Partner Central & AWS account linking guide](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources "https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources").
- AWS Partner Central users with mapped IAM roles need to update their
  existing policies. For more information about the latest prerequisites,
  refer to [Prerequisites](linking-prerequisites.md "linking-prerequisites.md") earlier in this guide.
  Yes, but you must link accounts first. You use AWS Partner Central to associate AWS Marketplace private offers with ACE opportunities.
  You use **Partner Connections** to associate Channel Partner private
  offers with ACE opportunities. Both methods require account linking before you can use them. For more information, refer to [Partner
  Connections](../sales-guide/partner-connections.md "../sales-guide/partner-connections.md") in the _AWS Partner Central Sales
  Guide_.
