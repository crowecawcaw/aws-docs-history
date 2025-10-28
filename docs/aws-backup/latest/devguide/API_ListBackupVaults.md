# ListBackupVaults

Returns a list of recovery point storage containers along with information about
them.

## Request Syntax

```
GET /backup-vaults/?maxResults=`MaxResults`&nextToken=`NextToken`&shared=`ByShared`&vaultType=`ByVaultType` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ByShared](#API_ListBackupVaults_RequestSyntax "#API_ListBackupVaults_RequestSyntax")**

This parameter will sort the list of vaults by shared vaults.

**[ByVaultType](#API_ListBackupVaults_RequestSyntax "#API_ListBackupVaults_RequestSyntax")**

This parameter will sort the list of vaults by vault type.

Valid Values: `BACKUP_VAULT | LOGICALLY_AIR_GAPPED_BACKUP_VAULT | RESTORE_ACCESS_BACKUP_VAULT`

**[MaxResults](#API_ListBackupVaults_RequestSyntax "#API_ListBackupVaults_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListBackupVaults_RequestSyntax "#API_ListBackupVaults_RequestSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupVaultList": [
      {
         "BackupVaultArn": "***string***",
         "BackupVaultName": "***string***",
         "CreationDate": ***number***,
         "CreatorRequestId": "***string***",
         "EncryptionKeyArn": "***string***",
         "LockDate": ***number***,
         "Locked": ***boolean***,
         "MaxRetentionDays": ***number***,
         "MinRetentionDays": ***number***,
         "NumberOfRecoveryPoints": ***number***,
         "VaultState": "***string***",
         "VaultType": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupVaultList](#API_ListBackupVaults_ResponseSyntax "#API_ListBackupVaults_ResponseSyntax")**

An array of backup vault list members containing vault metadata, including Amazon
Resource Name (ARN), display name, creation date, number of saved recovery points, and
encryption information if the resources saved in the backup vault are encrypted.

Type: Array of [BackupVaultListMember](API_BackupVaultListMember.md "API_BackupVaultListMember.md") objects

**[NextToken](#API_ListBackupVaults_ResponseSyntax "#API_ListBackupVaults_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListBackupVaults.md "../../../goto/cli2/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListBackupVaults.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForCpp/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListBackupVaults.md "../../../goto/boto3/backup-2018-11-15/ListBackupVaults.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListBackupVaults.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListBackupVaults.md")
