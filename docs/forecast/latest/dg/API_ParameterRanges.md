Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# ParameterRanges

Specifies the categorical, continuous, and integer hyperparameters, and their ranges of
tunable values. The range of tunable values determines which values that a hyperparameter
tuning job can choose for the specified hyperparameter. This object is part of the
[HyperParameterTuningJobConfig](API_HyperParameterTuningJobConfig.md "API_HyperParameterTuningJobConfig.md") object.

## Contents

**CategoricalParameterRanges**

Specifies the tunable range for each categorical hyperparameter.

Type: Array of [CategoricalParameterRange](API_CategoricalParameterRange.md "API_CategoricalParameterRange.md") objects

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Required: No

**ContinuousParameterRanges**

Specifies the tunable range for each continuous hyperparameter.

Type: Array of [ContinuousParameterRange](API_ContinuousParameterRange.md "API_ContinuousParameterRange.md") objects

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Required: No

**IntegerParameterRanges**

Specifies the tunable range for each integer hyperparameter.

Type: Array of [IntegerParameterRange](API_IntegerParameterRange.md "API_IntegerParameterRange.md") objects

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/ParameterRanges.md "../../../goto/SdkForCpp/forecast-2018-06-26/ParameterRanges.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/ParameterRanges.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/ParameterRanges.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/ParameterRanges.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/ParameterRanges.md")
