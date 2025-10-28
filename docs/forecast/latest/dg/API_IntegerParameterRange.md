Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# IntegerParameterRange

Specifies an integer hyperparameter and it's range of tunable values.
This object is part of the [ParameterRanges](API_ParameterRanges.md "API_ParameterRanges.md") object.

## Contents

**MaxValue**

The maximum tunable value of the hyperparameter.

Type: Integer

Required: Yes

**MinValue**

The minimum tunable value of the hyperparameter.

Type: Integer

Required: Yes

**Name**

The name of the hyperparameter to tune.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**ScalingType**

The scale that hyperparameter tuning uses to search the hyperparameter range.
Valid values:

Auto

Amazon Forecast hyperparameter tuning chooses the best scale for the hyperparameter.

Linear

Hyperparameter tuning searches the values in the hyperparameter range by using a
linear scale.

Logarithmic

Hyperparameter tuning searches the values in the hyperparameter range by using a
logarithmic scale.

Logarithmic scaling works only for ranges that have values greater than 0.

ReverseLogarithmic

Not supported for `IntegerParameterRange`.

Reverse logarithmic scaling works only for ranges that are entirely within the
range 0 <= x < 1.0.

For information about choosing a hyperparameter scale, see
[Hyperparameter Scaling](../../../sagemaker/latest/dg/automatic-model-tuning-define-ranges.md#scaling-type "../../../sagemaker/latest/dg/automatic-model-tuning-define-ranges.md#scaling-type").
One of the following values:

Type: String

Valid Values: `Auto | Linear | Logarithmic | ReverseLogarithmic`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/IntegerParameterRange.md "../../../goto/SdkForCpp/forecast-2018-06-26/IntegerParameterRange.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/IntegerParameterRange.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/IntegerParameterRange.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/IntegerParameterRange.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/IntegerParameterRange.md")
