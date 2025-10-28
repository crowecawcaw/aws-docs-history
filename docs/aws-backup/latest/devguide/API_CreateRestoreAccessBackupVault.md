# CreateRestoreAccessBackupVault

Creates a restore access backup vault that provides temporary access to recovery points in a logically air-gapped backup vault, subject to MPA approval.

## Request Syntax

```
PUT /restore-access-backup-vaults HTTP/1.1
Content-type: application/json

{
   "BackupVaultName": "`string`",
   "BackupVaultTags": {
      "`string`" : "`string`"
   },
   "CreatorRequestId": "`string`",
   "RequesterComment": "`string`",
   "SourceBackupVaultArn": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[BackupVaultName](#API_CreateRestoreAccessBackupVault_RequestSyntax "#API_CreateRestoreAccessBackupVault_RequestSyntax")**

The name of the backup vault to associate with an MPA approval team.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: No

**[BackupVaultTags](#API_CreateRestoreAccessBackupVault_RequestSyntax "#API_CreateRestoreAccessBackupVault_RequestSyntax")**

Optional tags to assign to the restore access backup vault.

Type: String to string map

Required: No

**[CreatorRequestId](#API_CreateRestoreAccessBackupVault_RequestSyntax "#API_CreateRestoreAccessBackupVault_RequestSyntax")**

A unique string that identifies the request and allows failed requests to be retried without the risk of executing the operation twice.

Type: String

Required: No

**[RequesterComment](#API_CreateRestoreAccessBackupVault_RequestSyntax "#API_CreateRestoreAccessBackupVault_RequestSyntax")**

A comment explaining the reason for requesting restore access to the backup vault.

Type: String

Required: No

**[SourceBackupVaultArn](#API_CreateRestoreAccessBackupVault_RequestSyntax "#API_CreateRestoreAccessBackupVault_RequestSyntax")**

The ARN of the source backup vault containing the recovery points to which temporary access is requested.

Type: String

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationDate": ***number***,
   "RestoreAccessBackupVaultArn": "***string***",
   "RestoreAccessBackupVaultName": "***string***",
   "VaultState": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationDate](#API_CreateRestoreAccessBackupVault_ResponseSyntax "#API_CreateRestoreAccessBackupVault_ResponseSyntax")**

> The date and time when the restore access backup vault was created, in Unix format and Coordinated Universal Time

Type: Timestamp

**[RestoreAccessBackupVaultArn](#API_CreateRestoreAccessBackupVault_ResponseSyntax "#API_CreateRestoreAccessBackupVault_ResponseSyntax")**

The ARN that uniquely identifies the created restore access backup vault.

Type: String

**[RestoreAccessBackupVaultName](#API_CreateRestoreAccessBackupVault_ResponseSyntax "#API_CreateRestoreAccessBackupVault_ResponseSyntax")**

The name of the created restore access backup vault.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[VaultState](#API_CreateRestoreAccessBackupVault_ResponseSyntax "#API_CreateRestoreAccessBackupVault_ResponseSyntax")**

The current state of the restore access backup vault.

Type: String

Valid Values: `CREATING | AVAILABLE | FAILED`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AlreadyExistsException**

The required resource already exists.

**Arn**

**Context**

**CreatorRequestId**

**Type**

HTTP Status Code: 400

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

**LimitExceededException**

A limit in the request has been exceeded; for example, a maximum number of items allowed
in a request.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/cli2/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/DotNetSDKV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/boto3/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateRestoreAccessBackupVault.md")
