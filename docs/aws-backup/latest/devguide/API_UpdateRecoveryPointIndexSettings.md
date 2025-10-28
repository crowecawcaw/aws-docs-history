# UpdateRecoveryPointIndexSettings

This operation updates the settings of a recovery point index.

Required: BackupVaultName, RecoveryPointArn, and IAMRoleArn

## Request Syntax

```
POST /backup-vaults/`backupVaultName`/recovery-points/`recoveryPointArn`/index HTTP/1.1
Content-type: application/json

{
   "IamRoleArn": "`string`",
   "Index": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_UpdateRecoveryPointIndexSettings_RequestSyntax "#API_UpdateRecoveryPointIndexSettings_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the Region where they are
created.

Accepted characters include lowercase letters, numbers, and hyphens.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[recoveryPointArn](#API_UpdateRecoveryPointIndexSettings_RequestSyntax "#API_UpdateRecoveryPointIndexSettings_RequestSyntax")**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[IamRoleArn](#API_UpdateRecoveryPointIndexSettings_RequestSyntax "#API_UpdateRecoveryPointIndexSettings_RequestSyntax")**

This specifies the IAM role ARN used for this operation.

For example, arn:aws:iam::123456789012:role/S3Access

Type: String

Required: No

**[Index](#API_UpdateRecoveryPointIndexSettings_RequestSyntax "#API_UpdateRecoveryPointIndexSettings_RequestSyntax")**

Index can have 1 of 2 possible values, either `ENABLED` or
`DISABLED`.

To create a backup index for an eligible `ACTIVE` recovery point
that does not yet have a backup index, set value to `ENABLED`.

To delete a backup index, set value to `DISABLED`.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultName": "***string***",
   "Index": "***string***",
   "IndexStatus": "***string***",
   "RecoveryPointArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultName](#API_UpdateRecoveryPointIndexSettings_ResponseSyntax "#API_UpdateRecoveryPointIndexSettings_ResponseSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the Region where they are
created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[Index](#API_UpdateRecoveryPointIndexSettings_ResponseSyntax "#API_UpdateRecoveryPointIndexSettings_ResponseSyntax")**

Index can have 1 of 2 possible values, either `ENABLED` or
`DISABLED`.

A value of `ENABLED` means a backup index for an eligible `ACTIVE`
recovery point has been created.

A value of `DISABLED` means a backup index was deleted.

Type: String

Valid Values: `ENABLED | DISABLED`

**[IndexStatus](#API_UpdateRecoveryPointIndexSettings_ResponseSyntax "#API_UpdateRecoveryPointIndexSettings_ResponseSyntax")**

This is the current status for the backup index associated
with the specified recovery point.

Statuses are: `PENDING` | `ACTIVE` | `FAILED` | `DELETING`

A recovery point with an index that has the status of `ACTIVE`
can be included in a search.

Type: String

Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

**[RecoveryPointArn](#API_UpdateRecoveryPointIndexSettings_ResponseSyntax "#API_UpdateRecoveryPointIndexSettings_ResponseSyntax")**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**InvalidRequestException**

Indicates that something is wrong with the input to the request. For example, a
parameter is of the wrong type.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/cli2/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/boto3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRecoveryPointIndexSettings.md")
