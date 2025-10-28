# Managing administrator and member accounts in Security Hub CSPM

If your AWS environment has multiple accounts, you can treat the accounts that use AWS Security Hub CSPM
as member accounts and associate them with a single administrator account. The administrator
can monitor your overall security posture and take [allowed actions](securityhub-accounts-allowed-actions.md "securityhub-accounts-allowed-actions.md") on member accounts. The administrator
can also perform various account management and
administration tasks at scale, such as monitoring estimated usage costs and assessing
account quotas.

You can associate member accounts with an administrator in two ways, by integrating Security Hub CSPM
with AWS Organizations or by manually sending and accepting membership invitations in Security Hub CSPM.

## Managing accounts with AWS Organizations

AWS Organizations is a global account
management service that lets AWS administrators to consolidate and manage
multiple AWS accounts. It provides account management and consolidated billing features that
are designed to support budgetary, security, and compliance needs. It's offered at no
additional charge, and it integrates with multiple AWS services, including AWS Security Hub CSPM, Amazon Macie,
and Amazon GuardDuty. For more information, see the [_AWS Organizations User
Guide_](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

When you integrate Security Hub CSPM and AWS Organizations, the Organizations management account designates a Security Hub CSPM delegated administrator.
Security Hub CSPM is automatically enabled in the delegated administrator account in the AWS Region in which it was designated.

After designating a delegated administrator, we recommend managing accounts in Security Hub CSPM with
[central configuration](central-configuration-intro.md "central-configuration-intro.md"). This is the most efficient way to customize
Security Hub CSPM and ensure adequate security coverage for your organization.

Central configuration lets the delegated administrator customize Security Hub CSPM across multiple
organization accounts and Regions rather than configuring Region-by-Region. You can create a
configuration policy for your entire organization, or create different configuration policies for
different accounts and OUs. The policies specify whether Security Hub CSPM is enabled or disabled in associated accounts and
which security standards and controls are enabled.

The delegated administrator can designate accounts as centrally managed or self-managed. Centrally managed accounts are configurable only by the
delegated administrator. Self-managed accounts can specify their own settings.

If you don't opt in to central configuration, the delegated administrator has a more limited ability to configure Security Hub CSPM, called
_local configuration_. Under local configuration, the delegated administrator can automatically
enable Security Hub CSPM and [default security standards](securityhub-auto-enabled-standards.md "securityhub-auto-enabled-standards.md") in new organization accounts in the current Region.
However, existing accounts don't use these settings, so configuration drift can occur after an account joins the organization.

Aside from these new account settings, local configuration is account-specific and Region-specific. Each organization account must configure the Security Hub CSPM service, standards, and controls separately
in each Region. Local configuration also doesn't support the use of configuration policies.

## Managing accounts manually by invitation

You must manually manage member accounts by invitation in Security Hub CSPM if you have a standalone account or
if you don't integrate with Organizations. A standalone account can't integrate with Organizations, so it's necessary to manage it manually.
We recommend integrating with AWS Organizations and using central configuration if you add additional accounts in the future.

When you use manual account management, you designate an account to be the Security Hub CSPM
administrator. The administrator account can view data in member
accounts and take certain actions on member account findings. The Security Hub CSPM
administrator invites other accounts to be member accounts, and the
administrator-member relationship is established when a prospective member account accepts
the invitation.

Manual account management doesn't
support the use of configuration policies. Without configuration policies, the administrator can't centrally customize Security Hub CSPM by configuring variable settings for
different accounts. Instead, each organization account must enable and configure Security Hub CSPM for itself separately
in each Region. This can make it more difficult and time consuming to ensure adequate security coverage across all of
the accounts and Regions in which you use Security Hub CSPM. It can also cause configuration drift as member accounts can specify their own settings without
input from the administrator.

To manage accounts by invitation, see [Managing accounts by invitation in Security Hub CSPM](account-management-manual.md "account-management-manual.md").
