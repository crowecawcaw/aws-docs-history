# ListMetricAttributions

Lists metric attributions.

## Request Syntax

```
{
   "datasetGroupArn": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[datasetGroupArn](#API_ListMetricAttributions_RequestSyntax "#API_ListMetricAttributions_RequestSyntax")**

The metric attributions' dataset group Amazon Resource Name (ARN).

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: No

**[maxResults](#API_ListMetricAttributions_RequestSyntax "#API_ListMetricAttributions_RequestSyntax")**

The maximum number of metric attributions to return in one page of results.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[nextToken](#API_ListMetricAttributions_RequestSyntax "#API_ListMetricAttributions_RequestSyntax")**

Specify the pagination token from a previous request to retrieve the next page of results.

Type: String

Length Constraints: Maximum length of 1500.

Pattern: `\p{ASCII}{0,1500}`

Required: No

## Response Syntax

```
{
   "metricAttributions": [
      {
         "creationDateTime": ***number***,
         "failureReason": "***string***",
         "lastUpdatedDateTime": ***number***,
         "metricAttributionArn": "***string***",
         "name": "***string***",
         "status": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[metricAttributions](#API_ListMetricAttributions_ResponseSyntax "#API_ListMetricAttributions_ResponseSyntax")**

The list of metric attributions.

Type: Array of [MetricAttributionSummary](API_MetricAttributionSummary.md "API_MetricAttributionSummary.md") objects

Array Members: Maximum number of 100 items.

**[nextToken](#API_ListMetricAttributions_ResponseSyntax "#API_ListMetricAttributions_ResponseSyntax")**

Specify the pagination token from a previous request to retrieve the next page of results.

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

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/cli2/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/DotNetSDKV3/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForCpp/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForGoV2/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForJavaScriptV3/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForKotlin/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForPHPV3/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/boto3/personalize-2018-05-22/ListMetricAttributions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/ListMetricAttributions.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/ListMetricAttributions.md")
