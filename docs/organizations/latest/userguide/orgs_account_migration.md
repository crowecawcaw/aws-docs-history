

# Migrate an account to another organization with AWS Organizations
<a name="orgs_account_migration"></a>

You can migrate an AWS account from one organization to another at any time. For example, migrating an account can be helpful in the case of a merger and acquisition when you need to consolidate one or more AWS accounts from multiple organizations into one organization.

Whatever your use case, migrating an account between organizations requires you to send an invite from the management account of the new organization, and to use the invited account to accept the invite to join the new organization.

**Note**  
**Closed or suspended accounts cannot be migrated.**  
You cannot migrate a closed or suspended account. To reactive an account, contact [Support](https://aws.amazon.com/contact-us/).  
**Four-day age requirement for created member accounts in an organization**  
To migrate an account that you created in an organization, you must wait until at least four days after the account was created. Invited accounts are not subject to this waiting period.  
**Seven-day age requirement for the organization**  
To migrate an account to a new organization, you must wait until at least seven days after the organization was created.  
**Replicating data between accounts**  
The following AWS Prescriptive Guidance provides information about strategies for replicating data between AWS accounts: [Resource replication or migration between AWS accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/resource-migration.html).

## What you need to do before migrating an account
<a name="migrate-account-prerequistes"></a>

Before migrating your AWS account from one organization to another, make sure you have completed the following steps.

### Step 1: Check that you have the necessary IAM permissions to migrate an account
<a name="migrate-account-step-1"></a>

#### Step 1
<a name="collapsible-migrate-account-step-1"></a>

Make sure you have applied the necessary permissions for migrating an account to the respective organizations.

**Note**  
With direct account transfer, you migrate an account by having the new organization send an invitation and the migrating account accept it. The account doesn't need to leave its current organization or operate as a standalone account first. For more information, see [AWS Organizations now supports direct account transfers](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-organizations-direct-account-transfers/).  
You need the `organizations:LeaveOrganization` permission only if you want an account to leave its organization and become a standalone account, rather than migrate directly to another organization.

**To have an account leave an organization and become a standalone account, you must have the following permissions:**
+ `organizations:DescribeOrganization` (console only)
+ `organizations:LeaveOrganization`

For more information, see [Leave an organization from your member account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_leave-as-member.html).

**To invite an AWS account to join an organization, you must have the following permissions:**
+ `organizations:DescribeOrganization` (console only)
+ `organizations:InviteAccountToOrganization`

For more information, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html).

**To migrate an account, you cannot have IAM policies or service control policies that prevent migration**

If you are the management account or a delegated administrator, you can control access to AWS resources by attaching permissions policies to IAM identities (users, groups, and roles) within an organization. For more information, see [IAM policies for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_iam-policies.html). 

Before migrating an account:
+ Check that there are no IAM policies or service control policies (SCPs) that prevent you from migrating the account.
+ Identify existing IAM policies and service control policies (SCPs) that you need to replicate in the organization where you are migrating the account.
+ Identify existing IAM policies which specify your organization ID. For example, [`aws:PrincipalOrgID`](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalorgid).

