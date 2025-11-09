AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Track the status of your migrations in AWS Migration Hub

With a migration underway, you can track its progress status as well as details for each
server grouped to the application. This status is communicated to AWS Migration Hub from the migration
tool at key points during the migration.

###### To track an application's migration status

1. After your application's migration has started, return to Migration Hub console and then
   choose **Dashboard** in the navigation pane.
2. Under **Most recently updated applications**, choose the name of
   your migrating application. Doing this displays the application's detail
   screen.
   1. If you do not see all of your application's servers listed in the
      application's details page, it could be because you have not grouped those
      servers into this application yet.
      See [Updates about my migrations don't appear
      inside an application](troubleshooting.md#migs-do-not-appear-in-app "troubleshooting.md#migs-do-not-appear-in-app").

3. The first time a migration task is started for a server associated with the
   application, applications with this server will change to the **In progress** status, automatically. After verifying the in-progress
   migration status from the application's detail screen, if the status is still
   **Not started**, you can manually change it to
   **In progress**. To change the status, choose
   **In progress** from the **Update
   status** menu.
4. Choose **Confirm**. A green confirmation message appears at the
   top of the screen, and the status label changes to **In
   progress**.
5. When the data in the application's detail screen indicates migration has
   completed, and you've performed testing and verification, change the status from
   **In progress** to **Completed** from the
   **Update status** menu.
6. Choose **Confirm**. A green confirmation message appears at the
   top of the screen, and the status label changes to
   **Completed**.
