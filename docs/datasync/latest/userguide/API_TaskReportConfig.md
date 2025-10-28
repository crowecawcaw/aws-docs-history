# TaskReportConfig

Specifies how you want to configure a task report, which provides detailed information
about for your AWS DataSync transfer.

For more information, see [Task reports](task-reports.md "task-reports.md").

## Contents

**Destination**

Specifies the Amazon S3 bucket where DataSync uploads your task report.
For more information, see [Task
reports](task-reports.md#task-report-access "task-reports.md#task-report-access").

Type: [ReportDestination](API_ReportDestination.md "API_ReportDestination.md") object

Required: No

**ObjectVersionIds**

Specifies whether your task report includes the new version of each object transferred
into an S3 bucket. This only applies if you [enable versioning on your
bucket](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md"). Keep in mind that setting this to `INCLUDE` can increase the
duration of your task execution.

Type: String

Valid Values: `INCLUDE | NONE`

Required: No

**OutputType**

Specifies the type of task report that you want:

- `SUMMARY_ONLY`: Provides necessary details about your task, including the
  number of files, objects, and directories transferred and transfer duration.
- `STANDARD`: Provides complete details about your task, including a full
  list of files, objects, and directories that were transferred, skipped, verified, and
  more.

Type: String

Valid Values: `SUMMARY_ONLY | STANDARD`

Required: No

**Overrides**

Customizes the reporting level for aspects of your task report. For example, your report
might generally only include errors, but you could specify that you want a list of successes
and errors just for the files that DataSync attempted to delete in your destination
location.

Type: [ReportOverrides](API_ReportOverrides.md "API_ReportOverrides.md") object

Required: No

**ReportLevel**

Specifies whether you want your task report to include only what went wrong with your
transfer or a list of what succeeded and didn't.

- `ERRORS_ONLY`: A report shows what DataSync was unable to
  transfer, skip, verify, and delete.
- `SUCCESSES_AND_ERRORS`: A report shows what DataSync was able and
  unable to transfer, skip, verify, and delete.

Type: String

Valid Values: `ERRORS_ONLY | SUCCESSES_AND_ERRORS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskReportConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskReportConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskReportConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskReportConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskReportConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskReportConfig.md")
