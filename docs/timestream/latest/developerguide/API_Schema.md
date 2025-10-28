For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Schema

A Schema specifies the expected data model of the table.

## Contents

**CompositePartitionKey**

A non-empty list of partition keys defining the attributes used to partition the table data. The order of the
list determines the partition hierarchy. The name and type of each partition key as well as the partition key order
cannot be changed after the table is created. However, the enforcement level of each partition key can be changed.

Type: Array of [PartitionKey](API_PartitionKey.md "API_PartitionKey.md") objects

Array Members: Minimum number of 1 item.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/Schema.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/Schema.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Schema.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Schema.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Schema.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Schema.md")
