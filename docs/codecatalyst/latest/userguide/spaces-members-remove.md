Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Removing or changing the role for a user with the

**Space administrator** role

You can remove or change the role for a user with the
**Space administrator** role for your space.

You must have the **Space administrator** role to remove a user with the
**Space administrator** role from a space. Changing the role for a user
with the **Space administrator** role essentially removes the user from the
**Space administrators** table. If that user does not have a
project role in any projects in the space, removing the **Space administrator**
role from the user will remove the user from the space.

###### Note

As a user with the **Space administrator** role, you cannot remove
yourself. Contact another user with the **Space administrator** role.

###### To remove a user with the **Space administrator** role from the **Space members** table

###### Note

For a user who has not been added explicitly to a project, they do not have any
project roles (**Project administrator** or **Contributor**). If the **Space administrator** role
is the user's only role, then the user is removed from the space entirely.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the space where you want to remove or change the role for a user with
   the **Space administrator** role.
3. Choose **Settings**, and then choose
   **Members**.
4. View the invitation status for the list of members, and make sure that the list
   contains no unauthorized pending invites to the space (a status of **Invited**).

###### Important

Before removing a user with the **Space administrator** role, you must
verify that no pending invites have been initiated. 5. Choose the **Members** tab. In the **Space
administrators** table, choose the user, and then choose
**Remove**.

On the **Remove member** dialog box, do one of the following.

    * Choose the option to remove only the user's **Space administrator**
     role. Choose **Remove**.


    ###### Important

    If the user does not have any other role assigned, then changing the role from
     **Space administrator** removes the user from the space.
    * Choose the option to remove a user with the **Space administrator**
     role from the space and all its projects. Choose
     **Remove**.

6. Refresh the **Members** tab. The user is automatically added to the
   list of project members in any project where the user had membership through project
   roles. If the **Space administrator** role was the user's only role, then
   the user is removed from the space entirely.
