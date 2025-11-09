# Control access to Amazon EBS snapshot lock

By default, users don't have permission to work with snapshot locks. To allow users
to use snapshot locks, you must create IAM policies that grant permission to use specific
resources and API actions. For more information, see [Creating IAM policies in the
IAM User Guide](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md").

###### Topics

- [Required permissions](#snapshot-lock-req-perms "#snapshot-lock-req-perms")
- [Restrict access with condition keys](#snapshot-lock-condition-keys "#snapshot-lock-condition-keys")

## Required permissions

To work with snapshot locks, users need the following permissions.

- `ec2:LockSnapshot` — To lock snapshots.
- `ec2:UnlockSnapshot` — To unlock snapshots.
- `ec2:DescribeLockedSnapshots` — To view snapshot lock settings.

The following is an example IAM policy that gives users permission to lock and unlock
snapshots, and to view snapshot lock settings. It includes the `ec2:DescribeSnapshots`
permission for console users. If some permissions are not needed, you can remove them from
the policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSnapshotLockOperations",
 "Effect": "Allow",
 "Action": [
 "ec2:LockSnapshot",
 "ec2:UnlockSnapshot",
 "ec2:DescribeLockedSnapshots",
 "ec2:DescribeSnapshots"
 ],
 "Resource": [
 "arn:aws:ec2:*::snapshot/*",
 "arn:aws:ec2:*:`111122223333`:volume/*"
 ]
 }
 ]
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

## Restrict access with condition keys

You can use condition keys to restrict how users are allowed to lock snapshots.

###### Topics

- [ec2:SnapshotLockDuration](#snapshotlockduration "#snapshotlockduration")
- [ec2:CoolOffPeriod](#cooloffperiod "#cooloffperiod")

### ec2:SnapshotLockDuration

You can use the `ec2:SnapshotLockDuration` condition key to restrict users
to specific lock durations when locking snapshots.

The following example policy restricts users to specifying a lock duration between
`10` and `50` days.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSnapshotLockWithDurationCondition",
 "Effect": "Allow",
 "Action": "ec2:LockSnapshot",
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "NumericGreaterThan": {
 "ec2:SnapshotLockDuration": 10
 },
 "NumericLessThan": {
 "ec2:SnapshotLockDuration": 50
 }
 }
 }
 ]
}`

```

### ec2:CoolOffPeriod

You can use the `ec2:CoolOffPeriod` condition key to prevent users
from locking snapshots in compliance mode without a cooling-off period.

The following example policy restricts users to specifying a cooling-off period
greater than `48` hours when locking snapshots in compliance mode.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSnapshotLockWithCondition",
 "Effect": "Allow",
 "Action": "ec2:LockSnapshot",
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "NumericGreaterThan": {
 "ec2:SnapshotTime": 48
 }
 }
 }
 ]
}`

```
