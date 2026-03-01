# Restore an Amazon EBS volume

When you restore an Amazon Elastic Block Store (EBS) snapshot, you can choose to restore it as an EBS
volume, restore it to a AWS Storage Gateway volume, or restore selected items from it to an Amazon S3
bucket.

## Restore to an EBS volume

When you restore a snapshot (periodic backup of EBS data) to a new volume, you will
specify the volume type, size in GiB, and an availability zone. You can optionally choose
to encrypt the new volume with an existing or new AWS KMS key.

## Restore to a gateway volume

When you restore to a gateway volume, you will need to specify a gateway in a
reachable state, choose your iSCSI target name, and choose a disk ID if your gateway is
volume stored or a capacity equal or greater than your snapshot if your gateway is volume
cached.

## File level restore to an Amazon S3 bucket

Prior to starting a restore job of EBS resources to an Amazon S3 bucket, review [EBS permissions](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md") and [Amazon S3 restore permissions](restoring-s3.md#s3-restore-permissions "restoring-s3.md#s3-restore-permissions") for access requirements. The necessary
permissions are contained in the managed policy [AWSBackupServiceRolePolicyForItemRestores](security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForItemRestores "security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForItemRestores") and should be included in the [IAM role](authentication.md "authentication.md") used for the restore operation.

All new object uploads, including restored data, to an S3 bucket is automatically
encrypted. When you choose this type of restore, specify SSE-S3 (server-side Amazon S3 managed
key) or SSE-KMS (server-side AWS KMS managed key). SSE-S3 is the default.

You can input up to five paths when restoring from the AWS Backup console; you can specify
multiple paths through the command line. A path must have a length less than 1024 bytes in
UTF-8 encoded strings, including the user-designated and AWS Backup-designated prefixes

If your snapshot contains multiple partitions, specify the file system identifier of
the partition that contains the data you plan to restore. This identifier can be found
using [Backup search](backup-search.md "backup-search.md") and is the same of the
UUID or file system Disk ID.

|                                                  | To new EBS volume                                                                          | To gateway                                                                                                                        | File level restore to S3 bucket                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Encryption**                                   | **Optional**. You can choose an existing AWS KMS key or create<br>a new KMS key.           |                                                                                                                                   | Required. Choose from SSE-S3, SSE-KMS, or the default destination bucket<br>encryption1.                                                                                                                                                                                                                                                    |
| **Permissions and roles**                        | Choose existing role; If none exists, default role with correct permissions<br>is created. | Choose existing role;If none exists, default role with correct permissions is<br>created                                          | Role choice must have sufficient [EBS](../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md "../../../aws-managed-policy/latest/reference/AWSBackupServiceRolePolicyForRestores.md") and [Amazon S3 restore permissions](restoring-s3.md#s3-restore-permissions "restoring-s3.md#s3-restore-permissions"). |
| **Restore from cold storage (EBS Archive Tier)** | Available                                                                                  | Unavailable                                                                                                                       | Unavailable                                                                                                                                                                                                                                                                                                                                 |
| **Settings to specify**                          | Volume type; size (GiB); Availability zone; Throughput                                     | Gateway (in a reachable state); iSCSI target name; Disk id (for volume stored<br>gateways); Capacity (for volume cached gateways) | Restore type, including: Destination bucket name; Path(s) to restore;<br>Encryption type; File level restore KMS Key Id if SSE-KMS is set as encryption<br>type                                                                                                                                                                             |

1In the AWS Backup console, you select one of the three
encryption options; if you use CLI to restore, omit `encryptionType` to restore
to the default destination bucket encryption.

## Restore an EBS snapshot with the AWS Backup console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Protected resources** and then
   choose the EBS resource ID you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the
   **Backups** pane, choose the radio button next to the recovery
   point ID of the resource. In the upper-right corner of the pane, choose
   **Restore**.
4. Specify the restore parameters for your resource. The restore parameters you enter
   are specific to the resource type that you selected.

For **Resource type**, choose the AWS resource to create when
restoring this backup. 5. If you choose **EBS volume**, provide the values for
**Volume type**, **Size (GiB)**, and choose an
**Availability zone**. After **Throughput**, there
will be an optional checkbox **Encrypt this volume**. _This
option will stay active if the EBS recovery point is encrypted._. You may
specify a KMS key or you may create an AWS KMS key.

If you choose **Storage Gateway volume**, choose a
**Gateway** in a reachable state. Also choose your **iSCSI
target name**. For _Volume stored_ gateways, choose a
**Disk Id**. For _Volume cached_ gateways,
choose a capacity that is at least as large as your protected resource.

If you choose **file level restore**, you can include up to 5
objects or folders from the snapshot. You can [search
your indexed backups](backup-search.md "backup-search.md") to find the file name or path.

    * Input the file paths.
    * Choose to use an existing Amazon S3 bucket or create a new bucket for the
     destination where the objects or folders will be restored.
    * Set the encryption of the restored object(s). You can choose the default
     destination bucket encryption, SSE-S3, or SSE-KMS. For additional detail, see
     [Restore S3 data using AWS Backup](restoring-s3.md "restoring-s3.md").

6. For **Restore role**, choose the IAM role that AWS Backup will
   assume for this restore. If the AWS Backup default role is not present in your account, a
   **Default role** is created for you with the correct permissions.
   You can delete this default role or make it unusable.
7. Choose **Restore backup** (**Restore items** is
   displayed for file level restore).

The **Restore jobs** pane will appear. A message at the top of
the page provides information about the restore job.

### Restore from archived EBS snapshots

Restoring an archived EBS snapshot moves it from cold to warm storage temporarily to
create a new EBS volume. This type of restore incurs a one-time retrieval charge.
Storage costs for both warm and cold storage are billed during this restore
period.

###### Tip

EBS volumes in cold storage can't be restored to a gateway volume or be restored
at the file level.

You can restore an archived EBS snapshot in cold storage by using the [AWS Backup console](https://console.aws.amazon.com/backup/ "https://console.aws.amazon.com/backup/") or the command line. A restore from
cold storage can take up to 72 hours. For more information, see [Archive Amazon EBS
snapshots](../../../ebs/latest/userguide/snapshot-archive.md "../../../ebs/latest/userguide/snapshot-archive.md") in the _Amazon EBS User Guide_.

Console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. Navigate to **Backup vaults** >
   `Vault` > **Restore archived EBS
   snapshot**.
3. In the **Settings** section, input a value from 0 to 180,
   inclusive, that specifies the number of days to temporarily restore an
   archived snapshot.
4. Input other settings: volume type, size, IOPS, availability zone,
   throughput, and encryption.
5. Choose your **restore role**.
6. Select **Restore backup**. On the confirmation pop up,
   confirm the snapshots and restore type. Then, select **Restore
   snapshot**.

AWS CLI

1. Use [`start-restore-job`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/start-restore-job.html")
2. Include the required parameters for archived EBS snapshot restore:

```
--recovery-point-arn arn:aws:backup:region:account-id:recovery-point:recovery-point-id
--metadata '{"temporaryRestoreDays":"value","volumeType":"value","volumeSize":"value","availabilityZone":"value"}'
--iam-role-arn arn:aws:iam::account-id:role/service-role/AWSBackupDefaultServiceRole
--resource-type EBS
```

3. Specify the temporary restore duration (0-180 days) in the `temporaryRestoreDays` parameter. This determines how long the archived snapshot will be available in warm storage.
4. Configure the new EBS volume settings including `volumeType` (gp2, gp3, io1, io2, st1, sc1), `volumeSize` in GiB, and target `availabilityZone`.
5. Monitor the restore job status using [`describe-restore-job`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-restore-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/describe-restore-job.html") with the returned restore job ID. Archive restores can take up to 72 hours to complete.

## Restore an EBS snapshot by AWS CLI

To restore Amazon EBS using the API or CLI, use `StartRestoreJob`. You can specify the following metadata during an Amazon EBS
restore:

```
aws:backup:request-id
availabilityZone
encrypted // if set to `true`, encryption will be enabled as volume is restored
iops
kmsKeyId // if included, this key will be used to encrypt the restored volume instead of default KMS Key Id
restoreType // include for file level restore - see details below
throughput
temporaryRestoreDays
volumeType
volumeSize
```

Example:

```
"restoreMetadata": "{\"encrypted\":\"false\",\"volumeId\":\"vol-04cc95f3490b5ceea\",\"availabilityZone\":null}"
```

**File level restore specifications**

`restoreType` is required for file level restore. For this type of restore,
the following unique metadata is required:

```
destinationBucketName //
pathsToRestore //
encryptionType // You can specify SSE-S3 or SSE-KMS; do not include if you want to restore to default encryption
kmsKeyId //

```

Filesystem identifier is optional for single partition Snapshots. If this information
is not passed, then just the absolute path without the “:” separator (such as
`{"/data/process/abc.txt", "/data/department/xyz.txt"}`) will be
accepted.
