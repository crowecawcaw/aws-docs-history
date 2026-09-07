

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Guest users
<a name="guest-users"></a>

The Wickr guest user feature allows individual guest users to sign in to the Wickr client and collaborate with Wickr network users. Wickr administrators can enable or disable guest users for their Wickr networks in the **Security Group** page of the Wickr admin console.

After the feature is enabled, guest users invited to your Wickr network can interact with users in your Wickr network. An add-on fee will apply for guests. 

![Guest user menu.](http://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/images/wickr-ent-guest-user.png)


**Topics**
+ [Enable or disable guest users](#guest-users-enable-disable)
+ [Block a guest user](#guest-user-block-user)

## Enable or disable guest users
<a name="guest-users-enable-disable"></a>

You can control guest user access from federation settings in security groups. To enable the guest user feature, see [ Federation](https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/federation.html).

## Block a guest user
<a name="guest-user-block-user"></a>

Blocked users can't communicate with anyone in your network.

**To block a guest user**

1. On the **Networks** page, choose the **Admin** link, to navigate to the Wickr Admin Console for that network.

1. In the navigation pane of the Wickr Admin Console, choose **User**, and then choose **Guest Users**.

1. On the **Guest Users** page, choose the **Guest Users** section.

1. The **Guest Users** section shows the guest users that have communicated in your Wickr network.

1. In the **Guest Users** section, find the email of the guest user you want to block.

1. On the right-hand side of the guest user's name, select the three dots, and choose **Block**.

1. Choose **Block** on the pop-up window.

1. To view the list of blocked users in your Wickr network, choose the **Blocked Users** section.

**To unblock a guest user**

1. On the **Networks** page, choose the **Admin** link, to navigate to the Wickr Admin Console for that network.

1. In the navigation pane of the Wickr Admin Console, choose **User**, and then choose **Guest Users**.

1. On the **Guest Users** page, choose the **Blocked Users** section.

1. The **Blocked Users** section shows the guest users that are blocked in your Wickr network.

1. In the **Blocked Users** section, find the email of the guest user you want to unblock.

1. On the right-hand side of the guest user's name, select the three dots, and choose **Unblock**.

1. Choose **Unblock** in the pop-up window.