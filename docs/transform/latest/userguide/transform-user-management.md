# Managing users

AWS Transform integrates with IAM Identity Center for user management. This section describes how to add users to IAM Identity Center and grant them access to AWS Transform.

## Adding users in IAM Identity Center

To add users in IAM Identity Center:

1. Navigate to the IAM Identity Center console.
2. In the navigation pane, choose **Users**.
3. Choose **Add user**.
4. Enter the required information:
   - **Username** - A unique identifier for the user (cannot be changed later)
   - **Email address** - The user's email address
   - **First name** and **Last name** - The user's name
   - **Display name** - The name that appears in the user list

5. For **Password**, choose how the user receives their password:
   - **Send an email** - Send setup instructions via email
   - **Generate a one-time password** - Create a password to share manually

6. Choose **Next** to review the user information.
7. Review the details and choose **Add user**.

After the user is added, they'll receive an email invitation to set up their IAM Identity Center account. The invitation link is valid for 7 days.

You can also learn about working with IAM Identity Center and AWS Transform in this video:

## Adding users to AWS Transform

After adding users to IAM Identity Center, you can grant them access to AWS Transform:

1. Return to the AWS Transform console.
2. In the navigation pane, choose **Users and groups**.
3. Select the **Users** tab or the **Groups** tab.
4. Search for and select the users or groups that you want to add from IAM Identity Center.
5. Choose **Assign users and groups** to grant the selected users or groups access to AWS Transform.

After adding users, they appear in the **Users** list with a status of "Pending" until they accept the invitation and sign in.
