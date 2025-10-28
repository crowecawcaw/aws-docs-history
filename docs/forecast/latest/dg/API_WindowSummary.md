Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# WindowSummary

The metrics for a time range within the evaluation portion of a dataset. This object is
part of the [EvaluationResult](API_EvaluationResult.md "API_EvaluationResult.md") object.

The `TestWindowStart` and `TestWindowEnd` parameters are determined
by the `BackTestWindowOffset` parameter of the [EvaluationParameters](API_EvaluationParameters.md "API_EvaluationParameters.md") object.

## Contents

**EvaluationType**

The type of evaluation.

- `SUMMARY` - The average metrics across all windows.
- `COMPUTED` - The metrics for the specified window.

Type: String

Valid Values: `SUMMARY | COMPUTED`

Required: No

**ItemCount**

The number of data points within the window.

Type: Integer

Required: No

**Metrics**

Provides metrics used to evaluate the performance of a predictor.

Type: [Metrics](API_Metrics.md "API_Metrics.md") object

Required: No

**TestWindowEnd**

The timestamp that defines the end of the window.

Type: Timestamp

Required: No

**TestWindowStart**

The timestamp that defines the start of the window.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/WindowSummary.md "../../../goto/SdkForCpp/forecast-2018-06-26/WindowSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/WindowSummary.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/WindowSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/WindowSummary.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/WindowSummary.md")
