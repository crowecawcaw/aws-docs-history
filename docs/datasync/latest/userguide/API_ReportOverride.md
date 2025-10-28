# ReportOverride

Specifies the level of detail for a particular aspect of your DataSync
[task
report](task-reports.md "task-reports.md").

## Contents

**ReportLevel**

Specifies whether your task report includes errors only or successes and errors.

For example, your report might mostly include only what didn't go well in your transfer
(`ERRORS_ONLY`). At the same time, you want to verify that your [task filter](filtering.md "filtering.md") is
working correctly. In this situation, you can get a list of what files DataSync
successfully skipped and if something transferred that you didn't to transfer
(`SUCCESSES_AND_ERRORS`).

Type: String

Valid Values: `ERRORS_ONLY | SUCCESSES_AND_ERRORS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ReportOverride.md "../../../goto/SdkForCpp/datasync-2018-11-09/ReportOverride.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportOverride.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportOverride.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportOverride.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportOverride.md")
