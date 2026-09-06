

# Add portal users in SiteWise Monitor
<a name="monitor-add-portal-users"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

You control which users have access to your portals. In each portal, the portal administrators create one or more projects and assign portal users as owners or viewers for each project. Each project owner can invite additional portal users to own or view the project.

Based on the user authentication service, choose one of the following options:

------
#### [ IAM Identity Center ]

If you want to add a user to the **Users** list, complete the following steps.

**To add portal users**

1. Choose users from the **Users** list to add to the portal. This adds the users to the **Portal users** list. If you're using SiteWise Monitor for the first time, you don't need to add your portal administrator as a portal user.
**Note**  
If you use IAM Identity Center as your identity store, and you're signed in to your AWS Organizations management account, you can choose **Create user** to create an IAM Identity Center user. IAM Identity Center sends the new user an email for them to set their password. You can then assign the user to the portal as a user. For more information, see [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

1. If you add a user that you don't want to have access to the portal, clear the check box for that user.

1. When you're finished selecting users, choose **Assign users**.

![The assign IAM Identity Center users step of the portal creation process.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/SSOUserAssign.png)


------
#### [ IAM ]

If you see the user or role that you want to add in the **IAM users** or **IAM roles** list, complete the following steps.

**To add portal users**

1. Do the following options:
   + Choose **IAM users** to add an IAM user as a portal user.
   + Choose **IAM roles** to add an IAM role as a portal user.

   If you're using SiteWise Monitor for the first time, you don't need to add your portal administrator as a portal user.

1. Select the check boxes for the users or roles that you want as portal users. This adds the users or roles to the **Portal users** list.

1. If you add a user that you don't want to have access to the portal, clear the check box for that user.

1. When you're finished selecting users, choose **Assign users**.

**Important**  <a name="iam-portal-user-permissions"></a>
Users or roles must have the `iotsitewise:DescribePortal` permission to sign in to the portal.

![The assign IAM users step of the portal creation process.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMUserAssign.png)


![The assign IAM step of the portal creation process.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMRoleAssign.png)


------

Congratulations\! You successfully created a portal, assigned portal administrators, and assigned users who can use that portal when invited to do so. Your portal administrators can now create projects and add assets to those projects. Then, your project owners can create dashboards to visualize the data for each project's assets.

You can change the list of portal users later. For more information, see [Add or remove portal users in AWS IoT SiteWise](portal-change-users.md).

If you need to make changes to the portal, see [Administer your SiteWise Monitor portals](administer-portals.md).

To get started in the portal, see [Getting started](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/getting-started.html) in the *SiteWise Monitor Application Guide*.