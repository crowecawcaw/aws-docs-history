# Manage users and groups for the
 monitor

An Organizations owner can use the Deadline Cloud console to manage the users and groups that have
 access to the Deadline Cloud monitor. You can choose from existing IAM Identity Center users and groups, or you
 can add new users and groups from the console.

1. Sign in to the AWS Management Console and open the Deadline Cloud [console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
 From the main page, in the **Get started** section, choose
 **Set up Deadline Cloud** or **Go to
 dashboard**.
2. In the left navigation pane, choose **User management**. By
 default, the **Groups** tab is selected.
Depending on the action to take, choose either the **Groups** tab or **Users** tab.


Groups
###### To create a group

1. Choose **Create group**.
2. Enter a group name. The name must be unique among groups in your
 IAM Identity Center organization.

###### To remove a group

1. Select the group to remove.
2. Choose **Remove**.
3. In the confirmation dialog, choose **Remove
 group**.


###### Note

You are removing the group from IAM Identity Center. Group members can no
 longer sign in to the Deadline Cloud or access farm resources.


Users
###### To add users

1. Choose the **Users** tab.
2. Choose **Add users**.
3. Enter the name, email address, and username for the new
 user.
4. (Optional) Choose one or more IAM Identity Center groups to add the new user
 to.
5. Choose **Send invite** to send the new user an
 email with instructions for joining your IAM Identity Center organization.

###### To remove a user

1. Select the user you to remove.
2. Choose **Remove**.
3. In the confirmation dialog, choose **Remove
 user**.


###### Note

You are removing the user from IAM Identity Center. The user can no longer
 sign in to the Deadline Cloud monitor or access farm resources.
