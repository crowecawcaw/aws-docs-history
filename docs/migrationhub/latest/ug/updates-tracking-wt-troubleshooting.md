AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Troubleshooting and manually

mapping migration updates in AWS Migration Hub

You can verify that the migration update is mapped to a server by viewing the update
on the **Updates** page. If a server has not been mapped to a migration
and you just started the migration task, see if it appears as mapped after waiting five
minutes and refreshing the page.

If after an initial wait of five minutes the update is still not mapped to a server,
then you can manually map the update to a server by selecting the
**Map** button. For more information, see the following procedure,
_To manually map a migration update to a discovered server_. For
officially supported migration tools, you should not need to manually map migration
updates. If this happens frequently, please contact AWS Support.

The following steps show you how to manually map a migration update to a discovered
server that couldn't be automapped.

###### To manually map a migration update to a discovered server

1. In the navigation pane, under **Migrate**, select
   **Updates**.
2. For each migration update row that has a **Map** button
   present in the **Action** column, select the
   **Map** button.
3. In the **Map to discovered server** box, select the radio
   button of the server you want to map to the migration update.
4. Choose **Save**. A green confirmation message appears at the
   top of the screen.
5. Verify that the server name of the server you just mapped is now present in
   the **Mapped servers** column.
