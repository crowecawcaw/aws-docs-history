# IAM permissions for block public access

for Amazon EBS snapshots

By default, users don't have permission to work with block public access for snapshots.
To allow users to work with block public access for snapshots, you must create IAM policies
that grant permission to use specific API actions. Once the policies are created, you must
add permissions to your users, groups, or roles.

To work with block public access for snapshots, users need the following permissions.

- `ec2:EnableSnapshotBlockPublicAccess` — Enable block public access
  for snapshots and modify the mode.
- `ec2:DisableSnapshotBlockPublicAccess` — Disable block public access
  for snapshots.
- `ec2:GetSnapshotBlockPublicAccessState` — View the block public access
  for snapshots setting for a Region.
  The following is an example IAM policy. If some permissions are not needed, you can
  remove them from the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "ec2:EnableSnapshotBlockPublicAccess",
 "ec2:DisableSnapshotBlockPublicAccess",
 "ec2:GetSnapshotBlockPublicAccessState"
 ],
 "Resource": "*"
 }]
}`

```

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