For more information, see [Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the *IAM User Guide* and [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

### Step 2: Check that you have removed IAM permissions that enable access to the old management account
<a name="migrate-account-step-2"></a>

#### Step 2
<a name="collapsible-migrate-account-step-2"></a>

Make sure you have removed IAM permissions that enable access to the old management account such as `OrganizationAccountAccessRole`.

When you remove a member account from an organization, any IAM role that was created to enable access by the organization's management account isn't automatically deleted. If you want to terminate this access from the former organization's management account, then you must manually delete the IAM role.

For information about how to delete a role, see [Deleting roles or instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html) in the *IAM User Guide*.

### Step 3: Back up all reports
<a name="migrate-account-step-3"></a>

#### Step 3
<a name="collapsible-migrate-account-step-3"></a>

Make sure to export or back up reports from the management account, especially billing reports. Organizational level reports and history are not stored when you migrate an account. It is recommended that you do a full export of all billing history. You can still access reports for member account such as AWS CloudTrail Event history and account billing history.

**Important**  
All organizational level reporting and history, such as organizational billing information in the management account, will be deleted after an account is removed from an organization.

For more information, see [Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), [Cost Explorer Reports](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-reports.html), [Savings Plans Reports](https://docs.aws.amazon.com/savingsplans/latest/userguide/ce-sp-usingPR.html#ce-dl-pr), and [Reserved Instance (RI) utilization and coverage](https://repost.aws/knowledge-center/ec2-ri-utilization-coverage-cost-explorer).

### Step 4: Check for organization dependencies
<a name="migrate-account-step-4"></a>

#### Step 4
<a name="collapsible-migrate-account-step-4"></a>

Make sure the migrating account does not have any organization-related dependencies.

**Dependencies to check:**
+ If the account is a delegated administrator, you must deregister the delegated administrator permissions before migrating the account. For more information, see [Services you can use with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html).
+ If the account is the management account, you must remove all member accounts from the organization and delete the organization before migrating. After you have deleted the organization, your management account will operate as a standalone account. After migration, the management account will be a member account of the new organization. For more information, see [Deleting an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_delete.html).
+ If any IAM permissions depend on the account, you will need to adjust the permissions for the old organization after you have migrated the account to the new organization in order for the old organization to function as before. For more information, see [Managing access permissions for your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_permissions_overview.html).
+ If you are using any account or organizational unit (OU) tags, you will need to recreate the tags in the new organization. 

To help identify these dependencies, you can use [Account Assessment for AWS Organizations](https://aws.amazon.com/solutions/implementations/account-assessment-for-aws-organizations/), which scans your organization to find delegated administrator accounts, identity-based and resource-based policies, and AWS services with trusted access enabled.

### (Optional) Step 5: Review guidance if you use AWS Control Tower
<a name="migrate-account-step-5"></a>

#### (Optional) Step 5
<a name="collapsible-migrate-account-step-5"></a>

If you are migrating an account to or from an organization managed by AWS Control Tower, review the following AWS Prescriptive Guidance: [Migrate an AWS member account from AWS Organizations to AWS Control Tower](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-an-aws-member-account-from-aws-organizations-to-aws-control-tower.html).

## What you need to do to migrate an account
<a name="migrate-account-process"></a>

The migration process requires for the new organization to send an invitation to the migrating account, and for the migrating account to accept the invitation from the new organization to join the new organization.

**To migrate an account**

1. Send an invitation from the management account of the new organization to the migrating account. For information about inviting accounts, see [Inviting an AWS account to join your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html).

1. Accept the invitation to join the new organization. For more information, see [Accepting an invitation from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_invites.html#orgs_manage_accounts_accept-decline-invite). Accounts that are migrated from one organization to another will be automatically added to the root of the new organization. Before moving an account to an organizational unit (OU) in the new organization, it is recommended that you check that migrating account has the appropriate organization policies and OU permissions.

1. If you want to migrate the management account, you must [remove all member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html) from the organization and [delete the organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_delete.html) before migrating the management account to the new organization. After you have deleted the old organization, your management account will operate as a standalone account and can accept the invitation from the new organization to join the new organization. If you accept the invitation, the management account will be a member account of the new organization.

## What you need to do after migrating an account
<a name="migrate-account-post"></a>

After migration your account from one organization to another, make sure you have completed the following steps.

**Post-migration review**

1. Evaluate all of the [billing tool configurations](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/reporting-cost-optimization-tools.html) for the migrated account, such as cost categories, budgets, and billing alarms.

1. Review and update the following monetary information for any accounts that you migrated from one organization to another:

   1. If necessary, [update the tax settings](https://repost.aws/knowledge-center/update-tax-registration-number) on the account.

   1. Make sure the [Support plan](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidatedbilling-support.html) for migrating account matches payer account for the new organization.

   1. Review any possible [tax exemptions](https://aws.amazon.com/tax-help/united-states/) that you might want to apply to the account you migrated.

1. Validate and confirm existing IAM policies and service control policies (SCPs) for the migrated account. For example, you might need to update the organization ID for some IAM policies to reflect the new organization.

1. Update [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) for new organization where you migrated the account. You will need to update all the previous cost allocation tags collected by account you migrated.

1. Any [Reserved Instances](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-behavior.html) and [Saving Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) will migrate along with the account. These are not retained in the old organization. Contact Support if these need to be transferred to the old organization.