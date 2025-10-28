# ProfileConfiguration

Configuration for profile jobs. Configuration can be used to select columns, do evaluations, and override default
parameters of evaluations. When configuration is undefined, the profile job will apply default settings to all
supported columns.

## Contents

###### Note

In the following list, the required parameters are described first.

**ColumnStatisticsConfigurations**

List of configurations for column evaluations. ColumnStatisticsConfigurations are used to
select evaluations and override parameters of evaluations for particular columns. When
ColumnStatisticsConfigurations is undefined, the profile job will profile all supported columns
and run all supported evaluations.

Type: Array of [ColumnStatisticsConfiguration](API_ColumnStatisticsConfiguration.md "API_ColumnStatisticsConfiguration.md") objects

Array Members: Minimum number of 1 item.

Required: No

**DatasetStatisticsConfiguration**

Configuration for inter-column evaluations. Configuration can be used to select evaluations and override
parameters of evaluations. When configuration is undefined, the profile job will run all supported
inter-column evaluations.

Type: [StatisticsConfiguration](API_StatisticsConfiguration.md "API_StatisticsConfiguration.md") object

Required: No

**EntityDetectorConfiguration**

Configuration of entity detection for a profile job. When undefined, entity detection is disabled.

Type: [EntityDetectorConfiguration](API_EntityDetectorConfiguration.md "API_EntityDetectorConfiguration.md") object

Required: No

**ProfileColumns**

List of column selectors. ProfileColumns can be used to select columns from the dataset. When
ProfileColumns is undefined, the profile job will profile all supported columns.

Type: Array of [ColumnSelector](API_ColumnSelector.md "API_ColumnSelector.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ProfileConfiguration.md "../../../goto/SdkForCpp/databrew-2017-07-25/ProfileConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ProfileConfiguration.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ProfileConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ProfileConfiguration.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ProfileConfiguration.md")
