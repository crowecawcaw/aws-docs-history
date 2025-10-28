# DefaultIntegerHyperParameterRange

Provides the name and default range of a integer-valued hyperparameter
and whether the hyperparameter is tunable. A tunable hyperparameter can
have its value determined during hyperparameter optimization (HPO).

## Contents

**isTunable**

Indicates whether the hyperparameter is tunable.

Type: Boolean

Required: No

**maxValue**

The maximum allowable value for the hyperparameter.

Type: Integer

Valid Range: Maximum value of 1000000.

Required: No

**minValue**

The minimum allowable value for the hyperparameter.

Type: Integer

Valid Range: Minimum value of -1000000.

Required: No

**name**

The name of the hyperparameter.

Type: String

Length Constraints: Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/DefaultIntegerHyperParameterRange.md "../../../goto/SdkForCpp/personalize-2018-05-22/DefaultIntegerHyperParameterRange.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/DefaultIntegerHyperParameterRange.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/DefaultIntegerHyperParameterRange.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/DefaultIntegerHyperParameterRange.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/DefaultIntegerHyperParameterRange.md")
