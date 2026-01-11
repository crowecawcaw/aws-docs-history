# Cluster snapshot considerations

Amazon DocumentDB creates daily automatic snapshots of your cluster during
your cluster's backup window. Amazon DocumentDB saves the automatic snapshots of
your cluster according to the backup retention period that you specify.
If necessary, you can recover your cluster to any point in time during
the backup retention period. Automatic snapshots don't occur while a
copy operation is executing in the same Region for the same cluster.

###### Topics

- [Backup storage](#backup_restore-backup_storage "#backup_restore-backup_storage")
- [Backup window](#backup_restore-backup_window "#backup_restore-backup_window")
- [Backup retention period](#backup_restore-backup_retention_period "#backup_restore-backup_retention_period")
- [Copy cluster snapshot encryption](#backup_restore-encryption "#backup_restore-encryption")
  In addition to automatic cluster snapshots, you can also manually
  create a cluster snapshot. You can copy both automatic and manual
  snapshots. For more information, see [Creating a manual cluster snapshot](backup_restore-create_manual_cluster_snapshot.md "backup_restore-create_manual_cluster_snapshot.md")
  and [Copying Amazon DocumentDB cluster snapshots](backup_restore-copy_cluster_snapshot.md "backup_restore-copy_cluster_snapshot.md").

###### Note

Your cluster must be in the _available_
state for an automatic snapshot to be taken.

You can't share an Amazon DocumentDB automated cluster snapshot. As a
workaround, you can create a manual snapshot by copying the
automated snapshot, and then share that copy. For more information
about copying a snapshot, see [Copying Amazon DocumentDB cluster snapshots](backup_restore-copy_cluster_snapshot.md "backup_restore-copy_cluster_snapshot.md").
For more information about restoring a cluster from a snapshot, see [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md "backup_restore-restore_from_snapshot.md").

## Backup storage

Your Amazon DocumentDB backup storage for each AWS Region is composed of
the backup storage needed for your backup retention period, which
includes automatic and manual cluster snapshots in that Region. The
default backup retention period is 1 day. For more information about
backup storage pricing, see [Amazon DocumentDB Pricing](https://aws.amazon.com/documentdb/pricing/ "https://aws.amazon.com/documentdb/pricing/").

When you delete a cluster, all of its automatic snapshots are
deleted and cannot be recovered. However, manual snapshots are not
deleted when you delete a cluster. if you choose to have Amazon DocumentDB
create a final snapshot (manual snapshot) before your cluster is
deleted, you can use the final snapshot to recover your cluster.

For more information on snapshots and storage, see [Understanding backup storage usage](backup_restore-understanding_backup_storage_usage.md "backup_restore-understanding_backup_storage_usage.md").

## Backup window

Automatic snapshots occur daily during the preferred backup
window. If the snapshot requires more time than allotted to the
backup window, the backup process continues until it finishes, even
though the backup window has ended. The backup window can't overlap
with the weekly maintenance window for the cluster.

If you don't specify a preferred backup window when you create
the cluster, Amazon DocumentDB assigns a default 30-minute backup window. This
window is chosen at random from an 8-hour block of time associated
with your cluster's Region. You can change your preferred backup
window by modifying the cluster. For more information, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

| Region Name               | Region         | UTC Time Block |
| ------------------------- | -------------- | -------------- |
| US East (Ohio)            | us-east-2      | 03:00-11:00    |
| US East (N. Virginia)     | us-east-1      | 03:00-11:00    |
| US West (Oregon)          | us-west-2      | 06:00-14:00    |
| Africa (Cape Town)        | af-south-1     | 03:00–11:00    |
| Asia Pacific (Hong Kong)  | ap-east-1      | 06:00-14:00    |
| Asia Pacific (Hyderabad)  | ap-south-2     | 06:30–14:30    |
| Asia Pacific (Malaysia)   | ap-southeast-5 | 13:00-21:00    |
| Asia Pacific (Mumbai)     | ap-south-1     | 06:00-14:00    |
| Asia Pacific (Osaka)      | ap-northeast-3 | 12:00-20:00    |
| Asia Pacific (Seoul)      | ap-northeast-2 | 13:00-21:00    |
| Asia Pacific (Singapore)  | ap-southeast-1 | 14:00-22:00    |
| Asia Pacific (Sydney)     | ap-southeast-2 | 12:00-20:00    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | 08:00-16:00    |
| Asia Pacific (Thailand)   | ap-southeast-7 | 15:00-23:00    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | 13:00-21:00    |
| Canada (Central)          | ca-central-1   | 03:00-11:00    |
| China (Beijing)           | cn-north-1     | 06:00-14:00    |
| China (Ningxia)           | cn-northwest-1 | 06:00-14:00    |
| Europe (Frankfurt)        | eu-central-1   | 21:00-05:00    |
| Europe (Ireland)          | eu-west-1      | 22:00-06:00    |
| Europe (London)           | eu-west-2      | 22:00-06:00    |
| Europe (Milan)            | eu-south-1     | 02:00-10:00    |
| Europe (Paris)            | eu-west-3      | 23:59-07:29    |
| Europe (Spain)            | eu-south-2     | 02:00–10:00    |
| Europe (Stockholm)        | eu-north-1     | 04:00–12:00    |
| Mexico (Central)          | mx-central-1   | 03:00-11:00    |
| Middle East (UAE)         | me-central-1   | 05:00–13:00    |
| South America (São Paulo) | sa-east-1      | 00:00-08:00    |
| Israel (Tel Aviv)         | il-central-1   | 04:00-12:00    |
| AWS GovCloud (US-East)    | us-gov-east-1  | 17:00-01:00    |
| AWS GovCloud (US-West)    | us-gov-west-1  | 06:00-14:00    |

## Backup retention period

The backup retention period is the number of days an automatic
backup is retained before being automatically deleted. Amazon DocumentDB
supports a backup retention period of 1–35
days.

You can set the backup retention period when you create a cluster.
If you don't explicitly set the backup retention period, the default
backup retention period of 1 day is assigned to your cluster. After
you create a cluster, you can modify the backup retention period by
modifying the cluster using either the AWS Management Console or the AWS CLI. For
more information, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

## Copy cluster snapshot encryption

Cluster and snapshot encryption is based on a KMS encryption key.
The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.

The following guidelines and limitations apply:

- Encryption is inferred from the cluster when creating a snapshot.
  If the cluster is encrypted, the snapshot of that cluster is encrypted with the same KMS key.
  If the cluster is not encrypted, the snapshot is not encrypted.
- If you copy an encrypted cluster snapshot from your Amazon Web Services account, you can specify a value for `KmsKeyId` to encrypt the copy with a new KMS encryption key.
  If you don't specify a value for `KmsKeyId` , then the copy of the cluster snapshot is encrypted with the same KMS key as the source cluster snapshot.
- If you copy an encrypted cluster snapshot that is shared from another Amazon Web Services account, then you must specify a value for `KmsKeyId`.
- To copy an encrypted cluster snapshot to another Amazon Web Services Region, set `KmsKeyId` to the KMS key ID that you want to use to encrypt the copy of the cluster snapshot in the destination Region.
  KMS encryption keys are specific to the Amazon Web Services Region that they are created in, and you can't use encryption keys from one Amazon Web Services Region in another Amazon Web Services Region.
- If you copy an unencrypted cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.
