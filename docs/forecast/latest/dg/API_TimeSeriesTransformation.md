Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# TimeSeriesTransformation

A transformation function is a pair of operations that select and modify the rows in a related time series. You select the rows that you want with a condition operation and you modify the rows with a transformation operation. All conditions are joined with an AND operation, meaning that all conditions must be true for the transformation to be applied. Transformations are applied in the order that they are listed.

## Contents

**Action**

An array of actions that define a time series and how it is transformed. These transformations create a new
time series that is used for the what-if analysis.

Type: [Action](API_Action.md "API_Action.md") object

Required: No

**TimeSeriesConditions**

An array of conditions that define which members of the related time series are transformed.

Type: Array of [TimeSeriesCondition](API_TimeSeriesCondition.md "API_TimeSeriesCondition.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/TimeSeriesTransformation.md "../../../goto/SdkForCpp/forecast-2018-06-26/TimeSeriesTransformation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/TimeSeriesTransformation.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/TimeSeriesTransformation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/TimeSeriesTransformation.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/TimeSeriesTransformation.md")
