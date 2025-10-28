# ListProtectedResourcesByBackupVault

This request lists the protected resources corresponding to each backup vault.

## Request Syntax

```
GET /backup-vaults/`backupVaultName`/resources/?backupVaultAccountId=`BackupVaultAccountId`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[BackupVaultAccountId](#API_ListProtectedResourcesByBackupVault_RequestSyntax "#API_ListProtectedResourcesByBackupVault_RequestSyntax")**

The list of protected resources by backup vault within the vault(s) you specify by account ID.

Pattern: `^[0-9]{12}$`

**[backupVaultName](#API_ListProtectedResourcesByBackupVault_RequestSyntax "#API_ListProtectedResourcesByBackupVault_RequestSyntax")**

The list of protected resources by backup vault within the vault(s) you specify by name.

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: Yes

**[MaxResults](#API_ListProtectedResourcesByBackupVault_RequestSyntax "#API_ListProtectedResourcesByBackupVault_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListProtectedResourcesByBackupVault_RequestSyntax "#API_ListProtectedResourcesByBackupVault_RequestSyntax")**

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
   "NextToken": "***string***",
   "Results": [
      {
         "LastBackupTime": ***number***,
         "LastBackupVaultArn": "***string***",
         "LastRecoveryPointArn": "***string***",
         "ResourceArn": "***string***",
         "ResourceName": "***string***",
         "ResourceType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListProtectedResourcesByBackupVault_ResponseSyntax "#API_ListProtectedResourcesByBackupVault_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

**[Results](#API_ListProtectedResourcesByBackupVault_ResponseSyntax "#API_ListProtectedResourcesByBackupVault_ResponseSyntax")**

These are the results returned for the request ListProtectedResourcesByBackupVault.

Type: Array of [ProtectedResource](API_ProtectedResource.md "API_ProtectedResource.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/cli2/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForCpp/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/boto3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListProtectedResourcesByBackupVault.md")
