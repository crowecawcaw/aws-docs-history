# Migrate an account to another

organization with AWS Organizations

You can migrate an AWS account from one organization to another at any time. For
example, migrating an account can be helpful in the case of a merger and acquisition when
you need to consolidate one or more AWS accounts from multiple organizations into one
organization.

Whatever your use case, migrating an account between organizations requires for you to
remove the account from the old organization, for you to make the account a standalone
account, and for the account to accept the invitation from the new organization to join the
new organization. Your workloads and services will continue to operate according to your
specifications during the migration. However, it is important to be aware of any
dependencies you might have in your organization.

###### Note

**Closed or suspended accounts cannot be migrated**

You cannot migrate a closed or suspended account.
To reactive an account,
contact [Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

**Four day age requirement**

To migrate an account that you created in an organization, you must wait until at least four days after the account was created.
Invited accounts aren't subject to this waiting period.

**Replicating data between accounts**

The following AWS Prescriptive Guidance provides
information about strategies for replicating data between AWS accounts:
[Resource replication or migration between AWS accounts](../../../prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/resource-migration.md "../../../prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/resource-migration.md").

## What you need to do before migrating

an account

Before migrating your AWS account from one organization to another, make
sure you have completed the following steps.

### Step 1: Check that you have the necessary

IAM permissions to migrate an account

Make sure you have applied the necessary permissions for migrating an
account to the respective
organizations.

**To leave an organization, you must have the following permissions:**

- `organizations:DescribeOrganization` (console
  only)
- `organizations:LeaveOrganization`
  For more information, see [Leave an organization from your member account](orgs_manage_accounts_leave-as-member.md "orgs_manage_accounts_leave-as-member.md").

**To invite an AWS account to join an organization, you must
have the following permissions:**

- `organizations:DescribeOrganization` (console
  only)
- `organizations:InviteAccountToOrganization`
  For more information, see [Inviting an AWS account to join your
  organization](orgs_manage_accounts_invites.md "orgs_manage_accounts_invites.md").

**To migrate an account, you cannot have IAM policies or service control policies that prevent migration**

If you are the management account or a delegated administrator, you can
control access to AWS resources by attaching permissions policies to IAM
identities (users, groups, and roles) within an organization. For more
information, see [IAM policies for AWS Organizations](orgs_permissions_iam-policies.md "orgs_permissions_iam-policies.md").

Before migrating an account:

- Check that there are no IAM policies or service control policies
  (SCPs) that prevent you from migrating the account.
- Identify existing IAM policies and service control
  policies (SCPs) that you need to replicate in the
  organization where you are migrating the account.
- Identify existing IAM policies which specify your organization ID.
  For example, [`aws:PrincipalOrgID`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid").
  For more information, see [Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the _IAM User Guide_ and [Service control policies (SCPs)](orgs_manage_policies_scps.md "orgs_manage_policies_scps.md").

### Step 2: Check that you have removed IAM permissions that enable access to the old management account

Make sure you have removed IAM permissions that enable access
to the old management account such as `OrganizationAccountAccessRole`.

When you remove a member account from an organization, any IAM role that
was created to enable access by the organization's management account isn't
automatically deleted. If you want to terminate this access from the former
organization's management account, then you must manually delete the IAM role.

For information about how to delete a role, see [Deleting roles or instance
profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the _IAM User Guide_.

### Step 3: Check your phone verification and payment method

The migrating account
must operate as a standalone account for a period of time before migrating to the new organization.

**To allow an account operate as a standalone account, check the following:**

- Make sure your phone verification is up-to-date.
- Make sure have have added a valid payment method
  for the account to address any charges that are incurred
  while the account is migrating.
- If you use invoicing
  for your payment method, make sure your invoice is up-to-date.

### Step 4: Back up all reports

Make sure to export or back up reports from the management account, especially
billing reports. Organizational level reports and history are not stored
when you migrate an account. It is recommended that you do a full export of
all billing history. You can still access reports for member account such as
AWS CloudTrail Event history and account billing history.

###### Important

All organizational level reporting and history, such as organizational billing information in
the management account, will be deleted after an account is removed from
an organization.

For more information, see [Cost and Usage Reports](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md"), [Cost Explorer Reports](../../../cost-management/latest/userguide/ce-reports.md "../../../cost-management/latest/userguide/ce-reports.md"), [Savings Plans Reports](../../../savingsplans/latest/userguide/ce-sp-usingPR.md#ce-dl-pr "../../../savingsplans/latest/userguide/ce-sp-usingPR.md#ce-dl-pr"), and [Reserved Instance (RI) utilization and coverage](https://repost.aws/knowledge-center/ec2-ri-utilization-coverage-cost-explorer "https://repost.aws/knowledge-center/ec2-ri-utilization-coverage-cost-explorer").

### Step 5: Check for organization dependencies

Make sure the migrating account does not have any organization-related dependencies.

**Dependencies to check:**

- If the account is a delegated
  administrator, you must deregister the delegated
  administrator permissions before migrating the account.
  For more information, see [Services you can use with AWS Organizations](orgs_integrate_services_list.md "orgs_integrate_services_list.md").
- If the account is the management
  account, you must remove all member accounts from the organization and delete the organization before migrating. After you have deleted the organization, your management account
  will operate as a standalone account. After migration,
  the management account will be a member account of the new organization.
  For more information, see [Deleting an organization](orgs_manage_org_delete.md "orgs_manage_org_delete.md").
- If any IAM permissions
  depend on the account,
  you will need to adjust the permissions for the old organization
  after you have migrated the account
  to the new organization in order for the old organization to function as before. For more information, see [Managing access permissions for your organization](orgs_permissions_overview.md "orgs_permissions_overview.md").
- If you are using any account or
  organizational unit (OU) tags, you will need to recreate the tags in the new organization.

### (Optional) Step 6: Review guidance if you use AWS Control Tower

If you are migrating
an account to or from an organization managed by
AWS Control Tower, review the following AWS Prescriptive Guidance: [Migrate an AWS member account from AWS Organizations to AWS Control Tower](../../../prescriptive-guidance/latest/patterns/migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower.md "../../../prescriptive-guidance/latest/patterns/migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower.md").

## What you need to do to migrate an account

The migration process requires for the new organization to send an invitation to the
migrating account, for the old organization to remove the migration account, and for the migrating account to accept the invitation from the new
organization to join the new organization.

###### To migrate an account

1. Send an invitation from the management account of the new organization to the
   migrating account. You should send the invitation to the account before it
   leaves the old organization. This helps to minimize the costs incurred when the
   migrating account temporarily operates as a standalone account. For information
   about inviting accounts, see [Inviting an AWS account to join your organization](orgs_manage_accounts_invites.md "orgs_manage_accounts_invites.md").
2. Remove the migrating account from the old organization. You can [remove a member account from your organization](orgs_manage_accounts_remove-member-account.md "orgs_manage_accounts_remove-member-account.md") using the management
   account or [leave an organization from as a member account](orgs_manage_accounts_leave-as-member.md "orgs_manage_accounts_leave-as-member.md").
3. Accept the invitation to join the new organization. For more information, see
   [Accepting an invitation from an organization](orgs_manage_accounts_invites.md#orgs_manage_accounts_accept-decline-invite "orgs_manage_accounts_invites.md#orgs_manage_accounts_accept-decline-invite"). Accounts that are
   migrated from one another organization to another will be automatically added to
   the root of the new organization. Before moving an account to an organizational
   unit (OU) in the new organization, it is recommended that you check that migrating account has the appropriate organization policies and OU
   permissions.
4. If you want to migrate the management account, you must [remove
   all member accounts](orgs_manage_accounts_remove.md "orgs_manage_accounts_remove.md") from the organization and [delete the
   organization](orgs_manage_org_delete.md "orgs_manage_org_delete.md") before migrating the management account to the new
   organization. After you have deleted the old organization, your management
   account will operate as a standalone account and can accept the invitation from
   the new organization to join the new organization. If you accept the invitation,
   the management account will be a member account of the new organization.

## What you need to do after migrating

an account

After migration your account from one organization to another, make sure you have
completed the following steps.

###### Post-migration review

1. Evaluate all of the [billing tool configurations](../../../whitepapers/latest/cost-optimization-laying-the-foundation/reporting-cost-optimization-tools.md "../../../whitepapers/latest/cost-optimization-laying-the-foundation/reporting-cost-optimization-tools.md") for the migrated account, such as cost categories, budgets, and billing alarms.
2. Review and update the following monetary information for any accounts that you migrated
   from one organization to another:
   1. If necessary, [update the tax settings](https://repost.aws/knowledge-center/update-tax-registration-number "https://repost.aws/knowledge-center/update-tax-registration-number") on the account.
   2. Make sure the [Support plan](../../../awsaccountbilling/latest/aboutv2/consolidatedbilling-support.md "../../../awsaccountbilling/latest/aboutv2/consolidatedbilling-support.md") for migrating account matches payer account for
      the new organization.
   3. Review any possible [tax exemptions](https://aws.amazon.com/tax-help/united-states/ "https://aws.amazon.com/tax-help/united-states/") that you might
      want to apply to the account you migrated.

3. Validate and confirm existing IAM policies and
   service control policies (SCPs) for the migrated account.
   For example, you might need to update the organization ID
   for some IAM policies to reflect the new organization.
4. Update [cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") for new organization where you migrated the account.
   You will need to update all the previous cost allocation tags collected by account you migrated.
5. Any [Reserved Instances](../../../awsaccountbilling/latest/aboutv2/ri-behavior.md "../../../awsaccountbilling/latest/aboutv2/ri-behavior.md") and [Saving Plans](../../../savingsplans/latest/userguide/what-is-savings-plans.md "../../../savingsplans/latest/userguide/what-is-savings-plans.md") will
   migrate along with the account. These are not retained in the old organization.
   Contact Support if these need to be transferred to the old organization.
