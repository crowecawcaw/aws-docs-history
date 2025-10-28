This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Delete a security group in

AWS Wickr

You can delete your Wickr security group.

Complete the following procedure to delete a security group.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, select the network name to
   navigate to that network.
3. In the navigation pane, choose **Security
   groups**.
4. On the **Security groups** page, find the security group
   you want to delete.
5. On the right-hand side of the security group you want to delete, select
   the vertical ellipsis icon (three dots), and then choose
   **Delete**.
6. Type **confirm** in the pop-up window, and then choose
   **Delete**.

When you delete a security group that has assigned users, those users are
automatically added to the default security group. To modify the security
group assigned to users see [Edit users in AWS Wickr network](edit-users.md "edit-users.md").
