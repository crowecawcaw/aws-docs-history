# AWS Well-Architected Tool identity-based

policy examples

By default, users and roles don't have permission to create or modify
AWS WA Tool resources. They also can't perform tasks using the
AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies
that grant users and roles permission to perform specific API operations on the specified
resources they need. The administrator must then attach those policies to the users
or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the
  AWS WA Tool console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allow users
  to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Granting full
  access to workloads](#security_iam_id-based-policy-examples-full-access "#security_iam_id-based-policy-examples-full-access")
- [Granting
  read-only access to workloads](#security_iam_id-based-policy-examples-readonly-access "#security_iam_id-based-policy-examples-readonly-access")
- [Accessing
  one workload](#security_iam_id-based-policy-examples-access-one-workload "#security_iam_id-based-policy-examples-access-one-workload")
- [Using a service-specific condition key for the AWS Well-Architected Tool Connector for Jira](#security_iam_id-based-policy-examples-service-specific-condition-key "#security_iam_id-based-policy-examples-service-specific-condition-key")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete AWS WA Tool resources in your
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

## Using the

AWS WA Tool console

To access the AWS Well-Architected Tool console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
AWS WA Tool resources in your AWS account. If you create an identity-based policy
that is more restrictive than the minimum required permissions, the console won't
function as intended for entities (users or roles) with that policy.

To ensure that those entities can still use the AWS WA Tool console, also attach
the following AWS managed policy to the entities:

```
WellArchitectedConsoleReadOnlyAccess
```

To allow the ability to create, change, and delete workloads, attach the following
AWS managed policy to the entities:

```
WellArchitectedConsoleFullAccess
```

For more information, see [Adding Permissions to a User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the
_IAM User Guide_.

You don't need to allow minimum console permissions for users that are making calls
only to the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that you're trying to perform.

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

## Granting full

access to workloads

In this example, you want to grant a user in your AWS account full access to
your workloads. Full access allows the user to perform all actions in AWS WA Tool. This
access is required to define workloads, delete workloads, view workloads, and update
workloads.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "wellarchitected:*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Granting

read-only access to workloads

In this example, you want to grant a user in your AWS account read-only
access to your workloads. Read-only access only allows the user to view workloads in
AWS WA Tool.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "wellarchitected:Get*",
 "wellarchitected:List*"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Accessing

one workload

In this example, you want to grant a user in your AWS account read-only
access to one of your workloads, `99999999999955555555555566666666`, in
the `us-west-2` Region. Your account ID is
`777788889999`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Effect" : "Allow",
 "Action" : [
 "wellarchitected:Get*",
 "wellarchitected:List*"
 ],
 "Resource": "arn:aws:wellarchitected:us-west-2:777788889999:workload/999999999999555555555555666666666"
 }
 ]
}`

```

## Using a service-specific condition key for the AWS Well-Architected Tool Connector for Jira

This example demonstrates how to use the service-specific condition key `wellarchitected:JiraProjectKey` to control which Jira projects can be linked to workloads in your account.

The following describes relevant uses for the condition key:

- **`CreateWorkload:`** When you apply `wellarchitected:JiraProjectKey` to `CreateWorkload`, you can define which custom Jira projects can be linked to any workload created by the user. For example, if a user tries to create a new workload with project ABC, but the policy only specifies project PQR, the action is denied.
- **`UpdateWorkload:`** When you apply `wellarchitected:JiraProjectKey` to `UpdateWorkload`, you can define which custom Jira projects can be linked to this particular workload or any workload. For example, if a user tries to update an existing workload with project ABC, but the policy specifies project PQR, the action is denied. Additionally, if the user has a workload that is linked to project PQR and tries to update the workload to be linked to project ABC, the action is denied.
- **`UpdateGlobalSettings:`** When you apply `wellarchitected:JiraProjectKey` to `UpdateGlobalSettings`, you can define which custom Jira projects can be linked to the AWS account. The account-level setting protects workloads in your account that do not override account-level Jira settings. For example, if a user has access to `UpdateGlobalSettings`, they cannot link workloads in your account to any projects that are not specified in the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "wellarchitected:UpdateGlobalSettings",
 "wellarchitected:CreateWorkload"
 ],
 "Resource": "*",
 "Condition": {
 "StringEqualsIfExists": {
 "wellarchitected:JiraProjectKey": ["ABC, PQR"]
 }
 }
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "wellarchitected:UpdateWorkload"
 ],
 "Resource": "arn:aws:wellarchitected:`us-east-1`:`111122223333`:`workload/example-workload`",
 "Condition": {
 "StringEqualsIfExists": {
 "wellarchitected:JiraProjectKey": ["ABC, PQR"]
 }
 }
 }
 ]
}`

```
