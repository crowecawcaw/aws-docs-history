# Transitioning to Organizations to manage accounts in Security Hub CSPM

When you manage accounts manually in AWS Security Hub CSPM, you must invite prospective member accounts and
configure each member account separately in each AWS Region.

By integrating Security Hub CSPM and AWS Organizations, you can eliminate the need to send invitations and gain more
control over how Security Hub CSPM is configured and customized in your organization. For this reason, we recommend using AWS Organizations
instead of Security Hub CSPM invitations to manage your member accounts. For information, see
[Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

It's possible to use a combined approach in which you use the AWS Organizations integration, but also manually invite accounts
outside of your organization. However, we recommend exclusively using the Organizations integration. [Central configuration](central-configuration-intro.md "central-configuration-intro.md"), a feature which helps
you manage Security Hub CSPM across multiple accounts and Regions, is only available when you integrate with Organizations.

This section covers how you can transition from manual invitation-based account management to managing accounts with
AWS Organizations.

## Integrating Security Hub CSPM with AWS Organizations

First, you must integrate Security Hub CSPM and AWS Organizations.

You can integrate these services by completing the following steps:

- Create an organization in AWS Organizations. For instructions, see [Create an organization](../../../organizations/latest/userguide/orgs_manage_org_create.md#create-org "../../../organizations/latest/userguide/orgs_manage_org_create.md#create-org") in the _AWS Organizations User Guide_.
- From the Organizations management account, designate a Security Hub CSPM delegated administrator account.

###### Note

The organization management account _cannot_ be set as the DA account.

For detailed instructions, see [Integrating Security Hub CSPM with AWS Organizations](designate-orgs-admin-account.md "designate-orgs-admin-account.md").

By completing the preceding steps, you grant [trusted access](../../../organizations/latest/userguide/services-that-can-integrate-securityhub.md#integrate-enable-ta-securityhub "../../../organizations/latest/userguide/services-that-can-integrate-securityhub.md#integrate-enable-ta-securityhub") for Security Hub CSPM in AWS Organizations. This also enables Security Hub CSPM in the current AWS Region for the delegated administrator account.

The delegated administrator can manage the organization in Security Hub CSPM, primarily by adding the
organization’s accounts as Security Hub CSPM member accounts. The administrator can also
access certain Security Hub CSPM settings, data, and resources for those accounts.

When you transition to account management using Organizations, invitation-based accounts don't automatically become Security Hub CSPM members.
Only the accounts that you add to your new organization can become Security Hub CSPM members.

After activating the integration, you can manage accounts with Organizations. For information, see [Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").
Account management varies based on your organization's configuration type.
