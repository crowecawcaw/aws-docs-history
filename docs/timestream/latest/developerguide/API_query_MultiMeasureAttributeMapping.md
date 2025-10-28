For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# MultiMeasureAttributeMapping

Attribute mapping for MULTI value measures.

## Contents

**MeasureValueType**

Type of the attribute to be read from the source column.

Type: String

Valid Values: `BIGINT | BOOLEAN | DOUBLE | VARCHAR | TIMESTAMP`

Required: Yes

**SourceColumn**

Source column from where the attribute value is to be read.

Type: String

Required: Yes

**TargetMultiMeasureAttributeName**

Custom name to be used for attribute name in derived table. If not provided, source
column name would be used.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/MultiMeasureAttributeMapping.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/MultiMeasureAttributeMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/MultiMeasureAttributeMapping.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/MultiMeasureAttributeMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/MultiMeasureAttributeMapping.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/MultiMeasureAttributeMapping.md")
