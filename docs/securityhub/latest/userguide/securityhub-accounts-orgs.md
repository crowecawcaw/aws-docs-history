

# Managing Security Hub CSPM for multiple accounts with AWS Organizations

You can integrate AWS Security Hub CSPM with AWS Organizations, and then manage Security Hub CSPM for accounts in your organization.

To integrate Security Hub CSPM with AWS Organizations, you create an organization in AWS Organizations. The Organizations management account designates one account as the Security Hub CSPM delegated administrator for the organization. The delegated administrator can then enable Security Hub CSPM for other accounts in the organization, add those accounts as Security Hub CSPM member accounts, and take allowed actions on the member accounts. The Security Hub CSPM delegated administrator can enable and manage Security Hub CSPM for up to 10,000 member accounts.

How much the delegated administrator can configure depends on the configuration type that your organization uses: [AWS Organizations declarative policies](accounts-orgs-policies.md) (recommended), [local configuration](local-configuration.md), or [central configuration](central-configuration-intro.md) (legacy). For a comparison, see [Managing accounts with AWS Organizations](securityhub-accounts.md#securityhub-orgs-account-management-overview).

When a declarative policy governs an account, Security Hub CSPM associates the account with the delegated administrator automatically, without invitations. A declarative policy that disables Security Hub CSPM removes the account's administrator and member associations, including invitation-based associations, which Security Hub CSPM doesn't restore. For more information, see [How declarative policies work in Security Hub CSPM](orgs-policies-how-they-work.md).

The Security Hub CSPM delegated administrator account can perform the following actions on member accounts:
+ Centrally configure Security Hub CSPM for member accounts and organizational units (OUs) by using declarative policies. If your organization still uses central configuration, the delegated administrator uses Security Hub CSPM configuration policies instead.
+ Automatically treat *new* accounts as Security Hub CSPM member accounts when they join the organization. If you use declarative policies, accounts that join the organization or move into a covered OU inherit the effective policy.
+ Treat *existing* organization accounts as Security Hub CSPM member accounts. This happens automatically for accounts that a declarative policy governs.
+ Disassociate member accounts that belong to the organization. If a declarative policy governs a member account, the delegated administrator can't disassociate it. If you use central configuration, you can disassociate a member account only after designating it as self-managed. Alternatively, you can associate a configuration policy that disables Security Hub CSPM with specific centrally managed member accounts.

For a full list of actions that the delegated administrator can perform on member accounts, see [Allowed actions by administrator and member accounts in Security Hub CSPM](securityhub-accounts-allowed-actions.md).

The topics in this section explain how to integrate Security Hub CSPM with AWS Organizations and how to manage Security Hub CSPM for accounts in an organization. Where relevant, each section identifies management benefits and differences for users of declarative policies and central configuration.

**Topics**
+ [Integrating Security Hub CSPM with AWS Organizations](designate-orgs-admin-account.md)
+ [Managing accounts with declarative policies in Security Hub CSPM](accounts-orgs-policies.md)
+ [Automatically enabling Security Hub CSPM in new organization accounts](accounts-orgs-auto-enable.md)
+ [Manually enabling Security Hub CSPM in new organization accounts](orgs-accounts-enable.md)
+ [Disassociating Security Hub CSPM member accounts from your organization](accounts-orgs-disassociate.md)