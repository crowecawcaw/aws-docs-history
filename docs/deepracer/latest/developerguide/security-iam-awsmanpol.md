# AWS managed policies for AWS DeepRacer

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed
to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because
they're available for all AWS customers to use. We recommend that you reduce permissions further by defining
[customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS
managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is
most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
existing services.

For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the
_IAM User Guide_.

The following AWS-managed policies are specific to using AWS DeepRacer multi-user
mode to sponsor multiple participants under your AWS account.

- `AWSDeepRacerAccountAdminAccess` Grants required AWS DeepRacer permissions for multi-user account admin.
- `AWSDeepRacerDefaultMultiUserAccess` Grants required AWS DeepRacer permissions to use the AWS DeepRacer console.

###### Topics

- [AWSDeepRacerAccountAdminAccess managed policy for
  AWS DeepRacer administrators](#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess "#security-iam-awsmanpol-AWSDeepRacerAccountAdminAccess")
- [AWSDeepRacerDefaultMultiUserAccess managed policy
  for AWS DeepRacer multi-user racers](#security-iam-awsmanpol-AWSDeepRacerDefaultUserAccess "#security-iam-awsmanpol-AWSDeepRacerDefaultUserAccess")
- [AWS DeepRacer updates to AWS managed policies](#security-iam-awsmanpol-updates "#security-iam-awsmanpol-updates")

## AWSDeepRacerAccountAdminAccess managed policy for

AWS DeepRacer administrators

To enable multiple profiles to use your AWS account ID and billing information with AWS DeepRacer, attach the
`AWSDeepRacerAccountAdminAccess` policy.

You can attach the `AWSDeepRacerAccountAdminAccess` policy to the IAM identity you want to use for
sponsoring other racers.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DeepRacerAdminAccessStatement",
 "Effect": "Allow",
 "Action": [
 "deepracer:*"
 ],
 "Resource": [
 "*"
 ],
 "Condition":
 {
 "Null": {
 "deepracer:UserToken": "true"
 }
 }
 }
 ]
}`

```

## AWSDeepRacerDefaultMultiUserAccess managed policy

for AWS DeepRacer multi-user racers

The policy, `AWSDeepRacerDefaultMultiUserAccess`, gives AWS DeepRacer racers access to all AWS DeepRacer actions except
multi-user account admin actions.

You can attach the `AWSDeepRacerDefaultMultiUserAccess` policy to the IAM identities of participants you
want to sponsor under your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "deepracer:Add*",
 "deepracer:Remove*",
 "deepracer:Create*",
 "deepracer:Perform*",
 "deepracer:Clone*",
 "deepracer:Get*",
 "deepracer:List*",
 "deepracer:Edit*",
 "deepracer:Start*",
 "deepracer:Set*",
 "deepracer:Update*",
 "deepracer:Delete*",
 "deepracer:Stop*",
 "deepracer:Import*",
 "deepracer:Tag*",
 "deepracer:Untag*"
 ],
 "Resource": [
 "*"
 ],
 "Condition": {
 "Null": {
 "deepracer:UserToken": "false"
 },
 "Bool": {
 "deepracer:MultiUser": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "deepracer:GetAccountConfig",
 "deepracer:GetTrack",
 "deepracer:ListTracks",
 "deepracer:TestRewardFunction"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Deny",
 "Action": [
 "deepracer:Admin*"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS DeepRacer updates to AWS managed policies

View details about updates to AWS managed policies for AWS DeepRacer since this service began tracking these changes. For
automatic alerts about changes to this page, subscribe to the RSS feed on the AWS DeepRacer Document history page.

| Change                                                                                      | Description                                                                                                                   | Date             |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `AWSDeepRacerAccountAdminAccess` and `AWSDeepRacerDefaultMultiUserAccess`<br>policies added | New managed policies added so you can sponsor multiple participants under one AWS DeepRacer account using<br>multi-user mode. | October 26, 2021 |
| AWS DeepRacer started tracking policy changes.                                              | AWS DeepRacer started tracking changes for its AWS managed policies.                                                          | October 26, 2021 |
