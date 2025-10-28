# Manually enabling Security Hub CSPM in new organization accounts

If you don't automatically enable Security Hub CSPM in new organization accounts when they join the organization, then
you can add those accounts as members and enable Security Hub CSPM in them manually after they join the organization. You must also manually enable Security Hub CSPM in AWS accounts that you
previously disassociated from an organization.

###### Note

This section doesn't apply to you if you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"). If you
use central configuration, you can create configuration policies that enable Security Hub CSPM in specified member accounts and organizational units (OUs). You can also
enable specific standards and controls in those accounts and OUs.

You can't enable Security Hub CSPM in an account if it is already a member account within a different organization.

You also can't enable Security Hub CSPM in an account that is currently suspended. If you try to enable the service in a
suspended account, the account status changes to **Account
Suspended**.

- If the account doesn't have Security Hub CSPM enabled, Security Hub CSPM is enabled in that account.
  The AWS Foundational Security Best Practices (FSBP) standard and CIS AWS
  Foundations Benchmark v1.2.0 also are enabled in the account unless your turn off default security standards.

The exception to this is the Organizations management account. Security Hub CSPM cannot be
enabled automatically in the Organizations management account. You must manually enable Security Hub CSPM in the Organizations
management account before you can add it as a member account.

- If the account already has Security Hub CSPM enabled, Security Hub CSPM doesn't make any other
  changes to the account. It only enables the membership.
  In order for Security Hub CSPM to generate control findings, member accounts must have AWS Config enabled and configured to record required
  resources. For more information, see [Enabling and configuring AWS Config](securityhub-prereq-config.md "securityhub-prereq-config.md").

Choose your preferred method, and follow the steps to enable an organization account as a Security Hub CSPM member account.

Security Hub CSPM console

###### To manually enable organization accounts as Security Hub CSPM members

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated administrator account. 2. In the Security Hub CSPM navigation pane, under **Settings**, choose **Configuration**. 3. In the **Accounts** list, select each
organization account that you want to enable. 4. Choose **Actions**, and then choose **Add member**.

Security Hub CSPM API
**To manually enable organization accounts as Security Hub CSPM members**

Invoke the [`CreateMembers`](../../1.0/APIReference/API_CreateMembers.md "../../1.0/APIReference/API_CreateMembers.md") API from the delegated administrator account. For each account to
enable, provide the account ID.

Unlike the manual invitation process, when you invoke `CreateMembers` to enable an
organization account, you don't need to send an invitation.

AWS CLI
**To manually enable organization accounts as Security Hub CSPM members**

Run
the [`create-members`](../../../cli/latest/reference/securityhub/create-members.md "../../../cli/latest/reference/securityhub/create-members.md") command from the delegated administrator account. For each account to
enable, provide the account ID.

Unlike the manual invitation process, when you run `create-members` to enable an
organization account, you don't need to send an invitation.

```
aws securityhub create-members --account-details '[{"AccountId": "`<accountId>`"}]'
```

**Example**

```
aws securityhub create-members --account-details '[{"AccountId": "123456789111"}, {"AccountId": "123456789222"}]'
```
