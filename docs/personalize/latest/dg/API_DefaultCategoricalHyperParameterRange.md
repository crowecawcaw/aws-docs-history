# DefaultCategoricalHyperParameterRange

Provides the name and default range of a categorical hyperparameter
and whether the hyperparameter is tunable. A tunable hyperparameter can
have its value determined during hyperparameter optimization (HPO).

## Contents

**isTunable**

Whether the hyperparameter is tunable.

Type: Boolean

Required: No

**name**

The name of the hyperparameter.

Type: String

Length Constraints: Maximum length of 256.

Required: No

**values**

A list of the categories for the hyperparameter.

Type: Array of strings

Array Members: Maximum number of 100 items.

Length Constraints: Maximum length of 1000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DefaultCategoricalHyperParameterRange.md "../../../goto/SdkForCpp/personalize-2018-05-22/DefaultCategoricalHyperParameterRange.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DefaultCategoricalHyperParameterRange.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DefaultCategoricalHyperParameterRange.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DefaultCategoricalHyperParameterRange.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DefaultCategoricalHyperParameterRange.md")
