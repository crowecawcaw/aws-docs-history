# GetBackupVaultNotifications

Returns event notifications for the specified backup vault.

## Request Syntax

```
GET /backup-vaults/`backupVaultName`/notification-configuration HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_GetBackupVaultNotifications_RequestSyntax "#API_GetBackupVaultNotifications_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "***string***",
   "BackupVaultEvents": [ "***string***" ],
   "BackupVaultName": "***string***",
   "SNSTopicArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultArn](#API_GetBackupVaultNotifications_ResponseSyntax "#API_GetBackupVaultNotifications_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

**[BackupVaultEvents](#API_GetBackupVaultNotifications_ResponseSyntax "#API_GetBackupVaultNotifications_ResponseSyntax")**

An array of events that indicate the status of jobs to back up resources to the backup
vault.

Type: Array of strings

Valid Values: `BACKUP_JOB_STARTED | BACKUP_JOB_COMPLETED | BACKUP_JOB_SUCCESSFUL | BACKUP_JOB_FAILED | BACKUP_JOB_EXPIRED | RESTORE_JOB_STARTED | RESTORE_JOB_COMPLETED | RESTORE_JOB_SUCCESSFUL | RESTORE_JOB_FAILED | COPY_JOB_STARTED | COPY_JOB_SUCCESSFUL | COPY_JOB_FAILED | RECOVERY_POINT_MODIFIED | BACKUP_PLAN_CREATED | BACKUP_PLAN_MODIFIED | S3_BACKUP_OBJECT_FAILED | S3_RESTORE_OBJECT_FAILED | CONTINUOUS_BACKUP_INTERRUPTED | RECOVERY_POINT_INDEX_COMPLETED | RECOVERY_POINT_INDEX_DELETED | RECOVERY_POINT_INDEXING_FAILED`

**[BackupVaultName](#API_GetBackupVaultNotifications_ResponseSyntax "#API_GetBackupVaultNotifications_ResponseSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the Region where they are
created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[SNSTopicArn](#API_GetBackupVaultNotifications_ResponseSyntax "#API_GetBackupVaultNotifications_ResponseSyntax")**

An ARN that uniquely identifies an Amazon Simple Notification Service (Amazon SNS)
topic; for example, `arn:aws:sns:us-west-2:111122223333:MyTopic`.

Type: String

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/cli2/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForCpp/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/boto3/backup-2018-11-15/GetBackupVaultNotifications.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupVaultNotifications.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetBackupVaultNotifications.md")
