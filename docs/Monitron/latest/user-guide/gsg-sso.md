Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Step 4: (optional) Add Amazon Monitron users to your project

In addition to admin users, you can also add users who lack admin permissions. For
example, these users might be technicians who only use the Amazon Monitron mobile app to
monitor assets, acknowledge notifications and enter closure codes.

For users who are not admin users:

- You use IAM Identity Center, not Amazon Monitron, to create their user accounts.
- You use the Amazon Monitron mobile app to add the users to projects, not the Amazon Monitron
  console.

###### Topics

- [To add users to IAM Identity Center](#add-sso "#add-sso")
- [To add a user using the mobile app](#add-user-mobile "#add-user-mobile")
- [How to add a user using the web app](#add-user-web "#add-user-web")

## To add users to IAM Identity Center

If your users already have accounts in IAM Identity Center in your AWS account, you can
skip these steps. You are ready to add the users to your project in the mobile
app. Otherwise, add your users to IAM Identity Center by completing the following
steps.

###### Note

The following steps are not required if all of your users are admin
users.

1. Open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. In the IAM Identity Center console, choose **Users**.
3. Repeat the following steps for each user that will access your project
   in the Amazon Monitron mobile app.
   1. On the **Users** page choose **Add
      user**.
   2. In the **User details** section, provide the
      username and contact information. Leave
      **Password** set to **Send an email
      to the user with password setup
      instructions**.

   ![User details form with fields for username, email, name, and password setup option.](images/gs-project-sso-user-details.png) 3. Choose **Next: Groups**. 4. Choose **Add user**. IAM Identity Center sends the user an
   email that contains a link to activate the IAM Identity Center user. The link
   is valid for up to seven days. Each user must open the email and
   accept the invitation before accessing your project in the Amazon Monitron
   mobile app.

## To add a user using the mobile app

1. Log into the Amazon Monitron mobile app on your smartphone.
2. Navigate to the project or site that you want to add a user to, and
   then to the **Users** list.
3. Choose **Add user**.

![User interface showing a list of users and an "Add user" button in the top right corner.](images/user-list-add.png) 4. Enter a user name.

Amazon Monitron searches the user directory for the user. 5. Choose the user from the list. 6. Choose the role that you want to assign the user:
**Admin**, **Technician**, or
**Viewer**. 7. Choose **Add**.

The new user appears on the **Users** list. 8. Send the new user an email invitation with a link for accessing the
project and downloading the Amazon Monitron mobile app. For more information,
see [Sending an
email invitation](resending-email.md "resending-email.md").

## How to add a user using the web app

1. Select **Users** from the navigation pane.
2. Choose **Add user**.

![User management interface showing a list of users with their roles and sites.](images/webapp_add-user.png) 3. Enter a user name.

Amazon Monitron searches the user directory for the user. 4. Choose the user from the list. 5. Choose the role that you want to assign the user:
**Admin**, **Technician**, or
**Read only**. 6. Choose **Add**.

The new user appears on the **Users** list. 7. Send the new user an email invitation with a link for accessing the
project and downloading the Amazon Monitron mobile app. For more information,
see [Sending an
email invitation](resending-email.md "resending-email.md").

![User management interface showing a list of 10 users with their names, roles, and assigned sites.](images/users-table.png)
