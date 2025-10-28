Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Using

identity-based policies for CodeGuru Reviewer

By default, users and IAM roles don't have permission to create or modify
Amazon CodeGuru Reviewer resources. They also can't perform tasks using the AWS Management Console,
AWS CLI, or AWS API. An administrator must create IAM policies that grant users
and roles permission to perform specific API operations on the specified resources they
need. The administrator must then attach those policies to the roles or groups
that require those permissions. To learn how to attach policies to an IAM role or group, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Permissions required to use the CodeGuru Reviewer
  console](#console-permissions "#console-permissions")
- [AWS managed (predefined) policies for
  CodeGuru Reviewer](#managed-policies "#managed-policies")
- [CodeGuru Reviewer updates to AWS managed
  policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")
- [Customer managed policy
  examples](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete CodeGuru Reviewer resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Permissions required to use the CodeGuru Reviewer

console

A user who uses the CodeGuru Reviewer console must have a minimum set of permissions that
allows the user to describe other AWS resources for the AWS account. You must
have permissions from the following services:

- CodeGuru Reviewer
- AWS CodeCommit (if your source code is in a CodeCommit repository)
- CodeConnections (if your source code is in a repository managed by CodeConnections, such as
  Bitbucket)
- AWS Identity and Access Management (IAM)

If your source code is in a GitHub repository, you must have an OAuth token to
connect to it. Associated GitHub repositories are not managed by CodeConnections. For more
information, see [Git automation with OAuth tokens](https://help.github.com/en/github/extending-github/git-automation-with-oauth-tokens#step-1-get-an-oauth-token "https://help.github.com/en/github/extending-github/git-automation-with-oauth-tokens#step-1-get-an-oauth-token") on the GitHub website.

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console won't function as intended.

The following shows an example of a permissions policy that allows a user to get
information about a repository association only in the `us-east-2` Region
for account `123456789012` for any repository association with a
universally unique identifier (UUID) that starts with `12345`.

## AWS managed (predefined) policies for

CodeGuru Reviewer

AWS addresses many common use cases by providing standalone IAM policies that
are created and administered by AWS. These AWS managed policies grant necessary
permissions for common use cases so you can avoid having to investigate what
permissions are needed. For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

To create and manage CodeGuru Reviewer service roles, you must also attach the AWS managed
policy named `IAMFullAccess`.

You can also create your own custom IAM policies to allow permissions for CodeGuru Reviewer
actions and resources. You can attach these custom policies to the roles or
groups that require those permissions.

The following AWS managed policies, which you can attach to users in your
account, are specific to CodeGuru Reviewer.

###### Topics

- [AmazonCodeGuruReviewerFullAccess](#managed-full-access "#managed-full-access")
- [AmazonCodeGuruReviewerReadOnlyAccess](#managed-read-only-access "#managed-read-only-access")
- [AmazonCodeGuruReviewerServiceRolePolicy](#managed-policy-for-codecommit-and-codestar-connections "#managed-policy-for-codecommit-and-codestar-connections")

### AmazonCodeGuruReviewerFullAccess

`AmazonCodeGuruReviewerFullAccess` – Provides full access to
CodeGuru Reviewer, including permissions to tag repository associations and to create,
update, and delete code reviews and repository associations. It also grants
permission to related resources in other services that integrate with CodeGuru Reviewer,
such as Amazon CloudWatch, CodeConnections, and CodeCommit. Apply this only to administrative-level
users to who you want to grant full control over CodeGuru Reviewer repository associations,
code reviews, and related resources in your AWS account, including the ability
to delete code reviews and repository associations.

The `AmazonCodeGuruReviewerFullAccess` policy contains the following
statement.

### AmazonCodeGuruReviewerReadOnlyAccess

`AmazonCodeGuruReviewerReadOnlyAccess` – Grants read-only access to
CodeGuru Reviewer and related resources in other AWS services. Apply this policy to users
who you want to grant the ability to view code reviews, but not to create or
make any changes to them.

The `AmazonCodeGuruReviewerReadOnlyAccess` policy contains the following
statement.

### AmazonCodeGuruReviewerServiceRolePolicy

`AmazonCodeGuruReviewerServiceRolePolicy` – Grants permission to
related resources in CodeCommit, CodeConnections, Amazon S3, and CloudWatch that are required to create
repository associations.

For CodeCommit repository associations, the CodeCommit and CloudWatch permissions in this
policy are required. For associations with repositories that are managed by an
AWS CodeStar connection, such as Bitbucket, the CodeConnections permissions are required. For
code reviews with security analysis, the Amazon S3 permissions are required.

When you create your first association with a CodeCommit, Amazon S3, or CodeConnections managed
repository, CodeGuru Reviewer adds the `AmazonCodeGuruReviewerServiceRolePolicy`
policy to your AWS account. This policy grants CodeGuru Reviewer access to CodeCommit
repositories, CodeConnections resources in your account that have an
`aws:ResourceTag/codeguru-reviewer` tag. It also grants access to Amazon S3
buckets that have a prefix that begins with `codeguru-reviewer-`. When you
associate a CodeCommit repository, CodeGuru Reviewer adds this tag to the repository. When you
associate an CodeConnections managed repository, CodeGuru Reviewer adds this tag to the CodeConnections
resource, if it doesn't already exist.

The `AmazonCodeGuruReviewerServiceRolePolicy` policy contains the
following statement.

## CodeGuru Reviewer updates to AWS managed

policies

View details about updates to AWS managed policies for CodeGuru Reviewer since this service
began tracking these changes. For automatic alerts about changes to this page,
subscribe to the RSS feed on the CodeGuru Reviewer [Amazon CodeGuru Reviewer User Guide document history](doc-history.md "doc-history.md").

| Change                                                                                                                                                                                      | Description                                                                                                                                                                              | Date           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [AmazonCodeGuruReviewerServiceRolePolicy](#managed-policy-for-codecommit-and-codestar-connections "#managed-policy-for-codecommit-and-codestar-connections") – Update to an existing policy | CodeGuru Reviewer added new permissions to allow access to the `CreateBucket`, `ListBucket`, `PutBucketPolicy`, and `PutLifecycleConfiguration` actions on an Amazon S3 bucket resource. | April 28, 2021 |
| CodeGuru Reviewer started tracking changes                                                                                                                                                  | CodeGuru Reviewer started tracking changes for its AWS managed policies.                                                                                                                 | July 2, 2020   | ## Customer managed policy examples You can create your own custom IAM policies to allow permissions for CodeGuru Reviewer actions and resources. You can attach these custom policies to the roles or groups that require those permissions. You can also create your own custom IAM policies for integration between CodeGuru Reviewer and other AWS services. The following example IAM policies grant permissions for various CodeGuru Reviewer actions. Use them to limit CodeGuru Reviewer access for your users and roles. These policies control the ability to perform actions with the CodeGuru Reviewer console, API, AWS SDKs, or the AWS CLI. ###### Note All examples use the US East (Ohio) Region (us-east-2) and contain fictitious account IDs. **Examples** <br>• [Example 1: Allow a user to see all recommendations created in an associated repository](#identity-based-policies-example-1 "#identity-based-policies-example-1") <br>• [Example 2: Allow a user to view code reviews in an associated repository in a single Region](#identity-based-policies-example-2 "#identity-based-policies-example-2") <br>• [Example 3: Allow a user to perform CodeGuru Reviewer operations in a single Region](#identity-based-policies-example-3 "#identity-based-policies-example-3") <br>• [Example 4: Allow read-only access to CodeGuru Reviewer operations for a user connecting from a specified IP address range](#identity-based-policies-example-4 "#identity-based-policies-example-4") ### Example 1: Allow a user to see all recommendations created in an associated repository The following example policy grants permissions for the AWS user with account ID `123456789012` to see a list of all recommendations in their AWS account and Region in the repository association with ID `association-uuid`. ### Example 2: Allow a user to view code reviews in an associated repository in a single Region The following shows an example of a permissions policy that allows a user with account ID `123456789012` to get information about code reviews in Region `us-east-2` in an associated repository with ID `association-uuid`. ### Example 3: Allow a user to perform CodeGuru Reviewer operations in a single Region The following permissions policy uses a wildcard character (`"codeguru-reviewer:*"`) to allow users to perform all CodeGuru Reviewer actions in the us-east-2 Region and not from other AWS Regions. ### Example 4: Allow read-only access to CodeGuru Reviewer operations for a user connecting from a specified IP address range You can create a policy that only allows users CodeGuru Reviewer read-only access if their IP address is within a certain IP address range. The following example grants read-only CodeGuru Reviewer permissions to users whose IP addresses are within the specified IP address block of 203.0.113.0/24. |
