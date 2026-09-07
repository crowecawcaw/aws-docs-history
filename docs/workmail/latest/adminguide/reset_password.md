

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Resetting user password
<a name="reset_password"></a>

If a user forgets their password or has trouble signing in to Amazon WorkMail, you can reset their password. 

**Note**  
If you've integrated Amazon WorkMail with an AD Connector directory, you must reset the user password in Active Directory.
If you've integrated Amazon WorkMail with IAM Identity Center, you can choose to reset the user password. For more information, see [ Reset the IAM Identity Center user password for an end user](https://docs.aws.amazon.com/singlesignon/latest/userguide/reset-password-for-user.html) in the *AWS IAM Identity Center User Guide*.



**To reset a user password**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, then choose the name of your organization.

1. In the navigation pane, choose **Users**.

1. In the list of users, select the check box next to the name of the user, and then choose **Reset password**.

1. In the **Reset Password** dialog box, enter the new password, and then choose **Reset**.