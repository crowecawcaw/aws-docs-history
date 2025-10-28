# Allow

users to view their own permissions

This example shows how you might create a policy that allows a users to view the
inline and managed policies that are attached to their user identity. This policy
includes permissions to complete this action on the console or programmatically
using the AWS CLI or AWS API.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ViewOwnUserInfo",
 "Effect": "Allow",
 "Action": [
 "iam:GetUser",
 "iam:GetUserPolicy",
 "iam:ListAttachedUserPolicies",
 "iam:ListGroupsForUser",
 "iam:ListUserPolicies"
 ],
 "Resource": [
 "arn:aws:iam::*:user/${aws:username}"
 ]
 },
 {
 "Sid": "NavigateInConsole",
 "Effect": "Allow",
 "Action": [
 "iam:GetGroupPolicy",
 "iam:GetPolicy",
 "iam:GetPolicyVersion",
 "iam:ListAttachedGroupPolicies",
 "iam:ListGroupPolicies",
 "iam:ListGroups",
 "iam:ListPolicies",
 "iam:ListPolicyVersions",
 "iam:ListUsers"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```
