# Create IAM roles for your compute environments and container instances

Your AWS Batch compute environments and container instances require AWS account credentials to make calls to
other AWS APIs on your behalf. Create an AWS Identity and Access Management role that provides these credentials to your compute environments
and container instances, then associate that role with your compute environments.

###### Note

To verify that your AWS account has the required permissions, see [Initial IAM service set up for your account](../../../IAM/latest/UserGuide/getting-started_create-admin-group.md "../../../IAM/latest/UserGuide/getting-started_create-admin-group.md").

The AWS Batch compute environment and container instance roles are automatically created for you in the console
first-run experience. So, if you intend to use the AWS Batch console, you can move ahead to the next section. If you
plan to use the AWS CLI instead, complete the procedures in [Using service-linked roles for
AWS Batch](using-service-linked-roles.md "using-service-linked-roles.md"), [Amazon ECS instance role](instance_IAM_role.md "instance_IAM_role.md"), and [Tutorial: Create the IAM execution role](create-execution-role.md "create-execution-role.md") before
creating your first compute environment.
