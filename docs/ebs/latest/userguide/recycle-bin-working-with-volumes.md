# Recover deleted volumes from the Recycle Bin

This topic explains how to recover Amazon EBS volumes from the Recycle Bin.

###### Topics

- [Permissions for working with volumes in the Recycle Bin](#volume-perms "#volume-perms")
- [View volumes in the Recycle Bin](#recycle-bin-view-volumes "#recycle-bin-view-volumes")
- [Restore volumes from the Recycle Bin](#recycle-bin-restore-volumes "#recycle-bin-restore-volumes")

## Permissions for working with volumes in the Recycle Bin

By default, users don't have permission to work with volumes that are in the
Recycle Bin. To allow users to work with these resources, you must create IAM policies
that grant permission to use specific resources and API actions. After the policies are
created, you must add permissions to your users, groups, or roles.

To view and recover volumes that are in the Recycle Bin, users must have
the following permissions:

- `ec2:ListVolumesInRecycleBin`
- `ec2:RestoreVolumeFromRecycleBin`

To manage tags for volumes in the Recycle Bin, users need the following additional
permissions.

- `ec2:CreateTags`
- `ec2:DeleteTags`

To use the Recycle Bin console, users need the `ec2:DescribeTags`
permission.

The following is an example IAM policy. It includes the `ec2:DescribeTags` permission
for console users, and it includes the `ec2:CreateTags` and `ec2:DeleteTags`
permissions for managing tags. If the permissions are not needed, you can remove them from the policy.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRecycleBinVolumeOperations",
      "Effect": "Allow",
      "Action": [
        "ec2:ListVolumesInRecycleBin",
        "ec2:RestoreVolumeFromRecycleBin"
      ],
      "Resource": "arn:aws:ec2:*:`123456789012`:volume/*"
    },
    {
      "Sid": "AllowVolumeTagOperations",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateTags",
        "ec2:DeleteTags",
        "ec2:DescribeTags"
      ],
      "Resource": "arn:aws:ec2:*:`123456789012`:volume/*"
    }
  ]
}
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

For more information about the permissions needed to use Recycle Bin, see [Permissions for working with Recycle Bin and
retention rules](recycle-bin-perms.md#rule-perms "recycle-bin-perms.md#rule-perms").

## View volumes in the Recycle Bin

While a volume is in the Recycle Bin, you can view limited information about it, including:

- The ID of the volume.
- The size of the volume.
- The volume type.
- The date and time when the volume was deleted and it entered Recycle Bin.
- The date and time when the retention period expires. The volume will be permanently
  deleted from the Recycle Bin at this time.

You can view the volumes in the Recycle Bin using one of the following methods.

Recycle Bin console

###### To view volumes in the Recycle Bin using the console

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Recycle Bin**.
3. The grid lists all of the volumes that are currently in the Recycle Bin. To view the
   details for a specific volume, select it in the grid and choose **Actions**,
   **View details**.

AWS CLI

###### To view volumes in the Recycle Bin using the AWS CLI

Use the [list-volumes-in-recycle-bin](../../../cli/latest/reference/ec2/list-volumes-in-recycle-bin.md "../../../cli/latest/reference/ec2/list-volumes-in-recycle-bin.md") AWS CLI command. Include the `--volume-id` option to
view a specific volume. Or omit the `--volume-id` option to view all volumes in the
Recycle Bin.

```
aws ec2 list-volumes-in-recycle-bin --volume-id `volume_id`
```

For example, the following command provides information about volume `vol-01234567890abcdef`
in the Recycle Bin.

```
aws ec2 list-volumes-in-recycle-bin --volume-id vol-01234567890abcdef
```

Example output:

```
{
    "VolumeRecycleBinInfo": [
        {
            "VolumeId": "vol-01234567890abcdef",
            "RecycleBinEnterTime": "2021-12-01T13:00:00.000Z",
            "RecycleBinExitTime": "2021-12-08T13:00:00.000Z"
        }
    ]
}
```

## Restore volumes from the Recycle Bin

You can't use a volume in any way while it is in the Recycle Bin. To use the volume,
you must first restore it. When you restore a volume from the Recycle Bin, the volume is
immediately available for use, and it is removed from the Recycle Bin. You can use a restored
volume in the same way that you use any other volume in your account.

You can restore a volume from the Recycle Bin using one of the following methods.

Recycle Bin console

###### To restore a volume from the Recycle Bin using the console

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/")
2. In the navigation pane, choose **Recycle Bin**.
3. The grid lists all of the volumes that are currently in the Recycle Bin. Select
   the volume to restore and choose **Recover**.
4. When prompted, choose **Recover**.

AWS CLI

###### To restore a deleted volume from the Recycle Bin using the AWS CLI

Use the [restore-volume-from-recycle-bin](../../../cli/latest/reference/ec2/restore-volume-from-recycle-bin.md "../../../cli/latest/reference/ec2/restore-volume-from-recycle-bin.md") AWS CLI command. For `--volume-id`,
specify the ID of the volume to restore.

```
aws ec2 restore-volume-from-recycle-bin --volume-id `volume_id`
```

For example, the following command restores volume `vol-01234567890abcdef` from the
Recycle Bin.

```
aws ec2 restore-volume-from-recycle-bin --volume-id vol-01234567890abcdef
```

Example output:

```
{
    "VolumeId": "vol-01234567890abcdef",
    "State": "available",
    "Size": 100,
    "VolumeType": "gp3",
    "AvailabilityZone": "us-east-1a",
    "CreateTime": "2021-12-01T13:00:00.000000+00:00",
    "Encrypted": false
}
```
