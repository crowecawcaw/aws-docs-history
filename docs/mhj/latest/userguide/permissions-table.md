AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Permissions

Migration Hub Journeys defines five roles: `MigrationSpaceAdmin`,
`MigrationSpaceContributor`, `JourneyAdmin`,
`JourneyContributor`, and `TeamContributor`. The following sections
describe the actions that each of the five roles can perform on migration spaces, migration
journeys, and teams. For information about how to get or assign these roles, see [Roles](roles.md "roles.md").

## Role permissions in migration spaces

The following table shows the actions that the `MigrationSpaceAdmin` and
`MigrationSpaceContributor` roles can perform on a migration space. The
`JourneyAdmin`, `JourneyContributor`, and
`TeamContributor` roles don't grant any permissions to perform any of the
actions listed in the table on migration spaces.

| Action                                                  | MigrationSpaceAdmin | MigrationSpaceContributor |
| ------------------------------------------------------- | ------------------- | ------------------------- |
| View a migration space                                  | Yes                 | Yes                       |
| Delete a migration space                                | Yes                 | No                        |
| Add an individual or a team as a migration-space member | Yes                 | No                        |
| View migration space memberships                        | Yes                 | Yes                       |
| Delete migration space memberships                      | Yes                 | No                        |
| Create a journey                                        | Yes                 | Yes                       |
| View migration space journeys                           | Yes                 | No                        |
| Create a team                                           | Yes                 | No                        |
| Delete a team                                           | Yes                 | No                        |

## Role permissions in migration journeys

The following table shows the actions that the `MigrationSpaceAdmin`,
`MigrationSpaceContributor`, `JourneyAdmin`, and
`JourneyContributor` roles can perform on a migration journey. The
`TeamContributor` role doesn't grant any permissions to perform any of the
actions listed in the table on migration journeys.

| Action                           | MigrationSpaceAdmin | MigrationSpaceContributor                                                          | JourneyAdmin                                                 | JourneyContributor                                                                 |
| -------------------------------- | ------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Transfer journey ownership       | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| Cancel journey transfer          | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| View journey details             | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete journey                   | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| Update journey                   | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Add individual as journey member | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| Add a team as journey member     | Yes                 | No                                                                                 | Yes if you are a member of the team that you want to<br>add. | No                                                                                 |
| View journey memberships         | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete journey membership        | Yes                 | You can only remove yourself. You cannot delete the membership<br>of someone else. | Yes                                                          | You can only remove yourself. You cannot delete the membership<br>of someone else. |
| Create phase                     | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Edit phase details               | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Move phase out of scope          | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Move phase into scope            | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete phase                     | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| View phases                      | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Create module                    | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete module                    | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| View modules                     | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| View module details              | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Edit module details              | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Move module out of scope         | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Move module into scope           | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Create task                      | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Edit task                        | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Rerank task                      | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete task                      | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| View tasks                       | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| View task details                | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Add comment                      | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| View comments                    | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete comment                   | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| Upload attachment                | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| View attachments                 | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Download attachment              | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Delete attachment                | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| Create template from journey     | Yes                 | No                                                                                 | Yes                                                          | No                                                                                 |
| Customize journey                | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |
| Reorder modules and phases       | Yes                 | No                                                                                 | Yes                                                          | Yes                                                                                |

## Role permissions in teams

The following table shows the actions that the `MigrationSpaceAdmin`,
`MigrationSpaceContributor`, and `TeamContributor` roles can perform
on a team. The `JourneyAdmin` and `JourneyContributor` roles don't
grant permissions to perform any of the actions listed in the table on teams.

| Action                 | MigrationSpaceAdmin | MigrationSpaceContributor                                                          | TeamContributor                                                                    |
| ---------------------- | ------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| View teams             | Yes                 | Yes                                                                                | No                                                                                 |
| View team details      | Yes                 | Yes                                                                                | Yes                                                                                |
| Create team membership | Yes                 | No                                                                                 | No                                                                                 |
| View team memberships  | Yes                 | Yes                                                                                | Yes                                                                                |
| Delete team membership | Yes                 | You can only remove yourself. You cannot delete the membership<br>of someone else. | You can only remove yourself. You cannot delete the membership<br>of someone else. |
