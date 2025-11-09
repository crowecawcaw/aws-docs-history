# User Pool Administration in Amazon WorkSpaces Applications

To create and manage users in the user pool, sign in to the WorkSpaces Applications console for the AWS
Region you want and choose **User Pool** in the left navigation pane.
The User Pool dashboard supports bulk operations on a list of users for some actions.
You can select multiple users on which to perform the same action from the
**Actions** list. Users in the user pool are created and managed on a per-Region basis.

WorkSpaces Applications does not support bulk user creation or disable. However, you can use
Amazon Cognito with the [CreateStreamingURL](../APIReference/API_CreateStreamingURL.md "../APIReference/API_CreateStreamingURL.md") API action to manage access efficiently for multiple
users. Amazon Cognito user pools let you quickly create your own directory to sign up and sign in
users. In addition, you can use Amazon Cognito user pools to store user profiles. For information
about how to integrate WorkSpaces Applications with your Cognito User Pool, see the [Create a SaaS
Portal with Amazon WorkSpaces Applications](https://aws.amazon.com/appstream2/getting-started/isv-workshops/saas/ "https://aws.amazon.com/appstream2/getting-started/isv-workshops/saas/") tutorial.

###### Note

WorkSpaces Applications sends email to users on your behalf when you create a new user created or assign a user to a stack. To ensure the email is delivered, add
`no-reply@accounts.`aws-region-code`.amazonappstream.com`
to your allow list, where `aws-region-code` is
a valid AWS Region code in which you are working. If users are having difficulty
finding the emails, ask them to check their "spam" email folder.

###### Tasks

- [Creating a User in Amazon WorkSpaces Applications](user-pool-admin-create.md "user-pool-admin-create.md")
- [Deleting a User in Amazon WorkSpaces Applications](user-pool-admin-deleting-user.md "user-pool-admin-deleting-user.md")
- [Assigning Stacks to Users in Amazon WorkSpaces Applications](user-pool-admin-assigning.md "user-pool-admin-assigning.md")
- [Unassigning Stacks from Users in Amazon WorkSpaces Applications](user-pool-admin-unassigning.md "user-pool-admin-unassigning.md")
- [Disabling Users in Amazon WorkSpaces Applications](user-pool-admin-disabling.md "user-pool-admin-disabling.md")
- [Enabling Users in Amazon WorkSpaces Applications](user-pool-admin-enabling.md "user-pool-admin-enabling.md")
- [Re-Sending Welcome Email in Amazon WorkSpaces Applications](user-pool-admin-email.md "user-pool-admin-email.md")
