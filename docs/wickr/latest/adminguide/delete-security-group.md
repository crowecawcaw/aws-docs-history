

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Delete a security group in AWS Wickr
<a name="delete-security-group"></a>

You can delete your Wickr security group.

Complete the following procedure to delete a security group.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **Security groups**.

1. On the **Security groups** page, find the security group you want to delete.

1. On the right-hand side of the security group you want to delete, select the vertical ellipsis icon (three dots), and then choose **Delete**.

1. Type **confirm** in the pop-up window, and then choose **Delete**.

   When you delete a security group that has assigned users, those users are automatically added to the default security group. To modify the security group assigned to users see [Edit users in AWS Wickr network](edit-users.md).