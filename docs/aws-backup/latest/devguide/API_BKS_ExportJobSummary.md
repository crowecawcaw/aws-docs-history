# ExportJobSummary

This is the summary of an export job.

## Contents

**ExportJobIdentifier**

This is the unique string that identifies a
specific export job.

Type: String

Required: Yes

**CompletionTime**

This is a timestamp of the time the export job
compeleted.

Type: Timestamp

Required: No

**CreationTime**

This is a timestamp of the time the export job
was created.

Type: Timestamp

Required: No

**ExportJobArn**

This is the unique ARN (Amazon Resource Name) that
belongs to the new export job.

Type: String

Required: No

**SearchJobArn**

The unique string that identifies the Amazon Resource
Name (ARN) of the specified search job.

Type: String

Required: No

**Status**

The status of the export job is one of the
following:

`CREATED`; `RUNNING`;
`FAILED`; or `COMPLETED`.

Type: String

Valid Values: `RUNNING | FAILED | COMPLETED`

Required: No

**StatusMessage**

A status message is a string that is returned for an export
job.

A status message is included for any status other
than `COMPLETED` without issues.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/ExportJobSummary.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/ExportJobSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/ExportJobSummary.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/ExportJobSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/ExportJobSummary.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/ExportJobSummary.md")
