

# Manage space members and permissions
<a name="omni-manage-space-members-and-permissions"></a>

Add members to your space, give them grants, and remove access when it is no longer needed. Only a Space Admin can add, edit, or delete grants. For what grants and permission levels are and how they combine, see [Control access to your space](omni-control-access-to-your-space.md).

Available in the Omni web UI only.

**Prerequisites**
+ You are signed in to your space in the Omni web UI.
+ You hold a grant with the **Space Admin** permission level.
+ The people you want to add can sign in to your domain. The users and groups available depend on how your domain's identity provider is set up; see [Set up Omni](omni-set-up-omni.md).

**Add a member**

1. Open **Settings**, and under **Space** choose **Manage permissions**. Choose **Add grants**. To change an existing grant instead, choose the principal's name to open their grants, open the grant, and choose **Edit grant**.

1. Under **Principals**, search for users, groups, access profiles, IAM roles, or alerts, and select one or more. (When editing an existing member, the member is already selected.)

1. Under **Grant name**, enter a name that identifies this grant, such as `dashboard-read`.

1. Under **Permission level**, choose **Viewer**, **Editor**, **Space Admin**, or **Custom**. For what each level allows, see [Control access to your space](omni-control-access-to-your-space.md). For a custom grant, select the actions to allow and, optionally, the resources they apply to; the actions are listed in [Custom grant actions](omni-custom-grant-actions.md).

1. (Optional) To limit the data this grant can see, under **Advanced: limit the data this principal can see**, choose **Add limits to data visibility** and build the data scope. For what a scope can express, see [Limit what members can see](omni-limit-what-members-can-see.md).

1. Choose **Add**, or **Save changes** when editing. The principal appears in the table with the new grant listed beside it.

**Remove access**

To remove access, choose the principal's name to open their grants, select the grant, and choose **Delete**. Deleting a grant cannot be undone. When you delete a member's last grant, they immediately lose access to every resource in the space.
+ A space must always keep at least one Space Admin, so you cannot delete the last grant that provides Space Admin access.
+ You cannot edit or delete your own grants. Ask another Space Admin to change your access.
+ An IAM Identity Center user also holds every grant given to a group they belong to, and deleting their own grants does not remove that inherited access. To remove all of their access, remove the user from those groups in IAM Identity Center or your identity provider, or delete the group's grants, which affects every member of the group.

**System managed grants**

Some grants are created by the service. The table marks them as system managed, and they cannot be edited or deleted.

**Give a resource its own access**

Some resources act when no one is signed in. An alert, for example, evaluates its query on a schedule. An access profile gives such a resource an identity of its own, and you add a profile as a member and give it a permission level as you would a person, with one exception: **Space Admin** is not available to an access profile, because space administration is reserved for people. See [Access profiles](omni-access-profiles.md).