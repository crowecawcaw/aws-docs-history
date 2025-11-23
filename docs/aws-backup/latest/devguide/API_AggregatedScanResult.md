# AggregatedScanResult

Contains aggregated scan results across multiple scan operations, providing a summary of scan status and findings.

## Contents

**FailedScan**

A Boolean value indicating whether any of the aggregated scans failed.

Type: Boolean

Required: No

**Findings**

An array of findings discovered across all aggregated scans.

Type: Array of strings

Valid Values: `MALWARE`

Required: No

**LastComputed**

The timestamp when the aggregated scan result was last computed, in Unix format and Coordinated Universal Time (UTC).

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/AggregatedScanResult.md "../../../goto/SdkForCpp/backup-2018-11-15/AggregatedScanResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/AggregatedScanResult.md "../../../goto/SdkForJavaV2/backup-2018-11-15/AggregatedScanResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/AggregatedScanResult.md "../../../goto/SdkForRubyV3/backup-2018-11-15/AggregatedScanResult.md")
