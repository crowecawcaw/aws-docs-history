# CreateLogicallyAirGappedBackupVault

Creates a logical container to where backups may be copied.

This request includes a name, the Region, the maximum number of retention days, the
minimum number of retention days, and optionally can include tags and a creator request
ID.

###### Note

Do not include sensitive data, such as passport numbers, in the name of a backup
vault.

## Request Syntax

```
PUT /logically-air-gapped-backup-vaults/`backupVaultName` HTTP/1.1
Content-type: application/json

{
   "BackupVaultTags": {
      "`string`" : "`string`"
   },
   "CreatorRequestId": "`string`",
   "EncryptionKeyArn": "`string`",
   "MaxRetentionDays": `number`,
   "MinRetentionDays": `number`
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_CreateLogicallyAirGappedBackupVault_RequestSyntax "#API_CreateLogicallyAirGappedBackupVault_RequestSyntax")**

The name of a logical container where backups are stored. Logically air-gapped
backup vaults are identified by names that are unique to the account used to create
them and the Region where they are created.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[BackupVaultTags](#API_CreateLogicallyAirGappedBackupVault_RequestSyntax "#API_CreateLogicallyAirGappedBackupVault_RequestSyntax")**

The tags to assign to the vault.

Type: String to string map

Required: No

**[CreatorRequestId](#API_CreateLogicallyAirGappedBackupVault_RequestSyntax "#API_CreateLogicallyAirGappedBackupVault_RequestSyntax")**

The ID of the creation request.

This parameter is optional. If used, this parameter must contain
1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

**[EncryptionKeyArn](#API_CreateLogicallyAirGappedBackupVault_RequestSyntax "#API_CreateLogicallyAirGappedBackupVault_RequestSyntax")**

The ARN of the customer-managed KMS key to use for encrypting the logically air-gapped backup vault. If not specified, the vault will be encrypted with an AWS-owned key managed by AWS Backup.

Type: String

Required: No

**[MaxRetentionDays](#API_CreateLogicallyAirGappedBackupVault_RequestSyntax "#API_CreateLogicallyAirGappedBackupVault_RequestSyntax")**

The maximum retention period that the vault retains its recovery points.

Type: Long

Required: Yes

**[MinRetentionDays](#API_CreateLogicallyAirGappedBackupVault_RequestSyntax "#API_CreateLogicallyAirGappedBackupVault_RequestSyntax")**

This setting specifies the minimum retention period
that the vault retains its recovery points.

The minimum value accepted is 7 days.

Type: Long

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "***string***",
   "BackupVaultName": "***string***",
   "CreationDate": ***number***,
   "VaultState": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultArn](#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax "#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax")**

The ARN (Amazon Resource Name) of the vault.

Type: String

**[BackupVaultName](#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax "#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax")**

The name of a logical container where backups are stored. Logically air-gapped
backup vaults are identified by names that are unique to the account used to create
them and the Region where they are created.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[CreationDate](#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax "#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax")**

The date and time when the vault was created.

This value is in Unix format, Coordinated Universal Time (UTC), and accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

**[VaultState](#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax "#API_CreateLogicallyAirGappedBackupVault_ResponseSyntax")**

The current state of the vault.

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

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/cli2/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/DotNetSDKV4/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/boto3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateLogicallyAirGappedBackupVault.md")
