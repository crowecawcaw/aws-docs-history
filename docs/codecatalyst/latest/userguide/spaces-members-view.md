Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Viewing members in a space

You can view the users in your space, including information about their display names,
aliases, and the role they have for the space. There are three roles for members in a
space:

- **Space administrator** – This role has all permissions in
  CodeCatalyst, including creating projects. Only assign this role to users who need to administer
  every aspect of a space, such as accessing all projects in the space.

You cannot change this role later
without
removing the user first. For more information, see [Space administrator role](ipa-role-types.md#ipa-role-space-admin "ipa-role-types.md#ipa-role-space-admin").

- **Power user** – This role is the second-most powerful role in
  Amazon CodeCatalyst spaces, but it has no access to projects in a space. It is designed for
  users who need to be able to create projects in a space and help manage the users and
  resources for the space. For more information, see [Power user role](ipa-role-types.md#ipa-role-power-user "ipa-role-types.md#ipa-role-power-user").
- **Limited access** – This role is assigned by default for
  users who join the space by accepting invitations to projects in the space.
  Project members are assigned a role in a project. For information about managing project
  members, see [Granting users project permissions](projects-members.md "projects-members.md").
  The **Space administrators** table shows users with the
  **Space administrator** role. These users are not shown in the
  **Space members** because they are automatically (implicitly)
  assigned to all projects in the space and do not have a role in a project.

The **Space members** table shows all members in the space that have
a role in a project while not having the **Space administrator** role.

Users are shown based on whether the user has the **Space administrator**
role in CodeCatalyst as follows:

- A user with the **Space administrator** role who later accepts a project
  invitation and role will not show in the **Space members**
  table under spaces or on the **Project members** table under projects.
  They will continue to be shown in the **Space administrators**
  table in both places. In each project, all users with the
  **Space administrator** role are shown in the project
  **Space administrators** table for that project.
- A user who accepts a project invitation to join with a project role is added to the
  space with the **Limited access** role. If the user's role later
  changes to the **Space administrator** role, but will also move from the
  **Space members** table to the **Space
  administrators** table. Under the project, the user will move from the
  **Project members** table to the **Space
  administrators** table.

###### To view users and roles in your space

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space.

###### Tip

If you belong to more than one space, choose a space in the top navigation
bar. 3. Choose **Settings**, and then choose
**Members**.

Users who are members of the space are shown in the **Space
members** table.

###### Tip

If you have the **Space administrator** role, you can view which
projects you have been directly invited to. Navigate to **Project
settings** for the project, and then choose **My
projects**.

In the **Status** column, the following are valid values:

    * **Invited** – CodeCatalyst sent the invitation but
     the user has not yet accepted or declined.
    * **Member** – The user accepted the
     invitation.
