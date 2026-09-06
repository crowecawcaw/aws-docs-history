

# Add or remove portal users in AWS IoT SiteWise
<a name="portal-change-users"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

You choose which users have access to your portals. Portal users appear in the list of users within a SiteWise Monitor portal. From this list, portal administrators can add project owners, and project owners can add project viewers.

**Note**  
Your portal administrators and portal users might contact you through a portal's support email if they need you to add or remove a user.

Based on the user authentication service, choose one of the following options.

------
#### [ IAM Identity Center ]

![Portal administrators section of the portal details page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/SSOUserDetail.png)


**To add portal users**

1. On the portal details page, in the **Portal users** section, choose **Assign users**.

1. On the **Assign users** page, select the check box for the users to add to the portal.
**Note**  
If you use IAM Identity Center as your identity store, and you're signed in to your AWS Organizations management account, you can choose **Create user** to create an IAM Identity Center user. IAM Identity Center sends the new user an email for them to set their password. You can then assign the user to the portal as a user. For more information, see [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

1. Choose **Assign users**.

![The "Assign users" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/SSOUserAssign2.png)


**To remove portal users**
+ On the portal details page, in the **Portal users** section, select the check box for the users to remove from the portal, and then choose **Remove from portal**.

------
#### [ IAM ]

![Portal administrators section of the portal details page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMRoleUserDetail.png)


**To add portal users**

1. On the portal details page, in the **Portal users** section, choose **Assign users**.

1. On the **Assign users** page, do the following:
   + Choose **IAM users** to add an IAM user as your portal user.
   + Choose **IAM roles** to add an IAM role as your portal user.

1. Select the check boxes for the users or roles that you want to add as your portal users. This adds the users or roles to the **Portal users** list.

1. Choose **Assign users**.

![The "Assign users" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMUserAssign2.png)


![The "Assign users" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMRoleAssign2.png)


**To remove portal users**
+ On the portal details page, in the **Portal users** section, select the check box for the users to remove from the portal, and then choose **Remove from portal**.

**Important**  <a name="iam-portal-user-permissions"></a>
Users or roles must have the `iotsitewise:DescribePortal` permission to sign in to the portal.

------