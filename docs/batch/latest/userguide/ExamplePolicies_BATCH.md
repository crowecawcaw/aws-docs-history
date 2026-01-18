# Resource: Example policies for AWS Batch

You can create specific IAM policies to restrict the calls and resources that users in
your account have access to. Then, you can attach those policies to users.

When you attach a policy to a user or group of users, the policy allows or denies the users
permission for specific tasks on specific resources. For more information, see [Permissions and Policies](../../../IAM/latest/UserGuide/PermissionsAndPolicies.md "../../../IAM/latest/UserGuide/PermissionsAndPolicies.md") in the
_IAM User Guide_. For instructions on how to manage and create custom IAM
policies, see [Managing IAM
Policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md").

The following examples show policy statements that you can use to control the permissions that users have for
AWS Batch.

###### Examples

- [Read-only access](iam-example-read-only.md "iam-example-read-only.md")
- [Resource: Restrict user, image, privilege, role](iam-example-job-def.md "iam-example-job-def.md")
- [Restrict job submission](iam-example-restrict-job-submission.md "iam-example-restrict-job-submission.md")
- [Restrict to a job queue](iam-example-restrict-job-queue.md "iam-example-restrict-job-queue.md")
- [Deny action when all conditions match strings](iam-example-job-def-deny-all-image-logdriver.md "iam-example-job-def-deny-all-image-logdriver.md")
- [Resource: Deny action when any
  condition keys match strings](iam-example-job-def-deny-any-image-logdriver.md "iam-example-job-def-deny-any-image-logdriver.md")
- [Use the batch:ShareIdentifier condition key](iam-example-share-identifier.md "iam-example-share-identifier.md")
- [Manage SageMaker AI resources with AWS Batch](iam-example-full-access-service-environment.md "iam-example-full-access-service-environment.md")
- [Restrict job submission by resource tags](iam-example-restrict-job-submission-by-tags.md "iam-example-restrict-job-submission-by-tags.md")
