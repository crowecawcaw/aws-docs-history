# Setting up email notifications for builds

You can set up email notifications for an AWS Amplify app to alert stakeholders or team members when a
build succeeds or fails. Amplify Hosting creates an Amazon Simple Notification Service (SNS) topic in your account and uses
it to configure email notifications. Notifications can be configured to apply to all branches or specific branches
of an Amplify app.

## Setting up email notifications

Use the following procedures to set up email notifications for all branches or specific
branches of an Amplify app.

###### To set up email notifications for an Amplify app

1. Sign in to the AWS Management Console and open the [Amplify
   console](https://console.aws.amazon.com/amplify/ "https://console.aws.amazon.com/amplify/").
2. Choose the app that you want to set up email notifications for.
3. In the navigation pane, choose **Hosting**, **Build
   notifications**. On the **Build notifications** page, choose
   **Manage notifications**.
4. On the **Manage notifications** page, choose **Add new**.
5. Do one of the following:
   - To send notifications for a single branch, for **Email**, enter the
     email address to send notifications to. For **Branch**, select the name of
     the branch to send notifications for.
   - To send notifications for all connected branches, for **Email**, enter
     the email address to send notifications to. For **Branch**, choose
     _All Branches_.

6. Choose **Save**.
