On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# DataPreProcessingConfiguration

The configuration is the `TargetSamplingRate`, which is the sampling rate of
the data after post processing by Amazon Lookout for Equipment. For example, if you provide data that has been
collected at a 1 second level and you want the system to resample the data at a 1 minute
rate before training, the `TargetSamplingRate` is 1 minute.

When providing a value for the `TargetSamplingRate`, you must attach the
prefix "PT" to the rate you want. The value for a 1 second rate is therefore
_PT1S_, the value for a 15 minute rate is _PT15M_,
and the value for a 1 hour rate is _PT1H_

## Contents

**TargetSamplingRate**

The sampling rate of the data after post processing by Amazon Lookout for Equipment. For example, if you
provide data that has been collected at a 1 second level and you want the system to
resample the data at a 1 minute rate before training, the `TargetSamplingRate`
is 1 minute.

When providing a value for the `TargetSamplingRate`, you must attach the
prefix "PT" to the rate you want. The value for a 1 second rate is therefore
_PT1S_, the value for a 15 minute rate is _PT15M_,
and the value for a 1 hour rate is _PT1H_

Type: String

Valid Values: `PT1S | PT5S | PT10S | PT15S | PT30S | PT1M | PT5M | PT10M | PT15M | PT30M | PT1H`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DataPreProcessingConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/DataPreProcessingConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DataPreProcessingConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/DataPreProcessingConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DataPreProcessingConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/DataPreProcessingConfiguration.md")
