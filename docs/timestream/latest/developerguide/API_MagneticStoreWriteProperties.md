For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# MagneticStoreWriteProperties

The set of properties on a table for configuring magnetic store writes.

## Contents

**EnableMagneticStoreWrites**

A flag to enable magnetic store writes.

Type: Boolean

Required: Yes

**MagneticStoreRejectedDataLocation**

The location to write error reports for records rejected asynchronously during magnetic store writes.

Type: [MagneticStoreRejectedDataLocation](API_MagneticStoreRejectedDataLocation.md "API_MagneticStoreRejectedDataLocation.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/MagneticStoreWriteProperties.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/MagneticStoreWriteProperties.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/MagneticStoreWriteProperties.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/MagneticStoreWriteProperties.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/MagneticStoreWriteProperties.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/MagneticStoreWriteProperties.md")
