AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Transferring a journey

After you create a migration journey, you can send a request to transfer the journey
to another individual. If that individual accepts the transfer, they can move the
journey to another migration space where they have the `MigrationSpaceAdmin`
role. That individual then becomes a `JourneyAdmin` for that journey. For
information about roles, see [Roles and permissions](permissions.md "permissions.md").

###### To transfer a journey

1. Open the Migration Hub Journeys console. For information about how to access the console, see [Accessing AWS Migration Hub Journeys](setup.md "setup.md").
2. In the left navigation pane, choose **Migration
   journeys**.
3. In the list of migration journeys, choose the name of the journey that you
   want to transfer.
4. Choose **Actions**, then choose **Transfer journey
   ownership**.
5. Enter the email address of the person to whom you want to transfer the
   journey, and then choose **Transfer**.
6. Notify the individual to whom you sent the transfer request that they will
   receive an email from the following address:
   `no-reply@es.prod.`reg`.service.migrationhub.aws`,
   where `reg` is your AWS Region.

The body of the email will have a **Respond** button that
they can use to accept or reject the transfer.

In addition to the invitation email, the individual can also go to
**Pending actions** in the navigation pane to see the
transfer request that you sent them, and to accept it or reject it. For more
information, see [Pending actions](pending-actions.md "pending-actions.md").

###### Important

For the transfer to take effect, the individual to whom you sent the
transfer request must accept that request. To accept the request, they can
choose **Respond** in the transfer email, or they can go
directly to **Pending actions** in the Migration Hub Journeys console.
For more information, see [Pending actions](pending-actions.md "pending-actions.md").
