# Managing multiple Macie accounts by

invitation

###### Note

We recommend using AWS Organizations instead of Macie invitations to manage member
accounts. For more information, see [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md").

You can centrally manage multiple Amazon Macie accounts in two ways, by integrating Macie
with AWS Organizations or by using membership invitations. If you use membership invitations, a
designated Macie administrator can manage Macie for as many as 1,000 accounts. The administrator can
also access Amazon Simple Storage Service (Amazon S3) inventory data and discover sensitive data in S3 buckets that
the accounts own. For details about tasks that the administrator can perform, see [Macie administrator and member account
relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md").

In an invitation-based organization, you associate Macie accounts with each other by
sending and accepting membership invitations in Macie. If you send an invitation and it’s
accepted by another account, you become the Macie administrator for the other account and the other
account becomes a member account in your organization. If you receive and accept an
invitation, your account becomes a member account and the Macie administrator can access certain
Macie settings, data, and resources for your account.

If you create an invitation-based organization in Macie, you can subsequently [transition to using
AWS Organizations](accounts-mgmt-invitations-notes.md#accounts-mgmt-invitations-notes-transition-ao "accounts-mgmt-invitations-notes.md#accounts-mgmt-invitations-notes-transition-ao") instead. You can also use both methods at the same time to manage
multiple Macie accounts. For example, if your AWS environment includes test accounts, you
might exclude the accounts from your organization in AWS Organizations and manage them separately by
invitation.

The topics in this section explain how to create and participate in an invitation-based
organization, and how to perform various administrative tasks for the organization.

###### Topics

- [Considerations and
  recommendations](accounts-mgmt-invitations-notes.md "accounts-mgmt-invitations-notes.md")
- [Creating and managing an
  organization](accounts-mgmt-invitations-administer.md "accounts-mgmt-invitations-administer.md")
- [Reviewing organization
  accounts](accounts-mgmt-invitations-review.md "accounts-mgmt-invitations-review.md")
- [Changing the administrator
  account](accounts-mgmt-invitations-admin-change.md "accounts-mgmt-invitations-admin-change.md")
- [Managing your
  membership in an organization](accounts-mgmt-invitations-membership-manage.md "accounts-mgmt-invitations-membership-manage.md")
