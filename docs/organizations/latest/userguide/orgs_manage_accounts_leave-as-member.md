# Leaving an organization from a

member account with AWS Organizations

When you sign in to a member account, you can leave an organization. The management account can't leave the organization using this
technique. To remove the management account, you must [delete the organization](orgs_manage_org_delete.md "orgs_manage_org_delete.md").

## Considerations

**An account’s status with an organization affects what cost and usage data is visible**

If a member account leaves an organization and becomes a standalone account,
the account no longer has access to cost and usage data from the time range when the account was a member of the organization.
The account has access only to the data that is generated as a standalone account.

If a member account leaves organization A to join organization B, the account no longer has access to cost and usage data from the time range when the account
was a member of organization A. The account has access only to the data that is generated as a member of organization B.

If an account rejoins an organization that it previously belonged to, the account regains access to its historical cost and usage data.

**The account is no longer covered by organization agreements that were accepted on its behalf**

If you leave an organization, you are no longer covered by organization agreements
that were accepted on your behalf by the management account of the organization. You
can view a list of these organization agreements in the AWS Artifact console on the [AWS Artifact Organization Agreements](https://console.aws.amazon.com/artifact/home?#!/agreements?tab=organizationAgreements "https://console.aws.amazon.com/artifact/home?#!/agreements?tab=organizationAgreements") page. Before leaving the organization,
you should determine (with the assistance of your legal, privacy, or compliance
teams where appropriate) whether it is necessary for you to have new agreement(s) in
place.

## Leave an organization from a member account

To leave an organization, complete the following procedure.

###### Minimum permissions

To leave an organization, you must have the following permissions:

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

###### To leave an organization from your member account

1. Sign in to the AWS Organizations console at [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an
   IAM user, assume an IAM role, or sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in a member account.

By default, you don't have access to the root user password in a
member account that was created using AWS Organizations. If required, recover
the root user password by following the steps in **Using the root user (Not recommended for everyday tasks)** in [Accessing member accounts in an
organization with AWS Organizations](orgs_manage_accounts_access.md "orgs_manage_accounts_access.md"). 2. On the **[Organizations Dashboard](https://console.aws.amazon.com/organizations/v2/home/dashboard "https://console.aws.amazon.com/organizations/v2/home/dashboard")** page, choose **Leave this
organization**. 3. In the **Confirm leaving the organization?**
dialog box, choose **Leave organization**. When
prompted, confirm your choice to remove the account. After you have confirmed,
you are redirected to the **Getting Started** page
of the AWS Organizations console, where you can view any pending invitations
for your account to join other organizations.

If you see a **You can't leave the organization
yet** message, your account doesn't have all the
required information to operate as a standalone account. If this is
the case, proceed to the next step. 4. If the **Confirm leaving the organization?**
dialog box displays the message **You can't leave the
organization yet**, choose the **Complete the
account sign-up steps** link.

If you do not see the **Complete the
account sign-up steps** link,
use [this link](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?client=organizations&enforcePI=True "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html?client=organizations&enforcePI=True")
to go the **Sign up for AWS** page complete the missing registration steps. 5. On the **Sign up for AWS** page, enter all of
the required information necessary for this to become a standalone
account. This might include the following types of
information:

    * Contact name and address
    * Valid payment method
    * Phone number verification
    * Support plan options

6. When you see the dialog box stating that the sign-up process is
   complete, choose **Leave organization**.

A confirmation dialog box appears. Confirm your choice to remove
the account. You are redirected to the **Getting
Started** page of the AWS Organizations console, where you can
view any pending invitations for your account to join other
organizations. 7. Remove the IAM roles that grant access to your account from the
organization.

###### Important

If your account was created in the organization, then Organizations
automatically created an IAM role in the account that enabled
access by the organization's management account. If the account
was invited to join, then Organizations did not automatically create such
a role, but you or another administrator might have created one
to get the same benefits. In either case, when you remove the
account from the organization, any such role isn't automatically
deleted. If you want to terminate this access from the former
organization's management account, then you must manually delete
this IAM role. For information about how to delete a role, see
[Deleting
roles or instance profiles](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the
_IAM User Guide_.

AWS CLI & AWS SDKs

###### To leave an organization as a member account

You can use one of the following commands to leave an
organization:

- AWS CLI: [leave-organization](../../../cli/latest/reference/organizations/leave-organization.md "../../../cli/latest/reference/organizations/leave-organization.md")

The following example causes the account whose credentials are
used to run the command to leave the organization.

```
`$` **aws organizations leave-organization**
```

This command produces no output when successful.

- AWS SDKs: [LeaveOrganization](../APIReference/API_LeaveOrganization.md "../APIReference/API_LeaveOrganization.md")

After the member account has left the organization, make sure to remove
the IAM roles that grant access to your account from the
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

Member accounts can also be removed by a user in the management account
with [remove-account-from-organization](../../../cli/latest/reference/organizations/remove-account-from-organization.md "../../../cli/latest/reference/organizations/remove-account-from-organization.md") instead. For more information,
see [Remove a member account
from an organization](orgs_manage_accounts_remove.md#orgs_manage_accounts_remove-member-account "orgs_manage_accounts_remove.md#orgs_manage_accounts_remove-member-account").
