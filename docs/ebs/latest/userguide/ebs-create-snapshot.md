# Create a snapshot of an EBS volume

You can create a single snapshot of a single volume. Alternatively, to automate snapshot
creation, use [Amazon Data Lifecycle Manager](snapshot-lifecycle.md "snapshot-lifecycle.md") or [AWS Backup](../../../aws-backup/latest/devguide/multi-volume-crash-consistent.md "../../../aws-backup/latest/devguide/multi-volume-crash-consistent.md"). To create
snapshots of all the volumes for an EC2 instance, use [multi-volume snapshots](ebs-create-snapshots.md "ebs-create-snapshots.md").

Console

###### To create a snapshot

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**,
   **Create snapshot**.
3. For **Resource type**, choose **Volume**.
4. For **Volume ID**, select the volume from which to create the
   snapshot. The **Encryption** field indicates the volume and resulting
   snapshot's encryption status. It can't be modified.
5. (_Optional_) For **Description**, enter a brief
   description for the snapshot.
6. If the volume is on an Outpost or in a Local Zone, the **Snapshot destination**
   field appears. Do one of the following:
   - If the volume is in a Local Zone, choose **Local Zone** to create
     the snapshot in the same Local Zone, or choose **AWS Region** to create
     the snapshot in the parent Region of the Local Zone.
   - If the volume is on an Outpost, choose **AWS Outpost**, to create
     the snapshot on the same Outpost, or choose **AWS Region** to create the
     snapshot in the parent Region of the Outpost.

###### Note

If the volume is in a Region, the **Snapshot destination** does not
appear. The snapshot is automatically created in the same Region as the volume. 7. (_Optional_) To assign custom tags to the snapshot, in the
**Tags** section, choose **Add tag**, and then
enter the key-value pair. You can add up to 50 tags. 8. Choose **Create snapshot**.

AWS CLI

###### To create a snapshot

Use the [create-snapshot](../../../cli/latest/reference/ec2/create-snapshot.md "../../../cli/latest/reference/ec2/create-snapshot.md")
command.

```
aws ec2 create-snapshot  \
    --volume-id `vol-01234567890abcdef` \
    --description "Snapshot of the root volume for i-1234567890abcdef0"
```

PowerShell

###### To create a snapshot

Use the [New-EC2Snapshot](../../../powershell/latest/reference/items/New-EC2Snapshot.md "../../../powershell/latest/reference/items/New-EC2Snapshot.md")
cmdlet.

```
New-EC2Snapshot `
    -VolumeId `vol-01234567890abcdef` `
    -Description "Snapshot of the root volume for i-1234567890abcdef0"
```
