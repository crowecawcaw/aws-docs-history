

# Reviewing a policy's impact before you apply it
<a name="guardduty-organization-policies-review-impact"></a>

Before you save a policy change that disables a protection plan, review which accounts and Regions currently have that protection plan enabled, so you understand what the change will turn off. Because a GuardDuty policy applies per Region, check the current enablement state per account and per Region.

**Warning**  
A policy that disables GuardDuty or a protection plan turns it off in every covered account where it is currently enabled, and prevents those accounts from turning it back on through the console or API. You can unintentionally disable protection that accounts rely on. Before you create or update a policy, identify the accounts and Regions the change affects, as described in this section, and confirm the impact is intended.

As the delegated administrator, you can review the current GuardDuty enablement across your organization by using the GuardDuty console **Accounts** page (switch Regions to review coverage in each Region), or programmatically with the following steps. Perform the API steps in each Region you want to review.

**To identify the accounts and Regions a policy affects**

1. Enumerate the accounts in your organization. Use the AWS Organizations `ListAccounts` API operation to list every account in the organization, including accounts that are not yet GuardDuty members.

1. Enumerate your GuardDuty member accounts. Use the GuardDuty `ListMembers` API operation to list the accounts that are already GuardDuty member accounts.

1. Review the enabled protection plans for each member account. Use the GuardDuty `GetMemberDetectors` API operation to see which features are enabled for each member account's detector.

1. Compare the current enablement against the protection plans your policy change will disable to identify the accounts and Regions the change affects.

An account that belongs to your organization but is not yet a GuardDuty member does not appear in `ListMembers`, and you cannot see its detector status until you add it as a member. When a GuardDuty policy applies to an account that is not yet a member, the account is automatically added as a member.

After you create and attach a policy, confirm the final policy that applies to a specific account. The effective policy is the aggregation of every policy the account inherits from its parent entities, combined with any policy attached directly to the account. To view it, use the AWS Organizations `DescribeEffectivePolicy` API operation, or its AWS CLI or AWS SDK equivalents, with the GuardDuty policy type. Any account with permission to call this operation can use it, including the delegated administrator account. For more information, see [Viewing effective declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_effective.html) in the AWS Organizations User Guide.