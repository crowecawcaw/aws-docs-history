# ListRestoreTestingSelections

Returns a list of restore testing selections. Can be filtered
by `MaxResults` and `RestoreTestingPlanName`.

## Request Syntax

```
GET /restore-testing/plans/`RestoreTestingPlanName`/selections?MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListRestoreTestingSelections_RequestSyntax "#API_ListRestoreTestingSelections_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRestoreTestingSelections_RequestSyntax "#API_ListRestoreTestingSelections_RequestSyntax")**

The next item following a partial list of returned items.
For example, if a request is made to return `MaxResults`
number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the nexttoken.

**[RestoreTestingPlanName](#API_ListRestoreTestingSelections_RequestSyntax "#API_ListRestoreTestingSelections_RequestSyntax")**

Returns restore testing selections by the specified restore testing
plan name.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "RestoreTestingSelections": [
      {
         "CreationTime": ***number***,
         "IamRoleArn": "***string***",
         "ProtectedResourceType": "***string***",
         "RestoreTestingPlanName": "***string***",
         "RestoreTestingSelectionName": "***string***",
         "ValidationWindowHours": ***number***
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRestoreTestingSelections_ResponseSyntax "#API_ListRestoreTestingSelections_ResponseSyntax")**

The next item following a partial list of returned items. For example,
if a request is made to return `MaxResults` number of items,
`NextToken` allows you to return more items in your list
starting at the location pointed to by the nexttoken.

Type: String

**[RestoreTestingSelections](#API_ListRestoreTestingSelections_ResponseSyntax "#API_ListRestoreTestingSelections_ResponseSyntax")**

The returned restore testing selections associated with the
restore testing plan.

Type: Array of [RestoreTestingSelectionForList](API_RestoreTestingSelectionForList.md "API_RestoreTestingSelectionForList.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/cli2/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/boto3/backup-2018-11-15/ListRestoreTestingSelections.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreTestingSelections.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreTestingSelections.md")
