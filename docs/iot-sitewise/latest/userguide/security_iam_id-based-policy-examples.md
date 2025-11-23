# AWS IoT SiteWise identity-based policy

examples

By default, entities (users and roles) don't have permission to create or modify AWS IoT SiteWise
resources. They also can't perform tasks using the AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS
API. To adjust permissions, an AWS Identity and Access Management (IAM) administrator must do the following:

1. Create IAM policies that grant users and roles permission to perform specific API
   operations on resources they need.
2. Attach those policies to the users or groups that require those permissions.
   To learn how to create an IAM identity-based policy using these example JSON policy
   documents, see [Creating policies on the JSON tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
   _IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Use the AWS IoT SiteWise
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Allow users to ingest data to assets in one hierarchy](#security_iam_id-based-policy-examples-ingest-to-one-asset-hierarchy "#security_iam_id-based-policy-examples-ingest-to-one-asset-hierarchy")
- [View AWS IoT SiteWise assets
  based on tags](#security_iam_id-based-policy-examples-view-asset-tags "#security_iam_id-based-policy-examples-view-asset-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS IoT SiteWise resources in your
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

## Use the AWS IoT SiteWise

console

To access the AWS IoT SiteWise console, you need a basic set of permissions. These
permissions let you see and manage details about the AWS IoT SiteWise resources in your
AWS account.

If you make a policy that's too restrictive, the console might not work as expected
for users or roles (entities) with that policy. To ensure that those entities can still
use the AWS IoT SiteWise console, attach the [AWSIoTSiteWiseConsoleFullAccess](https://console.aws.amazon.com/iam/home#/policies/policies/arn:aws:iam::aws:policy/AWSIoTSiteWiseConsoleFullAccess "https://console.aws.amazon.com/iam/home#/policies/policies/arn:aws:iam::aws:policy/AWSIoTSiteWiseConsoleFullAccess") managed policy to them or define equivalent
permissions for those entities. For more information, see [Adding permissions to a user](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

If entities are only using the AWS Command Line Interface (CLI) or the AWS IoT SiteWise API, and not the console,
they don't need these minimum permissions. In that case, just give them access to the
specific actions they need for their API tasks.

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

## Allow users to ingest data to assets in one hierarchy

In this example, you want to grant a user in your AWS account access to write data
to all asset properties in a specific hierarchy of assets, starting from the root asset
`a1b2c3d4-5678-90ab-cdef-22222EXAMPLE`. The policy grants the
`iotsitewise:BatchPutAssetPropertyValue` permission to the user. This policy
uses the `iotsitewise:assetHierarchyPath` condition key to restrict access to
assets whose hierarchy path matches the asset or its descendants.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PutAssetPropertyValuesForHierarchy",
 "Effect": "Allow",
 "Action": "iotsitewise:BatchPutAssetPropertyValue",
 "Resource": "arn:aws:iotsitewise:*:*:asset/*",
 "Condition": {
 "StringLike": {
 "iotsitewise:assetHierarchyPath": [
 "/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
 "/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE/*"
 ]
 }
 }
 }
 ]
}`

```

## View AWS IoT SiteWise assets

based on tags

Use conditions in your identity-based policy to control access to AWS IoT SiteWise resources
based on tags. This example shows how to create a policy that allows asset viewing.
However, permission is granted only if the asset tag `Owner` has the value of
that user's user name. This policy also grants permission to complete this action on the
console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ListAllAssets",
 "Effect": "Allow",
 "Action": [
 "iotsitewise:ListAssets",
 "iotsitewise:ListAssociatedAssets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DescribeAssetIfOwner",
 "Effect": "Allow",
 "Action": "iotsitewise:DescribeAsset",
 "Resource": "arn:aws:iotsitewise:*:*:asset/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Owner": "${aws:username}"
 }
 }
 }
 ]
}`

```

Attach this policy to the users in your account. If a user named
`richard-roe` attempts to view an AWS IoT SiteWise asset, the asset must be tagged
`Owner=richard-roe` or `owner=richard-roe`. Otherwise, Richard is
denied access. The condition tag key names are not case-sensitive. So, `Owner`
matches both `Owner` and `owner`. For more information, see [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
