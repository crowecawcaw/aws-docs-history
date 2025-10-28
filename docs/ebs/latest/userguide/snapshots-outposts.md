# Amazon EBS local snapshots on Outposts

Amazon EBS snapshots are a point-in-time copy of your EBS volumes.

By default, snapshots of EBS volumes on an AWS Outpost are stored in Amazon S3 in the Region of the
Outpost. You can also use Amazon EBS local snapshots on Outposts to store snapshots of volumes on an
Outpost locally in Amazon S3 on the Outpost itself. This ensures that the snapshot data resides on
the Outpost, and on your premises. In addition, you can use AWS Identity and Access Management (IAM) policies and
permissions to set up data residency enforcement policies to ensue that snapshot data does
not leave the Outpost. This is especially useful if you reside in a country or region that is not
yet served by an AWS Region and that has data residency requirements.

This topic provides information about working with Amazon EBS local snapshots on Outposts. For more
information about Amazon EBS snapshots and about working with snapshots in an AWS Region,
see [Amazon EBS snapshots](ebs-snapshots.md "ebs-snapshots.md").

For more information, see [AWS Outposts Family](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/") and the
[AWS Outposts Family Documentation](../../../outposts.md "../../../outposts.md").

###### Topics

- [Frequently asked questions](#faq "#faq")
- [Prerequisites](#prereqs "#prereqs")
- [Considerations](#considerations "#considerations")
- [Controlling access with IAM](#iam "#iam")
- [Working with local snapshots](#using "#using")

## Frequently asked questions

**1. What are local snapshots?**

By default, Amazon EBS snapshots of volumes on an Outpost are stored in Amazon S3 in the Region of the
Outpost. If the Outpost is provisioned with S3 on Outposts, you can choose to store the
snapshots locally on the Outpost itself. Local snapshots are incremental, which means that
only the blocks of the volume that have changed after your most recent snapshot are saved.
You can use these snapshots to restore a volume on the same Outpost as the snapshot at any
time. For more information about Amazon EBS snapshots, see [Amazon EBS snapshots](ebs-snapshots.md "ebs-snapshots.md").

**2. Why should I use local snapshots?**

Snapshots are a convenient way of backing up your data. With local snapshots, all of your
snapshot data is stored locally on the Outpost. This means that it does not leave your premises.
This is especially useful if you reside in a country or region that is not yet served by an AWS Region
and that has residency requirements.

Additionally, using local snapshots can help to reduce the bandwidth used for communication
between the Region and the Outpost in bandwidth constrained environments.

**3. How do I enforce snapshot data residency on an Outpost?**

You can use AWS Identity and Access Management (IAM) policies to control the permissions that principals (AWS accounts, IAM
users, and IAM roles) have when working with local snapshots and to enforce data residency. You
can create a policy that prevents principals from creating snapshots from Outpost volumes and instances
and storing the snapshots in an AWS Region. Currently, copying snapshots and images from an Outpost
to a Region is not supported. For more information, see [Controlling access with IAM](#iam "#iam").

**4. Are multi-volume, crash-consistent local snapshots supported?**

Yes, you can create multi-volume, crash-consistent local snapshots from instances on an Outpost.

**5. How do I create local snapshots?**

You can create snapshots manually using the AWS Command Line Interface (AWS CLI) or the Amazon EC2 console. For
more information see, [Working with local snapshots](#using "#using"). You can
also automate the lifecycle of local snapshots using Amazon Data Lifecycle Manager. For more
information see, [Automate snapshots on an Outpost](#dlm "#dlm").

**6. Can I create, use, or delete local snapshots if my Outpost loses connectivity to its Region?**

No. The Outpost must have connectivity with its Region as the Region provides the access, authorization,
logging, and monitoring services that are critical for your snapshots' health. If there is no connectivity,
you can't create new local snapshots, create volumes or launch instances from existing local snapshots,
or delete local snapshots.

**7. How quickly is Amazon S3 storage capacity made available after deleting
local snapshots?**

Amazon S3 storage capacity becomes available within 72 hours after deleting local snapshots and the volumes that
reference them.

**8. How can I ensure that I do not run out of Amazon S3 capacity on my Outpost?**

We recommend that you use Amazon CloudWatch alarms to monitor your Amazon S3 storage capacity, and delete snapshots
and volumes that you no longer need to avoid running out of storage capacity. If you are using Amazon Data Lifecycle Manager to
automate the lifecycle of local snapshots, ensure that your snapshot retention policies do not retain
snapshots for longer than is needed.

**9. What happens if I run out of local Amazon S3 capacity on an Outpost?**

If you run out of local Amazon S3 capacity on an Outpost, Amazon Data Lifecycle Manager will not be able to successfully create local snapshots
on the Outpost. Amazon Data Lifecycle Manager will attempt to create the local snapshots on the Outpost, but the snapshots immediately
transition to the `error` state and they are eventually deleted by Amazon Data Lifecycle Manager. We recommend that
you use the `SnapshotsCreateFailed` Amazon CloudWatch metric to monitor your snapshot lifecycle policies
for snapshot creation failures. For more information, see [Monitor Data Lifecycle Manager policies using CloudWatch](monitor-dlm-cw-metrics.md "monitor-dlm-cw-metrics.md").

**10. Can I use local snapshots and AMIs backed by local snapshots with Spot Instances and Spot Fleet?**

No, you can't use local snapshots or AMIs backed by local snapshots to launch Spot Instances
or a Spot Fleet.

**11. Can I use local snapshots and AMIs backed by local snapshots with Amazon EC2 Auto Scaling?**

Yes, you can use local snapshots and AMIs backed by local snapshots to launch Auto Scaling
groups in a subnet that is on the same Outpost as the snapshots. The Amazon EC2 Auto Scaling group service-linked
role must have permission to use the KMS key used to encrypt the snapshots.

You can't use local snapshots or AMIs backed by local snapshots to launch Auto Scaling groups
in an AWS Region.

## Prerequisites

To store snapshots on an Outpost, you must have an Outpost that is provisioned with
S3 on Outposts. For more information about S3 on Outposts, see [S3 on Outposts](../../../AmazonS3/latest/s3-outposts/S3onOutposts.md "../../../AmazonS3/latest/s3-outposts/S3onOutposts.md") in the
_Amazon S3 on Outposts User Guide_.

## Considerations

Keep the following in mind when working with local snapshots.

- The Outpost must have connectivity to their AWS Region to use local snapshots.
- Snapshot metadata is stored in the AWS Region associated with the Outpost. This
  does not include any snapshot data.
- Snapshots stored on an Outpost are encrypted by default. Unencrypted snapshots are
  not supported. Snapshots that are created on an Outpost and snapshots that are
  copied to an Outpost are encrypted using the default KMS key for the Region
  or a different KMS key that you specify at the time of the request.
- When you create a volume on an Outpost from a local snapshot, you cannot re-encrypt
  the volume using a different KMS key. Volumes created from local snapshots must
  be encrypted using the same KMS key as the source snapshot.
- After you delete local snapshots from an Outpost, the Amazon S3 storage capacity used by
  the deleted snapshots becomes available within 72 hours. For more information, see
  [Delete local snapshots](#delete-snapshots "#delete-snapshots").
- You can't export local snapshots from an Outpost.
- You can't enable fast snapshot restore for local snapshots.
- EBS direct APIs are not supported with local snapshots.
- You can't copy local snapshots or AMIs from an Outpost to an AWS Region, from one
  Outpost to another, or within an Outpost. However, you can copy snapshots from an AWS
  Region to an Outpost. For more information, see [Copy snapshots from an AWS Region to an Outpost](#copy-snapshots "#copy-snapshots").
- When copying a snapshot from an AWS Region to an Outpost, the data is transferred
  over the service link. Copying multiple snapshots simultaneously could impact other
  services running on the Outpost.
- You can't share local snapshots.
- You must use IAM policies to ensure that your data residency requirements are met. For
  more information, see [Controlling access with IAM](#iam "#iam").
- Local snapshots are incremental backups. Only the blocks in the volume
  that have changed after your most recent snapshot are saved. Each local snapshot
  contains all of the information that is needed to restore your data (from the moment
  when the snapshot was taken) to a new EBS volume. For more information, see
  [How Amazon EBS snapshots work](how_snapshots_work.md "how_snapshots_work.md").
- You can’t use IAM policies to enforce data residency for **CopySnapshot**
  and **CopyImage** actions.

## Controlling access with IAM

You can use AWS Identity and Access Management (IAM) policies to control the permissions that principals (AWS accounts,
IAM users, and IAM roles) have when working with local snapshots. The following are example
policies that you can use to grant or deny permission to perform specific actions with
local snapshots.

###### Important

Copying snapshots and images from an Outpost to a Region is currently not supported. As
result, you currently can’t use IAM policies to enforce data residency for **CopySnapshot**
and **CopyImage** actions.

###### Topics

- [Enforce data residency for snapshots](#enforce-residency-snapshot "#enforce-residency-snapshot")
- [Prevent principals from deleting local snapshots](#deny-delete "#deny-delete")

### Enforce data residency for snapshots

The following example policy prevents all principals from creating snapshots from volumes
and instances on Outpost `arn:aws:outposts:us-east-1:123456789012:outpost/op-1234567890abcdef`
and storing the snapshot data in an AWS Region. Principals can still create local snapshots.
This policy ensures that all snapshots remain on the Outpost.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ec2:CreateSnapshot",
 "ec2:CreateSnapshots"
 ],
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*",
 "Condition": {
 "StringEquals": {
 "ec2:SourceOutpostArn": "`arn:aws:outposts:us-east-1:123456789012:outpost/op-1234567890abcdef0`"
 },
 "Null": {
 "ec2:OutpostArn": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateSnapshot",
 "ec2:CreateSnapshots"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Prevent principals from deleting local snapshots

The following example policy prevents all principals from deleting local
snapshots that are stored on Outpost `arn:aws:outposts:us-east-1:123456789012:outpost/op-1234567890abcdef0`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "ec2:DeleteSnapshot"
 ],
 "Resource": "arn:aws:ec2:us-east-1::snapshot/*",
 "Condition": {
 "StringEquals": {
 "ec2:OutpostArn": "`arn:aws:outposts:us-east-1:123456789012:outpost/op-1234567890abcdef0`"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteSnapshot"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Working with local snapshots

The following sections explain how to use local snapshots.

###### Topics

- [Rules for storing snapshots](#lineage "#lineage")
- [Create local snapshots from volumes on an Outpost](#create-snapshot "#create-snapshot")
- [Create AMIs from local snapshots](#ami "#ami")
- [Copy snapshots from an AWS Region to an Outpost](#copy-snapshots "#copy-snapshots")
- [Copy AMIs from an AWS Region to an Outpost](#copy-amis "#copy-amis")
- [Create volumes from local snapshots](#volumes "#volumes")
- [Launch instances from AMIs backed by local snapshots](#instances "#instances")
- [Delete local snapshots](#delete-snapshots "#delete-snapshots")
- [Automate snapshots on an Outpost](#dlm "#dlm")

### Rules for storing snapshots

The following rules apply to snapshot storage:

- If the most recent snapshot of a volume is stored on an Outpost, then all successive snapshots
  must be stored on the same Outpost.
- If the most recent snapshot of a volume is stored in an AWS Region, then all successive
  snapshots must be stored in the same Region. To start creating local snapshots from that
  volume, do the following:

      1. Create a snapshot of the volume in the AWS Region.
      2. Copy the snapshot to the Outpost from the AWS Region.
      3. Create a new volume from the local snapshot.
      4. Attach the volume to an instance on the Outpost.

  For the new volume on the Outpost, the next snapshot can be stored on the Outpost or in the
  AWS Region. All successive snapshots must then be stored in that same location.

- Local snapshots, including snapshots created on an Outpost and snapshots copied to an
  Outpost from an AWS Region, can be used only to create volumes on the same Outpost.
- If you create a volume on an Outpost from a snapshot in a Region, then all successive snapshots of
  that new volume must be in the same Region.
- If you create a volume on an Outpost from a local snapshot, then all successive snapshots of that
  new volume must be on the same Outpost.

### Create local snapshots from volumes on an Outpost

You can create local snapshots from volumes on your Outpost. You can choose
to store the snapshots on the same Outpost as the source volume, or in the Region
for the Outpost.

Local snapshots can be used to create volumes on the same Outpost only.

For more information, see [Create Amazon EBS snapshots](ebs-creating-snapshot.md "ebs-creating-snapshot.md")

### Create AMIs from local snapshots

You can create Amazon Machine Images (AMIs) using a combination of local snapshots and snapshots
that are stored in the Region of the Outpost. For example, if you have an Outpost in `us-east-1`,
you can create an AMI with data volumes that are backed by local snapshots on that Outpost, and a
root volume that is backed by a snapshot in the `us-east-1` Region.

###### Note

- You can't create AMIs that include backing snapshots stored across
  multiple Outposts.
- You can’t currently create AMIs directly from instances on an Outpost
  using **CreateImage** API or the Amazon EC2
  console for an Outpost.
- AMIs that are backed by local snapshots can be used to launch
  instances on the same Outpost only.

###### To create an AMI on an Outpost from snapshots in a Region

1. Copy the snapshots from the Region to the Outpost. For more information, see
   [Copy snapshots from an AWS Region to an Outpost](#copy-snapshots "#copy-snapshots").
2. Use the Amazon EC2 console or the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command to create the AMI using the snapshot copies on
   the Outpost. For more information, see [Creating an AMI from a snapshot](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot").

###### To create an AMI on an Outpost from an instance on an Outpost

1. Create snapshots from the instance on the Outpost and store the snapshots on the Outpost.
   For more information, see [Create Amazon EBS snapshots](ebs-creating-snapshot.md "ebs-creating-snapshot.md").
2. Use the Amazon EC2 console or the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command to create the AMI using the local snapshots. For
   more information, see [Creating an AMI from a snapshot](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot").

###### To create an AMI in a Region from an instance on an Outpost

1. Create snapshots from the instance on the Outpost and store the snapshots in the Region.
   For more information, see [Create local snapshots from volumes on an Outpost](#create-snapshot "#create-snapshot")
   or [Create Amazon EBS snapshots](ebs-creating-snapshot.md "ebs-creating-snapshot.md").
2. Use the Amazon EC2 console or the [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") command to create the AMI using the snapshot copies in the Region.
   For more information, see [Creating an AMI from a snapshot](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot").

### Copy snapshots from an AWS Region to an Outpost

You can copy snapshots from an AWS Region to an Outpost. You can do this only if the
snapshots are in the Region for the Outpost. If the snapshots are in a different Region,
you must first copy the snapshot to the Region for the Outpost, and then copy it from
that Region to the Outpost.

###### Note

You can't copy local snapshots from an Outpost to a Region, from one Outpost
to another, or within the same Outpost.

For more information, see [Copy an Amazon EBS snapshot](ebs-copy-snapshot.md "ebs-copy-snapshot.md").

### Copy AMIs from an AWS Region to an Outpost

You can copy AMIs from an AWS Region to an Outpost. When you copy an AMI from a Region
to an Outpost, all of the snapshots associated with the AMI are copied from the Region to the
Outpost.

You can copy an AMI from a Region to an Outpost only if the snapshots associated with the
AMI are in the Region for the Outpost. If the snapshots are in a different Region,
you must first copy the AMI to the Region for the Outpost, and then copy it from
that Region to the Outpost.

###### Note

You can't copy an AMI from an Outpost to a Region, from one Outpost to
another, or within an Outpost.

You can copy AMIs from a Region to an Outpost using the [copy-image](../../../cli/latest/reference/ec2/copy-image.md "../../../cli/latest/reference/ec2/copy-image.md") AWS CLI command only.

### Create volumes from local snapshots

You can create volumes on an Outpost from local snapshots. Volumes must be created
on the same Outpost as the source snapshots. You cannot use local snapshots to create
volumes in the Region for the Outpost.

When you create a volume from a local snapshot, you cannot re-encrypt the volume
using different KMS key. Volumes created from local snapshots must be
encrypted using the same KMS key as the source snapshot.

For more information, see [Create an Amazon EBS volume](ebs-creating-volume.md "ebs-creating-volume.md").

### Launch instances from AMIs backed by local snapshots

You can launch instances from AMIs that are backed by local snapshots. You must launch
Instances on the same Outpost as the source AMI. For more information, see [Launch an instance on your Outpost](../../../outposts/latest/userguide/launch-instance.md "../../../outposts/latest/userguide/launch-instance.md") in the _AWS Outposts User
Guide_.

### Delete local snapshots

You can delete local snapshots from an Outpost. After you delete a snapshot from an Outpost,
the Amazon S3 storage capacity used by the deleted snapshot becomes available within 72 hours after
deleting the snapshot and the volumes that reference that snapshot.

Because Amazon S3 storage capacity does not become available immediately, we recommend that you
use Amazon CloudWatch alarms to monitor your Amazon S3 storage capacity. Delete snapshots and
volumes that you no longer need to avoid running out of storage capacity.

For more information about deleting snapshots, see [Delete a snapshot](ebs-deleting-snapshot.md#ebs-delete-snapshot "ebs-deleting-snapshot.md#ebs-delete-snapshot").

### Automate snapshots on an Outpost

You can create Amazon Data Lifecycle Manager snapshot lifecycle policies that automatically create, copy, retain,
and delete snapshots of your volumes and instances on an Outpost. You can choose
whether to store the snapshots in a Region or whether to store them locally on an
Outpost. Additionally, you can automatically copy snapshots that are created and
stored in an AWS Region to an Outpost.

The following table provides an overview of the supported features.

| Resource location | Snapshot destination | Cross-region copy | Fast snapshot restore | Cross-account sharing |
| ----------------- | -------------------- | ----------------- | --------------------- | --------------------- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| To Region         | To Outpost           |
| Region            | Region               | ✓                 | ✓                     | ✓                     | ✓   |
| Outpost           | Region               | ✓                 | ✓                     | ✓                     | ✓   |
| Outpost           | Outpost              | ✗                 | ✗                     | ✗                     | ✗   | ###### Considerations <br>• Only Amazon EBS snapshot lifecycle policies are currently supported. EBS-backed AMI policies and Cross-account sharing event policies are not supported. <br>• If a policy manages snapshots for volumes or instances in a Region, then snapshots are created in the same Region as the source resource. <br>• If a policy manages snapshots for volumes or instances on an Outpost, then snapshots can be created on the source Outpost, or in the Region for that Outpost. <br>• A single policy can't manage both snapshots in a Region and snapshots on an Outpost. If you need to automate snapshots in a Region and on an Outpost, you must create separate policies. <br>• Fast snapshot restore is not supported for snapshots created on an Outpost, or for snapshots copied to an Outpost. <br>• Cross-account sharing is not supported for snapshots created on an Outpost. For more information about creating a snapshot lifecycle that manages local snapshots, see [Automating snapshot lifecycles](snapshot-ami-policy.md "snapshot-ami-policy.md"). |
