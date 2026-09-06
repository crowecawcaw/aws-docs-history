

# Account linking FAQ
<a name="account-linking-faq"></a>

The following topics answer frequently asked questions about linking AWS Partner Central accounts with other AWS accounts.

## Who can link AWS Partner Central and AWS accounts?
<a name="who-can-link"></a>

Alliance Leads and Cloud Admins can link accounts, but only after an IAM administrator completes the [prerequisites](https://docs.aws.amazon.com/partner-central/latest/getting-started/linking-prerequisites.html). 

Alliance Leads can delegate linking by assigning Cloud Admin roles to existing users. For more information, refer to [Managing user roles and assignments](https://docs.aws.amazon.com/partner-central/latest/getting-started/managing-user-roles-and-assignments.html) later in this guide. 

## Is there any technical effort required, and what should I plan for?
<a name="effort-required"></a>

Identify an IAM administrator with console access to your target AWS account. The IAM administrator must complete the [prerequisites](https://docs.aws.amazon.com/partner-central/latest/getting-started/linking-prerequisites.html) before you initiate linking.

## Who is my IAM administrator?
<a name="who-is-admin"></a>

IAM administrators typically work in IT security, information security, or dedicated IAM teams. They implement policies, configure SSO, handle compliance reviews, and maintain access controls.

## Why do we need to have a Paid account to link AWS Partner Central and AWS accounts?
<a name="why-paid"></a>

Starting November 15, 2025, you must have a Paid account plan to renew your APN membership. On that date, AWS begins processing APN fee billings only for Partner Central accounts with linked AWS accounts at renewal. For more information, refer to [APN Fee Requirement Change for 2025](https://partnercentral.awspartner.com/partnercentral2/s/newsletter?url=APN-Fee-Requirement-Changes-for-2025). Marketplace sellers also need paid accounts for service usage.

## Can I unlink and re-link a new account, if I do not want to use my existing linked account as my primary account?
<a name="unlink-relink"></a>

You can unlink an AWS account, but doing so creates data persistence issues and requires manual reconciliation efforts. For more information about unlinking AWS accounts, refer to [Unlinking AWS Partner Central and AWS accounts](unlinking-apc-aws-marketplace.md) earlier in this guide.

## I don't have an AWS account that I can use for APN engagement. How do I create one?
<a name="dedicated-aws-acct"></a>

Coordinate with your IAM administrator to identify the team responsible for account approval and provisioning. For instructions on setting up an AWS account, refer to [Create an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) in the *AWS Account Management Reference Guide*. Be sure to select the [Paid account plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html).

## How do I provision a new AWS account?
<a name="provision-aws-acct"></a>

 Your IAM administrator should know the team responsible for account approval and provisioning. For information about setting up a new AWS account, refer to [Create an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) in the *AWS Account Management Reference Guide*. During that process, be sure to select the **Paid account plan**. For more information about account plans, refer to [Choosing an AWS Free Tier plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans.html) in the *AWS Billing User Guide*. 

## Which IAM policies should I use?
<a name="which-policies"></a>

You use AWS managed policies for the account linking prerequisites. By default, account linking uses AWS managed policies to assign IAM roles during account linking. However, IT admins can use custom AWS Marketplace policies to assign IAM roles to AWS Partner Central users such as an ACE team. The roles enable users to link ACE opportunities with AWS Marketplace private offers. For more information, refer to [Using custom policies to map users](user-role-mapping.md) later in this guide.

The links in the following list take you to the *AWS Managed Policy Reference*.

**AWS managed policies**
+  [AWSPartnerCentralFullAccess:](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralFullAccess) – Provides full access to AWS Partner Central; features and related AWS services. 
+  [AWSPartnerCentralOpportunityManagement:](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSPartnerCentralOpportunityManagement) – Provides necessary access for opportunity management activities. 
+  [AWSMarketplaceSellerOfferManagement:](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSMarketplaceSellerOfferManagement) – Enables seller access to offer and agreement management activities. 

For more information about the AWS Partner Central managed policies, refer to [AWS managed policies for AWS Partner Central users](managed-policies.md) later in this guide.

For more information about the AWS Marketplace managed policy, refer to [AWS managed policies for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awsmarketplaceselleroffermanagement) in the *AWS Marketplace Seller Guide*. 

**Custom AWS Marketplace policies**
+  `aws-marketplace:ListEntities` and `aws-marketplace:SearchAgreements` – Enables users to link ACE opportunities and AWS Marketplace private offers. 
+  `aws-marketplace:GetSellerDashboard:` – Grants access to the AWS Partner Central & Marketplace dashboard. 

For more information about the custom AWS Marketplace policies, refer to [ Policies and permissions for AWS Marketplace sellers](https://docs.aws.amazon.com/marketplace/latest/userguide/detailed-management-portal-permissions.html#seller-ammp-permissions) in the *AWS Marketplace Seller Guide*.

## Why can’t I complete account linking? I have alliance lead privileges
<a name="cant-finish-linking"></a>

You must have the alliance lead or cloud admin *role*, not the privileges.

## How do I unlink accounts?
<a name="unlink"></a>

Follow the steps in [Unlinking AWS Partner Central and AWS accounts](unlinking-apc-aws-marketplace.md) earlier in this guide.

## What happens to linked ACE opportunities \+ MPPO if I unlink an account?
<a name="unlink-ace"></a>

If you unlink and re-link to a different AWS Marketplace seller or AWS account, linked objects disappear. If a partner re-links to the same AWS Marketplace seller or AWS account, linked objects remain.

## How can I manage partner user access to a linked account?
<a name="manage-partner-user-access"></a>

Alliance leads use AWS Partner Central User Management to assign IAM roles to AWS Partner Central users and grant them access to a linked account. They can also remove the mapped roles to remove access a linked account.

In addition, each standard IAM role created during account linking comes with limited permissions. For more information about them, refer to [Understanding the role permissions](linking-prerequisites.md#standard-role-permissions) earlier in this guide.

## Selecting the PartnerCentralAceRole checkbox created 3 roles. Why?
<a name="all-roles"></a>

You use that option to bulk assign IAM roles to the Alliance, Cloud Admin, and ACE teams. The linking process creates the roles. Partners can use the IAM console to delete unwanted roles.

For more information, refer to [ Updated Account Linking User Guide](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources) in AWS Partner Central.

## Why can't we register our legal business name during account linking?
<a name="register-legal-name"></a>

Ensure you submitted an accurate account name. The AWS ID you select may already be in use, and it cannot be shared by multiple parties, especially if your company is merging. For guidance on what to during a merger, refer to:
+ [AWS Partners M&A Policy and FAQs](https://partnercentral.awspartner.com/partnercentral2/s/resources?sfdc.tabName=01r8a000001A846&Id=kA08W000000BiR2SAK) 
+  [How do I merge AWS Partner Central accounts?](https://partnercentral.awspartner.com/partnercentral2/s/resources?sfdc.tabName=01r8a000001A846&Id=kA08W000000BiR2SAK) 

## Why do I get the “Missing IAM Role Mapping”, “Missing Permission”, “Access denied”, and “Your AWS Marketplace IAM role does not have the required permissions” errors?
<a name="mapping-errors"></a>

The messages appear for the following reasons:
+ An AWS Partner Central user wasn't mapped to an IAM role. Ask the alliance lead or cloud admin to map the appropriate role to the user. For more information, refer to the [AWS Partner Central & AWS account linking guide](https://partnercentral.awspartner.com/partnercentral2/s/article?article=AWS-Partner-Central&category=Introductory_resources). 
+ AWS Partner Central users with mapped IAM roles need to update their existing policies. For more information about the latest prerequisites, refer to [Prerequisites](linking-prerequisites.md) earlier in this guide. 

## Can I associate AWS Marketplace private offers and Channel Partner private offers with ACE opportunities?
<a name="link-private"></a>

Yes, but you must link accounts first. You use AWS Partner Central to associate AWS Marketplace private offers with ACE opportunities. You use **Partner Connections** to associate Channel Partner private offers with ACE opportunities. Both methods require account linking before you can use them. For more information, refer to [Partner Connections](https://docs.aws.amazon.com/partner-central/latest/sales-guide/partner-connections.html) in the *AWS Partner Central Sales Guide*.