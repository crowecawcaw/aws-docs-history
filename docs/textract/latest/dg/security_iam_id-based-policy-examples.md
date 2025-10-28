# Amazon Textract Identity-Based

Policy Examples

By default, users and roles don't have permission to create or modify
Amazon Textract resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator then grants a user access to a role via temporary security credentials.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy Best
  Practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow Users
  to View Their Own Permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Giving Access
  to Synchronous Operations in Amazon Textract](#security_iam_sync-actions "#security_iam_sync-actions")
- [Giving Access to
  Asynchronous Operations in Amazon Textract](#security_iam_async-actions "#security_iam_async-actions")
- [Giving access to specific adapters in
  inference operations in Amazon Textract](#security_iam_adapter-inference "#security_iam_adapter-inference")
- [Disallow user to use adapters in
  inference operations](#security_iam_disallow-inference "#security_iam_disallow-inference")
- [Allow user to only use a specific group of
  adapters in inference operations, or no adapters](#security_iam_adapter-groups "#security_iam_adapter-groups")

## Policy Best

Practices

Identity-based policies determine whether someone can create, access, or delete Amazon Textract resources in your
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

## Allow Users

to View Their Own Permissions

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

## Giving Access

to Synchronous Operations in Amazon Textract

This example policy grants access to the synchronous actions in Amazon Textract to
an IAM user in your AWS account.

```
"Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "textract:DetectDocumentText",
                "textract:AnalyzeDocument"
            ],
            "Resource": "*"
        }
    ]

```

## Giving Access to

Asynchronous Operations in Amazon Textract

The following example policy gives an IAM user on your AWS account access to all
asynchronous operations used in Amazon Textract.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "textract:StartDocumentTextDetection",
 "textract:StartDocumentAnalysis",
 "textract:GetDocumentTextDetection",
 "textract:GetDocumentAnalysis"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Giving access to specific adapters in

inference operations in Amazon Textract

Although you can use `*` to access all resources in inference operations,
you can control a user's access to specific adapters.

## Disallow user to use adapters in

inference operations

## Allow user to only use a specific group of

adapters in inference operations, or no adapters

Tag the specific adapters that you want to control by using the
`TagResource` operation. The following example controls access to adapters
tagged with `{"env":"prod"}`.

### Allow user to manage adapter and

versions

### Permissions needed for

CreateAdapterVersion

In addition to `"textract:CreateAdapterVersion"` permission, the caller
identity also needs Amazon S3 and AWS Key Management Service (AWS KMS) permission to your training data in
Amazon S3 and the KMS key used to encrypt your data.
