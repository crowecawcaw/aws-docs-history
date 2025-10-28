For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# PartitionKey

An attribute used in partitioning data in a table. A dimension key partitions data using the values of the
dimension specified by the dimension-name as partition key, while a measure key partitions data using measure names
(values of the 'measure_name' column).

## Contents

**Type**

The type of the partition key. Options are DIMENSION (dimension key) and MEASURE (measure key).

Type: String

Valid Values: `DIMENSION | MEASURE`

Required: Yes

**EnforcementInRecord**

The level of enforcement for the specification of a dimension key in ingested records. Options are REQUIRED
(dimension key must be specified) and OPTIONAL (dimension key does not have to be specified).

Type: String

Valid Values: `REQUIRED | OPTIONAL`

Required: No

**Name**

The name of the attribute used for a dimension key.

Type: String

Length Constraints: Minimum length of 1.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/PartitionKey.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/PartitionKey.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/PartitionKey.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/PartitionKey.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/PartitionKey.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/PartitionKey.md")
