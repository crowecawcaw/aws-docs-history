

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Adding a user
<a name="add_user"></a>

When you add a user, Amazon WorkMail automatically creates mailboxes for them. Users can log in and access their mail from the Amazon WorkMail web application, their mobile device, or by using Microsoft Outlook on macOS or PC.

**To add a user**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Regions and endpoints](http://docs.aws.amazon.com/general/latest/gr/index.html?rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Organizations**, and then choose the organization to which you want to add users.

1. In the navigation pane, choose **Users**, and then choose **Add User**.

   The **Add a user** screen appears.

1. Under **User details**, in the **User name** field, enter the user's name. The name also appears in the **Email address** box. If you want the user to have a different email address from their user name, you can edit the **Email address** field.

1. (Optional) Enter the user's first and last name in the **First name** and **Last name** boxes. 

1. In the **Display name** box, enter the user's display name.

1. In the **Email address** box, accept the email alias or enter another one.

1. By default, user are displayed in the global address list. To hide the user from the global address list, clear the **Show in global address list** check box.

1. Select **Do not create a mailbox** to add a user as a remote user to the organization.

1. Under **Password setup**, enter the user's password in the **Password** and **Repeat password** boxes.

1. Choose **Add user**.