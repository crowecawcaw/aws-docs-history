# Managing multiple Macie accounts as an organization

If your AWS environment has multiple accounts, you can associate the Amazon Macie accounts in
your environment and centrally manage them as an organization in Macie. With this
configuration, a designated Macie administrator can assess and monitor the overall security posture
of your organization’s Amazon Simple Storage Service (Amazon S3) data estate, and discover sensitive data in your
organization’s S3 buckets. The administrator can also perform various account management and
administration tasks at scale, such as monitoring estimated usage costs and assessing
account quotas.

In Macie, an organization consists of a designated Macie administrator account and one or more
associated member accounts. You can associate the accounts in two ways, by integrating Macie
with AWS Organizations or by sending and accepting membership invitations in Macie. We recommend that
you integrate Macie with AWS Organizations.

AWS Organizations is a global account
management service that enables AWS administrators to consolidate and centrally manage
multiple AWS accounts. It provides account management and consolidated billing features that
are designed to support budgetary, security, and compliance needs. It’s offered at no
additional charge and it integrates with multiple AWS services, including Macie, AWS Security Hub CSPM,
and Amazon GuardDuty. To learn more, see the [AWS Organizations User
Guide](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

If you prefer to centrally manage multiple Macie accounts without using AWS Organizations, you can use
membership invitations instead. If you send an invitation and it’s accepted by another
account, your account becomes the Macie administrator account for the other account. If you receive and
accept an invitation, your account becomes a Macie member account and the Macie administrator account can
access and manage certain settings, data, and resources for your Macie account.

###### Topics

- [Macie administrator and member account
  relationships](accounts-mgmt-relationships.md "accounts-mgmt-relationships.md")
- [Managing multiple Macie accounts with AWS Organizations](accounts-mgmt-ao.md "accounts-mgmt-ao.md")
- [Managing multiple Macie accounts by
  invitation](accounts-mgmt-invitations.md "accounts-mgmt-invitations.md")
