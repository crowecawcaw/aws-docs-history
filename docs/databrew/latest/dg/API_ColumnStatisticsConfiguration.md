# ColumnStatisticsConfiguration

Configuration for column evaluations for a profile job. ColumnStatisticsConfiguration can be used to select
evaluations and override parameters of evaluations for particular columns.

## Contents

###### Note

In the following list, the required parameters are described first.

**Statistics**

Configuration for evaluations. Statistics can be used to select evaluations and override
parameters of evaluations.

Type: [StatisticsConfiguration](API_StatisticsConfiguration.md "API_StatisticsConfiguration.md") object

Required: Yes

**Selectors**

List of column selectors. Selectors can be used to select columns from the dataset.
When selectors are undefined, configuration will be applied to all supported columns.

Type: Array of [ColumnSelector](API_ColumnSelector.md "API_ColumnSelector.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ColumnStatisticsConfiguration.md "../../../goto/SdkForCpp/databrew-2017-07-25/ColumnStatisticsConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ColumnStatisticsConfiguration.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ColumnStatisticsConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ColumnStatisticsConfiguration.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ColumnStatisticsConfiguration.md")
