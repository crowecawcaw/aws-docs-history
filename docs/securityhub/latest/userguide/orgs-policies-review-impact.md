

# Reviewing a declarative policy's impact before you apply it in Security Hub CSPM

Before you save a declarative policy change, review the current AWS Security Hub CSPM configuration in the accounts and AWS Regions that the change affects. Because a Security Hub CSPM declarative policy governs configuration completely in each Region, it can disable standards and controls that the declarative policy doesn't list. Check the current state for each account and Region.

**Warning**  
A declarative policy completely governs Security Hub CSPM, standards, controls, and control parameters in each Region where it enables Security Hub CSPM. Standards that the declarative policy doesn't list are disabled, and parameters that it doesn't specify are reset to their default values. A declarative policy that disables Security Hub CSPM also removes administrator and member associations, including invitation-based associations that Security Hub CSPM doesn't restore. Governed accounts can't change these settings back through the console or API. Before you create or update a declarative policy, identify the accounts and Regions that the change affects and confirm that the impact is intended.

As the delegated administrator, you can review the current configuration of member accounts in the Security Hub CSPM console or programmatically. In the console, switch Regions to review each Region. To review the configuration programmatically, complete the following steps. Perform the Security Hub CSPM API steps in each Region that you want to review.

**To identify the accounts and Regions that a declarative policy affects**

1. **Enumerate the accounts in your organization.** Use the AWS Organizations [ListAccounts](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html) API operation to list every account, including accounts that aren't yet Security Hub CSPM members.

1. **Enumerate your Security Hub CSPM member accounts.** Use the Security Hub CSPM [ListMembers](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListMembers.html) API operation to list the member accounts of the delegated administrator and their `MemberStatus`.

1. **Identify administrator accounts.** For accounts in scope, use [GetAdministratorAccount](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetAdministratorAccount.html) to find accounts that are members of an administrator other than the delegated administrator. Then use `ListMembers` to find accounts that have their own members. Security Hub CSPM replaces or removes these associations when it applies a declarative policy.

1. **Review current central configuration governance.** If you use central configuration, use [ListConfigurationPolicyAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConfigurationPolicyAssociations.html) to see which configuration policy applies to each account. Attaching a Security Hub CSPM declarative policy disables all of these associations.

1. **Review the current standards and controls.** In the accounts you plan to cover, use [GetEnabledStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetEnabledStandards.html), [ListStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListStandardsControlAssociations.html), and [BatchGetSecurityControls](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchGetSecurityControls.html) to see which standards and controls are enabled and which control parameters are customized.

1. **Compare the configurations.** Compare the current configuration with the effective configuration that your declarative policy defines. This identifies the accounts and Regions that the change affects.

After you create and attach a declarative policy, confirm the effective policy for a specific account. The effective declarative policy combines the policies that the account inherits with those attached directly to the account. To view it, use the Organizations [DescribeEffectivePolicy](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html) API operation, or its AWS CLI or AWS SDK equivalent, with the `SECURITYHUB_CSPM_POLICY` policy type. Any account with permission to call this operation can use it, including the delegated administrator. For more information, see [Viewing effective declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_effective.html) in the *AWS Organizations User Guide*.