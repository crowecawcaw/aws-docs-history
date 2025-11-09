AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# AWS Systems Manager

identity-based policy examples

By default, AWS Identity and Access Management (IAM) entities (users and roles) don't have permission to
create or modify AWS Systems Manager resources. They also can't perform tasks using the Systems Manager
console, AWS Command Line Interface (AWS CLI), or AWS API. An administrator must create IAM
policies that grant users and roles permission to perform specific API operations on
the specified resources they need. The administrator must then attach those policies
to the users or groups that require those permissions.

The following is an example of a permissions policy that allows a user to delete
documents with names that begin with `MyDocument-` in the
US East (Ohio) (us-east-2) AWS Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "ssm:DeleteDocument"
 ],
 "Resource" : [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/MyDocument-*"
 ]
 }
 ]
}`

```

To learn how to create an IAM identity-based policy using these example JSON
Policy documents, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy
  best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Example:
  Permission to using the Systems Manager console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Example: Permission to allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Example: Permission to read and describe individual parameters](#security_iam_id-based-policy-examples-view-one-parameter "#security_iam_id-based-policy-examples-view-one-parameter")
- [Cross-service
  confused deputy prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md")
- [Customer managed policy
  examples](#customer-managed-policies "#customer-managed-policies")
- [Viewing Systems Manager documents based on tags](#security_iam_id-based-policy-examples-view-documents-tags "#security_iam_id-based-policy-examples-view-documents-tags")

## Policy

best practices

Identity-based policies determine whether someone can create, access, or delete Systems Manager resources in your
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

## Example:

Permission to using the Systems Manager console

To access the Systems Manager console, you must have a minimum set of permissions. These
permissions must allow you to list and view details about the Systems Manager
resources and other resources in your AWS account.

If you create an identity-based policy that is more restrictive than the
minimum required permissions, the console won't function as intended for IAM
entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, allow access to only the
actions that match the API operation that you're trying to perform.

To ensure that users and roles can still use the Systems Manager console, also attach
the [AmazonSSMFullAccess](../../../aws-managed-policy/latest/reference/AmazonSSMFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMFullAccess.md") or [AmazonSSMReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonSSMReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonSSMReadOnlyAccess.md") AWS managed policy to the entities. For
more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

## Example: Permission to allow users to view their own permissions

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user
identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Example: Permission to read and describe individual parameters

###### Example Read and describe one parameter

You can grant access to a parameter by attaching the following policy to
an identity.

JSON

```
`{
"Version":"2012-10-17",
"Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameter",
 "ssm:DescribeParameters"
 ],
 "Resource": "arn:aws:ssm:`us-east-1`:`111122223333`:parameter/`parameter-name`"
 }
]
}`

```

## Customer managed policy

examples

You can create standalone policies that you administer in your own
AWS account. We refer to these as _customer managed
policies_. You can attach these policies to multiple principal
entities in your AWS account. When you attach a policy to a principal entity,
you give the entity the permissions that are defined in the policy. For more
information, see [Customer managed policy examples](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") in the _[IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md")_.

The following examples of user policies grant permissions for various Systems Manager
actions. Use them to limit the Systems Manager access for your IAM entities
(users and roles). These policies work when performing actions in the
Systems Manager API, AWS SDKs, or the AWS CLI. For users who use the console,
you need to grant additional permissions specific to the console. For more
information, see [Example:
Permission to using the Systems Manager console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console").

###### Note

All examples use the US West (Oregon) Region (us-west-2) and contain fictitious
account IDs. The account ID shouldn't be specified in the Amazon Resource
Name (ARN) for AWS public documents (documents that begin with
`AWS-*`).

**Examples**

- [Example 1: Allow a user
  to perform Systems Manager operations in a single Region](#identity-based-policies-example-1 "#identity-based-policies-example-1")
- [Example 2: Allow a user
  to list documents for a single Region](#identity-based-policies-example-2 "#identity-based-policies-example-2")

### Example 1: Allow a user

to perform Systems Manager operations in a single Region

The following example grants permissions to perform Systems Manager
operations only in the US East (Ohio) Region
(us-east-2).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:*"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:*"
 ]
 }
 ]
}`

```

