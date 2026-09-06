

# Add or remove portal administrators
<a name="portal-change-admins-ai"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

In a few steps, you can add or remove users as administrators for a portal. Based on the user authentication service, choose one of the following options.

------
#### [ IAM Identity Center ]

![Portal administrators section of the portal details page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-SSOAdminDetail.png)


**To add portal administrators**

1. On the portal details page, in the **Administrators** section, choose **Assign administrators**.

1. On the **Assign administrators** page, select the users to add to the portal as administrators.
**Note**  
If you use IAM Identity Center as your identity store, and you're signed in to your AWS Organizations management account, you can choose **Create user** to create an IAM Identity Center user. IAM Identity Center sends the new user an email for them to set their password. You can then assign the user to the portal as an administrator. For more information, see [Manage identities in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

1. Choose **Assign administrators**.

![The "Assign administrators" page.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-SSOAdminAssign.png)


**To remove portal administrators**
+ On the portal details page, in the **Portal administrators** section, select the check box for each user to remove, and then choose **Remove from portal**.
**Note**  
The **Administrators(\#)** lists the number of administrators for the portal. You can add multiple portal administrators to manage and work on projects. 

------