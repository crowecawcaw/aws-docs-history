# Restore a Storage Gateway volume

If you are restoring an AWS Storage Gateway volume snapshot, you can choose to restore the
snapshot as an Storage Gateway volume or as an Amazon EBS volume. This is because AWS Backup integrates with
both services, and any Storage Gateway snapshot can be restored to either an Storage Gateway volume or an
Amazon EBS volume.

## Restore Storage Gateway through the AWS Backup console

###### To restore an Storage Gateway volume

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources** and then
   choose the Storage Gateway resource ID you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the
   **Backups** pane, choose the radio button next to the recovery
   point ID of the resource. In the upper-right corner of the pane, choose
   **Restore**.
4. Specify the restore parameters for your resource. The restore parameters you enter
   are specific to the resource type that you selected.

For **Resource type**, choose the AWS resource to create when
restoring this backup. 5. If you choose **Storage Gateway volume**, choose a
**Gateway** in a reachable state. Also choose your **iSCSI
target name**.

    1. For "Volume stored" gateways, choose a **Disk Id**.
    2. For "Volume cached" gateways, choose a capacity that is at least as large as
     your protected resource.

If you choose **EBS volume**, provide the values for
**Volume type**, **Size (GiB)**, and choose an
**Availability zone**. 6. For **Restore role**, choose the IAM role that AWS Backup will
assume for this restore.

###### Note

If the AWS Backup default role is not present in your account, a **Default
role** is created for you with the correct permissions. You can delete
this default role or make it unusable. 7. Choose **Restore backup**.

The **Restore jobs** pane appears. A message at the top of the
page provides information about the restore job.

## Restore Storage Gateway with AWS CLI

In the command line interface, [`start-restore-job`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html") allows you to restore a Storage Gateway
volume.

The following list is the accepted metadata.

```
gatewayArn // The Amazon Resource Name (ARN) of the gateway. Use the `ListGateways` operation to return a list of gateways for your account and AWS Region.
gatewayType // The type of created gateway. Valid value is `BACKUP_VM`
targetName
kmsKey
volumeSize
volumeSizeInBytes
diskId
```
