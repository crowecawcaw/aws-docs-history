Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# EvaluationResult

The results of evaluating an algorithm. Returned as part of the [GetAccuracyMetrics](API_GetAccuracyMetrics.md "API_GetAccuracyMetrics.md") response.

## Contents

**AlgorithmArn**

The Amazon Resource Name (ARN) of the algorithm that was evaluated.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**TestWindows**

The array of test windows used for evaluating the algorithm. The
`NumberOfBacktestWindows` from the [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md") object
determines the number of windows in the array.

Type: Array of [WindowSummary](API_WindowSummary.md "API_WindowSummary.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/EvaluationResult.md "../../../goto/SdkForCpp/forecast-2018-06-26/EvaluationResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/EvaluationResult.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/EvaluationResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/EvaluationResult.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/EvaluationResult.md")
