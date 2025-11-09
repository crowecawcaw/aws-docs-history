Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ListWhatIfForecastExports

Returns a list of what-if forecast exports created using the [CreateWhatIfForecastExport](API_CreateWhatIfForecastExport.md "API_CreateWhatIfForecastExport.md") operation. For each what-if forecast export,
this operation returns a summary of its properties, including its Amazon Resource Name (ARN). You can retrieve the complete set of properties by using the
what-if forecast export ARN with the [DescribeWhatIfForecastExport](API_DescribeWhatIfForecastExport.md "API_DescribeWhatIfForecastExport.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

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

**[Filters](#API_ListWhatIfForecastExports_RequestSyntax "#API_ListWhatIfForecastExports_RequestSyntax")**

An array of filters. For each filter, you provide a condition and a match statement. The condition is either
`IS` or `IS_NOT`, which specifies whether to include or exclude the what-if forecast
export jobs that match the statement from the list, respectively. The match statement consists of a key and a
value.

**Filter properties**

- `Condition` - The condition to apply. Valid values are `IS` and
  `IS_NOT`. To include the forecast export jobs that match the statement,
  specify `IS`. To exclude matching forecast export jobs, specify
  `IS_NOT`.
- `Key` - The name of the parameter to filter on. Valid values are
  `WhatIfForecastExportArn` and `Status`.
- `Value` - The value to match.

For example, to list all jobs that export a forecast named
_electricityWIFExport_, specify the following filter:

`"Filters": [ { "Condition": "IS", "Key": "WhatIfForecastExportArn", "Value":
 "arn:aws:forecast:us-west-2:<acct-id>:forecast/electricityWIFExport" } ]`

Type: Array of [Filter](API_Filter.md "API_Filter.md") objects

Required: No

**[MaxResults](#API_ListWhatIfForecastExports_RequestSyntax "#API_ListWhatIfForecastExports_RequestSyntax")**

The number of items to return in the response.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListWhatIfForecastExports_RequestSyntax "#API_ListWhatIfForecastExports_RequestSyntax")**

If the result of the previous request was truncated, the response includes a `NextToken`. To retrieve the next set of results, use the token in the next  request. Tokens expire after 24 hours.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "WhatIfForecastExports": [
      {
         "CreationTime": ***number***,
         "Destination": {
            "S3Config": {
               "KMSKeyArn": "***string***",
               "Path": "***string***",
               "RoleArn": "***string***"
            }
         },
         "LastModificationTime": ***number***,
         "Message": "***string***",
         "Status": "***string***",
         "WhatIfForecastArns": [ "***string***" ],
         "WhatIfForecastExportArn": "***string***",
         "WhatIfForecastExportName": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListWhatIfForecastExports_ResponseSyntax "#API_ListWhatIfForecastExports_ResponseSyntax")**

If the response is truncated, Forecast returns this token. To retrieve the next set of results, use the token in the next request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 3000.

Pattern: `.+`

**[WhatIfForecastExports](#API_ListWhatIfForecastExports_ResponseSyntax "#API_ListWhatIfForecastExports_ResponseSyntax")**

An array of `WhatIfForecastExports` objects that describe the matched forecast exports.

Type: Array of [WhatIfForecastExportSummary](API_WhatIfForecastExportSummary.md "API_WhatIfForecastExportSummary.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/cli2/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForCpp/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForGoV2/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForKotlin/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/boto3/forecast-2018-06-26/ListWhatIfForecastExports.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ListWhatIfForecastExports.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ListWhatIfForecastExports.md")
