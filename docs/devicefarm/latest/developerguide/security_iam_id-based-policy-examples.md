# AWS Device Farm identity-based policy examples

By default, IAM users and roles don't have permission to create or modify Device Farm resources. They also
can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM
policies that grant users and roles permission to perform specific API operations on the specified resources
they need. The administrator must then attach those policies to the IAM users or groups that require those
permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see
[Creating
Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the _IAM User Guide_.

###### Topics

- [Policy best practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Allow users to view their
  own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Accessing one Device Farm desktop
  browser testing project](#security_iam_id-based-policy-examples-access-one-project "#security_iam_id-based-policy-examples-access-one-project")
- [Viewing Device Farm desktop browser
  testing projects based on tags](#security_iam_id-based-policy-examples-view-project-tags "#security_iam_id-based-policy-examples-view-project-tags")

## Policy best practices

Identity-based policies determine whether someone can create, access, or delete Device Farm resources in your
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

## Allow users to view their

own permissions

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

## Accessing one Device Farm desktop

browser testing project

In this example, you want to grant an IAM user in your AWS account access to one of your Device Farm
destktop browser testing projects,
`arn:aws:devicefarm:us-west-2:111122223333:testgrid-project:123e4567-e89b-12d3-a456-426655441111`.
You want the account to be able to see items related to the project.

In addition to the `devicefarm:GetTestGridProject` endpoint, the account must have the
`devicefarm:ListTestGridSessions`, `devicefarm:GetTestGridSession`,
`devicefarm:ListTestGridSessionActions`, and
`devicefarm:ListTestGridSessionArtifacts` endpoints.

If you are using CI systems, you should give each CI runner unique access credentials. For example, a
CI system is unlikely to need more permissions than `devicefarm:ScheduleRun` or
`devicefarm:CreateUpload`. The following IAM policy outlines a minimal policy to allow a
CI runner to start a test of a new Device Farm native app test by creating an upload and using it to schedule
a test run:

## Viewing Device Farm desktop browser

testing projects based on tags

You can use conditions in your identity-based policy to control access to Device Farm resources based on
tags. This example shows how you might create a policy that allows the viewing of projects and sessions.
Permission is granted if the `Owner` tag of the requested resource matches the username of
the requesting account.

You can attach this policy to the IAM users in your account. If a user named
`richard-roe` attempts to view a Device Farm project or session, the project must be tagged
`Owner=richard-roe` or `owner=richard-roe`. Otherwise, the user is denied
access. The condition tag key `Owner` matches both `Owner` and `owner`
because condition key names are not case sensitive. For more information, see [IAM JSON Policy Elements:
Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
