Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Understanding user roles for spaces and projects

There are three roles available for a space:

- **Space administrator**
- **Power user**
- **Limited access**
  Users who accept an invitation to a project have the **Limited access**
  role automatically assigned to them in the space that contains the project.

There are four roles available for members in a project:

- **Project administrator**
- **Contributor**
- **Reviewer**
- **Read only**
  When you add a user to a project, CodeCatalyst automatically gives them the
  **Limited access** role. If you remove a user from all projects, CodeCatalyst
  automatically removes the Limited access role from that user.

## Space administrator role

The **Space administrator** role is the most powerful role in CodeCatalyst. Only
assign the **Space administrator** role to users who need to administer every
aspect of a space, because this role has all permissions in CodeCatalyst. Users with the
**Space administrator** role are the only users who can add or remove other users
from the **Space administrator** role and delete the space.

When you create a space, CodeCatalyst automatically assigns you the
**Space administrator** role. As a best practice, we recommend that you add this
role to at least one other user who can act in this role in case the original space creator
is unavailable.

## Power user role

The **Power user** role is the second-most powerful role in CodeCatalyst
spaces, but it has no access to projects in a space. It is designed for users who need to
be able to create projects in a space and help manage the users and resources for the
space. Assign the **Power user** role to users who are team leaders
or managers who need the ability to create projects and manage users in the space as part
of their work.

## Limited access role

The **Limited access** access role is the role most users will have in
CodeCatalyst spaces. It is the role automatically assigned to users when they accept an
invitation to a project in a space. It provides the limited permissions they need to work
within the space that contains that project. Assign the
**Limited access** role to users you invite directly to the space
unless their work requires that they manage some aspect of the space.

## Project administrator role

The **Project administrator** role is the most powerful role in a CodeCatalyst
project. Only assign this role to users who need to administer every aspect of a project,
including editing project settings, managing project permissions, and deleting projects.

Project roles do not have any permissions at the space level. Therefore, users with
the **Project administrator** role cannot create additional projects. Only users
with the **Space administrator** or **Power user** role can
create projects.

###### Note

The **Space administrator** role has all permissions in CodeCatalyst.

## Contributor role

The **Contributor** role is intended for the majority of members in
a CodeCatalyst project. Assign this role to users who need to be able to work with code, workflows,
issues, and actions in a project.

## Reviewer role

The **Reviewer** role is intended for users who need to be able to
interact with resources in a project, such as pull requests and issues, but not create and merge
code, create workflows, or start or stop workflow runs in a CodeCatalyst project. Assign the
**Reviewer** role to users who need to be able to approve and comment
on pull requests, create, update, resolve, and comment on issues, and view code and workflows in
a project.

## Read only role

The **Read only** role is intended for users who need to view the
resources and status of resources but not interact with them or contribute directly to the
project. Users with this role cannot create resources in CodeCatalyst, but they can view them and copy
them, such as cloning repositories and downloading attachments to issues to a local computer.
Assign the **Read only** role to users who need to view resources and the
state of the project, but not interact directly with it.
