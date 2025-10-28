# ListSchedules

Lists the DataBrew schedules that are defined.

## Request Syntax

```
GET /schedules?jobName=`JobName`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[JobName](#API_ListSchedules_RequestSyntax "#API_ListSchedules_RequestSyntax")**

The name of the job that these schedules apply to.

Length Constraints: Minimum length of 1. Maximum length of 240.

**[MaxResults](#API_ListSchedules_RequestSyntax "#API_ListSchedules_RequestSyntax")**

The maximum number of results to return in this request.

Valid Range: Minimum value of 1. Maximum value of 100.

**[NextToken](#API_ListSchedules_RequestSyntax "#API_ListSchedules_RequestSyntax")**

The token returned by a previous call to retrieve the next set of results.

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Schedules": [
      {
         "AccountId": "***string***",
         "CreateDate": ***number***,
         "CreatedBy": "***string***",
         "CronExpression": "***string***",
         "JobNames": [ "***string***" ],
         "LastModifiedBy": "***string***",
         "LastModifiedDate": ***number***,
         "Name": "***string***",
         "ResourceArn": "***string***",
         "Tags": {
            "***string***" : "***string***"
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Schedules](#API_ListSchedules_ResponseSyntax "#API_ListSchedules_ResponseSyntax")**

A list of schedules that are defined.

Type: Array of [Schedule](API_Schedule.md "API_Schedule.md") objects

**[NextToken](#API_ListSchedules_ResponseSyntax "#API_ListSchedules_ResponseSyntax")**

A token that you can use in a subsequent call to retrieve the next set of
results.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/ListSchedules.md "../../../goto/cli2/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/ListSchedules.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForCpp/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForGoV2/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForKotlin/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/ListSchedules.md "../../../goto/boto3/databrew-2017-07-25/ListSchedules.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ListSchedules.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ListSchedules.md")
