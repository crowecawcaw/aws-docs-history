# ScanAction

Defines a scanning action that specifies the malware scanner and scan mode to use.

## Contents

**MalwareScanner**

The malware scanner to use for the scan action. Currently only `GUARDDUTY` is supported.

Type: String

Valid Values: `GUARDDUTY`

Required: No

**ScanMode**

The scanning mode to use for the scan action.

Valid values: `FULL_SCAN` | `INCREMENTAL_SCAN`.

Type: String

Valid Values: `FULL_SCAN | INCREMENTAL_SCAN`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ScanAction.md "../../../goto/SdkForCpp/backup-2018-11-15/ScanAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ScanAction.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ScanAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ScanAction.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ScanAction.md")
