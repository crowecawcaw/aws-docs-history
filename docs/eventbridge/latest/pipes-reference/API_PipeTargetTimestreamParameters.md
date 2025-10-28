# PipeTargetTimestreamParameters

The parameters for using a Timestream for LiveAnalytics table as a
target.

## Contents

**DimensionMappings**

Map source data to dimensions in the target Timestream for LiveAnalytics
table.

For more information, see [Amazon Timestream for LiveAnalytics concepts](../../../timestream/latest/developerguide/concepts.md "../../../timestream/latest/developerguide/concepts.md")

Type: Array of [DimensionMapping](API_DimensionMapping.md "API_DimensionMapping.md") objects

Array Members: Minimum number of 1 item. Maximum number of 128 items.

Required: Yes

**TimeValue**

Dynamic path to the source data field that represents the time value for your data.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**VersionValue**

64 bit version value or source data field that represents the version value for your data.

Write requests with a higher version number will update the existing measure values of the record and version.
In cases where the measure value is the same, the version will still be updated.

Default value is 1.

Timestream for LiveAnalytics does not support updating partial measure values in a record.

Write requests for duplicate data with a
higher version number will update the existing measure value and version. In cases where
the measure value is the same, `Version` will still be updated. Default value is
`1`.

###### Note

`Version` must be `1` or greater, or you will receive a
`ValidationException` error.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**EpochTimeUnit**

The granularity of the time units used. Default is `MILLISECONDS`.

Required if `TimeFieldType` is specified as `EPOCH`.

Type: String

Valid Values: `MILLISECONDS | SECONDS | MICROSECONDS | NANOSECONDS`

Required: No

**MultiMeasureMappings**

Maps multiple measures from the source event to the same record in the specified Timestream for LiveAnalytics table.

Type: Array of [MultiMeasureMapping](API_MultiMeasureMapping.md "API_MultiMeasureMapping.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1024 items.

Required: No

**SingleMeasureMappings**

Mappings of single source data fields to individual records in the specified Timestream for LiveAnalytics table.

Type: Array of [SingleMeasureMapping](API_SingleMeasureMapping.md "API_SingleMeasureMapping.md") objects

Array Members: Minimum number of 0 items. Maximum number of 8192 items.

Required: No

**TimeFieldType**

The type of time value used.

The default is `EPOCH`.

Type: String

Valid Values: `EPOCH | TIMESTAMP_FORMAT`

Required: No

**TimestampFormat**

How to format the timestamps. For example,
`yyyy-MM-dd'T'HH:mm:ss'Z'`.

Required if `TimeFieldType` is specified as
`TIMESTAMP_FORMAT`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetTimestreamParameters.md "../../../goto/SdkForCpp/pipes-2015-10-07/PipeTargetTimestreamParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetTimestreamParameters.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/PipeTargetTimestreamParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetTimestreamParameters.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/PipeTargetTimestreamParameters.md")
