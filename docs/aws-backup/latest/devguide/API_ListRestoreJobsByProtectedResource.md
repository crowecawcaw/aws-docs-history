# ListRestoreJobsByProtectedResource

This returns restore jobs that contain the specified protected resource.

You must include `ResourceArn`. You can optionally include
`NextToken`, `ByStatus`, `MaxResults`,
`ByRecoveryPointCreationDateAfter` , and
`ByRecoveryPointCreationDateBefore`.

## Request Syntax

```
GET /resources/`resourceArn`/restore-jobs/?maxResults=`MaxResults`&nextToken=`NextToken`&recoveryPointCreationDateAfter=`ByRecoveryPointCreationDateAfter`&recoveryPointCreationDateBefore=`ByRecoveryPointCreationDateBefore`&status=`ByStatus` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ByRecoveryPointCreationDateAfter](#API_ListRestoreJobsByProtectedResource_RequestSyntax "#API_ListRestoreJobsByProtectedResource_RequestSyntax")**

Returns only restore jobs of recovery points that were created after the specified date.

**[ByRecoveryPointCreationDateBefore](#API_ListRestoreJobsByProtectedResource_RequestSyntax "#API_ListRestoreJobsByProtectedResource_RequestSyntax")**

Returns only restore jobs of recovery points that were created before the specified date.

**[ByStatus](#API_ListRestoreJobsByProtectedResource_RequestSyntax "#API_ListRestoreJobsByProtectedResource_RequestSyntax")**

Returns only restore jobs associated with the specified job status.

Valid Values: `PENDING | RUNNING | COMPLETED | ABORTED | FAILED`

**[MaxResults](#API_ListRestoreJobsByProtectedResource_RequestSyntax "#API_ListRestoreJobsByProtectedResource_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRestoreJobsByProtectedResource_RequestSyntax "#API_ListRestoreJobsByProtectedResource_RequestSyntax")**

The next item following a partial list of returned items. For example,
if a request ismade to return `MaxResults` number of items,
`NextToken` allows you to return more items in your list
starting at the location pointed to by the next token.

**[resourceArn](#API_ListRestoreJobsByProtectedResource_RequestSyntax "#API_ListRestoreJobsByProtectedResource_RequestSyntax")**

Returns only restore jobs that match the specified resource
Amazon Resource Name (ARN).

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "RestoreJobs": [
      {
         "AccountId": "***string***",
         "BackupSizeInBytes": ***number***,
         "BackupVaultArn": "***string***",
         "CompletionDate": ***number***,
         "CreatedBy": {
            "RestoreTestingPlanArn": "***string***"
         },
         "CreatedResourceArn": "***string***",
         "CreationDate": ***number***,
         "DeletionStatus": "***string***",
         "DeletionStatusMessage": "***string***",
         "ExpectedCompletionTimeMinutes": ***number***,
         "IamRoleArn": "***string***",
         "IsParent": ***boolean***,
         "ParentJobId": "***string***",
         "PercentDone": "***string***",
         "RecoveryPointArn": "***string***",
         "RecoveryPointCreationDate": ***number***,
         "ResourceType": "***string***",
         "RestoreJobId": "***string***",
         "SourceResourceArn": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***",
         "ValidationStatus": "***string***",
         "ValidationStatusMessage": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRestoreJobsByProtectedResource_ResponseSyntax "#API_ListRestoreJobsByProtectedResource_ResponseSyntax")**

The next item following a partial list of returned items. For example,
if a request is made to return `MaxResults` number of items,
`NextToken` allows youto return more items in your list starting
at the location pointed to by the next token

Type: String

**[RestoreJobs](#API_ListRestoreJobsByProtectedResource_ResponseSyntax "#API_ListRestoreJobsByProtectedResource_ResponseSyntax")**

An array of objects that contain detailed information about
jobs to restore saved resources.>

Type: Array of [RestoreJobsListMember](API_RestoreJobsListMember.md "API_RestoreJobsListMember.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/cli2/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/boto3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreJobsByProtectedResource.md")
