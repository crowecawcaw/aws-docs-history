Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Creating a team

A team can have role permissions, such as **Power user**, in a
space. A team can also have project permissions, such as
**Project administrator**, in a project. Teams can be associated with many
projects with different roles for each project. You can manage teams where the team members
are either individual users for an AWS Builder ID space or SSO groups for a space that
supports identity federation.

On the members page for space and project users, users can have multiple roles. Users
with multiple roles will show an indicator when they have multiple roles, and they will be
displayed with the role with the most permissions first.

###### Note

If your space supports identity federation, you must already have your SSO users or
your SSO groups set up in IAM Identity Center.

How you manage team members depends on how you will add and remove users. There are two
options for managing team members:

- **Adding users directly** — You add or remove users
  individually. For example, you add users to a team by choosing either AWS Builder ID users or
  SSO users that are already set up in IAM Identity Center. When you choose to manage team members by
  adding AWS Builder ID users or SSO users directly, the option to use **SSO
  groups** will no longer be available.
- **Use SSO groups** — You manage team members through SSO
  groups already set up in IAM Identity Center. When you choose to manage team members by using
  **SSO groups**, the option to add users directly will no longer be
  available.
  You must have the **Space administrator** role to manage teams.

###### To create a team

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space. Choose **Settings**, and then choose
   **Teams**.
3. Choose **Create team**.
4. In **Team name**, enter a descriptive name for your team.

###### Note

The team name must be unique in your space.

(Optional) In **Team description**, enter a description for your
team. 5. Under **Space role**, choose a role from the list of space roles
available in CodeCatalyst that you want to assign to the team. The role will be inherited by all
members of the team.

    * **Space administrator** - For details, see [Space administrator role](ipa-role-types.md#ipa-role-space-admin "ipa-role-types.md#ipa-role-space-admin").
    * **Limited access** - For details, see [Limited access role](ipa-role-types.md#ipa-role-limited-access "ipa-role-types.md#ipa-role-limited-access").
    * **Power user** - For details, see [Power user role](ipa-role-types.md#ipa-role-power-user "ipa-role-types.md#ipa-role-power-user").

6. In **Team membership**, choose one of the following to choose the
   method for adding members to the team.
   - Choose **Add members directly** to manage users individually.
     This includes adding AWS Builder ID users for a space or adding SSO users for a
     space that supports identity federation.
   - Choose **Use SSO Groups** to choose SSO groups that you have
     already set up in IAM Identity Center.

   In **SSO Groups** , choose the box next to the groups that you
   want to add. You can add up to five SSO groups.

###### Note

You cannot change this later. When you choose to manage team members by adding
AWS Builder ID users or SSO users directly, the option to use **SSO
groups** will no longer be available. When you choose to manage team members
by using **SSO groups**, the option to add users directly will no
longer be available. 7. Choose **Create**.

###### Note

When you choose to use SSO groups, note that the users in the SSO group are not
pulled upon creation of the team. The users will need to have signed in to CodeCatalyst before
they are visible in the list.
