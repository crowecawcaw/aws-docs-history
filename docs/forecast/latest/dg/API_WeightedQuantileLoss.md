Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# WeightedQuantileLoss

The weighted loss value for a quantile. This object is part of the [Metrics](API_Metrics.md "API_Metrics.md") object.

## Contents

**LossValue**

The difference between the predicted value and the actual value over the quantile,
weighted (normalized) by dividing by the sum over all quantiles.

Type: Double

Required: No

**Quantile**

The quantile. Quantiles divide a probability distribution into regions of equal
probability. For example, if the distribution was divided into 5 regions of equal probability,
the quantiles would be 0.2, 0.4, 0.6, and 0.8.

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/WeightedQuantileLoss.md "../../../goto/SdkForCpp/forecast-2018-06-26/WeightedQuantileLoss.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/WeightedQuantileLoss.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/WeightedQuantileLoss.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/WeightedQuantileLoss.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/WeightedQuantileLoss.md")
