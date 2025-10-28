For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ExecutionStats

Statistics for a single scheduled query run.

## Contents

**BytesMetered**

Bytes metered for a single scheduled query run.

Type: Long

Required: No

**CumulativeBytesScanned**

Bytes scanned for a single scheduled query run.

Type: Long

Required: No

**DataWrites**

Data writes metered for records ingested in a single scheduled query run.

Type: Long

Required: No

**ExecutionTimeInMillis**

Total time, measured in milliseconds, that was needed for the scheduled query run to
complete.

Type: Long

Required: No

**QueryResultRows**

Number of rows present in the output from running a query before ingestion to
destination data source.

Type: Long

Required: No

**RecordsIngested**

The number of records ingested for a single scheduled query run.

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ExecutionStats.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ExecutionStats.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ExecutionStats.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ExecutionStats.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ExecutionStats.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ExecutionStats.md")
