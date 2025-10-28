# HPOConfig

Describes the properties for hyperparameter optimization (HPO).

## Contents

**algorithmHyperParameterRanges**

The hyperparameters and their allowable ranges.

Type: [HyperParameterRanges](API_HyperParameterRanges.md "API_HyperParameterRanges.md") object

Required: No

**hpoObjective**

The metric to optimize during HPO.

###### Note

Amazon Personalize doesn't support configuring the `hpoObjective`
at this time.

Type: [HPOObjective](API_HPOObjective.md "API_HPOObjective.md") object

Required: No

**hpoResourceConfig**

Describes the resource configuration for HPO.

Type: [HPOResourceConfig](API_HPOResourceConfig.md "API_HPOResourceConfig.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-2018-05-22/HPOConfig.md "../../../goto/SdkForCpp/personalize-2018-05-22/HPOConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-2018-05-22/HPOConfig.md "../../../goto/SdkForJavaV2/personalize-2018-05-22/HPOConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-2018-05-22/HPOConfig.md "../../../goto/SdkForRubyV3/personalize-2018-05-22/HPOConfig.md")
