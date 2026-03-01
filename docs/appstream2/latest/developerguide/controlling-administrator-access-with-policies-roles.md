# Using AWS Managed Policies and Linked Roles to Manage Administrator Access to WorkSpaces Applications Resources

By default, IAM users don't have the permissions required to create or modify WorkSpaces Applications
resources, or perform tasks by using the WorkSpaces Applications API. This means that these users can't
perform these actions in the WorkSpaces Applications console or by using WorkSpaces Applications AWS CLI commands. To
allow IAM users to create or modify resources and perform tasks, attach an IAM
policy to the IAM users or groups that require those permissions.

When you attach a policy to a user, group of users, or IAM role, it allows or denies the users
permission to perform the specified tasks on the specified resources.

###### Contents

- [AWS Managed Policies Required to Access WorkSpaces Applications Resources](managed-policies-required-to-access-appstream-resources.md "managed-policies-required-to-access-appstream-resources.md")
- [Roles Required for WorkSpaces Applications, Application Auto Scaling, and AWS Certificate Manager Private CA](roles-required-for-appstream.md "roles-required-for-appstream.md")
- [Checking for the AmazonAppStreamServiceAccess Service Role and Policies](controlling-access-checking-for-iam-service-access.md "controlling-access-checking-for-iam-service-access.md")
- [Checking for the ApplicationAutoScalingForAmazonAppStreamAccess Service Role and Policies](controlling-access-checking-for-iam-autoscaling.md "controlling-access-checking-for-iam-autoscaling.md")
- [Checking for the AWSServiceRoleForApplicationAutoScaling_AppStreamFleet Service-Linked Role and Policies](controlling-access-checking-for-iam-service-linked-role-application-autoscaling-appstream-fleet.md "controlling-access-checking-for-iam-service-linked-role-application-autoscaling-appstream-fleet.md")
- [Checking for the AmazonAppStreamPCAAccess Service Role and Policies](controlling-access-checking-for-AppStreamPCAAccess.md "controlling-access-checking-for-AppStreamPCAAccess.md")
