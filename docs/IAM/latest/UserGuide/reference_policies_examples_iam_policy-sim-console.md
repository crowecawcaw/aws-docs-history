# IAM: Access the policy simulator console

This example shows how you might create an identity-based policy that allows using the policy simulator console for policies attached to a
user, group, or role in the current AWS account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "access-analyzer:ValidatePolicy",
 "iam:GetContextKeysForCustomPolicy",
 "iam:GetGroupPolicy",
 "iam:GetPolicyVersion",
 "iam:GetRole",
 "iam:GetRolePolicy",
 "iam:GetUser",
 "iam:GetUserPolicy",
 "iam:ListAttachedGroupPolicies",
 "iam:ListAttachedRolePolicies",
 "iam:ListAttachedUserPolicies",
 "iam:ListGroups",
 "iam:ListGroupPolicies",
 "iam:ListGroupsForUser",
 "iam:ListPolicies",
 "iam:ListRolePolicies",
 "iam:ListRoles",
 "iam:ListUserPolicies",
 "iam:ListUsers",
 "iam:SimulateCustomPolicy",
 "iam:SimulatePrincipalPolicy"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```
