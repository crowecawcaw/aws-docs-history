# ListRestoreTestingPlans

Returns a list of restore testing plans.

## Request Syntax

```
GET /restore-testing/plans?MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListRestoreTestingPlans_RequestSyntax "#API_ListRestoreTestingPlans_RequestSyntax")**

The maximum number of items to be returned.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListRestoreTestingPlans_RequestSyntax "#API_ListRestoreTestingPlans_RequestSyntax")**

The next item following a partial list of returned items.
For example, if a request is made to return `MaxResults`
number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the nexttoken.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "RestoreTestingPlans": [
      {
         "CreationTime": ***number***,
         "LastExecutionTime": ***number***,
         "LastUpdateTime": ***number***,
         "RestoreTestingPlanArn": "***string***",
         "RestoreTestingPlanName": "***string***",
         "ScheduleExpression": "***string***",
         "ScheduleExpressionTimezone": "***string***",
         "StartWindowHours": ***number***
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListRestoreTestingPlans_ResponseSyntax "#API_ListRestoreTestingPlans_ResponseSyntax")**

The next item following a partial list of returned items.
For example, if a request is made to return `MaxResults`
number of items, `NextToken` allows you to return more items
in your list starting at the location pointed to by the nexttoken.

Type: String

**[RestoreTestingPlans](#API_ListRestoreTestingPlans_ResponseSyntax "#API_ListRestoreTestingPlans_ResponseSyntax")**

This is a returned list of restore testing plans.

Type: Array of [RestoreTestingPlanForList](API_RestoreTestingPlanForList.md "API_RestoreTestingPlanForList.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/cli2/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/DotNetSDKV3/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForCpp/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/boto3/backup-2018-11-15/ListRestoreTestingPlans.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreTestingPlans.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListRestoreTestingPlans.md")
