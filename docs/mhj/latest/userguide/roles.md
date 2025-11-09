AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Roles

Migration Hub Journeys defines five roles: `MigrationSpaceAdmin`,
`MigrationSpaceContributor`, `JourneyAdmin`,
`JourneyContributor`, and `TeamContributor`. This topic explains how
to assign these roles. For the permissions that are associated with each of the five roles,
see [Permissions](permissions-table.md "permissions-table.md").

###### Important

When you edit the role of a team or an individual, it can take up to 5 minutes for the
role change to take effect after you see the change in the console.

## MigrationSpaceAdmin

When you create a migration space, you automatically get the
`MigrationSpaceAdmin` for that space. When you're a
`MigrationSpaceAdmin`, you can also grant this role to others.

###### To grant the `MigrationSpaceAdmin` role to an individual that is already a

member of the migration space

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space to which you want to give the individual the
   `MigrationSpaceAdmin` role.
3. Choose the **Individuals** tab.
4. Choose the radio button next to the name of the individual to whom you want to give
   the `MigrationSpaceAdmin` role.
5. Choose **Edit role**.
6. In the dialog box, choose the **MigrationSpaceAdmin**
   option.
7. Choose **Save**.

###### To grant the `MigrationSpaceAdmin` role to an individual that isn't

already a member of the migration space

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space to which you want to give the individual the
   `MigrationSpaceAdmin` role.
3. Choose the **Individuals** tab.
4. Choose **Invite**.
5. Enter the individual's email address and choose the
   **MigrationSpaceAdmin** option.
6. Choose **Invite**.

###### To grant the `MigrationSpaceAdmin` role to a team that is already a member

of the migration space

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space to which you want to give the individual the
   `MigrationSpaceAdmin` role.
3. Choose the **Teams** tab.
4. Choose the radio button next to the name of the team to which you want to give the
   `MigrationSpaceAdmin` role.
5. Choose **Edit role**.
6. In the dialog box, choose the **MigrationSpaceAdmin**
   option.
7. Choose **Update**.

###### To grant the `MigrationSpaceAdmin` role to a team that isn't already a

member of the migration space

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space in which you want to create a team and to
   make that team a `MigrationSpaceAdmin`.
3. Choose the **Teams** tab.
4. Choose **Create team**.
5. Enter a name and an optional description for the team, and choose the
   **MigrationSpaceAdmin** option.
6. Choose **Create**.

## MigrationSpaceContributor

A `MigrationSpaceAdmin` can invite an individual to become a
`MigrationSpaceContributor` in that space. The `MigrationSpaceAdmin`
can also create a new team and give it the `MigrationSpaceContributor` in that
space. In addition, a `MigrationSpaceAdmin` can change the role of a team or an
individual from `MigrationSpaceAdmin` to
`MigrationSpaceContributor`.

###### To invite an individual to become a `MigrationSpaceContributor`

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space to which you want to give the individual the
   `MigrationSpaceContributor` role.
3. Choose the **Individuals** tab.
4. Choose **Invite**.
5. Enter the individual's email address and choose the
   **MigrationSpaceContributor** option.
6. Choose **Invite**.
7. Notify the individual to whom you sent the invitation that they will receive an
   email from the following address:
   `no-reply@es.prod.us-east-2.service.migops.migration-services.aws.dev`

The body of the email will have a **Respond** button that they
can use to accept or reject the invitation.

In addition to the invitation email, the individual can also go to **Pending
actions** to see the invitation that you sent them and to accept it or reject
it. For more information, see [Pending actions](pending-actions.md "pending-actions.md").

###### Important

For the recipient of the invitation to get the
`MigrationSpaceContributor` role, they must accept the invitation that
you sent them. To accept the invitation, they can choose
**Respond** in the invitation email, or they can go directly to
**Pending actions** in the Migration Hub Journeys console. For more information,
see [Pending actions](pending-actions.md "pending-actions.md").

###### To create a team and give it the `MigrationSpaceContributor` role

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space in which you want to create the team.
3. Choose the **Teams** tab.
4. Choose **Create team**.
5. Enter a name and an optional description for the team, and choose the
   **MigrationSpaceContributor** option.
6. Choose **Create**.

###### To change the role of an individual from `MigrationSpaceAdmin` to

`MigrationSpaceContributor`

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space in which you want to make the change.
3. Choose the **Individuals** tab.
4. Choose the radio button next to the individual whose role you want to change.
5. Choose **Edit role**.
6. Choose the **MigrationSpaceContributor** option.
7. Choose **Update**.

###### To change the role of a team from `MigrationSpaceAdmin` to

`MigrationSpaceContributor`

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space in which you want to make the change.
3. Choose the **Teams** tab.
4. Choose the radio button next to the team whose role you want to change.
5. Choose **Edit role**.
6. Choose the **MigrationSpaceContributor** option.
7. Choose **Update**.

## JourneyAdmin

A `MigrationSpaceAdmin` or a `JourneyAdmin` can make an individual
or a team a `JourneyAdmin`.

###### To grant the `JourneyAdmin` role to an individual or a team that is

already a member of the migration journey

