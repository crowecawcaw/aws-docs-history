# Recommendations for

managing multiple accounts in Security Hub CSPM

The following section summarizes some restrictions and recommendations to keep in mind
when managing member accounts in AWS Security Hub CSPM.

## Maximum number of member

accounts

If you use the integration with AWS Organizations, Security Hub CSPM supports up to 10,000 member accounts per delegated administrator account in each
AWS Region. If you enable and manage Security Hub CSPM manually, Security Hub CSPM supports up to 1,000 member account invitations per administrator account in each
Region.

## Creating administrator-member relationships

###### Note

If you use the Security Hub CSPM integration with AWS Organizations, and haven't manually invited any
member accounts, this section doesn't apply to you.

An account can't be an administrator account and a member account at the same
time.

A member account can only be associated with one administrator account. If an
organization account is enabled by the Security Hub CSPM administrator account, the account cannot
accept an invitation from another account. If an account has already accepted an
invitation, the account cannot be enabled by the Security Hub CSPM administrator account for the
organization. It also cannot receive invitations from other accounts.

For the manual invitation process, accepting a membership invitation is
optional.

### Membership through AWS Organizations

If you integrate Security Hub CSPM with AWS Organizations, the Organizations management account can
designate a delegated administrator (DA) account for Security Hub CSPM. The organization
management account can't be set as the DA in Organizations. While this is permitted in Security Hub CSPM,
we recommend that the Organizations management account should _not_ be the DA.

We recommend that you choose the same DA account in all Regions. If you use [central configuration](central-configuration-intro.md "central-configuration-intro.md"), then Security Hub CSPM sets the same DA
account in all Regions in which you configure Security Hub CSPM for
your organization.

We also recommend that you choose the same DA account across AWS security and
compliance services to help you manage security-related issues in a single pane of
glass.

### Membership by invitation

For member accounts created by invitation, the administrator-member account
association is created only in the Region that the invitation is sent from. The
administrator account must enable Security Hub CSPM in each Region that you want to use it in.
The administrator account then invites each account to become a member account
in that Region.

###### Note

We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts.

## Coordinating administrator accounts

across services

Security Hub CSPM aggregates findings from various AWS services, such as Amazon GuardDuty, Amazon Inspector, and
Amazon Macie. Security Hub CSPM also allows users to pivot from a GuardDuty finding to start an
investigation in Amazon Detective.

However, the administrator-member relationships that you set up in these other
services do not automatically apply to Security Hub CSPM. Security Hub CSPM recommends that you use the same
account as the administrator account for all of these services. This administrator
account should be an account that is responsible for security tools. The same account
should also be the aggregator account for AWS Config.

For example, a user from the GuardDuty administrator account A can see findings for GuardDuty
member accounts B and C on the GuardDuty console. If account A then enables Security Hub CSPM, users
from account A do _not_ automatically see GuardDuty
findings for accounts B and C in Security Hub CSPM. A Security Hub CSPM administrator-member relationship is
also required for these accounts.

To do this, make account A the Security Hub CSPM administrator account and enable accounts B and C
to become Security Hub CSPM member accounts.
