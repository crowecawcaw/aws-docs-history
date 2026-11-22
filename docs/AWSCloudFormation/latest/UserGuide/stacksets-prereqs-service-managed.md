

# Grant service-managed permissions

With *service-managed* permissions, you don't create or maintain IAM roles in each target account yourself. CloudFormation creates them for you across the accounts in your organization, and keeps creating them as you add accounts, which removes most of the per-account setup that self-managed permissions require.

This topic provides instructions on how to grant the permissions required by StackSets to deploy across accounts and AWS Regions using *service-managed* permissions. With this permissions model, you activate trusted access with AWS Organizations, and CloudFormation creates the necessary IAM roles on your behalf. You can also provide your own execution role template to control the permissions that StackSets uses in your target accounts. To use *self-managed* permissions, see [Grant self-managed permissions](stacksets-prereqs-self-managed.md) instead.

**Topics**
+ [Activate trusted access for StackSets with AWS Organizations](stacksets-orgs-activate-trusted-access.md)
+ [Configure a custom execution role template for StackSets](stacksets-custom-execution-role.md)