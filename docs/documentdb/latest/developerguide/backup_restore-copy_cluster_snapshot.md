# Copying Amazon DocumentDB cluster snapshots

In Amazon DocumentDB, you can copy snapshots within the same AWS Region or to a different AWS Region.
You can also copy shared snapshots to your account in the same AWS Region or in a different AWS Region.
For more information on sharing snapshots, see [Sharing Amazon DocumentDB cluster snapshots](backup_restore-share_cluster_snapshots.md "backup_restore-share_cluster_snapshots.md").

###### Note

Amazon DocumentDB bills you based upon the amount of backup and snapshot
data you keep and the period of time that you keep it. For more
information about the storage associated with Amazon DocumentDB backups and
snapshots, see [Understanding backup storage usage](backup_restore-understanding_backup_storage_usage.md "backup_restore-understanding_backup_storage_usage.md").
For pricing information about Amazon DocumentDB storage, see [Amazon DocumentDB Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

###### Topics

- [Copying shared snapshots](#backup_restore-copy_shared_cluster_snapshot "#backup_restore-copy_shared_cluster_snapshot")
- [Copying snapshots across AWS Regions](#backup_restore-copy_snapshot_across_regions "#backup_restore-copy_snapshot_across_regions")
- [Limitations](#backup_restore-copy_cluster_snapshot-limitations "#backup_restore-copy_cluster_snapshot-limitations")
- [Handling encryption](#backup_restore-copy_cluster_snapshot-handle_encryption "#backup_restore-copy_cluster_snapshot-handle_encryption")
- [Parameter group considerations](#backup_restore-copy_cluster_snapshot-parameter_group_considerations "#backup_restore-copy_cluster_snapshot-parameter_group_considerations")
- [Copying a cluster snapshot](#backup_restore-copy_a_cluster_snapshot "#backup_restore-copy_a_cluster_snapshot")

## Copying shared snapshots

You can copy snapshots shared to you by other AWS accounts.
If you are copying an encrypted snapshot that has been shared from another AWS account, you must have access to the AWS KMS encryption key that was used to encrypt the snapshot.
For more information, see [Handling encryption](#backup_restore-copy_cluster_snapshot-handle_encryption "#backup_restore-copy_cluster_snapshot-handle_encryption").

## Copying snapshots across AWS Regions

When you copy a snapshot to an AWS Region that is different from
the source snapshot's AWS Region, each copy is a full snapshot. A
full snapshot copy contains all of the data and meta data required to
restore the Amazon DocumentDB cluster.

## Limitations

The following are some limitations when you copy snapshots:

- If you delete a source snapshot before the target snapshot
  becomes available, the snapshot copy may fail. Verify that the
  target snapshot has a status of `AVAILABLE` before
  you delete a source snapshot.
- You can have up to five snapshot copy requests in progress
  to a single destination Region per account.
- Depending on the AWS Regions involved and the amount of data to
  be copied, a cross-region snapshot copy can take hours to complete.
  In some cases, there might be a large number of cross-region
  snapshot copy requests from a given source AWS Region. In these
  cases, Amazon DocumentDB might put new cross-region copy requests from that
  source AWS Region into a queue until some in-progress copies
  complete. No progress information is displayed about copy requests
  while they are in the queue. Progress information is displayed when
  the copy starts.

## Handling encryption

You can copy a snapshot that has been encrypted using an AWS KMS
encryption key. If you copy an encrypted snapshot, the copy of the
snapshot must also be encrypted. If you copy an encrypted snapshot
within the same AWS Region, you can encrypt the copy with the same
AWS KMS encryption key as the original snapshot, or you can specify a
different AWS KMS encryption key. If you copy an encrypted snapshot
across Regions, you can't use the same AWS KMS encryption key for the
copy as used for the source snapshot, because AWS KMS keys are
Region-specific. Instead, you must specify an AWS KMS key valid in the
destination AWS Regionn.

The source snapshot remains encrypted throughout the copy process.
For more information, see [Data protection in Amazon DocumentDB](security.md "security.md").

###### Note

For Amazon DocumentDB cluster snapshots, you can't encrypt an
unencrypted cluster snapshot when you copy the snapshot.

## Parameter group considerations

When you copy a snapshot across Regions, the copy doesn't include
the parameter group used by the original Amazon DocumentDB cluster. When you
restore a snapshot to create a new cluster, that cluster gets the
default parameter group for the AWS Region it is created in. To give
the new cluster the same parameters as the original, you must do the
following:

1. In the destination AWS Region, [create an Amazon DocumentDB cluster parameter group](cluster_parameter_groups-create.md "cluster_parameter_groups-create.md")
   with the same settings as the original cluster. If one already
   exists in the new AWS Region, you can use that one.
2. After you restore the snapshot in the destination AWS Region, modify the new Amazon DocumentDB cluster and add the new or
   existing parameter group from the previous step. For more
   information, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

## Copying a cluster snapshot

You can copy an Amazon DocumentDB cluster using the AWS Management Console or the AWS CLI,
as follows.

Using the AWS Management Console
To make a copy of a cluster snapshot using the AWS Management Console,
complete the following steps. This procedure works for copying
encrypted or unencrypted cluster snapshots, in the same AWS Region or across Regions.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Snapshots**,
   and then choose the button to the left of the snapshot
   that you want to copy.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. From the **Actions** menu, choose
**Copy**. 4. In the resulting **Make Copy of cluster
snapshot** page, complete the
**Settings** section.

    1. **Destination Region** —
     Optional. To copy the cluster snapshot to a
     different AWS Region, choose that AWS Region for
     **Destination Region**.
    2. **New snapshot identifier**
     — Enter a name for the new snapshot.


    Target snapshot naming constraints:




    	* Cannot be the name of an existing snapshot.
    	* Length is [1—63] letters, numbers,
    	 or hyphens.
    	* First character must be a letter.
    	* Cannot end with a hyphen or contain two
    	 consecutive hyphens.
    	* Must be unique for all clusters across Amazon RDS,
    	 Neptune, and Amazon DocumentDB per AWS account, per
    	 Region.
    3. **Copy tags** — To copy
     any tags you have on your source snapshot to your
     snapshot copy, choose **Copy tags**.

5.  Complete the **Encryption-at-rest**
    section.
    1. **Encryption at rest** —
       If your snapshot is not encrypted, these options are not available to you because you cannot create an encrypted copy from an unencrypted snapshot.
       If your snapshot is encrypted, you can change the AWS KMS key used during encryption at rest.

    For more information about encrypting snapshot copies, see [Copy cluster snapshot encryption](backup_restore-cluster_snapshot_considerations.md#backup_restore-encryption "backup_restore-cluster_snapshot_considerations.md#backup_restore-encryption").

    For more information about encryption at rest, see [Encrypting Amazon DocumentDB data at rest](encryption-at-rest.md "encryption-at-rest.md"). 2. **AWS KMS Key** — From
    the drop-down list, choose one of the following:

        * **(default) aws/rds**
         — The account number and AWS KMS key ID
         are listed following this option.
        * **<some-key-name>**
         — If you created a key, it is listed
         and available for you to choose.
        * **Enter a key ARN**
         — In the **ARN** box,
         enter the Amazon Resource Name (ARN) for your
         AWS KMS key. The format of the ARN is
         `arn:aws:kms:<region>:<accountID>:key/<key-id>` .

6.  To make a copy of the selected snapshot, choose
    **Copy snapshot**. Alternatively, you
    can choose **Cancel** to not make a
    copy of the snapshot.

Using the AWS CLI
To make a copy of an unencrypted cluster snapshot using the
AWS CLI, use the `copy-db-cluster-snapshot` operation
with the following parameters. If you are copying the snapshot
to another AWS Region, run the command in the AWS Region to
which the snapshot will be copied.

- `--source-db-cluster-snapshot-identifier`
  — Required. The identifier of the cluster snapshot to make a copy of.
  The cluster snapshot must exist and be in the available state.
  If you are copying the snapshot to another AWS Region or if you are copying a shared cluster snapshot, this identifier must be in the ARN format of the source cluster snapshot.
  This parameter is not case sensitive.
- `--target-db-cluster-snapshot-identifier`
  — Required. The identifier of the new cluster
  snapshot to create from the source cluster snapshot.
  This parameter is not case sensitive.

Target snapshot naming constraints:

    + Cannot be the name of an existing snapshot.
    + Length is [1—63] letters, numbers, or
     hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two
     consecutive hyphens.
    + Must be unique for all clusters across Amazon RDS,
     Neptune, and Amazon DocumentDB per AWS account, per Region.

- `--source-region`
  — If you are copying the snapshot to another AWS Region, specify the AWS Region that the encrypted cluster
  snapshot will be copied from.

If you're copying the snapshot to another AWS Region
and you don't specify `--source-region`, you
must specify the `pre-signed-url` option
instead. The `pre-signed-url` value must be a
URL that contains a Signature Version 4 signed request
for the `CopyDBClusterSnapshot` action to be
called in the source AWS Region where the cluster
snapshot is copied from. To learn more about the
`pre-signed-url`, see [CopyDBClusterSnapshot](API_CopyDBClusterSnapshot.md "API_CopyDBClusterSnapshot.md").

- `--kms-key-id`
  — The KMS key identifier for the key to use to
  encrypt the copy of the cluster snapshot.

If you are copying an encrypted cluster snapshot to
another AWS Region, this parameter is required. You must
specify a KMS key for the destination AWS Region.

If you are copying an encrypted cluster snapshot in
the same AWS Region, the AWS KMS key parameter is optional.
The copy of the cluster snapshot is encrypted with the
same AWS KMS key as the source cluster snapshot. If you want
to specify a new AWS KMS encryption key to use to encrypt the
copy, you can do so using this parameter.

- `--copy-tags` — Optional.
  The tags and values to be copied over.

To cancel a copy operation once it's in progress, you can
delete the target cluster snapshot identified by
`--target-db-cluster-snapshot-identifier` or
`TargetDBClusterSnapshotIdentifier` while that
cluster snapshot is in **copying**
status.

###### Example

**Example 1: Copy an unencrypted snapshot to the same Region**

The following AWS CLI example creates a copy of `sample-cluster-snapshot` named `sample-cluster-snapshot-copy` in the same AWS Region as the source snapshot.
When the copy is made, all tags on the original snapshot are copied to the snapshot copy.

For Linux, macOS, or Unix:

```
aws docdb copy-db-cluster-snapshot \
    --source-db-cluster-snapshot-identifier sample-cluster-snapshot \
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy \
    --copy-tags
```

For Windows:

```
aws docdb copy-db-cluster-snapshot ^
    --source-db-cluster-snapshot-identifier sample-cluster-snapshot ^
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy ^
    --copy-tags
```

Output from this operation looks something like the
following.

```
{
    "DBClusterSnapshot": {
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1b",
            "us-east-1c"
        ],
        "DBClusterSnapshotIdentifier": "sample-cluster-snapshot-copy",
        "DBClusterIdentifier": "sample-cluster",
        "SnapshotCreateTime": "2020-03-27T08:40:24.805Z",
        "Engine": "docdb",
        "Status": "copying",
        "Port": 0,
        "VpcId": "vpc-abcd0123",
        "ClusterCreateTime": "2020-01-10T22:13:38.261Z",
        "MasterUsername": "master-user",
        "EngineVersion": "4.0.0",
        "SnapshotType": "manual",
        "PercentProgress": 0,
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/sample-key-id",
        "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:111122223333:cluster-snapshot:sample-cluster-snapshot-copy",
        "SourceDBClusterSnapshotArn": "arn:aws:rds:us-east-1:111122223333:cluster-snapshot:sample-cluster-snapshot"
    }
}
```

###### Example

**Example 2: Copy an unencrypted snapshot across AWS Regions**

The following AWS CLI example creates a copy of
`sample-cluster-snapshot`, which has the ARN
`arn:aws:rds:us-east-1:123456789012:cluster-snapshot:sample-cluster-snapshot`.
This copy is named named `sample-cluster-snapshot-copy`
and is in the AWS Region in which the command is run.

For Linux, macOS, or Unix:

```
aws docdb copy-db-cluster-snapshot \
    --source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:123456789012:cluster-snapshot:sample-cluster-snapshot \
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy
```

For Windows:

```
aws docdb copy-db-cluster-snapshot ^
    --source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:123456789012:cluster-snapshot:sample-cluster-snapshot ^
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy
```

Output from this operation looks something like the
following.

```
{
    "DBClusterSnapshot": {
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1b",
            "us-east-1c"
        ],
        "DBClusterSnapshotIdentifier": "sample-cluster-snapshot-copy",
        "DBClusterIdentifier": "sample-cluster",
        "SnapshotCreateTime": "2020-04-29T16:45:51.239Z",
        "Engine": "docdb",
        "AllocatedStorage": 0,
        "Status": "copying",
        "Port": 0,
        "VpcId": "vpc-abc0123",
        "ClusterCreateTime": "2020-04-28T16:43:00.294Z",
        "MasterUsername": "master-user",
        "EngineVersion": "4.0.0",
        "LicenseModel": "docdb",
        "SnapshotType": "manual",
        "PercentProgress": 0,
        "StorageEncrypted": false,
        "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:sample-cluster-snapshot-copy",
        "SourceDBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:sample-cluster-snapshot",
    }
}
```

###### Example

**Example 3: Copy an encrypted snapshot across AWS Regions**

The following AWS CLI example creates a copy of
`sample-cluster-snapshot` from the us-west-2 Region to
the us-east-1 Region. This command is called in the us-east-1
Region.

For Linux, macOS, or Unix:

```
aws docdb copy-db-cluster-snapshot \
    --source-db-cluster-snapshot-identifier arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot \
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy \
    --source-region us-west-2 \
    --kms-key-id sample-us-east-1-key
```

For Windows:

```
aws docdb copy-db-cluster-snapshot ^
    --source-db-cluster-snapshot-identifier arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot ^
    --target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy ^
    --source-region us-west-2 ^
    --kms-key-id sample-us-east-1-key
```

Output from this operation looks something like the
following.

```
{
    "DBClusterSnapshot": {
        "AvailabilityZones": [],
        "DBClusterSnapshotIdentifier": "sample-cluster-snapshot-copy",
        "DBClusterIdentifier": "sample-cluster",
        "SnapshotCreateTime": "2020-04-29T16:45:53.159Z",
        "Engine": "docdb",
        "AllocatedStorage": 0,
        "Status": "copying",
        "Port": 0,
        "ClusterCreateTime": "2020-04-28T16:43:07.129Z",
        "MasterUsername": "chimera",
        "EngineVersion": "4.0.0",
        "LicenseModel": "docdb",
        "SnapshotType": "manual",
        "PercentProgress": 0,
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/0846496a-d48e-41c4-9353-86d8301d7e35",
        "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:123456789012:cluster-snapshot:sample-cluster-snapshot-copy",
        "SourceDBClusterSnapshotArn": "arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot",
    }
}
```

###### Example

**Example 4: Copy an unencrypted shared snapshot across AWS Regions**

The following AWS CLI example, account - `123456789012`, creates a copy of an unencrypted cluster snapshot `sample-cluster-snapshot` shared by account - `999999999999` from the us-east-1 Region to the us-west-2 Region.
This command is called in the us-west-2 Region.
For more information on sharing snapshots, see [Sharing a snapshot](backup_restore-share_cluster_snapshots.md#backup_restore-share_snapshots "backup_restore-share_cluster_snapshots.md#backup_restore-share_snapshots").

For Linux, macOS, or Unix:

```
aws docdb copy-db-cluster-snapshot \
--region us-west-2 \
--source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:999999999999:cluster-snapshot:sample-cluster-snapshot \
--target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy
```

For Windows:

```
aws docdb copy-db-cluster-snapshot ^
--region us-west-2 ^
--source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:999999999999:cluster-snapshot:sample-cluster-snapshot ^
--target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy
```

Output from this operation looks something like the
following.

```
{
 "DBClusterSnapshots": [
 {
 "AvailabilityZones": [],
 "DBClusterSnapshotIdentifier": "sample-cluster-snapshot-copy",
 "DBClusterIdentifier": "sample-cluster",
 "SnapshotCreateTime": "2025-08-22T11:27:00.497000+00:00",
 "Engine": "docdb",
 "Status": "copying",
 "Port": 0,
 "ClusterCreateTime": "2024-07-02T16:44:50.246000+00:00",
 "MasterUsername": "master-user",
 "EngineVersion": "5.0.0",
 "SnapshotType": "manual",
 "PercentProgress": 0,
 "StorageEncrypted": false,
 "DBClusterSnapshotArn": "arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot-copy",
 "SourceDBClusterSnapshotArn": "arn:aws:rds:us-east-1:999999999999:cluster-snapshot:sample-cluster-snapshot"
 }
 ]
}
```

###### Example

**Example 5: Copy an encrypted shared snapshot across AWS Regions**

The following AWS CLI example, account - `123456789012` creates a copy of an encrypted cluster snapshot `sample-cluster-snapshot` shared by account - `999999999999` from the us-east-1 Region to the us-west-2 Region.
The target snapshot is encrypted with a customer managed KMS key - `arn:aws:kms:us-west-2:123456789012:key/6c1f3264-1797-472b-ba37-03011e682d28`.
This command is called in the us-west-2 Region.
For more information on sharing snapshots, see [Sharing a snapshot](backup_restore-share_cluster_snapshots.md#backup_restore-share_snapshots "backup_restore-share_cluster_snapshots.md#backup_restore-share_snapshots").

For Linux, macOS, or Unix:

```
aws docdb copy-db-cluster-snapshot \
--region us-west-2 \
--source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:999999999999:cluster-snapshot:sample-cluster-snapshot \
--target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy \
--kms-key-id arn:aws:kms:us-west-2:123456789012:key/6c1f3264-1797-472b-ba37-03011e682d28
```

For Windows:

```
aws docdb copy-db-cluster-snapshot ^
--region us-west-2 ^
--source-db-cluster-snapshot-identifier arn:aws:rds:us-east-1:999999999999:cluster-snapshot:sample-cluster-snapshot ^
--target-db-cluster-snapshot-identifier sample-cluster-snapshot-copy ^
--kms-key-id arn:aws:kms:us-west-2:123456789012:key/6c1f3264-1797-472b-ba37-03011e682d28
```

Output from this operation looks something like the
following.

```
{
 "DBClusterSnapshots": [
 {
 "AvailabilityZones": [],
 "DBClusterSnapshotIdentifier": "sample-cluster-snapshot-copy",
 "DBClusterIdentifier": "sample-cluster",
 "SnapshotCreateTime": "2025-08-22T11:27:00.497000+00:00",
 "Engine": "docdb",
 "Status": "copying",
 "Port": 0,
 "ClusterCreateTime": "2024-07-02T16:44:50.246000+00:00",
 "MasterUsername": "master-user",
 "EngineVersion": "5.0.0",
 "SnapshotType": "manual",
 "PercentProgress": 0,
 "StorageEncrypted": true,
 "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/6c1f3264-1797-472b-ba37-03011e682d28",
 "DBClusterSnapshotArn": "arn:aws:rds:us-west-2:123456789012:cluster-snapshot:sample-cluster-snapshot-copy",
 "SourceDBClusterSnapshotArn": "arn:aws:rds:us-east-1:999999999999:cluster-snapshot:sample-cluster-snapshot"
 }
 ]
}
```

###### Note

For more information about encrypting snapshot copies, see [Copy cluster snapshot encryption](backup_restore-cluster_snapshot_considerations.md#backup_restore-encryption "backup_restore-cluster_snapshot_considerations.md#backup_restore-encryption").

For more information about encryption at rest, see [Encrypting Amazon DocumentDB data at rest](encryption-at-rest.md "encryption-at-rest.md").
