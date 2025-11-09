# ListRecoveryPointsByResource

The information about the recovery points of the type specified by a
resource Amazon Resource Name (ARN).

###### Note

For Amazon EFS and Amazon EC2, this action only lists recovery points
created by AWS Backup.

## Request Syntax

```
GET /resources/`resourceArn`/recovery-points/?managedByAWSBackupOnly=`ManagedByAWSBackupOnly`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ManagedByAWSBackupOnly](#API_ListRecoveryPointsByResource_RequestSyntax "#API_ListRecoveryPointsByResource_RequestSyntax")**

This attribute filters recovery points based on ownership.

If this is
set to `TRUE`, the response will contain recovery points associated
with the selected resources that are managed by AWS Backup.

If this is set to `FALSE`, the response will contain all
recovery points associated with the selected resource.

Type: Boolean

**[MaxResults](#API_ListRecoveryPointsByResource_RequestSyntax "#API_ListRecoveryPointsByResource_RequestSyntax")**

The maximum number of items to be returned.

###### Note

Amazon RDS requires a value of at least 20.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRecoveryPointsByResource_RequestSyntax "#API_ListRecoveryPointsByResource_RequestSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

**[resourceArn](#API_ListRecoveryPointsByResource_RequestSyntax "#API_ListRecoveryPointsByResource_RequestSyntax")**

An ARN that uniquely identifies a resource. The format of the ARN depends on the
resource type.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "RecoveryPoints": [
      {
         "BackupSizeBytes": ***number***,
         "BackupVaultName": "***string***",
         "CreationDate": ***number***,
         "EncryptionKeyArn": "***string***",
         "EncryptionKeyType": "***string***",
         "IndexStatus": "***string***",
         "IndexStatusMessage": "***string***",
         "IsParent": ***boolean***,
         "ParentRecoveryPointArn": "***string***",
         "RecoveryPointArn": "***string***",
         "ResourceName": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***",
         "VaultType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRecoveryPointsByResource_ResponseSyntax "#API_ListRecoveryPointsByResource_ResponseSyntax")**

The next item following a partial list of returned items. For example, if a request is
made to return `MaxResults` number of items, `NextToken` allows you
to return more items in your list starting at the location pointed to by the next
token.

Type: String

**[RecoveryPoints](#API_ListRecoveryPointsByResource_ResponseSyntax "#API_ListRecoveryPointsByResource_ResponseSyntax")**

An array of objects that contain detailed information about recovery points of the
specified resource type.

###### Note

Only Amazon EFS and Amazon EC2 recovery points return
BackupVaultName.

Type: Array of [RecoveryPointByResource](API_RecoveryPointByResource.md "API_RecoveryPointByResource.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/cli2/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/boto3/backup-2018-11-15/ListRecoveryPointsByResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByResource.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRecoveryPointsByResource.md")
