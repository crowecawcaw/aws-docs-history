# AWS Resource Groups identity-based policy examples

By default, IAM principals, such as roles and users, don't have permission to create or
modify Resource Groups resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS
API. An IAM administrator must create IAM policies that grant the principals permission
to perform specific API operations on the specified resources they need. The administrator
must then attach those policies to the principals that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best practices](#security_iam_policy-best-practices "#security_iam_policy-best-practices")
- [Using the Resource Groups console and API](#security_iam_policy-examples-console "#security_iam_policy-examples-console")
- [Allow users to view their own permissions](#security_iam_policy-examples-own-permissions "#security_iam_policy-examples-own-permissions")
- [Viewing groups based on tags](#security_iam_policy-examples-view-tags "#security_iam_policy-examples-view-tags")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete Resource Groups resources in your
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

## Using the Resource Groups console and API

To access the AWS Resource Groups and Tag Editor console and API, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the Resource Groups
resources in your AWS account. If you create an identity-based policy that is more
restrictive than the minimum required permissions, the console and API commands won't
function as intended for principals (IAM roles or users) with that policy.

To ensure that those entities can still use Resource Groups, attach the following policy (or a
policy that contains the permissions listed in the following policy) to the entities.
For more information, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "resource-groups:*",
 "cloudformation:DescribeStacks",
 "cloudformation:ListStackResources",
 "tag:GetResources",
 "tag:TagResources",
 "tag:UntagResources",
 "tag:getTagKeys",
 "tag:getTagValues",
 "resource-explorer:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about granting access to Resource Groups, see [Granting permissions for using AWS Resource Groups and Tag Editor](gettingstarted-prereqs-permissions-howto.md "gettingstarted-prereqs-permissions-howto.md") in this guide.

## Allow users to view their own permissions

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

## Viewing groups based on tags

You can use conditions in your identity-based policy to control access to Resource Groups
resources based on tags. This example shows how you might create a policy that allows
viewing a resource, in this example, a resource group. However, permission is granted
only if the group tag `project` has the same value as the
`project` tag attached to the calling principal.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "resource-groups:GetGroup",
 "Resource": "arn:aws:resource-groups:`us-east-1`:`111122223333`:`group`/`group_name`",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/project": "${aws:PrincipalTag/project}"}
 }
 }
 ]
}`

```

You can attach this policy to the principals in your account. If a principal with the
tag key `project` and tag value `alpha` attempts to view a
resource group, the group must also be tagged `project=alpha`. Otherwise the
user is denied access. The condition tag key `project` matches both
`Project` and `project` because condition key names are not
case-sensitive. For more information, see [IAM JSON Policy
Elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
