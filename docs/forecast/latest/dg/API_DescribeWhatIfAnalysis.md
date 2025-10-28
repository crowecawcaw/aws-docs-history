Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeWhatIfAnalysis

Describes the what-if analysis created using the [CreateWhatIfAnalysis](API_CreateWhatIfAnalysis.md "API_CreateWhatIfAnalysis.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the properties provided in the `CreateWhatIfAnalysis` request, this operation lists the following properties:

- `CreationTime`
- `LastModificationTime`
- `Message` - If an error occurred, information about the error.
- `Status`

## Request Syntax

```
{
   "WhatIfAnalysisArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[WhatIfAnalysisArn](#API_DescribeWhatIfAnalysis_RequestSyntax "#API_DescribeWhatIfAnalysis_RequestSyntax")**

The Amazon Resource Name (ARN) of the what-if analysis that you are interested in.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "EstimatedTimeRemainingInMinutes": ***number***,
   "ForecastArn": "***string***",
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "Status": "***string***",
   "TimeSeriesSelector": {
      "TimeSeriesIdentifiers": {
         "DataSource": {
            "S3Config": {
               "KMSKeyArn": "***string***",
               "Path": "***string***",
               "RoleArn": "***string***"
            }
         },
         "Format": "***string***",
         "Schema": {
            "Attributes": [
               {
                  "AttributeName": "***string***",
                  "AttributeType": "***string***"
               }
            ]
         }
      }
   },
   "WhatIfAnalysisArn": "***string***",
   "WhatIfAnalysisName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

When the what-if analysis was created.

Type: Timestamp

**[EstimatedTimeRemainingInMinutes](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

The approximate time remaining to complete the what-if analysis, in minutes.

Type: Long

**[ForecastArn](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

The Amazon Resource Name (ARN) of the what-if forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[LastModificationTime](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

If an error occurred, an informational message about the error.

Type: String

**[Status](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

The status of the what-if analysis. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

###### Note

The `Status` of the what-if analysis must be `ACTIVE` before you can access the
analysis.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

**[TimeSeriesSelector](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

Defines the set of time series that are used to create the forecasts in a `TimeSeriesIdentifiers` object.

The `TimeSeriesIdentifiers` object needs the following information:

- `DataSource`
- `Format`
- `Schema`

Type: [TimeSeriesSelector](API_TimeSeriesSelector.md "API_TimeSeriesSelector.md") object

**[WhatIfAnalysisArn](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

The Amazon Resource Name (ARN) of the what-if analysis.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[WhatIfAnalysisName](#API_DescribeWhatIfAnalysis_ResponseSyntax "#API_DescribeWhatIfAnalysis_ResponseSyntax")**

The name of the what-if analysis.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/cli2/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/boto3/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeWhatIfAnalysis.md")
