# Local snapshots in Local Zones

Amazon EBS snapshots are a point-in-time copy of your EBS volumes.

Snapshots of EBS volumes in an AWS Local Zone can be stored in Amazon S3 in the same Local Zone or
in the parent Region of that Local Zone. Storing snapshots in a Local Zone can help you meet data
residency needs by ensuring that snapshot data is processed and stored in a specific country,
state, or municipality. You can also set up data residency enforcement policies using IAM
to ensure that snapshot data does not leave the Local Zone.

Local Zones are ideal for applications that require single-digit millisecond latency or local
data processing by bringing AWS infrastructure closer to your end users and business centers.
Additionally, you can meet data residency requirements for regulatory and compliance-sensitive
workloads. For more information, see [What is AWS Local Zones](../../../local-zones/latest/ug/what-is-aws-local-zones.md "../../../local-zones/latest/ug/what-is-aws-local-zones.md").

Local snapshots are currently supported in Local Zones that support Amazon S3. For more information,
see [AWS
Local Zones features.](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/").

###### Topics

- [Frequently asked questions](#faq "#faq")
- [Considerations](#considerations "#considerations")
- [Controlling access with IAM](#local-snaps-iam "#local-snaps-iam")

## Frequently asked questions

**1. What are Local snapshots in Local Zones?**

Local snapshots in Local Zones are snapshots that are stored in Amazon S3 in a Local Zone. By default,
snapshots of Amazon EBS volumes in a Local Zone are stored in Amazon S3 in the parent Region.
If the Local Zone supports Amazon S3, you can choose to store the snapshots locally in
the Local Zone instead. Like snapshots in AWS Regions, Local snapshots in Local Zones are incremental,
which means that only the blocks of the volume that have changed after your
most recent snapshot are saved. You can use these snapshots to restore an Amazon EBS
volume in the same Local Zone at any time.

**2. Why should I use Local snapshots?**

Use Local snapshots in Local Zones to meet data residency or data isolation requirements by ensuring
that your snapshot data resides in a specific geographic location, such as a
country, state, or municipality.

**3. How do I enforce snapshot data residency in Local Zones?**

You can use AWS Identity and Access Management (IAM) policies to control the permissions that principals
(AWS accounts, IAM users, and IAM roles) have when working with Local snapshots in Local Zones and to
enforce data residency. For example, you can create a policy that prevents users
from creating snapshots from volumes in a Local Zones and storing those snapshots in
an AWS Region. For more information, see [Controlling access with IAM](#local-snaps-iam "#local-snaps-iam").

**4. Are multi-volume, crash-consistent Local snapshots supported?**

Yes, you can create multi-volume, crash-consistent Local snapshots in Local Zones from instances in a
Local Zone.

**5. How do I create Local snapshots in Local Zones?**

You can create Local snapshots in Local Zones manually using the AWS CLI or the Amazon EC2 console. For more
information see, [Create a snapshot of an EBS volume](ebs-create-snapshot.md "ebs-create-snapshot.md").
You can also automate the lifecycle of Local snapshots in Local Zones using Amazon Data Lifecycle Manager. For more information
see, [Create Amazon Data Lifecycle Manager custom policy for EBS snapshots](snapshot-ami-policy.md "snapshot-ami-policy.md").

**6. Can I copy Local snapshots in Local Zones?**

Yes, you can copy snapshots from a Region to a Local Zone in the same Region, from
a Local Zone to its Region, and from one Local Zone to another Local Zone in the same
Local Zone group.

**7. How can I restore data from Local snapshots in Local Zones?**

You can use Local snapshots in Local Zones to create Amazon EBS volumes in the same Local Zone only.

**8. How are Local snapshots in Local Zones encrypted?**

Local snapshots can be unencrypted or encrypted by default. When encrypted
by default, Local snapshots are encrypted using the same AWS KMS key as the
source Amazon EBS volume. When you create a volume from a Local snapshot, you
can't re-encrypt the volume using a different KMS key. Volumes created from
Local snapshots must be encrypted using the same AWS KMS key as the source
snapshot.

**9. Can I create EBS-backed AMIs using Local snapshots in Local Zones?**

Yes, you can use Local snapshots in Local Zones when creating EBS-backed AMIs by specifying the
snapshot destination as Local Zones. For more information, see [Create an Amazon EBS-backed AMI](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md#creating-launching-ami-from-snapshot").

**10. Can I share Local snapshots in Local Zones?**

Yes, you can share Local snapshots in Local Zones with other AWS accounts that have enabled the
Local Zone for use in their account.

**11. Can I create a Local snapshot of a volume and then switch to creating snapshots
in the parent Region?**

No, after you create a Local snapshot of a volume, you can't create successive
snapshots of that volume in the Parent Region. Since all snapshots are incremental,
if the most recent snapshot of a volume is a Local snapshot, then all successive
snapshots of that volume must be Local snapshots.

## Considerations

Keep the following in mind when working with Local snapshots in Local Zones.

- Local snapshots are currently supported in Local Zones that support Amazon S3.
- The following features can't be used with Local snapshots in Local Zones:
  - VM Import/Export actions
  - Fast snapshot restore
  - EBS direct APIs
  - Recycle Bin
  - Snapshot archive

- You must use IAM policies to enforce your data residency requirements. For
  more information, see [Controlling access with IAM](#local-snaps-iam "#local-snaps-iam").
- If the most recent snapshot of a volume is a Local snapshot, then all successive
  snapshots must be Local snapshots. Similarly, if the most recent snapshot of a
  volume is stored in an AWS Region, then all successive snapshots must be stored
  in the same Region.

## Controlling access with IAM

You can use AWS Identity and Access Management (IAM) policies to control the permissions that principals
(AWS accounts, IAM users, and IAM roles) have when working with Local snapshots in Local Zones. The
following are example policies that you can use to grant or deny permission to perform
specific actions with Local snapshots in Local Zones.

###### Topics

- [Enforce data residency for Local snapshots in Local Zones](#dlz-enforce-residency-snapshot "#dlz-enforce-residency-snapshot")
- [Prevent sharing of Local snapshots in Local Zones](#dlz-deny-sharing "#dlz-deny-sharing")
- [Prevent principals from deleting Local snapshots in Local Zones](#dlz-deny-delete "#dlz-deny-delete")

### Enforce data residency for Local snapshots in Local Zones

The following example policy restricts users to creating only Local snapshots in Local Zones from volumes and
instances in a Local Zone. It prevents users from creating snapshots in a Region from volumes
and instances in a Local Zone.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Deny",
 "Action":
 [
 "ec2:CreateSnapshot",
 "ec2:CreateSnapshots"
 ],
 "Resource": "*",
 "Condition":
 {
 "StringEquals":
 {
 "ec2:Location": "regional",
 "ec2:SourceAvailabilityZone": "`local_zone`"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action":
 [
 "ec2:CreateSnapshot",
 "ec2:CreateSnapshots"
 ],
 "Resource": "*",
 "Condition":
 {
 "StringEquals":
 {
 "ec2:SourceAvailabilityZone": "`local_zone`"
 },
 "Null":
 {
 "ec2:Location": "true"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "ec2:CreateSnapshot",
 "ec2:CreateSnapshots"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Prevent sharing of Local snapshots in Local Zones

The following example policy prevents all users from sharing Local snapshots in Local Zones.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenySnapshotModifyInLocalZone",
 "Effect": "Deny",
 "Action": [
 "ec2:ModifySnapshotAttribute"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "StringEquals": {
 "ec2:AvailabilityZone": "`use1-atl2-az1`"
 }
 }
 },
 {
 "Sid": "AllowSnapshotModifyElsewhere",
 "Effect": "Allow",
 "Action": [
 "ec2:ModifySnapshotAttribute"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*"
 }
 ]
}`

```

### Prevent principals from deleting Local snapshots in Local Zones

The following example policy prevents all users from deleting Local snapshots in Local Zones.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenySnapshotDeleteInLocalZone",
 "Effect": "Deny",
 "Action": [
 "ec2:DeleteSnapshot"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*",
 "Condition": {
 "StringEquals": {
 "ec2:AvailabilityZone": "`use1-atl2-az1`"
 }
 }
 },
 {
 "Sid": "AllowSnapshotDeleteElsewhere",
 "Effect": "Allow",
 "Action": [
 "ec2:DeleteSnapshot"
 ],
 "Resource": "arn:aws:ec2:*::snapshot/*"
 }
 ]
}`

```