1. In the navigation pane, choose **Migration journeys**.
2. Choose the name of the migration journey to which you want to give the individual or
   team the `JourneyAdmin` role.
3. Choose the **Individuals and teams** tab.
4. Choose the radio button next to the individual or team to whom you want to give the
   `JourneyAdmin` role.
5. Choose **Edit role**.
6. In the dialog box, choose the **JourneyAdmin** option.
7. Choose **Save**.

###### To grant the `JourneyAdmin` role to an individual or a team that isn't

already a member of the migration journey

1. In the navigation pane, choose **Migration journeys**.
2. Choose the name of the migration journey to which you want to give the individual or
   team the **JourneyAdmin** role.
3. Choose the **Individuals and teams** tab.
4. Choose **Invite**.
5. Specify the email address of the individual or team that you want to invite.
6. Under **Role**, choose the **JourneyAdmin**
   option.
7. Choose **Invite**.
8. Notify the individual to whom you sent the invitation that they will receive an
   email from the following address:
   `no-reply@es.prod.us-east-2.service.migops.migration-services.aws.dev`

The body of the email will have a **Respond** button that they
can use to accept or reject the invitation.

In addition to the invitation email, the individual can also go to **Pending
actions** to see the invitation that you sent them and to accept it or reject
it. For more information, see [Pending actions](pending-actions.md "pending-actions.md").

###### Important

For the recipient of the invitation to get the `JourneyAdmin` role,
they must accept the invitation that you sent them. To accept the invitation, they can
choose **Respond** in the invitation email, or they can go directly
to **Pending actions** in the Migration Hub Journeys console. For more
information, see [Pending actions](pending-actions.md "pending-actions.md").

## JourneyContributor

A `MigrationSpaceAdmin` or a `JourneyAdmin` can invite an
individual or a team to become a `JourneyContributor`.

###### Important

If an individual or a team is a `JourneyContributor` in a journey, but a
`MigrationSpaceAdmin` in the migration space that contains that journey, then
that individual or team is effectively a `JourneyAdmin` of that journey. Their
role will appear as `JourneyContributor`, but they will be able to perform all
the actions that a `JourneyAdmin` has the permissions to perform.

###### To grant the `JourneyContributor` role to an individual or a team that is

already a member of the migration journey

1. In the navigation pane, choose **Migration journeys**.
2. Choose the name of the migration journey to which you want to give the individual or
   team the `JourneyContributor` role.
3. Choose the **Individuals and teams** tab.
4. Choose the radio button next to the individual or team to whom you want to give the
   `JourneyContributor` role.
5. Choose **Edit role**.
6. In the dialog box, choose the **JourneyContributor** option.
7. Choose **Save**.

###### To grant the `JourneyContributor` role to an individual or a team that

isn't already a member of the migration journey

1. In the navigation pane, choose **Migration journeys**.
2. Choose the name of the migration journey to which you want to give the individual or
   team the `JourneyContributor` role.
3. Choose the **Individuals and teams** tab.
4. Choose **Invite**.
5. Specify the email address of the individual or team that you want to invite.
6. Under **Role**, choose the **JourneyContributor**
   option.
7. Choose **Invite**.
8. Notify the individual to whom you sent the invitation that they will receive an
   email from the following address:
   `no-reply@es.prod.us-east-2.service.migops.migration-services.aws.dev`

The body of the email will have a **Respond** button that they
can use to accept or reject the invitation.

In addition to the invitation email, the individual can also go to **Pending
actions** to see the invitation that you sent them and to accept it or reject
it. For more information, see [Pending actions](pending-actions.md "pending-actions.md").

###### Important

For the recipient of the invitation to get the `JourneyContributor`
role, they must accept the invitation that you sent them. To accept the invitation,
they can choose **Respond** in the invitation email, or they can go
directly to **Pending actions** in the Migration Hub Journeys console. For more
information, see [Pending actions](pending-actions.md "pending-actions.md").

## TeamContributor

A `MigrationSpaceAdmin` can invite an individual to become a
`TeamContributor`.

###### To invite an individual to become a `TeamContributor`

1. In the navigation pane, choose **Migration spaces**.
2. Choose the name of the migration space to which you want to give the individual or
   team the `TeamContributor` role.
3. Choose the **Teams** tab.
4. Choose the name of the team to which you want to invite an individual.
5. Choose **Invite**.
6. Specify the email address of the individual that you want to invite.
7. Choose **Invite**.
8. Notify the individual to whom you sent the invitation that they will receive an
   email from the following address:
   `no-reply@es.prod.us-east-2.service.migops.migration-services.aws.dev`

The body of the email will have a **Respond** button that they
can use to accept or reject the invitation.

In addition to the invitation email, the individual can also go to **Pending
actions** to see the invitation that you sent them and to accept it or reject
it. For more information, see [Pending actions](pending-actions.md "pending-actions.md").

###### Important

For the recipient of the invitation to get the `TeamContributor` role,
they must accept the invitation that you sent them. To accept the invitation, they can
choose **Respond** in the invitation email, or they can go directly
to **Pending actions** in the Migration Hub Journeys console. For more
information, see [Pending actions](pending-actions.md "pending-actions.md").
