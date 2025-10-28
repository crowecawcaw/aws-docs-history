Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ListExplainabilities

Returns a list of Explainability resources created using the [CreateExplainability](API_CreateExplainability.md "API_CreateExplainability.md") operation. This operation returns a summary for
each Explainability. You can filter the list using an array of [Filter](API_Filter.md "API_Filter.md")
objects.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

To retrieve the complete set of properties for a particular Explainability resource,
use the ARN with the [DescribeExplainability](API_DescribeExplainability.md "API_DescribeExplainability.md") operation.

## Request Syntax

```
{
   "Filters": [
      {
         "Condition": "`string`",
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Filters](#API_ListExplainabilities_RequestSyntax "#API_ListExplainabilities_RequestSyntax")**

An array of filters. For each filter, provide a condition and a match statement. The
condition is either `IS` or `IS_NOT`, which specifies whether to
include or exclude the resources that match the statement from the list. The match
statement consists of a key and a value.

**Filter properties**

- `Condition` - The condition to apply. Valid values are
  `IS` and `IS_NOT`.
- `Key` - The name of the parameter to filter on. Valid values are
  `ResourceArn` and `Status`.
- `Value` - The value to match.

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**[MaxResults](#API_ListExplainabilities_RequestSyntax "#API_ListExplainabilities_RequestSyntax")**

The number of items returned in the response.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListExplainabilities_RequestSyntax "#API_ListExplainabilities_RequestSyntax")**

If the result of the previous request was truncated, the response includes a
NextToken. To retrieve the next set of results, use the token in the next request.
Tokens expire after 24 hours.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

Required: No

## Response Syntax

```
{
   "Explainabilities": [
      {
         "CreationTime": ***number***,
         "ExplainabilityArn": "***string***",
         "ExplainabilityConfig": {
            "TimePointGranularity": "***string***",
            "TimeSeriesGranularity": "***string***"
         },
         "ExplainabilityName": "***string***",
         "LastModificationTime": ***number***,
         "Message": "***string***",
         "ResourceArn": "***string***",
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Explainabilities](#API_ListExplainabilities_ResponseSyntax "#API_ListExplainabilities_ResponseSyntax")**

An array of objects that summarize the properties of each Explainability
resource.

Type: Array of [ExplainabilitySummary](API_ExplainabilitySummary.md "API_ExplainabilitySummary.md") objects

**[NextToken](#API_ListExplainabilities_ResponseSyntax "#API_ListExplainabilities_ResponseSyntax")**

Returns this token if the response is truncated. To retrieve the next set of results,
use the token in the next request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**InvalidNextTokenException**

The token is not valid. Tokens expire after 24 hours.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/ListExplainabilities.md "../../../goto/cli2/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/ListExplainabilities.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForCpp/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForGoV2/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForKotlin/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/ListExplainabilities.md "../../../goto/boto3/forecast-2018-06-26/ListExplainabilities.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ListExplainabilities.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ListExplainabilities.md")
