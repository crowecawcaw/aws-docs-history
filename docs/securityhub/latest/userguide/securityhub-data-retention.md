# Effect of account actions on Security Hub CSPM data

These account actions have the following effects on AWS Security Hub CSPM data.

## Security Hub CSPM disabled

If you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"),
the delegated administrator (DA) can create Security Hub CSPM configuration policies that disable
AWS Security Hub CSPM in specific accounts and organizational units (OUs). In this case, Security Hub CSPM is
disabled in the specified accounts and OUs in your home Region and any linked Regions.
If you don't use central configuration, you must disable Security Hub CSPM separately in each
account and Region where you enabled it. You can't use central configuration if Security Hub CSPM is
disabled in the DA account.

No findings are generated or updated for the administrator account if Security Hub CSPM is
disabled in the administrator account. Existing archived findings are deleted after 30
days. Existing active findings are deleted after 90 days.

Integrations with other AWS services are removed.

Enabled security standards and controls are disabled.

Other Security Hub CSPM data and settings, including custom actions, insights, and subscriptions
to third-party products are retained for 90 days.

## Member account disassociated

from administrator account

When a member account is disassociated from the administrator account, the
administrator account loses permission to view findings in the member account. However,
Security Hub CSPM is still enabled in both accounts.

If you use central configuration, the DA can't configure Security Hub CSPM for a member
account that's disassociated from the DA account.

Custom settings or integrations that are defined for the administrator account are not
applied to findings from the former member account. For example, after the accounts are
disassociated, you might have a custom action in the administrator account used as the
event pattern in an Amazon EventBridge rule. However, this custom action cannot be used in the
member account.

In the **Accounts** list for the Security Hub CSPM administrator account, a
removed account has a status of **Disassociated**.

## Member account is removed from

an organization

When a member account is removed from an organization, the Security Hub CSPM administrator account
loses permission to view findings in the member account. However, Security Hub CSPM is still enabled
in both accounts with the same settings they had before removal.

If you use central configuration, you can't configure Security Hub CSPM for a member account
after it's removed from the organization to which the delegated administrator belongs. However, the account retains the
settings it had prior to removal unless you manually change them.

In the **Accounts** list for the Security Hub CSPM administrator account, a
removed account has a status of **Deleted**.

## Account is suspended

When an AWS account is suspended, the account loses permission to view their
findings in Security Hub CSPM. No findings are generated or updated for that account. The
administrator account for a suspended account can view existing findings for the
account.

For an organization account, the member account status can also change to **Account Suspended**. This happens if the account is suspended
at the same time that the administrator account attempts to enable the account. The
administrator account for an **Account Suspended** account
cannot view findings for that account. Otherwise, the suspended status doesn't affect the member account status.

If you use central configuration, policy association fails if the delegated administrator tries to associate a configuration policy
with a suspended account.

After 90 days, the account is either terminated or reactivated. When the account is
reactivated, its Security Hub CSPM permissions are restored. If the member account status is
**Account Suspended**, the administrator account must
enable the account manually.

## Account is closed

When an AWS account is closed, Security Hub CSPM responds to the closure as follows.

If the account is a Security Hub CSPM administrator account, it is removed as an administrator
account and all the member accounts are removed. If the account is a member account, it
is disassociated and removed as a member from the Security Hub CSPM administrator account.

Security Hub CSPM retains existing archived findings in the account for 30 days. For a control
finding, the calculation of 30 days is based on the value for the `UpdatedAt`
field of the finding. For another type of finding, the calculation is based on the value
for the `UpdatedAt` or `ProcessedAt` field of the finding,
whichever date is latest. At the end of this 30-day period, Security Hub CSPM permanently deletes
the finding from the account.

Security Hub CSPM retains existing active findings in the account for 90 days. For a control
finding, the calculation of 90 days is based on the value for the `UpdatedAt`
field of the finding. For another type of finding, the calculation is based on the value
for the `UpdatedAt` or `ProcessedAt` field of the finding,
whichever date is latest. At the end of this 90-day period, Security Hub CSPM permanently deletes
the finding from the account.

For longer-term retention of existing findings, you can export the findings to an S3
bucket. You can do this by using a custom action with an Amazon EventBridge rule. For more
information, see [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md").

###### Important

For customers in AWS GovCloud (US) Regions, back up and then delete your policy data
and other account resources before you close your account. You won't have access to
the resources and data after you close your account.

For more information, see [Close an
AWS account](../../../awsaccountbilling/latest/aboutv2/close-account.md "../../../awsaccountbilling/latest/aboutv2/close-account.md") in the _AWS Account Management Reference Guide_.
