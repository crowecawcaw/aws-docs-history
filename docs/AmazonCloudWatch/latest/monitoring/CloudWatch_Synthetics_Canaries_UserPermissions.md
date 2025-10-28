# Required roles and permissions for users

who manage CloudWatch canaries

To view canary details and the results of canary runs, you must be signed in as a user with
either
the `CloudWatchSyntheticsFullAccess` or the
`CloudWatchSyntheticsReadOnlyAccess` policies attached. To read all Synthetics data in the
console, you also need the `AmazonS3ReadOnlyAccess` and
`CloudWatchReadOnlyAccess` policies. To view the source code used by canaries,
you also need the `AWSLambda_ReadOnlyAccess` policy.

To create canaries, you must be signed in as an user who has the
`CloudWatchSyntheticsFullAccess` policy or a similar set of permissions. To
create IAM roles for the canaries, you also need the following inline policy
statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iam:CreateRole",
 "iam:CreatePolicy",
 "iam:AttachRolePolicy"
 ],
 "Resource": [
 "arn:aws:iam::*:role/service-role/CloudWatchSyntheticsRole*",
 "arn:aws:iam::*:policy/service-role/CloudWatchSyntheticsPolicy*"
 ]
 }
 ]
}`

```

###### Important

Granting a user the `iam:CreateRole`, `iam:CreatePolicy`, and
`iam:AttachRolePolicy` permissions gives that user full administrative access
to your AWS account. For example, a user with these permissions can create a policy that
has full permissions for all resources and can attach that policy to any role. Be very
careful about who you grant these permissions to.

For information
about attaching policies and granting permissions to users, see [Changing Permissions
for an IAM User](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") and [To embed an inline policy for a user or role](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#embed-inline-policy-console "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md#embed-inline-policy-console").
