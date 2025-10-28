# Deregister an Amazon EC2 AMI

When you deregister an AMI, Amazon EC2 permanently deletes it. After you deregister an AMI, you can't
use it to launch new instances. You might consider deregistering an AMI when you have finished
using it.

To protect against accidental or malicious deregistering of an AMI, you can turn on [deregistration protection](ami-deregistration-protection.md "ami-deregistration-protection.md"). If you accidentally
deregister an EBS-backed AMI, you can use the [Recycle Bin](../../../ebs/latest/userguide/recycle-bin.md "../../../ebs/latest/userguide/recycle-bin.md") to restore it only if you
restore it within the allowed time period before it is permanently deleted.

When deregistering an AMI, you can optionally delete its associated snapshots at the same
time. However, if a snapshot is associated with multiple AMIs, it won't be deleted even if
specified for deletion, although the AMI will still be deregistered. Any snapshots not deleted
will continue to incur storage costs.

Deregistering an AMI has no effect on any instances that were launched from the AMI. You can
continue to use these instances. By default, deregistering an AMI also has no effect on any
snapshots that were created during the AMI creation process. You'll continue to incur usage
costs for these instances and storage costs for the snapshots. Therefore, to avoid incurring
unnecessary costs, we recommend that you terminate any instances and delete any snapshots that
you do not need. You can delete the snapshots either automatically during deregistration or
manually after deregistration. For more information, see [Avoid costs from unused
resources](#delete-unneeded-resources-to-avoid-unnecessary-costs "#delete-unneeded-resources-to-avoid-unnecessary-costs").

For instances launched from an AMI that is subsequently deregistered, you can still view
some high-level information about the AMI by using the
`describe-instance-image-metadata` AWS CLI command. For more information, see [describe-instance-image-metadata](../../../cli/latest/reference/ec2/describe-instance-image-metadata.md "../../../cli/latest/reference/ec2/describe-instance-image-metadata.md").

###### Contents

- [Considerations](#deregister-ami-considerations "#deregister-ami-considerations")
- [Deregister an AMI](#deregister-an-ami "#deregister-an-ami")
- [Avoid costs from unused
  resources](#delete-unneeded-resources-to-avoid-unnecessary-costs "#delete-unneeded-resources-to-avoid-unnecessary-costs")
- [Protect an Amazon EC2 AMI from deregistration](ami-deregistration-protection.md "ami-deregistration-protection.md")

## Considerations

- You can't deregister an AMI that is not owned by your account.
- You can't use Amazon EC2 to deregister an AMI that is managed by the AWS Backup service.
  Instead, use AWS Backup to delete the corresponding recovery points in the backup vault. For
  more information, see [Deleting backups](../../../aws-backup/latest/devguide/deleting-backups.md "../../../aws-backup/latest/devguide/deleting-backups.md") in the
  _AWS Backup Developer Guide_.

## Deregister an AMI

You can deregister EBS-backed AMIs and Amazon S3-backed AMIs. For EBS-backed AMIs, you can
optionally delete the associated snapshots at the same time. However, if a snapshot is
associated with other AMIs, it will not be deleted even if specified for deletion.

Console

###### To deregister an AMI

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **AMIs**.
3. From the filter bar, choose **Owned by me** to list your
   available AMIs, or choose **Disabled images** to list your disabled
   AMIs.
4. Select the AMI to deregister.
5. Choose **Actions**, **Deregister AMI**.
6. (Optional) To delete the associated snapshots during deregistration, select the
   **Delete associated snapshots** checkbox.

###### Note

If a snapshot is associated with other AMIs, it is not deleted, even if the
checkbox is selected. 7. Choose **Deregister AMI**.

It might take a few minutes before the console removes the AMI from the list.
Choose **Refresh** to refresh the status.

AWS CLI

###### To deregister an AMI

Use the following [deregister-image](../../../cli/latest/reference/ec2/deregister-image.md "../../../cli/latest/reference/ec2/deregister-image.md") command.

```
aws ec2 deregister-image --image-id `ami-0abcdef1234567890`
```

###### To deregister an AMI and delete its associated snapshots

Use the following [deregister-image](../../../cli/latest/reference/ec2/deregister-image.md "../../../cli/latest/reference/ec2/deregister-image.md") command and specify the
`--delete-associated-snapshots` parameter. Note that if a snapshot is
associated with other AMIs, it is not deleted, even if you specify this
parameter.

```
aws ec2 deregister-image \
    --image-id `ami-0abcdef1234567890` \
    --delete-associated-snapshots
```

PowerShell

###### To deregister an AMI

Use the [Unregister-EC2Image](../../../powershell/latest/reference/items/Unregister-EC2Image.md "../../../powershell/latest/reference/items/Unregister-EC2Image.md") cmdlet.

```
Unregister-EC2Image -ImageId `ami-0abcdef1234567890`
```

###### To deregister an AMI and delete its associated snapshots

Use the [Unregister-EC2Image](../../../powershell/latest/reference/items/Unregister-EC2Image.md "../../../powershell/latest/reference/items/Unregister-EC2Image.md") cmdlet and specify the
`-DeleteAssociatedSnapshots` parameter. Note that if a snapshot is
associated with other AMIs, it is not deleted, even if you specify this
parameter.

```
Unregister-EC2Image `
    -ImageId `ami-0abcdef1234567890` `
    -DeleteAssociatedSnapshots
```

## Avoid costs from unused

resources

Deregistering an AMI doesn't, by default, delete all of the resources that are associated
with the AMI. These resources include the snapshots for EBS-backed AMIs and the files in Amazon S3
for Amazon S3-backed AMIs. When you deregister an AMI, you also don't terminate or stop any
instances launched from the AMI.

You will continue to incur costs for storing the snapshots and files, and you will incur
costs for any running instances.

To avoid incurring these types of unnecessary costs, we recommend deleting any resources
that you don't need.

###### EBS-backed AMIs

- Delete the associated snapshots while deregistering the AMI. For more information, see
  [Deregister an AMI](#deregister-an-ami "#deregister-an-ami").
- If you deregister an AMI without deleting its associated snaphots, you can manually
  [delete the
  snapshots](../../../ebs/latest/userguide/ebs-deleting-snapshot.md#ebs-delete-snapshot "../../../ebs/latest/userguide/ebs-deleting-snapshot.md#ebs-delete-snapshot"). The snapshot of the instance root volume created during AMI creation
  has the following description format:

```
Created by CreateImage(`i-1234567890abcdef0`) for `ami-0abcdef1234567890`
```

- If you no longer need the instances that were launched from the AMI, you can
  [stop](Stop_Start.md#starting-stopping-instances "Stop_Start.md#starting-stopping-instances") or
  [terminate](terminating-instances.md#terminating-instances-console "terminating-instances.md#terminating-instances-console") them.
  To list the instances, filter by the ID of the AMI.

###### Amazon S3-backed AMIs

- Delete the bundle in Amazon S3 by using the [ec2-delete-bundle](ami-tools-commands.md#ami-delete-bundle "ami-tools-commands.md#ami-delete-bundle") (AMI tools) command.
- If the Amazon S3 bucket is empty after you delete the bundle, and you have no further
  use for that bucket, you can [delete the bucket](../../../AmazonS3/latest/userguide/delete-bucket.md "../../../AmazonS3/latest/userguide/delete-bucket.md").
- If you no longer need the instances that were launched from the AMI, you can
  [terminate](terminating-instances.md#terminating-instances-console "terminating-instances.md#terminating-instances-console") them.
  To list the instances, filter by the ID of the AMI.
