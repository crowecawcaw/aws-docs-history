

# Managing administrator and member accounts in Security Hub CSPM
<a name="securityhub-accounts"></a>

If your AWS environment has multiple accounts, you can treat the accounts that use AWS Security Hub CSPM as member accounts and associate them with a single administrator account. The administrator can monitor your overall security posture and take [allowed actions](securityhub-accounts-allowed-actions.md) on member accounts. The administrator can also perform various account management and administration tasks at scale, such as monitoring estimated usage costs and assessing account quotas.

You can associate member accounts with an administrator in two ways, by integrating Security Hub CSPM with AWS Organizations or by manually sending and accepting membership invitations in Security Hub CSPM.

## Managing accounts with AWS Organizations
<a name="securityhub-orgs-account-management-overview"></a>

AWS Organizations is a global account management service that allows AWS administrators to consolidate and manage multiple AWS accounts. It provides account management and consolidated billing features that are designed to support budgetary, security, and compliance needs. It's offered at no additional charge, and it integrates with multiple AWS services, including AWS Security Hub, AWS Security Hub CSPM, Amazon Macie, and Amazon GuardDuty. For more information, see the [*AWS Organizations User Guide*](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html).

When you integrate Security Hub CSPM and AWS Organizations, the Organizations management account designates a Security Hub CSPM delegated administrator. Security Hub CSPM is automatically enabled in the delegated administrator account in the AWS Region in which it was designated.

After you designate a delegated administrator, you can configure Security Hub CSPM for the accounts in your organization in the following ways. We recommend declarative policies.


| Approach | How it works | When to use it | 
| --- | --- | --- | 
| [Declarative policies](accounts-orgs-policies.md) (recommended) | An AWS Organizations declarative policy of type `SECURITYHUB_CSPM_POLICY` centrally enables and configures Security Hub CSPM, standards, controls, and control parameters for the organization root, organizational units (OUs), or accounts in each AWS Region. Accounts that join the organization or move into a covered OU inherit the policy. Security Hub CSPM associates governed accounts with the delegated administrator automatically. | Use declarative policies for all multi-account configuration in an organization. | 
| [Local configuration](local-configuration.md) | Local configuration is the default configuration type after you integrate with Organizations. The delegated administrator can automatically enable Security Hub CSPM and [default security standards](securityhub-auto-enabled-standards.md) in new organization accounts in the current Region. Existing accounts don't use these settings, and each account configures Security Hub CSPM, standards, and controls separately in each Region. | Use local configuration for accounts and Regions that no declarative policy governs. | 
| [Central configuration](central-configuration-intro.md) (legacy) | The delegated administrator creates Security Hub CSPM configuration policies and associates them with accounts and OUs. Declarative policies are replacing central configuration. | If your organization uses central configuration, migrate to declarative policies. For more information, see [Declarative policies and central configuration in Security Hub CSPM](orgs-policies-and-central-config.md). | 

**Important**  
You can't use declarative policies and central configuration in the same organization at the same time. When you attach the first Security Hub CSPM policy to any target, Security Hub CSPM disables central configuration for the entire organization. For more information, see [Declarative policies and central configuration in Security Hub CSPM](orgs-policies-and-central-config.md).

## Managing accounts manually by invitation
<a name="securityhub-manual-account-management-overview"></a>

You must manually manage member accounts by invitation in Security Hub CSPM if you have a standalone account or if you don't integrate with Organizations. A standalone account can't integrate with Organizations, so it's necessary to manage it manually. If you add more accounts in the future, we recommend integrating with AWS Organizations and using [declarative policies](accounts-orgs-policies.md).

When you use manual account management, you designate an account to be the Security Hub CSPM administrator. The administrator account can view data in member accounts and take certain actions on member account findings. The Security Hub CSPM administrator invites other accounts to be member accounts, and the administrator-member relationship is established when a prospective member account accepts the invitation.

Manual account management doesn't support the use of configuration policies. Without configuration policies, the administrator can't centrally customize Security Hub CSPM by configuring variable settings for different accounts. Instead, each organization account must enable and configure Security Hub CSPM for itself separately in each Region. This can make it more difficult and time consuming to ensure adequate security coverage across all of the accounts and Regions in which you use Security Hub CSPM. It can also cause configuration drift as member accounts can specify their own settings without input from the administrator.

To manage accounts by invitation, see [Managing accounts by invitation in Security Hub CSPM](account-management-manual.md).