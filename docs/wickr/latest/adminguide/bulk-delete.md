

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Bulk delete users in AWS Wickr network
<a name="bulk-delete"></a>

You can bulk delete Wickr network users in the **User management** section in the AWS Management Console for Wickr.

**Note**  
The option to bulk delete users only applies when SSO is not enabled.

To bulk delete your Wickr network users using a CSV template, complete the following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **User management**.

1. The **Team directory** tab displays users registered to your Wickr network.

1. In the **Team directory** tab, choose **Manage users**, and then choose **Bulk delete**. 

1. On the **Bulk delete users** page, download the sample CSV template. To download the sample template, choose **Download template**.

1. Complete the template by adding the email of the users you want to bulk delete from your network.

1. Upload the completed CSV template. You can drag and drop the file into the upload box, or select **choose a file**.

1. Select the check box, **I understand that deleting user is not reversible**.

1. Choose **Delete users**.
**Note**  
This action will immediately start deleting users and may take several minutes. Deleted users will no longer able to sign in to your Wickr network in the Wickr client.

To bulk delete your Wickr network users by downloading a CSV of your team directory, complete the following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **User management**.

1. The **Team directory** tab displays users registered to your Wickr network.

1. In the **Team directory** tab, choose **Manage users**, and then choose **Download as CSV**. 

1. After you download the team directory CSV template, remove the rows of users who don't need to be deleted.

1. In the **Team directory** tab, choose **Manage users**, and then choose **Bulk delete**. 

1. On the **Bulk delete users** page, upload the team directory CSV template. You can drag and drop the file into the upload box, or select **Choose a file**.

1. Select the check box, **I understand that deleting user is not reversible**.

1. Choose **Delete users**.
**Note**  
This action will immediately start deleting users and may take several minutes. Deleted users will no longer able to sign in to your Wickr network in the Wickr client.