# DB cluster snapshot copying

With Amazon Aurora, you can copy automated backups or manual DB cluster snapshots. After you copy a snapshot, the copy is a manual
snapshot. You can make multiple copies of an automated backup or manual snapshot, but each copy must have a unique
identifier.

You can copy a snapshot within the same AWS Region, you can copy a snapshot across AWS Regions, and you can copy shared
snapshots. You can copy snapshots to another AWS Region or account in a single step.

###### Note

Amazon bills you based upon the amount of Amazon Aurora backup and snapshot data you keep and the
period of time that you keep it. For information about the storage associated with Aurora
backups and snapshots, see [Understanding Amazon Aurora backup storage usage](aurora-storage-backup.md "aurora-storage-backup.md"). For pricing information about Aurora
storage, see [Amazon RDS for Aurora
pricing](https://aws.amazon.com/rds/aurora/pricing "https://aws.amazon.com/rds/aurora/pricing").

Review the limitations and considerations for DB cluster snapshot copying. To copy DB cluster snapshots, see one of the following topics.

- [Copying a DB cluster snapshot with the AWS Management Console](USER_CopyDBClusterSnapshot.md "USER_CopyDBClusterSnapshot.md")
- [Copying an unencrypted DB cluster snapshot by using the AWS CLI or Amazon RDS API](USER_CopyDBClusterSnapshot.Unencrypted.md "USER_CopyDBClusterSnapshot.Unencrypted.md")
- [Copying an encrypted DB cluster snapshot by using the AWS CLI or Amazon RDS API](USER_CopyDBClusterSnapshot.Encrypted.md "USER_CopyDBClusterSnapshot.Encrypted.md")
- [Copying a DB cluster snapshot across accounts](USER_CopyDBClusterSnapshot.md "USER_CopyDBClusterSnapshot.md")

## Limitations

The following are some limitations when you copy snapshots:

- You can't copy a snapshot to or from the following AWS Regions:
  - China (Beijing)
  - China (Ningxia)

- You can copy a snapshot between AWS GovCloud (US-East) and AWS GovCloud (US-West).
  However, you can't copy a snapshot between these AWS GovCloud (US) Regions and
  commercial AWS Regions.
- If you delete a source snapshot before the target snapshot becomes available, the snapshot
  copy might fail. Verify that the target snapshot has a status of
  `AVAILABLE` before you delete a source snapshot.
- You can have up to five snapshot copy requests in progress to a single destination Region
  per account.
- When you request multiple snapshot copies for the same source DB instance, they're queued internally. The copies
  requested later won't start until the previous snapshot copies are completed. For more information, see [Why is my EC2 AMI
  or EBS snapshot creation slow?](https://aws.amazon.com/premiumsupport/knowledge-center/ebs-snapshot-ec2-ami-creation-slow/ "https://aws.amazon.com/premiumsupport/knowledge-center/ebs-snapshot-ec2-ami-creation-slow/") in the AWS Knowledge Center.
- Depending on the AWS Regions involved and the amount of data to be copied, a cross-Region
  snapshot copy can take hours to complete. In some cases, there might be a large
  number of cross-Region snapshot copy requests from a given source Region. In
  such cases, Amazon RDS might put new cross-Region copy requests from that source
  Region into a queue until some in-progress copies complete. No progress
  information is displayed about copy requests while they are in the queue.
  Progress information is displayed when the copy starts.
- Aurora doesn't support incremental snapshots. Aurora DB cluster snapshot copies are always stored as full
  copies. A full snapshot copy contains all of the data and metadata required to restore the DB cluster.

## Considerations for snapshot copying

The following are considerations when copying snapshots.

###### Topics

- [Considerations for shared snapshot copying](#aurora-copy-snapshot.Shared "#aurora-copy-snapshot.Shared")
- [Considerations for encrypted DB cluster snapshot copying](#aurora-copy-snapshot.Encryption "#aurora-copy-snapshot.Encryption")
- [Considerations for Cross-Region snapshot copying](#aurora-copy-snapshot.AcrossRegions "#aurora-copy-snapshot.AcrossRegions")
- [Considerations for parameter groups](#aurora-copy-snapshot.Parameters "#aurora-copy-snapshot.Parameters")

### Considerations for shared snapshot copying

You can copy snapshots shared to you by other AWS accounts. In some cases, you might copy an
encrypted snapshot that has been shared from another AWS account. In these cases, you
must have access to the AWS KMS key that was used to encrypt the
snapshot. For more information, see
[Sharing encrypted snapshots](share-encrypted-snapshot.md "share-encrypted-snapshot.md").

#### Cross-Region and cross-account copy in a single step

To copy a snapshot cross-Region and cross-account in a single action, you must first share the snapshot with the target AWS account.
If the snapshot is encrypted, you must also share the AWS KMS key with the target AWS account. If the snapshot is encrypted with the default AWS KMS key,
you must first copy the snapshot to re-encrypt it with a customer managed key before sharing it with the target account. Once shared, you can initiate a copy
to that account (in-Region or cross-Region) from the target account.

### Considerations for encrypted DB cluster snapshot copying

You can copy a snapshot that has been encrypted using a KMS key. If you copy an encrypted snapshot, the copy of the snapshot must
also be encrypted. If you copy an encrypted snapshot within the same AWS Region, you can encrypt the copy with the same
KMS key as the original snapshot. Or you can specify a different KMS key.

If you copy an encrypted snapshot across Regions, you must specify a KMS key valid in the destination AWS Region. It can
be a Region-specific KMS key, or a multi-Region key. For more information on multi-Region KMS keys, see [Using multi-Region keys in
AWS KMS](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md").

For more information about AWS KMS key management for Amazon RDS, see [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").

The source snapshot remains encrypted throughout the copy process. For more information, see
[Limitations of Amazon Aurora encrypted DB clusters](Overview.md#Overview.Encryption.Limitations "Overview.md#Overview.Encryption.Limitations").

###### Note

For Amazon Aurora DB cluster snapshots, you can't encrypt an unencrypted DB cluster snapshot when
you copy the snapshot.

To copy encrypted DB cluster snapshots, see the following topics.

- [Copying an encrypted DB cluster snapshot by using the AWS CLI or Amazon RDS API](USER_CopyDBClusterSnapshot.Encrypted.md "USER_CopyDBClusterSnapshot.Encrypted.md")
- [Copying a DB cluster snapshot across accounts](USER_CopyDBClusterSnapshot.md "USER_CopyDBClusterSnapshot.md")

### Considerations for Cross-Region snapshot copying

You can copy DB cluster snapshots across AWS Regions. However, there are certain
constraints and considerations for cross-Region snapshot copying.

Depending on the AWS Regions involved and the amount of data to be copied, a cross-Region snapshot copy can take hours to
complete.

In some cases, there might be a large number of cross-Region snapshot copy
requests from a given source AWS Region. In such cases, Amazon RDS might put new
cross-Region copy requests from that source AWS Region into a queue until some
in-progress copies complete. No progress information is displayed about copy
requests while they are in the queue. Progress information is displayed when the
copying starts.

Data transfer charges applies for cross-Region snapshot copy. Cross-Region snapshot copying creates full copies in the target data, but the data transfer
charges are incremental. Incremental data includes both the new data that has been added
to a customer’s database since the last copy, as well as any changes made to existing
data.
For more information, see [Creating backup copies across AWS Regions](../../../aws-backup/latest/devguide/cross-region-backup.md "../../../aws-backup/latest/devguide/cross-region-backup.md") in the _AWS Backup Developer Guide_.

###### Note

Aurora copies the minimum amount of data required to create a full copy of a snapshot in the destination region. Data
transfer charges apply when copying snapshots between regions.

### Considerations for parameter groups

When you copy a snapshot across Regions, the copy doesn't include the parameter group used
by the original DB cluster. When you restore a snapshot to create a new DB cluster, that DB
cluster gets the default parameter group for the AWS Region it is created in. To give the new DB
cluster the same parameters as the original, do the following:

1. In the destination AWS Region, create a DB cluster
   parameter group with the same settings as the original DB cluster.
   If one already exists in the new AWS Region, you can use that one.
2. After you restore the snapshot in the destination AWS Region, modify the new DB
   cluster and add the new or existing parameter group from the previous step.
