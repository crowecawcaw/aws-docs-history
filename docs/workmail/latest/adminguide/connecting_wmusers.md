# Associating Amazon WorkMail users with IAM Identity Center users

When a user signs in to the Amazon WorkMail web client with their IAM Identity Center user credentials, the
client will open the mailbox of the associated Amazon WorkMail user. If no user in the WorkMail
organization is associated with the IAM Identity Center user, WorkMail will create an association
between the IAM Identity Center user signing in and the WorkMail user having the same username, if
such a WorkMail user exists. Otherwise, the client will display an error message to the
user.

###### Note

You are recommended to use the same username for a user across Amazon WorkMail and IAM Identity Center
because WorkMail will create the association automatically when the user first signs
in to the Amazon WorkMail web client with their IAM Identity Center user credentials. When the usernames are
different, you are responsible to create the association.

###### To associate users, follow these steps.

1. Open the Amazon WorkMail console at
   [https://console.aws.amazon.com/workmail/](https://console.aws.amazon.com/workmail/ "https://console.aws.amazon.com/workmail/").

If necessary, change the AWS Region. In the bar at the top of the console
window, open the **Select a Region** list and
choose a Region. For more information, see [Region and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the
_Amazon Web Services General Reference_. 2. In the navigation pane, choose **Identity Center**.

The **IAM Identity Center Settings** page appears. 3. Choose **Associate
users**. 4. Under **Select a WorkMail user**, select the Amazon WorkMail user you
wish to associate. 5. Under **Enter the IAM Identity Center user ID**, enter the ID of the IAM Identity Center
user you wish to associate. You may copy the ID from the **Assigned
users** tab on the **Identity Center**
page.

###### Note

The IAM Identity Center user must be authorized to access the Amazon WorkMail application. 6. Choose **Associate users**.

Once the association is successful, the Amazon WorkMail user can log into Amazon WorkMail using the
MFA IAM Identity Center credentials.

###### Note

You can also associate Amazon WorkMail users with IAM Identity Center users when you edit the Amazon WorkMail user
details. For more information, see [Editing user details](edit_user.md "edit_user.md").
