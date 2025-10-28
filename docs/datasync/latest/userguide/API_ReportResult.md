# ReportResult

Indicates whether DataSync created a complete [task report](task-reports.md "task-reports.md") for your
transfer.

## Contents

**ErrorCode**

Indicates the code associated with the error if DataSync can't create a complete
report.

Type: String

Required: No

**ErrorDetail**

Provides details about issues creating a report.

Type: String

Required: No

**Status**

Indicates whether DataSync is still working on your report, created a report, or
can't create a complete report.

Type: String

Valid Values: `PENDING | SUCCESS | ERROR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ReportResult.md "../../../goto/SdkForCpp/datasync-2018-11-09/ReportResult.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportResult.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ReportResult.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportResult.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ReportResult.md")
