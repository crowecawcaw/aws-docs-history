Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# PredictorExecution

The algorithm used to perform a backtest and the status of those tests.

## Contents

**AlgorithmArn**

The ARN of the algorithm used to test the predictor.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: No

**TestWindows**

An array of test windows used to evaluate the algorithm. The
`NumberOfBacktestWindows` from the [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md")
object determines the number of windows in the array.

Type: Array of [TestWindowSummary](API_TestWindowSummary.md "API_TestWindowSummary.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/PredictorExecution.md "../../../goto/SdkForCpp/forecast-2018-06-26/PredictorExecution.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorExecution.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorExecution.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorExecution.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorExecution.md")
