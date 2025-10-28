# Removing a member account from an

organization with AWS Organizations

Removing a member account does not close the account,
instead it removes the member account from the organization. The former member account
becomes a standalone AWS account that is no longer managed by AWS Organizations.

Afterwards, the
account is no longer subject to any policies and is responsible for its own bill payments.
The organization's management account is no longer charged for any expenses accrued by the
account after it's been removed from the organization.

## Considerations

**IAM access roles created by the management account are not automatically deleted**

When you remove a member account from the organization, any IAM role that
was created to enable access by the organization's management account isn't
automatically deleted. If you want to terminate this access from the former
organization's management account, then you must manually delete the IAM role.
For information about how to delete a role, see [Deleting roles or instance
profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the _IAM User Guide_.

**You can remove an account from your organization only if the account has the information that is required for it to operate as a standalone account**

You can remove an account from your organization only if the account has the
information that is required for it to operate as a standalone account. When you
create an account in an organization using the AWS Organizations console, API, or AWS CLI
commands, all the information that is required of standalone accounts is
_not_ automatically collected.

For each account that you
want to make standalone, you must choose a support plan, provide and verify the
required contact information, and provide a current payment method. AWS uses
the payment method to charge for any billable (not AWS Free Tier) AWS
activity that occurs while the account isn't attached to an organization. To
remove an account that doesn't yet have this information, follow the steps in
[Leaving an organization from a
member account with AWS Organizations](orgs_manage_accounts_leave-as-member.md "orgs_manage_accounts_leave-as-member.md").

**You must wait until
at least four days after the account was created**

To remove an account that you created in the organization, you must wait until
at least four days after the account was created. Invited accounts aren't
subject to this waiting period.

**The owner of
the account that leaves becomes responsible for all new costs accrued**

At the moment the account successfully leaves the organization, the owner of
the AWS account becomes responsible for all new AWS costs accrued, and the
account's payment method is used. The management account of the organization is
no longer responsible.

**The account cannot be a delegated administrator
account for any AWS service enabled for the organization**

The account that you want to remove must not be a delegated administrator
account for any AWS service enabled for your organization. If the account is a
delegated administrator, you must first change the delegated administrator
account to another account that is remaining in the organization. For more
information about how to disable or change the delegated administrator account
for an AWS service, see the documentation for that service.

**The account no longer has
access to cost and usage data**

When a member account leaves an organization, that account no longer has
access to cost and usage data from the time range when the account was a member
of the organization. However, the management account of the organization can
still access the data. If the account rejoins the organization, the account can
access that data again.

**Tags attached to the account
are deleted**

When a member account leaves an organization, all tags attached to the account
are deleted.

**Principals in the account are no longer affected by any organization policies**

The principals in the account are no longer affected by any [policies](orgs_manage_policies.md "orgs_manage_policies.md") that applied in the
organization. This means that restrictions imposed by SCPs are gone, and the
users and roles in the account might have more permissions than they had
before. Other organization policy types can no longer be enforced or
processed.

**The account is no
longer be covered by organization agreements**

If a member account is removed from an organization, that member account will no
longer be covered by organization agreements. Management account administrators
should communicate this to member accounts before removing member accounts from the
organization, so that member accounts can put new agreements in place if necessary.
A list of active organization agreements can be viewed in the AWS Artifact console on the
[AWS Artifact Organization
Agreements](https://console.aws.amazon.com/artifact/home?#!/agreements?tab=organizationAgreements "https://console.aws.amazon.com/artifact/home?#!/agreements?tab=organizationAgreements") page.

**Integration with other services might be disabled**

Integration with other services might be disabled. If you remove an
account from an organization that has integration with an AWS service
enabled, the users in that account can no longer use that service.

## Remove a member account

from an organization

When you sign in to the organization's management account, you can remove member
accounts from the organization that you no longer need. To do this, complete the
following procedure. This procedure applies only to member accounts. To remove the
management account, you must [delete the
organization](orgs_manage_org_delete.md "orgs_manage_org_delete.md").

###### Minimum permissions

To remove one or more member accounts from your organization, you must sign in as
a user or role in the management account with the following permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console
- `organizations:RemoveAccountFromOrganization`
  If you choose to sign in as a user or role in a member account in step 5, then
  that user or role must have the following permissions:

- `organizations:DescribeOrganization` – required only when using the Organizations console.
- `organizations:LeaveOrganization` – Note that the
  organization administrator can apply a policy to your account that removes
  this permission, preventing you from removing your account from the
  organization.
- If you sign in as an IAM user and the account is missing payment
  information, the user must have either `aws-portal:ModifyBilling`
  and `aws-portal:ModifyPaymentMethods` permissions (if the account
  has not yet migrated to fine-grained permissions) OR
  `payments:CreatePaymentInstrument` and
  `payments:UpdatePaymentPreferences` permissions (if the
  account has migrated to fine-grained permissions). Also, the member account
  must have IAM user access to billing enabled. If this isn't already
  enabled, see [Activating Access to the Billing and Cost Management Console](../../../awsaccountbilling/latest/aboutv2/grantaccess.md#ControllingAccessWebsite-Activate "../../../awsaccountbilling/latest/aboutv2/grantaccess.md#ControllingAccessWebsite-Activate") in
  the _AWS Billing User Guide_.

AWS Management Console

###### To remove a member account from your organization

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, find and choose the check box
   ![Blue checkmark icon indicating confirmation or completion of a task.](images/checkbox-selected.png)
   next to each member account that you want to
   remove from your organization. You can navigate the OU hierarchy or
   enable **View AWS accounts only** to
   see a flat list of accounts without the OU structure. If you have a
   lot of accounts, you might have to choose **Load more
   accounts in '_ou-name_'** at the bottom of the list to
   find all of those you want to move.

On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, find and choose the name of the member
account that you want to remove from your organization.
You might have to expand OUs (choose the
![Gray cloud icon representing cloud computing or storage services.](images/console-expand.png)
) to find the account that you want. 3. Choose **Actions**, then under
**AWS account**, choose **Remove from
organization**. 4. In the **Remove account '_account-name_' (#_account-id-num_) from
organization?** dialog box, choose **Remove account**. 5. If AWS Organizations fails to remove one or more of the accounts, it's
typically because you have not provided all the required information
for the account to operate as a standalone account. Perform the
following steps:

    1. Sign in to the failed accounts. We recommend that you sign
     in to the member account by choosing **Copy
     link**, and then pasting it into the address
     bar of a new incognito browser window. If you do not see **Copy link**,
     use [this link](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?client=organizations&enforcePI=True "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?client=organizations&enforcePI=True")
     to go the **Sign up for AWS** page and complete the missing registration steps. If you don't use an
     incognito window, you're signed out of the management
     account and won't be able to navigate back to this dialog
     box.
    2. The browser takes you directly to the sign-up process to
     complete any steps that are missing for this account.
     Complete all the steps presented. They might include the
     following:




    	* Provide contact information
    	* Provide a valid payment method
    	* Verify the phone number
    	* Select a support plan option
    3. After you complete the last sign-up step, AWS
     automatically redirects your browser to the AWS Organizations console
     for the member account. Choose **Leave
     organization**, and then confirm your choice in
     the confirmation dialog box. You are redirected to the
     **Getting Started** page of the
     AWS Organizations console, where you can view any pending invitations
     for your account to join other organizations.
    4. Remove the IAM roles that grant access to your account
     from the organization.


    ###### Important

    If your account was created in the organization, then
     Organizations automatically created an IAM role in the account
     that enabled access by the organization's management
     account. If the account was invited to join, then Organizations
     did not automatically create such a role, but you or
     another administrator might have created one to get the
     same benefits. In either case, when you remove the
     account from the organization, any such role isn't
     automatically deleted. If you want to terminate this
     access from the former organization's management
     account, then you must manually delete this IAM role.
     For information about how to delete a role, see [Deleting roles or instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the
     *IAM User Guide*.

AWS CLI & AWS SDKs

###### To remove a member account from your organization

You can use one of the following commands to remove a member
account:

- AWS CLI: [remove-account-from-organization](../../../cli/latest/reference/organizations/remove-account-from-organization.md "../../../cli/latest/reference/organizations/remove-account-from-organization.md")

```
`$` **aws organizations remove-account-from-organization \
 --account-id 123456789012**
```

This command produces no output when successful.

- AWS SDKs: [RemoveAccountFromOrganization](../APIReference/API_RemoveAccountFromOrganization.md "../APIReference/API_RemoveAccountFromOrganization.md")

After the member account has been removed from the organization, make sure
to remove the IAM roles that grant access to your account from the
organization.

###### Important

If your account was created in the organization, then Organizations
automatically created an IAM role in the account that enabled access
by the organization's management account. If the account was invited to
join, then Organizations did not automatically create such a role, but you or
another administrator might have created one to get the same benefits.
In either case, when you remove the account from the organization, any
such role isn't automatically deleted. If you want to terminate this
access from the former organization's management account, then you must
manually delete this IAM role. For information about how to delete a
role, see [Deleting roles or
instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the
_IAM User Guide_.

Member accounts can remove themselves with [leave-organization](../../../cli/latest/reference/organizations/leave-organization.md "../../../cli/latest/reference/organizations/leave-organization.md") instead. For more information, see [Leaving an organization from a
member account with AWS Organizations](orgs_manage_accounts_leave-as-member.md "orgs_manage_accounts_leave-as-member.md").
