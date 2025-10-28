# Amazon Kendra Identity-based

policy examples

By default, users and roles don't have permission to create or modify Amazon Kendra
resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM
administrator must create IAM policies that grant users and roles permission to perform
specific API operations on the specified resources they need. The administrator must then
attach those policies to the users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [AWS
  Managed (Predefined) Polices for Amazon Kendra](#security_iam_id-predefined-policies "#security_iam_id-predefined-policies")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Accessing one
  Amazon Kendra index](#security_iam_id-based-policy-examples-access-query-index "#security_iam_id-based-policy-examples-access-query-index")
- [Tag-based policy examples](#examples-tagging "#examples-tagging")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Amazon Kendra resources in your
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

## AWS

Managed (Predefined) Polices for Amazon Kendra

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. These policies are called AWS managed policies.
AWS managed policies make it easier for you to assign permissions to users, groups,
and roles than if you had to write the policies yourself. For more information, see
[Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

The following AWS managed policies, which you can attach to groups and roles in
your account, are specific to Amazon Kendra:

- **AmazonKendraReadOnly** — Grants read-only
  access to Amazon Kendra resources.
- **AmazonKendraFullAccess** — Grants full
  access to create, read, update, delete, tag, and run all Amazon Kendra
  resources.

For the console, your role must also have `iam:CreateRole`,
`iam:CreatePolicy`, `iam:AttachRolePolicy`, and
`s3:ListBucket` permissions.

###### Note

You can review these permissions by signing in to the IAM console and searching
for specific policies.

You can also create your own custom policies to allow permissions for
Amazon Kendra API actions. You can attach these custom policies to the IAM roles or
groups that require those permissions. For examples of IAM policies for
Amazon Kendra, see [Amazon Kendra Identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Allow users

to view their own permissions

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

## Accessing one

Amazon Kendra index

In this example, you want to grant an user in your AWS account access to query an
index.

## Tag-based policy examples

Tag-based policies are JSON policy documents that specify the actions that a
principal can perform on tagged resources.

### Example: Use a tag to access a

resource

This example policy grants a user or role in your AWS account permission to use
the `Query` operation with any resource tagged with the key
`department` and the value
`finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kendra:Query"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "finance"
 }
 }
 }
 ]
}`

```

### Example: Use a tag to activate Amazon Kendra

operations

This example policy grants a user or role in your AWS account permission to use
any Amazon Kendra operation except `TagResource` operation with any resource
tagged with the key `department` and the value
`finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kendra:*",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "kendra:TagResource"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/department": "finance"
 }
 }
 }
 ]
}`

```

### Example: Use a tag to restrict

access to an operation

This example policy restricts access for a user or role in your AWS account to
use the `CreateIndex` operation unless the user provides the
`department` tag and it has the allowed values
`finance` and `IT`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kendra:CreateIndex",
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": "kendra:CreateIndex",
 "Resource": "*",
 "Condition": {
 "Null": {
 "aws:RequestTag/department": "true"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": "kendra:CreateIndex",
 "Resource": "*",
 "Condition": {
 "ForAnyValue:StringNotEquals": {
 "aws:RequestTag/department": [
 "finance",
 "IT"
 ]
 }
 }
 }
 ]
}`

```
