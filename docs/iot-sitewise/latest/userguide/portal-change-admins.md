

# Add or remove portal administrators in AWS IoT SiteWise
<a name="portal-change-admins"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

In a few steps, you can add or remove users as administrators for a portal. Based on the user authentication service, choose one of the following options.

------
#### [ IAM Identity Center ]

![Portal administrators section of the portal details page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/SSOAdminDetail.png)


**To add portal administrators**

1. On the portal details page, in the **Portal administrators** section, choose **Assign administrators**.

1. On the **Assign administrators** page, select the check boxes for the users to add to the portal as administrators.
**Note**  
If you use IAM Identity Center as your identity store, and you're signed in to your AWS Organizations management account, you can choose **Create user** to create an IAM Identity Center user. IAM Identity Center sends the new user an email for them to set their password. You can then assign the user to the portal as an administrator. For more information, see [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

1. Choose **Assign administrators**.

![The "Assign administrators" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/SSOAdminAssign.png)


**To remove portal administrators**
+ On the portal details page, in the **Portal administrators** section, select the check box for each user to remove, and then choose **Remove from portal**.
**Note**  
We recommend that you select at least one portal administrator.

------
#### [ IAM ]

![Portal administrators section of the portal details page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMAdminDetail.png)


**To add portal administrators**

1. On the portal details page, in the **Portal administrators** section, choose **Assign administrators**.

1. On the **Assign administrators** page, do the following:
   + Choose **IAM users**, if you want to add an IAM user as your portal administrator.
   + Choose **IAM roles**, if you want to add an IAM role as your portal administrator.

1. Select the check boxes for the users or roles that you want as your portal administrators. This adds the users or roles to the **Portal administrators** list.

1. Choose **Assign administrators**.

**Important**  <a name="iam-portal-user-permissions"></a>
Users or roles must have the `iotsitewise:DescribePortal` permission to sign in to the portal.

![The "Assign administrators" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMUserAdminAssign.png)


![The "Assign administrators" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/IAMRoleAdminAssign.png)


**To remove portal administrators**
+ On the portal details page, in the **Portal administrators** section, select the check box for each user to remove, and then choose **Remove from portal**.
**Note**  
Leaving a portal without a portal administrator is not recommended.

------