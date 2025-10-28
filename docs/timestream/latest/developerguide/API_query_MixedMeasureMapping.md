For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# MixedMeasureMapping

MixedMeasureMappings are mappings that can be used to ingest data into a mixture of
narrow and multi measures in the derived table.

## Contents

**MeasureValueType**

Type of the value that is to be read from sourceColumn. If the mapping is for MULTI,
use MeasureValueType.MULTI.

Type: String

Valid Values: `BIGINT | BOOLEAN | DOUBLE | VARCHAR | MULTI`

Required: Yes

**MeasureName**

Refers to the value of measure_name in a result row. This field is required if
MeasureNameColumn is provided.

Type: String

Required: No

**MultiMeasureAttributeMappings**

Required when measureValueType is MULTI. Attribute mappings for MULTI value
measures.

Type: Array of [MultiMeasureAttributeMapping](API_query_MultiMeasureAttributeMapping.md "API_query_MultiMeasureAttributeMapping.md") objects

Array Members: Minimum number of 1 item.

Required: No

**SourceColumn**

This field refers to the source column from which measure-value is to be read for
result materialization.

Type: String

Required: No

**TargetMeasureName**

Target measure name to be used. If not provided, the target measure name by default
would be measure-name if provided, or sourceColumn otherwise.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/MixedMeasureMapping.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/MixedMeasureMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/MixedMeasureMapping.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/MixedMeasureMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/MixedMeasureMapping.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/MixedMeasureMapping.md")
