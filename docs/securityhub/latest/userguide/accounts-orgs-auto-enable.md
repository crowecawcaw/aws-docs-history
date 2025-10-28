# Automatically enabling Security Hub CSPM in new organization accounts

When new accounts join your organization, they are added to the list on the
**Accounts** page of the AWS Security Hub CSPM console. For organization accounts,
**Type** is **By organization**. By default, new accounts
don't become Security Hub CSPM members when they join the organization. Their status is **Not a member**.
The delegated administrator account can automatically add new accounts as members and enable Security Hub CSPM in these accounts when they join the
organization.

###### Note

Although many AWS Regions are active by default for your AWS account, you must activate certain Regions manually.
These Regions are called opt-in Regions in this document. To automatically enable Security Hub CSPM in a new account in an opt-in Region, the account must
have that Region activated first. Only the account owner can activate the opt-in Region. For more information about opt-in Regions,
see [Specify which AWS Regions your account can use](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md").

This process is different based on whether you use central configuration (recommended) or
local configuration.

## Automatically enabling new organization

accounts (central configuration)

If you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"), you can
automatically enable Security Hub CSPM in new and existing organization accounts by creating a configuration policy in which Security Hub CSPM
is enabled. You can then associate the policy with the organization root or specific organizational units (OUs).

If you associate a configuration policy in which Security Hub CSPM is enabled with a specific OU,
Security Hub CSPM is automatically enabled in all accounts (existing and new) that belong to that OU. New accounts that don't belong to the OU are
self-managed and don't automatically have Security Hub CSPM enabled. If you associate a configuration policy in which Security Hub CSPM is enabled with the root,
Security Hub CSPM is automatically enabled in all accounts (existing and new) that join the organization. The exceptions are if an account uses a different policy through
application or inheritance, or is self-managed.

In your configuration policy, you can also define which security standards and controls should be enabled in the OU. To generate
control findings for enabled standards, the accounts in the OU must have AWS Config enabled and configured to record required
resources. For more information about AWS Config recording, see [Enabling and configuring AWS Config](securityhub-prereq-config.md "securityhub-prereq-config.md").

For instructions on creating a configuration policy, see [Creating and associating configuration policies](create-associate-policy.md "create-associate-policy.md").

## Automatically enabling new organization

accounts (local configuration)

When you use local configuration and turn on automatic enablement of default standards, Security Hub CSPM adds _new_ organization accounts
as members and enables Security Hub CSPM in them in the current Region. Other Regions aren't affected. In addition, turning on automatic
enablement doesn't enable Security Hub CSPM in _existing_ organization accounts unless they were already added as member accounts.

After turning on automatic enablement, default security standards are enabled
for new member accounts in the current Region when they join the organization. The default standards are AWS Foundational Security Best Practices
(FSBP) and Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0. You can't change the default standards. If you
want to enable other standards throughout your organization, or enable standards for select accounts and OUs, we recommend using central configuration.

To generate control findings for the default standards (and other enabled standards), accounts in your organization must have AWS Config enabled and configured to record required
resources. For more information about AWS Config recording, see [Enabling and configuring AWS Config](securityhub-prereq-config.md "securityhub-prereq-config.md").

Choose your preferred method, and follow the steps to
automatically enable Security Hub CSPM in new organization accounts. These instructions apply only if you use local configuration.

Security Hub CSPM console

###### To automatically enable new organization accounts as Security Hub CSPM members

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign is using the credentials of the delegated administrator account. 2. In the Security Hub CSPM navigation pane, under **Settings**, choose
**Configuration**. 3. In the **Accounts** section, turn on **Auto-enable accounts**.

Security Hub CSPM API
**To automatically enable new organization accounts as Security Hub CSPM members**

Invoke the [`UpdateOrganizationConfiguration`](../../1.0/APIReference/API_UpdateOrganizationConfiguration.md "../../1.0/APIReference/API_UpdateOrganizationConfiguration.md") API from the delegated administrator account. Set the `AutoEnable`
field to `true` to automatically enable Security Hub CSPM in new organization accounts.

AWS CLI
**To automatically enable new organization accounts as Security Hub CSPM members**

Run
the [`update-organization-configuration`](../../../cli/latest/reference/securityhub/update-organization-configuration.md "../../../cli/latest/reference/securityhub/update-organization-configuration.md")
command from the delegated administrator account. Include the `auto-enable` parameter to automatically enable Security Hub CSPM in
new organization accounts.

```
aws securityhub update-organization-configuration --auto-enable
```
