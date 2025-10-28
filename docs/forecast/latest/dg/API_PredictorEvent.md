Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# PredictorEvent

Provides details about a predictor event, such as a retraining.

## Contents

**Datetime**

The timestamp for when the event occurred.

Type: Timestamp

Required: No

**Detail**

The type of event. For example, `Retrain`. A retraining event denotes the timepoint when a predictor was retrained. Any monitor results from before the `Datetime` are from the previous predictor. Any new metrics are for the newly retrained predictor.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/PredictorEvent.md "../../../goto/SdkForCpp/forecast-2018-06-26/PredictorEvent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorEvent.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/PredictorEvent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorEvent.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/PredictorEvent.md")
