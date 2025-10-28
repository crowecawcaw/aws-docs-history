This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Enable or disable guest users in AWS Wickr network

You can enable or disable guest users in your Wickr network.

Complete the following procedure to enable or disable guest users for your Wickr
network.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/ "https://console.aws.amazon.com/wickr/").
2. On the **Networks** page, choose the **Admin** link,
   to navigate to Wickr Admin Console for that network.

You're redirected to the Wickr Admin Console for a specific network. 3. In the navigation pane of the Wickr Admin Console, choose **Network
Settings**, and then choose **Security
Group**. 4. Choose **Details** for a specific security group.

###### Note

You can enable guest users for individual security groups only. To enable
guest users for all security groups in your Wickr network, you must enable
the feature for each security group in your network. 5. Choose the **Federation** tab in the security group details
page. 6. There are two locations where the toggle to allow guest users will be
available:

    * **Local Federation —** For networks in US East
     (Northern Virginia), choose **Edit** next to the
     **Local Federation** section of the page.
    * **Global Federation —** For all other networks in
     other regions, choose **Edit** next to the
     **Global Federation** section of the page.

7. Select **Allow guest users** to enable guest users for the
   security group, or deselect it to disable it.
8. Choose **Save** to save the change and make it effective for
   the security group.

Registered users in the specific security group in your Wickr network can
now interact with guest users. For more information, see [Guest
users](../userguide/guest-users.md "../userguide/guest-users.md") in the _Wickr User Guide_.
