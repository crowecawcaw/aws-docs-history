# Inline policies for Signer

Inline policies are standalone identity-based policies that an administrator
creates and embeds directly into a single principal (user, group, or role).
Administrators can create and manage policies using the [AWS Management Console](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md"), the
[AWS Command Line Interface
(AWS CLI)](../../../IAM/latest/UserGuide/access_policies_create-cli.md "../../../IAM/latest/UserGuide/access_policies_create-cli.md"), or the [IAM API](../../../IAM/latest/UserGuide/access_policies_create-api.md "../../../IAM/latest/UserGuide/access_policies_create-api.md").

**To manage policies in the AWS Management Console**

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### Examples

- [Limit Access for Signing to All Signing Profiles
  Within an Account](#all_profiles "#all_profiles")
- [Limit Access for Signing to a Specific
  Signing Profile](#particular_profile "#particular_profile")
- [Limit Access for Signing to a Specific
  Signing Profile Version](#particular_version "#particular_version")
- [Allow Full Access](#policy-full-access "#policy-full-access")

## Limit Access for Signing to All Signing Profiles

Within an Account

The following policies allow a principal to discover every
`SigningProfile` within an account and to use any of them to
submit, describe, and list signing jobs.

**Policy for Lambda**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "signer:GetSigningProfile",
 "signer:ListSigningProfiles",
 "signer:StartSigningJob",
 "signer:DescribeSigningJob",
 "signer:ListSigningJobs"
 ],
 "Resource":"*"
 }
 ]
}`

```

**Policy for containers**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "signer:GetSigningProfile",
 "signer:ListSigningProfiles",
 "signer:SignPayload",
 "signer:GetRevocationStatus",
 "signer:DescribeSigningJob",
 "signer:ListSigningJobs"
 ],
 "Resource":"*"
 }
 ]
}`

```

## Limit Access for Signing to a Specific

Signing Profile

The following policies allow a principal to call
`GetSigningProfile` and `StartSigningJob` only on
profile `MySigningProfile`.

**Policy for Lambda**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "signer:GetSigningProfile",
 "signer:StartSigningJob"
 ],
 "Resource": "arn:aws:signer:`us-east-1`:444455556666:/signing-profiles/`MySigningProfile`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "signer:ListSigningJobs",
 "signer:ListSigningProfiles",
 "signer:DescribeSigningJob"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Policy for containers**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "signer:GetSigningProfile",
 "signer:SignPayload"
 ],
 "Resource": "arn:aws:signer:`us-east-1`:444455556666:/signing-profiles/`MySigningProfile`"
 },
 {
 "Effect": "Allow",
 "Action": [
 "signer:ListSigningJobs",
 "signer:ListSigningProfiles",
 "signer:DescribeSigningJob"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Limit Access for Signing to a Specific

Signing Profile Version

The following policy allows a principal to call `GetSigningProfile`
and `StartSigningJob` only on version `abcde12345` of
profile `MySigningProfile`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "signer:GetSigningProfile",
 "signer:SignPayload"
 ],
 "Resource": "arn:aws:signer:`us-east-1`:444455556666:/signing-profiles/`MySigningProfile`",
 "Condition": {
 "StringEquals": {
 "signer:ProfileVersion": "`version`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "signer:ListSigningJobs",
 "signer:ListSigningProfiles",
 "signer:DescribeSigningJob"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Allow Full Access

The following policy allows a principal to perform any AWS Signer action.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":"signer:*",
 "Resource":"*"
 }
 ]
}`

```
