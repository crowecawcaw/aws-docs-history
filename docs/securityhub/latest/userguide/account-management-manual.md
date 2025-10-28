# Managing accounts by invitation in Security Hub CSPM

You can centrally manage multiple AWS Security Hub CSPM accounts in two ways, by integrating Security Hub CSPM
with AWS Organizations or by manually sending and accepting membership invitations. You must use the
manual process if you have a standalone account or you don't integrate with AWS Organizations. In
manual account management, the Security Hub CSPM administrator invites accounts to become members. The
administrator-member relationship is established when a prospective member accepts the
invitation. A Security Hub CSPM administrator account can manage Security Hub CSPM for up 1,000 invitation-based
member accounts.

###### Note

If you create an invitation-based organization in Security Hub CSPM, you can subsequently [transition to using
AWS Organizations](accounts-transition-to-orgs.md "accounts-transition-to-orgs.md") instead. If you have more than one member account, we recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts.
For information, see [Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

Cross-Region aggregation of findings and other data is available for
accounts that you invite through the manual invitation process. However, the administrator must invite the
member account from the aggregation Region and all linked Regions in order for cross-Region aggregation to work. In addition,
the member account must have Security Hub CSPM enabled in the aggregation Region and all linked Regions to give the administrator
the ability to view findings from the member account.

Configuration policies aren't supported for manually-invited
member accounts. Instead, you must configure Security Hub CSPM settings separately in each member account and AWS Region when you use
the manual invitation process.

You must also use the manual invitation-based process for accounts that don't belong to your organization. For
example, you might not include a test account in your organization. Or, you might want to
consolidate accounts from multiple organizations under a single Security Hub CSPM administrator account.
The Security Hub CSPM administrator account must send invitations to accounts that belong to other
organizations.

On the **Configuration** page of the Security Hub CSPM console, accounts that were
added by invitation are listed in the **Invitation accounts** tab. If you
use [central configuration](central-configuration-intro.md "central-configuration-intro.md"), but also
invite accounts outside of your organization, you can view findings from invitation-based
accounts in this tab. However, the Security Hub CSPM administrator can't configure invitation-based
accounts across Regions through the use of configuration policies.

The topics in this section explain how to manage member accounts through invitations.

###### Topics

- [Adding and inviting member accounts in Security Hub CSPM](securityhub-accounts-add-invite.md "securityhub-accounts-add-invite.md")
- [Responding to an invitation to be a Security Hub CSPM
  member account](securityhub-invitation-respond.md "securityhub-invitation-respond.md")
- [Disassociating member accounts in Security Hub CSPM](securityhub-disassociate-members.md "securityhub-disassociate-members.md")
- [Deleting member accounts in Security Hub CSPM](securityhub-delete-member-accounts.md "securityhub-delete-member-accounts.md")
- [Disassociating from a Security Hub CSPM administrator account](securityhub-disassociate-from-admin.md "securityhub-disassociate-from-admin.md")
- [Transitioning to Organizations to manage accounts in Security Hub CSPM](accounts-transition-to-orgs.md "accounts-transition-to-orgs.md")
