

# Actions, resources, and condition keys for AWS Backup storage
<a name="list_backup-storage"></a>

AWS Backup storage (service prefix: `backup-storage`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/aws-backup/latest/devguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/aws-backup/latest/devguide/security-considerations.html#authentication) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/backup-storage/backup-storage.json) for this service.

**Topics**
+ [Actions defined by AWS Backup storage](#list_backup-storage-actions-as-permissions)
+ [Permission-only actions for AWS Backup storage](#list_backup-storage-permission-only-actions)
+ [Resource types defined by AWS Backup storage](#list_backup-storage-resources-for-iam-policies)
+ [Condition keys for AWS Backup storage](#list_backup-storage-policy-keys)

## Actions defined by AWS Backup storage
<a name="list_backup-storage-actions-as-permissions"></a>

AWS Backup storage has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Backup storage
<a name="list_backup-storage-permission-only-actions"></a>

The following actions are defined by AWS Backup storage but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CommitBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to commit backup job |  |   | Write | 
|   [DeleteObjects](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to delete objects |  |   | Write | 
|   [DescribeBackupJob](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to describe backup job |  |   | Write | 
|   [GetBaseBackup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to get base backup |  |   | Write | 
|   [GetChunk](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to get data from a recovery point for a restore job |  |   | Write | 
|   [GetIncrementalBaseBackup](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to get incremental base backup |  |   | Write | 
|   [GetObjectMetadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to get metadata from a recovery point for a restore job |  |   | Write | 
|   [ListChunks](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to list data from a recovery point for a restore job |  |   | Write | 
|   [ListObjects](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to list data from a recovery point for a restore job |  |   | Write | 
|   [MountCapsule](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_CreateBackupVault.html)  | Associates a KMS key to a backup vault |  |   | Write | 
|   [NotifyObjectComplete](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to mark an uploaded data as completed for a backup job |  |   | Write | 
|   [PutChunk](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to upload data to an AWS Backup-managed recovery point for a backup job |  |   | Write | 
|   [PutObject](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to put object |  |   | Write | 
|   [StartObject](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to upload data to an AWS Backup-managed recovery point for a backup job |  |   | Write | 
|   [UpdateObjectComplete](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-data-transfer.html)  | Grants permission to update object complete |  |   | Write | 

## Resource types defined by AWS Backup storage
<a name="list_backup-storage-resources-for-iam-policies"></a>

AWS Backup storage does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Backup storage
<a name="list_backup-storage-policy-keys"></a>

AWS Backup storage has no service-specific condition keys that can be used in the `Condition` element of policy statements.