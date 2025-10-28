# Create multi-volume EBS snapshots from an EC2 instance

By default, when you create multi-volume snapshots from an Amazon EC2 instance, Amazon EBS creates
snapshots of all the Amazon EBS volumes that are attached to the instance. However, you can
choose to exclude the root volume, or specific data volumes if needed.

###### Tip

We recommend that you tag your multi-volume snapshots so that it's easy to identify and
manage them collectively. You can also copy the tags from the source volumes to the corresponding
snapshots to set the snapshot metadata, such as access policies, attachment information, and
cost allocation, to match the source volume.

###### Considerations for multi-volume snapshots

- If all of the snapshots complete successfully, a `createSnapshots` CloudWatch event
  with a result of `succeeded` is sent to your AWS account. If any one snapshot in
  the multi-volume snapshot set fails, all of the other snapshots enter the `error`
  state and a `createSnapshots` CloudWatch event with a result of `failed` is
  sent to your account. For more information, see [Create snapshots (createSnapshots)](ebs-cloud-watch-events.md#create-snapshots-complete "ebs-cloud-watch-events.md#create-snapshots-complete").
- Multi-volume snapshots support up to 128 Amazon EBS volumes attached to an instance, including the
  root volume and up to 127 data volumes.
- Each snapshot in the multi-volume snapshot set is an individual snapshot that can be used
  in the same way, and that supports the same features, as an individual snapshot.
- You can take application-consistent snapshots of all the Amazon EBS volumes attached to an Amazon EC2 Windows
  instance using [AWS Systems Manager command documents](../../../AWSEC2/latest/UserGuide/create-vss-snapshots-ssm.md "../../../AWSEC2/latest/UserGuide/create-vss-snapshots-ssm.md").

Console

###### To create multi-volume snapshots

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Snapshots**, **Create snapshot**.
3. For **Resource type**, choose **Instance**.
4. For **Description**, enter a brief description for the snapshots.
   This description is applied to all of the snapshots.
5. If the instance is on an Outpost or in a Local Zone, the **Snapshot destination**
   field appears. Do one of the following:
   - If the instance is in a Local Zone, choose **Local Zone** to create
     the snapshots in the same Local Zone, or choose **AWS Region** to create
     the snapshots in the parent Region of the Local Zone.
   - If the instance is on an Outpost, choose **AWS Outpost**, to create
     the snapshots on the same Outpost, or choose **AWS Region** to create the
     snapshots in the parent Region of the Outpost.

###### Note

If the instance is in a Region, the **Snapshot destination** does not
appear. The snapshot is automatically created in the same Region as the instance. 6. (_Optional_) To exclude the instance's root volume, select
**Exclude root volume**. 7. (_Optional_) To exclude data volumes, select **Exclude
specific data volumes**. The **Attached data volumes** section
lists all of the data volumes that are currently attached to the selected instance.

Select the data volumes to exclude. Only the volumes that remain unselected will be
included in the multi-volume snapshot set. 8. (_Optional_) To automatically copy tags from the source volumes to
the corresponding snapshots, for **Copy tags from source volume**, select
**Copy tags**. 9. (_Optional_) To assign additional custom tags to the snapshots, in
the **Tags** section, choose **Add tag**, and then
enter the key-value pair. You can add up to 50 tags. 10. Choose **Create snapshot**.

AWS CLI

###### To create multi-volume snapshots

Use the [create-snapshots](../../../cli/latest/reference/ec2/create-snapshots.md "../../../cli/latest/reference/ec2/create-snapshots.md") command.

```
aws ec2 create-snapshots \
    --instance-specification InstanceId=`i-1234567890abcdef0` \
    --description "from a multi-volume snapshot of i-1234567890abcdef0"
```

To exclude the root volume, add the following to the `--instance-specification`
option.

```
ExcludeBootVolume=true
```

To exclude a data volume, add the following to the `--instance-specification`
option.

```
ExcludeDataVolumeIds=`vol-01234567890abcdef`
```

PowerShell

###### To create multi-volume snapshots

Use the [New-EC2SnapshotBatch](../../../powershell/latest/reference/items/New-EC2SnapshotBatch.md "../../../powershell/latest/reference/items/New-EC2SnapshotBatch.md")
cmdlet.

```
New-EC2SnapshotBatch `
    -InstanceSpecification_InstanceId `i-1234567890abcdef0` `
    -Description "from a multi-volume snapshot of i-1234567890abcdef0"
```

To exclude the root volume, add the following parameter.

```
-InstanceSpecification_ExcludeBootVolume $true
```

To exclude data volumes, add the following parameter.

```
-InstanceSpecification_ExcludeDataVolumes "`vol-01234567890abcdef`"
```
