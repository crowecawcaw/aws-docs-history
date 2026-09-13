

# Share a volume
<a name="share-volume"></a>

You can use AWS Resource Access Manager (AWS RAM) to share Amazon EBS volumes with other AWS accounts. After you share a volume, consuming accounts can view volume information and create copies of the shared volume in the same Availability Zone. For more information about creating copies, see [Copy an Amazon EBS volume](ebs-copying-volume.md). Consuming accounts can't attach, modify, delete, or create snapshots of a shared volume.

For example, you can share production volumes with development accounts to refresh test environments with up-to-date production data while maintaining account-level isolation.

You can share volumes that are:
+ Unencrypted
+ Encrypted with a customer managed key

You can't share volumes that are encrypted with the default AWS managed key for Amazon EBS.

**Topics**
+ [Permissions](#share-volume-permissions)
+ [Share a volume](#share-volume-procedure)
+ [View shared volumes](#view-shared-volumes)
+ [Considerations for sharing volumes](#share-volume-considerations)
+ [Monitor sharing activity](#share-volume-monitoring)
+ [Shared volumes and Recycle Bin](#shared-volumes-recycle-bin)
+ [Pricing](#share-volume-pricing)

## Permissions
<a name="share-volume-permissions"></a>

When you create a resource share for shared volumes, you must associate managed permissions with the resource share. The managed permissions determine which actions consuming accounts can perform on the shared volumes in the resource share. AWS RAM provides the following AWS managed permissions:
+ **AWSRAMDefaultPermissionEBSVolume** (default) – Grants consuming accounts permission to view volume information.
+ **AWSRAMPermissionEBSVolumeCopyAccess** – Grants consuming accounts permission to view volume information and create copies of the shared volume.

Alternatively, you can create a customer managed permission for the `ec2:Volume` resource type. For more information, see [Creating and using customer managed permissions](https://docs.aws.amazon.com/ram/latest/userguide/create-customer-managed-permissions.html) in the *AWS RAM User Guide*.

## Share a volume
<a name="share-volume-procedure"></a>

Use one of the following methods to share an Amazon EBS volume.

------
#### [ Console ]

**To share a volume**

1. Open the Amazon Elastic Compute Cloud console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Volumes**.

1. Select the volume, and then choose **Actions**, **Share volume**.

1. Do one of the following:
   + To add the volume to an existing resource share, select the resource share.
   + To create a new resource share, choose **Create new resource share**. This opens the AWS RAM console, where you configure the share.

1. For **Principals**, add the accounts to share the volume with. You can add individual account IDs, organizational units (OUs), or your entire organization.

1. For **Managed permissions**, choose one of the following:
   + **AWSRAMDefaultPermissionEBSVolume** (default) – Consuming accounts can view volume metadata only.
   + **AWSRAMPermissionEBSVolumeCopyAccess** – Consuming accounts can view volume metadata and create copies of the shared volume.
   + A customer managed permission that you created for the `ec2:Volume` resource type.

1. Choose **Create resource share**.

------
#### [ AWS CLI ]

Use the [create-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html) command. Specify the volume ARN, the consuming account, and the permission ARN. To find the volume ARN, call [describe-volumes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html). The response includes the `VolumeArn` field for each volume.

The following example creates a resource share that shares volume `vol-1234567890abcdef0` with account `222222222222`, and assigns the `AWSRAMPermissionEBSVolumeCopyAccess` managed permission:

```
aws ram create-resource-share \
--name {{my-volume-share}} \
--resource-arns {{arn:aws:ec2:us-east-1:111111111111:volume/vol-1234567890abcdef0}} \
--principals {{222222222222}} \
--permission-arns {{arn:aws:ram::aws:permission/AWSRAMPermissionEBSVolumeCopyAccess}} \
--region us-east-1
```

To share with the default permission (`AWSRAMDefaultPermissionEBSVolume`, describe only), omit the `--permission-arns` parameter:

```
aws ram create-resource-share \
--name {{my-volume-share}} \
--resource-arns {{arn:aws:ec2:us-east-1:111111111111:volume/vol-1234567890abcdef0}} \
--principals {{222222222222}} \
--region us-east-1
```

------

For more information about resource shares, see [Creating a resource share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the *AWS RAM User Guide*.

## View shared volumes
<a name="view-shared-volumes"></a>

After you create the resource share, the specified accounts receive an invitation. Accounts outside your organization in AWS Organizations must accept the invitation before they can access shared volumes. For more information, see [Accepting and rejecting resource share invitations](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-create.html) in the *AWS RAM User Guide*.

You can view the volumes that are shared with your account using one of the following methods.

------
#### [ Console ]

**To view shared volumes**

1. Open the Amazon Elastic Compute Cloud console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Volumes**.

1. Do one of the following:
   + Choose the **Shared with me** preset filter to show all volumes shared with your account.
   + Choose **Add filter**, **Owner ID**, and then enter the sharing account ID.

Shared volumes display the sharing account ID in the **Owner ID** column.

------
#### [ AWS CLI ]

Use the [describe-volumes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html) command with the `owner-id` filter to show volumes shared with you by a specific account.

```
aws ec2 describe-volumes \
--filters Name=owner-id,Values={{111111111111}} \
--region us-east-1
```

Shared volumes include the `OwnerId` field in the response, which shows the sharing account ID.

------

## Considerations for sharing volumes
<a name="share-volume-considerations"></a>

Consider the following when you share volumes with other accounts.
+ You can share unencrypted volumes and volumes encrypted with a customer managed key. You can't share volumes encrypted with the default AWS managed key for Amazon EBS.
+ To share a volume, the volume owner's account must have `kms:DescribeKey` permission on the default Amazon EBS encryption key. This is required for all volumes, including unencrypted volumes, because the service validates the volume's encryption state during the share process.
+ To share a volume encrypted with a customer managed key, you must also share the KMS key with the consuming account. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) in the *AWS Key Management Service Developer Guide*.
+ To create copies of a shared encrypted volume, the consuming account requires `kms:CreateGrant`, `kms:GenerateDataKey`, `kms:GenerateDataKeyWithoutPlaintext`, `kms:ReEncrypt*`, and `kms:Decrypt` on the KMS key.
+ Consuming accounts can't attach, modify, delete, or create snapshots of a shared volume. They can only view volume metadata and create copies.
+ Only one copy operation can be in progress on a shared volume at a time, across all accounts the volume is shared with. Additional copy requests return an error until the current operation completes.
+ Availability Zone names (such as `us-east-1a`) map to different physical locations in different AWS accounts. Use Availability Zone IDs (such as `use1-az1`) to identify the same physical location across accounts. For more information, see [Availability Zone IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html) in the *AWS RAM User Guide*.
+ Removing a volume from a resource share doesn't cancel in-progress copy operations.
+ Deleting the source volume doesn't cancel in-progress copy operations.

## Monitor sharing activity
<a name="share-volume-monitoring"></a>

### AWS CloudTrail API logging
<a name="share-volume-monitoring-cloudtrail"></a>

All volume sharing and copy API calls are logged in AWS CloudTrail. `CopyVolumes` API calls are logged for both the account that initiates the copy and the volume owner's account. For more information, see [Logging Amazon Elastic Compute Cloud API calls with AWS CloudTrail](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitor-with-cloudtrail.html).

### Amazon EventBridge notifications
<a name="share-volume-monitoring-eventbridge"></a>

Amazon EBS sends Amazon EventBridge events when cross-account copy operations complete. Both the volume owner and the consuming account receive the event. Volume copy events use the detail type `EBS Volume Notification` with the event name `sharedVolumeCopy`. The event includes the volume ID, the completion status (`completed` or `failed`), and a timestamp.

To set up notifications, create an Amazon EventBridge rule that matches `EBS Volume Notification` events with the `sharedVolumeCopy` event name. For more information, see [Amazon EventBridge events for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-cloud-watch-events.html).

## Shared volumes and Recycle Bin
<a name="shared-volumes-recycle-bin"></a>

If you have a Recycle Bin retention rule that applies to volumes, deleting a shared volume moves it to Recycle Bin. The volume stays in its AWS RAM resource shares throughout the retention period. When you restore the volume from Recycle Bin, it's accessible through the same resource shares it belonged to before deletion.

Note the following resource share behavior for a volume that is in Recycle Bin:
+ If you removed an account from the resource share while the volume was in Recycle Bin, restoring the volume doesn't re-grant that account access.
+ If you added an account to the resource share while the volume was in Recycle Bin, that account has access to the volume after restoration.

After you restore a volume from Recycle Bin, verify that only intended accounts have access by reviewing your resource shares in the [AWS RAM console](https://console.aws.amazon.com/ram/).

## Pricing
<a name="share-volume-pricing"></a>

There is no cost for sharing volumes through AWS RAM. The account that creates a copy pays the volume copy fee and regular Amazon EBS volume charges for the new volume. For more information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/).