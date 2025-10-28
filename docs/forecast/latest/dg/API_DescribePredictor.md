Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# DescribePredictor

###### Note

This operation is only valid for legacy predictors created with CreatePredictor. If you
are not using a legacy predictor, use [DescribeAutoPredictor](API_DescribeAutoPredictor.md "API_DescribeAutoPredictor.md").

Describes a predictor created using the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md")
operation.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

In addition to listing the properties provided in the `CreatePredictor`
request, this operation lists the following properties:

- `DatasetImportJobArns` - The dataset import jobs used to import training
  data.
- `AutoMLAlgorithmArns` - If AutoML is performed, the algorithms that were
  evaluated.
- `CreationTime`
- `LastModificationTime`
- `Status`
- `Message` - If an error occurred, information about the error.

## Request Syntax

```
{
   "PredictorArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[PredictorArn](#API_DescribePredictor_RequestSyntax "#API_DescribePredictor_RequestSyntax")**

The Amazon Resource Name (ARN) of the predictor that you want information about.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "AlgorithmArn": "***string***",
   "AutoMLAlgorithmArns": [ "***string***" ],
   "AutoMLOverrideStrategy": "***string***",
   "CreationTime": ***number***,
   "DatasetImportJobArns": [ "***string***" ],
   "EncryptionConfig": {
      "KMSKeyArn": "***string***",
      "RoleArn": "***string***"
   },
   "EstimatedTimeRemainingInMinutes": ***number***,
   "EvaluationParameters": {
      "BackTestWindowOffset": ***number***,
      "NumberOfBacktestWindows": ***number***
   },
   "FeaturizationConfig": {
      "Featurizations": [
         {
            "AttributeName": "***string***",
            "FeaturizationPipeline": [
               {
                  "FeaturizationMethodName": "***string***",
                  "FeaturizationMethodParameters": {
                     "***string***" : "***string***"
                  }
               }
            ]
         }
      ],
      "ForecastDimensions": [ "***string***" ],
      "ForecastFrequency": "***string***"
   },
   "ForecastHorizon": ***number***,
   "ForecastTypes": [ "***string***" ],
   "HPOConfig": {
      "ParameterRanges": {
         "CategoricalParameterRanges": [
            {
               "Name": "***string***",
               "Values": [ "***string***" ]
            }
         ],
         "ContinuousParameterRanges": [
            {
               "MaxValue": ***number***,
               "MinValue": ***number***,
               "Name": "***string***",
               "ScalingType": "***string***"
            }
         ],
         "IntegerParameterRanges": [
            {
               "MaxValue": ***number***,
               "MinValue": ***number***,
               "Name": "***string***",
               "ScalingType": "***string***"
            }
         ]
      }
   },
   "InputDataConfig": {
      "DatasetGroupArn": "***string***",
      "SupplementaryFeatures": [
         {
            "Name": "***string***",
            "Value": "***string***"
         }
      ]
   },
   "IsAutoPredictor": ***boolean***,
   "LastModificationTime": ***number***,
   "Message": "***string***",
   "OptimizationMetric": "***string***",
   "PerformAutoML": ***boolean***,
   "PerformHPO": ***boolean***,
   "PredictorArn": "***string***",
   "PredictorExecutionDetails": {
      "PredictorExecutions": [
         {
            "AlgorithmArn": "***string***",
            "TestWindows": [
               {
                  "Message": "***string***",
                  "Status": "***string***",
                  "TestWindowEnd": ***number***,
                  "TestWindowStart": ***number***
               }
            ]
         }
      ]
   },
   "PredictorName": "***string***",
   "Status": "***string***",
   "TrainingParameters": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AlgorithmArn](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The Amazon Resource Name (ARN) of the algorithm used for model training.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[AutoMLAlgorithmArns](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

When `PerformAutoML` is specified, the ARN of the chosen algorithm.

Type: Array of strings

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[AutoMLOverrideStrategy](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

###### Note

The `LatencyOptimized` AutoML override strategy is only available in private beta.
Contact AWS Support or your account manager to learn more about access privileges.

The AutoML strategy used to train the predictor. Unless `LatencyOptimized`
is specified, the AutoML strategy optimizes predictor accuracy.

This parameter is only valid for predictors trained using AutoML.

Type: String

Valid Values: `LatencyOptimized | AccuracyOptimized`

**[CreationTime](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

When the model training task was created.

Type: Timestamp

**[DatasetImportJobArns](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

An array of the ARNs of the dataset import jobs used to import training data for the
predictor.

Type: Array of strings

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

**[EncryptionConfig](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

An AWS Key Management Service (KMS) key and the AWS Identity and Access Management (IAM) role that Amazon Forecast can assume to access
the key.

Type: [EncryptionConfig](API_EncryptionConfig.md "API_EncryptionConfig.md") object

**[EstimatedTimeRemainingInMinutes](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The estimated time remaining in minutes for the predictor training job to complete.

Type: Long

**[EvaluationParameters](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast
evaluates a predictor by splitting a dataset into training data and testing data. The
evaluation parameters define how to perform the split and the number of iterations.

Type: [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md") object

**[FeaturizationConfig](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The featurization configuration.

Type: [FeaturizationConfig](API_FeaturizationConfig.md "API_FeaturizationConfig.md") object

**[ForecastHorizon](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The number of time-steps of the forecast. The forecast horizon is also called the
prediction length.

Type: Integer

**[ForecastTypes](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The forecast types used during predictor training. Default value is
`["0.1","0.5","0.9"]`

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Length Constraints: Minimum length of 2. Maximum length of 4.

Pattern: `(^0?\.\d\d?$|^mean$)`

**[HPOConfig](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The hyperparameter override values for the algorithm.

Type: [HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md "API_HyperParameterTuningJobConfig.md") object

**[InputDataConfig](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

Describes the dataset group that contains the data to use to train the predictor.

Type: [InputDataConfig](API_InputDataConfig.md "API_InputDataConfig.md") object

**[IsAutoPredictor](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

Whether the predictor was created with [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md").

Type: Boolean

**[LastModificationTime](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The last time the resource was modified. The timestamp depends on the status of the
job:

- `CREATE_PENDING` - The `CreationTime`.
- `CREATE_IN_PROGRESS` - The current timestamp.
- `CREATE_STOPPING` - The current timestamp.
- `CREATE_STOPPED` - When the job stopped.
- `ACTIVE` or `CREATE_FAILED` - When the job finished or
  failed.

Type: Timestamp

**[Message](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

If an error occurred, an informational message about the error.

Type: String

**[OptimizationMetric](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The accuracy metric used to optimize the predictor.

Type: String

Valid Values: `WAPE | RMSE | AverageWeightedQuantileLoss | MASE | MAPE`

**[PerformAutoML](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

Whether the predictor is set to perform AutoML.

Type: Boolean

**[PerformHPO](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

Whether the predictor is set to perform hyperparameter optimization (HPO).

Type: Boolean

**[PredictorArn](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The ARN of the predictor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[PredictorExecutionDetails](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

Details on the the status and results of the backtests performed to evaluate the accuracy
of the predictor. You specify the number of backtests to perform when you call the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation.

Type: [PredictorExecutionDetails](API_PredictorExecutionDetails.md "API_PredictorExecutionDetails.md") object

**[PredictorName](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The name of the predictor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

**[Status](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The status of the predictor. States include:

- `ACTIVE`
- `CREATE_PENDING`, `CREATE_IN_PROGRESS`,
  `CREATE_FAILED`
- `DELETE_PENDING`, `DELETE_IN_PROGRESS`,
  `DELETE_FAILED`
- `CREATE_STOPPING`, `CREATE_STOPPED`

###### Note

The `Status` of the predictor must be `ACTIVE` before you can use
the predictor to create a forecast.

Type: String

Length Constraints: Maximum length of 256.

**[TrainingParameters](#API_DescribePredictor_ResponseSyntax "#API_DescribePredictor_ResponseSyntax")**

The default training parameters or overrides selected during model training. When running
AutoML or choosing HPO with CNN-QR or DeepAR+, the optimized values for the chosen
hyperparameters are returned. For more information, see [Amazon Forecast Algorithms](aws-forecast-choosing-recipes.md "aws-forecast-choosing-recipes.md").

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 100 items.

Key Length Constraints: Maximum length of 256.

Key Pattern: `^[a-zA-Z0-9\-\_\.\/\[\]\,\\]+$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `^[a-zA-Z0-9\-\_\.\/\[\]\,\"\\\s]+$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/DescribePredictor.md "../../../goto/cli2/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribePredictor.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForCpp/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForGoV2/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForKotlin/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/DescribePredictor.md "../../../goto/boto3/forecast-2018-06-26/DescribePredictor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribePredictor.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/DescribePredictor.md")
