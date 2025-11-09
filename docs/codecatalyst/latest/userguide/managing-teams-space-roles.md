Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Granting space roles for a team

Teams are a way to group users so that you can grant and manage team access to projects in CodeCatalyst. As an example, you can use teams to quickly manage roles and permissions for users by giving a team the ability to manage a space for users.

A team can have role permissions, such as **Power user**, in a
space. You can change the space role for a team, but note that all members of the team
will inherit those permissions.

You must have the **Space administrator** role to manage teams.

###### Changing the space role for a team

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space. Choose **Settings**, and then choose
   **Teams**.
3. In **Actions**, choose **Change space role**. You
   can change the space role to one of the following. This changes the role for all
   members of the team.
   - **Space administrator** - For details, see [Space administrator role](ipa-role-types.md#ipa-role-space-admin "ipa-role-types.md#ipa-role-space-admin").
   - **Limited access** - For details, see [Limited access role](ipa-role-types.md#ipa-role-limited-access "ipa-role-types.md#ipa-role-limited-access").
   - **Power user** - For details, see [Power user role](ipa-role-types.md#ipa-role-power-user "ipa-role-types.md#ipa-role-power-user").

4. Choose **Save**.
