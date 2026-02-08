# Switching AWS Regions

We recommend that you install IAM Identity Center in a Region that you intend to keep available for
users, not a Region that you might need to disable. For more information, see [Considerations for choosing an
AWS Region](identity-center-region-considerations.md "identity-center-region-considerations.md").

You can switch your IAM Identity Center Region only by [deleting your current
IAM Identity Center instance](delete-config.md "delete-config.md") and creating an instance in another Region. If you already enabled an
AWS managed application with your existing IAM Identity Center instance, disable the application before
deleting IAM Identity Center. For instructions on disabling AWS managed applications, see [Disabling an AWS managed application](awsapps-remove.md "awsapps-remove.md").

###### Note

If you are considering switching your IAM Identity Center Region to enable the deployment of an AWS managed application in another Region,
consider replicating your IAM Identity Center instance to that Region instead.
For more information, see [Using IAM Identity Center across multiple
AWS Regions](multi-region-iam-identity-center.md "multi-region-iam-identity-center.md").

###### Configuration considerations in the new Region

You must recreate users, groups, permission sets, applications, and assignments in the new
IAM Identity Center instance. You can use the IAM Identity Center account and application assignment [APIs](../APIReference/welcome.md "../APIReference/welcome.md") to get a
snapshot of your configuration and then use that snapshot to rebuild your configuration in a new
Region. Switching to a different Region also changes the URL for the [AWS access portal](using-the-portal.md "using-the-portal.md"), which provides your users with single sign-on
access to their AWS accounts and applications. You might also need to recreate some IAM Identity Center
configuration through the Management Console of your new instance.
