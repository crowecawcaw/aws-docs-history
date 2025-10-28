Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# CategoricalParameterRange

Specifies a categorical hyperparameter and it's range of tunable values.
This object is part of the [ParameterRanges](API_ParameterRanges.md "API_ParameterRanges.md") object.

## Contents

**Name**

The name of the categorical hyperparameter to tune.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 63.

Pattern: `^[a-zA-Z][a-zA-Z0-9_]*`

Required: Yes

**Values**

A list of the tunable categories for the hyperparameter.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 20 items.

Length Constraints: Maximum length of 256.

Pattern: `^[a-zA-Z0-9\_\-]+$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/CategoricalParameterRange.md "../../../goto/SdkForCpp/forecast-2018-06-26/CategoricalParameterRange.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/CategoricalParameterRange.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/CategoricalParameterRange.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/CategoricalParameterRange.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/CategoricalParameterRange.md")
