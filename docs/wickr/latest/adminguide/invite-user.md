

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Invite a user in AWS Wickr network
<a name="invite-user"></a>

You can invite a user in your Wickr network.

Complete the following procedure to invite a user in your Wickr network.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **User management**.

1. In the **Team directory** tab, choose **Invite user**.

1. On the **Invite user** page, enter the user's email address and security group. Email address and security group are the only fields that is required. Be sure to choose the appropriate security group for the user. Wickr will send an invitation email to the address you specify for the user.

1. Choose **Invite user**.

   An email is sent to the user. The email provides download links for the Wickr client applications, and a link to register for Wickr. As users register for Wickr using the link in the email, their status in the Wickr team directory will change from **Pending** to **Active**.
**Important**  
Invitation links expire after 21 days. If a user does not register within 21 days, you must resend the invitation from the **Team directory** tab.