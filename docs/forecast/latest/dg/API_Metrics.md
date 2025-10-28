Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Metrics

Provides metrics that are used to evaluate the performance of a predictor. This object is
part of the [WindowSummary](API_WindowSummary.md "API_WindowSummary.md") object.

## Contents

**AverageWeightedQuantileLoss**

The average value of all weighted quantile losses.

Type: Double

Required: No

**ErrorMetrics**

Provides detailed error metrics for each forecast type. Metrics include root-mean
square-error (RMSE), mean absolute percentage error (MAPE), mean absolute scaled error (MASE),
and weighted average percentage error (WAPE).

Type: Array of [ErrorMetric](API_ErrorMetric.md "API_ErrorMetric.md") objects

Required: No

**RMSE**

_This member has been deprecated._

The root-mean-square error (RMSE).

Type: Double

Required: No

**WeightedQuantileLosses**

An array of weighted quantile losses. Quantiles divide a probability distribution into
regions of equal probability. The distribution in this case is the loss function.

Type: Array of [WeightedQuantileLoss](API_WeightedQuantileLoss.md "API_WeightedQuantileLoss.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/Metrics.md "../../../goto/SdkForCpp/forecast-2018-06-26/Metrics.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/Metrics.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/Metrics.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/Metrics.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/Metrics.md")
