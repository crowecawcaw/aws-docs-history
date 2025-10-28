# Managing Security Hub CSPM for multiple accounts with

AWS Organizations

You can integrate AWS Security Hub CSPM with AWS Organizations, and then manage Security Hub CSPM for accounts in your organization.

To integrate Security Hub CSPM with AWS Organizations, you create an organization in AWS Organizations. The Organizations management account designates one account as the Security Hub CSPM delegated administrator for
the organization. The delegated administrator can then enable Security Hub CSPM for other accounts in the organization, add those accounts as Security Hub CSPM member accounts, and
take allowed actions on the member accounts. The Security Hub CSPM delegated administrator can enable and manage Security Hub CSPM for up to 10,000 member accounts.

The extent of the delegated administrator's configuration abilities depend on whether you use [central configuration](central-configuration-intro.md "central-configuration-intro.md").
With central configuration enabled, you don't need to configure Security Hub CSPM
separately in each member account and AWS Region. The delegated administrator can enforce specific Security Hub CSPM settings in specified member accounts and organizational
units (OUs) across Regions.

The Security Hub CSPM delegated administrator account can perform the following actions on member accounts:

- If using central configuration, centrally configure Security Hub CSPM for member accounts and OUs by
  creating Security Hub CSPM configuration policies. Configuration policies can be used to enable and disable
  Security Hub CSPM, enable and disable standards, and enable and disable controls.
- Automatically treat _new_ accounts as Security Hub CSPM member
  accounts when they join the organization. If you use central configuration, a configuration policy that
  is associated with an OU includes existing and new accounts that are part of the OU.
- Treat _existing_ organization accounts as Security Hub CSPM member
  accounts. This happens automatically if you use central configuration.
- Disassociate member accounts that belong to the organization. If you use central configuration, you can disassociate a member account only after
  designating it as self-managed. Alternatively, you can associate a configuration policy that disables Security Hub CSPM with specific centrally managed member accounts.
  If you don't opt in to central configuration, your organization uses the default configuration type called local configuration.
  Under local configuration, the delegated administrator has a more limited ability to enforce settings in member accounts. For more
  information, see [Understanding local configuration in Security Hub CSPM](local-configuration.md "local-configuration.md").

For a full list of actions that the delegated administrator can perform on member accounts, see
[Allowed actions by administrator and member accounts in Security Hub CSPM](securityhub-accounts-allowed-actions.md "securityhub-accounts-allowed-actions.md").

The topics in this section explain how to integrate Security Hub CSPM with AWS Organizations and how to manage Security Hub CSPM for
accounts in an organization. Where relevant,
each section identifies management benefits and differences for users of central configuration.

###### Topics

- [Integrating Security Hub CSPM with AWS Organizations](designate-orgs-admin-account.md "designate-orgs-admin-account.md")
- [Automatically enabling Security Hub CSPM in new organization accounts](accounts-orgs-auto-enable.md "accounts-orgs-auto-enable.md")
- [Manually enabling Security Hub CSPM in new organization accounts](orgs-accounts-enable.md "orgs-accounts-enable.md")
- [Disassociating Security Hub CSPM member accounts from your
  organization](accounts-orgs-disassociate.md "accounts-orgs-disassociate.md")
