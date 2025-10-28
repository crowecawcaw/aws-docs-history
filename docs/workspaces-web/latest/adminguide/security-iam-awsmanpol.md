# AWS managed policies for WorkSpaces Secure Browser

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services may occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services don't remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the `ReadOnlyAccess` AWS managed policy
provides read-only access to all AWS services and resources. When a service launches a new
feature, AWS adds read-only permissions for new operations and resources. For a list and
descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

###### Topics

- [AWS managed
  policy: AmazonWorkSpacesWebServiceRolePolicy](security-iam-awsmanpol-AmazonWorkSpacesWebServiceRolePolicy.md "security-iam-awsmanpol-AmazonWorkSpacesWebServiceRolePolicy.md")
- [AWS managed policy:
  AmazonWorkSpacesSecureBrowserReadOnly](security-iam-awsmanpol-AmazonWorkSpacesSecureBrowserReadOnly.md "security-iam-awsmanpol-AmazonWorkSpacesSecureBrowserReadOnly.md")
- [AWS managed policy:
  AmazonWorkSpacesWebReadOnly](security-iam-awsmanpol-AmazonWorkSpacesWebReadOnly.md "security-iam-awsmanpol-AmazonWorkSpacesWebReadOnly.md")
- [WorkSpaces Secure Browser updates to AWS managed
  policies](security-iam-awsmanpol-updates.md "security-iam-awsmanpol-updates.md")
