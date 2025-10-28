# Example policies for

administering IAM resources

Following are examples of IAM policies that allow users to perform tasks associated with
managing IAM users, groups, and credentials. This includes policies that permit users manage
their own passwords, access keys, and multi-factor authentication (MFA) devices.

For examples of policies that let users perform tasks with other AWS services, like Amazon S3,
Amazon EC2, and DynamoDB, see [Example IAM identity-based policies](access_policies_examples.md "access_policies_examples.md").

###### Topics

- [Allow a user to list the account's groups,
  users, policies, and more for reporting purposes](#iampolicy-example-userlistall "#iampolicy-example-userlistall")
- [Allow a user to manage a group's
  membership](#iampolicy-example-usermanagegroups "#iampolicy-example-usermanagegroups")
- [Allow a user to manage IAM users](#creds-policies-users "#creds-policies-users")
- [Allow users to set account password
  policy](#creds-policies-set-password-policy "#creds-policies-set-password-policy")
- [Allow users to generate and retrieve
  IAM credential reports](#iampolicy-generate-credential-report "#iampolicy-generate-credential-report")
- [Allow all IAM actions (admin access)](#creds-policies-all-iam "#creds-policies-all-iam")

## Allow a user to list the account's groups,

users, policies, and more for reporting purposes

The following policy allows the user to call any IAM action that starts with the
string `Get` or `List`, and to generate reports. To view the example
policy, see [IAM: Allows read-only
access to the IAM console](reference_policies_examples_iam_read-only-console.md "reference_policies_examples_iam_read-only-console.md").

## Allow a user to manage a group's

membership

The following policy allows the user to update the membership of the group called
_MarketingGroup_. To view the example policy, see [IAM: Allows managing a
group's membership programmatically and in the console](reference_policies_examples_iam_manage-group-membership.md "reference_policies_examples_iam_manage-group-membership.md").

## Allow a user to manage IAM users

The following policy allows a user to perform all the tasks associated with managing IAM
users but not to perform actions on other entities, such as creating groups or policies.
Allowed actions include these:

- Creating the user (the [`CreateUser`](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md") action).
- Deleting the user. This task requires permissions to perform all of the following
  actions: [`DeleteSigningCertificate`](../APIReference/API_DeleteSigningCertificate.md "../APIReference/API_DeleteSigningCertificate.md"), [`DeleteLoginProfile`](../APIReference/API_DeleteLoginProfile.md "../APIReference/API_DeleteLoginProfile.md"),
  [`RemoveUserFromGroup`](../APIReference/API_RemoveUserFromGroup.md "../APIReference/API_RemoveUserFromGroup.md"), and [`DeleteUser`](../APIReference/API_DeleteUser.md "../APIReference/API_DeleteUser.md").
- Listing users in the account and in groups (the [`GetUser`](../APIReference/API_GetUser.md "../APIReference/API_GetUser.md"), [`ListUsers`](../APIReference/API_ListUsers.md "../APIReference/API_ListUsers.md") and [`ListGroupsForUser`](../APIReference/API_ListGroupsForUser.md "../APIReference/API_ListGroupsForUser.md")
  actions).
- Listing and removing policies for the user (the [`ListUserPolicies`](../APIReference/API_ListUserPolicies.md "../APIReference/API_ListUserPolicies.md"),
  [`ListAttachedUserPolicies`](../APIReference/API_ListAttachedUserPolicies.md "../APIReference/API_ListAttachedUserPolicies.md"), [`DetachUserPolicy`](../APIReference/API_DetachUserPolicy.md "../APIReference/API_DetachUserPolicy.md"),
  [`DeleteUserPolicy`](../APIReference/API_DeleteUserPolicy.md "../APIReference/API_DeleteUserPolicy.md") actions)
- Renaming or changing the path for the user (the [`UpdateUser`](../APIReference/API_UpdateUser.md "../APIReference/API_UpdateUser.md") action). The
  `Resource` element must include an ARN that covers both the source path and
  the target path. For more information on paths, see [Friendly names and paths](reference_identifiers.md#identifiers-friendly-names "reference_identifiers.md#identifiers-friendly-names").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowUsersToPerformUserActions",
 "Effect": "Allow",
 "Action": [
 "iam:ListPolicies",
 "iam:GetPolicy",
 "iam:UpdateUser",
 "iam:AttachUserPolicy",
 "iam:ListEntitiesForPolicy",
 "iam:DeleteUserPolicy",
 "iam:DeleteUser",
 "iam:ListUserPolicies",
 "iam:CreateUser",
 "iam:RemoveUserFromGroup",
 "iam:AddUserToGroup",
 "iam:GetUserPolicy",
 "iam:ListGroupsForUser",
 "iam:PutUserPolicy",
 "iam:ListAttachedUserPolicies",
 "iam:ListUsers",
 "iam:GetUser",
 "iam:DetachUserPolicy"
 ],
 "Resource": "*"
 },
 {
 "Sid": "AllowUsersToSeeStatsOnIAMConsoleDashboard",
 "Effect": "Allow",
 "Action": [
 "iam:GetAccount*",
 "iam:ListAccount*"
 ],
 "Resource": "*"
 }
 ]
}`

```

A number of the permissions included in the preceding policy allow the user to perform
tasks in the AWS Management Console. Users who perform user-related tasks from the [AWS CLI](http://aws.amazon.com/cli/ "http://aws.amazon.com/cli/"), the [AWS SDKs](http://aws.amazon.com/tools/ "http://aws.amazon.com/tools/"), or the IAM HTTP query API only might not need certain permissions.
For example, if users already know the ARN of policies to detach from a user, they do not need
the `iam:ListAttachedUserPolicies` permission. The exact list of permissions that a
user requires depends on the tasks that the user must perform while managing other users.

The following permissions in the policy allow access to user tasks via the
AWS Management Console:

- `iam:GetAccount*`
- `iam:ListAccount*`

## Allow users to set account password

policy

You might give some users permissions to get and update the [password policy](id_credentials_passwords_account-policy.md "id_credentials_passwords_account-policy.md") of your
AWS account. To view the example policy, see [IAM: Allows setting the
account password requirements programmatically and in the console](reference_policies_examples_iam_set-account-pass-policy.md "reference_policies_examples_iam_set-account-pass-policy.md").

## Allow users to generate and retrieve

IAM credential reports

You can give users permission to generate and download a report that lists all users in
your AWS account. The report also lists the status of various user credentials, including
passwords, access keys, MFA devices, and signing certificates. For more information about
credential reports, see [Generate credential reports for your
AWS account](id_credentials_getting-report.md "id_credentials_getting-report.md"). To view the example policy, see [IAM: Generate and retrieve
IAM credential reports](reference_policies_examples_iam-credential-report.md "reference_policies_examples_iam-credential-report.md").

## Allow all IAM actions (admin access)

You might give some users administrative permissions to perform all actions in IAM,
including managing passwords, access keys, MFA devices, and user certificates. The following
example policy grants these permissions.

###### Warning

When you give a user full access to IAM, there is no limit to the permissions that
user can grant to him/herself or others. The user can create new IAM entities (users or
roles) and grant those entities full access to all resources in your AWS account. When you
give a user full access to IAM, you are effectively giving them full access to all
resources in your AWS account. This includes access to delete all resources. You should
grant these permissions to only trusted administrators, and you should enforce multi-factor
authentication (MFA) for these administrators.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "iam:*",
 "Resource": "*"
 }
}`

```
