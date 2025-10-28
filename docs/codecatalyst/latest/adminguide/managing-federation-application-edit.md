Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Editing Identity Center application details

You can edit the details for your Identity Center application, such as choosing SSO users and groups
that are available in IAM Identity Center.

###### Note

Users or groups that are added to IAM Identity Center assignments usually appear in CodeCatalyst within two
hours. Depending on the amount of data being synchronized, this process might take longer.

###### To edit space and Identity Center application details

1. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").
2. Choose **IAM Identity Center**. On the **IAM Identity Center** page, under
   **Application Enabled Spaces**, view the spaces enabled for SSO and
   associated with your application.

###### Tip

Make sure you are signed in to the AWS Management Console with the AWS account that will be the
specified billing account for your space. 3. Choose your space from the list, and then choose **Edit
space**, 4. On the **Edit assigned users and groups** page, view your application
details. 5. In **Groups connected to this space**, choose the SSO groups that you
want to add to your space. The users in these groups can be viewed in the member
lists in your CodeCatalyst space, projects, and teams. 6. Under **Space administrators**, in **Assign additional
administrators**, choose the users to which you want to assign the
**Space administrator** role for your space. These are members of the
SSO group who have individual permissions in CodeCatalyst. 7. To make updates to your connected groups, choose **Manage in IAM Identity Center**.
You will be taken to IAM Identity Center where you can work with your Identity federation administrator
to configure SSO users and groups for your instance in IAM Identity Center.
