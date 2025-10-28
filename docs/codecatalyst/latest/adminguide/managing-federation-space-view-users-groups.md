Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Viewing SSO users and groups for

a space

You must have the **Space administrator** role and access to the billing
account for your space to view SSO users and groups for your space. You cannot directly
add or remove SSO users or groups in CodeCatalyst.

###### Note

Users or groups that are added to IAM Identity Center assignments usually appear in CodeCatalyst within two
hours. Depending on the amount of data being synchronized, this process might take longer.

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. To view users in each group, choose the group. To view application details in the
   AWS Management Console, choose **View application**.

To view information in IAM Identity Center, choose **IAM Identity Center**. You will be taken to
IAM Identity Center, where you can work with your Identity federation administrator to configure SSO
users and groups for your instance in IAM Identity Center.
