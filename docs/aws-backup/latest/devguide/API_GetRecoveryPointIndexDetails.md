# GetRecoveryPointIndexDetails

This operation returns the metadata and details specific to
the backup index associated with the specified recovery point.

## Request Syntax

```
GET /backup-vaults/`backupVaultName`/recovery-points/`recoveryPointArn`/index HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_GetRecoveryPointIndexDetails_RequestSyntax "#API_GetRecoveryPointIndexDetails_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the Region where they are
created.

Accepted characters include lowercase letters, numbers, and hyphens.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[recoveryPointArn](#API_GetRecoveryPointIndexDetails_RequestSyntax "#API_GetRecoveryPointIndexDetails_RequestSyntax")**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "***string***",
   "IndexCompletionDate": ***number***,
   "IndexCreationDate": ***number***,
   "IndexDeletionDate": ***number***,
   "IndexStatus": "***string***",
   "IndexStatusMessage": "***string***",
   "RecoveryPointArn": "***string***",
   "SourceResourceArn": "***string***",
   "TotalItemsIndexed": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultArn](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

An ARN that uniquely identifies the backup vault where the recovery
point index is stored.

For example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

**[IndexCompletionDate](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

The date and time that a backup index finished creation, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[IndexCreationDate](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

The date and time that a backup index was created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[IndexDeletionDate](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

The date and time that a backup index was deleted, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

**[IndexStatus](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

This is the current status for the backup index associated
with the specified recovery point.

Statuses are: `PENDING` | `ACTIVE` | `FAILED` | `DELETING`

A recovery point with an index that has the status of `ACTIVE`
can be included in a search.

Type: String

Valid Values: `PENDING | ACTIVE | FAILED | DELETING`

**[IndexStatusMessage](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

A detailed message explaining the status of a backup index associated
with the recovery point.

Type: String

**[RecoveryPointArn](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

An ARN that uniquely identifies a recovery point; for example,
`arn:aws:backup:us-east-1:123456789012:recovery-point:1EB3B5E7-9EB0-435A-A80B-108B488B0D45`.

Type: String

**[SourceResourceArn](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

A string of the Amazon Resource Name (ARN) that uniquely identifies
the source resource.

Type: String

**[TotalItemsIndexed](#API_GetRecoveryPointIndexDetails_ResponseSyntax "#API_GetRecoveryPointIndexDetails_ResponseSyntax")**

Count of items within the backup index associated with the
recovery point.

Type: Long

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/cli2/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/DotNetSDKV4/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForCpp/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForGoV2/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForJavaV2/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForKotlin/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForPHPV3/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/boto3/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/GetRecoveryPointIndexDetails.md "../../../goto/SdkForRubyV3/backup-2018-11-15/GetRecoveryPointIndexDetails.md")
