# Changing a delegated administrator

Changing your delegated administrator in AWS Audit Manager is a two-step process. First, you
need to remove the current delegated administrator account. Then, you can add a new
account as the delegated administrator.

Follow the steps on this page to change your delegated administrator.

###### Contents

- [Prerequisites](change-delegated-admin.md#change-delegated-admin-prerequisites "change-delegated-admin.md#change-delegated-admin-prerequisites")
  - [Before you remove the current
    account](change-delegated-admin.md#before-you-remove "change-delegated-admin.md#before-you-remove")
  - [Before you add the new account](change-delegated-admin.md#before-you-add "change-delegated-admin.md#before-you-add")

- [Procedure](change-delegated-admin.md#change-delegated-admin-procedure "change-delegated-admin.md#change-delegated-admin-procedure")
- [Next steps](change-delegated-admin.md#change-delegated-admin-next-steps "change-delegated-admin.md#change-delegated-admin-next-steps")
- [Additional
  resources](change-delegated-admin.md#change-delegated-admin-additional-resources "change-delegated-admin.md#change-delegated-admin-additional-resources")

## Prerequisites

### Before you remove the current

account

Before you remove the current delegated administrator account, keep in mind
the following considerations:

- **Evidence finder cleanup task** - If the
  current delegated administrator (account A) enabled evidence finder,
  you'll need to perform a cleanup task before you assign account B as the
  new delegated administrator.

Before you use your management account to remove account A, make sure
that account A signs in to Audit Manager and disables evidence finder. Disabling
evidence finder automatically deletes the event data store that was
created in the account when evidence finder was enabled.

If this task isn’t completed, the event data store remains in account
A. In this case, we recommend that the original delegated administrator
uses CloudTrail Lake to manually [delete the event data store](../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md "../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md").

This cleanup task is necessary to ensure that you don't end up with
multiple event data stores. Audit Manager ignores an unused event data store
after you remove or change a delegated administrator account. However,
if you don't delete the unused event data store, the event data store
continues to incur storage costs from CloudTrail Lake.

- **Data deletion** - When you remove a
  delegated administrator account for Audit Manager, the data for that account
  isn’t deleted. If you want to delete resource data for a delegated
  administrator account, you must perform that task separately before you
  remove the account. Either, you can do this in the Audit Manager console. Or, you
  can use one of the delete API operations that are provided by Audit Manager. For
  a list of available delete operations, see [Deletion of Audit Manager data](data-protection.md#data-deletion-and-retention "data-protection.md#data-deletion-and-retention").

At this time, Audit Manager doesn't provide an option to delete evidence for a
specific delegated administrator. Instead, when your management account
deregisters Audit Manager, we perform a cleanup for the current delegated
administrator account at the time of deregistration.

### Before you add the new account

Before you add the new delegated administrator account, keep in mind the
following considerations:

- The new account must be part of an organization.
- Before you designate a new delegated administrator, you must [enable all features in your organization](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"). You must also
  [configure your organization's Security Hub settings](setup-recommendations.md#securityhub-recommendations "setup-recommendations.md#securityhub-recommendations"). This way,
  Audit Manager can collect Security Hub evidence from your member accounts.
- The delegated administrator account must have access on the KMS key
  that you provided when setting up Audit Manager.
- You can't use your AWS Organizations management account as a delegated
  administrator in Audit Manager.

## Procedure

You can change a delegated administrator using the Audit Manager console, the AWS Command Line Interface
(AWS CLI), or the Audit Manager API.

###### Warning

When you change a delegated administrator, you continue to have access to the
evidence that you previously collected under the old delegated administrator
account. However, Audit Manager stops collecting and attaching evidence to the old
delegated administrator account.

Audit Manager console

###### To change the current delegated administrator on the Audit Manager

console

1. (Optional) If the current delegated administrator (account A)
   enabled evidence finder, perform the following cleanup task:
   1. Before assigning account B as the new delegated
      administrator, make sure that account A signs in to Audit Manager
      and disables evidence finder.

   Disabling evidence finder automatically deletes the
   event data store that was created when account A enabled
   evidence finder. If you don't complete this step, then
   account A must go to CloudTrail Lake and manually [delete the event data store](../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md "../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md"). Otherwise, the
   event data store remains in account A and continues to
   incur CloudTrail Lake storage charges.

2. From the **General** settings tab, go to the
   **Delegated administrator** section and
   choose **Remove**.
3. In the pop-up window that appears, choose
   **Remove** to confirm.
4. Under **Delegated administrator account ID**,
   enter the ID of the new delegated administrator account.
5. Choose **Delegate**.

AWS CLI

###### To change the current delegated administrator in the

AWS CLI

First, run the [deregister-organization-admin-account](../../../cli/latest/reference/auditmanager/deregister-organization-admin-account.md "../../../cli/latest/reference/auditmanager/deregister-organization-admin-account.md") command using the
`--admin-account-id` parameter to specify the account
ID of the current delegated administrator.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager deregister-organization-admin-account --admin-account-id `111122223333`
```

Then, run the [register-organization-admin-account](../../../cli/latest/reference/auditmanager/register-organization-admin-account.md "../../../cli/latest/reference/auditmanager/register-organization-admin-account.md") command using the
`--admin-account-id` parameter to specify the account ID
of the new delegated administrator.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager register-organization-admin-account --admin-account-id `444455556666`
```

Audit Manager API

###### To change the current delegated administrator using the

API

First, call the [DeregisterOrganizationAdminAccount](../APIReference/API_DeregisterOrganizationAdminAccount.md "../APIReference/API_DeregisterOrganizationAdminAccount.md") operation and use
the [adminAccountId](../APIReference/API_DeregisterOrganizationAdminAccount.md#auditmanager-DeregisterOrganizationAdminAccount-request-adminAccountId "../APIReference/API_DeregisterOrganizationAdminAccount.md#auditmanager-DeregisterOrganizationAdminAccount-request-adminAccountId") parameter to specify the account ID of
the current delegated administrator.

Then, call the [RegisterOrganizationAdminAccount](../APIReference/API_RegisterOrganizationAdminAccount.md "../APIReference/API_RegisterOrganizationAdminAccount.md") operation and use the
[adminAccountId](../APIReference/API_RegisterOrganizationAdminAccount.md#auditmanager-RegisterOrganizationAdminAccount-request-adminAccountId "../APIReference/API_RegisterOrganizationAdminAccount.md#auditmanager-RegisterOrganizationAdminAccount-request-adminAccountId") parameter to specify the account ID of the
new delegated administrator.

For more information, choose the previous links to read more in the
_Audit Manager API Reference_. This includes
information about how to use this operation and parameter in one of the
language-specific AWS SDKs.

## Next steps

To remove your delegated administrator account, see [Removing a delegated administrator](remove-delegated-admin.md "remove-delegated-admin.md").

## Additional

resources

- [Creating and
  managing an organization](../../../organizations/latest/userguide/orgs_manage_org.md "../../../organizations/latest/userguide/orgs_manage_org.md")
- [Troubleshooting delegated administrator and
  AWS Organizations issues](delegated-admin-issues.md "delegated-admin-issues.md")
