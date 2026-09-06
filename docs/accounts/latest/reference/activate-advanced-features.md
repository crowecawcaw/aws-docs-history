

# Activate advanced AWS features
<a name="activate-advanced-features"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

When you activate advanced features, you take complete control of the AWS Organization, management account, and delegated administrator account that are used to manage the projects you created and team members you invited. You will directly manage the security, governance, and team membership of your AWS environment. You have access to additional AWS services, multi-Region capabilities, and enhanced administrative and billing controls.

You must upgrade your account before you activate advanced features. For more information, see [Upgrade your account in AWS Settings](upgrade-account.md).

## What happens when you activate advanced features
<a name="activate-advanced-features-what-happens"></a>

When you activate advanced features, the following changes will immediately be applied to your management account and the AWS Organization that contains your projects:
+ You are now the administrator of the AWS organization that contains your projects.
+ You manage your projects as member accounts in your organization. As the administrator of this organization, you can create member accounts in the organization.
+ To give member accounts that you invite to join your organization an administrator role, you must create an OrganizationAccountAccessRole. For more information, see [Creating the OrganizationAccountAccessRole in an invited member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create-cross-account-role.html).
+ Your team members are referred to as workforce identities and they can still access your AWS accounts. You can also choose to customize the identity source of your workforce using IAM Identity Center. You can continue to use AWS Builder ID as the identity source, or you can change this to an external identity source. If you change your identity source from AWS Builder ID to another identity source, it is irreversible. You can't re-enable AWS Builder ID as an identity source in the future. For more information, see [Change identity source from AWS Builder ID](change-identity-source.md).
+ You control AWS access for users and groups in your IAM Identity Center organization instance using Account access manager. You can use this feature to modify user access, while still allowing your users to sign in using `aws login` to receive their IAM role session credentials from the browser. For more information, see [AWS Account Access Manager](https://docs.aws.amazon.com/IAM/latest/UserGuide/account-access-manager.html).
+ AWS creates a member account called Identity Delegated Admin in your organization with a delegated administrator role. This role is used to perform most administrative tasks in the IAM Identity Center and account access manager. The delegated administrator role must be used in US East (N. Virginia). For more information, see [Delegated administration](https://docs.aws.amazon.com/singlesignon/latest/userguide/delegated-admin.html).
+ You can now configure Resource Control Policies (RCPs) and Service Control Policies (SCPs) to enforce custom guardrails in your organization. Previously, AWS managed RCPs and SCPs on your behalf. You can modify those policies after you activate advanced features. For more information, see [Remove organization policies](remove-org-policies.md).

When you activate advanced features, the following changes are also applied to your AWS organization:
+ If you have a spend limit for any of your AWS accounts, it is removed. You cannot create a spend limit if you activate advanced features. Instead, you have access to the entire suite of Billing and Cost Management Tools. This includes setting budgets, downloading cost explorer reports, and detecting unusual spend with AWS Cost Anomaly Detection. You can use these advanced tools to analyze, organize, plan, and optimize your costs.
+ You can access all AWS services. The available services are listed in [AWS services not supported for our new AWS experience](supported-services-sign-up-new.md#unsupported-services). You should plan your architecture and consult the service documentation before enabling these services. In addition, Agent Toolkit provides many [skills](https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills) to work with these services.
+ You gain access to additional AWS Regions, opt-in Regions, and access to multi-Region capabilities. Multi-Region architecture improves resilience for your workloads. We recommend that you plan for how you will constrain and audit your regional footprint. It's important to ensure that resources you create are only present in the Regions you intend to use.
+ You can turn off IAM role manager for each AWS account in your organization. IAM role manager is an optional account setting that automatically provisions roles, so you and your workforce don't need to set them up. For more information, see [How to enable and disable role manager (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_role-manager.html#id_roles_create_role-manager_enable-disable).
+ You can use [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html).

When you activate advanced features, the following changes are also applied to your user experience:
+ Previously, the AWS Management Console showed a simplified view with a menu that you used to change between projects and access AWS Settings. The AWS Management Console expands to include additional features such as Region selector, additional services, and setting a color for account that you can access to visibly distinguish between them. For more information, see [Console features](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html#console-features).
+ You can now also do the following:
  + Disable multi-session console support.
  + Designate your AWS account as HIPAA or SEC compliant.
  + Use AWS Marketplace.
  + Earn extra credits from AWS Activate.
  + Work with an AWS Training Partner.
  + Purchase an AWS Skill Builder Team subscription.
  + Enroll in an Enterprise Agreement with AWS.
  + Create a Professional Services contract.
  + Join AWS Partner Network.

## How will AWS Settings change after I activate advanced features?
<a name="activate-advanced-features-settings-change"></a>

After you activate advanced features, AWS Settings will be available as long as you use AWS Builder ID as your identity source. AWS Settings will only be accessible from [https://settings.aws.com](https://settings.aws.com). You won't be able to access it from the AWS Management Console. AWS Settings will provide links to manage your account using your management account. With your management account, you can access the following AWS Management Console locations from AWS Settings. Only use the management account to perform administrative tasks that require root-level permissions, including:
+ Access the Billing and Cost Management Console to view your billing information.
+ Access the AWS Organization console to modify the SCPs and RCPs that govern your organization.
+ Access the AWS Account Access Manager console to modify the fine grain access for your workforce identities.
+ Access the IAM Identity Center to change your identity source.

You can also use AWS Settings to access your AWS accounts in your organization, and any project shared with you.

If you want to create custom roles and access them from AWS Settings in your accounts, you must set the session length to 12 hours.

If you have team member access to a project, you can view and access it in the same way as before you activated advanced features. Any projects shared with you are not impacted if you activate advanced features for your own management account and AWS organization.

## Can I still create a project in AWS Settings after I activate advanced features?
<a name="activate-advanced-features-create-project"></a>

You cannot create a project in your current AWS Organization after you activate advanced features. You must create a member account in your organization.

You can create a new managed AWS Organization with preconfigured defaults. To do this, create a new project in AWS Settings. You can then create additional projects and invite team members to collaborate. You can activate advanced features for this management account as well.

The new preconfigured environment that you access will have no connection to the previous AWS organization that was created when you first signed up for AWS.

## How to prepare to activate advanced features
<a name="activate-advanced-features-prepare"></a>

We recommend doing the following before you activate advanced features:
+ Inform all your team members that you will be activating advanced features. Unless you modify any settings, your team members will have the same access to the projects, but the AWS Management Console changes from the simplified view to a view that shows Regions and provides access to more services. If you later change the identity source or add new SCPs or RCPs, inform your workforce since those changes can affect how they sign in and what they can access.
+ View the spend for all your current projects and note if any projects contain costs that significantly fluctuate. Without a spend limit, you will be responsible for all costs incurred by your resources. We recommend that you delete or pause idle resources before you activate advanced features.
+ Plan what changes you'll be making to your AWS organizations and research best practices. If you plan on creating resources in a different AWS Region, modify the service control policy that is applied for all users to restrict AWS Regions. You need to modify the statementID for `RegionFloor` to include any new Regions. For more information, see [Service control policies for projects](scps-and-rcps-for-projects.md#scps-for-projects).
+ If you followed the steps in [Connect an AI coding tool](connect-ai-coding-tool.md), your AI tool has context only about the new AWS experience. This can cause problems as you develop using advanced features. We recommend the following:
  + Remove the `aws-starter-rules.md` file from the location you saved it. The rules file was saved depending on your agent. For more information, see [Where to put the rules file](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/rules-files.html#rules-file-location).

## How to activate advanced features
<a name="activate-advanced-features-how-to"></a>

You can activate advanced features in AWS Settings. Activation cannot be reversed.

**To activate advanced features**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Projects**.

1. For **Actions**, choose **Explore advanced features**.

   Because activation cannot be reversed, we'll provide more time to explore and learn about the activation process.

1. When you are ready to activate, do the following:

   1. For **Team name**, enter a team name. This is the name of the IAM Identity Center instance used to store your workforce identities. Your workforce will see this name.

   1. For **Choose management account email address**, choose an email address. This email address is used to access the management account and perform tasks that require root-level permissions. If you use a different email address, the AWS Builder ID email will still have access to the management account from AWS Settings, as long as you still use AWS Builder ID as your identity source.

   1. Complete the verification process for the management account email address.

   1. Choose **Review and complete activation**.

   1. Confirm your choice and choose **activate**. If you do this, you cannot revert your account.

Congratulations, you've activated advanced AWS features\!

## After you activate advanced features
<a name="activate-advanced-features-after"></a>

After you activated advanced features, you can do the following:
+ [Manage workforce members](manage-workforce-members.md)
+ [Change identity source from AWS Builder ID](change-identity-source.md)
+ [Remove organization policies](remove-org-policies.md)
+ [Create an organizational unit](https://docs.aws.amazon.com/organizations/latest/userguide/create_ou.html)
+ [Enable or disable AWS Regions in your account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html)
+ [Create IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)