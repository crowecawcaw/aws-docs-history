

# AWS managed policies for AWS Transfer Family
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create AWS Identity and Access Management (IAM) customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions that they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*. For a detailed listing of all AWS managed policies, see the [AWS managed policy reference guide](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html).

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the `ReadOnlyAccess` AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSTransferConsoleFullAccess
<a name="security-iam-awsmanpol-transferconsolefullaccess"></a>

The `AWSTransferConsoleFullAccess` policy provides full access to Transfer Family through the AWS Management Console. For more information, see [Service-linked role for AWS Transfer Family](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSTransferConsoleFullAccess.html).

## AWS managed policy: AWSTransferFullAccess
<a name="security-iam-awsmanpol-transferfullaccess"></a>

 The `AWSTransferFullAccess` policy provides full access to Transfer Family services. For more information, see [Service-linked role for AWS Transfer Family](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSTransferFullAccess.html).

## AWS managed policy: AWSTransferLoggingAccess
<a name="security-iam-awsmanpol-transferloggingaccess"></a>

 The `AWSTransferLoggingAccess` policy grants AWS Transfer Family full access to create log streams and groups and put log events to your account. For more information, see [Service-linked role for AWS Transfer Family](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSTransferLoggingAccess.html).

## AWS managed policy: AWSTransferReadOnlyAccess
<a name="security-iam-awsmanpol-transferreadonlyaccess"></a>

 The `AWSTransferReadOnlyAccess` policy provides read-only access to Transfer Family services. For more information, see [Service-linked role for AWS Transfer Family](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSTransferReadOnlyAccess.html).

## AWS managed policy: AWSTransferServiceRolePolicy
<a name="security-iam-awsmanpol-transferservicerolepolicy"></a>

The `AWSTransferServiceRolePolicy` policy is attached to the AWSServiceRoleForTransfer service-linked role and allows Transfer Family to integrate with other AWS services on your behalf. You can't attach this policy to your own IAM entities. For more information, see [Using service-linked roles for AWS Transfer Family](using-service-linked-roles.md).

**Permissions details**

This policy allows Transfer Family to complete the following actions in AWS Secrets Manager:
+ Retrieve SFTP host key material from Transfer Family managed secrets to serve to incoming connections.
+ List and batch retrieve secrets in the same AWS account to discover the host key secrets that Transfer Family manages.
+ Delete orphaned Transfer Family managed secrets that are no longer associated with a Transfer Family host key resource.

For more information, see [AWSTransferServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSTransferServiceRolePolicy.html).

## AWS Transfer Family updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Transfer Family since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history for AWS Transfer Family](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
|  [AWSTransferServiceRolePolicy](#security-iam-awsmanpol-transferservicerolepolicy) – New policy  | AWS Transfer Family added the `AWSTransferServiceRolePolicy` managed policy, attached to the AWSServiceRoleForTransfer service-linked role, to support storing SFTP host keys in AWS Secrets Manager. | October 6, 2026 | 
|  Documentation update  | Added sections for each of the Transfer Family managed policies. | January 27, 2022 | 
|  [AWSTransferReadOnlyAccess](#security-iam-awsmanpol-transferreadonlyaccess) – Update to an existing policy  | AWS Transfer Family added new permissions to allow the policy to read AWS Managed Microsoft AD. | September 30, 2021 | 
| AWS Transfer Family started tracking changes | AWS Transfer Family started tracking changes for its AWS managed policies. | June 15, 2021 | 