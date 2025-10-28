Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Removing a space member

You can remove a member of your space when they do not need to access any of the
space resources. You must have the **Space administrator** role to remove a
member from a space.

The **Space administrators** table shows users with the
**Space administrator** role. These users are not shown in the **Space
members** table because they are automatically (implicitly) assigned to all
projects in the space and do not have a role in a project. You can only directly remove a
member of your space in this table.

###### To remove a user from the **Project members** table

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space.

###### Tip

If you belong to more than one space, choose a space in the top navigation
bar. 3. Choose **Settings**, and then choose
**Members**. 4. Choose the user in the **Project members** table. Choose
**Remove**.

###### Note

Removing a member from the space will remove the user from all projects in the
space, along with permissions associated with the resources in those projects.
