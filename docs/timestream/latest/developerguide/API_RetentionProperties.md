For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# RetentionProperties

Retention properties contain the duration for which your time-series data must be stored in the magnetic store
and the memory store.

## Contents

**MagneticStoreRetentionPeriodInDays**

The duration for which data must be stored in the magnetic store.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 73000.

Required: Yes

**MemoryStoreRetentionPeriodInHours**

The duration for which data must be stored in the memory store.

Type: Long

Valid Range: Minimum value of 1. Maximum value of 8766.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/RetentionProperties.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/RetentionProperties.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/RetentionProperties.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/RetentionProperties.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/RetentionProperties.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/RetentionProperties.md")
