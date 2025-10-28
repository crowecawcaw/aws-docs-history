# Best practices for Volume Gateway

This section contains the following topics, which provide information about the best
practices for working with gateways, local disks, snapshots, and data. We recommend that you
familiarize yourself with the information outlined in this section, and attempt to follow these
guidelines in order to avoid problems with your AWS Storage Gateway. For additional guidance on diagnosing
and solving common issues you might encounter with your deployment, see [Troubleshooting your gateway](troubleshooting-gateway-issues.md "troubleshooting-gateway-issues.md").

###### Topics

- [Best practices: recovering your data](#recover-data-from-gateway "#recover-data-from-gateway")
- [Cleaning up unnecessary resources](#cleanup "#cleanup")
- [Reducing the amount of billed storage on a volume](#reduce-bill-volume "#reduce-bill-volume")

## Best practices: recovering your data

Although it is rare, your gateway might encounter an unrecoverable failure. Such a failure
can occur in your virtual machine (VM), the gateway itself, the local storage, or elsewhere.
If a failure occurs, we recommend that you follow the instructions in the appropriate
section following to recover your data.

###### Important

Storage Gateway doesn’t support recovering a gateway VM from a snapshot that is created by
your hypervisor or from your Amazon EC2 Amazon Machine Image (AMI). If your gateway VM
malfunctions, activate a new gateway and recover your data to that gateway using the
instructions following.

###### Topics

- [Recovering from an unexpected virtual
  machine shutdown](#recover-from-gateway-shutdown "#recover-from-gateway-shutdown")
- [Recovering your data from a malfunctioning
  gateway or VM](#recover-from-gateway "#recover-from-gateway")
- [Recovering your data from an irrecoverable
  volume](#recover-from-volume "#recover-from-volume")
- [Recovering your data from a malfunctioning
  cache disk](#recover-from-cahe-disk "#recover-from-cahe-disk")
- [Recovering your data from a corrupted file
  system](#recover-corrupt-file-system "#recover-corrupt-file-system")
- [Recovering your data from an inaccessible data
  center](#disaster-recovery "#disaster-recovery")

### Recovering from an unexpected virtual

machine shutdown

If your VM shuts down unexpectedly, for example during a power outage, your gateway
becomes unreachable. When power and network connectivity are restored, your gateway
becomes reachable and starts to function normally. Following are some steps you can take
at that point to help recover your data:

- If an outage causes network connectivity issues, you can troubleshoot the
  issue. For information about how to test network connectivity, see [Testing your gateway
  connection to the internet](MaintenanceTestGatewayConnectivity-common.md "MaintenanceTestGatewayConnectivity-common.md").
- For cached volumes setups, when your gateway becomes reachable, your volumes go
  into BOOTSTRAPPING status. This functionality ensures that your locally stored
  data continues to be synchronized with AWS. For more information on this
  status, see [Understanding Volume Statuses and
  Transitions](StorageVolumeStatuses.md "StorageVolumeStatuses.md").
- If your gateway malfunctions and issues occur with your volumes or tapes as a
  result of an unexpected shutdown, you can recover your data. For information
  about how to recover your data, see the sections following that apply to your
  scenario.

### Recovering your data from a malfunctioning

gateway or VM

If your gateway or virtual machine malfunctions, you can recover data
that has been uploaded to AWS and stored on a volume in Amazon S3. For cached volumes
gateways, you recover data from a recovery snapshot. For stored volumes gateways, you
can recover data from your most recent Amazon EBS snapshot of the volume. For Tape Gateways,
you recover one or more tapes from a recovery point to a new Tape Gateway.

If your cached volumes gateway becomes unreachable, you can use the
following steps to recover your data from a recovery snapshot:

1. In the AWS Management Console, choose the malfunctioning gateway, choose the volume you
   want to recover, and then create a recovery snapshot from it.
2. Deploy and activate a new Volume Gateway. Or, if you have an existing
   functioning Volume Gateway, you can use that gateway to recover your volume
   data.
3. Find the snapshot you created and restore it to a new volume on the
   functioning gateway.
4. Mount the new volume as an iSCSI device on your on-premises application
   server.

For detailed information on how to recover cached volumes data from a
recovery snapshot, see [Your Cached Gateway is Unreachable
And You Want to Recover Your Data](troubleshoot-volume-issues.md#RecoverySnapshotTroubleshooting "troubleshoot-volume-issues.md#RecoverySnapshotTroubleshooting").

### Recovering your data from an irrecoverable

volume

If the status of your volume is IRRECOVERABLE, you can no longer use this
volume.

For stored volumes, you can retrieve your data from the irrecoverable volume to a new
volume by using the following steps:

1. Create a new volume from the disk that was used to create the irrecoverable
   volume.
2. Preserve existing data when you are creating the new volume.
3. Delete all pending snapshot jobs for the irrecoverable volume.
4. Delete the irrecoverable volume from the gateway.

For cached volumes, we recommend using the last recovery point to clone a new
volume.

For detailed information about how to retrieve your data from an irrecoverable volume
to a new volume, see [The Console Says
That Your Volume Is Irrecoverable](troubleshoot-volume-issues.md#troubleshoot-volume-issues.VolumeIrrecoverable "troubleshoot-volume-issues.md#troubleshoot-volume-issues.VolumeIrrecoverable").

### Recovering your data from a malfunctioning

cache disk

If your cache disk encounters a failure, we recommend you use the following steps to
recover your data depending on your situation:

- If the malfunction occurred because a cache disk was removed from your host,
  shut down the gateway, re-add the disk, and restart the gateway.
- If the cache disk is corrupted or not accessible, shut down the gateway, reset
  the cache disk, reconfigure the disk for cache storage, and restart the
  gateway.

### Recovering your data from a corrupted file

system

If your file system gets corrupted, you can use the `fsck`
command to check your file system for errors and repair it. If you can repair the file
system, you can then recover your data from the volumes on the file system, as described
following:

1. Shut down your virtual machine and use the Storage Gateway Management Console to
   create a recovery snapshot. This snapshot represents the most current data
   stored in AWS.

###### Note

You use this snapshot as a fallback if your file system can't be repaired
or the snapshot creation process can't be completed successfully.

For information about how to create a recovery snapshot, see [Your Cached Gateway is Unreachable
And You Want to Recover Your Data](troubleshoot-volume-issues.md#RecoverySnapshotTroubleshooting "troubleshoot-volume-issues.md#RecoverySnapshotTroubleshooting"). 2. Use the `fsck` command to check your file system for
errors and attempt a repair. 3. Restart your gateway VM. 4. When your hypervisor host starts to boot up, press and hold down shift key to
enter the grub boot menu. 5. From the menu, press `e` to edit. 6. Choose the kernel line (the second line), and then press
`e` to edit. 7. Append the following option to the kernel command line:
`init=/bin/bash`. Use a space to separate the previous
option from the option you just appended. 8. Delete both `console=` lines, making sure to delete all values
following the `=` symbol, including those separated by commas. 9. Press `Return` to save the changes. 10. Press `b` to boot your computer with the modified kernel
option. Your computer will boot to a `bash#` prompt. 11. Enter `/sbin/fsck -f
 `/dev/sda1``to run this command
 manually from the prompt, to check and repair your file system. If the command
 does not work with the`/dev/sda1`path, you can use
`lsblk`to determine the root filesystem device for
`/` and use that path instead. 12. When the file system check and repair is complete, reboot the instance. The
grub settings will revert to the original values, and the gateway will boot up
normally. 13. Wait for snapshots that are in-progress from the original gateway to complete,
and then validate the snapshot data.

You can continue to use the original volume as-is, or you can create a new gateway
with a new volume based on either the recovery snapshot or the completed snapshot.
Alternatively, you can create a new volume from any of your completed snapshots from
this volume.

### Recovering your data from an inaccessible data

center

If your gateway or data center becomes inaccessible for some reason, you can recover
your data to another gateway in a different data center or recover to a gateway hosted
on an Amazon EC2 instance. If you don't have access to another data center, we recommend
creating the gateway on an Amazon EC2 instance. The steps you follow depends on the gateway
type you are covering the data from.

###### To recover data from a Volume Gateway in an inaccessible data center

1. Create and activate a new Volume Gateway on an Amazon EC2 host. For more
   information, see [Deploy a customized Amazon EC2 instance for
   Volume Gateway](ec2-gateway-common.md "ec2-gateway-common.md").

###### Note

Gateway stored volumes can't be hosted on Amazon EC2 instance. 2. Create a new volume and choose the EC2 gateway as the target gateway. For more
information, see [Creating a storage volume](GettingStartedCreateVolumes.md "GettingStartedCreateVolumes.md").

Create the new volume based on an Amazon EBS snapshot or clone from last recovery
point of the volume you want to recover.

If your volume is based on a snapshot, provide the snapshot id.

If you are cloning a volume from a recovery point, choose the source
volume.

## Cleaning up unnecessary resources

If you created your gateway as an example exercise or a test, consider cleaning up to avoid
incurring unexpected or unnecessary charges.

###### To clean up resources you don't need

1. Delete any snapshots. For instructions, see [Deleting snapshots of your storage volumes](DeletingASnapshot.md "DeletingASnapshot.md").
2. Unless you plan to continue using the gateway, delete it. For more information, see [Deleting your gateway and removing associated
   resources](deleting-gateway-common.md "deleting-gateway-common.md").
3. Delete the Storage Gateway VM from your on-premises host. If you created your gateway on an Amazon EC2
   instance, terminate the instance.

## Reducing the amount of billed storage on a volume

Deleting files from your file system doesn't necessarily delete data from the underlying
block device or reduce the amount of data stored on your volume. If you want to reduce the amount
of billed storage on your volume, we recommend overwriting your files with zeros to compress the
storage to a negligible amount of actual storage. Storage Gateway charges for volume usage based on
compressed storage.

###### Note

If you use a delete tool that overwrites the data on your volume with random data, your
usage will not be reduced. This is because the random data is not compressible.
