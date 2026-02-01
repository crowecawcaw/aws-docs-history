Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CreateAutoPredictor

Creates an Amazon Forecast predictor.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

Amazon Forecast creates predictors with AutoPredictor, which involves applying the
optimal combination of algorithms to each time series in your datasets. You can use
CreateAutoPredictor to create new predictors or upgrade/retrain
existing predictors.

**Creating new predictors**

The following parameters are required when creating a new predictor:

- `PredictorName` - A unique name for the predictor.
- `DatasetGroupArn` - The ARN of the dataset group used to train the
  predictor.
- `ForecastFrequency` - The granularity of your forecasts (hourly,
  daily, weekly, etc).
- `ForecastHorizon` - The number of time-steps that the model
  predicts. The forecast horizon is also called the prediction length.
  When creating a new predictor, do not specify a value for
  `ReferencePredictorArn`.

**Upgrading and retraining predictors**

The following parameters are required when retraining or upgrading a predictor:

- `PredictorName` - A unique name for the predictor.
- `ReferencePredictorArn` - The ARN of the predictor to retrain or
  upgrade.
  When upgrading or retraining a predictor, only specify values for the
  `ReferencePredictorArn` and `PredictorName`.

## Request Syntax

```
{
   "DataConfig": {
      "AdditionalDatasets": [
         {
            "Configuration": {
               "`string`" : [ "`string`" ]
            },
            "Name": "`string`"
         }
      ],
      "AttributeConfigs": [
         {
            "AttributeName": "`string`",
            "Transformations": {
               "`string`" : "`string`"
            }
         }
      ],
      "DatasetGroupArn": "`string`"
   },
   "EncryptionConfig": {
      "KMSKeyArn": "`string`",
      "RoleArn": "`string`"
   },
   "ExplainPredictor": `boolean`,
   "ForecastDimensions": [ "`string`" ],
   "ForecastFrequency": "`string`",
   "ForecastHorizon": `number`,
   "ForecastTypes": [ "`string`" ],
   "MonitorConfig": {
      "MonitorName": "`string`"
   },
   "OptimizationMetric": "`string`",
   "PredictorName": "`string`",
   "ReferencePredictorArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "TimeAlignmentBoundary": {
      "DayOfMonth": `number`,
      "DayOfWeek": "`string`",
      "Hour": `number`,
      "Month": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DataConfig](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The data configuration for your dataset group and any additional datasets.

Type: [DataConfig](API_DataConfig.md "API_DataConfig.md") object

Required: No

**[EncryptionConfig](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

An AWS Key Management Service (KMS) key and an AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to
access the key. You can specify this optional object in the
[CreateDataset](API_CreateDataset.md "API_CreateDataset.md") and [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") requests.

Type: [EncryptionConfig](API_EncryptionConfig.md "API_EncryptionConfig.md") object

Required: No

**[ExplainPredictor](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

Create an Explainability resource for the predictor.

Type: Boolean

Required: No

**[ForecastDimensions](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

An array of dimension (field) names that specify how to group the generated
forecast.

For example, if you are generating forecasts for item sales across all your stores,
and your dataset contains a `store_id` field, you would specify
`store_id` as a dimension to group sales forecasts for each store.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: No

**[ForecastFrequency](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The frequency of predictions in a forecast.

Valid intervals are an integer followed by Y (Year), M (Month), W (Week), D (Day), H (Hour), and min (Minute). For example,
"1D" indicates every day and "15min" indicates every 15 minutes. You cannot specify a value that would overlap with the next larger frequency. That means, for example, you cannot specify a frequency of 60 minutes, because that is equivalent to 1 hour. The valid values for each frequency are the following:

- Minute - 1-59
- Hour - 1-23
- Day - 1-6
- Week - 1-4
- Month - 1-11
- Year - 1

Thus, if you want every other week forecasts, specify "2W". Or, if you want quarterly forecasts, you specify "3M".

The frequency must be greater than or equal to the TARGET_TIME_SERIES dataset
frequency.

When a RELATED_TIME_SERIES dataset is provided, the frequency must be equal to the
RELATED_TIME_SERIES dataset frequency.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5.

Pattern: `^Y|M|W|D|H|30min|15min|10min|5min|1min$`

Required: No

**[ForecastHorizon](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The number of time-steps that the model predicts. The forecast horizon is also called
the prediction length.

The maximum forecast horizon is the lesser of 500 time-steps or 1/4 of the
TARGET_TIME_SERIES dataset length. If you are retraining an existing AutoPredictor, then
the maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the
TARGET_TIME_SERIES dataset length.

If you are upgrading to an AutoPredictor or retraining an existing AutoPredictor, you
cannot update the forecast horizon parameter. You can meet this requirement by providing
longer time-series in the dataset.

Type: Integer

Required: No

**[ForecastTypes](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The forecast types used to train a predictor. You can specify up to five forecast
types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or
higher. You can also specify the mean forecast with `mean`.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Length Constraints: Minimum length of 2. Maximum length of 4.

Pattern: `(^0?\.\d\d?$|^mean$)`

Required: No

**[MonitorConfig](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The configuration details for predictor monitoring. Provide a name for the monitor resource to enable predictor monitoring.

Predictor monitoring allows you to see how your predictor's performance changes over time.
For more information, see [Predictor Monitoring](predictor-monitoring.md "predictor-monitoring.md").

Type: [MonitorConfig](API_MonitorConfig.md "API_MonitorConfig.md") object

Required: No

**[OptimizationMetric](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The accuracy metric used to optimize the predictor.

Type: String

Valid Values: `WAPE | RMSE | AverageWeightedQuantileLoss | MASE | MAPE`

Required: No

**[PredictorName](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

A unique name for the predictor

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**[ReferencePredictorArn](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The ARN of the predictor to retrain or upgrade. This parameter is only used when
retraining or upgrading a predictor. When creating a new predictor, do not specify a
value for this parameter.

When upgrading or retraining a predictor, only specify values for the
`ReferencePredictorArn` and `PredictorName`. The value for
`PredictorName` must be a unique predictor name.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**[Tags](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

Optional metadata to help you categorize and organize your predictors. Each tag
consists of a key and an optional value, both of which you define. Tag keys and values
are case sensitive.

The following restrictions apply to tags:

- For each resource, each tag key must be unique and each tag key must have one
  value.
- Maximum number of tags per resource: 50.
- Maximum key length: 128 Unicode characters in UTF-8.
- Maximum value length: 256 Unicode characters in UTF-8.
- Accepted characters: all letters and numbers, spaces representable in UTF-8,
  and + - = . \_ : / @. If your tagging schema is used across other services and
  resources, the character restrictions of those services also apply.
- Key prefixes cannot include any upper or lowercase combination of
  `aws:` or `AWS:`. Values can have this prefix. If a
  tag value has `aws` as its prefix but the key does not, Forecast
  considers it to be a user tag and will count against the limit of 50 tags. Tags
  with only the key prefix of `aws` do not count against your tags per
  resource limit. You cannot edit or delete tag keys with this prefix.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[TimeAlignmentBoundary](#API_CreateAutoPredictor_RequestSyntax "#API_CreateAutoPredictor_RequestSyntax")**

The time boundary Forecast uses to align and aggregate any data that doesn't align with your forecast frequency. Provide the unit of time and the time boundary as a key value pair.
For more information on specifying a time boundary, see [Specifying a Time Boundary](data-aggregation.md#specifying-time-boundary "data-aggregation.md#specifying-time-boundary").
If you
don't provide a time boundary, Forecast uses a set of [Default Time Boundaries](data-aggregation.md#default-time-boundaries "data-aggregation.md#default-time-boundaries").

Type: [TimeAlignmentBoundary](API_TimeAlignmentBoundary.md "API_TimeAlignmentBoundary.md") object

Required: No

## Response Syntax

```
{
   "PredictorArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PredictorArn](#API_CreateAutoPredictor_ResponseSyntax "#API_CreateAutoPredictor_ResponseSyntax")**

The Amazon Resource Name (ARN) of the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of resources per account has been exceeded.

HTTP Status Code: 400

**ResourceAlreadyExistsException**

There is already a resource with this name. Try again with a different name.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/cli2/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForCpp/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForGoV2/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForKotlin/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/boto3/forecast-2018-06-26/CreateAutoPredictor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateAutoPredictor.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CreateAutoPredictor.md")
