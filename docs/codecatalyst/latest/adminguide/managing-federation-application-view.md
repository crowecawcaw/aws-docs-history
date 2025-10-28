Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Viewing Identity Center application details

You can view the details for the space associated with your Identity Center application.

###### Note

Users or groups that are added to IAM Identity Center assignments usually appear in CodeCatalyst within two
hours. Depending on the amount of data being synchronized, this process might take longer.

###### To view space and Identity Center application details

1. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").
2. Choose **IAM Identity Center**. On the **IAM Identity Center** page, under
   **Application Enabled Spaces**, view the spaces enabled for SSO and
   associated with your application.

###### Tip

Make sure you are signed in to the AWS Management Console with the AWS account that will be the
specified billing account for your space. 3. In **Space name**, view the name for your space. 4. In **Display name**, view the name that displays on the sign-in page
for your space. 5. In **Application name**, view the name of your Identity Center application. 6. In **Space administrators**, view the users that you have assigned
the **Space administrator** role for your space. These are members of the
SSO group who have individual permissions in CodeCatalyst. 7. In **Connected groups**, view the SSO groups that you have added to
your space. The users in these groups can be viewed in the member lists in your
CodeCatalyst space, projects, and teams. 8. To make updates to your connected groups, choose **Edit
Identity Center application**. You will be taken to IAM Identity Center where you can work with your
Identity federation administrator to configure SSO users and groups for your instance in
IAM Identity Center.
