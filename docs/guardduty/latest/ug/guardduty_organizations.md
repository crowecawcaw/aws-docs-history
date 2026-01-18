# Managing GuardDuty accounts with AWS Organizations

In an AWS organization, the management account can designate any account within this
organization as the delegated GuardDuty administrator account. For this administrator account, GuardDuty gets enabled automatically only in the
current AWS Region. By default, the administrator account can enable and manage GuardDuty for all the member
accounts in the organization within that Region. The administrator account can view and add members to
this AWS organization.

The following sections will walk you through various tasks that you may perform as a
delegated GuardDuty administrator account.

###### Contents

- [Considerations and recommendations for using
  GuardDuty with AWS Organizations](#delegated_admin_important "#delegated_admin_important")
- [Permissions required to designate a
  delegated GuardDuty administrator account](organizations_permissions.md "organizations_permissions.md")
- [Designating a delegated GuardDuty administrator account](delegated-admin-designate.md "delegated-admin-designate.md")
- [Setting organization auto-enable
  preferences](set-guardduty-auto-enable-preferences.md "set-guardduty-auto-enable-preferences.md")
- [Adding members to the
  organization](add-member-accounts-guardduty-organization.md "add-member-accounts-guardduty-organization.md")
- [(Optional) Enable protection
  plans for existing member accounts](guardduty_quick_protection_plan_config.md "guardduty_quick_protection_plan_config.md")
- [Continually
  managing your member accounts within GuardDuty](maintaining-guardduty-organization-delegated-admin.md "maintaining-guardduty-organization-delegated-admin.md")
- [Suspending GuardDuty for
  member account](suspending-guardduty-member-account-from-admin.md "suspending-guardduty-member-account-from-admin.md")
- [Disassociating
  (removing) member account from administrator account](disassociate-remove-member-account-from-admin.md "disassociate-remove-member-account-from-admin.md")
- [Deleting member accounts
  from GuardDuty organization](delete-member-accounts-guardduty-organization.md "delete-member-accounts-guardduty-organization.md")
- [Changing the delegated GuardDuty administrator account](change-guardduty-delegated-admin.md "change-guardduty-delegated-admin.md")

## Considerations and recommendations for using

GuardDuty with AWS Organizations

The following considerations and recommendations can help you understand how a
delegated GuardDuty administrator account operates in GuardDuty:

**A delegated GuardDuty administrator account can manage a maximum of 50,000
members.**

There is a limit of 50,000 member accounts per delegated GuardDuty administrator account. This includes
member accounts that are added through AWS Organizations or those who accepted the
GuardDuty administrator account's invitation to join their organization. However, there could
be more than 50,000 accounts in your AWS organization.

If you exceed the 50,000 member accounts limit, you will receive a
notification from CloudWatch, Health Dashboard, and an email to the designated
delegated GuardDuty administrator account.

**A delegated GuardDuty administrator account is Regional.**

Unlike AWS Organizations, GuardDuty is a Regional service. The delegated GuardDuty administrator accounts and their
member accounts must be added through AWS Organizations in each desired Region where
you have GuardDuty enabled. If the organization management account designates a
delegated GuardDuty administrator account in only US East (N. Virginia), then delegated GuardDuty administrator account will only manage member
accounts added to the organization in that Region. For more information
about feature parity in Regions where GuardDuty is available, see [Regions and endpoints](guardduty_regions.md "guardduty_regions.md").

**Special cases for opt-in Regions**

- When a delegated GuardDuty administrator account opts out of an opt-in Region, even if your organization
  has the GuardDuty auto-enable configuration set to either new member accounts only
  (`NEW`) or all member accounts (`ALL`), GuardDuty
  cannot be enabled for any member account in the organization that currently
  has GuardDuty disabled. For information about the
  configuration of your member accounts,
  open **Accounts** in the [GuardDuty console](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") navigation pane or use the
  [ListMembers](../APIReference/API_ListMembers.md "../APIReference/API_ListMembers.md") API.
- When working with the GuardDuty auto-enable configuration set to
  `NEW`, ensure that the following sequence is
  met:

      1. The member accounts opt-in to an opt-in Region.
      2. Add the member accounts to your organization in
       AWS Organizations.

  If you change the order of these steps, the GuardDuty auto-enable
  setting with `NEW`
  **will not** work in the specific
  opt-in Region because the member account is no longer new to the
  organization. GuardDuty provides two alternate solutions:

      + Set the GuardDuty auto-enable configuration to
       `ALL`, that includes new and existing members
       accounts. In this case, the order of these steps is not
       relevant.
      + If a member account is already a part of your
       organization, manage the GuardDuty configuration for this
       account individually in the specific opt-in Region by using
       the GuardDuty console or the API.

**Required for an AWS organization to have the same
delegated GuardDuty administrator account across all the AWS Regions.**

You must designate one member account as the delegated GuardDuty administrator account across all the
AWS Regions where GuardDuty is enabled. For example, if you designate a member
account `111122223333` in
`Europe (Ireland)`, you can't designate
another member account `555555555555` in
`Canada (Central)`. It is required that
you use the same account as delegated GuardDuty administrator account in all other Regions.

You can designate a new delegated GuardDuty administrator account at any point in time. For more information
about removing the existing delegated GuardDuty administrator account, see [Changing the delegated GuardDuty administrator account](change-guardduty-delegated-admin.md "change-guardduty-delegated-admin.md").

**Not recommended to set your organization's
management account as the delegated GuardDuty administrator account.**

Your organization's management account can be the delegated GuardDuty administrator account. However, the
AWS security best practices follow the principle of least privilege and
doesn't recommend this configuration.

**Changing a delegated GuardDuty administrator account does not disable GuardDuty for member
accounts.**

If you remove a delegated GuardDuty administrator account, GuardDuty removes all the member accounts associated
with this delegated GuardDuty administrator account. GuardDuty still remains enabled for all these member
accounts.
