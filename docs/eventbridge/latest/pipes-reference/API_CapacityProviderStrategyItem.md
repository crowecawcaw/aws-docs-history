# CapacityProviderStrategyItem

The details of a capacity provider strategy. To learn more, see [CapacityProviderStrategyItem](../../../AmazonECS/latest/APIReference/API_CapacityProviderStrategyItem.md "../../../AmazonECS/latest/APIReference/API_CapacityProviderStrategyItem.md") in the Amazon ECS API Reference.

## Contents

**capacityProvider**

The short name of the capacity provider.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**base**

The base value designates how many tasks, at a minimum, to run on the specified capacity
provider. Only one capacity provider in a capacity provider strategy can have a base
defined. If no value is specified, the default value of 0 is used.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100000.

Required: No

**weight**

The weight value designates the relative percentage of the total number of tasks
launched that should use the specified capacity provider. The weight value is taken into
consideration after the base value, if defined, is satisfied.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 1000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/CapacityProviderStrategyItem.md "../../../goto/SdkForCpp/pipes-2015-10-07/CapacityProviderStrategyItem.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/CapacityProviderStrategyItem.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/CapacityProviderStrategyItem.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/CapacityProviderStrategyItem.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/CapacityProviderStrategyItem.md")
