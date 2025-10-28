End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Allow

users to view their own permissions in AWS IoT Events

This example shows how you might create a policy that allows users to view the inline
and managed policies that are attached to their user identity. Allowing users to view
their own IAM permissions is useful for security awareness and self-service
capabilities. This policy includes permissions to complete this action on the console or
programmatically using the AWS CLI or AWS API.

JSON

```
`{
 "Version":"2012-10-17",
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
 "Resource": [
 "arn:aws:iam::*:user/${aws:username}"
 ]
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
 }`

```
