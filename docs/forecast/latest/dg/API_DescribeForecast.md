Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribeForecast

Describes a forecast created using the [CreateForecast](API_CreateForecast.md "API_CreateForecast.md") operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the properties provided in the `CreateForecast` request,
this operation lists the following properties:

- `DatasetGroupArn` - The dataset group that provided the training
  data.
- `CreationTime`
- `LastModificationTime`
- `Status`
- `Message` - If an error occurred, information about the error.

## Request Syntax

```
{
   "ForecastArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ForecastArn](#API_DescribeForecast_RequestSyntax "#API_DescribeForecast_RequestSyntax")**

The Amazon Resource Name (ARN) of the forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "DatasetGroupArn": "***string***",
   "EstimatedTimeRemainingInMinutes": ***number***,
   "ForecastArn": "***string***",
   "ForecastName": "***string***",
   "ForecastTypes": [ "***string***" ],
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "PredictorArn": "***string***",
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
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

When the forecast creation task was created.

Type: Timestamp

**[DatasetGroupArn](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The ARN of the dataset group that provided the data used to train the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[EstimatedTimeRemainingInMinutes](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The estimated time remaining in minutes for the forecast job to complete.

Type: Long

**[ForecastArn](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The forecast ARN as specified in the request.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[ForecastName](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The name of the forecast.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[ForecastTypes](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The quantiles at which probabilistic forecasts were generated.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Length Constraints: Minimum length of 2. Maximum length of 4.

Pattern: `(^0?\.\d\d?$|^mean$)`

**[LastModificationTime](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

If an error occurred, an informational message about the error.

Type: String

**[PredictorArn](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The ARN of the predictor used to generate the forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[Status](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The status of the forecast. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`

###### Note

The `Status` of the forecast must be `ACTIVE` before you can query
or export the forecast.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_]+$`

**[TimeSeriesSelector](#API_DescribeForecast_ResponseSyntax "#API_DescribeForecast_ResponseSyntax")**

The time series to include in the forecast.

Type: [TimeSeriesSelector](API_TimeSeriesSelector.md "API_TimeSeriesSelector.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribeForecast.md "../../../goto/cli2/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeForecast.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribeForecast.md "../../../goto/boto3/forecast-2018-06-26/DescribeForecast.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeForecast.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribeForecast.md")
