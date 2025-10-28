# RestoreJobSummary

This is a summary of restore jobs created
or running within the most recent 30 days.

The returned summary may contain the following:
Region, Account, State, ResourceType, MessageCategory,
StartTime, EndTime, and Count of included jobs.

## Contents

**AccountId**

The account ID that owns the jobs within the summary.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**Count**

The value as a number of jobs in a job summary.

Type: Integer

Required: No

**EndTime**

The value of time in number format of a job end time.

This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**Region**

The AWS Regions within the job summary.

Type: String

Required: No

**ResourceType**

This value is the job count for the specified resource type.
The request `GetSupportedResourceTypes` returns
strings for supported resource types.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**StartTime**

The value of time in number format of a job start time.

This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**State**

This value is job count for jobs
with the specified state.

Type: String

Valid Values: `CREATED | PENDING | RUNNING | ABORTED | COMPLETED | FAILED | AGGREGATE_ALL | ANY`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RestoreJobSummary.md "../../../goto/SdkForCpp/backup-2018-11-15/RestoreJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreJobSummary.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RestoreJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreJobSummary.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RestoreJobSummary.md")
