# Managing account invitations with AWS Organizations

After you [create an organization](orgs_manage_org_create.md "orgs_manage_org_create.md") and [verify that you own the email address](about-email-verification.md "about-email-verification.md") associated with
the management account, you can invite existing AWS accounts to join your
organization. Use the AWS Organizations console to initiate
and manage invitations that you send to other accounts. You can send an invitation to
other accounts only from the management account of your organization.

When you invite an account, AWS Organizations sends an invitation to the account owner, who can decide to accept or decline the invitation.

If you are the administrator of an AWS account, you also can accept or decline an
invitation from an organization. If you accept, your account becomes a member of that
organization.

To create an account that automatically is part of an organization, see [Creating a member account in an organization
with AWS Organizations](orgs_manage_accounts_create.md "orgs_manage_accounts_create.md").

###### Important

All accounts in an organization must come from the same AWS partition as the
management account. Accounts in the commercial AWS Regions partition can't be
in an organization with accounts from the China Regions partition or accounts in
the AWS GovCloud (US) Regions partition.

###### Topics

- [Considerations](#impact_of_join "#impact_of_join")
- [Sending invitations](orgs_manage_accounts_invite-account.md "orgs_manage_accounts_invite-account.md")
- [Managing pending invitations](orgs_manage_accounts_manage-invites.md "orgs_manage_accounts_manage-invites.md")
- [Accepting or declining invitations](orgs_manage_accounts_accept-decline-invite.md "orgs_manage_accounts_accept-decline-invite.md")

## Considerations

**Limitations on the number of invite you can send per day**

For limitations on the number of invitations you can send per day, see [Maximum and minimum values](orgs_reference_limits.md#min-max-values "orgs_reference_limits.md#min-max-values"). Accepted invitations don't count against this quota.
As soon as one invitation is accepted, you can send another invitation that same day. Each
invitation must be responded to within 15 days, or it expires.

An invitation that is sent to an account counts against the quota of accounts in your
organization. The count is reset if the invited account declines, the management account
cancels the invitation, or the invitation expires.

**An account can only join one organization**

An account can only join one organization. If you receive multiple
invitations, you can accept only one.

**Billing history and reports stay with the management account**

Billing history and reports for all accounts stay with the management account in an
Organization. Before you move the account to a new Organization, export or back up any billing
and report histories for any member accounts that you want to keep. This might include
[Cost and Usage Reports](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md"), [Cost Explorer Reports](../../../cost-management/latest/userguide/ce-reports.md "../../../cost-management/latest/userguide/ce-reports.md"), [Savings Plans Reports](../../../savingsplans/latest/userguide/ce-sp-usingPR.md#ce-dl-pr "../../../savingsplans/latest/userguide/ce-sp-usingPR.md#ce-dl-pr"), and [Reserved Instance (RI) utilization and coverage](https://repost.aws/knowledge-center/ec2-ri-utilization-coverage-cost-explorer "https://repost.aws/knowledge-center/ec2-ri-utilization-coverage-cost-explorer").

**The management account is responsible for all charges accrued by member accounts**

After an account accepts the invitation to join an organization, the management account of the organization becomes responsible for all charges accrued by the new member
account. The payment method attached to the member account is no longer used. Instead, the
payment method attached to the management account of the organization pays for all charges
accrued by the member account.

**Organizations automatically creates the service-linked role `AWSServiceRoleForOrganizations`**

AWS Organizations creates a service-linked role called `AWSServiceRoleForOrganizations` to support integrations between AWS Organizations and other AWS
services. For more information, see [AWS Organizations and service-linked
roles](orgs_integrate_services.md#orgs_integrate_services-using_slrs "orgs_integrate_services.md#orgs_integrate_services-using_slrs"). The invited account must have
this role if your organization supports [all features](orgs_getting-started_concepts.md#feature-set-all "orgs_getting-started_concepts.md#feature-set-all"). You can delete this
role if the organization supports only the [consolidated billing](orgs_getting-started_concepts.md#feature-set-cb-only "orgs_getting-started_concepts.md#feature-set-cb-only") feature set.
If you delete this role and later you enable all features in your
organization, AWS Organizations recreates this role for the account.

**Organizations does not automatically create the IAM role `OrganizationAccountAccessRole`**

For invited member accounts, AWS Organizations doesn't automatically create the IAM
role [OrganizationAccountAccessRole](orgs_manage_accounts_access-cross-account-role.md "orgs_manage_accounts_access-cross-account-role.md"). This role grants users in the
management account administrative access to the member account. If you want to
enable that level of administrative control to an invited account, you can
manually add the role. For more information, see [Creating
OrganizationAccountAccessRole for an invited account with AWS Organizations](orgs_manage_accounts_create-cross-account-role.md "orgs_manage_accounts_create-cross-account-role.md").

###### Note

When you create an account in your organization instead of inviting an existing
account to join, AWS Organizations automatically creates the IAM role `OrganizationAccountAccessRole`by default.

**Policies attached to the root or OU that contain the account immediately apply**

If you have any policies attached to the root or
the organizational unit (OU) that contains the invited account, those policies immediately apply to
all users and roles in the invited account.

You can [enable service trust
for another AWS service](orgs_integrate_services_list.md "orgs_integrate_services_list.md") for your organization. When you do,
that trusted service can create service-linked roles or perform actions in
any member account in the organization, including an invited account.

**Organizations with only the consolidated billing feature set can still invite accounts**

You can invite an account to join an organization that has only the consolidated
billing features enabled. If you later want to enable all features for the
organization, invited accounts must approve the change.
