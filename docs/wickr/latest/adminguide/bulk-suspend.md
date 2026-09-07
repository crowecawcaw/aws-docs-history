

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Bulk suspend users in AWS Wickr network
<a name="bulk-suspend"></a>

You can bulk suspend Wickr network users in the **User management** section in the AWS Management Console for Wickr.

**Note**  
The option to bulk suspend users only applies when SSO is not enabled.

To bulk suspend your Wickr network users, complete the following procedure.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **User management**.

1. The **Team directory** tab displays users registered to your Wickr network.

1. In the **Team directory** tab, choose **Manage users**, and then choose **Bulk suspend**. 

1. On the **Bulk suspend users** page, download the sample CSV template. To download the sample template, choose **Download template**.

1. Complete the template by adding the email of the users you want to bulk suspend from your network.

1. Upload the completed CSV template. You can drag and drop the file into the upload box, or select **choose a file**.

1. Choose **Suspend users**.
**Note**  
This action will immediately start suspending users and may take several minutes. Suspended users can't sign in to your Wickr network in the Wickr client. When you suspend a user who is currently signed in to your Wickr network in the client, that user is automatically signed out.