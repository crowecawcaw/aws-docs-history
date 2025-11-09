Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Granting project roles for a team at the space level

A team in CodeCatalyst is similar to a user in that the team members can have role permissions,
such as **Project administrator**, in a project. A role change will be applied
to the team, and all members of the team will inherit those permissions. You can choose one
role for each project that will be automatically granted to the team.

You must have the **Space administrator** role to manage teams.

###### To add or change a project role

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space. Choose **Settings**, and then choose
   **Teams**.
3. Choose the **Project roles** tab.
4. To change a role, choose the selector next to the project in this list, and then
   choose **Change role**. To add a role, choose **Add project
   role**. In **Project**, choose the project you want to add and
   in **Role**, choose the role. Choose one of the available project
   roles:
   - **Project administrator** - For details, see [Project administrator role](ipa-role-types.md#ipa-role-project-admin "ipa-role-types.md#ipa-role-project-admin").
   - **Contributor** - For details, see [Contributor role](ipa-role-types.md#ipa-role-contributor "ipa-role-types.md#ipa-role-contributor").
   - **Reviewer** - For details, see [Reviewer role](ipa-role-types.md#ipa-role-reviewer "ipa-role-types.md#ipa-role-reviewer").
   - **Read only** - For details, see [Read only role](ipa-role-types.md#ipa-role-read-only "ipa-role-types.md#ipa-role-read-only").

5. Choose **Save**.

###### To remove a project role

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space. Choose **Settings**, and then choose
   **Teams**.
3. Choose the **Project roles** tab.
4. Choose the role you want to remove.

###### Important

Removing a role from a team removes the associated permissions for all users in the
team. 5. Choose **Save**.
