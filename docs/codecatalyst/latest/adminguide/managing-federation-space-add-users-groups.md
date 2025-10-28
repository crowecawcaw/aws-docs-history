Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Adding SSO groups to a space

that supports identity federation

You can use the Amazon CodeCatalyst page in the AWS Management Console to add SSO groups to your space. You must have
already worked with your Identity federation administrator to create the SSO users and groups
for your instance in IAM Identity Center. For a high-level reference to the prerequisites steps to configure
SSO users and groups in IAM Identity Center, see [Prerequisite 3: Setting up identity federation in
IAM Identity Center](setting-up-federation.md#setting-up-prereq-identity "setting-up-federation.md#setting-up-prereq-identity").

###### Note

Users or groups that are added to IAM Identity Center assignments usually appear in CodeCatalyst within two
hours. Depending on the amount of data being synchronized, this process might take longer.

You must have the **Space administrator** role and access to the billing
account for your space to view SSO users and groups for your space.

You cannot directly add or remove users to your space in CodeCatalyst. You must work with your
Identity federation administrator to manage SSO users and groups in IAM Identity Center. CodeCatalyst syncs on a
regular basis with the IAM Identity Center identity store with the latest directory status for your
space members.

1. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").
2. Navigate to the page for your space. Choose **Edit SSO**. Choose
   the SSO groups you want to add to your space.
3. To view more information in IAM Identity Center, choose **IAM Identity Center**.
