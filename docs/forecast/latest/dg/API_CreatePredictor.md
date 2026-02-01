Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CreatePredictor

###### Note

This operation creates a legacy predictor that does not include all the predictor
functionalities provided by Amazon Forecast. To create a predictor that is compatible with all
aspects of Forecast, use [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md").

Creates an Amazon Forecast predictor.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In the request, provide a dataset group and either specify an algorithm or let Amazon Forecast
choose an algorithm for you using AutoML. If you specify an algorithm, you also can override
algorithm-specific hyperparameters.

Amazon Forecast uses the algorithm to train a predictor using the latest version of the datasets
in the specified dataset group. You can then generate a forecast using the [CreateForecast](API_CreateForecast.md "API_CreateForecast.md") operation.

To see the evaluation metrics, use the [GetAccuracyMetrics](API_GetAccuracyMetrics.md "API_GetAccuracyMetrics.md") operation.

You can specify a featurization configuration to fill and aggregate the data fields in the
`TARGET_TIME_SERIES` dataset to improve model training. For more information, see
[FeaturizationConfig](API_FeaturizationConfig.md "API_FeaturizationConfig.md").

For RELATED_TIME_SERIES datasets, `CreatePredictor` verifies that the
`DataFrequency` specified when the dataset was created matches the
`ForecastFrequency`. TARGET_TIME_SERIES datasets don't have this restriction.
Amazon Forecast also verifies the delimiter and timestamp format. For more information, see [Importing Datasets](howitworks-datasets-groups.md "howitworks-datasets-groups.md").

By default, predictors are trained and evaluated at the 0.1 (P10), 0.5 (P50), and 0.9
(P90) quantiles. You can choose custom forecast types to train and evaluate your predictor by
setting the `ForecastTypes`.

**AutoML**

If you want Amazon Forecast to evaluate each algorithm and choose the one that minimizes the
`objective function`, set `PerformAutoML` to `true`. The
`objective function` is defined as the mean of the weighted losses over the
forecast types. By default, these are the p10, p50, and p90 quantile losses. For more
information, see [EvaluationResult](API_EvaluationResult.md "API_EvaluationResult.md").

When AutoML is enabled, the following properties are disallowed:

- `AlgorithmArn`
- `HPOConfig`
- `PerformHPO`
- `TrainingParameters`
  To get a list of all of your predictors, use the [ListPredictors](API_ListPredictors.md "API_ListPredictors.md")
  operation.

###### Note

Before you can use the predictor to create a forecast, the `Status` of the
predictor must be `ACTIVE`, signifying that training has completed. To get the
status, use the [DescribePredictor](API_DescribePredictor.md "API_DescribePredictor.md") operation.

## Request Syntax

```
{
   "AlgorithmArn": "`string`",
   "AutoMLOverrideStrategy": "`string`",
   "EncryptionConfig": {
      "KMSKeyArn": "`string`",
      "RoleArn": "`string`"
   },
   "EvaluationParameters": {
      "BackTestWindowOffset": `number`,
      "NumberOfBacktestWindows": `number`
   },
   "FeaturizationConfig": {
      "Featurizations": [
         {
            "AttributeName": "`string`",
            "FeaturizationPipeline": [
               {
                  "FeaturizationMethodName": "`string`",
                  "FeaturizationMethodParameters": {
                     "`string`" : "`string`"
                  }
               }
            ]
         }
      ],
      "ForecastDimensions": [ "`string`" ],
      "ForecastFrequency": "`string`"
   },
   "ForecastHorizon": `number`,
   "ForecastTypes": [ "`string`" ],
   "HPOConfig": {
      "ParameterRanges": {
         "CategoricalParameterRanges": [
            {
               "Name": "`string`",
               "Values": [ "`string`" ]
            }
         ],
         "ContinuousParameterRanges": [
            {
               "MaxValue": `number`,
               "MinValue": `number`,
               "Name": "`string`",
               "ScalingType": "`string`"
            }
         ],
         "IntegerParameterRanges": [
            {
               "MaxValue": `number`,
               "MinValue": `number`,
               "Name": "`string`",
               "ScalingType": "`string`"
            }
         ]
      }
   },
   "InputDataConfig": {
      "DatasetGroupArn": "`string`",
      "SupplementaryFeatures": [
         {
            "Name": "`string`",
            "Value": "`string`"
         }
      ]
   },
   "OptimizationMetric": "`string`",
   "PerformAutoML": `boolean`,
   "PerformHPO": `boolean`,
   "PredictorName": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "TrainingParameters": {
      "`string`" : "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AlgorithmArn](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

The Amazon Resource Name (ARN) of the algorithm to use for model training. Required if
`PerformAutoML` is not set to `true`.

###### Supported algorithms:

- `arn:aws:forecast:::algorithm/ARIMA`
- `arn:aws:forecast:::algorithm/CNN-QR`
- `arn:aws:forecast:::algorithm/Deep_AR_Plus`
- `arn:aws:forecast:::algorithm/ETS`
- `arn:aws:forecast:::algorithm/NPTS`
- `arn:aws:forecast:::algorithm/Prophet`

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**[AutoMLOverrideStrategy](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

###### Note

The `LatencyOptimized` AutoML override strategy is only available in private beta.
Contact AWS Support or your account manager to learn more about access privileges.

Used to overide the default AutoML strategy, which is to optimize predictor accuracy.
To apply an AutoML strategy that minimizes training time, use
`LatencyOptimized`.

This parameter is only valid for predictors trained using AutoML.

Type: String

Valid Values: `LatencyOptimized | AccuracyOptimized`

Required: No

**[EncryptionConfig](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

An AWS Key Management Service (KMS) key and the AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access
the key.

Type: [EncryptionConfig](API_EncryptionConfig.md "API_EncryptionConfig.md") object

Required: No

**[EvaluationParameters](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast
evaluates a predictor by splitting a dataset into training data and testing data. The
evaluation parameters define how to perform the split and the number of iterations.

Type: [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md") object

Required: No

**[FeaturizationConfig](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

The featurization configuration.

Type: [FeaturizationConfig](API_FeaturizationConfig.md "API_FeaturizationConfig.md") object

Required: Yes

**[ForecastHorizon](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Specifies the number of time-steps that the model is trained to predict. The forecast
horizon is also called the prediction length.

For example, if you configure a dataset for daily data collection (using the
`DataFrequency` parameter of the [CreateDataset](API_CreateDataset.md "API_CreateDataset.md") operation) and
set the forecast horizon to 10, the model returns predictions for 10 days.

The maximum forecast horizon is the lesser of 500 time-steps or 1/3 of the
TARGET_TIME_SERIES dataset length.

Type: Integer

Required: Yes

**[ForecastTypes](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Specifies the forecast types used to train a predictor. You can specify up to five
forecast types. Forecast types can be quantiles from 0.01 to 0.99, by increments of 0.01 or
higher. You can also specify the mean forecast with `mean`.

The default value is `["0.10", "0.50", "0.9"]`.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Length Constraints: Minimum length of 2. Maximum length of 4.

Pattern: `(^0?\.\d\d?$|^mean$)`

Required: No

**[HPOConfig](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Provides hyperparameter override values for the algorithm. If you don't provide this
parameter, Amazon Forecast uses default values. The individual algorithms specify which
hyperparameters support hyperparameter optimization (HPO). For more information, see [Amazon Forecast Algorithms](aws-forecast-choosing-recipes.md "aws-forecast-choosing-recipes.md").

If you included the `HPOConfig` object, you must set `PerformHPO` to
true.

Type: [HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md "API_HyperParameterTuningJobConfig.md") object

Required: No

**[InputDataConfig](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Describes the dataset group that contains the data to use to train the predictor.

Type: [InputDataConfig](API_InputDataConfig.md "API_InputDataConfig.md") object

Required: Yes

**[OptimizationMetric](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

The accuracy metric used to optimize the predictor. The default value is `AverageWeightedQuantileLoss`.

Type: String

Valid Values: `WAPE | RMSE | AverageWeightedQuantileLoss | MASE | MAPE`

Required: No

**[PerformAutoML](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Whether to perform AutoML. When Amazon Forecast performs AutoML, it evaluates the algorithms it
provides and chooses the best algorithm and configuration for your training dataset.

The default value is `false`. In this case, you are required to specify an
algorithm.

Set `PerformAutoML` to `true` to have Amazon Forecast perform AutoML. This
is a good option if you aren't sure which algorithm is suitable for your training data. In
this case, `PerformHPO` must be false.

Type: Boolean

Required: No

**[PerformHPO](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

Whether to perform hyperparameter optimization (HPO). HPO finds optimal hyperparameter
values for your training data. The process of performing HPO is known as running a
hyperparameter tuning job.

The default value is `false`. In this case, Amazon Forecast uses default
hyperparameter values from the chosen algorithm.

To override the default values, set `PerformHPO` to `true` and,
optionally, supply the [HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md "API_HyperParameterTuningJobConfig.md") object. The tuning job
specifies a metric to optimize, which hyperparameters participate in tuning, and the valid
range for each tunable hyperparameter. In this case, you are required to specify an algorithm
and `PerformAutoML` must be false.

The following algorithms support HPO:

- DeepAR+
- CNN-QR

Type: Boolean

Required: No

**[PredictorName](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

A name for the predictor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**[Tags](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

The optional metadata that you apply to the predictor to help you categorize and organize
them. Each tag consists of a key and an optional value, both of which you define.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one
  value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that
  other services may have restrictions on allowed characters. Generally allowed characters
  are: letters, numbers, and spaces representable in UTF-8, and the following characters: +

* = . \_ : / @.

- Tag keys and values are case sensitive.
- Do not use `aws:`, `AWS:`, or any upper or lowercase combination
  of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag
  keys with this prefix. Values can have this prefix. If a tag value has `aws` as
  its prefix but the key does not, then Forecast considers it to be a user tag and will
  count against the limit of 50 tags. Tags with only the key prefix of `aws` do
  not count against your tags per resource limit.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[TrainingParameters](#API_CreatePredictor_RequestSyntax "#API_CreatePredictor_RequestSyntax")**

The hyperparameters to override for model training. The hyperparameters that you can
override are listed in the individual algorithms. For the list of supported algorithms, see
[Amazon Forecast Algorithms](aws-forecast-choosing-recipes.md "aws-forecast-choosing-recipes.md").

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

Key Pattern: `^[a-zA-Z0-9\-\_\.\/\[\]\,\\]+$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `^[a-zA-Z0-9\-\_\.\/\[\]\,\"\\\s]+$`

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

**[PredictorArn](#API_CreatePredictor_ResponseSyntax "#API_CreatePredictor_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/CreatePredictor.md "../../../goto/cli2/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/CreatePredictor.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForCpp/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForGoV2/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForKotlin/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/CreatePredictor.md "../../../goto/boto3/forecast-2018-06-26/CreatePredictor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CreatePredictor.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CreatePredictor.md")
