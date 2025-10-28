For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Dimension

Represents the metadata attributes of the time series. For example, the name and Availability Zone of an EC2
instance or the name of the manufacturer of a wind turbine are dimensions.

## Contents

**Name**

Dimension represents the metadata attributes of the time series. For example, the name and Availability Zone of
an EC2 instance or the name of the manufacturer of a wind turbine are dimensions.

For constraints on dimension names, see [Naming Constraints](ts-limits.md#limits.naming "ts-limits.md#limits.naming").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 60.

Required: Yes

**Value**

The value of the dimension.

Type: String

Required: Yes

**DimensionValueType**

The data type of the dimension for the time-series data point.

Type: String

Valid Values: `VARCHAR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/Dimension.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/Dimension.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Dimension.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Dimension.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Dimension.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Dimension.md")
