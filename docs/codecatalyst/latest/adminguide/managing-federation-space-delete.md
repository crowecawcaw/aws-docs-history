Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Deleting a space that supports

identity federation

You can delete a space that supports identity federation when you no longer need it.

###### Note

Deleting the space will delete all projects and resources in the space. Deleting
the space will remove the associated SSO users and groups from the space.

You must have the **Space administrator** role and access to the billing
account for your space to view SSO users and groups for your space.

###### To delete a space that supports identity federation

1. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").
2. On the page for your space, choose **Delete**.

###### Tip

Make sure you are signed in to the AWS Management Console with the AWS account that will be the
specified billing account for your space. 3. Choose **Delete**. 4. You can retain the previously associated Identity Center application or delete it.
