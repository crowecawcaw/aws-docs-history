Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Granting users project permissions

You
can manage the members in your projects using the Amazon CodeCatalyst console.
You can add or remove users, manage current members'
roles, send invitations to join your project, and cancel invitations that have not yet been
accepted.

On the members page for space and project users, users can have multiple roles. Users
with multiple roles will show an indicator when they have multiple roles, and they will be
displayed with the role with the most permissions first.

## Getting a list of members and their project roles

When you add a user to your project, you assign a role that grants project permissions as
follows:

- The **Project administrator** role has
  all
  permissions in a project. Only assign this role
  to users who need to administer every aspect of a project, including editing project settings,
  managing project permissions, and deleting the project. For more information, see [Project administrator role](ipa-role-types.md#ipa-role-project-admin "ipa-role-types.md#ipa-role-project-admin").
- The **Contributor** role has the permissions required to work in a
  project. Assign this role to those users who need to work with code, workflows, issues, and
  actions in a project. For more information, see [Contributor role](ipa-role-types.md#ipa-role-contributor "ipa-role-types.md#ipa-role-contributor").
- The **Reviewer** role has review permissions. For details, see
  [Reviewer role](ipa-role-types.md#ipa-role-reviewer "ipa-role-types.md#ipa-role-reviewer").
- The **Read only** role has read permissions. For details, see [Read only role](ipa-role-types.md#ipa-role-read-only "ipa-role-types.md#ipa-role-read-only").

You do not need to invite a user with the **Space administrator** role to your
project because they already have implicit access to all projects in the space.

When you invite a user to your project (without assigning the
**Space administrator** role), the user will show in the **Project
members** table under projects and in the**Project members** table
under spaces.

###### To view users and roles in a space

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the space with the project you want to view. Under
   **Projects**, choose your project.
3. In the navigation pane, choose **Project settings**.
4. Choose the **Members** tab.

The **Project members** table shows all members that have a role in a
project.

###### Tip

If you have the **Space administrator** role, you can view which projects
you have been directly invited
to.
Navigate to **Project settings** for the project, and then choose
**My projects**.

The **Space administrators** table shows users with the
**Space administrator** role. These users are automatically (implicity) assigned
to all projects in the space and do not have a role in a project.

In the **Status** column, the following are valid values:

    * **Invited** – CodeCatalyst sent the invitation but the
     user has not yet accepted or declined.
    * **Member** – The user accepted the
     invitation.

###### Topics

- [Inviting
  a user to a project](#projects-members-add "#projects-members-add")
- [Canceling an invitation](#projects-members-cancel-invite "#projects-members-cancel-invite")
- [Removing a user from your project](#projects-members-remove "#projects-members-remove")
- [Accepting or declining an invitation for a project](#w24aac25c19c15c25 "#w24aac25c19c15c25")

## Inviting

a user to a project

You can use the console to invite users to your project. You can invite members of your
space or add names from outside your space.

To invite users to your project, you must be signed in with the
**Project administrator** or **Space administrator** role.

You do not need to invite a user with the **Space administrator** role to your
project because they already have implicit access to all projects in the space.

When you invite a user to your project (without assigning the
**Space administrator** role), the user will show in the **Project
members** table under projects and in the**Project members** table
under spaces.

###### To invite a member to your project from the Project settings tab

1. Navigate to your project.

###### Tip

You can choose which project to view in the top navigation bar. 2. In the navigation pane, choose **Project settings**. 3. Choose the **Members** tab. 4. In **Project members**, choose **Invite new
member**. 5. Type the new member's email address, choose the role for this member, and then choose
**Invite**. For more information about roles, see [Granting access with user roles](ipa-roles.md "ipa-roles.md").

###### To invite a member to your project from the Project overview page

1. Navigate to your project.

###### Tip

You can choose which project to view in the top navigation bar. 2. Choose the **Members +** button. 3. Type the new member's email address, choose the role for this member, and then choose
**Invite**. For more information about roles, see [Granting access with user roles](ipa-roles.md "ipa-roles.md").

## Canceling an invitation

If you recently sent an invitation, you can cancel it as long as the invitation hasn't yet
been accepted.

To manage project invitations, you must have the **Project administrator**
or **Space administrator** role.

###### To cancel a project member invitation

1. Navigate to the project where you have sent an invitation that you want to cancel.
2. In the navigation pane, choose **Project settings**.
3. View the **Members** tab and verify that the member has a status of
   **Invited**.

###### Note

You can only cancel an invitation that has not yet been accepted. 4. Choose the option next to the row with the invited member, and then choose
**Cancel invitation**. 5. A confirmation window displays. Choose **Cancel invitation** to
confirm.

## Removing a user from your project

You can use the console to remove a user from your project.

To remove a user from your project, you must be signed in with the
**Project administrator** or **Space administrator** role.

###### Note

Removing
a user from all projects within a space automatically removes the user from that
space.

###### To remove a user from a project

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to the space with the project you want to view. Under
   **Projects**, choose your project.
3. In the navigation pane, choose **Project settings**.
4. Choose the **Members** tab.
5. Choose the selector next to the profile you want to remove, and then choose
   **Remove**.
6. Confirm that you want to remove the user, and then choose
   **Remove**.

## Accepting or declining an invitation for a project

You might receive an email invitation to join an Amazon CodeCatalyst project. You can accept or
decline the invitation.

###### To accept or decline an invitation

1. Open the invitation email.
2. Choose the project link in the email.
3. Choose **Accept** or **Decline**.

If you choose **Decline**, an email is sent to the project management
account notifying them that you declined the invitation.
