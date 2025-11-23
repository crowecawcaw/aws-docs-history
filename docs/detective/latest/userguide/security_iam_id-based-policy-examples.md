# Amazon Detective identity-based policy

examples

By default, IAM users and roles don't have permission to create or modify Detective
resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API.

An IAM administrator must create IAM policies that grant users and roles permission
to perform specific API operations on the specified resources they need. The administrator
then attaches those policies to the IAM users or groups that require those
permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Using the Detective
  console](#security_iam_id-based-policy-examples-console "#security_iam_id-based-policy-examples-console")
- [Allowing
  users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions "#security_iam_id-based-policy-examples-view-own-permissions")
- [Administrator
  account: Managing the member accounts in a behavior graph](#security_iam_id-based-policy-examples-admin-account-mgmt "#security_iam_id-based-policy-examples-admin-account-mgmt")
- [Administrator
  account: Using a behavior graph for investigation](#security_iam_id-based-policy-examples-admin-investigate "#security_iam_id-based-policy-examples-admin-investigate")
- [Member account:
  Managing behavior graph invitations and memberships](#security_iam_id-based-policy-examples-member-account "#security_iam_id-based-policy-examples-member-account")
- [Administrator
  account: Restricting access based on tag values](#security_iam_id-based-policy-examples-graph-tags "#security_iam_id-based-policy-examples-graph-tags")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Detective resources in your
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

## Using the Detective

console

To use the Amazon Detective console, the user or role must have access to the relevant
actions, which match corresponding actions in the API.

To enable Detective and become an administrator account for a behavior graph, the user or role
must be granted permission for the `CreateGraph` action.

To use the Detective console to perform any administrator account actions, the user or role must
be granted permission for the `ListGraphs` action. This grants permission to
retrieve the behavior graphs their account is an administrator account for. They also must be granted
permission to perform specific administrator account actions.

The most basic administrator account actions are to view a list of member accounts in a
behavior graph, and to use the behavior graph for investigation.

- To view the list of member accounts in a behavior graph, the principal must be
  granted permission for the `ListMembers` action.
- To conduct investigation in a behavior graph, the principal must be granted
  permission for the `SearchGraph` action.

To use the Detective console to perform any member account actions, the user or role must
be granted permission for the `ListInvitations` action. This grants
permission to view behavior graph invitations. They can then be granted permission for
specific member account actions.

## Allowing

users to view their own permissions

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

## Administrator

account: Managing the member accounts in a behavior graph

This example policy is intended for administrator account users who are only responsible for
managing the member accounts used in the behavior graph. The policy also allows the user
to view the usage information and deactivate Detective. The policy does not grant permission
to use the behavior graph for investigation.

JSON

```
`{"Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":["detective:ListMembers","detective:CreateMembers","detective:DeleteMembers","detective:DeleteGraph","detective:Get*","detective:StartMonitoringMember"],
 "Resource":"arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
 },
 {
 "Effect":"Allow",
 "Action":["detective:CreateGraph","detective:ListGraphs"],
 "Resource":"*"
 }
 ]
}`

```

## Administrator

account: Using a behavior graph for investigation

This example policy is intended for administrator account users who use the behavior graph
for investigation only. They cannot view or edit the list of member accounts in the
behavior graph.

JSON

```
`{"Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":["detective:SearchGraph"],
 "Resource":"arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899"
 },
 {
 "Effect":"Allow",
 "Action":["detective:ListGraphs"],
 "Resource":"*"
 }
 ]
}`

```

## Member account:

Managing behavior graph invitations and memberships

This example policy is intended for users belonging to a member account. In the
example, the member account belongs to two behavior graphs. The policy grants permission
to respond to invitations and remove the member account from the behavior graph.

JSON

```
`{"Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":["detective:AcceptInvitation","detective:RejectInvitation","detective:DisassociateMembership"],
 "Resource":[
 "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899",
 "arn:aws:detective:us-east-1:444455556666:graph:056d2a9521xi2bbluw1d164680eby416"
 ]
 },
 {
 "Effect":"Allow",
 "Action":["detective:ListInvitations"],
 "Resource":"*"
 }
 ]
}`

```

## Administrator

account: Restricting access based on tag values

The following policy allows the user to use a behavior graph for investigation if the
`SecurityDomain` tag of the behavior graph matches the
`SecurityDomain` tag of the user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "detective:SearchGraph"
 ],
 "Resource": "arn:aws:detective:*:*:graph:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/SecurityDomain": "aws:PrincipalTag/SecurityDomain"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "detective:ListGraphs"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following policy prevents the users from using a behavior graph for investigation
if the value of the `SecurityDomain` tag for the behavior graph is
`Finance`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[ {
 "Effect":"Deny",
 "Action":["detective:SearchGraph"],
 "Resource":"arn:aws:detective:*:*:graph:*",
 "Condition": {
 "StringEquals": {"aws:ResourceTag/SecurityDomain": "Finance"}
 }
 } ]
}`

```
