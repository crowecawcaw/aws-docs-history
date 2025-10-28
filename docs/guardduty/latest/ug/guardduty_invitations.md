# Managing GuardDuty accounts by invitation

To manage accounts outside of your organization, you can use the legacy invitation method.
When you use this method, your account is designated as a administrator account when another account
accepts your invitation to become a member account.

###### Note

GuardDuty recommends using AWS Organizations instead of GuardDuty invitations, to manage your member accounts.
For more information, see [Managing accounts with
AWS Organizations](guardduty_organizations.md "guardduty_organizations.md").

If your account is not an administrator account, you can accept an invitation from another account. When
you accept, your account becomes a member account. An AWS account cannot be a GuardDuty
administrator account and member account at the same time.

When you accept an invitation from one account, you can't accept an invitation from
another account. To accept an invitation from another account, you will first need to
disassociate your account from the existing administrator account. Alternatively, the administrator account can also
disassociate and remove your account from their organization.

Accounts associated by invitation have the similar overall administrator account-to-member relationship as
accounts associated by AWS Organizations, as described in [Understanding the relationship
between GuardDuty administrator account and member accounts](administrator_member_relationships.md "administrator_member_relationships.md"). However, invitation administrator account users
cannot enable GuardDuty on behalf of associated member accounts or view other non-member
accounts within their AWS Organizations organization.

###### Important

Cross-regional data transfer may occur when GuardDuty creates member accounts using this
method. In order to verify member accounts' email addresses, GuardDuty uses an email
verification service that operates only in the US East (N. Virginia) Region.

###### Topics

- [Adding accounts by invitation](guardduty_become_console.md "guardduty_become_console.md")
- [Consolidating GuardDuty administrator accounts under a single
  organization](consolidate-orgs.md "consolidate-orgs.md")
