# PutBackupVaultNotifications

Turns on notifications on a backup vault for the specified topic and events.

## Request Syntax

```
PUT /backup-vaults/`backupVaultName`/notification-configuration HTTP/1.1
Content-type: application/json

{
   "BackupVaultEvents": [ "`string`" ],
   "SNSTopicArn": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_PutBackupVaultNotifications_RequestSyntax "#API_PutBackupVaultNotifications_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[BackupVaultEvents](#API_PutBackupVaultNotifications_RequestSyntax "#API_PutBackupVaultNotifications_RequestSyntax")**

An array of events that indicate the status of jobs to back up resources to the backup
vault. For the list of supported events, common use cases, and code samples, see [Notification options
with AWS Backup](backup-notifications.md "backup-notifications.md").

###### Note

The list below includes both supported events and deprecated events that are no longer
in use (for reference). Deprecated events do not return statuses or notifications.

Type: Array of strings

Valid Values: `BACKUP_JOB_STARTED | BACKUP_JOB_COMPLETED | BACKUP_JOB_SUCCESSFUL | BACKUP_JOB_FAILED | BACKUP_JOB_EXPIRED | RESTORE_JOB_STARTED | RESTORE_JOB_COMPLETED | RESTORE_JOB_SUCCESSFUL | RESTORE_JOB_FAILED | COPY_JOB_STARTED | COPY_JOB_SUCCESSFUL | COPY_JOB_FAILED | RECOVERY_POINT_MODIFIED | BACKUP_PLAN_CREATED | BACKUP_PLAN_MODIFIED | S3_BACKUP_OBJECT_FAILED | S3_RESTORE_OBJECT_FAILED | CONTINUOUS_BACKUP_INTERRUPTED | RECOVERY_POINT_INDEX_COMPLETED | RECOVERY_POINT_INDEX_DELETED | RECOVERY_POINT_INDEXING_FAILED`

Required: Yes

**[SNSTopicArn](#API_PutBackupVaultNotifications_RequestSyntax "#API_PutBackupVaultNotifications_RequestSyntax")**

The Amazon Resource Name (ARN) that specifies the topic for a backup vault’s events; for
example, `arn:aws:sns:us-west-2:111122223333:MyVaultTopic`.

Type: String

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/cli2/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/DotNetSDKV4/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForCpp/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForGoV2/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForJavaV2/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForKotlin/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForPHPV3/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/boto3/backup-2018-11-15/PutBackupVaultNotifications.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultNotifications.md "../../../goto/SdkForRubyV3/backup-2018-11-15/PutBackupVaultNotifications.md")
