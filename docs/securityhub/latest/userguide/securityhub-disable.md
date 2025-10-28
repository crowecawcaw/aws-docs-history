# Disabling Security Hub CSPM

You can disable AWS Security Hub CSPM by using the Security Hub CSPM console or the Security Hub API. If you disable
Security Hub CSPM, you can enable it again later.

If your organization uses central configuration, the delegated Security Hub CSPM administrator can
create configuration policies that disable Security Hub CSPM for specific accounts and organizational
units (OUs) and keep Security Hub CSPM enabled for others. Configuration policies affect the home Region
and all linked Regions. For more information, see [Understanding central configuration in Security Hub CSPM](central-configuration-intro.md "central-configuration-intro.md").

If you disable Security Hub CSPM for an account, the following occurs:

- All Security Hub CSPM standards and controls are disabled for the account.
- Security Hub CSPM stops generating, updating, and ingesting findings for the account.
- After 30 days, Security Hub CSPM permanently deletes all existing archived findings for the
  account. The findings cannot be recovered by using Security Hub CSPM.
- After 90 days, Security Hub CSPM permanently deletes all existing active findings for the
  account. The findings cannot be recovered by using Security Hub CSPM.
- After 90 days, Security Hub CSPM permanently deletes all existing insights and Security Hub CSPM
  configuration settings for the account. The data and settings cannot be
  recovered.
  To retain existing findings, you can export the findings to an S3 bucket before you
  disable Security Hub CSPM. You can do this by using a custom action with an Amazon EventBridge rule. For more
  information, see [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md").

If you re-enable Security Hub CSPM within 90 days of disabling it for an account, you regain access to
existing active findings, as well as insights and Security Hub CSPM configuration settings for the
account. If you re-enable Security Hub CSPM within 30 days, you also regain access to existing archived
findings for the account. However, existing findings might be inaccurate because they will
reflect the state of your AWS environment when you disabled Security Hub CSPM. In addition, as you
re-enable individual standards and controls, Security Hub CSPM might initially generate duplicate
findings for specific AWS resources, depending on the standards and controls that you
enable. For these reasons, we recommend that you do one of the following:

- Change the workflow status of all existing findings to `RESOLVED`
  before you disable Security Hub CSPM. For more information, see [Setting the workflow status of findings](findings-workflow-status.md "findings-workflow-status.md").
- Disable all standards at least six days before you disable Security Hub CSPM. Security Hub CSPM then
  archives all existing findings on a best-effort basis, typically within three to
  five days. For more information, see [Disabling a standard](disable-standards.md "disable-standards.md").
  You can't disable Security Hub CSPM in the following cases:

- Your account is the delegated Security Hub CSPM administrator account for an organization. If
  you use central configuration, you can't associate a configuration policy that
  disables Security Hub CSPM for the delegated administrator account. The association can succeed
  for other accounts, but Security Hub CSPM doesn't apply the policy to the delegated
  administrator account.
- Your account is a Security Hub CSPM administrator account by invitation, and you have member
  accounts. Before you can disable Security Hub CSPM, you must disassociate all of your member
  accounts. To learn how, see [Disassociating member accounts in Security Hub CSPM](securityhub-disassociate-members.md "securityhub-disassociate-members.md").
  Before the owner of a member account can disable Security Hub CSPM, the account must disassociate from
  its administrator account. For an organization account, only the administrator account can
  disassociate a member account. For more information, see [Disassociating Security Hub CSPM member accounts from your
  organization](accounts-orgs-disassociate.md "accounts-orgs-disassociate.md"). For a manually invited account, either the
  administrator account or the member account can disassociate the account. For more
  information, see [Disassociating member accounts in Security Hub CSPM](securityhub-disassociate-members.md "securityhub-disassociate-members.md") or [Disassociating from a Security Hub CSPM administrator account](securityhub-disassociate-from-admin.md "securityhub-disassociate-from-admin.md"). Disassociation isn't required if you
  use central configuration because the Security Hub CSPM administrator can create a policy that disables
  Security Hub CSPM for specific member accounts.

When you disable Security Hub CSPM for an account, it's disabled only in the current AWS Region.
However, if you use central configuration to disable Security Hub CSPM for specific accounts, it's
disabled in the home Region and all linked Regions.

To disable Security Hub CSPM, choose your preferred method and follow the steps.

Security Hub CSPM console
Follow these steps to disable Security Hub CSPM by using the console.

###### To disable Security Hub CSPM

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, under **Settings**, choose
   **General**.
3. In the **Disable Security Hub CSPM** section, choose
   **Disable Security Hub CSPM**.
4. When prompted for confirmation, choose **Disable
   Security Hub CSPM**.

Security Hub API
To disable Security Hub CSPM programmatically, use the [DisableSecurityHub](../../1.0/APIReference/API_DisableSecurityHub.md "../../1.0/APIReference/API_DisableSecurityHub.md") operation of the AWS Security Hub API. Or, if you're
using the AWS CLI, run the [disable-security-hub](../../../cli/latest/reference/securityhub/disable-security-hub.md "../../../cli/latest/reference/securityhub/disable-security-hub.md") command. For example, the following command
disables Security Hub CSPM in the current AWS Region:

```
`$` `aws securityhub disable-security-hub`
```
