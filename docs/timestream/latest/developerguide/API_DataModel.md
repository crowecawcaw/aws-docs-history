For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DataModel

Data model for a batch load task.

## Contents

**DimensionMappings**

Source to target mappings for dimensions.

Type: Array of [DimensionMapping](API_DimensionMapping.md "API_DimensionMapping.md") objects

Array Members: Minimum number of 1 item.

Required: Yes

**MeasureNameColumn**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**MixedMeasureMappings**

Source to target mappings for measures.

Type: Array of [MixedMeasureMapping](API_MixedMeasureMapping.md "API_MixedMeasureMapping.md") objects

Array Members: Minimum number of 1 item.

Required: No

**MultiMeasureMappings**

Source to target mappings for multi-measure records.

Type: [MultiMeasureMappings](API_MultiMeasureMappings.md "API_MultiMeasureMappings.md") object

Required: No

**TimeColumn**

Source column to be mapped to time.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**TimeUnit**

The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds,
or other supported values. Default is `MILLISECONDS`.

Type: String

Valid Values: `MILLISECONDS | SECONDS | MICROSECONDS | NANOSECONDS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/DataModel.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/DataModel.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DataModel.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/DataModel.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DataModel.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/DataModel.md")
