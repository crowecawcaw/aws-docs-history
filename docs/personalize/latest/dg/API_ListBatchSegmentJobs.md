# ListBatchSegmentJobs

Gets a list of the batch segment jobs that have been performed off of a solution
version that you specify.

## Request Syntax

```
{
   "maxResults": `number`,
   "nextToken": "`string`",
   "solutionVersionArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[maxResults](#API_ListBatchSegmentJobs_RequestSyntax "#API_ListBatchSegmentJobs_RequestSyntax")**

The maximum number of batch segment job results to return in each page. The default
value is 100.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListBatchSegmentJobs_RequestSyntax "#API_ListBatchSegmentJobs_RequestSyntax")**

The token to request the next page of results.

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

**[solutionVersionArn](#API_ListBatchSegmentJobs_RequestSyntax "#API_ListBatchSegmentJobs_RequestSyntax")**

The Amazon Resource Name (ARN) of the solution version that the batch segment jobs used to generate batch segments.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

## Response Syntax

```
{
   "batchSegmentJobs": [
      {
         "batchSegmentJobArn": "***string***",
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "jobName": "***string***",
         "lastUpdatedDateTime": ***number***,
         "solutionVersionArn": "***string***",
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[batchSegmentJobs](#API_ListBatchSegmentJobs_ResponseSyntax "#API_ListBatchSegmentJobs_ResponseSyntax")**

A list containing information on each job that is returned.

Type: Array of [BatchSegmentJobSummary](API_BatchSegmentJobSummary.md "API_BatchSegmentJobSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListBatchSegmentJobs_ResponseSyntax "#API_ListBatchSegmentJobs_ResponseSyntax")**

The token to use to retrieve the next page of results. The value is `null` when
there are no more results to return.

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/cli2/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/DotNetSDKV4/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/boto3/personalize-2018-05-22/ListBatchSegmentJobs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListBatchSegmentJobs.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListBatchSegmentJobs.md")
