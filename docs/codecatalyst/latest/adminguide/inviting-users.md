Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Inviting users to a Builder ID space

###### Note

This topic describes how to invite users who sign in to CodeCatalyst with a AWS Builder ID. To
invite users that are managed as part of SSO users and groups, see [Administering spaces that support identity
federation](managing-federation-space.md "managing-federation-space.md").

You can invite users to your CodeCatalyst space (instead of inviting them to a project within
a space). Inviting users to a space is useful when you want that user to help you manage
the space. Users who will manage a space will also need the
**Space administrator** or **Power user** role. Assigning
one of those roles to other users can help you distribute the responsibilities of managing the
space across more people without having to invite these users to projects.

###### Note

You must have the **Space administrator** or
**Power user** role to invite members.

The **Space administrators** table shows users with the
**Space administrator** role. These users are not shown in the
**Space members** table because they are automatically
(implicitly) assigned to all projects in the space and do not have a role in a
project.

Members who accept a project invitation are added to the space by default. The
**Project members** table shows all members in the space that have a role in
a project.

###### Important

Only invite users you trust. Inviting someone grants them access to your space and
resources according to the permissions you assign.

###### To invite a user to your space

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your space.
3. Choose **Settings**, and then choose **Members**.
4. Choose **Invite**.
5. Enter the email of the person you would like to invite to join your space. In
   **Role**, choose the role you want to assign that user in the space.
6. Choose **Invite**
