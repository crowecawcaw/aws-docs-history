# Copy an Amazon EBS volume

You can create an instant point-in-time copy of an Amazon EBS volume within the same
Availability Zone. A volume copy begins as a crash-consistent, point in time copy of
the source volume. It includes all the data blocks written to the source volume at the
time the volume copy initialization begins. The volume copy gets its own unique volume
ID. Volume copies are created immediately and can be attached to an Amazon EC2 instance
once it reaches the `available` state. Using volume copies, you can quickly
copy your production data for test and development environments.

## Initialization

Volume copies are initialized after creation. During initialization, the data blocks
are copied from the source volume and written to the volume copy in the background. The
volume remains in the `initializing` state until initialization completes.

###### Performance during initialization

Copy operations do not affect the performance of the source volume. You can continue
using the source volume normally during the copy process. Copied volumes can be accessed
instantly without waiting for the data to be copied from the source volume. Volume copies
provide instant access to data with single-digit millisecond latency, however, actual
latency might vary depending on the volume type. During initialization, the volume copy
delivers **baseline performance** equal to the lowest of the
following three values:

- 3,000 IOPS and 125 MiB/s
- The provisioned performance for the **source volume**
- The provisioned performance for the **volume copy**

The volume copy can exceed the baseline performance when the following criteria are met:

1. Both the source volume and volume copy are provisioned with more than 3,000 IOPS and
   125 MiB/s.
2. The source volume has unutilized performance capacity (driven performance is less than
   provisioned performance)

For example, if the source volume is provisioned with 10,000 IOPS and your workload is
currently driving only 5,000 IOPS, and the volume copy is provisioned with 10,000 IOPS, the
volume copy can achieve performance higher than the 3,000 IOPS baseline performance during
initialization by using the source volume's unutilized 5,000 IOPS.

###### Initialization duration

The time it takes to initialize a volume copy depends on the size of the block data
written to the source volume at the time of creating the volume copy. Volume copies are
initialized on a best-effort basis, with the following general guidelines. For the first
1 TiB of data blocks, volume initialization takes up to 6 hours. For each subsequent 1
TiB of data blocks up to 16 TiB, initialization takes 1.2 hours per TiB. For written data
larger than 16 TiB, initialization takes 24 hours.

###### Monitor initialization progress

You can monitor the initialization progress using the [describe-volume-status](../../../cli/latest/reference/ec2/describe-volume-status.md "../../../cli/latest/reference/ec2/describe-volume-status.md")
AWS CLI command or Amazon EventBridge. For more information, see [Monitor the status of Amazon EBS
volume initialization](ebs-initialize-monitor.md "ebs-initialize-monitor.md").

## Encryption

Copies of encrypted volumes are automatically encrypted with the same KMS key as
the source volume. You can't copy unencrypted volumes.

## Considerations

- You can create copies from encrypted source volumes only. You can't create copies from
  unencrypted source volumes.
- You can create only one volume copy from a source volume at a time. You can create
  subsequent copies of the same source volume only once the previous volume copy has been
  fully initialized.
- You can have a maximum of 5 in-progress volume copies per Region. If you exceed this quota,
  you get the `CopyVolumesLimitExceeded` error. You can [request a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")
  if needed.
- The volume copy must be created in the same Availability Zone as the source volume.
- The size of the volume copy must be equal to or greater than the size of the source volume.
- You can't copy a volume copy while it is being created or initialized.
- To create a volume copy, the source volume must be in the `available` or
  `in-use` state, and volume modifications must be in the `completed`
  or `optimizing` state.
- Volume copies are subject to the same account and Regional storage and IOPS quotas
  as regular Amazon EBS volumes. For more information, see [Amazon EBS quotas](../../../general/latest/gr/ebs-service.md#limits_ebs "../../../general/latest/gr/ebs-service.md#limits_ebs").
- If you delete the source volume while the copy operation is in progress, the copy operation
  still completes.
- Tags assigned to the source volume are not assigned to the volume copy.
- You can't create copies from volumes on Outposts or in Wavelength Zones.

## Pricing

When you initiate volume copy operation, you are charged a one-time fee per GiB of data
blocks written to the volume copy. After the volume copy is created, it is charged the same
way as any other Amazon EBS volume in your account. For more information, see [Amazon EBS pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

## Copy a volume

Use one of the following methods to copy an Amazon EBS volume.

Console

###### To copy a volume

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Volumes**.
3. Select the volume to copy and choose **Actions**,
   **Copy volume**.
4. For **Volume type**, choose the volume type for the copy.
   The default volume type is **gp3**.
5. For **Size**, enter the size for the volume copy, in GiBs.
   The size must be equal to or greater than the size of the source volume.
6. (_`io1`, `io2`, and `gp3` only_) For **IOPS**,
   enter the maximum number of input/output operations per second (IOPS) for the
   volume copy.
7. (_`gp3` only_) For **Throughput**,
   enter the throughput for the volume copy, in MiB/s.
8. (_`io1` and `io2` only_) To enable the volume copy for
   Amazon EBS Multi-Attach, select **Enable Multi-Attach**.
9. (_Optional_) To assign custom tags to the volume copy,
   in the **Tags** section, choose **Add tag**,
   and then enter a tag key and value pair.
10. Choose **Copy volume**.
11. The copied volume enters the `creating` state and then transitions
    to `available` shortly after. You can then attach it to an Amazon EC2 instance
    in the same Availability Zone.

AWS CLI

###### To copy a volume

Use the [copy-volumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-volumes.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-volumes.html")
command.

The following example creates a volume copy of `vol-01234567890abcdef` with the
`gp3` volume type, a size of `100` GiB, and throughput of
`250` MiB/s.

```
aws ec2 copy-volumes \
--source-volume-id `vol-01234567890abcdef` \
--volume-type `gp3` \
--size `100` \
--throughput `250`
```

PowerShell

###### To copy a volume

Use the [Copy-EC2Volume](../../../powershell/latest/reference/items/Copy-EC2Volume.md "../../../powershell/latest/reference/items/Copy-EC2Volume.md")
cmdlet.

The following example creates a volume copy of `vol-01234567890abcdef` with the
`gp3` volume type, a size of `100` GiB, and throughput of
`250` MiB/s.

```
Copy-EC2Volume `
-SourceVolumeId `vol-01234567890abcdef` `
-VolumeType `gp3` `
-Size `100` `
-Throughput `250`
```
