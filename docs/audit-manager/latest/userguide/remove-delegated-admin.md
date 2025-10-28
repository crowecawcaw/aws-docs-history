# Removing a delegated administrator

Removing the delegated administrator account stops further evidence collection for
that account, but you retain access to the previously collected evidence.

If you need to remove your delegated administrator account for Audit Manager, you can follow
the necessary steps on this page. Follow the prerequisites and procedures carefully, as
they involve cleaning up resources to avoid unnecessary storage costs.

## Prerequisites

Before you remove the delegated administrator account from Audit Manager, keep in mind the
following considerations:

**Evidence finder cleanup task**

If the current delegated administrator enabled evidence finder, you
need to perform a cleanup task.

Before you use your management account to remove the current delegated
administrator, make sure that the current delegated administrator
account signs in to Audit Manager and disables evidence finder. Disabling
evidence finder automatically deletes the event data store that was
created in the account when evidence finder was enabled.

If this task isn’t completed, the event data store remains in their
account. In this case, we recommend that the original delegated
administrator uses CloudTrail Lake to manually [delete the event data store](../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md "../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md").

This cleanup task is necessary to ensure that you don't end up with
multiple event data stores. Audit Manager ignores an unused event data store
after you remove or change a delegated administrator account. However,
if you don't delete the unused event data store, the event data store
continues to incur storage costs from CloudTrail Lake.

**Data deletion**

When you remove a delegated administrator account for Audit Manager, the data
for that account isn’t deleted. If you want to delete resource data for
a delegated administrator account, you must perform that task separately
before you remove the account. Either, you can do this in the Audit Manager
console. Or, you can use one of the delete API operations that are
provided by Audit Manager. For a list of available delete operations, see [Deletion of Audit Manager data](data-protection.md#data-deletion-and-retention "data-protection.md#data-deletion-and-retention").

At this time, Audit Manager doesn't provide an option to delete evidence for a
specific delegated administrator. Instead, when your management account
deregisters Audit Manager, we perform a cleanup for the current delegated
administrator account at the time of deregistration.

## Procedure

You can remove a delegated administrator using the Audit Manager console, the AWS Command Line Interface
(AWS CLI), or the Audit Manager API.

###### Warning

When you remove a delegated administrator, you continue to have access to the
evidence that you previously collected under that delegated administrator
account. However, Audit Manager stops collecting and attaching evidence to the old
delegated administrator account.

Audit Manager console

###### To remove the current delegated administrator on the Audit Manager

console

1. (Optional) If the current delegated administrator enabled
   evidence finder, perform the following cleanup task:
   1. Make sure that the current delegated administrator
      account signs in to Audit Manager and disables evidence finder.

   Disabling evidence finder automatically deletes the
   event data store that was created in their account when
   they enabled evidence finder. If this step isn't
   completed, the delegated administrator account must use
   CloudTrail Lake to manually [delete the event data store](../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md "../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md"). Otherwise, the
   event data store remains in their account and continues
   to incur CloudTrail Lake storage charges.

2. From the **General** settings tab, go to the
   **Delegated administrator** section and
   choose **Remove**.
3. In the pop-up window that appears, choose
   **Remove** to confirm.

AWS CLI
Disabling evidence finder automatically deletes the event data store
that was created in their account when they enabled evidence finder. If
this step isn't completed, the delegated administrator account must use
CloudTrail Lake to manually [delete the event data store](../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md "../../../awscloudtrail/latest/userguide/query-eds-disable-termination.md"). Otherwise, the event data
store remains in their account and continues to incur CloudTrail Lake storage
charges.

###### To remove the current delegated administrator in the

AWS CLI

Run the [deregister-organization-admin-account](../../../cli/latest/reference/auditmanager/deregister-organization-admin-account.md "../../../cli/latest/reference/auditmanager/deregister-organization-admin-account.md") command and use
the `--admin-account-id` parameter to specify the account
ID of the delegated administrator.

In the following example, replace the `placeholder
 text` with your own information.

```
aws auditmanager deregister-organization-admin-account --admin-account-id `111122223333`
```

Audit Manager API

###### To remove the current delegated administrator using the

API

Call the [DeregisterOrganizationAdminAccount](../APIReference/API_DeregisterOrganizationAdminAccount.md "../APIReference/API_DeregisterOrganizationAdminAccount.md") operation and use
the [adminAccountId](../APIReference/API_DeregisterOrganizationAdminAccount.md#auditmanager-DeregisterOrganizationAdminAccount-request-adminAccountId "../APIReference/API_DeregisterOrganizationAdminAccount.md#auditmanager-DeregisterOrganizationAdminAccount-request-adminAccountId") parameter to specify the account ID of
the delegated administrator.

For more information, choose the previous links to read more in the
_Audit Manager API Reference_. This includes
information about how to use this operation and parameter in one of the
language-specific AWS SDKs.

## Additional

resources

- [Troubleshooting delegated administrator and
  AWS Organizations issues](delegated-admin-issues.md "delegated-admin-issues.md")
