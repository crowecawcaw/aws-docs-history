# How Amazon EC2 AMI copy works

Copying a source AMI results in an identical but distinct new AMI that we also
refer to as the _target_ AMI. The target AMI has its
own unique AMI ID. You can change or deregister the source AMI with no effect on the
target AMI. The reverse is also true.

With an EBS-backed AMI, each of its backing snapshots is copied to an identical but
distinct target snapshot. If you copy an AMI to a new Region, the snapshots are
complete (non-incremental) copies. If you encrypt unencrypted backing snapshots or
encrypt them to a new KMS key, the snapshots are complete (non-incremental) copies.
Subsequent copy operations of an AMI result in incremental copies of the backing
snapshots.

###### Contents

- [Cross-Region copying](#copy-amis-across-regions "#copy-amis-across-regions")
- [Cross-account copying](#copy-ami-across-accounts "#copy-ami-across-accounts")
- [Time-based AMI copy operations](#ami-time-based "#ami-time-based")
- [Encryption and copying](#ami-copy-encryption "#ami-copy-encryption")

## Cross-Region copying

Copying an AMI across geographically diverse Regions provides the following
benefits:

- Consistent global deployment: Copying an AMI from one Region to another
  enables you to launch consistent instances in different Regions based on the
  same AMI.
- Scalability: You can more easily design and build global applications that
  meet the needs of your users, regardless of their location.
- Performance: You can increase performance by distributing your
  application, as well as locating critical components of your application in
  closer proximity to your users. You can also take advantage of
  Region-specific features, such as instance types or other AWS
  services.
- High availability: You can design and deploy applications across AWS
  Regions, to increase availability.

The following diagram shows the relationship between a source AMI and two copied
AMIs in different Regions, as well as the EC2 instances launched from each. When
you launch an instance from an AMI, it resides in the same Region where the AMI
resides. If you make changes to the source AMI and want those changes to be
reflected in the AMIs in the target Regions, you must recopy the source AMI to
the target Regions.

![AMIs copied in different Regions](images/ami_copy.png)

When you first copy an Amazon S3-backed AMI to a Region, we create an Amazon S3 bucket for the
AMIs copied to that Region. All Amazon S3-backed AMIs that you copy to that Region
are stored in this bucket. The bucket names have the following format:
amis-for-`account`-in-`region`-`hash`.
For example:
`amis-for-123456789012-in-us-east-2-yhjmxvp6`.

###### Prerequisite

Prior to copying an AMI, you must ensure that the contents of the source
AMI are updated to support running in a different Region. For example, you
should update any database connection strings or similar application
configuration data to point to the appropriate resources. Otherwise, instances
launched from the new AMI in the destination Region might still use the
resources from the source Region, which can impact performance and cost.

###### Limitations

- Destination Regions are limited to 300 concurrent AMI copy operations.
  This also applies to time-based AMI copy operations.
- You can't copy a paravirtual (PV) AMI to a Region that does not support PV
  AMIs. For more information, see [Virtualization types](ComponentsAMIs.md#virtualization_types "ComponentsAMIs.md#virtualization_types").

## Cross-account copying

If an AMI from another AWS account is [shared with your AWS account](sharingamis-explicit.md "sharingamis-explicit.md"), you can copy the shared AMI. This is
known as cross-account copying. The AMI that is shared with you is the source AMI.
When you copy the source AMI, you create a new AMI. The new AMI is often referred to
as the target AMI.

###### AMI costs

- For a shared AMI, the account of the shared AMI is charged for the storage
  in the Region.
- If you copy an AMI that is shared with your account, you are the owner of
  the target AMI in your account.
  - The owner of the source AMI is charged standard Amazon EBS or Amazon S3
    transfer fees.
  - You are charged for the storage of the target AMI in the
    destination Region.

###### Resource permissions

To copy an AMI that was shared with you from another account, the owner of the source AMI
must grant you read permissions for the storage that backs the AMI, not just for
the AMI itself. The storage is either the associated EBS snapshot (for an
Amazon EBS-backed AMI) or an associated S3 bucket (for an Amazon S3-backed AMI). If the
shared AMI has encrypted snapshots, the owner must share the key or keys with
you. For more information about granting resource permissions, for EBS
snapshots, see [Share an
Amazon EBS snapshot with other AWS accounts](../../../ebs/latest/userguide/ebs-modifying-snapshot-permissions.md "../../../ebs/latest/userguide/ebs-modifying-snapshot-permissions.md") in the
_Amazon EBS User Guide_, and for S3 buckets, see [Identity and access management for Amazon S3](../../../AmazonS3/latest/userguide/security-iam.md "../../../AmazonS3/latest/userguide/security-iam.md") in the
_Amazon S3 User Guide_.

###### Note

Tags that are attached to the source AMI are not copied across accounts to the
target AMI.

## Time-based AMI copy operations

When you initiate a time-based AMI copy operation for an EBS-backed AMI with a single
associated snapshot, it behaves in the same way as an **individual
time-based snapshot copy operation**, and the same throughput limitations
apply.

When you initiate a time-based AMI copy operation for an EBS-backed AMI with a multiple
associated snapshots, it behaves in the same way as **concurrent time-based
snapshot copy operations**, and the same throughput limitations apply. Each
associated snapshot results in a separate snapshot copy request, each of which contributes
to your cumulative snapshot copy throughput quota. The completion duration that you specify
applies to each associated snapshot.

For more information, see [Time-based copies](../../../ebs/latest/userguide/time-based-copies.md "../../../ebs/latest/userguide/time-based-copies.md") in the _Amazon EBS User Guide_.

## Encryption and copying

The following table shows encryption support for various AMI-copying scenarios.
While it is possible to copy an unencrypted snapshot to yield an encrypted snapshot,
you cannot copy an encrypted snapshot to yield an unencrypted one.

| Scenario | Description                | Supported |
| -------- | -------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Unencrypted to unencrypted | Yes       |
| 2        | Encrypted to encrypted     | Yes       |
| 3        | Unencrypted to encrypted   | Yes       |
| 4        | Encrypted to unencrypted   | No        | ###### Note Encrypting during the `CopyImage` action applies only to Amazon EBS-backed AMIs. Because an Amazon S3-backed AMI does not use snapshots, you can't use copying to change its encryption status. When you copy an AMI without specifying encryption parameters, the backing snapshot is copied with its original encryption status by default. Therefore, if the source AMI is backed by an unencrypted snapshot, the resulting target snapshot will also be unencrypted. Similarly, if the source AMI's snapshot is encrypted, the resulting target snapshot will also be encrypted by the same AWS KMS key. For AMIs backed by multiple snapshots, each target snapshot preserves the encryption state of its corresponding source snapshot. To change the encryption state of the target backing snapshots during an AMI copy, you can specify encryption parameters. The following example shows a non-default case, where encryption parameters are specified with the `CopyImage` action to change the target AMI's encryption state. **Copy an unencrypted source AMI to an encrypted target AMI** In this scenario, an AMI backed by an unencrypted root snapshot is copied to an AMI with an encrypted root snapshot. The `CopyImage` action is invoked with two encryption parameters, including a customer managed key. As a result, the encryption status of the root snapshot changes, so that the target AMI is backed by a root snapshot containing the same data as the source snapshot, but encrypted using the specified key. You incur storage costs for the snapshots in both AMIs, as well as charges for any instances you launch from either AMI. ###### Note Enabling encryption by default has the same effect as setting the `Encrypted` parameter to `true` for all snapshots in the AMI. ![Copy AMI and encrypt snapshot on the fly](images/ami-to-ami-convert.png) Setting the `Encrypted` parameter encrypts the single snapshot for this instance. If you do not specify the `KmsKeyId` parameter, the default customer managed key is used to encrypt the snapshot copy. For more information about copying AMIs with encrypted snapshots, see [Use encryption with EBS-backed AMIs](AMIEncryption.md "AMIEncryption.md"). |
