# Delete users from your Connect Customer instance

###### Important

- You can't undo a deletion.
- When a user is deleted from Connect Customer, you won't be able to
  configure their agent settings any more. For example, you won't be able to
  assign a routing profile to them.
- If you delete a user record that has an associated quick connect, you need
  to [delete the quick connect](quick-connects-delete.md "quick-connects-delete.md"),
  too. Otherwise it will be orphaned. When agents attempt to transfer calls to
  it, no one is there to answer the call.
- Orphaned quick connects can disrupt other Connect Customer processes such as instance
  replication and syncing processes that are done as part of [Connect Customer Global
  Resiliency](setup-connect-global-resiliency.md "setup-connect-global-resiliency.md").
  This topic explains how to delete user records using the Connect Customer admin website. To delete user records
  programmatically, see [DeleteUser](../APIReference/API_DeleteUser.md "../APIReference/API_DeleteUser.md") in the
  _Connect Customer API Reference Guide_. To use the CLI, see [delete-user](../../../cli/latest/reference/connect/delete-user.md "../../../cli/latest/reference/connect/delete-user.md").

## What happens to the user's metrics?

The user's data in contact records and reports is retained. The data is preserved
for the consistency of the historical metrics. For example, when you search for
contact records, you'll still see the agent's username, any contact recordings
involving the agent.

In the historical metrics reports, the agent's data will be included in the
**Agent performance** metrics report. However, you won't be
able to see an **Agent activity audit** of the deleted agent
because their name won't appear in the drop-down list.

## How to delete users

You can delete users from the user list page or from an individual user's detail
page.

### Delete users from the list page

1. Sign in to Connect Customer using an **Admin**
   account, or an account assigned to a security profile that has
   **Users - Remove** permission.
2. In Connect Customer, on the left navigation menu, choose
   **Users**.
   Choose one or more users you want to delete.

![The User management page with users selected for deletion.](images/user-cloudscape-delete-step1.png) 3. Choose **Actions**, and then choose
**Delete**. 4. In the confirmation dialog, review the list of users to be deleted,
and then choose **Delete** to confirm. 5. The service deletes the users. When the deletion completes, the
progress bar shows success and a warning icon appears next to the
**Refresh** button to indicate the table needs
refreshing.

![The User management page after successful deletion.](images/user-cloudscape-delete-step4.png) 6. Refresh the table. The deleted users no longer appear in the
list.

### Delete a user from the detail page

1. On the user detail page, choose the **Delete**
   button in the page header.
2. In the confirmation dialog, choose **Delete** to
   confirm.
3. The service deletes the user. The **User
   management** page opens.

## Required permissions to delete users

Before you can update permissions in a security profile, you must be logged in
with an Connect Customer account that has the following permissions:
**Users - Remove**.

![The users and permissions section of the security profiles page, Users option.](images/SecurityProfile_cloudscape_users_edit.png)

By default, the Connect Customer
**Admin** security profile has these permissions.
