# Default permissions profiles

Every RES project comes with two default permission profiles that Global Administrators can
configure. (In addition, Global Administrators can create and modify new permission profiles
for a project.) The following table shows the allowed permissions for the default permission
profiles- "Project Member" and "Project Owner". Permission profiles, and the permissions they
grant to select users of a project, only apply to the project that they belong to; Global
Administrators are super users who have all the permissions below across all projects.

| Permissions                       | Description                                                                                                         | Project Member | Project Owner |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------- | -------------- | ------------- |
| Create Session                    | Create your own session. Users can always stop and terminate their own<br>sessions with or without this permission. | X              | X             |
| Create/terminate others' sessions | Create or terminate another user's session within a project.                                                        |                | X             |
| Update Project membership         | Update users and groups associated with a project.                                                                  |                | X             |
| Update Project Status             | Enable or disable a project.                                                                                        |                | X             |