### Example 2: Allow a user

to list documents for a single Region

The following example grants permissions to list all document names that
begin with `Update` in the
US East (Ohio) Region (us-east-2).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:ListDocuments"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:document/Update*"
 ]
 }
 ]
}`

```

### Example 3: Allow a user

to use a specific SSM document to run commands on specific
nodes

The following example IAM policy allows a user to do the following in
the US East (Ohio) Region (us-east-2):

- List Systems Manager documents (SSM documents) and document
  versions.
- View details about documents.
- Send a command using the document specified in the policy. The
  name of the document is determined by the following entry.

```
arn:aws:ssm:us-east-2:`aws-account-ID`:document/`Systems-Manager-document-name`
```

- Send a command to three nodes. The nodes are determined by the
  following entries in the second `Resource`
  section.

```
"arn:aws:ec2:us-east-2:`aws-account-ID`:instance/i-02573cafcfEXAMPLE",
"arn:aws:ec2:us-east-2:`aws-account-ID`:instance/i-0471e04240EXAMPLE",
"arn:aws:ec2:us-east-2:`aws-account-ID`:instance/i-07782c72faEXAMPLE"
```

- View details about a command after it has been sent.
- Start and stop workflows in Automation, a tool in
  AWS Systems Manager.
- Get information about Automation workflows.

If you want to give a user permission to use this document to send
commands on any node for which the user has access, you could specify an
entry similar to the following in the `Resource` section and
remove the other node entries. The following example uses the
US East (Ohio) Region (us-east-2).

```
"arn:aws:ec2:us-east-2:*:instance/*"
```

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "ssm:ListDocuments",
 "ssm:ListDocumentVersions",
 "ssm:DescribeDocument",
 "ssm:GetDocument",
 "ssm:DescribeInstanceInformation",
 "ssm:DescribeDocumentParameters",
 "ssm:DescribeInstanceProperties"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "ssm:SendCommand",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/i-02573cafcfEXAMPLE",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/i-0471e04240EXAMPLE",
 "arn:aws:ec2:`us-east-1`:`111122223333`:instance/i-07782c72faEXAMPLE",

 "arn:aws:ssm:`us-east-1`:`111122223333`:document/`Systems-Manager-document-name`"
 ]
 },
 {
 "Action": [
 "ssm:CancelCommand",
 "ssm:ListCommands",
 "ssm:ListCommandInvocations"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "ec2:DescribeInstanceStatus",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": "ssm:StartAutomationExecution",
 "Effect": "Allow",
 "Resource": [
 "arn:aws:ssm:`us-east-1`:`111122223333`:automation-definition/*"
 ]
 },
 {
 "Action": "ssm:DescribeAutomationExecutions",
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 },
 {
 "Action": [
 "ssm:StopAutomationExecution",
 "ssm:GetAutomationExecution"
 ],
 "Effect": "Allow",
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## Viewing Systems Manager documents based on tags

You can use conditions in your identity-based policy to control access to
Systems Manager resources based on tags. This example shows how you might
create a policy that allows viewing an SSM document. However, permission is
granted only if the document tag `Owner` has the value of that user's
user name. This policy also grants the permissions necessary to complete this
action on the console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListDocumentsInConsole",
 "Effect": "Allow",
 "Action": "ssm:ListDocuments",
 "Resource": "*"
 },
 {
 "Sid": "ViewDocumentIfOwner",
 "Effect": "Allow",
 "Action": "ssm:GetDocument",
 "Resource": "arn:aws:ssm:*:*:document/*",
 "Condition": {
 "StringEquals": {"ssm:ResourceTag/Owner": "${aws:username}"}
 }
 }
 ]
}`

```

You can attach this policy to the users in your account. If a user named
`richard-roe` attempts to view an Systems Manager document, the
document must be tagged `Owner=richard-roe` or
`owner=richard-roe`. Otherwise they're denied access. The
condition tag key `Owner` matches both `Owner` and
`owner` because condition key names aren't case-sensitive. For
more information, see [IAM
JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
