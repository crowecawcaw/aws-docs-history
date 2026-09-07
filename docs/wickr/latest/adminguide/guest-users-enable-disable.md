

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Enable or disable guest users in AWS Wickr network
<a name="guest-users-enable-disable"></a>

You can enable or disable guest users in your Wickr network.

Complete the following procedure to enable or disable guest users for your Wickr network.

1. Open the AWS Management Console for Wickr at [https://console.aws.amazon.com/wickr/](https://console.aws.amazon.com/wickr/).

1. On the **Networks** page, select the network name to navigate to that network.

1. In the navigation pane, choose **Security groups**.

1. Select the name for a specific security group.
**Note**  
You can enable guest users for individual security groups only. To enable guest users for all security groups in your Wickr network, you must enable the feature for each security group in your network.

1. Choose the **Federation** tab in the security group.

1. There are two locations where the option to enable guest users are available:
   + **Local federation —** For networks in US East (Northern Virginia), choose **Edit** in the **Local federation** section of the page.
   + **Global federation —** For all other networks in other regions, choose **Edit** in the **Global federation** section of the page.

1. On the **Edit federation** page, select **Enable federation**.

1. Choose **Save changes** to save the change and make it effective for the security group.

   Registered users in the specific security group in your Wickr network can now interact with guest users. For more information, see [Guest users](https://docs.aws.amazon.com/wickr/latest/userguide/guest-users.html) in the *Wickr User Guide*.