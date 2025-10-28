For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# RejectedRecord

Represents records that were not successfully inserted into Timestream due to data validation issues
that must be resolved before reinserting time-series data into the system.

## Contents

**ExistingVersion**

The existing version of the record. This value is populated in scenarios where an identical record exists with a
higher version than the version in the write request.

Type: Long

Required: No

**Reason**

The reason why a record was not successfully inserted into Timestream. Possible causes of failure
include:

- Records with duplicate data where there are multiple records with the same dimensions, timestamps, and measure
  names but:

      + Measure values are different
      + Version is not present in the request, *or* the value of version in the new record is
       equal to or lower than the existing value

  If Timestream rejects data for this case, the `ExistingVersion` field in the
  `RejectedRecords` response will indicate the current record’s version. To force an update, you can
  resend the request with a version for the record set to a value greater than the
  `ExistingVersion`.

- Records with timestamps that lie outside the retention duration of the memory store.

###### Note

When the retention window is updated, you will receive a `RejectedRecords` exception if you
immediately try to ingest data within the new window. To avoid a `RejectedRecords` exception, wait
until the duration of the new window to ingest new data. For further information, see [Best Practices for Configuring Timestream](best-practices.md#configuration "best-practices.md#configuration") and [the
explanation of how storage works in Timestream](storage.md "storage.md").

- Records with dimensions or measures that exceed the Timestream defined limits.

For more information, see [Access Management](ts-limits.md "ts-limits.md") in the Timestream Developer Guide.

Type: String

Required: No

**RecordIndex**

The index of the record in the input request for WriteRecords. Indexes begin with 0.

Type: Integer

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/RejectedRecord.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/RejectedRecord.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/RejectedRecord.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/RejectedRecord.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/RejectedRecord.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/RejectedRecord.md")
