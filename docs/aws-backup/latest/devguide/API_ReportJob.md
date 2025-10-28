# ReportJob

Contains detailed information about a report job. A report job compiles a report based
on a report plan and publishes it to Amazon S3.

## Contents

**CompletionTime**

The date and time that a report job is completed, in Unix format and Coordinated
Universal Time (UTC). The value of `CompletionTime` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**CreationTime**

The date and time that a report job is created, in Unix format and Coordinated Universal
Time (UTC). The value of `CreationTime` is accurate to milliseconds. For
example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**ReportDestination**

The S3 bucket name and S3 keys for the destination where the report job publishes the
report.

Type: [ReportDestination](API_ReportDestination.md "API_ReportDestination.md") object

Required: No

**ReportJobId**

The identifier for a report job. A unique, randomly generated, Unicode, UTF-8 encoded
string that is at most 1,024 bytes long. Report job IDs cannot be edited.

Type: String

Required: No

**ReportPlanArn**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Type: String

Required: No

**ReportTemplate**

Identifies the report template for the report. Reports are built using a report
template. The report templates are:

`RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT |
 COPY_JOB_REPORT | RESTORE_JOB_REPORT`

Type: String

Required: No

**Status**

The status of a report job. The statuses are:

`CREATED | RUNNING | COMPLETED | FAILED`

`COMPLETED` means that the report is available for your review at your
designated destination. If the status is `FAILED`, review the
`StatusMessage` for the reason.

Type: String

Required: No

**StatusMessage**

A message explaining the status of the report job.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ReportJob.md "../../../goto/SdkForCpp/backup-2018-11-15/ReportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ReportJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ReportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ReportJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ReportJob.md")
