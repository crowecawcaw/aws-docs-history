# StatisticsConfiguration

Configuration of evaluations for a profile job. This configuration can be used to select
evaluations and override the parameters of selected evaluations.

## Contents

###### Note

In the following list, the required parameters are described first.

**IncludedStatistics**

List of included evaluations. When the list is undefined, all supported
evaluations will be included.

Type: Array of strings

Array Members: Minimum number of 1 item.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^[A-Z\_]+$`

Required: No

**Overrides**

List of overrides for evaluations.

Type: Array of [StatisticOverride](API_StatisticOverride.md "API_StatisticOverride.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/StatisticsConfiguration.md "../../../goto/SdkForCpp/databrew-2017-07-25/StatisticsConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/StatisticsConfiguration.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/StatisticsConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/StatisticsConfiguration.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/StatisticsConfiguration.md")
