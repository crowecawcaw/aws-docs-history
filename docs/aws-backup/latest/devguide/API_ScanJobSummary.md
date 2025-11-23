# ScanJobSummary

Contains summary information about scan jobs, including counts and metadata for a specific time period and criteria.

## Contents

**AccountId**

The account ID that owns the scan jobs included in this summary.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**Count**

The number of scan jobs that match the specified criteria.

Type: Integer

Required: No

**EndTime**

The value of time in number format of a job end time.

This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**MalwareScanner**

Specifies the malware scanner used during the scan job. Currently only supports `GUARDDUTY`.

Type: String

Valid Values: `GUARDDUTY`

Required: No

**Region**

The AWS Region where the scan jobs were executed.

Type: String

Required: No

**ResourceType**

The type of AWS resource for the scan jobs included in this summary.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**ScanResultStatus**

The scan result status for the scan jobs included in this summary.

Valid values: `THREATS_FOUND` | `NO_THREATS_FOUND`.

Type: String

Valid Values: `NO_THREATS_FOUND | THREATS_FOUND`

Required: No

**StartTime**

The value of time in number format of a job start time.

This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to
milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018
12:11:30.087 AM.

Type: Timestamp

Required: No

**State**

The state of the scan jobs included in this summary.

Valid values: `CREATED` | `RUNNING` | `COMPLETED` |
`COMPLETED_WITH_ISSUES` | `FAILED` | `CANCELED`.

Type: String

Valid Values: `CREATED | COMPLETED | COMPLETED_WITH_ISSUES | RUNNING | FAILED | CANCELED | AGGREGATE_ALL | ANY`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ScanJobSummary.md "../../../goto/SdkForCpp/backup-2018-11-15/ScanJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ScanJobSummary.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ScanJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ScanJobSummary.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ScanJobSummary.md")
