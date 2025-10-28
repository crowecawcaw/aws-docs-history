# ReportPlan

Contains detailed information about a report plan.

## Contents

**CreationTime**

The date and time that a report plan is created, in Unix format and Coordinated
Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**DeploymentStatus**

The deployment status of a report plan. The statuses are:

`CREATE_IN_PROGRESS | UPDATE_IN_PROGRESS | DELETE_IN_PROGRESS |
 COMPLETED`

Type: String

Required: No

**LastAttemptedExecutionTime**

The date and time that a report job associated with this report plan last attempted to
run, in Unix format and Coordinated Universal Time (UTC). The value of
`LastAttemptedExecutionTime` is accurate to milliseconds. For example, the
value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**LastSuccessfulExecutionTime**

The date and time that a report job associated with this report plan last successfully
ran, in Unix format and Coordinated Universal Time (UTC). The value of
`LastSuccessfulExecutionTime` is accurate to milliseconds. For example, the
value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

Type: Timestamp

Required: No

**ReportDeliveryChannel**

Contains information about where and how to deliver your reports, specifically your
Amazon S3 bucket name, S3 key prefix, and the formats of your reports.

Type: [ReportDeliveryChannel](API_ReportDeliveryChannel.md "API_ReportDeliveryChannel.md") object

Required: No

**ReportPlanArn**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Type: String

Required: No

**ReportPlanDescription**

An optional description of the report plan with a maximum 1,024 characters.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `.*\S.*`

Required: No

**ReportPlanName**

The unique name of the report plan. This name is between 1 and 256 characters starting
with a letter, and consisting of letters (a-z, A-Z), numbers (0-9), and underscores
(\_).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

Required: No

**ReportSetting**

Identifies the report template for the report. Reports are built using a report
template. The report templates are:

`RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT |
 COPY_JOB_REPORT | RESTORE_JOB_REPORT`

If the report template is `RESOURCE_COMPLIANCE_REPORT` or
`CONTROL_COMPLIANCE_REPORT`, this API resource also describes the report
coverage by AWS Regions and frameworks.

Type: [ReportSetting](API_ReportSetting.md "API_ReportSetting.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ReportPlan.md "../../../goto/SdkForCpp/backup-2018-11-15/ReportPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ReportPlan.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ReportPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ReportPlan.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ReportPlan.md")
