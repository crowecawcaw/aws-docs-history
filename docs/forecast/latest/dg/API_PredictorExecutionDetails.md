Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# PredictorExecutionDetails

Contains details on the backtests performed to evaluate the accuracy of the predictor. The
tests are returned in descending order of accuracy, with the most accurate backtest appearing
first. You specify the number of backtests to perform when you call the [CreatePredictor](API_CreatePredictor.md "API_CreatePredictor.md") operation.

## Contents

**PredictorExecutions**

An array of the backtests performed to evaluate the accuracy of the predictor against a
particular algorithm. The `NumberOfBacktestWindows` from the [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md") object determines the number of windows in the
array.

Type: Array of [PredictorExecution](API_PredictorExecution.md "API_PredictorExecution.md") objects

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/PredictorExecutionDetails.md "../../../goto/SdkForCpp/forecast-2018-06-26/PredictorExecutionDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorExecutionDetails.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorExecutionDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorExecutionDetails.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorExecutionDetails.md")
