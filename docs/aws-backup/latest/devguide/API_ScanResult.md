# ScanResult

Contains the results of a security scan, including scanner information, scan state, and any findings discovered.

## Contents

**Findings**

An array of findings discovered during the scan.

Type: Array of strings

Valid Values: `MALWARE`

Required: No

**LastScanTimestamp**

The timestamp of when the last scan was performed, in Unix format and Coordinated Universal Time (UTC).

Type: Timestamp

Required: No

**MalwareScanner**

The malware scanner used to perform the scan. Currently only `GUARDDUTY` is supported.

Type: String

Valid Values: `GUARDDUTY`

Required: No

**ScanJobState**

The final state of the scan job.

Valid values: `COMPLETED` | `FAILED` | `CANCELED`.

Type: String

Valid Values: `COMPLETED | COMPLETED_WITH_ISSUES | FAILED | CANCELED`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ScanResult.md "../../../goto/SdkForCpp/backup-2018-11-15/ScanResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ScanResult.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ScanResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ScanResult.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ScanResult.md")
