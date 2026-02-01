Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# GetAccuracyMetrics

Provides metrics on the accuracy of the models that were trained by the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation. Use metrics to see how well the model performed and
to decide whether to use the predictor to generate a forecast. For more information, see
[Predictor
Metrics](metrics.md "metrics.md").

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

This operation generates metrics for each backtest window that was evaluated. The number
of backtest windows (`NumberOfBacktestWindows`) is specified using the [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md") object, which is optionally included in the
`CreatePredictor` request. If `NumberOfBacktestWindows` isn't
specified, the number defaults to one.

The parameters of the `filling` method determine which items contribute to the
metrics. If you want all items to contribute, specify `zero`. If you want only
those items that have complete data in the range being evaluated to contribute, specify
`nan`. For more information, see [FeaturizationMethod](API_FeaturizationMethod.md "API_FeaturizationMethod.md").

###### Note

Before you can get accuracy metrics, the `Status` of the predictor must be
`ACTIVE`, signifying that training has completed. To get the status, use the
[DescribePredictor](API_DescribePredictor.md "API_DescribePredictor.md") operation.

## Request Syntax

```
{
   "PredictorArn": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[PredictorArn](#API_GetAccuracyMetrics_RequestSyntax "#API_GetAccuracyMetrics_RequestSyntax")**

The Amazon Resource Name (ARN) of the predictor to get metrics for.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

## Response Syntax

```
{
   "AutoMLOverrideStrategy": "***string***",
   "IsAutoPredictor": ***boolean***,
   "OptimizationMetric": "***string***",
   "PredictorEvaluationResults": [
      {
         "AlgorithmArn": "***string***",
         "TestWindows": [
            {
               "EvaluationType": "***string***",
               "ItemCount": ***number***,
               "Metrics": {
                  "AverageWeightedQuantileLoss": ***number***,
                  "ErrorMetrics": [
                     {
                        "ForecastType": "***string***",
                        "MAPE": ***number***,
                        "MASE": ***number***,
                        "RMSE": ***number***,
                        "WAPE": ***number***
                     }
                  ],
                  "RMSE": ***number***,
                  "WeightedQuantileLosses": [
                     {
                        "LossValue": ***number***,
                        "Quantile": ***number***
                     }
                  ]
               },
               "TestWindowEnd": ***number***,
               "TestWindowStart": ***number***
            }
         ]
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AutoMLOverrideStrategy](#API_GetAccuracyMetrics_ResponseSyntax "#API_GetAccuracyMetrics_ResponseSyntax")**

###### Note

The `LatencyOptimized` AutoML override strategy is only available in private beta.
Contact AWS Support or your account manager to learn more about access privileges.

The AutoML strategy used to train the predictor. Unless `LatencyOptimized`
is specified, the AutoML strategy optimizes predictor accuracy.

This parameter is only valid for predictors trained using AutoML.

Type: String

Valid Values: `LatencyOptimized | AccuracyOptimized`

**[IsAutoPredictor](#API_GetAccuracyMetrics_ResponseSyntax "#API_GetAccuracyMetrics_ResponseSyntax")**

Whether the predictor was created with [CreateAutoPredictor](API_CreateAutoPredictor.md "API_CreateAutoPredictor.md").

Type: Boolean

**[OptimizationMetric](#API_GetAccuracyMetrics_ResponseSyntax "#API_GetAccuracyMetrics_ResponseSyntax")**

The accuracy metric used to optimize the predictor.

Type: String

Valid Values: `WAPE | RMSE | AverageWeightedQuantileLoss | MASE | MAPE`

**[PredictorEvaluationResults](#API_GetAccuracyMetrics_ResponseSyntax "#API_GetAccuracyMetrics_ResponseSyntax")**

An array of results from evaluating the predictor.

Type: Array of [EvaluationResult](API_EvaluationResult.md "API_EvaluationResult.md") objects

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

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

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/cli2/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/DotNetSDKV4/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForCpp/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForGoV2/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForKotlin/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/boto3/forecast-2018-06-26/GetAccuracyMetrics.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/GetAccuracyMetrics.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/GetAccuracyMetrics.md")
