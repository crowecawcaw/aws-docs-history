This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Bulk suspend users in AWS Wickr network

You can bulk suspend Wickr network users in the **User**
section of the Wickr Admin Console for Wickr.

###### Note

The option to bulk suspend users only applies when SSO is not enabled.

To bulk suspend your Wickr network users, complete the following
procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. In the navigation pane of the Wickr Admin Console, choose
   **User**, and then choose **Team
   Directory**.

The **Team Directory** page displays users registered to
your Wickr network. 3. On the **Team Directory** page, choose **Manage
Users**. 4. On the **Manage Users** pop-up window, choose
**Suspend Users**. 5. Download the sample CSV template. To download the sample template, choose
**Download Template**. 6. Complete the template by adding the email of the users you want to bulk
suspend from your network. 7. Upload the completed CSV template. You can drag and drop the file into the
upload box, or select **choose a file**. 8. After your upload the CSV file, choose **Suspend
Users**.

###### Note

This action will immediately start suspending users and may take
several minutes. Suspended users can't sign in to your Wickr network
in the Wickr client. When you suspend a user who is currently signed
in to your Wickr network in the client, that user is automatically
signed out.
