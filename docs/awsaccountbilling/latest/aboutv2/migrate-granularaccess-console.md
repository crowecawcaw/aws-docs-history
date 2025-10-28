# Using the console to bulk migrate your policies

###### Note

The following AWS Identity and Access Management (IAM) actions have reached the end of standard support on July 2023:

- `*aws-portal*` namespace
- `*purchase-orders:ViewPurchaseOrders*`
- `*purchase-orders:ModifyPurchaseOrders*`
  If you're using AWS Organizations, you can use the [bulk policy migrator scripts](migrate-iam-permissions.md "migrate-iam-permissions.md") or bulk policy migrator to update
  polices from your payer account. You can also use the [old to granular action
  mapping reference](migrate-granularaccess-iam-mapping-reference.md "migrate-granularaccess-iam-mapping-reference.md") to verify the IAM actions that need to be added.

If you have an AWS account, or are a part of an AWS Organizations created on or after
March 6, 2023, 11:00 AM (PDT), the fine-grained actions are already in effect in your
organization.

This section covers how you can use the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/") to migrate your legacy policies from your Organizations accounts or standard accounts to the fine-grained actions in bulk. You can complete migrating your legacy policies using the console in two ways:

**Using the AWS recommended migration process**

This is a streamlined, single-action process where you migrates legacy actions to the fine-grained actions as mapped by AWS. For more information, see [Using recommended actions to bulk migrate legacy policies](migrate-console-streamlined.md "migrate-console-streamlined.md").

**Using the customized migration process**

This process allows you to review and change the actions recommended by AWS prior to the bulk migration, as well as customize which accounts in your organization are migrated. For more information, see [Customizing actions to bulk migrate legacy policies](migrate-console-customized.md "migrate-console-customized.md").

## Prerequisites for bulk migrating using the console

Both migration options require you to consent in the console so that AWS can recommend fine-grained actions to the legacy IAM actions you have assigned. To do this, you will need to login to your AWS account as an [IAM principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") with the following IAM actions to continue with the policy updates.

Management account

```
// Required to view page
"ce:GetConsoleActionSetEnforced",
"aws-portal:GetConsoleActionSetEnforced",
"purchase-orders:GetConsoleActionSetEnforced",
"ce:UpdateConsoleActionSetEnforced",
"aws-portal:UpdateConsoleActionSetEnforced",
"purchase-orders:UpdateConsoleActionSetEnforced",
"iam:GetAccountAuthorizationDetails",
"s3:CreateBucket",
"s3:DeleteObject",
"s3:ListAllMyBuckets",
"s3:GetObject",
"s3:PutObject",
"s3:ListBucket",
"s3:PutBucketAcl",
"s3:PutEncryptionConfiguration",
"s3:PutBucketVersioning",
"s3:PutBucketPublicAccessBlock",
"lambda:GetFunction",
"lambda:DeleteFunction",
"lambda:CreateFunction",
"lambda:InvokeFunction",
"lambda:RemovePermission",
"scheduler:GetSchedule",
"scheduler:DeleteSchedule",
"scheduler:CreateSchedule",
"cloudformation:ActivateOrganizationsAccess",
"cloudformation:CreateStackSet",
"cloudformation:CreateStackInstances",
"cloudformation:DescribeStackSet",
"cloudformation:DescribeStackSetOperation",
"cloudformation:ListStackSets",
"cloudformation:DeleteStackSet",
"cloudformation:DeleteStackInstances",
"cloudformation:ListStacks",
"cloudformation:ListStackInstances",
"cloudformation:ListStackSetOperations",
"cloudformation:CreateStack",
"cloudformation:UpdateStackInstances",
"cloudformation:UpdateStackSet",
"cloudformation:DescribeStacks",
"ec2:DescribeRegions",
"iam:GetPolicy",
"iam:GetPolicyVersion",
"iam:GetUserPolicy",
"iam:GetGroupPolicy",
"iam:GetRole",
"iam:GetRolePolicy",
"iam:CreatePolicyVersion",
"iam:DeletePolicyVersion",
"iam:ListAttachedRolePolicies",
"iam:ListPolicyVersions",
"iam:PutUserPolicy",
"iam:PutGroupPolicy",
"iam:PutRolePolicy",
"iam:SetDefaultPolicyVersion",
"iam:GenerateServiceLastAccessedDetails",
"iam:GetServiceLastAccessedDetails",
"iam:GenerateOrganizationsAccessReport",
"iam:GetOrganizationsAccessReport",
"organizations:ListAccounts",
"organizations:ListPolicies",
"organizations:DescribePolicy",
"organizations:UpdatePolicy",
"organizations:DescribeOrganization",
"organizations:ListAccountsForParent",
"organizations:ListRoots",
"sts:AssumeRole",
"sso:ListInstances",
"sso:ListPermissionSets",
"sso:GetInlinePolicyForPermissionSet",
"sso:DescribePermissionSet",
"sso:PutInlinePolicyToPermissionSet",
"sso:ProvisionPermissionSet",
"sso:DescribePermissionSetProvisioningStatus",
"notifications:ListNotificationHubs" // Added to ensure Notifications API does not return 403
```

Member account or standard account

```
// Required to view page
"ce:GetConsoleActionSetEnforced",
"aws-portal:GetConsoleActionSetEnforced",
"purchase-orders:GetConsoleActionSetEnforced",
"ce:UpdateConsoleActionSetEnforced", // Not needed for member account
"aws-portal:UpdateConsoleActionSetEnforced", // Not needed for member account
"purchase-orders:UpdateConsoleActionSetEnforced", // Not needed for member account
"iam:GetAccountAuthorizationDetails",
"ec2:DescribeRegions",
"s3:CreateBucket",
"s3:DeleteObject",
"s3:ListAllMyBuckets",
"s3:GetObject",
"s3:PutObject",
"s3:ListBucket",
"s3:PutBucketAcl",
"s3:PutEncryptionConfiguration",
"s3:PutBucketVersioning",
"s3:PutBucketPublicAccessBlock",
"iam:GetPolicy",
"iam:GetPolicyVersion",
"iam:GetUserPolicy",
"iam:GetGroupPolicy",
"iam:GetRolePolicy",
"iam:GetRole",
"iam:CreatePolicyVersion",
"iam:DeletePolicyVersion",
"iam:ListAttachedRolePolicies",
"iam:ListPolicyVersions",
"iam:PutUserPolicy",
"iam:PutGroupPolicy",
"iam:PutRolePolicy",
"iam:SetDefaultPolicyVersion",
"iam:GenerateServiceLastAccessedDetails",
"iam:GetServiceLastAccessedDetails",
"notifications:ListNotificationHubs" // Added to ensure Notifications API does not return 403
```

###### Topics

- [Using recommended actions to bulk migrate legacy policies](migrate-console-streamlined.md "migrate-console-streamlined.md")
- [Customizing actions to bulk migrate legacy policies](migrate-console-customized.md "migrate-console-customized.md")
- [Rollingback your bulk migration policy changes](migrate-console-rollback.md "migrate-console-rollback.md")
- [Confirming your migration](#migrate-console-complete "#migrate-console-complete")

## Confirming your migration

You can see if there are any AWS Organizations accounts that still need to migrate by using the migration tool.

###### To confirm if all accounts migrated

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the search bar at the top of the page, enter `Bulk Policy Migrator`.
3. On the **Manage new IAM actions** page, choose the **Migrate accounts** tab.

All accounts have migrated successfully if the table doesn't show any remaining accounts.
