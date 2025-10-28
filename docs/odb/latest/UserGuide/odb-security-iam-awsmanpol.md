# AWS managed policies for Oracle Database@AWS

To add permissions to permission sets and roles, it's easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(permission sets and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services don't remove permissions from an AWS managed policy, so policy updates
don't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed policy: AmazonODBServiceRolePolicy](#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy "#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy")

## AWS managed policy: AmazonODBServiceRolePolicy

You can't attach the `AmazonODBServiceRolePolicy` policy to your IAM entities.
This policy is attached to a service-linked role that allows Oracle Database@AWS to perform actions on your behalf.
For more information, see [Using service-linked roles for Oracle Database@AWS](odb-SLR.md "odb-SLR.md").

To view more details about the policy, including the latest version of the JSON policy document, see
[AmazonODBServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonODBServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonODBServiceRolePolicy.md") in the _AWS Managed Policy Reference Guide_.
