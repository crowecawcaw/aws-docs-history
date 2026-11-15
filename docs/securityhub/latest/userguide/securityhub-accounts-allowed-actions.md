

# Allowed actions by administrator and member accounts in Security Hub CSPM
<a name="securityhub-accounts-allowed-actions"></a>

Administrator and member accounts have access to AWS Security Hub CSPM actions noted in the following tables. In the tables, the values have the following meanings:
+ **Any –** The account can perform the action for any member account under the same administrator.
+ **Current –** The account can perform the action only for itself (the account that you're currently signed in to).
+ **Dash –** Indicates that the account cannot perform the action.
+ **Through declarative policy –** The account can't perform the action directly through Security Hub CSPM. Instead, the setting comes from the account's effective Security Hub CSPM declarative policy, which the management account or an authorized delegated administrator manages in AWS Organizations.

As noted in the tables, allowed actions differ based on whether you integrate with AWS Organizations and how you manage accounts: with Security Hub CSPM declarative policies, central configuration, or local configuration. For information about these options, see [Managing accounts with AWS Organizations](securityhub-accounts.md#securityhub-orgs-account-management-overview).

Security Hub CSPM doesn't copy member account findings into the administrator account. In Security Hub CSPM, all findings are ingested into a specific Region for a specific account. In each Region, the administrator account can view and manage findings for their member accounts in that Region.

If you set an aggregation Region, the administrator account can view and manage member account findings from linked Regions that are replicated to the aggregation Region. For more information about cross-Region aggregation, see [Cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html).

The following tables specify the default permissions for administrator and member accounts. You can use custom IAM policies to further restrict access to Security Hub CSPM features and functions. For guidance and examples, see the blog post[ Aligning IAM policies to user personas for AWS Security Hub CSPM](https://aws.amazon.com/blogs/security/aligning-iam-policies-to-user-personas-for-aws-security-hub/).

## Allowed actions if you integrate with Organizations and use declarative policies
<a name="orgs-policies-allowed-actions"></a>

Administrator and member accounts can access Security Hub CSPM actions as follows if you integrate with Organizations and use Security Hub CSPM declarative policies. A declarative policy governs an account separately in each Region. In this table, a *governed member account* is a member account in a Region that its effective Security Hub CSPM declarative policy governs. A *self-managed member account* is a member account in a Region that no declarative policy governs.


| Action | Security Hub CSPM delegated administrator account (with delegated permissions for Security Hub CSPM declarative policies) | Governed member account | Self-managed member account | 
| --- | --- | --- | --- | 
| Create and manage Security Hub CSPM declarative policies | Any (requires an AWS Organizations delegation policy for the `SECURITYHUB_CSPM_POLICY` policy type) | – | – | 
| Create and manage Security Hub CSPM central configuration policies | – (can view and delete existing configuration policies) | – | – | 
| View organization accounts | Any | – | – | 
| Disassociate member account | Self-managed member accounts only | – | – | 
| Delete member account | Any non-organization account | – | – | 
| Enable and disable Security Hub CSPM | Through declarative policy for governed accounts, including the current account if a declarative policy governs it | Through declarative policy | Current (to disable, the account must first disassociate from the administrator account) | 
| View findings and finding history | Any | Current | Current | 
| Update findings | Any | Current | Current | 
| View insight results | Any | Current | Current | 
| View control details | Any | Current | Current | 
| Turn consolidated control findings on or off | Any | – | – | 
| Enable and disable standards | Through declarative policy for governed accounts, or current if no declarative policy governs the current account | Through declarative policy | Current | 
| Enable and disable controls | Through declarative policy for governed accounts, or current if no declarative policy governs the current account | Through declarative policy | Current | 
| Automatically enable new controls | Through declarative policy for governed accounts, or current if no declarative policy governs the current account | Through declarative policy | Current | 
| Customize control parameters | Through declarative policy for governed accounts, or current if no declarative policy governs the current account | Through declarative policy | Current | 
| Enable and disable integrations | Current | Current | Current | 
| Configure cross-Region aggregation | Any | – | – | 
| Configure custom actions | Current | Current | Current | 
| Configure automation rules | Any | – | – | 
| Configure custom insights | Current | Current | Current | 

**Note**  
The organization's management account can also create and manage Security Hub CSPM declarative policies. Declarative policies don't use a home Region or linked Regions, so the action to select a home Region and linked Regions doesn't apply. When a declarative policy enables Security Hub CSPM, Security Hub CSPM associates governed accounts with the delegated administrator automatically. When a declarative policy disables Security Hub CSPM, Security Hub CSPM removes the administrator and member associations for the affected accounts, including invitation-based associations. For more information, see [How declarative policies work in Security Hub CSPM](orgs-policies-how-they-work.md).

## Allowed actions if you integrate with Organizations and use central configuration
<a name="central-configuration-allowed-actions"></a>

Administrator and member accounts can access Security Hub CSPM actions as follows if you integrate with Organizations and use central configuration.


|  Action  |  Security Hub CSPM delegated administrator account  |  Centrally managed member account  |  Self-managed member account  | 
| --- | --- | --- | --- | 
| Create and manage Security Hub CSPM configuration policies | For self and centrally managed accounts | – | – | 
| View organization accounts | Any | – | – | 
| Disassociate member account | Any | – | – | 
| Delete member account | Any non-organization account | – | – | 
| Disable Security Hub CSPM | For current account and centrally managed accounts | – | Current (must be disassociated from the administrator account) | 
| View findings and finding history | Any | Current | Current | 
| Update findings | Any | Current | Current | 
| View insight results | Any | Current | Current | 
| View control details | Any | Current | Current | 
| Turn consolidated control findings on or off | Any | – | – | 
| Enable and disable standards | For current account and centrally managed accounts | – | Current | 
| Enable and disable controls | For current account and centrally managed accounts | – | Current | 
| Enable and disable integrations | Current | Current | Current | 
| Configure cross-Region aggregation | Any | – | – | 
| Select home Region and linked Regions | Any (must stop and restart central configuration to change home Region) | – | – | 
| Configure custom actions | Current | Current | Current | 
| Configure automation rules | Any | – | – | 
| Configure custom insights | Current | Current | Current | 

## Allowed actions if you integrate with Organizations and use local configuration
<a name="orgs-allowed-actions"></a>

Administrator and member accounts can access Security Hub CSPM actions as follows if you integrate with Organizations and use local configuration.


|  Action  |  Security Hub CSPM delegated administrator account  |  Member account  | 
| --- | --- | --- | 
| Create and manage Security Hub CSPM configuration policies | – | – | 
| View organization accounts | Any | – | 
| Disassociate member account | Any | – | 
| Delete member account | – | – | 
| Disable Security Hub CSPM | – | Current (if account is disassociated from delegated administrator) | 
| View findings and finding history | Any | Current | 
| Update findings | Any | Current | 
| View insight results | Any | Current | 
| View control details | Any | Current | 
| Turn consolidated control findings on or off | Any | – | 
| Enable and disable standards | Current | Current | 
| Automatically enable Security Hub CSPM and default standards in new organization accounts | For current account and new organization accounts | – | 
| Enable and disable controls | Current | Current | 
| Enable and disable integrations | Current | Current | 
| Configure cross-Region aggregation | Any | – | 
| Configure custom actions | Current | Current | 
| Configure automation rules | Any | – | 
| Configure custom insights | Current | Current | 

## Allowed actions for invitation-based accounts
<a name="manual-allowed-actions"></a>

Administrator and member accounts can access Security Hub CSPM actions as follows if you use the invitation-based method to manually manage accounts instead of integrating with AWS Organizations.


|  Action  |  Security Hub CSPM administrator account  |  Member account  | 
| --- | --- | --- | 
| Create and manage Security Hub CSPM configuration policies | – | – | 
| View organization accounts | Any | – | 
| Disassociate member account | Any | Current | 
| Delete member account | Any | – | 
| Disable Security Hub CSPM | Current (if there are no enabled member accounts) | Current (if account is disassociated from administrator account) | 
| View findings and finding history | Any | Current | 
| Update findings | Any | Current | 
| View insight results | Any | Current | 
| View control details | Any | Current | 
| Turn consolidated control findings on or off | Any | – | 
| Enable and disable standards | Current | Current | 
| Automatically enable Security Hub CSPM and default standards in new organization accounts | – | – | 
| Enable and disable controls | Current | Current | 
| Enable and disable integrations | Current | Current | 
| Configure cross-Region aggregation | Any | – | 
| Configure custom actions | Current | Current | 
| Configure automation rules | Any | – | 
| Configure custom insights | Current | Current | 