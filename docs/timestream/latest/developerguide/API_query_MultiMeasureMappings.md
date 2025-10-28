For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# MultiMeasureMappings

Only one of MixedMeasureMappings or MultiMeasureMappings is to be provided.
MultiMeasureMappings can be used to ingest data as multi measures in the derived
table.

## Contents

**MultiMeasureAttributeMappings**

Required. Attribute mappings to be used for mapping query results to ingest data for
multi-measure attributes.

Type: Array of [MultiMeasureAttributeMapping](API_query_MultiMeasureAttributeMapping.md "API_query_MultiMeasureAttributeMapping.md") objects

Array Members: Minimum number of 1 item.

Required: Yes

**TargetMultiMeasureName**

The name of the target multi-measure name in the derived table. This input is required
when measureNameColumn is not provided. If MeasureNameColumn is provided, then value
from that column will be used as multi-measure name.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/MultiMeasureMappings.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/MultiMeasureMappings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/MultiMeasureMappings.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/MultiMeasureMappings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/MultiMeasureMappings.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/MultiMeasureMappings.md")
