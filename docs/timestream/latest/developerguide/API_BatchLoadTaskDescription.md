For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# BatchLoadTaskDescription

Details about a batch load task.

## Contents

**CreationTime**

The time when the Timestream batch load task was created.

Type: Timestamp

Required: No

**DataModelConfiguration**

Data model configuration for a batch load task. This contains details about where a data model for a batch load
task is stored.

Type: [DataModelConfiguration](API_DataModelConfiguration.md "API_DataModelConfiguration.md") object

Required: No

**DataSourceConfiguration**

Configuration details about the data source for a batch load task.

Type: [DataSourceConfiguration](API_DataSourceConfiguration.md "API_DataSourceConfiguration.md") object

Required: No

**ErrorMessage**

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**LastUpdatedTime**

The time when the Timestream batch load task was last updated.

Type: Timestamp

Required: No

**ProgressReport**

Type: [BatchLoadProgressReport](API_BatchLoadProgressReport.md "API_BatchLoadProgressReport.md") object

Required: No

**RecordVersion**

Type: Long

Required: No

**ReportConfiguration**

Report configuration for a batch load task. This contains details about where error reports are stored.

Type: [ReportConfiguration](API_ReportConfiguration.md "API_ReportConfiguration.md") object

Required: No

**ResumableUntil**

Type: Timestamp

Required: No

**TargetDatabaseName**

Type: String

Required: No

**TargetTableName**

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

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/BatchLoadTaskDescription.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/BatchLoadTaskDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/BatchLoadTaskDescription.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/BatchLoadTaskDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/BatchLoadTaskDescription.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/BatchLoadTaskDescription.md")
