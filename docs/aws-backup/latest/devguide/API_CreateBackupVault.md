# CreateBackupVault

Creates a logical container where backups are stored. A `CreateBackupVault`
request includes a name, optionally one or more resource tags, an encryption key, and a
request ID.

###### Note

Do not include sensitive data, such as passport numbers, in the name of a backup
vault.

## Request Syntax

```
PUT /backup-vaults/`backupVaultName` HTTP/1.1
Content-type: application/json

{
   "BackupVaultTags": {
      "`string`" : "`string`"
   },
   "CreatorRequestId": "`string`",
   "EncryptionKeyArn": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[backupVaultName](#API_CreateBackupVault_RequestSyntax "#API_CreateBackupVault_RequestSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the AWS
Region where they are created. They consist of letters, numbers, and hyphens.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[BackupVaultTags](#API_CreateBackupVault_RequestSyntax "#API_CreateBackupVault_RequestSyntax")**

The tags to assign to the backup vault.

Type: String to string map

Required: No

**[CreatorRequestId](#API_CreateBackupVault_RequestSyntax "#API_CreateBackupVault_RequestSyntax")**

A unique string that identifies the request and allows failed requests to be retried
without the risk of running the operation twice. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or '-\_.' characters.

Type: String

Required: No

**[EncryptionKeyArn](#API_CreateBackupVault_RequestSyntax "#API_CreateBackupVault_RequestSyntax")**

The server-side encryption key that is used to protect your backups; for example,
`arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultArn": "***string***",
   "BackupVaultName": "***string***",
   "CreationDate": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultArn](#API_CreateBackupVault_ResponseSyntax "#API_CreateBackupVault_ResponseSyntax")**

An Amazon Resource Name (ARN) that uniquely identifies a backup vault; for example,
`arn:aws:backup:us-east-1:123456789012:backup-vault:aBackupVault`.

Type: String

**[BackupVaultName](#API_CreateBackupVault_ResponseSyntax "#API_CreateBackupVault_ResponseSyntax")**

The name of a logical container where backups are stored. Backup vaults are identified
by names that are unique to the account used to create them and the Region where they are
created. They consist of lowercase letters, numbers, and hyphens.

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

**[CreationDate](#API_CreateBackupVault_ResponseSyntax "#API_CreateBackupVault_ResponseSyntax")**

The date and time a backup vault is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationDate` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/CreateBackupVault.md "../../../goto/cli2/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/CreateBackupVault.md "../../../goto/DotNetSDKV3/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForCpp/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForGoV2/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForJavaV2/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForKotlin/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForPHPV3/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/CreateBackupVault.md "../../../goto/boto3/backup-2018-11-15/CreateBackupVault.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/CreateBackupVault.md "../../../goto/SdkForRubyV3/backup-2018-11-15/CreateBackupVault.md")
