# Recover deleted AMIs from the Recycle Bin

This topic explains how to recover Amazon EBS-backed AMIs from the Recycle Bin.

###### Topics

- [Permissions for working with AMIs in the Recycle Bin](#ami-perms "#ami-perms")
- [View AMIs in the Recycle Bin](#recycle-bin-view-ami "#recycle-bin-view-ami")
- [Restore AMIs from the Recycle Bin](#recycle-bin-restore-ami "#recycle-bin-restore-ami")

## Permissions for working with AMIs in the Recycle Bin

By default, users don't have permission to work with AMIs that are in the Recycle Bin.
To allow users to work with these resources, you must create IAM policies that grant
permission to use specific resources and API actions. After the policies are created, you must
add permissions to your users, groups, or roles.

To view and recover AMIs that are in the Recycle Bin, users must have the following
permissions:

- `ec2:ListImagesInRecycleBin`
- `ec2:RestoreImageFromRecycleBin`

To manage tags for AMIs in the Recycle Bin, users need the following additional
permissions.

- `ec2:CreateTags`
- `ec2:DeleteTags`

To use the Recycle Bin console, users need the `ec2:DescribeTags`
permission.

The following is an example IAM policy. It includes the `ec2:DescribeTags`
permission for console users, and it includes the `ec2:CreateTags` and
`ec2:DeleteTags` permissions for managing tags. If the permissions are not
needed, you can remove them from the policy.

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

## View AMIs in the Recycle Bin

While an AMI is in the Recycle Bin, you can view limited information about it, including:

- The name, description, and unique ID of the AMI.
- The date and time when the AMI was deleted and it entered Recycle Bin.
- The date and time when the retention period expires. The AMI will be permanently
  deleted at this time.

You can view the AMIs in the Recycle Bin using one of the following methods.

Recycle Bin console

###### To view deleted AMIs in the Recycle Bin using the console

1. Open the Recycle Bin console at [console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/").
2. In the navigation pane, choose **Recycle Bin**.
3. The grid lists all of the resources that are currently in the Recycle Bin. To
   view the details for a specific AMI, select it in the grid, and choose
   **Actions**, **View details**.

AWS CLI

###### To view deleted AMIs in the Recycle Bin using the AWS CLI

Use the [list-images-in-recycle-bin](../../../cli/latest/reference/ec2/list-images-in-recycle-bin.md "../../../cli/latest/reference/ec2/list-images-in-recycle-bin.md") AWS CLI command. To view specific AMIs, include
the `--image-id` option and specify the IDs of the AMIs to view. You can
specify up to 20 IDs in a single request.

To view all of the AMIs in the Recycle Bin, omit the `--image-id`
option. If you do not specify a value for `--max-items`, the command returns
1,000 items per page, by default. For more information, see [Pagination](../../../AWSEC2/latest/APIReference/Query-Requests.md#api-pagination "../../../AWSEC2/latest/APIReference/Query-Requests.md#api-pagination") in the _Amazon EC2 API Reference_.

```
aws ec2 list-images-in-recycle-bin --image-id `ami_id`
```

For example, the following command provides information about AMI `ami-01234567890abcdef`
in the Recycle Bin.

```
aws ec2 list-images-in-recycle-bin --image-id ami-01234567890abcdef
```

Example output:

```
{
    "Images": [
        {
            "ImageId": "ami-0f740206c743d75df",
            "Name": "My AL2 AMI",
            "Description": "My Amazon Linux 2 AMI",
            "RecycleBinEnterTime": "2021-11-26T21:04:50+00:00",
            "RecycleBinExitTime": "2022-03-06T21:04:50+00:00"
        }
    ]
}
```

###### Important

If you receive the following error, you might need to update your AWS CLI version. For more information, see [Command not found errors](../../../cli/latest/userguide/cli-chap-troubleshooting.md#tshoot-install-not-found "../../../cli/latest/userguide/cli-chap-troubleshooting.md#tshoot-install-not-found") .

```
aws.exe: error: argument operation: Invalid choice, valid choices are: ...
```

## Restore AMIs from the Recycle Bin

You can't use an AMI in any way while it is in the Recycle Bin. To use the AMI,
you must first restore it. When you restore an AMI from the Recycle Bin, the AMI is
immediately available for use, and it is removed from the Recycle Bin. You can use a
restored AMI in the same way that you use any other AMI in your account.

You can restore an AMI from the Recycle Bin using one of the following methods.

Recycle Bin console

###### To restore an AMI from the Recycle Bin using the console

1. Open the Recycle Bin console at [console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/ "https://console.aws.amazon.com/rbin/home/").
2. In the navigation pane, choose **Recycle Bin**.
3. The grid lists all of the resources that are currently in the Recycle Bin.
   Select the AMI to restore, and choose **Recover**.
4. When prompted, choose **Recover**.

AWS CLI

###### To restore a deleted AMI from the Recycle Bin using the AWS CLI

Use the [restore-image-from-recycle-bin](../../../cli/latest/reference/ec2/restore-image-from-recycle-bin.md "../../../cli/latest/reference/ec2/restore-image-from-recycle-bin.md") AWS CLI command. For `--image-id`, specify the
ID of the AMI to restore.

```
aws ec2 restore-image-from-recycle-bin --image-id `ami_id`
```

For example, the following command restores AMI `ami-01234567890abcdef` from the
Recycle Bin.

```
aws ec2 restore-image-from-recycle-bin --image-id ami-01234567890abcdef
```

The command returns no output on success.

###### Important

If you receive the following error, you might need to update your AWS CLI version. For more information, see [Command not found errors](../../../cli/latest/userguide/cli-chap-troubleshooting.md#tshoot-install-not-found "../../../cli/latest/userguide/cli-chap-troubleshooting.md#tshoot-install-not-found") .

```
aws.exe: error: argument operation: Invalid choice, valid choices are: ...
```
