# Considerations for invitation-based

organizations in Macie

###### Note

We recommend using AWS Organizations instead of Macie invitations to manage member
accounts. For more information, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").

Before you create or begin managing an invitation-based organization in Amazon Macie, consider
the following requirements and recommendations. Also ensure that you understand the [relationship between Macie administrator and member
accounts](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

###### Topics

- [Choosing a
  Macie administrator account](#accounts-mgmt-invitations-notes-admin-designate "#accounts-mgmt-invitations-notes-admin-designate")
- [Sending invitations and managing
  Macie member accounts](#accounts-mgmt-invitations-notes-members-manage "#accounts-mgmt-invitations-notes-members-manage")
- [Responding to and
  managing membership invitations](#accounts-mgmt-invitations-notes-invitations-manage "#accounts-mgmt-invitations-notes-invitations-manage")
- [Transitioning to
  AWS Organizations](#accounts-mgmt-invitations-notes-transition-ao "#accounts-mgmt-invitations-notes-transition-ao")

## Choosing a

Macie administrator account

While you determine which account should be the Macie administrator account for the organization,
keep the following in mind:

- An organization can have only one Macie administrator account.
- An account can’t be a Macie administrator and member account at the same time.
- Macie is a Regional service. This means that the association between a
  Macie administrator account and a member account is Regional—the association exists
  only in the AWS Region that an invitation is sent from and accepted in. For
  example, if the Macie administrator sends invitations in the US East (N. Virginia) Region
  and those invitations are accepted, the Macie administrator can manage the member
  accounts only in that Region.
- To centrally manage Macie accounts in multiple AWS Regions, the Macie administrator
  must sign in to each Region where the organization currently uses or plans to
  use Macie, and send invitations to the appropriate accounts in each of those
  Regions. For a list of Regions where Macie is currently available, see [Amazon Macie endpoints and quotas](../../../general/latest/gr/macie.md "../../../general/latest/gr/macie.md") in the
  _AWS General Reference_.
- A member account can be associated with only one Macie administrator account at a time. If your
  organization uses Macie in multiple Regions, this means that the Macie administrator account
  must be the same in all of those Regions. However, administrator and member accounts
  must send and accept invitations separately in each Region.

If the Macie administrator’s AWS account is suspended, isolated, or closed, all associated member accounts are automatically removed as member
accounts but Macie continues to be enabled for the accounts. The accounts become standalone Macie accounts. If [automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md") was enabled for a
member account, it's disabled for the account. This also disables access
to statistical data, inventory data, and other information that Macie
produced and directly provided while performing automated discovery for the account.
After 30 days, this data expires and Macie permanently deletes it. To
restore access to the data before it expires, restore the Macie administrator’s
AWS account, and then use that account to create and configure the
organization again.

## Sending invitations and managing

Macie member accounts

As the Macie administrator for an invitation-based organization, keep the following in mind when
you send invitations and manage accounts in the organization:

- If you send an invitation, related data might be transferred across AWS Regions.
  This is the case because Macie verifies the receiving account’s email address by
  using an email verification service that operates only in the US East (N. Virginia)
  Region.
- You can send an invitation to any active AWS account, including accounts that
  haven’t enabled Macie. However, to accept or decline an invitation, the receiving
  account must enable Macie in the Region that the invitation was sent from.
- In each AWS Region, a Macie administrator account can be associated with no more than
  1,000 accounts by invitation. This includes accounts that haven’t responded to
  invitations yet. If your account meets this quota, you can’t add or invite
  additional accounts. To determine how many accounts are currently associated
  with your account, you can use the **Accounts** page on the
  Amazon Macie console or the [ListMembers](../APIReference/members.md "../APIReference/members.md") operation
  of the Amazon Macie API. For more information, see [Reviewing Macie accounts for an
  invitation-based organization](accounts-mgmt-invitations-review.md "accounts-mgmt-invitations-review.md").

To reduce the number of associated accounts, you can: delete associations with
accounts that aren’t currently member accounts, remove the necessary number of
member accounts, or a combination of the two. If an account resigns from your
organization or declines an invitation that you sent, it also reduces the number
of accounts that are associated with your account.

- An account can be associated with only one Macie administrator account at a time. This means
  that an account can’t accept your invitation if it’s already associated with another
  Macie administrator account. The account must first disassociate from its current
  Macie administrator account.
- In an invitation-based organization, a member account can disassociate from its
  Macie administrator account at any time. If this happens, Macie continues to be enabled for
  the account but the account becomes a standalone Macie account. Macie doesn't
  notify you if a member account disassociates from your administrator account.
  However, the account continues to appear in your account inventory and it has a
  status of **Member resigned**.
- If you remove a member account from your organization, Macie continues to be enabled for
  the account. The account becomes a standalone Macie account.

## Responding to and

managing membership invitations

As a recipient of an invitation or a member of an invitation-based organization, keep
the following in mind when you respond to and manage invitations that you receive:

- Before you accept an invitation, ensure that you understand the [relationship between Macie administrator and
  member accounts](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").
- Your account can be associated with only one Macie administrator account at a time. If
  you accept an invitation and subsequently want to join another organization (by
  invitation or through AWS Organizations), you have to first disassociate your account
  from its current Macie administrator account. You can then join the other
  organization.
- To accept or decline an invitation, you have to enable Macie in the
  AWS Region that the invitation was sent from. The account that sent the
  invitation can’t enable Macie in that Region for you. Declining an invitation is
  optional. If you decline an invitation, you can optionally disable Macie in the
  applicable Region after you decline the invitation.
- If you’re a Macie administrator, you can’t accept an invitation to become a member
  account—an account can’t be a Macie administrator and member account at the same
  time. To become a member account, you must first disassociate your account from
  all of its member accounts by removing all member accounts from your current
  organization.
- Macie is a Regional service. If you accept an invitation, the association
  between your account and the Macie administrator account is Regional—the association
  exists only in the AWS Region that the invitation was sent from and accepted
  in.
- If you use Macie in multiple Regions, the Macie administrator account for your account
  has to be the same in all of those Regions. However, the Macie administrator has to send
  invitations to you separately in each Region, and you have to accept the
  invitations separately in each Region.
- You can disassociate your account from a Macie administrator account at any time.
  Similarly, your Macie administrator can remove your account from their organization at
  any time. If either happens:
  - Macie continues to be enabled for your account. Your account becomes a
    standalone Macie account.
  - Automated sensitive data discovery is disabled for your account, if it was enabled. This
    also disables access to existing statistical data, inventory data, and
    other information that Macie produced and directly provided while
    performing automated discovery for your account. You can enable automated discovery for your
    account again. However, this doesn't restore access to the existing
    data. Instead, Macie generates and maintains new data while it performs
    automated discovery for your account.

## Transitioning to

AWS Organizations

After you create an invitation-based organization in Macie, you can transition to
using AWS Organizations instead. To simplify the transition, we recommend that you designate the
existing, invitation-based administrator account as the Macie administrator account for the
organization in AWS Organizations.

If you do this, all currently associated member accounts continue to be members. If a member
account is part of the organization in AWS Organizations, the account’s association automatically
changes from **By invitation** to **Via AWS Organizations** in
Macie. If a member account isn’t part of the organization in AWS Organizations, the account’s
association continues to be **By invitation**. In both cases, the
accounts continue to be associated with the Macie administrator account as member accounts. For
sensitive data discovery, this also means that the accounts can continue to access
statistical and other data that Macie produced and directly provided while performing
automated sensitive data discovery for the accounts. In addition, if the Macie administrator configured sensitive data discovery jobs
to analyze data for the accounts, subsequent job runs will continue to include resources
that the accounts own.

We recommend this approach because a member account can be associated with only one
Macie administrator account at a time. If you designate a different account as the Macie administrator account
for an organization in AWS Organizations, the designated administrator won’t be able to manage
accounts that are already associated with another Macie administrator account by invitation. Each
member account must first disassociate from its current, invitation-based
administrator account. Only then can the Macie administrator for the AWS Organizations organization
add the member account to their organization and begin managing Macie for the
account.

After you integrate Macie with AWS Organizations and configure your organization in Macie, you
can optionally designate a different Macie administrator account for the organization. You can also
continue to use invitations to associate and manage member accounts that aren't part of
your organization in AWS Organizations.

For information about integrating Macie with AWS Organizations, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").
