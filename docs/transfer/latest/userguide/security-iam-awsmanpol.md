# AWS managed policies for AWS Transfer Family

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create AWS Identity and Access Management (IAM)
customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions that
they need. To get started quickly, you can use our AWS managed policies. These policies
cover common use cases and are available in your AWS account. For more information about
AWS managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_. For a
detailed listing of all AWS managed policies, see the [AWS managed
policy reference guide](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md").

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only
access to all AWS services and resources. When a service launches a new feature, AWS adds
read-only permissions for new operations and resources. For a list and descriptions of job
function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AWSTransferConsoleFullAccess

The `AWSTransferConsoleFullAccess` policy provides full access to Transfer Family
through the AWS Management Console. For more information, see
[Service-linked role for AWS Transfer Family](../../../aws-managed-policy/latest/reference/AWSTransferConsoleFullAccess.md "../../../aws-managed-policy/latest/reference/AWSTransferConsoleFullAccess.md").

## AWS managed policy: AWSTransferFullAccess

The `AWSTransferFullAccess` policy provides full access to Transfer Family services. For more information, see
[Service-linked role for AWS Transfer Family](../../../aws-managed-policy/latest/reference/AWSTransferFullAccess.md "../../../aws-managed-policy/latest/reference/AWSTransferFullAccess.md").

## AWS managed policy: AWSTransferLoggingAccess

The `AWSTransferLoggingAccess` policy grants AWS Transfer Family full access to create
log streams and groups and put log events to your account. For more information, see
[Service-linked role for AWS Transfer Family](../../../aws-managed-policy/latest/reference/AWSTransferLoggingAccess.md "../../../aws-managed-policy/latest/reference/AWSTransferLoggingAccess.md").

## AWS managed policy: AWSTransferReadOnlyAccess

The `AWSTransferReadOnlyAccess` policy provides read-only access to Transfer Family
services. For more information, see
[Service-linked role for AWS Transfer Family](../../../aws-managed-policy/latest/reference/AWSTransferReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSTransferReadOnlyAccess.md").

## AWS Transfer Family updates to AWS managed

policies

View details about updates to AWS managed policies for AWS Transfer Family since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the [Document history for AWS Transfer Family](doc-history.md "doc-history.md") page.

| Change                                                                                                                                                         | Description                                                                                        | Date               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------ |
| Documentation update                                                                                                                                           | Added sections for each of the Transfer Family managed policies.                                   | January 27, 2022   |
| [AWSTransferReadOnlyAccess](#security-iam-awsmanpol-transferreadonlyaccess "#security-iam-awsmanpol-transferreadonlyaccess") –<br>Update to an existing policy | AWS Transfer Family added new permissions to allow the policy to read<br>AWS Managed Microsoft AD. | September 30, 2021 |
| AWS Transfer Family started tracking changes                                                                                                                   | AWS Transfer Family started tracking changes for its AWS managed policies.                         | June 15, 2021      |
