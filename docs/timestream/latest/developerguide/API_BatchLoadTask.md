For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# BatchLoadTask

Details about a batch load task.

## Contents

**CreationTime**

The time when the Timestream batch load task was created.

Type: Timestamp

Required: No

**DatabaseName**

Database name for the database into which a batch load task loads data.

Type: String

Required: No

**LastUpdatedTime**

The time when the Timestream batch load task was last updated.

Type: Timestamp

Required: No

**ResumableUntil**

Type: Timestamp

Required: No

**TableName**

Table name for the table into which a batch load task loads data.

Type: String

Required: No

**TaskId**

The ID of the batch load task.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 32.

Pattern: `[A-Z0-9]+`

Required: No

**TaskStatus**

Status of the batch load task.

Type: String

Valid Values: `CREATED | IN_PROGRESS | FAILED | SUCCEEDED | PROGRESS_STOPPED | PENDING_RESUME`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/BatchLoadTask.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/BatchLoadTask.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/BatchLoadTask.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/BatchLoadTask.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/BatchLoadTask.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/BatchLoadTask.md")
