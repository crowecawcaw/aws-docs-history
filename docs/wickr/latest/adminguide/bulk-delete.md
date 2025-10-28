This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Bulk delete users in AWS Wickr network

You can bulk delete Wickr network users in the **User
management** section in the AWS Management Console for Wickr.

###### Note

The option to bulk delete users only applies when SSO is not enabled.

To bulk delete your Wickr network users using a CSV template, complete the
following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **User
   management**.
4. The **Team directory** tab displays users registered to
   your Wickr network.
5. In the **Team directory** tab, choose **Manage
   users**, and then choose **Bulk delete**.
6. On the **Bulk delete users** page, download the sample
   CSV template. To download the sample template, choose **Download
   template**.
7. Complete the template by adding the email of the users you want to bulk
   delete from your network.
8. Upload the completed CSV template. You can drag and drop the file into the
   upload box, or select **choose a file**.
9. Select the check box, **I understand that deleting user is not
   reversible**.
10. Choose **Delete users**.

###### Note

This action will immediately start deleting users and may take several
minutes. Deleted users will no longer able to sign in to your Wickr
network in the Wickr client.
To bulk delete your Wickr network users by downloading a CSV of your team
directory, complete the following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **User
   management**.
4. The **Team directory** tab displays users registered to
   your Wickr network.
5. In the **Team directory** tab, choose **Manage
   users**, and then choose **Download as CSV**.
6. After you download the team directory CSV template, remove the rows of
   users who don't need to be deleted.
7. In the **Team directory** tab, choose **Manage
   users**, and then choose **Bulk delete**.
8. On the **Bulk delete users** page, upload the team
   directory CSV template. You can drag and drop the file into the upload box,
   or select **Choose a file**.
9. Select the check box, **I understand that deleting user is not
   reversible**.
10. Choose **Delete users**.

###### Note

This action will immediately start deleting users and may take several
minutes. Deleted users will no longer able to sign in to your Wickr
network in the Wickr client.
