Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ErrorMetric

Provides detailed error metrics to evaluate the performance of a predictor. This object
is part of the [Metrics](API_Metrics.md "API_Metrics.md") object.

## Contents

**ForecastType**

The Forecast type used to compute WAPE, MAPE, MASE, and RMSE.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 4.

Pattern: `(^0?\.\d\d?$|^mean$)`

Required: No

**MAPE**

The Mean Absolute Percentage Error (MAPE)

Type: Double

Required: No

**MASE**

The Mean Absolute Scaled Error (MASE)

Type: Double

Required: No

**RMSE**

The root-mean-square error (RMSE).

Type: Double

Required: No

**WAPE**

The weighted absolute percentage error (WAPE).

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ErrorMetric.md "../../../goto/SdkForCpp/forecast-2018-06-26/ErrorMetric.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ErrorMetric.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ErrorMetric.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ErrorMetric.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ErrorMetric.md")
