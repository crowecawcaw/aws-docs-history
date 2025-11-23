# ReportSetting

Contains detailed information about a report setting.

## Contents

**ReportTemplate**

Identifies the report template for the report. Reports are built using a report
template. The report templates are:

`RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT |
 COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT`

Type: String

Required: Yes

**Accounts**

These are the accounts to be included in the report.

Use string value of `ROOT` to include all organizational units.

Type: Array of strings

Required: No

**FrameworkArns**

The Amazon Resource Names (ARNs) of the frameworks a report covers.

Type: Array of strings

Required: No

**NumberOfFrameworks**

The number of frameworks a report covers.

Type: Integer

Required: No

**OrganizationUnits**

These are the Organizational Units to be included in the report.

Type: Array of strings

Required: No

**Regions**

These are the Regions to be included in the report.

Use the wildcard as the string value to include all Regions.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ReportSetting.md "../../../goto/SdkForCpp/backup-2018-11-15/ReportSetting.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ReportSetting.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ReportSetting.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ReportSetting.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ReportSetting.md")
