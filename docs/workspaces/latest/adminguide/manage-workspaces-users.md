# Manage users in WorkSpaces Personal

As an administrator for WorkSpaces, you can perform the following
tasks to manage WorkSpaces users.

## Edit user information

You can use the WorkSpaces console to edit the user information for a WorkSpace.

###### Note

This feature is available only if you use AWS Managed Microsoft AD or Simple AD. If you use
Microsoft Active Directory through AD Connector or a trust relationship, you can
manage users and groups using the [Active Directory module](https://docs.microsoft.com/powershell/module/activedirectory/ "https://docs.microsoft.com/powershell/module/activedirectory/"). If you use Microsoft Entra ID or Custom WorkSpaces directory,
you can manage users and groups with Microsoft Entra ID or your Identity Providers.

###### To edit user information

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select a user and choose **Actions**, **Edit
   users**.
4. Update **First name**, **Last name**, and
   **Email** as needed.
5. Choose **Update**.

## Add or delete users

You can create users from the Amazon WorkSpaces console only during the process of
launching a WorkSpace, and you cannot delete users through the Amazon WorkSpaces console.
Most user management tasks, including managing user groups, must be performed
through your directory.

###### To add or delete users and groups

To add, delete, or otherwise manage users and groups, you must do this through your directory. You'll
perform most administrative tasks for your WorkSpaces directory using directory management tools, such as
the Active Directory Administration Tools. For more information, see
[Set up Active Directory Administration Tools for WorkSpaces Personal](directory_administration.md "directory_administration.md").

###### Important

Before you can remove a user, you must delete the WorkSpace assigned to that user.
For more information, see [Delete a WorkSpace in WorkSpaces Personal](delete-workspaces.md "delete-workspaces.md").

The process you use for managing users and groups depends on which type of directory you're using.

- If you're using AWS Managed Microsoft AD, see [Manage Users and Groups in AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/ms_ad_manage_users_groups.md") in the
  _AWS Directory Service Administration Guide_.
- If you're using Simple AD, see [Manage Users and Groups in Simple AD](../../../directoryservice/latest/admin-guide/simple_ad_manage_users_groups.md "../../../directoryservice/latest/admin-guide/simple_ad_manage_users_groups.md") in the
  _AWS Directory Service Administration Guide_.
- If you use Microsoft Active Directory through AD Connector or a trust relationship, you can
  manage users and groups by using the [Active Directory module](https://docs.microsoft.com/powershell/module/activedirectory/ "https://docs.microsoft.com/powershell/module/activedirectory/").

## Send an invitation email

You can send an invitation email to a user manually if needed.

###### Note

If you're using AD Connector or a trusted domain, invitation emails aren't automatically
sent to your users, so you must send them manually. Invitation emails also aren't sent
automatically if the user already exists in Active Directory.

###### To resend an invitation email

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. On the **WorkSpaces** page, use the search box to search for the user
   you want to send an invitation to, and then select the corresponding WorkSpace from the
   search results. You can select only one WorkSpace at a time.
4. Choose **Actions**, **Invite users**.
5. On the **Invite users to the WorkSpace** page, choose
   **Send invite**.
