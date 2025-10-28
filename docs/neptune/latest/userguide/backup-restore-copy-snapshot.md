# Copying a DB Cluster Snapshot

With Neptune, you can copy automated or manual DB cluster snapshots. After you copy a
snapshot, the copy is a manual snapshot.

You can copy a snapshot within the same AWS region and across AWS regions.
Snapshots can be copied across regions and accounts in a single step.

Copying an automated snapshot to another AWS account is a two-step process: First, you create
a manual snapshot from the automated snapshot, and then you copy the manual snapshot to the
other account.

As an alternative to copying, you can also share manual snapshots with other AWS accounts.
For more information, see [Sharing a DB Cluster Snapshot](backup-restore-share-snapshot.md "backup-restore-share-snapshot.md").

###### Topics

- [Limitations on Copying a Snapshot](#backup-restore-copy-snapshot-limitations "#backup-restore-copy-snapshot-limitations")
- [Retention of DB Cluster Snapshot Copies](#backup-restore-copy-snapshot-retention "#backup-restore-copy-snapshot-retention")
- [Handling Encryption When Copying Snapshots](#backup-restore-copy-snapshot-encryption "#backup-restore-copy-snapshot-encryption")
- [Copying Snapshots Across AWS Regions](#backup-restore-copy-snapshot-cross-region "#backup-restore-copy-snapshot-cross-region")
- [Copying a DB Cluster Snapshot Using
  the Console](#backup-restore-copy-snapshot-console "#backup-restore-copy-snapshot-console")
- [Copying a DB Cluster Snapshot Using
  the AWS CLI](#backup-restore-copy-snapshot-cli "#backup-restore-copy-snapshot-cli")

## Limitations on Copying a Snapshot

The following are some limitations when you copy snapshots:

- You can copy a snapshot between China (Beijing) and China (Ningxia),
  but you can't copy a snapshot between these China regions and other AWS Regions.
- You can copy a snapshot between AWS GovCloud (US-East) and AWS GovCloud (US-West),
  but you can't copy a snapshot between these AWS GovCloud (US) regions and other AWS Regions.
- If you delete a source snapshot before the target snapshot becomes available, the snapshot
  copy might fail. Verify that the target snapshot has a status of `AVAILABLE`
  before you delete a source snapshot.
- You can have up to five snapshot copy requests in progress to a single Region per account.
- Depending on the regions involved and the amount of data to be copied,
  a cross-region snapshot copy can take hours to complete.

If there is a large number of cross-region snapshot copy requests from
a given source AWS Region, Neptune may put new cross-region copy requests
from that source AWS Region into a queue until some in-progress copies
complete. No progress information is displayed about copy requests while
they are in that queue. Progress information is displayed only after the
copy starts.

## Retention of DB Cluster Snapshot Copies

Neptune deletes automated snapshots as follows:

- At the end of their retention period.
- When you disable automated snapshots for a DB cluster.
- When you delete a DB cluster.

If you want to keep an automated snapshot for a longer period, copy it to create a manual
snapshot, which is then retained until you delete it. Neptune storage costs might apply to
manual snapshots if they exceed your default storage space.

For more information about backup storage costs, see [Neptune Pricing](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").

## Handling Encryption When Copying Snapshots

You can copy a snapshot that has been encrypted using an AWS KMS encryption key. If you copy
an encrypted snapshot, the copy of the snapshot must also be encrypted. You can encrypt the
copy with the same AWS KMS encryption key as the original snapshot, or you can specify a different
AWS KMS encryption key.

You cannot encrypt an unencrypted DB cluster snapshot when you copy it.

For Amazon Neptune DB cluster snapshots, you can also leave the DB cluster snapshot
unencrypted and instead specify a AWS KMS encryption key when restoring. The restored DB cluster
is encrypted using the specified key.

## Copying Snapshots Across AWS Regions

###### Note

This feature is available starting in [Neptune engine release 1.0.2.1](engine-releases-1.0.2.md "engine-releases-1.0.2.md").

When you copy a snapshot to an AWS Region that is different
from the source snapshot's AWS Region, the first copy is a full snapshot copy, even
if you copy an incremental snapshot. A full snapshot copy contains all of the data and
metadata required to restore the DB instance. After the first snapshot copy, you can
copy incremental snapshots of the same DB instance to the same destination region within
the same AWS account.

An incremental snapshot contains only the data that has changed
after the most recent snapshot of the same DB instance. Incremental snapshot copying
is faster and results in lower storage costs than full snapshot copying. Incremental
snapshot copying across AWS Regions is supported for both unencrypted and encrypted
snapshots.

###### Important

For shared snapshots, copying incremental snapshots is not
supported. For shared snapshots, all of the copies are full snapshots, even within
the same region.

Depending on the AWS Regions involved and the amount of data
to be copied, a cross-region snapshot copy can take hours to complete.

## Copying a DB Cluster Snapshot Using

the Console

If your source database engine is Neptune, then your snapshot is a DB cluster
snapshot. For each AWS account, you can copy up to five DB cluster snapshots at a time
per AWS Region. Copying both encrypted and unencrypted DB cluster snapshots is supported.

For more information about data transfer pricing, see [Neptune Pricing](https://aws.amazon.com/neptune/pricing/ "https://aws.amazon.com/neptune/pricing/").

To cancel a copy operation after it is in progress, delete the target DB cluster snapshot
while that DB cluster snapshot is in **copying** status.

The following procedure works for copying encrypted or unencrypted DB cluster snapshots:

###### To copy a DB cluster snapshot

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Snapshots**.
3. Select the check box for the DB cluster snapshot you want to copy.
4. Choose **Actions**, and then choose **Copy
   Snapshot**. The **Make Copy of DB Snapshot** page
   appears.
5. Enter the name of the DB cluster snapshot copy in **New DB Snapshot
   Identifier**.
6. To copy tags and values from the snapshot to the copy of the snapshot, choose
   **Copy Tags**.
7. For **Enable Encryption**, choose one of the following options:
   - Choose **Disable encryption** if the DB cluster snapshot isn't
     encrypted and you don't want to encrypt the copy.
   - Choose **Enable encryption** if the DB cluster snapshot isn't
     encrypted but you want to encrypt the copy. In this case, for **Master
     Key**, specify the AWS KMS key identifier to use to encrypt the DB cluster
     snapshot copy.
   - Choose **Enable encryption** if the DB cluster snapshot is
     encrypted. In this case, you must encrypt the copy, so **Yes** is
     already selected. For **Master Key**, specify the AWS KMS key
     identifier to use to encrypt the DB cluster snapshot copy.

8. Choose **Copy Snapshot**.

## Copying a DB Cluster Snapshot Using

the AWS CLI

You can copy a DB snapshot using the [copy-db-cluster-snapshot](api-snapshots.md#CopyDBClusterSnapshot "api-snapshots.md#CopyDBClusterSnapshot")
AWS CLI command.

If you are copying the snapshot to a new AWS Region, run the command in
the new Region.

Use the following parameter descriptions and examples to determine which
parameters to use in copying a snapshot with the AWS CLI.

- `--source-db-cluster-snapshot-identifier`   –  
  The identifier for the source DB snapshot.
  - If the source snapshot is in the same AWS Region as the copy,
    specify a valid DB snapshot identifier, like `neptune:instance1-snapshot-20130805`.
  - If the source snapshot is in a different AWS Region than the copy,
    specify a valid DB snapshot ARN like
    `arn:aws:neptune:us-west-2:123456789012:snapshot:instance1-snapshot-20130805`.
  - If you are copying from a shared manual DB snapshot,
    this parameter must be the Amazon Resource Name (ARN) of the shared
    DB snapshot.
  - If you are copying an encrypted snapshot, this parameter must
    be in the ARN format for the source AWS Region, and must match the
    `SourceDBSnapshotIdentifier` in the `PreSignedUrl` parameter.

- `--target-db-cluster-snapshot-identifier` –   –  
  The identifier for the new copy of the encrypted DB snapshot.
- `--kms-key-id` –   –  
  The AWS KMS key ID for an encrypted DB snapshot. The AWS KMS key ID is the Amazon Resource Name
  (ARN), AWS KMS key identifier, or the AWS KMS key alias for the AWS KMS encryption key.
  - If you copy an encrypted DB snapshot from your AWS account,
    you can specify a value for this parameter to encrypt the copy with a new AWS KMS encryption key.
    If you don't specify a value for this parameter, then the copy of the DB snapshot is
    encrypted with the same AWS KMS key as the source DB snapshot.
  - You cannot use this parameter to create an encrypted copy of an
    unencrypted snapshot. Trying to do so will generate an error.
  - If you copy an encrypted snapshot to a different AWS Region,
    then you must specify a AWS KMS key for the destination AWS Region. AWS KMS encryption
    keys are specific to the AWS Region that they are created in, and you cannot
    use encryption keys from one AWS Region in another AWS Region.

- `--source-region` –   –  
  The ID of the AWS Region where the source DB snapshot is. If you copy an encrypted snapshot
  to a different AWS Region, then you must specify this option.
- `--region` –   –  
  The ID of the AWS Region into which you are copying the snapshot. If you copy an
  encrypted snapshot to a different AWS Region, then you must specify this option.

###### Example From Unencrypted, To Same Region

The following code creates a copy of a snapshot, with the new name `mydbsnapshotcopy`,
from the `us-east-1` AWS region to the `us-west-2` region.

For Linux, OS X, or Unix:

```
aws neptune copy-db-cluster-snapshot \
  --source-db-cluster-snapshot-identifier `instance1-snapshot-20130805` \
  --target-db-cluster-snapshot-identifier `mydbsnapshotcopy`
```

For Windows:

```
aws neptune copy-db-cluster-snapshot ^
  --source-db-cluster-snapshot-identifier `instance1-snapshot-20130805` ^
  --target-db-cluster-snapshot-identifier `mydbsnapshotcopy`
```

###### Example From Unencrypted, Across Regions

The following code creates a copy of a snapshot, with the new name `mydbsnapshotcopy`,
from the `us-east-1` AWS region to the `us-west-2` region.
Run the command in the `us-west-2` region.

For Linux, OS X, or Unix:

```
aws neptune copy-db-cluster-snapshot \
  --source-db-cluster-snapshot-identifier `arn:aws:neptune:us-east-1:123456789012:snapshot:instance1-snapshot-20130805` \
  --target-db-cluster-snapshot-identifier `mydbsnapshotcopy` \
  --source-region `us-east-1` \
  --region `us-west-2`
```

For Windows:

```
aws neptune copy-db-cluster-snapshot ^
  --source-db-cluster-snapshot-identifier `arn:aws:neptune:us-east-1:123456789012:snapshot:instance1-snapshot-20130805` ^
  --target-db-cluster-snapshot-identifier `mydbsnapshotcopy` ^
  --source-region `us-east-1` ^
  --region `us-west-2`
```

###### Example From Encrypted, Across Regions

The following code example copies an encrypted DB snapshot from the
`us-east-1` AWS region to the `us-west-2` region.
Run the command in the `us-west-2` region.

For Linux, OS X, or Unix:

```
aws neptune copy-db-cluster-snapshot \
  --source-db-cluster-snapshot-identifier `arn:aws:neptune:us-west-2:123456789012:snapshot:instance1-snapshot-20161115` \
  --target-db-cluster-snapshot-identifier `mydbsnapshotcopy` \
  --source-region `us-east-1` \
  --region `us-west-2`
  --kms-key-id `my_us_west_2_key`
```

For Windows:

```
aws neptune copy-db-cluster-snapshot ^
  --source-db-cluster-snapshot-identifier `arn:aws:neptune:us-west-2:123456789012:snapshot:instance1-snapshot-20161115` ^
  --target-db-cluster-snapshot-identifier `mydbsnapshotcopy` ^
  --source-region `us-east-1` ^
  --region `us-west-2`
  --kms-key-id `my-us-west-2-key`
```
