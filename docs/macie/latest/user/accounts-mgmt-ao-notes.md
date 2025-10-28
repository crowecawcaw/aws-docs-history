# Considerations for using Macie with

AWS Organizations

Before you integrate Amazon Macie with AWS Organizations and configure your organization in Macie,
consider the following requirements and recommendations. Also ensure that you understand the
[relationship between Macie administrator and member
accounts](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

###### Topics

- [Designating an
  administrator account](#accounts-mgmt-ao-notes-admin-designate "#accounts-mgmt-ao-notes-admin-designate")
- [Changing or removing
  the administrator account designation](#accounts-mgmt-ao-notes-admin-remove "#accounts-mgmt-ao-notes-admin-remove")
- [Adding and removing
  member accounts](#accounts-mgmt-ao-notes-members-manage "#accounts-mgmt-ao-notes-members-manage")
- [Transitioning from an invitation-based organization](#accounts-mgmt-ao-notes-transition-invitations "#accounts-mgmt-ao-notes-transition-invitations")

## Designating a

Macie administrator account

While you determine which account should be the delegated Macie administrator account for your
organization, keep the following in mind:

- An organization can have only one delegated Macie administrator account.
- An account can’t be a Macie administrator and member account at the same time.
- Only the AWS Organizations management account for an organization can designate the
  delegated Macie administrator account for the organization. Only the management account can
  subsequently change or remove that designation.
- The AWS Organizations management account for an organization can also be the delegated
  Macie administrator account for the organization. However, we don't recommend this
  configuration based on AWS security best practices and the principle of least
  privilege. Users who have access to the management account for billing purposes
  are likely to be different from users who need access to Macie for information
  security purposes.

If you prefer this configuration, you must enable Macie for the organization's
management account in at least one AWS Region before you designate the account
as the delegated Macie administrator account. Otherwise, the account won't be able to
access and manage Macie settings and resources for member accounts.

- Unlike AWS Organizations, Macie is a Regional service. This means that the designation
  of a Macie administrator account is a Regional designation. It also means that associations
  between Macie administrator and member accounts are Regional. For example, if
  the management account designates a Macie administrator account in the US East (N. Virginia)
  Region, the Macie administrator can manage Macie for member accounts only in that
  Region.

To centrally manage Macie accounts in multiple AWS Regions, the management
account must sign in to each Region where the organization currently uses or
will use Macie, and then designate the Macie administrator account in each of those
Regions. The Macie administrator can then configure the organization in each of those
Regions. For a list of Regions where Macie is currently available, see [Amazon Macie endpoints and quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the
_AWS General Reference_.

- An account can be associated with only one Macie administrator account at a time. If your
  organization uses Macie in multiple Regions, the designated Macie administrator account
  must be the same in all of those Regions. However, your organization’s
  management account must designate the administrator account separately in each
  Region.
- An account can be the delegated Macie administrator account for only one organization at
  a time. If you manage multiple organizations in AWS Organizations, you must designate a
  different Macie administrator account for each organization. This is due to an AWS Organizations
  requirement—an account can be a member of only one organization at a
  time.

If the Macie administrator’s AWS account is suspended, isolated, or closed, all associated
Macie member accounts are automatically removed as Macie member accounts but Macie
continues to be enabled for the accounts. If [automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md") was enabled for one or more member accounts, it's disabled for
the accounts. This also disables access to statistical data, inventory data, and other
information that Macie produced and directly provided while performing automated discovery for the
accounts. To restore access to this data, the following must occur within 30
days:

1. The Macie administrator’s AWS account is restored.
2. The AWS Organizations management account designates the account as the Macie administrator account
   again.
3. The Macie administrator configures the organization and enables automated discovery for the
   appropriate accounts again.

After 30 days, Macie permanently deletes data that it previously produced and directly
provided while performing automated discovery for the applicable accounts.

## Changing or removing the

designation of a Macie administrator account

Only the AWS Organizations management account for an organization can change or remove the
designation of a delegated Macie administrator account for the organization.

If the management account changes or removes the designation:

- All associated member accounts are removed as Macie member accounts but Macie continues to
  be enabled for the accounts. The accounts become standalone Macie accounts. To
  pause or stop using Macie, a user of a member account must suspend (pause) or
  disable (stop) Macie for the account.
- Automated sensitive data discovery is disabled for each account that it was enabled for. This
  also disables access to statistical data, inventory data, and other information
  that Macie produced and directly provided while performing automated discovery for each
  account. To restore access to this data, the management account must designate
  the same Macie administrator account again within 30 days. In addition, the Macie administrator
  must configure the organization again and re-enable automated discovery for each account
  within 30 days. After 30 days, the data expires and Macie permanently deletes
  it.

## Adding and removing Macie member

accounts

As you add, remove, and otherwise manage member accounts for your organization, keep
the following in mind:

- A Macie administrator account can be associated with no more than 10,000 Macie member accounts in
  each AWS Region. If your organization exceeds this quota, the Macie administrator
  won’t be able to add member accounts until they remove the necessary number of
  existing member accounts in the Region. When an organization meets this quota,
  we notify the Macie administrator by creating an AWS Health event for their
  account. We also send email to the address that’s associated with their
  account.

If you’re the Macie administrator for an organization, you can determine how many member accounts
are currently associated with your account by using the
**Accounts** page on the Amazon Macie console or the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation of the Amazon Macie API. For more information,
see [Reviewing Macie accounts for an organization](accounts-mgmt-ao-review.md "accounts-mgmt-ao-review.md").

- An account can be associated with only one Macie administrator account at a time. This
  means that an account can’t accept a Macie invitation from another account if
  it’s already associated with the Macie administrator account for an organization in
  AWS Organizations.

Similarly, if an account already accepted an invitation, the Macie administrator for
an organization in AWS Organizations can’t add the account as a Macie member account. The
account must first disassociate from its current, invitation-based
administrator account.

- To add the AWS Organizations management account as a Macie member account, a user of
  the management account must first enable Macie for the account. The Macie administrator
  isn’t allowed to enable Macie for the management account.
- If the Macie administrator removes a Macie member account:
  - Macie continues to be enabled for the account. The account becomes a standalone Macie
    account. To pause or stop using Macie, a user of the account must
    suspend (pause) or disable (stop) Macie for the account.
  - Automated sensitive data discovery is disabled for the account, if it was enabled. This
    also disables access to statistical data, inventory data, and other
    information that Macie produced and directly provided while performing
    automated discovery for the account.

- A member account can’t disassociate from its Macie administrator account. Only the
  Macie administrator can remove an account as a Macie member account.

## Transitioning from an

invitation-based organization

If you already associated a Macie administrator account with member accounts by using Macie
membership invitations, we recommend that you designate that account as the delegated
Macie administrator account for your organization in AWS Organizations. This simplifies the transition from
an invitation-based organization.

If you do this, all currently associated member accounts continue to be members. If a member
account is part of your organization in AWS Organizations, the account’s association
automatically changes from **By invitation** to **Via
AWS Organizations** in Macie. If a member account isn’t part of your organization in
AWS Organizations, the account’s association continues to be **By invitation**.
In both cases, the accounts continue to be associated with the delegated
Macie administrator account as member accounts. For sensitive data discovery, this also means that
the accounts can continue to access statistical and other data that Macie produced and
directly provided while performing automated sensitive data discovery for the accounts. In addition, if the
Macie administrator configured sensitive data discovery jobs to analyze data for the accounts, subsequent job
runs will continue to include resources that the accounts own.

We recommend this approach because an account can’t be associated with more than one
Macie administrator account at the same time. If you designate a different account as the
Macie administrator account for your organization in AWS Organizations, the designated administrator won’t
be able to manage accounts that are already associated with another Macie administrator account by
invitation. Each member account must first disassociate from its current,
invitation-based administrator account. The Macie administrator for your organization in
AWS Organizations can then add the account as a Macie member account and begin managing the
account.

After you integrate Macie with AWS Organizations and you configure your organization in Macie,
you can optionally designate a different Macie administrator account for the organization. You can
also continue to use invitations to associate and manage member accounts that aren't
part of your organization in AWS Organizations.
