

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Associating Amazon WorkMail users with IAM Identity Center users
<a name="connecting_wmusers"></a>

When a user signs in to the Amazon WorkMail web client with their IAM Identity Center user credentials, the client will open the mailbox of the associated Amazon WorkMail user. If no user in the WorkMail organization is associated with the IAM Identity Center user, WorkMail will create an association between the IAM Identity Center user signing in and the WorkMail user having the same username, if such a WorkMail user exists. Otherwise, the client will display an error message to the user.

**Note**  
You are recommended to use the same username for a user across Amazon WorkMail and IAM Identity Center because WorkMail will create the association automatically when the user first signs in to the Amazon WorkMail web client with their IAM Identity Center user credentials. When the usernames are different, you are responsible to create the association.

**To associate users, follow these steps.**

1. Open the Amazon WorkMail console at [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/).

   If necessary, change the AWS Region. In the bar at the top of the console window, open the **Select a Region** list and choose a Region. For more information, see [Region and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*.

1. In the navigation pane, choose **Identity Center**.

   The **IAM Identity Center Settings** page appears.

1. Choose **Associate users**.

1. Under **Select a WorkMail user**, select the Amazon WorkMail user you wish to associate.

1. Under **Enter the IAM Identity Center user ID**, enter the ID of the IAM Identity Center user you wish to associate. You may copy the ID from the **Assigned users** tab on the **Identity Center** page.
**Note**  
The IAM Identity Center user must be authorized to access the Amazon WorkMail application.

1. Choose **Associate users**.

   Once the association is successful, the Amazon WorkMail user can log into Amazon WorkMail using the MFA IAM Identity Center credentials.

**Note**  
You can also associate Amazon WorkMail users with IAM Identity Center users when you edit the Amazon WorkMail user details. For more information, see [Editing user details](edit_user.md).