# Identity-based policy

examples

By default, IAM users and roles who have one of the managed policies for AWS CodeCommit,
AWS CodeBuild, AWS CodeDeploy, or AWS CodePipeline applied have permissions to connections,
notifications, and notification rules that align with the intent of those policies. For
example, IAM users or roles that have one of the full access policies
(**AWSCodeCommitFullAccess**,
**AWSCodeBuildAdminAccess**,
**AWSCodeDeployFullAccess**, or
**AWSCodePipeline_FullAccess**) applied to them also have full
access to notifications and notification rules created for the resources for those
services.

Other IAM users and roles don't have permission to create or modify AWS CodeStar Notifications and AWS CodeConnections
resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An
IAM administrator must create IAM policies that grant users and roles permission to
perform API operations on the specified resources they need. The administrator must then
attach those policies to the IAM users or groups that require those
permissions.
