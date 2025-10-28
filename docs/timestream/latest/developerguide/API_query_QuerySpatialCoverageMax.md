For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QuerySpatialCoverageMax

Provides insights into the table with the most sub-optimal spatial range scanned by your query.

## Contents

**PartitionKey**

The partition key used for partitioning, which can be a default `measure_name` or a [customer defined partition key](customer-defined-partition-keys.md "customer-defined-partition-keys.md").

Type: Array of strings

Required: No

**TableArn**

The Amazon Resource Name (ARN) of the table with the most sub-optimal spatial pruning.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**Value**

The maximum ratio of spatial coverage.

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QuerySpatialCoverageMax.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QuerySpatialCoverageMax.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QuerySpatialCoverageMax.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QuerySpatialCoverageMax.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QuerySpatialCoverageMax.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QuerySpatialCoverageMax.md")
