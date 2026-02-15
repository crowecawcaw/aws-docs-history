#

Identity-based policy examples for Amazon Translate

By default, users and roles don't have permission to create or modify
Amazon Translate resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant
permission to perform specific API operations on the specific resources that they need.
The administrator must then attach those policies to the users or roles that
require those permissions.

To learn how to create an IAM identity-based policy using the following example JSON
policy documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Identity-based
  policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow access to the
  Amazon Translate console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Specify resources in a policy](#iam_id-policy-examples-resource-permissions "#iam_id-policy-examples-resource-permissions")
- [Permissions
  for using customer managed keys with custom terminologies](#kms-permissions "#kms-permissions")

## Identity-based

policy best practices

Identity-based policies determine whether someone can create, access, or delete Amazon Translate resources in your
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
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
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

## Allow access to the

Amazon Translate console

To access the Amazon Translate console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
Amazon Translate resources in your AWS account. If you create an identity-based
policy that is more restrictive than the minimum required permissions, the console
won't function as intended for entities (users, groups or roles) with that
policy.

For Amazon Translate console permissions, you can attach the
`TranslateFullAccess` AWS managed policy to
the entities. For more information, see [AWS managed policies for Amazon Translate](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You also need permissions for the actions shown in the following policy.
These permissions are included in the `TranslateFullAccess` policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "iam:GetRole",
 "s3:ListAllMyBuckets",
 "s3:ListBucket",
 "s3:GetBucketLocation"
 ],
 "Resource": "*"

 }
 ]
}`

```

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that they're trying to perform. For more information,
see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

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

## Specify resources in a policy

For many Amazon Translate API actions, you can restrict the scope of a policy by specifying
resources that are allowed (or not allowed) for the action. For a list of the actions
that can specify resources, see [Actions Defined by Amazon Translate](../../../IAM/latest/UserGuide/list_amazontranslate.md#amazontranslate-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazontranslate.md#amazontranslate-actions-as-permissions"). You can specify the following
resources in a policy:

- **Custom terminology** – Use the following ARN format:

`arn:`partition`:translate:`region`:`account`:terminology/`terminology-name`/LATEST`

- **Parallel data** – Use the following ARN format:

`arn:`partition`:translate:`region`:`account`:parallel-data/`parallel-data-name``

You can use the wildcard character to specify multiple resources in the policy. The
following example policy allows all custom terminology resources for all Amazon Translate actions.

###### Example

```
{
        "Sid": "Example1",
        "Effect": "Allow",
        "Action": "translate:*",
        "Resource": [
             "arn:aws:translate:us-west-2:123456789012:terminology/*"
        ]
}
```

The following example policy denies access to a specific parallel data resource for the **GetParallelData** action.

###### Example

```
{
        "Sid": "Example2",
        "Effect": "Deny",
        "Action": "translate:GetParallelData",
        "Resource": [
             "arn:aws:translate:us-west-2:123456789012:parallel-data/test-parallel-data"
        ]
}
```

## Permissions

for using customer managed keys with custom terminologies

If you use AWS Key Management Service (AWS KMS) customer managed keys with Amazon Translate custom terminologies, you might
need additional permissions in your KMS key policy.

To call the `ImportTerminology` operation with a customer managed key, add
the following permissions to your existing KMS key policy.

JSON

```
`{
 "Id": "key-consolepolicy-3",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access for use with Amazon Translate",
 "Effect": "Allow",
 "Principal": {
 "AWS": "IAM USER OR ROLE ARN"
 },
 "Action": [
 "kms:CreateAlias",
 "kms:CreateGrant",
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:GetKeyPolicy",
 "kms:PutKeyPolicy",
 "kms:RetireGrant"
 ],
 "Resource": "*"
 }
 ]
}`

```

To call the `GetTerminology` operation for a custom terminology that
was imported with a KMS customer managed key, add the following permissions in the KMS key
policy.

JSON

```
`{
 "Id": "key-consolepolicy-3",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access for use with Amazon Translate",
 "Effect": "Allow",
 "Principal": {
 "AWS": "IAM USER OR ROLE ARN"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GetKeyPolicy",
 "kms:PutKeyPolicy"
 ],
 "Resource": "*"
 }
 ]
}`

```

To call the `ListTerminologies` or `DeleteTermionlogy`
operations for a custom terminology that was imported with a customer managed key, you don't
need to have any special AWS KMS permissions.

To use customer managed keys with all custom terminologies operations, add the following
permissions in the KMS key policy.

JSON

```
`{
 "Id": "key-consolepolicy-3",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access for use with Amazon Translate",
 "Effect": "Allow",
 "Principal": {
 "AWS": "IAM USER OR ROLE ARN"
 },
 "Action": [
 "kms:CreateGrant",
 "kms:Decrypt",
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:GetKeyPolicy",
 "kms:PutKeyPolicy",
 "kms:RetireGrant"
 ],
 "Resource": "*"
 }
 ]
}`

```

For details about the Amazon Translate operations and resources, see
[Actions, resources, and condition keys for Amazon Translate](../../../service-authorization/latest/reference/list_amazontranslate.md "../../../service-authorization/latest/reference/list_amazontranslate.md") in the _Service Authorization Reference_.
