# ListBackupPlanVersions

Returns version metadata of your backup plans, including Amazon Resource Names (ARNs),
backup plan IDs, creation and deletion dates, plan names, and version IDs.

## Request Syntax

```
GET /backup/plans/`backupPlanId`/versions/?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[backupPlanId](#API_ListBackupPlanVersions_RequestSyntax "#API_ListBackupPlanVersions_RequestSyntax")**

Uniquely identifies a backup plan.

Required: Yes

**[MaxResults](#API_ListBackupPlanVersions_RequestSyntax "#API_ListBackupPlanVersions_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListBackupPlanVersions_RequestSyntax "#API_ListBackupPlanVersions_RequestSyntax")**

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
   "BackupPlanVersionsList": [
      {
         "AdvancedBackupSettings": [
            {
               "BackupOptions": {
                  "***string***" : "***string***"
               },
               "ResourceType": "***string***"
            }
         ],
         "BackupPlanArn": "***string***",
         "BackupPlanId": "***string***",
         "BackupPlanName": "***string***",
         "CreationDate": ***number***,
         "CreatorRequestId": "***string***",
         "DeletionDate": ***number***,
         "LastExecutionDate": ***number***,
         "VersionId": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupPlanVersionsList](#API_ListBackupPlanVersions_ResponseSyntax "#API_ListBackupPlanVersions_ResponseSyntax")**

An array of version list items containing metadata about your backup plans.

Type: Array of [BackupPlansListMember](API_BackupPlansListMember.md "API_BackupPlansListMember.md") objects

**[NextToken](#API_ListBackupPlanVersions_ResponseSyntax "#API_ListBackupPlanVersions_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/cli2/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/DotNetSDKV4/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForCpp/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/boto3/backup-2018-11-15/ListBackupPlanVersions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListBackupPlanVersions.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListBackupPlanVersions.md")
