

Amazon CodeCatalyst will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For more information, see [Migrating from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

# Adding the **Space administrator** role to SSO users in a space
<a name="managing-federation-space-change-administrator"></a>

You can use the Amazon CodeCatalyst page in the AWS Management Console to assign the **Space administrator** role to individual users in your SSO groups. You cannot directly add or remove users in your space in CodeCatalyst. You must have already worked with your Identity federation administrator to create the SSO users and groups for your instance in IAM Identity Center. CodeCatalyst syncs on a regular basis with the IAM Identity Center identity store with the latest directory status for your space members.

**Note**  
Users or groups that are added to IAM Identity Center assignments usually appear in CodeCatalyst within two hours. Depending on the amount of data being synchronized, this process might take longer. 

You must have the **Space administrator** role and access to the billing account for your space to view SSO users and groups for your space. 

1. Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2\#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/).

1. Navigate to the page for your space. Choose **Edit IAM Identity Center**. 

1. Choose the individual users that you want to grant the **Space administrator** role for your space.

1. To view more information in IAM Identity Center, choose **IAM Identity Center**.