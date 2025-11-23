# Recover deleted snapshots from the Recycle Bin

This topic explains how to recover Amazon EBS snapshots from the Recycle Bin.

###### Topics

- [Permissions for working with snapshots in the Recycle Bin](#snap-perms "#snap-perms")
- [View snapshots in the Recycle Bin](#recycle-bin-view-snaps "#recycle-bin-view-snaps")
- [Restore snapshots from the Recycle Bin](#recycle-bin-restore-snaps "#recycle-bin-restore-snaps")

## Permissions for working with snapshots in the Recycle Bin

By default, users don't have permission to work with snapshots that are in the
Recycle Bin. To allow users to work with these resources, you must create IAM policies
that grant permission to use specific resources and API actions. After the policies are
created, you must add permissions to your users, groups, or roles.

To view and recover snapshots that are in the Recycle Bin, users must have
the following permissions:

- `ec2:ListSnapshotsInRecycleBin`
- `ec2:RestoreSnapshotFromRecycleBin`

To manage tags for snapshots in the Recycle Bin, users need the following additional
permissions.

- `ec2:CreateTags`
- `ec2:DeleteTags`

To use the Recycle Bin console, users need the `ec2:DescribeTags`
permission.

The following is an example IAM policy. It includes the `ec2:DescribeTags` permission
for console users, and it includes the `ec2:CreateTags` and `ec2:DeleteTags`
permissions for managing tags. If the permissions are not needed, you can remove them from the policy.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

For more information about the permissions needed to use Recycle Bin, see [Permissions for working with Recycle Bin and
retention rules](recycle-bin-perms.md#rule-perms "recycle-bin-perms.md#rule-perms").

## View snapshots in the Recycle Bin

While a snapshot is in the Recycle Bin, you can view limited information about it, including:

- The ID of the snapshot.
- The snapshot description.
- The ID of the volume from which the snapshot was created.
- The date and time when the snapshot was deleted and it entered Recycle Bin.
- The date and time when the retention period expires. The snapshot will be permanently
  deleted from the Recycle Bin at this time.

You can view the snapshots in the Recycle Bin using one of the following methods.

Recycle Bin console

###### To view snapshots in the Recycle Bin using the console

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Recycle Bin**.
3. The grid lists all of the snapshots that are currently in the Recycle Bin. To view the
   details for a specific snapshot, select it in the grid and choose **Actions**,
   **View details**.

AWS CLI

###### To view snapshots in the Recycle Bin using the AWS CLI

Use the [list-snapshots-in-recycle-bin](../../../cli/latest/reference/ec2/list-snapshots-in-recycle-bin.md "../../../cli/latest/reference/ec2/list-snapshots-in-recycle-bin.md") AWS CLI command. Include the `--snapshot-id` option to
view a specific snapshot. Or omit the `--snapshot-id` option to view all snapshots in the
Recycle Bin.

```
aws ec2 list-snapshots-in-recycle-bin --snapshot-id `snapshot_id`
```

For example, the following command provides information about snapshot `snap-01234567890abcdef`
in the Recycle Bin.

```
aws ec2 list-snapshots-in-recycle-bin --snapshot-id snap-01234567890abcdef
```

Example output:

```
{
    "SnapshotRecycleBinInfo": [
        {
            "Description": "Monthly data backup snapshot",
            "RecycleBinEnterTime": "2021-12-01T13:00:00.000Z",
            "RecycleBinExitTime": "2021-12-15T13:00:00.000Z",
            "VolumeId": "vol-abcdef09876543210",
            "SnapshotId": "snap-01234567890abcdef"
        }
    ]
}
```

## Restore snapshots from the Recycle Bin

You can't use a snapshot in any way while it is in the Recycle Bin. To use the snapshot,
you must first restore it. When you restore a snapshot from the Recycle Bin, the snapshot is
immediately available for use, and it is removed from the Recycle Bin. You can use a restored
snapshot in the same way that you use any other snapshot in your account.

You can restore a snapshot from the Recycle Bin using one of the following methods.

Recycle Bin console

###### To restore a snapshot from the Recycle Bin using the console

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Recycle Bin**.
3. The grid lists all of the snapshots that are currently in the Recycle Bin. Select
   the snapshot to restore and and choose **Recover**.
4. When prompted, choose **Recover**.

AWS CLI

###### To restore a deleted snapshot from the Recycle Bin using the AWS CLI

Use the [restore-snapshot-from-recycle-bin](../../../cli/latest/reference/ec2/restore-snapshot-from-recycle-bin.md "../../../cli/latest/reference/ec2/restore-snapshot-from-recycle-bin.md") AWS CLI command. For `--snapshot-id`,
specify the ID of the snapshot to restore.

```
aws ec2 restore-snapshot-from-recycle-bin --snapshot-id `snapshot_id`
```

For example, the following command restores snapshot `snap-01234567890abcdef` from the
Recycle Bin.

```
aws ec2 restore-snapshot-from-recycle-bin --snapshot-id snap-01234567890abcdef
```

Example output:

```
{
    "SnapshotId": "snap-01234567890abcdef",
    "Description": "Monthly data backup snapshot",
    "Encrypted": false,
    "OwnerId": "111122223333",
    "Progress": "100%",
    "StartTime": "2021-12-01T13:00:00.000000+00:00",
    "State": "recovering",
    "VolumeId": "vol-ffffffff",
    "VolumeSize": 30
}
```
