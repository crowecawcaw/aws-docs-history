For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Record

Represents a time-series data point being written into Timestream. Each record contains an array of
dimensions. Dimensions represent the metadata attributes of a time-series data point, such as the instance name or
Availability Zone of an EC2 instance. A record also contains the measure name, which is the name of the measure being
collected (for example, the CPU utilization of an EC2 instance). Additionally, a record contains the measure value
and the value type, which is the data type of the measure value. Also, the record contains the timestamp of when the
measure was collected and the timestamp unit, which represents the granularity of the timestamp.

Records have a `Version` field, which is a 64-bit `long` that you can use for updating
data points. Writes of a duplicate record with the same dimension, timestamp, and measure name but different measure
value will only succeed if the `Version` attribute of the record in the write request is higher than that
of the existing record. Timestream defaults to a `Version` of `1` for records without
the `Version` field.

## Contents

**Dimensions**

Contains the list of dimensions for time-series data points.

Type: Array of [Dimension](API_Dimension.md "API_Dimension.md") objects

Array Members: Maximum number of 128 items.

Required: No

**MeasureName**

Measure represents the data attribute of the time series. For example, the CPU utilization of an EC2 instance or
the RPM of a wind turbine are measures.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**MeasureValue**

Contains the measure value for the time-series data point.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**MeasureValues**

Contains the list of MeasureValue for time-series data points.

This is only allowed for type `MULTI`. For scalar values, use `MeasureValue` attribute of
the record directly.

Type: Array of [MeasureValue](API_MeasureValue.md "API_MeasureValue.md") objects

Required: No

**MeasureValueType**

Contains the data type of the measure value for the time-series data point. Default type is
`DOUBLE`. For more information, see [Data types](writes.md#writes.data-types "writes.md#writes.data-types").

Type: String

Valid Values: `DOUBLE | BIGINT | VARCHAR | BOOLEAN | TIMESTAMP | MULTI`

Required: No

**Time**

Contains the time at which the measure value for the data point was collected. The time value plus the unit
provides the time elapsed since the epoch. For example, if the time value is `12345` and the unit is
`ms`, then `12345 ms` have elapsed since the epoch.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**TimeUnit**

The granularity of the timestamp unit. It indicates if the time value is in seconds, milliseconds, nanoseconds,
or other supported values. Default is `MILLISECONDS`.

Type: String

Valid Values: `MILLISECONDS | SECONDS | MICROSECONDS | NANOSECONDS`

Required: No

**Version**

64-bit attribute used for record updates. Write requests for duplicate data with a higher version number will
update the existing measure value and version. In cases where the measure value is the same, `Version`
will still be updated. Default value is `1`.

###### Note

`Version` must be `1` or greater, or you will receive a `ValidationException`
error.

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/Record.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/Record.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Record.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Record.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Record.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Record.md")
