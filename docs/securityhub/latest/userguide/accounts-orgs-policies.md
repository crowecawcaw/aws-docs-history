

# Managing accounts with declarative policies in Security Hub CSPM
<a name="accounts-orgs-policies"></a>

With an AWS Security Hub CSPM declarative policy, you can centrally enable and configure Security Hub CSPM across the accounts in your organization. You use an AWS Organizations declarative policy to specify where Security Hub CSPM is enabled or disabled in each AWS Region. You can target the organization root, organizational units (OUs), or individual accounts. You also specify the standards, controls, and control parameters that apply. Accounts that join the organization, or move into an OU that has an attached declarative policy, inherit the declarative policy. Security Hub CSPM then configures them according to their effective declarative policy.

Security Hub CSPM declarative policies replace [central configuration](central-configuration-intro.md) as the recommended way to manage Security Hub CSPM across an organization. The two mechanisms are mutually exclusive. When you attach your first declarative policy, Security Hub CSPM disables central configuration for the entire organization. For more information about declarative policy structure, inheritance, validation, and example declarative policies, see [Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm.html) in the *AWS Organizations User Guide*.

## Prerequisites
<a name="accounts-orgs-policies-prereqs"></a>

Before you use Security Hub CSPM declarative policies, complete the following prerequisites:

1. Enable [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-securityhub.html#integrate-enable-ta-securityhub) for Security Hub CSPM in AWS Organizations.

1. (Optional) Designate a [delegated Security Hub CSPM administrator account](designate-orgs-admin-account.md). Security Hub CSPM requires a delegated administrator to automatically associate governed accounts as members.

1. Attach the [delegation policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-policy-delegate-update.html) that grants the delegated administrator permission to manage Security Hub CSPM declarative policies.

1. Make sure that the `AWSServiceRoleForSecurityHub` [service-linked role](using-service-linked-roles.md) exists in the organization's management account.

1. Enable the `SECURITYHUB_CSPM_POLICY` policy type on the organization root. For instructions, see [Enabling a policy type](https://docs.aws.amazon.com/organizations/latest/userguide/enable-policy-type.html) in the *AWS Organizations User Guide*. If you create your first declarative policy in the Security Hub console, the console enables the policy type for you.

**Warning**  
If you use central configuration, attaching a Security Hub CSPM declarative policy to any target, even a single account, disables central configuration for the entire organization. Accounts that central configuration governed but that the new declarative policy doesn't cover become self-managed. To move your existing configuration without coverage gaps, use the import tool described in [Declarative policies and central configuration in Security Hub CSPM](orgs-policies-and-central-config.md).

For instructions on completing these prerequisites, see [Getting started with Security Hub CSPM policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_securityhub-cspm_getting-started.html) in the *AWS Organizations User Guide*.