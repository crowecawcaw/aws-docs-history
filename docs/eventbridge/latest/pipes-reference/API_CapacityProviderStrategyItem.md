

# CapacityProviderStrategyItem
<a name="API_CapacityProviderStrategyItem"></a>

The details of a capacity provider strategy. To learn more, see [CapacityProviderStrategyItem](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CapacityProviderStrategyItem.html) in the Amazon ECS API Reference.

## Contents
<a name="API_CapacityProviderStrategyItem_Contents"></a>

 ** capacityProvider **   <a name="eventbridge-Type-CapacityProviderStrategyItem-capacityProvider"></a>
The short name of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

 ** base **   <a name="eventbridge-Type-CapacityProviderStrategyItem-base"></a>
The base value designates how many tasks, at a minimum, to run on the specified capacity provider. Only one capacity provider in a capacity provider strategy can have a base defined. If no value is specified, the default value of 0 is used.   
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100000.  
Required: No

 ** weight **   <a name="eventbridge-Type-CapacityProviderStrategyItem-weight"></a>
The weight value designates the relative percentage of the total number of tasks launched that should use the specified capacity provider. The weight value is taken into consideration after the base value, if defined, is satisfied.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000.  
Required: No

## See Also
<a name="API_CapacityProviderStrategyItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pipes-2015-10-07/CapacityProviderStrategyItem) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pipes-2015-10-07/CapacityProviderStrategyItem) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pipes-2015-10-07/CapacityProviderStrategyItem) 