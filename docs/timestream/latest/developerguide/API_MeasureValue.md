For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# MeasureValue

Represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or the
RPM of a wind turbine are measures. MeasureValue has both name and value.

MeasureValue is only allowed for type `MULTI`. Using `MULTI` type, you can pass multiple
data attributes associated with the same time series in a single record

## Contents

**Name**

The name of the MeasureValue.

For constraints on MeasureValue names, see [Naming
Constraints](ts-limits.md#limits.naming "ts-limits.md#limits.naming") in the Amazon Timestream Developer Guide.

Type: String

Length Constraints: Minimum length of 1.

Required: Yes

**Type**

Contains the data type of the MeasureValue for the time-series data point.

Type: String

Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP | MULTI`

Required: Yes

**Value**

The value for the MeasureValue. For information, see [Data types](writes.md#writes.data-types "writes.md#writes.data-types").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/MeasureValue.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/MeasureValue.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/MeasureValue.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/MeasureValue.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/MeasureValue.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/MeasureValue.md")
