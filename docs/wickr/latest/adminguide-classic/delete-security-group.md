This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Delete a security group in

AWS Wickr

You can delete your Wickr security group.

Complete the following procedure to delete a security group.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, choose the **Admin** link,
   to navigate to Wickr Admin Console for that network.

You're redirected to the Wickr Admin Console for a specific network. 3. In the navigation pane of the Wickr Admin Console, choose
**Network Settings**, and then choose
**Security Group**. 4. Choose the vertical ellipsis icon next to the name of the security group
that you want to delete. 5. Choose **Remove** to delete the security group.

When you delete a security group that has assigned users, those users are
automatically added to the default security group. To modify the security
group assigned to users see [Edit users in AWS Wickr network](edit-users.md "edit-users.md").
