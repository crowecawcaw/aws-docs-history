# Replace the root volume for an Amazon EC2 instance without stopping it

Amazon EC2 enables you to replace the root Amazon EBS volume for a running
instance while retaining the following:

- Data stored on instance store volumes — Instance store volumes remain attached
  to the instance after the root volume has been restored.
- Data stored on data (non-root) Amazon EBS volumes — Non-root Amazon EBS volumes remain
  attached to the instance after the root volume has been restored.
- Network configuration — All network interfaces remain attached to the instance
  and they retain their IP addresses, identifiers, and attachment IDs. When the instance
  becomes available, all pending network traffic is flushed. Additionally, the instance
  remains on the same physical host, so it retains its public and private IP addresses and
  DNS name.
- IAM policies — IAM profiles and policies (such as tag-based policies)
  that are associated with the instance are retained and enforced.

###### Contents

- [How root volume replacement works](#replace-root-how "#replace-root-how")
- [Considerations](#replace-root-considerations "#replace-root-considerations")
- [Replace a root volume](#replace "#replace")

## How root volume replacement works

When you replace the root volume for an instance, we create _root volume
replacement task_. The original root volume is detached from the instance, and the new root volume is
attached to the instance in its place. The instance's block device mapping is updated to
reflect the ID of the replacement root volume.

When you replace the root volume for an instance, you must specify the source of the
snapshot for the new volume. The following are the possible options.

This option replaces the current root volume with a volume that is based on the
snapshot that was used to create it.

###### Considerations for using the launch state

The replacement root volume gets the same type, size, and delete on termination attributes
as the original root volume.

This option replaces the current root volume with a replacement volume that is based
on the snapshot that you specify. For example, a specific snapshot that you previously
created from this root volume. This is useful if you need to recover from issues caused
by corruption of the root volume or network configuration errors in the guest operating
system.

The replacement root volume gets the same type, size, and delete on termination attributes
as the original root volume.

###### Considerations for using a snapshot

- You can only use snapshots that were created directly from the instance's current
  or previous root volumes.
- You can't use snapshot copies created from snapshots that were taken from the root
  volume.
- After successfully replacing the root volume, you can still use snapshots taken
  from the original root volume to replace the new (replacement) root volume.
  This option replaces the current root volume using an AMI that you specify.
  This is useful if you need to perform operating system and application patching or upgrades.
  The AMI must have the same product code, billing information, architecture type, and
  virtualization type as the instance.

If the instance is enabled for ENA or sriov-net, then you must use an AMI
that supports those features. If the instance is not enabled for ENA or sriov-net, then
you can either select an AMI that doesn't include support for those features, or you
can automatically add support if you select an AMI that supports ENA or sriov-net.

If the instance is enabled for NitroTPM, then you must use an AMI that has NitroTPM
enabled. NitroTPM support is not enabled if the instance was not configured for it,
regardless of the AMI that you select.

You can select an AMI with a different boot mode than that of the instance, as long
as the instance supports the boot mode of the AMI. If the instance does not support the
boot mode, the request fails. If the instance supports the boot mode, the new boot mode is
propagated to the instance and its UEFI data is updated accordingly. If you manually
modified the boot order or added a private UEFI Secure Boot key to load private kernel
modules, the changes are lost during root volume replacement.

The replacement root volume gets the same volume type and delete on termination
attribute as the original root volume, and it gets the size of the AMI root volume block
device mapping.

###### Note

The size of the AMI root volume block device mapping must be equal to or greater
than the size of the original root volume. If the size of the AMI root volume block
device mapping is smaller than the size of the original root volume, the request fails.

After the root volume replacement task completes, the following new and updated
information is reflected when you describe the instance using the console, AWS CLI or AWS
SDKs:

- New AMI ID
- New volume ID for the root volume
- Updated boot mode configuration (if changed by the AMI)
- Updated NitroTPM configuration (if enabled by the AMI)
- Updated ENA configuration (if enabled by the AMI)
- Updated sriov-net configuration (if enabled by the AMI)
  The new AMI ID is also reflected in the instance metadata.

###### Considerations for using an AMI:

- If you use an AMI that has multiple block device mappings, only the root volume
  of the AMI is used. The other (non-root) volumes are ignored.
- You can only use this feature if you have permissions to the AMI and its
  associated root volume snapshot. You cannot use this feature with AWS Marketplace AMIs.
- You can only use an AMI without a product code only if the instance does not
  have a product code.
- The size of the AMI root volume block device mapping must be equal to or greater
  than the size of the original root volume. If the size of the AMI root volume block
  device mapping is smaller than the size of the original root volume, the request fails.
- The instance identity documents for the instance are automatically updated.
- If the instance supports NitroTPM, the NitroTPM data for the instance is reset and
  new keys are generated.

You can choose whether to keep the original root volume after the root volume replacement
process has completed. If you choose delete the original root volume after the replacement
process completes, the original root volume is automatically deleted and becomes unrecoverable.
If you choose to keep the original root volume after the process completes, the volume remains
provisioned in your account; you must manually delete the volume when you no longer need it.

The root volume replacement task transitions through the following states:

- `pending` — The replacement volume is being created.
- `in-progress` — The original volume is being detached and the replacement
  volume is being attached.
- `succeeded` — The replacement volume has been successfully
  attached to the instance and the instance is available.
- `failing` — The replacement task is in the process of failing.
- `failed` — The replacement task has failed, but the root
  volume is still attached.
- `failing-detached` — The replacement task is in the process of
  failing and the instance might not have a root volume attached.
- `failed-detached` — The replacement task has failed and the
  instance doesn't have a root volume attached.

If the root volume replacement task fails, the instance is rebooted and the original root
volume remains attached to the instance.

## Considerations

Before you begin, consider the following.

###### Requirements

- The instance must be in the `running` state.
- The instance is automatically rebooted during the process. The contents of the memory
  (RAM) is erased during the reboot. No manual reboots are required.
- You can't replace the root volume if it is an instance store volume. Only instances
  with Amazon EBS root volumes are supported.
- You can replace the root volume for all virtualized instance types and EC2 Mac bare
  metal instances. No other bare metal instance types are supported.
- You can only use snapshots that were created directly from the instance's current
  or previous root volumes.
- If your account is enabled for Amazon EBS encryption by default in the current Region,
  the replacement root volume created by the root volume replacement task is always
  encrypted, regardless of the encryption status of the specified snapshot or the root
  volume of the specified AMI.

###### Encryption outcomes

The following table summarizes the possible encryption outcomes.

|                                                                | Original root volume | Specified snapshot or AMI | Encryption by default | Replacement root volume                                                                                                                                                                                                                                                    | Encryption key used for replacement root volume |
| -------------------------------------------------------------- | -------------------- | ------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Restore replacement root volume to<br>initial launch state** | Encrypted            | Not applicable            | Not considered        | Encrypted                                                                                                                                                                                                                                                                  | Same KMS key as original root volume            |
| Unencrypted                                                    | Not applicable       | Disabled                  | Unencrypted           | Not applicable                                                                                                                                                                                                                                                             |
| Unencrypted                                                    | Not applicable       | Enabled                   | Encrypted             | Account's default KMS key for Amazon EBS encryption                                                                                                                                                                                                                        |
| **Restore replacement root volume from snapshot or AMI**       | Encrypted            | Unencrypted               | Not considered        | Encrypted                                                                                                                                                                                                                                                                  | Same KMS key as original root volume            |
| Encrypted                                                      | Encrypted            | Not considered            | Encrypted             | Same KMS key as original root volume                                                                                                                                                                                                                                       |
| Unencrypted                                                    | Unencrypted          | Disabled                  | Unencrypted           | Not applicable                                                                                                                                                                                                                                                             |
| Unencrypted                                                    | Unencrypted          | Enabled                   | Encrypted             | Account's default KMS key for Amazon EBS encryption                                                                                                                                                                                                                        |
| Unencrypted                                                    | Encrypted            | Not considered            | Encrypted             | If the AMI or snapshot is owned by the account, the replacement volume is encrypted<br>with the AMI or snapshot’s KMS key. If AMI or snapshot is shared with the account,<br>replacement volume is encrypted with the account's default KMS key for Amazon EBS encryption. |

## Replace a root volume

When you replace the root volume for an instance, a _root volume replacement
task_ is created. You can use the root volume replacement task to monitor the
progress and outcome of the replacement process.

Console

###### To replace the root volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select the instance for which to replace the root volume and choose
   **Actions**, **Monitor and troubleshoot**,
   **Replace root volume**.

###### Note

The **Replace root volume** action is disabled if the selected
instance is not in the `running` state. 4. For **Restore**, choose one of the following options:

    * **Launch state** – Restore the replacement root
     volume from the snapshot that was used to create the current root
     volume.
    * **Snapshot** – Restore the replacement root volume to
     the snapshot that you specify. For **Snapshot**, select the
     snapshot to use.
    * **Image** – Restore the replacement root volume using
     the AMI that you specify. For **Image**, select the AMI to use.

5. (Optional) For **Volume initialization rate**, you can specify the Amazon EBS Provisioned Rate for Volume Initialization
   (volume initialization rate), in MiB/s, at which the snapshot blocks are to be downloaded from Amazon S3 to the volume. For
   more information, see [Use an Amazon EBS Provisioned Rate for Volume Initialization](../../../ebs/latest/userguide/initalize-volume.md#volume-initialization-rate "../../../ebs/latest/userguide/initalize-volume.md#volume-initialization-rate"). To use the default initialization rate
   or fast snapshot restore (if it is enabled for the selected snapshot), don't specify a rate.
6. (Optional) To delete the root volume that you are replacing, select
   **Delete replaced root volume**.
7. Choose **Create replacement task**.
8. To monitor the replacement task, choose the **Storage** tab for
   the instance and expand **Recent root volume replacement tasks**.

AWS CLI

###### To restore the replacement root volume to the launch state

Use the [create-replace-root-volume-task](../../../cli/latest/reference/ec2/create-replace-root-volume-task.md "../../../cli/latest/reference/ec2/create-replace-root-volume-task.md") command. For `--instance-id`, specify the ID of the instance
for which to replace the root volume. Omit the `--snapshot-id` and `--image-id` parameters.
To delete the original root volume after it has been replaced, include `--delete-replaced-root-volume`
and specify `true`. To specify the volume initialization rate at which the snapshot blocks are
downloaded from Amazon S3 to the volume, for `--volume-initialization-rate`, specify a value between
`100` and `300` MiB/s.

```
aws ec2 create-replace-root-volume-task \
--instance-id `i-1234567890abcdef0` \
--delete-replaced-root-volume \
--volume-initialization-rate `150`
```

###### To restore the replacement root volume to a specific snapshot

Use the [create-replace-root-volume-task](../../../cli/latest/reference/ec2/create-replace-root-volume-task.md "../../../cli/latest/reference/ec2/create-replace-root-volume-task.md")
command. For `--instance-id`, specify the ID of the instance for which to replace the root volume.
For `--snapshot-id`, specify the ID of the snapshot to use. To delete the original root volume
after it has been replaced, include `--delete-replaced-root-volume` and specify `true`.
To specify the volume initialization rate at which the snapshot blocks are downloaded from Amazon S3 to the volume,
for `--volume-initialization-rate`, specify a value between `100` and `300`
MiB/s.

```
aws ec2 create-replace-root-volume-task \
--instance-id `i-1234567890abcdef0` \
--snapshot-id `snap-9876543210abcdef0` \
--delete-replaced-root-volume \
--volume-initialization-rate `150`
```

###### To restore the replacement root volume using an AMI

Use the [create-replace-root-volume-task](../../../cli/latest/reference/ec2/create-replace-root-volume-task.md "../../../cli/latest/reference/ec2/create-replace-root-volume-task.md") command. For `--instance-id`, specify the ID of the instance
for which to replace the root volume. For `--image-id`, specify the ID of the AMI to use. To delete
the original root volume after it has been replaced, include `--delete-replaced-root-volume` and
specify `true`. To specify the volume initialization rate at which the snapshot blocks are
downloaded from Amazon S3 to the volume, for `--volume-initialization-rate`, specify a value between
`100` and `300` MiB/s.

```
aws ec2 create-replace-root-volume-task \
--instance-id `i-1234567890abcdef0` \
--image-id `ami-09876543210abcdef` \
--delete-replaced-root-volume \
--volume-initialization-rate `150`
```

###### To view the status of a root volume replacement task

Use the [describe-replace-root-volume-tasks](../../../cli/latest/reference/ec2/describe-replace-root-volume-tasks.md "../../../cli/latest/reference/ec2/describe-replace-root-volume-tasks.md") command and specify the IDs of the
root volume replacement tasks to view.

```
aws ec2 describe-replace-root-volume-tasks \
    --replace-root-volume-task-ids `replacevol-1234567890abcdef0` \
    --query ReplaceRootVolumeTasks[].TaskState
```

The following is example output.

```
[
    "succeeded"
]
```

Alternatively, specify the `instance-id` filter to filter the results by instance.

```
`$` aws ec2 describe-replace-root-volume-tasks \
    --filters Name=instance-id,Values=`i-1234567890abcdef0`
```

PowerShell

###### To restore the replacement root volume to the launch state

Use the [New-EC2ReplaceRootVolumeTask](../../../powershell/latest/reference/items/New-EC2ReplaceRootVolumeTask.md "../../../powershell/latest/reference/items/New-EC2ReplaceRootVolumeTask.md")
command. For `-InstanceId`, specify the ID of the instance for which to replace the root volume. Omit
the `-SnapshotId` and `-ImageId` parameters. To delete the original root volume after it has
been replaced, include `-DeleteReplacedRootVolume` and specify `$true`. To specify the volume initialization rate
at which the snapshot blocks are downloaded from Amazon S3 to the volume, for
`-VolumeInitializationRate`, specify a value between `100` and `300` MiB/s.

```
New-EC2ReplaceRootVolumeTask `
    -InstanceId `i-1234567890abcdef0` `
    -VolumeInitializationRate `150` `
    -DeleteReplacedRootVolume $true
```

###### To restore the replacement root volume to a specific snapshot

Use the [New-EC2ReplaceRootVolumeTask](../../../powershell/latest/reference/items/New-EC2ReplaceRootVolumeTask.md "../../../powershell/latest/reference/items/New-EC2ReplaceRootVolumeTask.md")
command. For `--InstanceId`, specify the ID of the instance for which to replace the root volume. For
`-SnapshotId`, specify the ID of the snapshot to use. To delete the original root volume after it has
been replaced, include `-DeleteReplacedRootVolume` and specify `$true`. To specify the
volume initialization rate at which the snapshot blocks are downloaded from Amazon S3 to the volume, for
`-VolumeInitializationRate`, specify a value between `100` and `300` MiB/s.

```
New-EC2ReplaceRootVolumeTask `
    -InstanceId `i-1234567890abcdef0` `
    -SnapshotId `snap-9876543210abcdef0` `
    -VolumeInitializationRate `150` `
    -DeleteReplacedRootVolume $true
```

###### To restore the replacement root volume using an AMI

Use the [New-EC2ReplaceRootVolumeTask](../../../powershell/latest/reference/items/New-EC2ReplaceRootVolumeTask.md "../../../powershell/latest/reference/items/New-EC2ReplaceRootVolumeTask.md")
command. For `-InstanceId`, specify the ID of the instance for which to replace the root volume. For
`-ImageId`, specify the ID of the AMI to use. To delete the original root volume after it has been
replaced, include `-DeleteReplacedRootVolume` and specify `$true`. To specify the volume initialization rate
at which the snapshot blocks are downloaded from Amazon S3 to the volume, for
`-VolumeInitializationRate`, specify a value between `100` and `300` MiB/s.

```
New-EC2ReplaceRootVolumeTask `
    -InstanceId `i-1234567890abcdef0` `
    -ImageId `ami-0abcdef1234567890` `
    -VolumeInitializationRate `150` `
    -DeleteReplacedRootVolume $true
```

###### To view the status of a root volume replacement task

Use the [Get-EC2ReplaceRootVolumeTask](../../../powershell/latest/reference/items/Get-EC2ReplaceRootVolumeTask.md "../../../powershell/latest/reference/items/Get-EC2ReplaceRootVolumeTask.md")
command and specify the IDs of the root volume replacement tasks to view.

```
(Get-EC2ReplaceRootVolumeTask `
    -ReplaceRootVolumeTaskIds `replacevol-1234567890abcdef0`).TaskState.Value
```

The following is example output.

```
Succeeded
```

Alternatively, specify the `instance-id` filter to filter the results by instance.

```
`PS C:\>` Get-EC2ReplaceRootVolumeTask -Filters @{Name = 'instance-id'; Values = '`i-1234567890abcdef0`'} | Format-Table
```
